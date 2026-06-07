## 1.6 Norms: the bridge to analysis

### Vector norms

A **norm** on $\mathbb{R}^n$ is a map $\|\cdot\| : \mathbb{R}^n \to \mathbb{R}$ satisfying positivity, homogeneity, and the triangle inequality. Common norms:

| Name | Definition | Use |
|------|------------|-----|
| $\ell^2$ | $\|\mathbf{x}\|_2 = \sqrt{\sum x_i^2}$ | Energy norms, RMS error |
| $\ell^1$ | $\|\mathbf{x}\|_1 = \sum |x_i|$ | Sparse regression |
| $\ell^\infty$ | $\|\mathbf{x}\|_\infty = \max |x_i|$ | Pointwise max error |

All norms on $\mathbb{R}^n$ are **equivalent**: constants $c_1, c_2$ exist with $c_1 \|\mathbf{x}\|_a \le \|\mathbf{x}\|_b \le c_2 \|\mathbf{x}\|_a$. In finite dimensions, convergence in one norm is convergence in all.

### Matrix norms

The **induced** $\ell^2$ matrix norm is the largest singular value $\sigma_{\max}(A)$. The condition number $\kappa(A) = \|A\| \|A^{-1}\|$ measures worst-case error amplification.

In numerical experiments—comparing a central-difference temperature field to an exact solution, for instance—we report $\|\mathbf{T}_{\text{num}} - \mathbf{T}_{\text{exact}}\|_2$ and watch it decay as resolution refines. That decay rate foreshadows **convergence orders** in FEM.

### From vectors to functions

Replace $\sum |x_i|^2$ with $\int |u(x)|^2 \, dx$ and $\mathbb{R}^n$ with a space of functions. The $\ell^2$ norm becomes the **$L^2$ norm**:

$$
\|u\|_{L^2(\Omega)} = \left( \int_\Omega |u|^2 \, d\Omega \right)^{1/2}.
$$

Add derivatives and we reach **Sobolev norms** in Part II—the setting where FEM error analysis lives.

### Closing the part

Linear algebra gave us:

- **Representation** — matrices encode operators
- **Solution** — factorizations solve $A\mathbf{x}=\mathbf{b}$
- **Structure** — subspaces, rank, symmetry
- **Geometry** — orthogonality, projections
- **Spectra** — eigenvalues, conditioning
- **Measurement** — norms quantify error

Part II lifts each idea from $\mathbb{R}^n$ to infinite-dimensional spaces where PDE solutions reside. The wire we introduced in the Prologue will reappear as a domain $\Omega$ with a displacement field $u \in H^1(\Omega)$—but that language requires the functional analysis we develop next.
