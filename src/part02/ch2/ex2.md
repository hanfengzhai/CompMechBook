## 2.2 Normed spaces and operators

### Normed spaces

A **normed space** $(V, \|\cdot\|)$ is a vector space $V$ with a norm $\|\cdot\| : V \to \mathbb{R}$ satisfying positivity, homogeneity, and the triangle inequality. Every norm induces a metric $d(u,v) = \|u-v\|$.

**Examples for computation:**

| Space | Norm | Role |
|-------|------|------|
| $\mathbb{R}^n$ | $\|\mathbf{x}\|_2$ | Algebraic systems |
| $C(\bar{\Omega})$ | $\|u\|_\infty = \sup |u|$ | Classical solutions |
| $L^2(\Omega)$ | $\|u\|_{L^2}$ | Least-squares residual |
| $H^1(\Omega)$ | $\|u\|_{H^1}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2$ | Elliptic energy |

A normed space is a **Banach space** if it is complete under its norm.

### Bounded linear operators

A map $T : V \to W$ is **bounded** if there exists $C$ with $\|Tu\|_W \le C \|u\|_V$ for all $u \in V$. The **operator norm** is

$$
\|T\| = \sup_{\|u\|=1} \|Tu\|.
$$

The stiffness operator $\mathcal{K} : H_0^1(\Omega) \to H^{-1}(\Omega)$ defined by $\langle \mathcal{K}u, v \rangle = \int_\Omega k \nabla u \cdot \nabla v \, d\Omega$ is bounded and coercive—properties that guarantee a unique weak solution.

### Compactness (preview)

In finite dimensions, bounded sequences have convergent subsequences. In infinite dimensions, this fails without extra structure. **Rellich–Kondrachov** compact embedding $H^1(\Omega) \hookrightarrow L^2(\Omega)$ for bounded $\Omega$ is what makes Galerkin approximations work: discrete spaces are finite-dimensional, hence compact inside $H^1$.

**Takeaway.** Operators on function spaces are the continuum limit of matrices. Boundedness and coercivity are the continuum limit of $\kappa(K) < \infty$ and $K$ positive definite.
