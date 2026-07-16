# The Finite Volume Method in One Dimension

Part IV discretized elliptic problems on the copper wire — tension, conduction, bending — with trial functions and global stiffness. Part V turns to **conservation laws** and **hyperbolic fluxes**: the language of cooling air around a heated conductor, shock waves in a gas, and any field whose evolution is governed by net flux through control surfaces rather than by minimizing a quadratic energy.

The integral form of a conservation law balances fluxes through control volume boundaries. The finite volume method (FVM) replaces continuous averages with **cell averages** and exact fluxes with **numerical flux functions** that depend on data from neighboring cells. The 1D algorithm is clean enough to implement in an afternoon and rich enough to capture shocks — the standard first milestone in CFD education.

The author's FVM notes and CFD curriculum treat 1D advection and the Sod shock tube as mandatory verification cases before advancing to 2D grids and Navier–Stokes. This chapter follows that path.

## Scene: hot wire, cool air

The copper wire from the prologue carries current; its surface runs hotter than the surrounding air. Along a one-dimensional slice through the boundary layer — distance measured normal to the wire — temperature and heat flux obey a conservation law: what enters a control volume must equal what leaves plus what accumulates. Partition that slice into cells, store **cell averages** instead of point values, and balance fluxes at interfaces.

A coarse partition captures the gross gradient from hot wire to cool freestream; refine the cells near the wall and the same algorithm resolves the steep thermal boundary layer without changing philosophy — only the numerical flux at each face. This is FVM in miniature: conservation first, pointwise PDE second. The wire's conjugate heat transfer loop (Part V, Chapter 4) will exchange these cell-averaged fluxes with the FEM conduction field inside the solid; the 1D algorithm here is where that handshake begins.

## Mesh and cell averages

Partition \([x_{\min}, x_{\max}]\) into cells with interfaces at \(x_{j-1/2}\), centers at \(x_j\), and widths \(\Delta x_j\). The **cell average** at time \(t_n\) is

\[
U_j^n \approx \frac{1}{\Delta x_j}\int_{x_{j-1/2}}^{x_{j+1/2}} U(x, t_n)\, dx.
\]

Integrating \(\partial U/\partial t + \partial F/\partial x = 0\) over cell \(j\) and dividing by \(\Delta x_j\):

\[
\frac{d U_j}{dt} + \frac{F_{j+1/2} - F_{j-1/2}}{\Delta x_j} = 0.
\]

This is the **semi-discrete finite volume scheme**. Time discretization completes the method.

**Face fluxes** \(F_{j+1/2}\) are numerical approximations to the true flux at the interface, computed from \(U_j, U_{j+1}\), and possibly wider stencils. The choice of numerical flux determines accuracy, stability, and shock-capturing ability (Chapter 3).

## Fully discrete update

Forward Euler in time gives the explicit **FVM update**:

\[
U_j^{n+1} = U_j^n - \frac{\Delta t}{\Delta x_j}\left(F_{j+1/2}^n - F_{j-1/2}^n\right).
\]

Higher-order **Runge–Kutta** time stepping (RK2, RK3, TVD-RK) is standard for accuracy and stability. Stiff diffusive terms in Navier–Stokes may require implicit or IMEX schemes — treated in Chapter 4.

The **CFL condition** links \(\Delta t\) and \(\Delta x\): for advection at speed \(|a|\),

\[
\frac{|a|\,\Delta t}{\Delta x} \le C_{\text{CFL}},
\]

with \(C_{\text{CFL}} \le 1\) for explicit upwind schemes. Nonlinear systems use the maximum wave speed from the Riemann problem. Violating CFL produces instability — the discrete analog of Part I's eigenvalue stability analysis applied to the semi-discrete flux Jacobian.

## Consistency and conservation

A numerical flux function \(\mathcal{F}(U_L, U_R)\) is **consistent** if

\[
\mathcal{F}(U, U) = F(U).
\]

The scheme is **conservative** if the flux entering cell \(j\) from the right face equals the flux leaving cell \(j+1\) from the left face — same value, opposite sign. Summing the semi-discrete equations over all cells:

\[
\frac{d}{dt}\sum_j \Delta x_j U_j = F_{\text{left boundary}} - F_{\text{right boundary}}.
\]

