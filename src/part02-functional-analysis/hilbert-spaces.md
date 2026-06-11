# Inner product spaces and Hilbert spaces

## Inner products

An **inner product** on a vector space \(V\) is a map \(\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}\) (real case) such that for all \(u,v,w \in V\) and scalars \(\alpha, \beta\):

1. \(\langle u, v \rangle = \langle v, u \rangle\) (symmetry).
2. \(\langle \alpha u + \beta v, w \rangle = \alpha\langle u,w\rangle + \beta\langle v,w\rangle\) (linearity in first slot).
3. \(\langle u, u \rangle \ge 0\) with equality iff \(u = 0\) (positive definiteness).

The induced norm is \(\|u\| = \sqrt{\langle u, u \rangle}\).

**Examples.**

- \(\mathbb{R}^n\): \(\langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x}^\top \mathbf{y}\).
- \(L^2(\Omega)\): \(\langle u, v \rangle = \int_\Omega u v \, dx\).
- Weighted mass matrix in FEM: \(\langle u_h, v_h \rangle = \mathbf{u}^\top \mathbf{M} \mathbf{v}\) for \(u_h, v_h\) in a finite element space.

## Cauchy–Schwarz inequality

**Theorem.** For any inner product space,

\[
|\langle u, v \rangle| \le \|u\|\,\|v\|.
\]

*Proof.* For scalar \(t\), \(0 \le \langle u + tv, u + tv \rangle = \|u\|^2 + 2t\langle u,v\rangle + t^2\|v\|^2\). The discriminant of this quadratic in \(t\) must be non-positive, yielding the inequality. ∎

## Orthogonality and projection

\(u \perp v\) means \(\langle u, v \rangle = 0\).

For a closed subspace \(W \subset H\) of a Hilbert space \(H\), every \(u \in H\) admits a unique decomposition

\[
u = u_W + u^\perp, \qquad u_W \in W,\; u^\perp \perp W.
\]

\(u_W\) is the **orthogonal projection** of \(u\) onto \(W\) and minimizes \(\|u - w\|\) over \(w \in W\).

**FEM connection.** Galerkin FEM finds \(u_h \in V_h\) such that the residual is orthogonal to \(V_h\) in the energy inner product—discrete orthogonal projection in disguise.

## Hilbert spaces

A **Hilbert space** is a complete inner product space.

\(L^2(\Omega)\) and \(H^1(\Omega)\) (defined shortly) are Hilbert spaces.

## Riesz representation (preview)

For a Hilbert space \(H\) and continuous linear functional \(\ell : H \to \mathbb{R}\), there exists unique \(f \in H\) such that

\[
\ell(u) = \langle f, u \rangle \quad \forall u \in H.
\]

Load functionals in variational forms are often Riesz representers.

## Energy inner product in elasticity

For displacements \(u, v \in H^1_0(\Omega)\),

\[
a(u,v) = \int_\Omega \boldsymbol{\varepsilon}(u) : \mathbb{C} : \boldsymbol{\varepsilon}(v)\, dx
\]

is an inner product if \(\mathbb{C}\) is symmetric positive definite and boundary conditions eliminate rigid modes. The induced norm \(\|u\|_a = \sqrt{a(u,u)}\) is the **energy norm**—the natural norm for measuring FEM error in elliptic problems.

<div class="bridge">

**Bridge.** Hilbert spaces have geometry. Linear operators are the maps between them—differential operators in mechanics are prime examples, once domain and range are chosen correctly.

</div>
