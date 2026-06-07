## 5.1 Integral form and flux functions

### 1D conservation law

Consider a conserved quantity $U(x,t)$ with flux $F(U)$:

$$
\frac{\partial U}{\partial t} + \frac{\partial F(U)}{\partial x} = 0.
$$

Integrate over control volume $[x_{j-1/2}, x_{j+1/2}]$ of width $\Delta x_j$:

$$
\frac{d}{dt} \int_{x_{j-1/2}}^{x_{j+1/2}} U \, dx + F\big|_{x_{j+1/2}} - F\big|_{x_{j-1/2}} = 0.
$$

Define cell average $U_j(t) \approx \frac{1}{\Delta x_j}\int_{cell} U \, dx$. The **semidiscrete FVM** is

$$
\frac{dU_j}{dt} + \frac{F_{j+1/2} - F_{j-1/2}}{\Delta x_j} = 0,
$$

where $F_{j+1/2}$ is the **numerical flux** at the face—chosen to respect wave structure between neighboring cells.

### Euler equations (compressible flow)

For ideal gas dynamics in 1D, $U = [\rho, \rho u, \rho e_{\text{total}}]^T$ and

$$
F(U) = \left[\rho u,\; \rho u^2 + p,\; (\rho e_{\text{total}} + p)u\right]^T.
$$

In 3D conservation form (from CFD notes),

$$
\frac{\partial \mathbf{U}}{\partial t} + \frac{\partial \mathbf{E}}{\partial x} + \frac{\partial \mathbf{F}}{\partial y} + \frac{\partial \mathbf{G}}{\partial z} - \frac{\partial \mathbf{E}_v}{\partial x} - \cdots = 0,
$$

with state vector $\mathbf{U} = [\rho, \rho u, \rho v, \rho w, \rho E]^T$, convective fluxes $\mathbf{E}, \mathbf{F}, \mathbf{G}$, and viscous fluxes $\mathbf{E}_v, \mathbf{F}_v, \mathbf{G}_v$.

### Cell averages vs point values

FVM stores **averages**; reconstruction (MUSCL, WENO) builds left/right states at faces for higher accuracy. FEM stores **nodal values** and weakly enforces continuity—different philosophies, same PDEs.

**Takeaway.** FVM begins at the integral law—the form physics actually conserves. Discretization fails if face fluxes are inconsistent.
