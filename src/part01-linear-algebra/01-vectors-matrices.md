# Vectors, Matrices, and the Language We Already Speak

Every computational mechanics code, before it knows anything about stress tensors or Navier–Stokes, knows about arrays. A displacement field on a mesh is a vector of nodal values. A stiffness matrix is a sparse array coupling degrees of freedom. Even the most exotic multiscale scheme eventually calls a linear solver. Linear algebra is not a prerequisite chapter we endure on the way to "real" mechanics — it is the grammar in which mechanics is written once discretized.

Return to the copper wire from the prologue. At the scale of a tensile test, an engineer might model it as a chain of axial bar elements. Each node carries one scalar displacement along the wire axis. Stack those scalars into a column vector, assemble a stiffness matrix from element contributions, and the equilibrium problem is linear algebra before it is anything else. The wire does not know it is being approximated; the code only sees numbers in \(\mathbb{R}^N\).

## Vectors as state

A **state** is whatever we need to know to predict the future. For a truss with \(n\) nodes in 2D, the state might be \(\mathbf{u} \in \mathbb{R}^{2n}\) stacking horizontal and vertical displacements. For a finite element model with \(N\) degrees of freedom, \(\mathbf{u} \in \mathbb{R}^N\).

Two operations appear immediately:

- **Addition**: superposition of increments, \(\mathbf{u} + \delta\mathbf{u}\).
- **Scalar multiplication**: scaling a perturbation, \(\alpha \delta\mathbf{u}\).

These make the set of states into a **vector space**. The dimension \(N\) counts independent degrees of freedom. Already we have a preview of Part II: when \(N \to \infty\), vectors become functions, but the grammar stays the same.

### Column vectors, geometry, and the inner product

We write vectors as columns \(\mathbf{u} \in \mathbb{R}^N\). The **standard inner product** is

\[
\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v} = \sum_{i=1}^{N} u_i v_i.
\]

Geometrically, \(\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\,\|\mathbf{v}\|\cos\theta\). Orthogonal vectors decouple in energy expressions — a fact that reappears when eigenvectors of symmetric stiffness matrices are interpreted as independent deformation modes.

The **Euclidean norm** is \(\|\mathbf{u}\| = \sqrt{\mathbf{u}\cdot\mathbf{u}}\). In finite elements, we often use a **weighted** inner product with a mass matrix \(\mathbf{M}\):

\[
(\mathbf{u}, \mathbf{v})_{\mathbf{M}} = \mathbf{u}^T \mathbf{M} \mathbf{v}.
\]

The mass matrix approximates the \(L^2\) inner product of continuous fields on a mesh (Part III). For a uniform mesh of bar elements on the copper wire, \(\mathbf{M}\) is diagonal with entries proportional to element length — a discrete version of integrating \(u v\) over the domain.

## Matrices as linear maps

A matrix \(\mathbf{K} \in \mathbb{R}^{N \times N}\) acts on a vector:

\[
\mathbf{f} = \mathbf{K}\mathbf{u}.
\]

In static elasticity, \(\mathbf{K}\) is the **stiffness matrix** and \(\mathbf{f}\) the load vector. The map \(\mathbf{u} \mapsto \mathbf{K}\mathbf{u}\) is **linear**:

