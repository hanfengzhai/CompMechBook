# Linear functionals and the dual space

## Linear functionals

A **linear functional** on a vector space \(V\) is a linear map \(\ell : V \to \mathbb{R}\) (or \(\mathbb{C}\)).

**Mechanics examples.**

- Point evaluation \(\delta_x(u) = u(x)\) (not continuous on \(L^2\) without more structure).
- Work done by loads: \(\ell(u) = \int_\Omega \mathbf{f}\cdot \mathbf{u}\, dx\).
- Constraint functionals in contact mechanics.

\(\ell\) is **bounded** if \(|\ell(u)| \le C\|u\|\). Bounded functionals are **continuous**.

## Dual space

The **dual space** \(V^\ast\) is the space of bounded linear functionals on \(V\), normed by

\[
\|\ell\| = \sup_{\|u\|=1} |\ell(u)|.
\]

If \(V\) is Hilbert, Riesz representation identifies \(V^\ast \cong V\):

\[
\ell(u) = \langle f, u \rangle, \qquad f \in V.
\]

## Weak formulation as dual pairing

Consider the Poisson problem \(-\Delta u = f\) in \(\Omega\), \(u=0\) on \(\partial\Omega\). Multiply by test function \(v\) and integrate:

\[
\int_\Omega \nabla u \cdot \nabla v\, dx = \int_\Omega f v\, dx.
\]

Define bilinear form \(a(u,v) = \int \nabla u\cdot\nabla v\) and functional \(\ell(v) = \int f v\). Seek \(u \in H^1_0(\Omega)\) such that

\[
a(u,v) = \ell(v) \quad \forall v \in H^1_0(\Omega).
\]

The right-hand side is a linear functional on \(H^1_0\).

## Hahn–Banach (statement)

Bounded functionals on a subspace extend to the whole space without increasing norm. This guarantees plenty of test functionals to probe solutions.

## Lax–Milgram theorem

**Theorem.** Let \(H\) be a Hilbert space and \(a : H \times H \to \mathbb{R}\) a bilinear form. If

1. **Continuity:** \(|a(u,v)| \le C\|u\|\|v\|\).
2. **Coercivity:** \(a(u,u) \ge \alpha \|u\|^2\) for some \(\alpha > 0\).

Then for every \(\ell \in H^\ast\) there exists unique \(u \in H\) with

\[
a(u,v) = \ell(v) \quad \forall v \in H,
\]

and \(\|u\| \le \|\ell\|/\alpha\).

*Proof idea.* Riesz representation applied to the bounded linear map \(v \mapsto \ell(v)\) with respect to the inner product induced by \(a\) via coercivity. ∎

Lax–Milgram is the existence theorem behind linear elasticity, heat conduction, and countless FEM formulations.

<div class="bridge">

**Bridge.** Weak forms use \(H^1\) functions whose derivatives exist in a **weak** sense—defined through integration by parts against smooth test functions.

</div>
