## 5.2 Godunov-type schemes and Riemann solvers

### Piecewise constant reconstruction

Assume cell averages $U_j^n$ are piecewise constant. At face $j+1/2$, left state $U_L = U_j$ and right state $U_R = U_{j+1}$ define a **Riemann problem**: find self-similar solution $U(x/t)$ connecting $U_L$ and $U_R$.

The **Godunov flux** is

$$
F_{j+1/2} = F(U^*(0)),
$$

where $U^*(0)$ is the exact (or approximate) Riemann solution at $x=0$.

### Approximate Riemann solvers

Exact Riemann solutions for Euler are expensive. **Roe**, **HLL**, **HLLC**, and **Osher** solvers use wave-structure approximations—linearized Roe matrix, fastest/slowest wave speeds in HLL—that are cheap and robust.

### CFL condition

Explicit time stepping requires

$$
\Delta t \le C \frac{\Delta x}{|\lambda_{\max}|},
$$

where $|\lambda_{\max}|$ is the largest wave speed (fluid velocity plus sound speed). Violating CFL blows up the simulation—hyperbolic problems wear their stability criterion on their sleeve.

### Viscous terms

Navier–Stokes adds parabolic viscous fluxes $\mathbf{E}_v, \mathbf{F}_v$. These are often discretized with centered differences on faces (second order) while convective fluxes use upwinding—operator splitting by physical character, echoing Part III.

**Takeaway.** The Riemann solver is where FVM "knows" about shocks. FEM on the same problem needs stabilization (SUPG, DG) to avoid Gibbs oscillations.