\[
\mathbf{K}(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha \mathbf{K}\mathbf{u} + \beta \mathbf{K}\mathbf{v}.
\]

Nonlinear mechanics still linearizes: at each Newton step we solve a tangent system \(\mathbf{K}_T \delta\mathbf{u} = \mathbf{R}\). The matrix is the local linear model.

Matrix multiplication composes maps. If \(\mathbf{y} = \mathbf{B}\mathbf{x}\) and \(\mathbf{z} = \mathbf{A}\mathbf{y}\), then \(\mathbf{z} = (\mathbf{A}\mathbf{B})\mathbf{x}\). In a finite element pipeline, the composition "restrict to element → integrate constitutive law → scatter to global vector" is exactly this algebra, implemented sparsely.

### Transpose, symmetry, and storage

The transpose \(\mathbf{K}^T\) swaps rows and columns. For linear elasticity in small strain, \(\mathbf{K}\) is **symmetric** (\(\mathbf{K} = \mathbf{K}^T\)), reflecting the symmetry of the bilinear form \(\mathbf{v}^T \mathbf{K}\mathbf{u}\). Symmetry allows storing only the upper triangle and using Cholesky or conjugate gradient solvers tuned for symmetric positive definite systems.

| Matrix role | Typical size | Structure | Appears in |
|-------------|--------------|-----------|------------|
| Stiffness \(\mathbf{K}\) | \(N \times N\) | Sparse, symmetric SPD | Static FEM |
| Mass \(\mathbf{M}\) | \(N \times N\) | Sparse, symmetric SPD | Dynamics, \(L^2\) projection |
| Damping \(\mathbf{C}\) | \(N \times N\) | Sparse | Viscoelastic models |
| Jacobian | \(N \times N\) | Sparse, nonsymmetric | Nonlinear Newton steps |
| Constraint \(\mathbf{C}\) | \(m \times N\) | Sparse | Contact, incompressibility |

## Inner products and energy

The elastic **strain energy** of a discrete system is

\[
\Pi(\mathbf{u}) = \tfrac{1}{2}\mathbf{u}^T \mathbf{K} \mathbf{u} - \mathbf{f}^T \mathbf{u}.
\]

Minimizing \(\Pi\) gives \(\mathbf{K}\mathbf{u} = \mathbf{f}\). This discrete energy principle is the finite-dimensional shadow of the variational principles in Part III and Part IV.

Setting \(\partial \Pi / \partial \mathbf{u} = \mathbf{0}\) yields equilibrium. The quadratic form \(\mathbf{u}^T \mathbf{K}\mathbf{u}\) is twice the stored elastic energy when \(\mathbf{K}\) is the small-strain stiffness. Pull the copper wire: the discrete energy increases quadratically in displacement as long as the material stays in the linear elastic range.

## Worked example: three-node bar in axial tension

Consider a 1D copper wire discretized by three nodes and two bar elements of length \(L/2\), Young's modulus \(E\), area \(A\). Each bar element has local stiffness

\[
\mathbf{k}_e = \frac{EA}{L/2}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Fix node 1 (\(u_1 = 0\)) and apply force \(F\) at node 3. After eliminating the constrained degree of freedom, the reduced system for \((u_2, u_3)\) is

\[
\frac{EA}{L/2}\begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}
\begin{bmatrix} u_2 \\ u_3 \end{bmatrix}
=
\begin{bmatrix} 0 \\ F \end{bmatrix}.
\]

Solution gives \(u_3 = 3FL/(2EA)\): the end displacement predicted by a two-element model. Refining the mesh (increasing \(N\)) converges toward the continuum solution \(u(x) = Fx/(EA)\) — the first hint that \(\mathbb{R}^N\) approximates a function space as \(N\) grows.

## Matrix decompositions: previews that matter

Full factorizations are standard in ME 300A; in computational mechanics we meet them constantly:

- **LU** (\(\mathbf{K} = \mathbf{L}\mathbf{U}\)): general direct solve; pivoting for stability.
- **Cholesky** (\(\mathbf{K} = \mathbf{L}\mathbf{L}^T\)): for symmetric positive definite \(\mathbf{K}\); used in implicit time stepping and nonlinear subproblems.
- **QR** (\(\mathbf{A} = \mathbf{Q}\mathbf{R}\)): orthonormal bases; least squares; constraint handling.
- **Eigendecomposition** (\(\mathbf{K} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^T\)): normal modes, stability, principal directions (Chapter 3).
- **SVD** (\(\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^T\)): rank, conditioning, reduced-order models.

We do not need every algorithm in this chapter. We need the picture: **decompositions expose structure** — symmetry, spectrum, independence — that raw floating-point arrays hide.

## Norms and convergence

We measure size with \(\|\mathbf{u}\|\). Numerical methods produce approximations \(\mathbf{u}_h\); we ask whether \(\|\mathbf{u} - \mathbf{u}_h\|\) is small.

Three norms dominate finite element error analysis:

| Name | Definition | Meaning |
|------|------------|---------|
| Energy norm | \(\|\mathbf{u}-\mathbf{u}_h\|_{\mathbf{K}} = \sqrt{(\mathbf{u}-\mathbf{u}_h)^T \mathbf{K}(\mathbf{u}-\mathbf{u}_h)}\) | Natural for elliptic problems |
| \(L^2\) norm | \(\sqrt{(\mathbf{u}-\mathbf{u}_h)^T \mathbf{M}(\mathbf{u}-\mathbf{u}_h)}\) | Mean-square field error |
| \(L^\infty\) norm | \(\max_i |u_i - u_{h,i}|\) | Worst nodal error |

When we pass to function spaces in Part II, these become the \(H^1\), \(L^2\), and \(L^\infty\) norms — same ideas, richer setting.

## The four fundamental subspaces (finite-dimensional preview)

For \(\mathbf{A} \in \mathbb{R}^{m \times n}\), the **column space** \(\mathcal{R}(\mathbf{A})\) is the set of reachable outputs; the **null space** \(\mathcal{N}(\mathbf{A})\) is the set of inputs mapped to zero. For an unconstrained stiffness matrix, rigid-body modes live in \(\mathcal{N}(\mathbf{K})\). Boundary conditions and constraints remove them — otherwise \(\mathbf{K}\mathbf{u}=\mathbf{f}\) has no unique solution.

The **row space** and **left null space** govern solvability: \(\mathbf{f}\) must lie in the column space of \(\mathbf{K}\) for equilibrium to exist. In mixed formulations (pressure–velocity, contact), the augmented system’s block structure makes these subspaces explicit. Part IV’s assembly chapter is, in disguise, linear algebra on sparse matrices whose null spaces encode physics.

## Sparsity and scale

A million-node copper-wire bundle model might have \(N \sim 10^6\) degrees of freedom but only \(\mathcal{O}(10^1)\) nonzeros per row of \(\mathbf{K}\) — each node couples only to neighbors on the mesh. **Sparsity** is why direct solvers use reorderings (Cuthill–McKee, nested dissection) and why iterative methods (CG, GMRES) beat dense \(\mathcal{O}(N^3)\) factorization at large \(N\). The matrix pattern is the graph of the mesh; refining the discretization increases \(N\) and narrows the bandwidth but preserves the local coupling structure.

| Operation | Dense cost | Sparse typical cost |
|-----------|------------|---------------------|
| Matrix–vector product | \(N^2\) | \(\mathcal{O}(N)\) |
| Cholesky factorization | \(N^3/3\) | Depends on fill-in |
| Conjugate gradient | — | \(\mathcal{O}(N \sqrt{\kappa})\) per solve |

Conditioning of \(\mathbf{K}\) — tied to material contrast, mesh quality, and constraint patterns — determines whether a sparse direct factorization or an iterative solver with preconditioner is the practical choice. Chapter 3 connects this to the eigenvalue spectrum; Part IV connects it to mesh refinement and error control.

## Why this matters for the story

Computational mechanics does not replace linear algebra with something exotic. It **lifts** linear algebra to functions, then **projects** back to finite dimensions. The stiffness matrix is not an ad hoc data structure; it is the Riesz representation of a bilinear form restricted to a finite-dimensional subspace.

Finite volume methods (Part V) assemble conservation balances that also reduce to sparse linear systems — different discretization philosophy, same \(\mathbf{A}\mathbf{x}=\mathbf{b}\) at the end of the day. Molecular dynamics integrators advance a state vector by matrix–vector products with the Hessian of an interatomic potential. The copper wire at every scale eventually asks: what is the state vector, and what matrix maps it forward or toward equilibrium? Part I answers that question in finite dimensions; Part II and Part III lift it to fields.

## Bridge

With vectors and matrices in hand, we next examine **linear maps** abstractly: change of basis, coordinate transformations, and the assembly operators that translate element-level physics into global systems. The bar element stiffness in the worked example above was written in local node coordinates; connecting two elements requires a change of coordinates — the subject of the next chapter. The copper wire, meshed or unmeshed, is the same physical object in every basis we choose.

