# Linear maps and change of basis

## Linear maps abstracted

A map \(T : V \to W\) between vector spaces is **linear** if

\[
T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})
\]

for all scalars \(\alpha, \beta\) and vectors \(\mathbf{u}, \mathbf{v}\).

In finite dimensions, choosing bases \(\{\mathbf{e}_i\}\) for \(V\) and \(\{\mathbf{f}_j\}\) for \(W\) represents \(T\) as a matrix with entries

\[
a_{ji} = \text{the } j\text{-th component of } T(\mathbf{e}_i) \text{ in the } \mathbf{f}\text{-basis}.
\]

**Key idea.** The map \(T\) is geometric; the matrix \(\mathbf{A}\) is a coordinate expression.

## Change of basis

Let \(\mathbf{P}\) be the matrix whose columns are the new basis vectors expressed in the old basis. If \(\mathbf{x}\) are old coordinates and \(\tilde{\mathbf{x}}\) new coordinates, then

\[
\mathbf{x} = \mathbf{P}\tilde{\mathbf{x}}.
\]

The matrix of \(T\) transforms as

\[
\tilde{\mathbf{A}} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P}.
\]

**Similarity transformations** preserve eigenvalues—why modal analysis is independent of whether you measure displacements in meters or millimeters, as long as you are consistent.

## The stiffness matrix in different bases

Consider a 1D bar element with linear shape functions. In local coordinates \(\xi \in [0,1]\),

\[
\mathbf{u}_e = \mathbf{N}(\xi)\mathbf{d}_e, \qquad
\mathbf{N}(\xi) = \begin{pmatrix} 1-\xi & \xi \end{pmatrix}.
\]

The element stiffness in local coordinates is

\[
\mathbf{k}_e = \int_0^1 \mathbf{B}^\top \mathbf{D} \mathbf{B}\, |\det J|\, d\xi,
\]

with \(\mathbf{B} = d\mathbf{N}/d\xi\). After mapping to global coordinates via an connectivity table, the same physical stiffness appears in a larger sparse \(\mathbf{K}\).

Nothing mystical happened: we changed basis from element-local nodal values to global nodal values.

## Range, null space, rank

For \(\mathbf{A} : \mathbb{R}^n \to \mathbb{R}^m\):

- **Range** \(\mathcal{R}(\mathbf{A}) = \{\mathbf{A}\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\}\): reachable outputs.
- **Null space** \(\mathcal{N}(\mathbf{A}) = \{\mathbf{x} : \mathbf{A}\mathbf{x} = \mathbf{0}\}\): inputs invisible to the map.
- **Rank** \(\mathrm{rank}(\mathbf{A}) = \dim \mathcal{R}(\mathbf{A})\).

**Mechanics.** Null vectors of \(\mathbf{K}\) are rigid-body modes. The rank deficiency of an unconstrained elasticity problem is 6 in 3D (three translations, three rotations).

## Adjoint and symmetry

In \(\mathbb{R}^n\) with the standard inner product, the **adjoint** of \(A\) is represented by \(\mathbf{A}^\top\). The map is **self-adjoint** if \(\mathbf{A} = \mathbf{A}^\top\).

For weighted inner products \(\langle \mathbf{u}, \mathbf{v} \rangle_{\mathbf{M}} = \mathbf{u}^\top \mathbf{M}\mathbf{v}\) (common in generalized eigenvalue problems \(\mathbf{K}\mathbf{x} = \lambda \mathbf{M}\mathbf{x}\)), symmetry becomes \(\mathbf{K}^\top \mathbf{M} = \mathbf{M}\mathbf{K}\).

## Composition and projection

Many numerical schemes are **projections**:

\[
\mathbf{u}_h = \mathbf{P}\mathbf{u},
\]

where \(\mathbf{P}\) projects a high-dimensional or infinite-dimensional state onto a finite subspace. FEM chooses \(\mathbf{P}\) via Galerkin projection; POD model reduction chooses \(\mathbf{P}\) from dominant modes.

Understanding linear maps as "something before coordinates" makes Part II natural: a function \(u(x)\) is a vector in an infinite-dimensional space, and a PDE operator is a linear map on that space.

<div class="bridge">

**Bridge.** Change of basis is the first hint of *equivalence*: many matrices describe the same physics. The deepest equivalence in mechanics is spectral—diagonalizing symmetric operators reveals principal directions. Eigenvalues are next.

</div>
