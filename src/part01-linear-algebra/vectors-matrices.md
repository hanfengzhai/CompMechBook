# Vectors, matrices, and systems

## Vectors as containers of degrees of freedom

A **vector** is an ordered list of numbers. In mechanics we always attach meaning to the ordering: entry \(i\) might be the \(x\)-displacement of node \(i\), or the velocity component in a particular direction.

For \(\mathbf{x}, \mathbf{y} \in \mathbb{R}^n\) and scalars \(\alpha, \beta\):

\[
\mathbf{x} + \mathbf{y} = (x_1+y_1, \ldots, x_n+y_n)^\top, \qquad
\alpha \mathbf{x} = (\alpha x_1, \ldots, \alpha x_n)^\top.
\]

The **dot product**

\[
\mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i = \mathbf{x}^\top \mathbf{y}
\]

measures alignment. In later chapters the dot product generalizes to inner products on function spaces; for now it is how we define angles and lengths:

\[
\|\mathbf{x}\|_2 = \sqrt{\mathbf{x} \cdot \mathbf{x}}.
\]

## Matrices as linear maps

An \(m \times n\) matrix \(\mathbf{A}\) represents a linear map \(A : \mathbb{R}^n \to \mathbb{R}^m\):

\[
(A\mathbf{x})_i = \sum_{j=1}^n a_{ij} x_j.
\]

**Mechanics interpretation.** If \(\mathbf{u}\) lists displacements and \(\mathbf{f} = \mathbf{K}\mathbf{u}\), then entry \(f_i\) is the force at degree of freedom \(i\) produced by the displacement field \(\mathbf{u}\) through the stiffness operator.

### Basic operations

- **Product** \(\mathbf{C} = \mathbf{A}\mathbf{B}\): apply \(B\), then \(A\).
- **Transpose** \((\mathbf{A}^\top)_{ij} = a_{ji}\): swaps domain and codomain in the inner-product sense.
- **Inverse** \(\mathbf{A}^{-1}\) when it exists: the map that undoes \(A\).

**Caution (from practice).** The statement "\(\mathbf{A}\mathbf{B} = \mathbf{I}\) implies \(\mathbf{A} = \mathbf{I}\)" is **false**. A counterexample:

\[
\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad
\mathbf{B} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.
\]

Similarly, \(\mathbf{A}\mathbf{B} = \mathbf{0}\) does not force either factor to vanish.

## Systems of equations

The linear system

\[
\mathbf{A}\mathbf{x} = \mathbf{b}
\]

asks: which input \(\mathbf{x}\) produces output \(\mathbf{b}\) under map \(A\)?

| Situation | Meaning |
|-----------|---------|
| Square \(\mathbf{A}\), \(\det \mathbf{A} \neq 0\) | unique solution \(\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}\) |
| Rectangular \(\mathbf{A}\) | least-squares or compatibility conditions |
| Singular \(\mathbf{A}\) | rigid-body modes or unconstrained mechanisms |

In FEM, singular stiffness matrices almost always signal **missing boundary conditions** or **mechanisms**.

## Symmetry and definiteness

A square matrix is **symmetric** if \(\mathbf{A} = \mathbf{A}^\top\). For symmetric \(\mathbf{A}\):

- \(\mathbf{A}\) is **positive definite** (PD) if \(\mathbf{x}^\top \mathbf{A}\mathbf{x} > 0\) for all \(\mathbf{x} \neq \mathbf{0}\).
- **Positive semi-definite** (PSD) allows \(\mathbf{x}^\top \mathbf{A}\mathbf{x} = 0\) for some \(\mathbf{x} \neq \mathbf{0}\).

Elastic stiffness matrices are symmetric PSD. Adding Dirichlet boundary conditions typically makes them PD.

**Proof sketch (PD stiffness).** For linear elasticity, strain energy \(U = \tfrac{1}{2}\mathbf{u}^\top \mathbf{K}\mathbf{u}\) is non-negative and vanishes only for rigid motions. Fixing translations and rotations removes the null space, yielding PD on the reduced system.

## Block structure and sparsity

Real stiffness matrices are **sparse**: each node connects only to neighbors, so \(\mathbf{K}\) has a banded or block-sparse pattern. Exploiting sparsity is not optional at engineering scale.

Example block form for a partitioned mesh:

\[
\begin{pmatrix} \mathbf{K}_{11} & \mathbf{K}_{12} \\ \mathbf{K}_{21} & \mathbf{K}_{22} \end{pmatrix}
\begin{pmatrix} \mathbf{u}_1 \\ \mathbf{u}_2 \end{pmatrix}
=
\begin{pmatrix} \mathbf{f}_1 \\ \mathbf{f}_2 \end{pmatrix}.
\]

Substructuring and domain decomposition—ideas we meet again in multiscale modeling—begin here.

<div class="bridge">

**Bridge.** Matrices encode linear maps between finite-dimensional spaces. In continuum mechanics the unknown is often a *function* (displacement field \(u(\mathbf{x})\)), not a finite list. The next chapter studies change of basis—the idea that the *same* map looks different in different coordinates—and prepares us to replace finite vectors with functions in Part II.

</div>
