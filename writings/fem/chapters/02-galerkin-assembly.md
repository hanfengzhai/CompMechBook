# Galerkin's Method and Global Assembly

[IV.1](01-weighted-residuals.md) posed the operational question Part III deferred: given a weak form, how do we approximate the solution on a mesh? Weighted residuals answered with a family of methods; Galerkin chose test functions from the same space as trials — the orthogonal projection of the true solution onto \(V_h\) in the energy inner product Part II named. This chapter is where that projection becomes **code**: loop over elements, form local contributions, scatter into global sparse structure.

Weighted residuals gave us the logic: enforce \(\int r\, w_i = 0\) for chosen weights. Galerkin chose \(w_i = \phi_i\). The finite element method chooses the \(\phi_i\) to be local, piecewise-polynomial **shape functions** on a mesh. What remains is the algorithm that every FEM code shares — from a twenty-line Matlab script for a homework bar problem to Abaqus assembling a million-element turbine disk.

That algorithm is **global assembly**: loop over elements, compute local contributions, scatter into a global sparse matrix. It is structured linear algebra — the change-of-basis story from Part I, executed millions of times with a sparsity pattern dictated by mesh connectivity.

## Story so far (Parts I–III & IV.1)

| Stage | What the wire became | Key object |
|-------|----------------------|------------|
| Part I | \(\mathbf{K}\mathbf{u}=\mathbf{f}\); scatter maps \(\mathbf{L}_e\) | Finite-dimensional equilibrium |
| Part II–III | Weak form \(a(u,v)=\ell(v)\); energy minimum on \(V_h\) | Continuum target for refinement |
| [IV.1](01-weighted-residuals.md) | Galerkin: test = trial | Orthogonal projection in energy norm |
| **IV.2 (here)** | Global \(\mathbf{K}\), \(\mathbf{F}\) from element loops | Assembly as structured linear algebra |

The [prologue](../../prologue/00-many-scales.md) promised that **Act III — Pulling** would turn grip displacement into numbers on the load cell. Assembly is the backstage step that makes that act honest — each scatter into \(\mathbf{K}\) is the finite-dimensional echo of the energy inner product Part II defined and Part III minimized.

## Scene: the mesh becomes a matrix

Return to the copper wire in the tensile frame. Part I reduced it to a chain of springs; Part III wrote equilibrium as a weak form in \(H^1\); now a graduate student opens a FEM script and imports the same geometry as a one-dimensional mesh — twenty quadratic line elements along the axis, a refined cluster near the grip where stress will peak.

The script loops over elements. On each segment it evaluates shape functions \(N_I(\xi)\) at Gauss points, forms the local stiffness \(\mathbf{k}_e = \int B^T D B \, d\xi\), and **scatters** entries into global indices. When the loop finishes, the screen shows a sparse banded matrix and a load vector — the same symbols as Part I, now built from integrals of the weak form rather than hand-written spring constants.

The operator clicks **Solve**. The displacement curve overlays the experimental trace from Part I: linear at first, then diverging as plasticity (still absent from this elastic model) would take over. Nothing mystical happened. Galerkin assembly is the proof that Part III's weak form and Part I's \(\mathbf{K}\mathbf{u}=\mathbf{f}\) are the same story at two resolutions — continuous field and finite-dimensional projection. The rest of this chapter makes that loop explicit enough to code.

## The Galerkin system

Let \(V_h = \text{span}\{\phi_1, \ldots, \phi_N\} \subset V\). Seek

\[
u_h = \sum_{j=1}^{N} U_j \phi_j
\]

such that

\[
a(u_h, \phi_i) = \ell(\phi_i), \qquad i = 1,\ldots,N.
\]

Substituting the expansion and using bilinearity of \(a(\cdot,\cdot)\):

\[
\sum_{j=1}^{N} U_j\, a(\phi_j, \phi_i) = \ell(\phi_i).
\]

Define the **global stiffness matrix** and **load vector**:

\[
K_{ij} = a(\phi_j, \phi_i), \qquad F_i = \ell(\phi_i).
\]

The discrete problem is \(\mathbf{K}\mathbf{U} = \mathbf{F}\). For Poisson's equation with \(a(u,v) = \int \nabla u\cdot\nabla v\) and \(\ell(v) = \int f v\), \(\mathbf{K}\) is symmetric and positive semi-definite; essential boundary conditions render it positive definite.

