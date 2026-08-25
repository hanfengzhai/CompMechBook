# Linear Maps, Bases, and Change of Coordinates

A matrix is not merely a table of numbers. It is a **linear map** expressed in a particular basis. Change the basis and the matrix changes; the map itself does not. This distinction — coordinate representation versus intrinsic object — runs through every scale of computational mechanics.

When we mesh the copper wire for a tensile test, each bar element has a **local** coordinate system aligned with the element axis. The global displacement vector lives in a **global** basis tied to node numbering. Assembly is the book-keeping that says: "this local degree of freedom is global degree of freedom 17." That book-keeping is a linear map.

## Scene: two languages for the same grip load

The tensile frame displays grip displacement in millimeters; the finite element deck stores it as degree of freedom 1. The bar element on the wire axis has its own local axis; the global stiffness matrix sees a completely different numbering. Same physics, three coordinate systems. Assembly is the map that declares them equivalent — and if that map is wrong, the wire appears to stretch when only one end moves.

## Linear maps and their matrix representations

A map \(T: \mathbb{R}^n \to \mathbb{R}^m\) is linear if

\[
T(\alpha \mathbf{x} + \beta \mathbf{y}) = \alpha T(\mathbf{x}) + \beta T(\mathbf{y}).
\]

Every such map can be written as \(T(\mathbf{x}) = \mathbf{A}\mathbf{x}\) for some \(\mathbf{A} \in \mathbb{R}^{m \times n}\). Examples in mechanics:

- **Gradient operator** (discretized): nodal values \(\mapsto\) strains at quadrature points.
- **Assembly operator**: element vectors \(\mapsto\) global vector.
- **Constitutive map** (linearized): strains \(\mapsto\) stresses.
- **Isoparametric map**: reference element coordinates \(\mapsto\) physical coordinates.

The composition of linear maps is linear. A finite element strain–displacement operator is built by composing: shape function gradients (reference to physical) with the symmetric gradient operator.

## Bases and coordinates

A **basis** \(\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}\) lets us write \(\mathbf{x} = \sum_j x_j \mathbf{e}_j\). The coordinates \(x_j\) depend on the basis; the vector \(\mathbf{x}\) does not.

If \(\mathbf{B}\) is the matrix whose columns are new basis vectors expressed in the old basis, then coordinates transform as

\[
\mathbf{x}_{\text{old}} = \mathbf{B}\,\mathbf{x}_{\text{new}}, \qquad
\mathbf{A}_{\text{new}} = \mathbf{B}^{-1}\mathbf{A}_{\text{old}}\mathbf{B}.
\]

In finite elements, we change coordinates constantly: from reference element to physical element, from local degrees of freedom to global ones. Assembly is a structured change of basis.

### Orthonormal bases and the QR factorization

An **orthonormal basis** satisfies \(\mathbf{q}_i \cdot \mathbf{q}_j = \delta_{ij}\). The matrix \(\mathbf{Q}\) with orthonormal columns is orthogonal: \(\mathbf{Q}^T\mathbf{Q} = \mathbf{I}\). The QR factorization \(\mathbf{A} = \mathbf{Q}\mathbf{R}\) expresses any full-rank map as rotation/reflection followed by triangular scaling.

QR appears in least-squares fitting of material data, in constraint projection for contact algorithms, and in building orthonormal modal bases from raw eigenvectors. When \(\mathbf{Q}\) is orthogonal, changing coordinates does not distort lengths — a numerical convenience as well as a geometric one.

## The stiffness matrix in local and global frames

Consider a single bar element with local stiffness \(\mathbf{k}_e \in \mathbb{R}^{2\times 2}\). An assembly matrix \(\mathbf{L}_e\) maps local DOFs to global DOFs:

\[
\mathbf{K} = \sum_e \mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e.
\]

Each \(\mathbf{L}_e\) is a sparse "scatter" operator — a change of coordinates. The global stiffness is the sum of the same physical stiffness expressed in different local frames and planted into a shared global basis.

For a 2D truss member at angle \(\theta\) to the horizontal, the local axial stiffness \(\mathbf{k}_{\text{local}}\) transforms to global coordinates via a rotation \(\mathbf{R}(\theta)\):

\[
\mathbf{k}_{\text{global}} = \mathbf{R}^T \mathbf{k}_{\text{local}} \mathbf{R}.
\]

The copper wire pulled along its axis uses only axial bars (\(\theta = 0\)); a bent specimen or a cable net requires this rotation at every element — same physics, different matrix in the global basis.

