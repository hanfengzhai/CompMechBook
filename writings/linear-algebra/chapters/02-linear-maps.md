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

Element 1 maps local DOFs \((u_1, u_2)\) to global indices; element 2 maps \((u_2, u_3)\). Assembly gives

\[
\mathbf{K} = k\begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}.
\]

The middle row reflects that node 2 feels stiffness from both elements — superposition in the global basis. This \(3 \times 3\) pattern is the one-dimensional prototype of the sparse assembly loops in Part IV.

## Worked example: ten bars on the wire

Scale the prototype to the homework mesh from Part I's opening scene: ten equal bar elements model a 100 mm copper cylinder pulled along its axis. Each element has length \(L_e = 10\) mm, cross-section \(A\), and axial stiffness \(k = EA/L_e\). Node 1 is fixed (\(u_1 = 0\)); node 11 carries the grip displacement; interior nodes 2–10 are free.

Assembly is the same scatter pattern repeated ten times. Element \(e\) connects nodes \(e\) and \(e+1\), contributing \(k\) to entries \((e,e)\), \((e+1,e+1)\), and \(-k\) to the off-diagonals \((e,e+1)\) and \((e+1,e)\). The global \(\mathbf{K}\) is tridiagonal with \(2k\) on the interior diagonal and \(k\) on the end that meets the moving grip — the **same map**, ten times, in a shared global basis.

Apply a unit load at node 11. The discrete solution \(\mathbf{u}\) is nearly linear along the axis — a discrete stand-in for the smooth field \(u(x)\) Part II will treat as a limit. Refine to twenty elements and the plotted profile smooths; refine again and the eye stops distinguishing mesh from continuum. The **assembly operator** did not change its logic; only the scatter matrix \(\mathbf{L}_e\) grew. That is the narrative hinge to Chapter 4: when \(N \to \infty\), we stop asking for bigger vectors and start asking for a function space.

| Mesh | Nodes \(N+1\) | What the plot shows |
|------|---------------|---------------------|
| 10 elements | 11 | Piecewise-linear displacement; visible kinks at nodes |
| 40 elements | 41 | Smooth curve; nodal values hard to distinguish from a field |
| 160 elements | 161 | Engineering plot indistinguishable from continuum solution |

The copper wire on screen is still a column vector — but the experiment already hints at the field description Parts II and III will make precise.

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

## Bridge

Not every linear map is best viewed in the standard basis. The modes of vibration of a fixed–fixed copper wire, the principal stretches of a deformation gradient, and the normal modes of a coupled oscillator all arise from choosing a basis that **diagonalizes** the map. That is the story of eigenvalues — and the discrete preview of the spectral theorem we will meet in Part II.

The eigenvectors of \(\mathbf{K}\) (with appropriate mass weighting) are standing-wave patterns on the mesh; their eigenvalues are squared natural frequencies. Before we pass to infinite-dimensional operators, we master this decoupling in \(\mathbb{R}^N\).
