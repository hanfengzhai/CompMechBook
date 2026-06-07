## 2.5 Weak derivatives and Sobolev spaces

### Motivation

Classical solutions of $-\Delta u = f$ require $u \in C^2(\Omega)$—twice differentiable everywhere. Physical fields have corners, kinks, and material interfaces where $C^2$ fails. **Weak derivatives** relax smoothness: $u$ may not have a classical $\partial u / \partial x$, but an integral identity can still define $\partial u / \partial x$ as an $L^2$ function.

### Weak derivative

For $u \in L^2(\Omega)$, a function $u_{x_i} \in L^2(\Omega)$ is a **weak partial derivative** if

$$
\int_\Omega u \, \frac{\partial \phi}{\partial x_i} \, d\Omega = -\int_\Omega u_{x_i} \phi \, d\Omega
$$

for all smooth test functions $\phi$ with compact support in $\Omega$. Integration by parts transfers derivatives from $u$ to $\phi$—the same maneuver that produces the weak form of a BVP.

### Sobolev spaces

For $k \ge 0$ and $1 \le p \le \infty$,

$$
W^{k,p}(\Omega) = \{ u \in L^p(\Omega) : D^\alpha u \in L^p(\Omega) \text{ for } |\alpha| \le k \},
$$

with norm combining $L^p$ norms of $u$ and its weak derivatives. The case $p = 2$, written $H^k(\Omega)$, is Hilbert.

**$H^1(\Omega)$** is the standard energy space for second-order elliptic problems: functions whose gradient is square-integrable. **$H_0^1(\Omega)$** is the subspace of $H^1$ functions that vanish on $\partial\Omega$ in the trace sense—homogeneous Dirichlet boundary conditions.

### Trace theorem

Restriction $u|_{\partial\Omega}$ is well-defined for $u \in H^1(\Omega)$ via a bounded **trace operator** $\gamma : H^1(\Omega) \to L^2(\partial\Omega)$. Dirichlet data $u = g$ on $\partial\Omega$ is imposed on $\gamma u$, not pointwise.

### Embeddings

For bounded Lipschitz $\Omega$,

$$
H^1(\Omega) \hookrightarrow L^2(\Omega) \quad \text{(compact if bounded)}.
$$

Functions in $H^1$ need not be continuous pointwise in 2D and 3D, but they are continuous **almost everywhere** in a weak sense sufficient for engineering post-processing.

**Takeaway.** $H^1$ is where Galerkin lives. FEM shape functions are piecewise polynomials in $H^1$; their gradients are piecewise constant or linear—square integrable, not necessarily continuous.