## Worked example: two-element assembly

Two bar elements connect nodes 1–2 and 2–3 with the same \(k = EA/L\). The local element stiffness is

\[
\mathbf{k} = k\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Element 1 maps local DOFs \((u_1, u_2)\) to global indices; element 2 maps \((u_2, u_3)\). Write the scatter maps explicitly:

\[
\mathbf{L}_1 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}, \qquad
\mathbf{L}_2 = \begin{bmatrix} 0 & 0 \\ 1 & 0 \\ 0 & 1 \end{bmatrix},
\]

each a \(3 \times 2\) matrix that embeds local DOFs into global indices \((1,2)\) and \((2,3)\). Then assembly is the formula from above:

\[
\mathbf{K} = \mathbf{L}_1^T \mathbf{k} \mathbf{L}_1 + \mathbf{L}_2^T \mathbf{k} \mathbf{L}_2
= k\begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}.
\]

The middle row reflects that node 2 feels stiffness from both elements — superposition in the global basis. Each \(\mathbf{L}_e\) has exactly two ones per column (one per local DOF); multiplying \(\mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\) **plants** the \(2 \times 2\) element block into the global positions without ever forming a dense global matrix in a production code — the scatter loop in Part IV is this multiply, repeated for millions of elements.

| Operation | Matrix form | What a FEM code does |
|-----------|-------------|----------------------|
| Gather | \(\mathbf{u}_e = \mathbf{L}_e^T \mathbf{u}\) | Read nodal values for element nodes |
| Local multiply | \(\mathbf{f}_e = \mathbf{k}_e \mathbf{u}_e\) | Element stiffness times local displacement |
| Scatter | \(\mathbf{f} \mathrel{+}= \mathbf{L}_e \mathbf{f}_e\) | Add element forces into global residual |

The transpose pattern is not accidental: gathering local DOFs uses \(\mathbf{L}_e^T\); scattering element forces uses \(\mathbf{L}_e\). Virtual work \(\mathbf{u}^T \mathbf{f}\) is invariant under this change of coordinates — the discrete shadow of the adjoint relationship developed in Part II. This \(3 \times 3\) pattern is the one-dimensional prototype of the sparse assembly loops in Part IV.

## Lab act: rotation when the wire is not aligned with the global axis

Real fixtures rarely align every element with the global \(x\)-axis. Suppose a short copper segment is modeled as a 2D truss bar of length \(L = 0.5\,\text{m}\), cross-section \(A = 1\,\text{mm}^2\), \(E = 120\,\text{GPa}\), oriented at \(\theta = 30^\circ\) to the horizontal. The **local** axial stiffness (DOFs along the bar) is

\[
\mathbf{k}_{\text{local}} = \frac{EA}{L}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \approx 2.4 \times 10^8 \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}\,\text{N/m}.
\]

Each node carries two global DOFs \((u_x, u_y)\). The rotation matrix that maps local axial displacement to global components is

\[
\mathbf{R} = \begin{bmatrix} \cos\theta & 0 \\ \sin\theta & 0 \\ 0 & \cos\theta \\ 0 & \sin\theta \end{bmatrix}
\quad\text{(4 rows: node 1 then node 2)},
\]

so the **global** element stiffness is \(\mathbf{k}_{\text{global}} = \mathbf{R}^T \mathbf{k}_{\text{local}} \mathbf{R}\) — a \(4 \times 4\) block coupling \(u_x\) and \(u_y\) at both ends. For \(\theta = 30^\circ\), \(\cos^2\theta = 3/4\) and \(\sin^2\theta = 1/4\), so an axial load along the bar produces both horizontal and vertical global reactions even though the local problem is one-dimensional.

| Check | Local frame | Global frame |
|-------|-------------|--------------|
| Load along bar axis | Single DOF pair \((u_1, u_2)\) | Coupled \((u_{x1}, u_{y1}, u_{x2}, u_{y2})\) |
| Stiffness pattern | Tridiagonal \(2 \times 2\) | Dense \(4 \times 4\) block with off-diagonal \(u_x\)–\(u_y\) terms |
| Physical meaning | Stretch along bar | Same stretch, different matrix entries |

This is the same change-of-basis formula \(\mathbf{A}_{\text{new}} = \mathbf{B}^{-1}\mathbf{A}_{\text{old}}\mathbf{B}\) with \(\mathbf{B} = \mathbf{R}\): the map (axial stiffness) is intrinsic; the matrix is not. Part IV's isoparametric Jacobian performs the same job in 3D on curved elements — reference coordinates to physical coordinates, every quadrature point. If you verify one rotated bar by hand, you have verified the idea behind every `B`-matrix in a structural code.

