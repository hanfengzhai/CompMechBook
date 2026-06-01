# Linear Maps, Bases, and Change of Coordinates

A matrix is not merely a table of numbers. It is a **linear map** expressed in a particular basis. Change the basis and the matrix changes; the map itself does not. This distinction — coordinate representation versus intrinsic object — runs through every scale of computational mechanics.

## Linear maps and their matrix representations

A map \(T: \mathbb{R}^n \to \mathbb{R}^m\) is linear if

\[
T(\alpha \mathbf{x} + \beta \mathbf{y}) = \alpha T(\mathbf{x}) + \beta T(\mathbf{y}).
\]

Every such map can be written as \(T(\mathbf{x}) = \mathbf{A}\mathbf{x}\) for some \(\mathbf{A} \in \mathbb{R}^{m \times n}\). Examples in mechanics:

- **Gradient operator** (discretized): nodal values \(\mapsto\) strains at quadrature points.
- **Assembly operator**: element vectors \(\mapsto\) global vector.
- **Constitutive map** (linearized): strains \(\mapsto\) stresses.

## Bases and coordinates

A **basis** \(\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}\) lets us write \(\mathbf{x} = \sum_j x_j \mathbf{e}_j\). The coordinates \(x_j\) depend on the basis; the vector \(\mathbf{x}\) does not.

If \(\mathbf{B}\) is the matrix whose columns are new basis vectors expressed in the old basis, then coordinates transform as

\[
\mathbf{x}_{\text{old}} = \mathbf{B}\,\mathbf{x}_{\text{new}}, \qquad
\mathbf{A}_{\text{new}} = \mathbf{B}^{-1}\mathbf{A}_{\text{old}}\mathbf{B}.
\]

In finite elements, we change coordinates constantly: from reference element to physical element, from local degrees of freedom to global ones. Assembly is a structured change of basis.

## The stiffness matrix in local and global frames

Consider a single bar element with local stiffness \(\mathbf{k}_e \in \mathbb{R}^{2\times 2}\). An assembly matrix \(\mathbf{L}_e\) maps local DOFs to global DOFs:

\[
\mathbf{K} = \sum_e \mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e.
\]

Each \(\mathbf{L}_e\) is a sparse "scatter" operator — a change of coordinates. The global stiffness is the sum of the same physical stiffness expressed in different local frames and planted into a shared global basis.

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

Positive definiteness guarantees a unique equilibrium and makes conjugate gradient solvers effective. In Part II, the same property appears as **coercivity** of an elliptic operator.

## Rank, null space, and constraints

The **null space** of \(\mathbf{K}\) consists of rigid-body modes — displacements that produce no strain. Unconstrained bodies have nontrivial null spaces; boundary conditions remove them.

Lagrange multiplier methods (used heavily in contact and in mixed finite elements) augment the system:

\[
\begin{bmatrix} \mathbf{K} & \mathbf{C}^T \\ \mathbf{C} & \mathbf{0} \end{bmatrix}
\begin{bmatrix} \mathbf{u} \\ \boldsymbol{\lambda} \end{bmatrix}
=
\begin{bmatrix} \mathbf{f} \\ \mathbf{g} \end{bmatrix}.
\]

The constraint matrix \(\mathbf{C}\) encodes the geometry of admissible motion. Understanding null spaces at the matrix level prevents singular systems at the code level.

## Bridge to the next chapter

Not every linear map is best viewed in the standard basis. The modes of vibration, the principal stretches of a deformation gradient, and the normal modes of a coupled oscillator all arise from choosing a basis that **diagonalizes** the map. That is the story of eigenvalues — and the discrete preview of the spectral theorem we will meet in Part II.
