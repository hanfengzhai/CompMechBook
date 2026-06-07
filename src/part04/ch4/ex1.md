## 4.1 From strong form to weak form

### Model problem

Find $u : \Omega \to \mathbb{R}$ on $\Omega = (a,b)$ such that

$$
-\frac{d}{dx}\left(k(x)\frac{du}{dx}\right) + c(x)u = f(x), \quad x \in \Omega,
$$

with mixed boundary conditions: Dirichlet $u(a) = g_0$, Neumann $u'(b) = h_1$, etc.

Define the differential operator $\mathcal{L}(x,u) = -\big(k(x)u'(x)\big)' + c(x)u(x)$. The **strong form** demands $\mathcal{L}(x,u) - f(x) = 0$ at every point.

### Residual and test functions

An approximate solution $\hat{u}$ produces a **domain residual** $R_\Omega = \mathcal{L}(x,\hat{u}) - f$. Weighted residual methods require

$$
\int_\Omega R_\Omega \, v \, d\Omega = 0
$$

for all $v$ in a test space $\mathcal{V}$.

### Integration by parts

Transferring one derivative from $\hat{u}$ to $v$:

$$
\int_\Omega k \hat{u}' v' \, d\Omega + \int_\Omega c \hat{u} v \, d\Omega = \int_\Omega f v \, d\Omega + \big[k \hat{u}' v\big]_{\partial\Omega}.
$$

Boundary terms implement Neumann and Robin conditions; Dirichlet data constrain the trial space $\mathcal{S}$.

### Trial and test spaces

- **Trial space** $\mathcal{S}$: approximate solutions live here; must satisfy essential BCs.
- **Test space** $\mathcal{V}$: typically smooth functions with homogeneous essential BCs.

For **Galerkin's method**, $\mathcal{V}$ is chosen equal to the homogeneous version of $\mathcal{S}$ (same dimension after Dirichlet reduction).

### Higher-order example

Even for $u''' = f$ with multiple boundary conditions, repeated integration by parts yields a weak form involving only $u''$ and $v''$ paired integrals—provided test functions are smooth enough and boundary terms are consistent.

**Takeaway.** The weak form is the input to FEM. If you cannot write the weak form, you cannot assemble the stiffness matrix correctly.
