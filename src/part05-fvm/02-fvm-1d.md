# The Finite Volume Method in One Dimension

FVM replaces continuous averages with cell averages and face fluxes with numerical flux functions. The 1D algorithm is clean enough to implement in an afternoon and rich enough to capture shocks.

## Cell averages

Partition \([x_{\min}, x_{\max}]\) into cells of width \(\Delta x_j\). Define the cell average at time \(t_n\):

\[
U_j^n \approx \frac{1}{\Delta x_j}\int_{x_{j-1/2}}^{x_{j+1/2}} U(x, t_n)\, dx.
\]

Integrating the conservation law over cell \(j\) and dividing by \(\Delta x_j\):

\[
\frac{U_j^{n+1} - U_j^n}{\Delta t} + \frac{F_{j+1/2} - F_{j-1/2}}{\Delta x_j} = 0.
\]

**Face fluxes** \(F_{j+1/2}\) must be computed from neighboring cell values — this is where the physics and numerics meet.

## The semi-discrete form

\[
\frac{d U_j}{dt} = -\frac{F_{j+1/2} - F_{j-1/2}}{\Delta x_j}.
\]

Time discretization (forward Euler, Runge–Kutta, implicit schemes) completes the method. Stability constraints link \(\Delta t\) and \(\Delta x\) through the spectrum of the semi-discrete flux Jacobian — the CFL condition.

## Consistency and conservation

A numerical flux \(\mathcal{F}(U_j, U_{j+1})\) is **consistent** if \(\mathcal{F}(U, U) = F(U)\). The semi-discrete scheme is **conservative** if fluxes at \(j+1/2\) are shared between cells \(j\) and \(j+1\) with opposite signs — global conservation follows by telescoping sums.

## Linear advection as sanity check

For \(U_t + a U_x = 0\), upwind flux

\[
F_{j+1/2} = a U_j \quad (a > 0)
\]

is stable under CFL \(|a|\Delta t / \Delta x \le 1\). Central differencing is unstable for pure advection — energy grows instead of advecting. Upwinding introduces numerical diffusion; higher-order schemes (MUSCL, WENO) reduce it.

## Bridge

Nonlinear systems require **Riemann solvers** at faces — exact or approximate solutions to local shock-tube problems. That is how FVM captures discontinuities without oscillations.