## Projections and idempotent maps

A linear map \(\mathbf{P}\) is a **projection** if \(\mathbf{P}^2 = \mathbf{P}\). An **orthogonal projection** onto a subspace spanned by columns of \(\mathbf{Q}\) is \(\mathbf{P} = \mathbf{Q}\mathbf{Q}^T\).

Galerkin approximation can be viewed as projecting the infinite-dimensional solution onto a finite trial subspace. If \(\mathbf{u}_h = \mathbf{Q}\mathbf{a}\) with columns of \(\mathbf{Q}\) representing basis functions sampled at nodes, the discrete equations are the projected residual. The trial space is the subspace onto which we project; the test space (in standard Galerkin) is the same — a choice revisited in Part III and Part IV.

## Symmetry and positive definiteness

For linear elasticity in small strain, the stiffness matrix is **symmetric**:

\[
\mathbf{K} = \mathbf{K}^T.
\]

This reflects the symmetry of the bilinear form

\[
a(\mathbf{u}, \mathbf{v}) = \mathbf{v}^T \mathbf{K}\mathbf{u}.
\]

If the body is properly constrained and the material is stable, \(\mathbf{K}\) is **positive definite**:

\[
\mathbf{u}^T \mathbf{K}\mathbf{u} > 0 \quad \text{for all } \mathbf{u} \neq \mathbf{0}.
\]

Positive definiteness guarantees a unique equilibrium and makes conjugate gradient solvers effective. In Part II, the same property appears as **coercivity** of an elliptic operator; in Part III, coercivity is what the Lax–Milgram theorem demands.

| Property | Matrix level | Continuum level (Part III) |
|----------|--------------|----------------------------|
| Symmetry | \(\mathbf{K} = \mathbf{K}^T\) | \(a(u,v) = a(v,u)\) |
| Positive definite | \(\mathbf{u}^T\mathbf{K}\mathbf{u} > 0\) | Coercivity: \(a(u,u) \ge \alpha \|u\|^2\) |
| Invertible (after BCs) | Unique \(\mathbf{u}\) for each \(\mathbf{f}\) | Unique weak solution |

## Rank, null space, and constraints

The **null space** of \(\mathbf{K}\) consists of rigid-body modes — displacements that produce no strain. An unconstrained copper wire in 3D has six rigid modes: three translations and three rotations. Unconstrained bodies have nontrivial null spaces; boundary conditions remove them.

The **rank** of \(\mathbf{K}\) counts independent rows/columns after constraints. A singular system means either a mechanism (null space) or redundant constraints (inconsistent rows).

Lagrange multiplier methods (used heavily in contact and in mixed finite elements) augment the system:

\[
\begin{bmatrix} \mathbf{K} & \mathbf{C}^T \\ \mathbf{C} & \mathbf{0} \end{bmatrix}
\begin{bmatrix} \mathbf{u} \\ \boldsymbol{\lambda} \end{bmatrix}
=
\begin{bmatrix} \mathbf{f} \\ \mathbf{g} \end{bmatrix}.
\]

The constraint matrix \(\mathbf{C}\) encodes the geometry of admissible motion. Understanding null spaces at the matrix level prevents singular systems at the code level.

## The singular value decomposition as universal change of coordinates

Any matrix \(\mathbf{A} \in \mathbb{R}^{m \times n}\) admits an SVD \(\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^T\). The columns of \(\mathbf{V}\) are input directions; columns of \(\mathbf{U}\) are output directions; \(\sigma_i\) scales along each pair.

Mechanically, SVD identifies **principal response directions**: which displacement patterns produce the largest forces, and which load patterns excite the largest displacements. Reduced-order models for the copper wire might retain only the first few singular modes — a low-rank approximation of a high-dimensional map. The SVD also quantifies **rank deficiency**: near-zero \(\sigma_i\) signal mechanisms or ill-conditioning.

## Sparse storage: the scatter map in computer memory

The assembly formula \(\mathbf{K} = \sum_e \mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\) is a mathematical sum of rank-one (or low-rank) updates planted at sparse index pairs. A production FEM code never forms the dense \(N \times N\) matrix — it stores only the **nonzero entries** and the **row/column indices** that tell the solver where each stiffness contribution lives.