Part I taught us to think of \(\mathbf{K}\) as a linear map. Part III taught us that \(\mathbf{K}\) is the Riesz representation of the bilinear form restricted to \(V_h\). Assembly is how we compute its entries without ever forming full trial or test functions on the whole domain.

## Element-level contributions

Partition \(\Omega\) into elements \(\Omega_e\), \(e = 1,\ldots, N_e\). Shape functions are defined **locally** on each element: on element \(e\), restrict to \(n_e\) nodes with shape functions \(N_a(\xi)\), \(a = 1,\ldots,n_e\), where \(\xi\) are reference coordinates.

The **local stiffness matrix** is

\[
k_{ab}^e = \int_{\Omega_e} \nabla N_a \cdot \nabla N_b \, d\Omega.
\]

The **local load vector** is

\[
f_a^e = \int_{\Omega_e} f N_a \, d\Omega.
\]

Integrals over physical element \(\Omega_e\) are evaluated on a **reference element** \(\hat{\Omega}\) via the isoparametric map \(\mathbf{x}(\xi)\) and Jacobian \(\mathbf{J} = \partial \mathbf{x}/\partial \xi\):

\[
\int_{\Omega_e} g(\mathbf{x})\, d\Omega = \int_{\hat{\Omega}} g(\mathbf{x}(\xi))\, |\det \mathbf{J}|\, d\xi.
\]

**Quadrature** approximates the reference integral by a weighted sum of function values at quadrature points — the subject of Chapter 3.

## The assembly scatter operation

Let \(\mathbf{L}_e\) be the **local-to-global scatter matrix**: a rectangular matrix mapping local DOF indices on element \(e\) to global indices. Then the global system satisfies

\[
\mathbf{K} = \sum_{e=1}^{N_e} \mathbf{L}_e^T \mathbf{k}^e \mathbf{L}_e, \qquad \mathbf{F} = \sum_{e=1}^{N_e} \mathbf{L}_e^T \mathbf{f}^e.
\]

In practice, \(\mathbf{L}_e\) is never stored as a dense matrix. Instead, each element carries a **connectivity array** listing global node indices, and assembly loops over local pairs \((a,b)\), adding \(k_{ab}^e\) to \(K_{i_a i_b}\) where \(i_a, i_b\) are the global indices of local nodes \(a, b\).

Sparsity follows from locality: \(K_{ij} \neq 0\) only if nodes \(i\) and \(j\) share at least one element. The **mesh graph** — nodes as vertices, edges between nodes sharing an element — determines the sparsity pattern. Precomputing this pattern before filling entries is standard in production codes.

## Worked example: 1D linear bar element

Consider a uniform copper wire segment discretized with two linear elements on \([0, L]\), nodes at \(x_0 = 0\), \(x_1 = L/2\), \(x_2 = L\). On a single element \([x_1, x_2]\) of length \(h\), map \(\xi \in [0,1]\) via \(x = x_1 + h\xi\).

Linear shape functions:

\[
N_1(\xi) = 1 - \xi, \qquad N_2(\xi) = \xi.
\]

Derivatives: \(dN_1/dx = -1/h\), \(dN_2/dx = 1/h\). With constant \(EA\),

\[
k_{ab}^e = \int_{x_1}^{x_2} EA \frac{dN_a}{dx}\frac{dN_b}{dx}\, dx = \frac{EA}{h} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Assembling two identical elements in series gives a global \(3 \times 3\) stiffness:

\[
\mathbf{K} = \frac{EA}{h}\begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}.
\]

This is tridiagonal — the discrete Laplacian structure from Part I's eigenvalue chapter, now arising from a physical stiffness. Imposing \(U_0 = 0\) (fixed end) and solving \(\mathbf{K}\mathbf{U} = \mathbf{F}\) with a point load at the free end reproduces the linear displacement profile \(u(x) = Fx/(EA)\) exactly, because the exact solution is piecewise linear and lies in \(V_h\). This is the **patch test** in action.

## 2D Poisson with P1 triangles

Move to a 2D domain — say, the cross-section of the copper wire under steady Joule heating, modeled as \(-\Delta T = q/J\) with \(T\) the temperature field. Triangulate the cross-section; each triangle has three vertices with barycentric coordinates \((\lambda_1, \lambda_2, \lambda_3)\), \(\lambda_1 + \lambda_2 + \lambda_3 = 1\).

