## 1.2 Linear systems and elimination

The central computational problem of linear algebra is solving

$$
A \mathbf{x} = \mathbf{b},
$$

where $A \in \mathbb{R}^{n \times n}$ and $\mathbf{b} \in \mathbb{R}^n$. Every implicit time step, every Newton correction, every FE solve reduces to this pattern.

### Gaussian elimination and LU factorization

**Gaussian elimination** transforms $A$ into upper triangular form by elementary row operations. The result is an **LU factorization** $A = LU$ with $L$ lower triangular (unit diagonal) and $U$ upper triangular. Forward and back substitution then solve the system in $O(n^2)$ operations after an $O(n^3)$ factorization.

For a tridiagonal matrix arising from a 1D FE mesh or finite-difference stencil, elimination can be specialized to $O(n)$—a fact we exploit whenever a problem has nearest-neighbor coupling only.

### Pivoting and stability

Without **pivoting**, elimination can amplify roundoff errors. **Partial pivoting** (row swaps) yields $PA = LU$ with a permutation $P$. The growth factor in $U$ controls backward stability; ill-conditioned systems may need iterative refinement or higher precision regardless of pivoting.

### Conditioning

The **condition number** $\kappa(A) = \|A\| \|A^{-1}\|$ measures sensitivity of $\mathbf{x}$ to perturbations in $A$ or $\mathbf{b}$. A large $\kappa$ means the problem is **ill-conditioned**: small measurement errors become large solution errors. In FE, poorly shaped elements can inflate $\kappa(K)$; in MD, stiff bond potentials do the same for the Hessian.

### Worked idea: perturbed systems

Consider a nearly singular parameter $\varepsilon$ entering a coefficient of $A$. As $\varepsilon \to 0$, $\|A^{-1}\|$ grows and the numerical solution may diverge from the physical limit. Tracking $\|\mathbf{x}_{\text{numerical}} - \mathbf{x}_{\text{exact}}\|$ against $\varepsilon$ on a log scale reveals exponential error growth—a preview of how we will study discretization error in Part IV.

### Where this reappears

| Context | System | Structure |
|---------|--------|-----------|
| Static FEM | $K \mathbf{U} = \mathbf{F}$ | Symmetric positive definite (SPD) |
| Implicit heat step | $(M + \Delta t K)\mathbf{U}^{n+1} = \cdots$ | SPD |
| Newton–Raphson (nonlinear) | $J \Delta\mathbf{U} = -\mathbf{R}$ | Often nonsymmetric |

SPD systems admit **Cholesky factorization** $A = LL^T$, twice as fast as LU and numerically stable without pivoting. That is why elliptic FEM codes love Cholesky—or conjugate gradient, which needs only matrix-vector products with $K$.

**Takeaway.** Solving linear systems is not a footnote; it is the inner loop of computational mechanics. The factorization you choose should match the matrix structure the physics provides.
