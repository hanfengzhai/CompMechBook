## 2.1 Metric spaces and convergence

### Definition

A **metric space** $(X, d)$ is a set $X$ with a **metric** $d : X \times X \to \mathbb{R}$ satisfying:

1. **Non-negativity:** $d(x,y) \ge 0$, with equality iff $x = y$
2. **Symmetry:** $d(x,y) = d(y,x)$
3. **Triangle inequality:** $d(x,z) \le d(x,y) + d(y,z)$

### Examples

- **Euclidean space:** $(\mathbb{R}^n, d_2)$ with $d_2(\mathbf{x},\mathbf{y}) = \|\mathbf{x}-\mathbf{y}\|_2$
- **Continuous functions:** $C[a,b]$ with $d_\infty(f,g) = \max_{t \in [a,b]} |f(t) - g(t)|$
- **$L^2$ distance:** $d_{L^2}(f,g) = \|f-g\|_{L^2}$ (defined modulo null sets)

The last two already differ: a sequence can converge uniformly but not in $L^2$, or vice versa. **Choice of metric is a modeling choice**—it determines what "close" means.

### Open sets, closed sets, completeness

Open balls $B(x_0, r) = \{x : d(x,x_0) < r\}$ generate a **topology**. A Cauchy sequence $\{x_n\}$ satisfies $d(x_m, x_n) \to 0$ as $m,n \to \infty$. A metric space is **complete** if every Cauchy sequence converges in $X$.

Complete metric spaces are where iterative solvers and fixed-point theorems live. Completing $C[a,b]$ under the $L^2$ metric yields $L^2[a,b]$—functions are identified if they agree almost everywhere.

### Convergence in mechanics

When we say a FE solution $u_h$ converges to $u$, we mean $\|u_h - u\| \to 0$ in a chosen norm. Pointwise convergence at every $x$ is stronger than $L^2$ convergence; **energy norm** convergence (involving derivatives) is different still. Part IV will make these distinctions quantitative.

**Takeaway.** A metric turns "the approximation looks good" into a testable inequality. The norm we pick must match the energy of the physical problem.
