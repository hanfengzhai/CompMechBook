# Inner Products and Hilbert Spaces

Where a norm tells us how large a object is, an inner product tells us how aligned two objects are. In mechanics, orthogonality of modes, projection onto subspaces, and energy identities all arise from inner products.

## Definition

An **inner product** on \(V\) is a map \((\cdot,\cdot): V \times V \to \mathbb{R}\) (conjugate-linear in the second argument for complex spaces; linear in both for real spaces) such that:

1. \((u,u) \ge 0\) with equality iff \(u = 0\)
2. \((u,v) = (v,u)\)
3. \((u, \alpha v + w) = \alpha (u,v) + (u,w)\)

It induces a norm \(\|u\| = \sqrt{(u,u)}\). A **Hilbert space** is a complete inner-product space.

## \(L^2\) as the canonical Hilbert space

\[
(u,v)_{L^2} = \int_\Omega u(x)\, v(x)\, d\Omega
\]

makes \(L^2(\Omega)\) a Hilbert space. Parseval's identity extends orthonormal expansions: if \(\{\phi_k\}\) is an orthonormal basis,

\[
\|u\|_{L^2}^2 = \sum_k |(u,\phi_k)|^2.
\]

Fourier modes decouple because they are orthogonal in \(L^2\).

## Best approximation in subspaces

Given a closed subspace \(W \subset H\) and \(u \in H\), there exists a unique **best approximant** \(u_W \in W\) minimizing \(\|u - w\|\). It satisfies the **orthogonality condition**

\[
(u - u_W, w) = 0 \quad \forall w \in W.
\]

This is the theoretical heart of the Galerkin method: the finite element solution is the best approximation to the true solution in the energy norm, **if** we measure orthogonality with the correct bilinear form.

## Riesz representation

Every continuous linear functional \(\ell \in H^*\) on a Hilbert space can be written uniquely as

\[
\ell(v) = (f, v)
\]

for some \(f \in H\). Loads in weak forms are functionals; Riesz representation turns them into functions we can integrate against test functions.

## Energy inner products

For Poisson's equation, the **energy inner product** is

\[
a(u,v) = \int_\Omega \nabla u \cdot \nabla v \, d\Omega.
\]

It is an inner product on \(H^1_0(\Omega)\) (equivalent to the \(H^1\) norm by Poincaré's inequality). The weak solution satisfies

\[
a(u,v) = (f,v)_{L^2} \quad \forall v \in H^1_0(\Omega),
\]

which is equivalent to **Galerkin orthogonality of the error**:

\[
a(u - u_h, v_h) = 0 \quad \forall v_h \in V_h.
\]

The discrete error is \(H^1\)-orthogonal to the test space in the energy inner product — Céa's lemma follows.

## Bridge

Operators on Hilbert spaces generalize matrices. Dual spaces generalize row vectors and Lagrange multipliers. Weak convergence generalizes convergence in norm when oscillations persist — exactly what happens near shocks and defects.