The **compressed sparse row (CSR)** format is the standard encoding:

| Array | Length | Meaning |
|-------|--------|---------|
| `values` | nnz | Nonzero entries of \(\mathbf{K}\) in row-major order |
| `col_indices` | nnz | Column index of each entry |
| `row_ptr` | \(N+1\) | Start index in `values` for each row |

For the three-node bar from the worked example, \(\mathbf{K} = k\begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}\) with seven nonzeros:

```text
values      = [ k, -k, -k, 2k, -k, -k, k ]
col_indices = [ 0,  1,  0,  1,  2,  1,  2 ]
row_ptr     = [ 0,  2,  5,  7 ]
```

Matrix–vector multiply \(\mathbf{y} = \mathbf{K}\mathbf{x}\) becomes a loop over rows: for each row \(i\), accumulate `values[j] * x[col_indices[j]]` for \(j\) from `row_ptr[i]` to `row_ptr[i+1]-1`. No dense storage, no wasted multiplies by zero — the same sparsity pattern Part I.1 attributed to **local coupling** is now a data structure.

The scatter map \(\mathbf{L}_e\) is what the assembly loop implements without ever building \(\mathbf{L}_e\) explicitly:

```text
for each element e:
    gather u_e from global u using connectivity table
    f_e = k_e @ u_e
    for each local DOF i:
        global_I = connectivity[e, i]
        for each local DOF j:
            global_J = connectivity[e, j]
            K[global_I, global_J] += k_e[i, j]   # scatter-add
```

The connectivity table is the sparse index map; the scatter-add is the CSR update. When two elements share a node (node 2 in the two-element example), their contributions **add** at the same matrix entry — superposition in the global basis, implemented as `+=` in the assembly loop.

| Concept (this chapter) | CSR / assembly equivalent |
|--------------------------|---------------------------|
| Change of basis \(\mathbf{L}_e\) | Connectivity table: local DOF → global index |
| \(\mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\) | Scatter-add of element block into global `values` |
| Sparsity from local coupling | `nnz` grows \(\mathcal{O}(N)\) for 1D bars, \(\mathcal{O}(N)\)–\(\mathcal{O}(N \log N)\) for 3D tetrahedra |
| Symmetry \(\mathbf{K} = \mathbf{K}^T\) | Store upper triangle only; mirror on scatter, or store full with duplicate entries |

**Why this matters for the copper wire.** A million-node 3D mesh might have \(N \sim 10^6\) DOFs but only \(\text{nnz} \sim 10^7\)–\(10^8\) — a fill ratio of 0.01% or less. Conjugate gradient (Part I.1) and algebraic multigrid preconditioners operate on CSR arrays, not dense matrices. Ill-conditioning from material contrast ([I.1](01-vectors-matrices.md)) shows up in the **condition number of the sparse system**, not in the storage format — but the format is what makes solving a million-DOF wire mesh feasible on a workstation.

Direct sparse solvers (Cholesky on SPD systems) exploit the same sparsity pattern for fill-reducing reorderings (Cuthill–McKee, nested dissection). The reordering is a **permutation** of the basis — another change of coordinates that reduces fill-in during factorization. Part IV's mesh generators and Part VII's polycrystal meshes both produce connectivity patterns whose quality (bandwidth, element aspect ratio) directly affects solver cost.

## Lab act: verify strain energy invariance under rotation

The rotated bar in the Lab act above must store the **same elastic energy** in local and global frames. This is the numerical check that assembly and rotation are implemented consistently — a one-line test every element routine should pass.

Take the \(4 \times 4\) global stiffness \(\mathbf{k}_{\text{global}}\) for a bar at \(\theta = 30^\circ\) and a displacement vector \(\mathbf{u}_{\text{global}}\) that corresponds to pure axial stretch \(\delta\) in the local frame: \(u_{\text{local}} = [\delta, 0]^T\) at each end, mapped through \(\mathbf{R}\). Compute:

\[
W_{\text{global}} = \tfrac{1}{2}\, \mathbf{u}_{\text{global}}^T \mathbf{k}_{\text{global}} \mathbf{u}_{\text{global}}, \qquad
W_{\text{local}} = \tfrac{1}{2}\, \mathbf{u}_{\text{local}}^T \mathbf{k}_{\text{local}} \mathbf{u}_{\text{local}}.
\]

These must agree to machine precision. If \(W_{\text{global}} \neq W_{\text{local}}\), the rotation matrix \(\mathbf{R}\) is wrong, the local stiffness is not symmetric, or the gather/scatter map permutes DOFs incorrectly.