Interior fluxes telescope. **Global conservation** holds exactly on the discrete level — a property Galerkin FEM does not guarantee unless the formulation is carefully designed (e.g., conservative DG).

## Linear advection: upwind vs. central

For \(U_t + a U_x = 0\) with \(a > 0\), the **upwind flux** is

\[
F_{j+1/2} = a U_j.
\]

Information flows from left to right; the face value comes from the upwind cell. This scheme is stable for CFL \(\le 1\) and dissipates high wavenumbers — numerical diffusion smears sharp fronts over a few cells.

**Central flux** \(F_{j+1/2} = a(U_j + U_{j+1})/2\) is second-order accurate on smooth data but **unstable** for pure advection: parasitic modes grow unbounded. Adding artificial viscosity restores stability at the cost of smearing.

The lesson generalizes: hyperbolic operators need **directional bias** in the discretization. Part IV's symmetric Galerkin form is ideal for elliptic problems; hyperbolic problems demand upwind or Riemann fluxes.

## Example: advection of a square pulse

Initialize \(U_j^0 = 1\) on \([0.2, 0.4]\) and 0 elsewhere on \([0,1]\) with periodic boundaries. Advect with \(a = 1\) for one period. Upwind moves the pulse without growth; central blows up. MUSCL with a limiter (Chapter 3) advects with less smearing than first-order upwind.

This test — trivial analytically, diagnostic numerically — should run before any shock tube calculation.

### Worked example: a 70-line Python advection solver

The listing below implements first-order upwind FVM for \(U_t + a U_x = 0\) on \([0,1]\) with periodic boundaries. It verifies CFL stability and conservation of the pulse integral (up to quadrature error).

```python
#!/usr/bin/env python3
"""1D periodic advection: U_t + a U_x = 0, first-order upwind FVM."""
import numpy as np

def solve_advection(a=1.0, nx=200, nt=500, t_end=1.0):
    x = np.linspace(0, 1, nx, endpoint=False)
    dx = x[1] - x[0]
    dt = t_end / nt
    cfl = abs(a) * dt / dx
    if cfl > 1.0:
        raise ValueError(f"CFL={cfl:.3f} > 1; reduce dt or increase nx")

    U = np.zeros(nx)
    U[(x >= 0.2) & (x < 0.4)] = 1.0
    mass0 = U.sum() * dx

    for _ in range(nt):
        F = np.zeros(nx + 1)
        for j in range(nx + 1):
            jl = (j - 1) % nx
            jr = j % nx
            U_L = U[jl] if a >= 0 else U[jr]
            F[j] = a * U_L
        U = U - (dt / dx) * (F[1:] - F[:-1])

    mass1 = U.sum() * dx
    print(f"CFL={cfl:.3f}, mass drift={abs(mass1 - mass0):.2e}")
    return x, U

if __name__ == "__main__":
    x, U = solve_advection()
    peak = U.max()
    print(f"peak after one period (expect ~1.0): {peak:.4f}")
```

Run with increasing `nx` at fixed CFL: the smeared pulse width should shrink as \(O(\Delta x)\). Switch the flux to central differencing (`F[j] = a * 0.5 * (U[jl] + U[jr])`) and watch instability appear within a few steps — the same directional bias Part IV's symmetric Galerkin form does not provide for hyperbolic problems.

For the heated copper wire's cooling air (Part V, Chapter 4), this script is the skeleton: replace scalar \(U\) with \(\mathbf{U} = (\rho, \rho u, \rho E)\), replace upwind with an HLLC flux (Chapter 3), and add viscous fluxes implicitly when the Reynolds number is large.

## Burgers' equation: shock formation

Burgers' equation \(U_t + \partial(U^2/2)/\partial x = 0\) is a scalar model for nonlinear wave steepening. Smooth initial data develops a shock in finite time. A first-order upwind scheme captures the shock as a few-cell transition; exact solutions (rarefaction and shock relations) validate the numerical flux.

For flux \(F(U) = U^2/2\), upwind chooses

\[
F_{j+1/2} = \begin{cases} U_j^2/2 & \text{if } (U_j + U_{j+1})/2 > 0 \\ U_{j+1}^2/2 & \text{otherwise} \end{cases}
\]

Godunov's flux for Burgers is the exact Riemann solution — piecewise linear in the states.

## 1D Euler: toward the shock tube

