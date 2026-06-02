# Vectors, Matrices, and the Language We Already Speak

Every computational mechanics code, before it knows anything about stress tensors or Navier–Stokes, knows about arrays. A displacement field on a mesh is a vector of nodal values. A stiffness matrix is a sparse array coupling degrees of freedom. Even the most exotic multiscale scheme eventually calls a linear solver. Linear algebra is not a prerequisite chapter we endure on the way to "real" mechanics — it is the grammar in which mechanics is written once discretized.

## Vectors as state

A **state** is whatever we need to know to predict the future. For a truss with \(n\) nodes in 2D, the state might be \(\mathbf{u} \in \mathbb{R}^{2n}\) stacking horizontal and vertical displacements. For a finite element model with \(N\) degrees of freedom, \(\mathbf{u} \in \mathbb{R}^N\).

Two operations appear immediately:

- **Addition**: superposition of increments, \(\mathbf{u} + \delta\mathbf{u}\).
- **Scalar multiplication**: scaling a perturbation, \(\alpha \delta\mathbf{u}\).

These make the set of states into a **vector space**. The dimension \(N\) counts independent degrees of freedom. Already we have a preview of Part II: when \(N \to \infty\), vectors become functions, but the grammar stays the same.

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

## Inner products and energy

The **standard inner product** on \(\mathbb{R}^N\) is

\[
\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{N} u_i v_i.
\]

In finite elements, we often use a **weighted** inner product with a mass matrix \(\mathbf{M}\):

\[
(\mathbf{u}, \mathbf{v})_{\mathbf{M}} = \mathbf{u}^T \mathbf{M} \mathbf{v}.
\]

The elastic **strain energy** of a discrete system is

\[
\Pi(\mathbf{u}) = \tfrac{1}{2}\mathbf{u}^T \mathbf{K} \mathbf{u} - \mathbf{f}^T \mathbf{u}.
\]

Minimizing \(\Pi\) gives \(\mathbf{K}\mathbf{u} = \mathbf{f}\). This discrete energy principle is the finite-dimensional shadow of the variational principles in Part III and Part IV.

## Norms and convergence

We measure size with the **Euclidean norm** \(\|\mathbf{u}\| = \sqrt{\mathbf{u}\cdot\mathbf{u}}\). Numerical methods produce approximations \(\mathbf{u}_h\); we ask whether \(\|\mathbf{u} - \mathbf{u}_h\|\) is small.

Three norms dominate finite element error analysis:

| Name | Definition | Meaning |
|------|------------|---------|
| Energy norm | \(\|\mathbf{u}-\mathbf{u}_h\|_{\mathbf{K}} = \sqrt{(\mathbf{u}-\mathbf{u}_h)^T \mathbf{K}(\mathbf{u}-\mathbf{u}_h)}\) | Natural for elliptic problems |
| \(L^2\) norm | \(\sqrt{(\mathbf{u}-\mathbf{u}_h)^T \mathbf{M}(\mathbf{u}-\mathbf{u}_h)}\) | Mean-square field error |
| \(L^\infty\) norm | \(\max_i |u_i - u_{h,i}|\) | Worst nodal error |

When we pass to function spaces in Part II, these become the \(H^1\), \(L^2\), and \(L^\infty\) norms — same ideas, richer setting.

## Why this matters for the story

Computational mechanics does not replace linear algebra with something exotic. It **lifts** linear algebra to functions, then **projects** back to finite dimensions. The stiffness matrix is not an ad hoc data structure; it is the Riesz representation of an bilinear form restricted to a finite-dimensional subspace.

With that in mind, we next examine linear maps, change of basis, and the special matrices that decouple complex coupled systems: eigenvalues.
