# Normed linear spaces

## Definition

A **normed linear space** (or **Banach space** if complete) is a vector space \(V\) over \(\mathbb{R}\) or \(\mathbb{C}\) with a map \(\|\cdot\| : V \to [0,\infty)\) such that for all \(u,v \in V\) and scalar \(\alpha\):

1. \(\|u\| = 0 \iff u = 0\).
2. \(\|\alpha u\| = |\alpha|\,\|u\|\).
3. \(\|u+v\| \le \|u\| + \|v\|\) (triangle inequality).

The induced metric is \(d(u,v) = \|u-v\|\).

**Examples in mechanics.**

| Space | Norm | Use |
|-------|------|-----|
| \(\mathbb{R}^n\) | \(\|\mathbf{x}\|_2\) | FEM DOF vectors |
| \(C(\bar\Omega)\) | \(\|u\|_\infty = \sup |u|\) | classical solutions |
| \(L^2(\Omega)\) | \(\|u\|_{L^2} = (\int |u|^2)^{1/2}\) | least-squares error |
| \(H^1(\Omega)\) | \(\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2\) | energy norms |

## Equivalence of norms in finite dimensions

**Theorem.** On a finite-dimensional vector space, any two norms are **equivalent**: there exist \(c, C > 0\) such that

\[
c\|u\|_a \le \|u\|_b \le C\|u\|_a.
\]

*Proof sketch.* It suffices to show any norm is equivalent to \(\|\cdot\|_2\) on \(\mathbb{R}^n\). Continuity of \(\|\cdot\|\) on the compact unit sphere \(\{u : \|u\|_2 = 1\}\) gives positive minimum \(c\) and finite maximum \(C\). ∎

In infinite dimensions, norms are **not** equivalent in general—\(L^2\) and \(L^\infty\) behave differently, and mesh refinement changes which norm best measures error.

## Banach spaces

A **Banach space** is a complete normed space.

\(L^p(\Omega)\) for \(1 \le p < \infty\) is Banach; \(C(\bar\Omega)\) with \(\|\cdot\|_\infty\) is Banach.

Completeness ensures Cauchy sequences of approximate solutions converge *within the space*—the analytical justification for passing to weak formulations.

## Boundedness and operator norms

A linear operator \(T : V \to W\) is **bounded** if

\[
\|T\| = \sup_{\|u\|=1} \|Tu\| < \infty.
\]

Boundedness \(\iff\) continuity at \(0\) \(\iff\) continuity everywhere.

For FEM, the stiffness operator \(u \mapsto -\mathrm{div}(\mathbf{D}\nabla u)\), when properly posed on \(H^1_0\), is bounded as a map from \(H^1\) to \(H^{-1}\) (dual space—developed soon).

## Best approximation in subspaces

Given a closed subspace \(W \subset V\) and \(u \in V\), an element \(u_h \in W\) minimizes \(\|u - u_h\|\) if and only if the residual is orthogonal to \(W\) in Hilbert spaces (next chapter). In Banach spaces alone, uniqueness of best approximants is not guaranteed—another reason energy methods favor Hilbert spaces.

---

**Theorem (uniform boundedness, statement).** Let \(\{T_n\}\) be a sequence of bounded linear maps from Banach space \(V\) to Banach space \(W\). If \(\sup_n \|T_n u\| < \infty\) for each fixed \(u \in V\), then \(\sup_n \|T_n\| < \infty\).

This principle guards against mesh-dependent operators blowing up silently.

<div class="bridge">

**Bridge.** Norms measure size. Inner products add angles and orthogonality—enabling Galerkin orthogonality of FEM residuals.

</div>
