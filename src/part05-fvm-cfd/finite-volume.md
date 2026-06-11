# Finite volume method

## Cell averages

Partition the domain into cells \([x_{j-1/2}, x_{j+1/2}]\) of width \(\Delta x\). Define cell-average solution

\[
U_j^n \approx \frac{1}{\Delta x}\int_{x_{j-1/2}}^{x_{j+1/2}} U(x, t^n)\, dx.
\]

Integrate conservation law over cell \([j]\) and time step \([t^n, t^{n+1}]\):

\[
U_j^{n+1} = U_j^n - \frac{\Delta t}{\Delta x}\left(F_{j+1/2}^{n+1/2} - F_{j-1/2}^{n+1/2}\right).
\]

**Design problem:** choose numerical flux \(F_{j+1/2}\) consistently and stably.

## Godunov-type fluxes

**Upwind:** use flux from the side from which characteristics enter.

**Lax–Friedrichs:**

\[
F_{j+1/2} = \tfrac{1}{2}\left(F(U_R) + F(U_L)\right) - \tfrac{c}{2}(U_R - U_L),
\]

with wave speed estimate \(c\).

## Shock tube problem

The author's FVM presentation (Nov. 2020) uses the **Sod shock tube** as a canonical test: initial discontinuity separates high-pressure and low-pressure regions; Euler dynamics produce shock, contact, and rarefaction fan.

FVM captures shocks without oscillations when fluxes respect upwinding and CFL stability:

\[
\Delta t \le C \frac{\Delta x}{|u| + c_s},
\]

with sound speed \(c_s\).

## Illustris & TNG connection

The same presentation references large cosmological hydrodynamic simulations (Illustris, TNG)—reminders that FVM at scale couples gravity, star formation, and MHD on adaptive meshes. The classroom shock tube is the seed of galaxy formation codes.

## Comparison with FEM

| Aspect | FEM | FVM |
|--------|-----|-----|
| Natural form | variational / Galerkin | integral conservation |
| Shock handling | stabilization / DG | upwind fluxes |
| Mesh | often unstructured | often structured / AMR |

**Discontinuous Galerkin (DG)** hybrids combine FEM bases with FVM-like numerical fluxes—bridging Parts IV and V.

## Artificial dissipation and boundary conditions

The author's CFD note series covers **artificial dissipation** (stabilizing central schemes), **boundary conditions** (inflow, outflow, walls), and **mesh transformation**—practical layers atop the mathematical core.

<div class="bridge">

**Bridge.** FVM discretizes conservation; **CFD** is the full workflow for Navier–Stokes at engineering complexity.

</div>
