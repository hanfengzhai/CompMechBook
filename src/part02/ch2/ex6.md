## 2.6 Variational formulations of BVPs

We now assemble the pipeline from a PDE to a variational problem—the exact object FEM discretizes.

### Strong form (1D model)

Find $u : [a,b] \to \mathbb{R}$ such that

$$
-\frac{d}{dx}\left(k(x)\frac{du}{dx}\right) + b(x)u = f(x), \quad x \in (a,b),
$$

with boundary conditions (Dirichlet $u(a) = g_0$, Neumann $u'(b) = h_1$, Robin, etc.).

### Residual and weighted residual

The **strong residual** is $R = Lu - f$ where $L$ is the differential operator. An approximate $\hat{u}$ leaves $R \neq 0$. The **method of weighted residuals** demands

$$
\int_\Omega R \, v \, d\Omega = 0
$$

for all test functions $v$ in a suitable space—orthogonality of the residual to tests, finite-dimensional least squares generalized.

### Integration by parts → weak form

Applying integration by parts once transfers one derivative from $u$ to $v$:

$$
\int_\Omega k u' v' \, d\Omega + \int_\Omega b u v \, d\Omega = \int_\Omega f v \, d\Omega + \text{boundary terms}.
$$

The left side defines a bilinear form $a(u,v)$; the right side defines a linear functional $\ell(v)$.

### Abstract problem

Find $u \in \mathcal{S}$ such that

$$
a(u, v) = \ell(v) \quad \forall v \in \mathcal{V},
$$

where $\mathcal{S}$ encodes essential (Dirichlet) boundary conditions and $\mathcal{V}$ is the test space (often $\mathcal{V} = \mathcal{S}$ for Galerkin).

### Example: Poisson with Dirichlet data

Let $\Omega \subset \mathbb{R}^d$, $f \in L^2(\Omega)$, $g$ on $\partial\Omega$. Seek $u \in H^1(\Omega)$ with $\gamma u = g$ and

$$
\int_\Omega \nabla u \cdot \nabla v \, d\Omega = \int_\Omega f v \, d\Omega \quad \forall v \in H_0^1(\Omega).
$$

Lax–Milgram applies; the solution minimizes the Dirichlet energy.

### Closing Part II

We have climbed from metrics to Hilbert spaces to the **weak form**—the precise infinite-dimensional problem that FEM approximates by choosing finite-dimensional $\mathcal{S}_h \subset \mathcal{S}$ and $\mathcal{V}_h \subset \mathcal{V}$.

Part III writes the continuum equations of solid and fluid mechanics in forms ready for this treatment. Part IV implements the discretization.