P1 shape functions are the barycentric coordinates themselves: \(N_a = \lambda_a\). Gradients are **constant** on each triangle:

\[
\nabla N_a = \frac{1}{2A} \begin{bmatrix} y_b - y_c \\ x_c - x_b \end{bmatrix},
\]

where \(A\) is the triangle area and \((a,b,c)\) is a cyclic permutation of vertices. The local stiffness becomes

\[
k_{ab}^e = A\, (\nabla N_a \cdot \nabla N_b),
\]

computable in closed form without quadrature for this element.

Global assembly scatters each \(3 \times 3\) local matrix into the global system. Row \(i\) of \(\mathbf{K}\) has nonzeros only in columns corresponding to nodes connected to node \(i\) by an edge — the **stencil** of the 2D discrete Laplacian. Problem Session 6 in the FEA teaching notes walks this calculation explicitly for a small triangular mesh.

## Vector problems and block structure

For linear elasticity, each node carries \(d\) displacement components in \(d\) dimensions. The trial function for node \(a\), component \(i\) is \(\mathbf{N}_{a,i} = N_a \mathbf{e}_i\). The global stiffness has **block structure**: coupling between node \(a\) component \(i\) and node \(b\) component \(j\) arises from

\[
K_{(a,i)(b,j)} = \int_{\Omega_e} \mathbb{C}_{ikjl}\, \partial_k N_a\, \partial_l N_b\, d\Omega
\]

(summation over repeated indices). For isotropic materials and uniform meshes, blocks decouple when the problem has symmetries, but general 3D meshes produce fully populated \(3 \times 3\) blocks per node pair.

The **DOF map** assigns a global index to each (node, component) pair. Boundary conditions on individual components — roller supports, symmetry planes — modify rows and columns of \(\mathbf{K}\) accordingly.

## Data structures in production codes

A minimal FEM implementation stores:

| Structure | Contents | Purpose |
|-----------|----------|---------|
| Mesh | Node coordinates, element connectivity, boundary markers | Geometry and topology |
| DOF map | (node, component) \(\to\) global index | Vector problems, constraints |
| Sparsity pattern | List of (row, col) pairs with nonzero entries | Preallocate \(\mathbf{K}\) |
| Quadrature tables | Points \(\xi_q\), weights \(w_q\) on reference elements | Numerical integration |
| Material arrays | \(E\), \(\nu\), \(\rho\), etc. per element or quadrature point | Constitutive evaluation |

High-level frameworks — **FEniCS**, **Firedrake**, **deal.II** — accept UFL/Symbolic weak forms and generate assembly loops automatically. The FEA notes include FEniCS and Firedrake tutorials for 2D Poisson; understanding the generated loop remains essential for debugging wrong boundary conditions, incorrect Jacobians, and locking in nearly incompressible materials.

## Assembly for time-dependent and nonlinear problems

For parabolic problems \(u_t - \Delta u = f\), backward Euler gives

\[
\frac{1}{\Delta t}\mathbf{M}(\mathbf{U}^{n+1} - \mathbf{U}^n) + \mathbf{K}\mathbf{U}^{n+1} = \mathbf{F}^{n+1},
\]

where \(\mathbf{M}\) is the **mass matrix** \(M_{ij} = \int \phi_i \phi_j\, d\Omega\), assembled with the same scatter pattern as \(\mathbf{K}\). The system \((\mathbf{M}/\Delta t + \mathbf{K})\mathbf{U}^{n+1} = \mathbf{M}\mathbf{U}^n/\Delta t + \mathbf{F}^{n+1}\) is solved each time step.

For nonlinear problems, assembly runs inside Newton iterations. The **tangent stiffness** \(\mathbf{K}_T = \partial \mathbf{R}/\partial \mathbf{U}\) is assembled from derivatives of the weak form with respect to nodal values — conceptually the same loop, with a different integrand.

## Connection to Part I and Part III

Assembly is where the abstract meets the concrete:

- Part I's sparse matrix is filled entry by entry from element integrals.
- Part III's bilinear form \(a(\cdot,\cdot)\) becomes the sum of local forms \(a_e(\cdot,\cdot)\).
- Part II's best approximation property holds because \(\mathbf{K}\) is the Gram matrix of the energy inner product on \(V_h\).