For the Euler system, cell averages are vector-valued \(\mathbf{U}_j \in \mathbb{R}^3\). The semi-discrete form is

\[
\frac{d \mathbf{U}_j}{dt} = -\frac{1}{\Delta x_j}\left(\mathcal{F}(\mathbf{U}_j, \mathbf{U}_{j+1}) - \mathcal{F}(\mathbf{U}_{j-1}, \mathbf{U}_j)\right).
\]

Primitive variables \((\rho, u, p)\) are recovered from \(\mathbf{U}\) for plotting and boundary conditions. Negative density or pressure from a bad flux indicates scheme failure — positivity-preserving limiters exist but add complexity.

The **Sod shock tube** (Chapter 3) initializes piecewise constant states; the exact Riemann solution provides reference data for verification.

## Boundary conditions in 1D FVM

- **Periodic**: \(\mathbf{U}_0 = \mathbf{U}_{N-1}\), ghost cells mirror interior data.
- **Inflow**: specify \(\mathbf{U}\) or characteristic inflow variables at the boundary face.
- **Outflow**: zero-gradient extrapolation \(\mathbf{U}_{\text{ghost}} = \mathbf{U}_{\text{last interior}}\).
- **Reflecting wall**: velocity reverses; density and pressure copied from interior.

Ghost-cell strategies extend the stencil near boundaries without special-case flux formulas. Consistency with the integral form requires that boundary fluxes match the physical flux specification.

## Accuracy: order of the scheme

First-order upwind is \(O(\Delta x)\) in smooth regions, \(O(1)\) near shocks (shock width fixed at \(O(\Delta x)\)). Linear reconstruction plus limited slopes yields **MUSCL** schemes of second order in space. The tradeoff: higher order needs wider stencils and limiters to prevent oscillations at discontinuities.

Temporal accuracy follows the ODE integrator: forward Euler is \(O(\Delta t)\); SSP-RK3 is \(O(\Delta t^3\) for smooth problems subject to CFL limits.

## Connection to Part I and Part IV

The semi-discrete FVM system \(\mathbf{U}_t = \mathbf{A}(\mathbf{U})\) is a large ODE. Stability of explicit stepping depends on eigenvalues of the flux Jacobian — Part I's spectral radius story. When diffusive terms appear (viscosity in Navier–Stokes), the Jacobian gains stiff negative eigenvalues; implicit treatment of diffusion while keeping advection explicit (**IMEX**) splits the physics cleanly.

FVM on irregular grids in 2D/3D uses face areas and cell volumes in place of \(\Delta x\); the 1D logic is unchanged.

## Implementation sketch

A minimal 1D Euler solver requires:

1. Initialize \(\mathbf{U}_j\) on a uniform grid.
2. Loop over time steps: compute numerical fluxes at all interfaces, update cell averages.
3. Apply CFL check each step.
4. Convert to primitives for output; abort if \(\rho < 0\).

Under 100 lines in Python or C for first-order HLL flux — enough to reproduce Sod's solution and build intuition before OpenFOAM.

## Source terms and splitting

Many applications add stiff source terms \(S(U)\) — chemical reaction, gravity, friction. **Operator splitting** advances advection and sources separately: Strang splitting for second-order accuracy, or implicit treatment of stiff sources (IMEX) while keeping advection explicit under CFL. The 1D update becomes

\[
U_j^{n+1} = \mathcal{A}_{\Delta t}\left(U_j^n - \frac{\Delta t}{\Delta x}(F_{j+1/2}^n - F_{j-1/2}^n)\right),
\]

where \(\mathcal{A}_{\Delta t}\) is the source integrator. Splitting errors appear if scales are comparable; monolithic coupling may be necessary for detonation or fast chemistry.

## Relation to finite differences

On uniform grids, first-order FVM with upwind flux equals first-order finite differences on cell averages. The FVM framework generalizes naturally to unstructured meshes via face areas and cell volumes, whereas classical FD stencils assume structured topology. For CFD on complex domains (cooling channels around the copper wire), FVM or FV-based DG on general meshes is the practical choice.

## Bridge

Nonlinear systems require **Riemann solvers** at faces — exact or approximate solutions to local shock-tube problems that translate left and right cell states into a consistent flux. That is how FVM captures discontinuities without spurious oscillations. The next chapter develops Godunov, Roe, HLL, and HLLC fluxes — the engines of shock capturing.
