# Normed Spaces and Completeness

A norm is a length. On \(\mathbb{R}^N\), the Euclidean norm works. On function spaces, we choose norms that reflect the physics we care about — mean-square error, energy, maximum deflection.

## Definition

A **norm** on a vector space \(V\) assigns \(\|v\| \in \mathbb{R}_{\ge 0}\) satisfying:

1. \(\|v\| = 0 \iff v = 0\)
2. \(\|\alpha v\| = |\alpha|\,\|v\|\)
3. \(\|v + w\| \le \|v\| + \|w\|\) (triangle inequality)

A **normed space** \((V, \|\cdot\|)\) is a vector space with a norm. A norm induces a **metric** \(d(u,v) = \|u-v\|\), hence a notion of convergence.

## Examples that matter in mechanics

**\(L^p(\Omega)\)** for \(p \ge 1\):

\[
\|u\|_{L^p} = \left(\int_\Omega |u|^p \, d\Omega\right)^{1/p}.
\]

\(L^2\) is the default for energy and least-squares. \(L^\infty\) captures worst-case values:

\[
\|u\|_{L^\infty} = \text{ess sup}_{x \in \Omega} |u(x)|.
\]

**\(H^1(\Omega)\)** (Sobolev, previewed here):

\[
\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2.
\]

Functions in \(H^1\) need not be classically differentiable, but they have **weak derivatives** in \(L^2\). This is exactly the regularity FEM solutions possess.

## Cauchy sequences and completeness

A sequence \(\{u_n\}\) is **Cauchy** if \(\|u_n - u_m\| \to 0\) as \(n,m \to \infty\). In \(\mathbb{R}^N\), every Cauchy sequence converges. In spaces of smooth functions with the \(L^2\) norm, it does not: smooth functions can Cauchy-converge to a discontinuous limit.

A normed space is **complete** if every Cauchy sequence converges in the space. A complete normed space is a **Banach space**.

\(L^2(\Omega)\) and \(H^1(\Omega)\) are Banach (indeed Hilbert) spaces. The space \(C^\infty(\Omega)\) with the \(L^2\) norm is not.

## Why completeness matters for FEM

Galerkin approximations produce sequences \(u_h\) as mesh size decreases. We want \(u_h \to u\) in a meaningful norm. Proofs typically show \(\{u_h\}\) is Cauchy in an energy norm, then use completeness to identify the limit. Without a complete space, the limit might fall outside the admissible class — the discrete solutions would converge to something that is not a valid weak solution.

## Equivalent norms and hidden constants

On finite-dimensional spaces, all norms are **equivalent**: \(\|\cdot\|_a\) and \(\|\cdot\|_b\) differ by constant factors. In infinite dimensions, \(L^2\) and \(H^1\) are not equivalent on the whole space — \(H^1\) controls \(L^2\) but not conversely. This asymmetry is why coercivity in the \(H^1\) norm controls \(L^2\) error through Poincaré inequalities.

## Bridge

Norms measure size. Inner products measure angle and projection. Hilbert spaces — complete inner-product spaces — are where Galerkin orthogonality and energy minimization become rigorous.