The copper wire's displacement field, once meshed, is a vector \(\mathbf{U} \in \mathbb{R}^N\). Assembly is the map from continuum physics to that vector equation.

## Bridge

Global assembly is the map from continuum physics to \(\mathbf{K}\mathbf{U}=\mathbf{F}\) — but the integrals inside each element depend on **shape functions**, **reference-to-physical maps**, and **quadrature rules**. The accuracy, cost, and robustness of the method — whether P1 triangles suffice or Q2 elements are needed, whether reduced integration causes hourglassing — are determined in the next chapter.

| What IV.2 assembled | What IV.3 must specify |
|-----------------------|------------------------|
| Local \(\mathbf{K}^e\), \(\mathbf{f}^e\) from weak form | Shape functions \(\phi_i\) on reference elements |
| Scatter/gather into global sparsity pattern | Isoparametric Jacobian \(J\) and \(\det J\) in integrals |
| DOF map for vector problems on the wire | Quadrature points/weights that integrate polynomials exactly |
| Mass matrix for transient heat on the wire | Locking, hourglassing, and patch-test failures |

Recall the pipeline from [Part III.4](../part03-pdes/04-energy-methods.md#bridge-to-part-iv): weak form → energy minimum → Rayleigh–Ritz on \(V_h\). Assembly is the operational half of Rayleigh–Ritz; element technology is the other half. The copper wire's tensile mesh is only as trustworthy as the P1 bar elements (1D), triangles (2D cross-section), or tets (3D grip region) that define \(V_h\).

Return to the [prologue](../../prologue/00-many-scales.md): **Act III — Pulling** is where grip displacement becomes numbers on the load cell. Assembly is the backstage step that makes that act honest — each `scatter` into \(\mathbf{K}\) and \(\mathbf{f}\) is the finite-dimensional echo of the energy inner product Part II defined and Part III minimized. Part I taught the pattern as \(\mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\); here the same map runs on millions of elements. When the linear elastic climb on the force–displacement trace disagrees with experiment, check assembly before blaming constitutive physics — a transposed connectivity array or wrong DOF map corrupts the story before dislocations or yield enter.

| Prologue act | Assembly artifact on the wire | Upstream chapter that defined it |
|--------------|-------------------------------|----------------------------------|
| I — Mounting | Global DOF map and BC rows | Part I scatter maps; Part III Dirichlet tags |
| II — Warming | Thermal \(\mathbf{K}_T\), \(\mathbf{f}_q\) from Joule source | Part III.4 energy minimum on \(V_h\) |
| III — Pulling | Mechanical \(\mathbf{K}\), \(\mathbf{f}\) from end displacement | Part IV.1 Galerkin orthogonality |
| VI — Foundation (preview) | Mass matrix \(\mathbf{M}\) for dynamics | Part I eigenmodes; Part II spectral theory |

| Assembly step | Part I vocabulary | Part III weak form | What IV.3 specifies |
|---------------|-------------------|--------------------|---------------------|
| Local \(\mathbf{k}_e\) | Element stiffness | \(\int a(\phi_i,\phi_j)\) | Shape functions \(\phi_i\), quadrature |
| Scatter into \(\mathbf{K}\) | \(\mathbf{L}_e^T\mathbf{k}_e\mathbf{L}_e\) | Global bilinear form | DOF map, sparsity pattern |
| Load vector \(\mathbf{f}\) | Nodal forces | \(\ell(\phi_i)\) | Consistent vs. lumped loads |

Turn the page when assembly feels like bookkeeping but the stress contour still jumps between meshes — the fault is usually element order or quadrature, not the scatter loop.

| Prologue act | Assembly output | Next chapter's element question |
|--------------|-----------------|--------------------------------|
| II — Warming | Thermal \(\mathbf{K}_T\), \(\mathbf{f}_q\) | P1 triangles vs. quadrature on \(\int k\|\nabla T\|^2\) |
| III — Pulling | Mechanical \(\mathbf{K}\), \(\mathbf{f}\) | Block \(\mathbf{B}^T\mathbb{C}\mathbf{B}\) at Gauss points |
| IV — Hardening (preview) | Same mesh, evolving \(\mathbb{C}\) | Anisotropic texture from cold-drawn wire |