| Test | Expected | Failure mode |
|------|----------|--------------|
| Energy invariance | \(\|W_{\text{global}} - W_{\text{local}}\| < 10^{-12}\) | Wrong \(\cos\theta/\sin\theta\) in \(\mathbf{R}\) |
| Symmetry | \(\mathbf{k}_{\text{global}} = \mathbf{k}_{\text{global}}^T\) | Missing scatter-add on off-diagonal coupling |
| Axial load path | Global force aligns with bar axis after \(\mathbf{k}\mathbf{u}\) | Connectivity table transposed |

For \(\delta = 10\,\mu\text{m}\), \(EA/L = 2.4 \times 10^8\,\text{N/m}\), the stored energy is \(W = \tfrac{1}{2}(EA/L)\delta^2 \approx 1.2 \times 10^{-2}\,\text{J}\) per element — the same number the load cell integrates over the full wire when all elements agree on what "stretch" means. Part IV's isoparametric elements pass the same test in 3D: strain energy computed in reference or physical coordinates must match; failure is the first sign of a bad Jacobian or inconsistent quadrature.

## Linear maps in the FEM pipeline (forward connection)

Part IV implements the following chain, each step a linear map (possibly composed with nonlinear constitutive updates):

```
Reference element  →  Physical element (Jacobian map)
Nodal values       →  Strains (B-matrix / symmetric gradient)
Strains            →  Stresses (constitutive, linearized as D-matrix)
Element forces     →  Global residual (assembly / scatter)
```

The **Jacobian** of the isoparametric map appears in every element integral; it is the determinant of a small matrix that measures how reference volume elements stretch into physical space. Ill-shaped elements (near-zero Jacobian) blow up conditioning — a geometric warning visible only after we understand maps, not just matrices.

Finite volume methods (Part V) use different maps — cell volumes, face normals, flux integrals — but the same principle: express physics in a convenient local frame, then transform to a global conservation statement.

## The transpose as adjoint: loads meet duals early

Every linear map \(\mathbf{A}: \mathbb{R}^n \to \mathbb{R}^m\) has a **transpose** \(\mathbf{A}^T: \mathbb{R}^m \to \mathbb{R}^n\). In mechanics, transposes are not abstract — they convert **forces to nodal loads** and **displacements to strains**:

\[
\mathbf{f} = \mathbf{A}^T \boldsymbol{\sigma}, \qquad \boldsymbol{\varepsilon} = \mathbf{B}\mathbf{u}.
\]

Virtual work \(\mathbf{u}^T \mathbf{f} = \boldsymbol{\varepsilon}^T \boldsymbol{\sigma}\) is the statement that \(\mathbf{B}^T\) is the **adjoint** of the strain operator with respect to the standard inner products — the discrete shadow of integration by parts in Part III.

| Operation | Map | Transpose / adjoint | Mechanical meaning |
|-----------|-----|---------------------|-------------------|
| Equilibrium | \(\mathbf{K}\mathbf{u} = \mathbf{f}\) | \(\mathbf{f}^T \mathbf{u}\) is work | Bilinear form \(a(u,v)\) in Part II |
| Assembly scatter | \(\mathbf{L}_e\) maps local → global | \(\mathbf{L}_e^T\) gathers element forces | Same connectivity, reverse direction |
| Least squares fit | \(\mathbf{A}\mathbf{x} \approx \mathbf{b}\) | Normal equations \(\mathbf{A}^T\mathbf{A}\) | Material calibration from test data |

When \(\mathbf{K}\) is symmetric, the map and its adjoint coincide — the same symmetry Part III demands for the energy bilinear form. Non-symmetric maps (convection operators in Part V, unsymmetric contact Jacobians) break this identity; their adjoints appear in **sensitivity analysis** and **a posteriori error estimation** (dual-weighted residuals in Part IV.5).

**Preview for Part II:** a load functional \(\ell(v) = \int f v\) is not a vector in the same space as displacement — it lives in the **dual** \(V^*\). The Riesz representation theorem (Part II.3) identifies dual objects with vectors only in Hilbert space. Until then, remember: \(\mathbf{f}\) enters equilibrium through \(\mathbf{K}^T = \mathbf{K}\), but Neumann data and traction loads are always "adjoint-side" objects paired with test functions.

## Concept map checkpoint (linear maps)

Assembly is geometry, not bookkeeping. Before eigenvalues diagonalize the map, summarize:

