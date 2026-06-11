# Metric spaces

## Definition

A **metric space** \((X, d)\) is a set \(X\) together with a map \(d : X \times X \to [0, \infty)\) satisfying, for all \(x, y, z \in X\):

1. **Positivity:** \(d(x,y) = 0 \iff x = y\).
2. **Symmetry:** \(d(x,y) = d(y,x)\).
3. **Triangle inequality:** \(d(x,z) \le d(x,y) + d(y,z)\).

**Examples.**

- \(\mathbb{R}^n\) with \(d(\mathbf{x},\mathbf{y}) = \|\mathbf{x}-\mathbf{y}\|_2\).
- Any normed space with \(d(x,y) = \|x-y\|\).
- \(C([0,1])\) with \(d(f,g) = \max_{x\in[0,1]} |f(x)-g(x)|\) (uniform metric).

In computational mechanics we secretly use metrics whenever we measure errors: root-mean-square norms, energy norms, and maximum nodal differences are all distances.

## Open and closed sets

A set \(U \subset X\) is **open** if for every \(x \in U\) there exists \(\varepsilon > 0\) such that

\[
B_\varepsilon(x) = \{ y \in X : d(x,y) < \varepsilon \} \subset U.
\]

A set is **closed** if its complement is open.

**Interpretation.** Open sets are neighborhoods in which small perturbations stay inside; closed sets contain their limit points—important for feasible sets in optimization and for domains with boundary.

## Convergence and completeness

A sequence \(\{x_n\}\) **converges** to \(x\) if \(d(x_n, x) \to 0\).

A sequence is **Cauchy** if \(d(x_m, x_n) \to 0\) as \(m,n \to \infty\).

A metric space is **complete** if every Cauchy sequence converges to a point in \(X\).

**Mechanics example.** Continuous functions on \([0,1]\) with the uniform metric form a complete space. Polynomial approximations to a continuous displacement field converge uniformly if the limit is continuous.

Incomplete spaces are dangerous: Cauchy sequences of approximate solutions might "want" to converge to an object not in your space (e.g. a discontinuous function). Completing the space leads to Sobolev spaces and weak solutions.

## Compactness (preview)

\(K \subset X\) is **sequentially compact** if every sequence in \(K\) has a convergent subsequence in \(K\). In \(\mathbb{R}^n\), compact \(\iff\) closed and bounded (Heine–Borel).

Compactness underpins existence theorems (e.g. minimizers of energy functionals) via the **direct method in the calculus of variations**.

## Continuous maps

\(T : X \to Y\) is **continuous** at \(x_0\) if \(x \to x_0\) implies \(T(x) \to T(x_0)\). Equivalently: preimages of open sets are open.

Isometries preserve distance; contractions shrink it. Both appear in stability proofs for iterative solvers.

---

**Theorem (contraction mapping).** If \((X,d)\) is complete and \(T : X \to X\) satisfies \(d(Tx, Ty) \le \alpha\, d(x,y)\) with \(0 \le \alpha < 1\), then \(T\) has a unique fixed point \(x^\ast\), and the iteration \(x_{k+1} = T(x_k)\) converges to \(x^\ast\) from any start.

*Proof.* Standard: show \(\{x_k\}\) is Cauchy using the contraction property; completeness gives limit \(x^\ast\); uniqueness follows by comparing distances between two putative fixed points. ∎

This theorem is the backbone of implicit time-stepping and nonlinear FEM Newton iterations.

<div class="bridge">

**Bridge.** A metric tells us when approximations are close. Vector spaces add linear structure; norms add homogeneity and compatibility with scaling—yielding Banach spaces.

</div>