| Question | Linear-map answer (copper wire) |
|----------|--------------------------------|
| What **object**? | Linear map \(\mathbf{A}\): local element data → global equilibrium |
| What **structure**? | Change of basis, scatter/gather, transpose as adjoint |
| What **theorem**? | SVD reveals principal response directions; symmetry \(\Leftrightarrow\) self-adjoint bilinear form |
| What **breaks**? | Wrong Jacobian (ill-shaped elements); rank deficiency; non-symmetric maps without adjoint care |

Part IV's pipeline — reference element → physical element → B-matrix → assembly — is the same map story at million-node scale. When the grip applies a global displacement, local element axes must agree on what "stretch" means.

## Bridge

Not every linear map is best viewed in the standard basis. The modes of vibration of a fixed–fixed copper wire, the principal stretches of a deformation gradient, and the normal modes of a coupled oscillator all arise from choosing a basis that **diagonalizes** the map. That is the story of eigenvalues — and the discrete preview of the spectral theorem we will meet in Part II.

| What I.2 established | What I.3 (eigenvalues) adds |
|----------------------|---------------------------|
| \(\mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\) scatter/gather | \(\mathbf{K}\mathbf{v}=\omega^2\mathbf{M}\mathbf{v}\); decoupled modal coordinates |
| Rotations, local/global frames, SVD principal directions | Natural frequencies on the spring-chain wire; Lanczos for lowest modes |
| SPD and symmetry as coercivity shadows | Spectral theorem preview before Part II operators |

**Scale-boundary handshake (I.1 → I.2 → I.3).**

| Vectors/matrices export ([I.1](01-vectors-matrices.md)) | Linear maps output (this chapter) | Eigenvalue consumer ([I.3](03-eigenvalues.md)) | Failure mode |
|---------------------------------------------------------|-----------------------------------|-----------------------------------------------|--------------|
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) nodal equilibrium | \(\mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\) scatter/gather assembly | \(\mathbf{K}\mathbf{v}=\omega^2\mathbf{M}\mathbf{v}\) modal decoupling | Wrong Jacobian in a rotated bar element |
| SPD symmetry \(\mathbf{K}=\mathbf{K}^T\) | Transpose as adjoint: \(\mathbf{B}^T\) maps stress to nodal loads | Self-adjoint generalized eigenproblem | Non-symmetric maps without adjoint care |
| Sparse local coupling in \(\mathbf{K}\) | Change of basis / rotation \(\mathbf{R}^T\mathbf{k}\mathbf{R}\) | Diagonalizing basis where \(\mathbf{K}\) acts by scaling | Rank deficiency → spurious rigid-body modes |
| Energy \(\mathbf{u}^T \mathbf{K}\mathbf{u}\) | Strain operator \(\boldsymbol{\varepsilon}=\mathbf{B}\mathbf{u}\) | Modal strain-energy partition by mode | Mixed local/global coordinates without rotation |

The rotated-bar Lab act is the numerical face of this handshake: assembly is geometry, not bookkeeping — and eigenvalues are the coordinate system in which the map tells its simplest story. When the wire hums at unexpected frequencies, check rank deficiency (rigid-body modes the grips must remove) before blaming material constants.

Return to the [prologue](../prologue/00-many-scales.md): **Act I — Mounting** fixes the wire, but a tap on the fixture excites **standing-wave pitches** — discrete normal modes before any continuum limit. [I.2](02-linear-maps.md) showed that assembly is a change of basis (\(\mathbf{L}_e\)); [I.3](03-eigenvalues.md) asks which basis **diagonalizes** the stiffness map so each mode oscillates independently. The Lab act that rotated a misaligned bar element is the same idea: wrong coordinates mix DOFs; eigenvectors are the coordinates where \(\mathbf{K}\) acts by pure scaling.

When the wire hums at unexpected frequencies, check rank deficiency (rigid-body modes the grips must remove) before blaming material constants — the same diagnostic [Part II.5](../part02-functional-analysis/05-spectral-theorem.md) will elevate to operator spectra. Part I's opening [**concept map**](00-opening.md#the-concept-map) asked what breaks if structure is missing; [I.3](03-eigenvalues.md) makes decoupling explicit before [I.4](04-toward-infinity.md) sends \(N\to\infty\) and Part II names the operator behind every assembled matrix.

Turn the page when assembly feels like bookkeeping rather than geometry — eigenvalues are the coordinate system in which the map tells its simplest story.
