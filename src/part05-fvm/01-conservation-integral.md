# Integral Forms of Conservation Laws

[IV.5](../fem/chapters/05-convergence.md) closed Part IV with Céa's lemma — proof that the Galerkin mesh converges to the weak solution Part II promised — and offered **Door A** to this part: when the thermocouple climbs and Robin fluxes at the wire surface feel like placeholders, the surrounding air needs its own discretization. Part IV meshed conduction **inside** the solid; Part V begins **outside** it, with a different philosophy that respects the same physics.

Where FEM whispers "multiply by a test function and integrate by parts," FVM declares "integrate the conservation law over a control volume and balance fluxes." Both respect the same physics; the bookkeeping differs. Part III wrote PDEs in strong form; Part IV discretized elliptic operators with trial functions. Part V begins with the form that hyperbolic and conservation-law physics prefer: **integral balance** on control volumes.

The copper wire reappears in a different guise. Solid mechanics on the wire still favors FEM, but imagine air cooling the heated specimen, or a shock tube test validating a CFD code before it simulates that cooling jet. Those flows are governed by conservation of mass, momentum, and energy — laws that make sense even when the pointwise PDE breaks down at shocks.

## Story so far (Parts I–IV)

| Stage | What the wire became | Key object |
|-------|----------------------|------------|
| Parts I–III | Weak forms; \(H^1\) fields; strong-form PDEs | Elliptic operators on the solid |
| Part IV | Galerkin assembly; \(\mathbf{K}\mathbf{U}=\mathbf{F}\); Céa convergence | FEM inside the copper wire |
| **V.1 (here)** | Integral balance on control volumes | Conservation contract for the fluid side |

Part IV meshed conduction **inside** the solid; this chapter states the **conservation contract** for the air **outside** it — what enters a control volume must equal what leaves plus what accumulates. The [prologue](../../prologue/00-many-scales.md) **Act II — Warming** showed the wire surface running hot; conjugate heat transfer in [V.4](04-navier-stokes-cfd.md) will handshake FEM temperature fields with FVM enthalpy fluxes named here.

## Scene: air leaving the wire

The thermal camera from Part III showed the wire hot; now widen the frame. Still air in the lab carries heat away from the surface by natural convection — no fan, just buoyancy-driven flow. A CFD practitioner does not start by writing Navier–Stokes at a single point in the room. She tiles the air volume into control volumes, each a small box surrounding a node, and asks a bookkeeping question: **how much enthalpy flows in through each face, and how much flows out?**

For the cell glued to the wire surface, one face exchanges heat with the solid; the others exchange with neighboring air cells. In steady state, the sum of convective fluxes through all faces balances the heat conducted from the copper. No shape functions, no weak form of the wire's displacement — only **flux balance on volumes**. That is the finite volume instinct: conservation first, pointwise PDE second.

When the operator later turns on a fan, the same grid may capture a turbulent wake; the fluxes become numerically approximated Riemann problems rather than laminar gradients. Part V builds from this scene — integral balance on cells — through one-dimensional prototypes to Navier–Stokes and conjugate heat transfer with the wire from Part IV.

## From strong form to integral form

Consider a conserved scalar or vector quantity \(U(\mathbf{x}, t)\) with flux \(\mathbf{F}(U)\) and source \(S\). The strong-form conservation law is

\[
\frac{\partial U}{\partial t} + \nabla\cdot \mathbf{F}(U) = S \quad \text{in } \Omega.
\]

Integrate over a fixed control volume \(\Omega_i \subset \Omega\) and apply the divergence theorem:

\[
\frac{d}{dt}\int_{\Omega_i} U \, dV + \oint_{\partial \Omega_i} \mathbf{F}(U)\cdot\mathbf{n} \, dS = \int_{\Omega_i} S \, dV.
\]

In **steady state** with no sources, net flux through the boundary vanishes:

\[
\oint_{\partial \Omega_i} \mathbf{F}\cdot\mathbf{n} \, dS = 0.
\]

This statement is **exact** for any control volume — it requires only that the integral form of the PDE holds in a weak (distributional) sense. Discontinuities in \(U\) across a shock surface do not invalidate the balance; they constrain the Rankine–Hugoniot jump conditions that the flux must satisfy.

## Why integral form matters for computation

Strong-form finite differences approximate derivatives at points. At a shock, derivatives are distributions, not grid-sized numbers. Central differencing produces Gibbs oscillations; upwinding fixes stability but must be designed carefully.

Finite volume methods never form \(\partial \mathbf{F}/\partial x\) at a face. They store **cell averages** and compute **numerical fluxes** at interfaces such that the discrete update mimics the integral balance. Conservation is **built in** — not an accident of a stable scheme.

Part I's telescoping sums reappear: if fluxes at shared faces are equal and opposite for adjacent cells, summing the semi-discrete equations over the domain eliminates interior fluxes and yields global conservation.

## 1D conservation law template

In one space dimension, control volumes are intervals \([x_{j-1/2}, x_{j+1/2}]\) of width \(\Delta x_j\). The integral form becomes

\[
\frac{d}{dt}\int_{x_{j-1/2}}^{x_{j+1/2}} U\, dx + F(U)\big|_{x_{j+1/2}} - F(U)\big|_{x_{j-1/2}} = \int_{x_{j-1/2}}^{x_{j+1/2}} S\, dx.
\]

Define the **cell average** \(\bar{U}_j = \frac{1}{\Delta x_j}\int_{x_{j-1/2}}^{x_{j+1/2}} U\, dx\). Dividing by \(\Delta x_j\):

\[
\frac{d\bar{U}_j}{dt} + \frac{F_{j+1/2} - F_{j-1/2}}{\Delta x_j} = \bar{S}_j.
\]

Face fluxes \(F_{j+1/2}\) must be computed from neighboring cell data — the central design problem of FVM, treated in Chapters 2 and 3.

## The 1D Euler equations

Compressible inviscid flow in 1D is the canonical nonlinear system. Conserved variables are

\[
\mathbf{U} = \begin{bmatrix} \rho \\ \rho u \\ \rho E \end{bmatrix},
\]

where \(\rho\) is density, \(u\) is velocity, and \(E = e + u^2/2\) is specific total energy (\(e\) = internal energy). Fluxes are

\[
\mathbf{F}(\mathbf{U}) = \begin{bmatrix} \rho u \\ \rho u^2 + p \\ (\rho E + p) u \end{bmatrix}.
\]

Pressure closes the system via an **equation of state** — for ideal gas, \(p = (\gamma - 1)\rho e\) with \(\gamma = 1.4\) for air.

The PDE \(\partial \mathbf{U}/\partial t + \partial \mathbf{F}/\partial x = 0\) integrates to flux balance on each cell. **Shocks**, **contact discontinuities**, and **rarefaction waves** are weak solutions: the integral form holds everywhere, but classical derivatives do not exist on the shock surface.

The author's [FVM notes](https://hanfengzhai.github.io/file/FVM_note.pdf) develop this system as the entry point to shock capturing — the CFD counterpart of patch tests in FEM.

## Connection to Part III

Part III classified PDEs by character:

| Type | Prototype | Natural discretization |
|------|-----------|------------------------|
| Elliptic | \(-\Delta u = f\) | FEM (Part IV) |
| Parabolic | \(u_t - \Delta u = f\) | FEM + time stepping |
| Hyperbolic | \(U_t + F(U)_x = 0\) | FVM, DG, upwind schemes |

Real applications mix types. **Navier–Stokes** (Chapter 4) couples hyperbolic advection with parabolic diffusion and an elliptic pressure field. **Thermoelasticity** couples elliptic solids with parabolic heat. The integral form handles the hyperbolic piece; FEM or FVM handles the rest.

## FEM vs FVM: complementary philosophies

| Aspect | FEM (elliptic focus) | FVM (hyperbolic focus) |
|--------|---------------------|------------------------|
| Primary unknown | Field in trial space | Cell averages (or point values) |
| Local coupling | Stiffness matrix entries | Flux through faces |
| Natural BCs | Essential/natural split from weak form | Flux specification at boundaries |
| Shock handling | Less natural (unless DG) | Riemann solvers at faces |
| Conservation | Not automatic for Galerkin | Automatic by construction |
| Mesh | Unstructured triangles/tets common | Structured/unstructured; face topology |

Many production **CFD codes** (OpenFOAM, STAR-CCM+, Fluent's finite-volume core) are FVM or flux-difference schemes. Many **solid mechanics codes** (Abaqus, CalculiX) are FEM. **Fluid–structure interaction** couples the two at interfaces: FEM supplies structural displacement; FVM supplies fluid traction on the wetted surface.

## Boundary conditions in integral form

At a domain boundary, the integral balance exposes fluxes directly:

- **Inflow**: specify \(\mathbf{F}\cdot\mathbf{n}\) or characteristic variables entering the domain.
- **Outflow**: specify pressure or use zero-gradient extrapolation.
- **Wall**: no-penetration fixes normal velocity; no-slip fixes tangential velocity (viscous case).

Essential conditions in FEM become flux or state constraints in FVM. The copper wire's surface in a cooling-flow simulation might use no-slip on the solid boundary and specified inlet velocity for the air stream.

## Applications across scales

Finite volume ideas appear far beyond shock tubes:

- **Geophysics**: ocean circulation, tsunami propagation — conservation of mass and momentum on spherical or Cartesian grids.
- **Thermal hydraulics**: nuclear reactor core cooling — integral heat and mass balances on subchannel volumes.
- **Mantle convection**: planetary-scale Stokes flow with advection of temperature — FVM or staggered-grid FDM on spherical shells.
- **Astrophysics**: cosmological hydrodynamics (Illustris/TNG simulations mentioned in the FVM notes) — conservation on adaptive octree meshes.

The method is **scale-agnostic** because conservation is scale-agnostic. The same flux-differencing logic applies to a 1D Sod shock tube and a billion-cell galaxy formation run — only the Riemann solver complexity and parallel mesh infrastructure change.

## Linear advection as the simplest conservation law

Before Euler, consider \(U_t + a U_x = 0\) with constant speed \(a\). Here \(\mathbf{F}(U) = aU\). The integral update is

\[
\frac{d\bar{U}_j}{dt} + a \frac{U_{j+1/2} - U_{j-1/2}}{\Delta x} = 0.
\]

Choosing the face value from the upwind side ( \(U_{j-1/2} = U_j\) if \(a > 0\) ) yields a stable scheme under CFL \(|a|\Delta t / \Delta x \le 1\). Central differencing of face values is unstable — energy grows instead of advecting. This instability foreshadows the need for **upwind bias** and **Riemann fluxes** in nonlinear systems.

## Weak solutions and Rankine–Hugoniot conditions

A shock at speed \(s\) satisfies

\[
s \llbracket U \rrbracket = \llbracket F(U) \rrbracket,
\]

where \(\llbracket \cdot \rrbracket\) denotes the jump across the shock. Numerical fluxes that satisfy a discrete version of this condition **converge to weak solutions** as \(\Delta x \to 0\). Entropy conditions select the physically correct weak solution among many mathematical possibilities.

## Discrete vs. continuous conservation

Galerkin FEM for advection does not automatically conserve mass or energy at the discrete level unless the formulation is carefully constructed (e.g., conservative DG, skew-symmetric splitting). FVM builds conservation into the face-flux definition. For long-time integration of climate, astrophysics, or reacting flows, discrete conservation prevents slow drift in total mass or energy that can accumulate over millions of time steps.

The tradeoff: first-order FVM is robust but dissipative; high-order FVM with limiters is sharper but more complex. Part IV's FEM excels where symmetry and energy minimization dominate; Part V's FVM excels where flux balance and shock stability dominate.

## From shock tubes to cosmological volumes

The same integral-balance philosophy scales from homework shock tubes to galaxy formation. The author's [FVM notes](https://hanfengzhai.github.io/note/FVM.pdf) close with the **Illustris–TNG** project, where the moving-mesh code **Arepo** solves (magneto)hydrodynamics on a Voronoi tessellation of space. Cell-centered volume averages of density \(\rho\), velocity \(\mathbf{u}\), and magnetic field \(\mathbf{B}\) evolve by finite-volume fluxes; second-order accuracy in time uses a predictor–corrector structure analogous to MUSCL in space:

\[
\rho^{n+1} = \rho^n - \tfrac{1}{2}\Delta t\,(\rho^n \nabla\cdot\mathbf{u} + \mathbf{u}\cdot\nabla\rho^n), \qquad
\mathbf{u}^{n+1} = \mathbf{u}^n - \tfrac{1}{2}\Delta t\left(\mathbf{u}^n\nabla\cdot\mathbf{u}^n + \frac{1}{\rho}\nabla p^n\right),
\]

with a matching update for pressure from the ideal-gas law. The schematic is unchanged from the 1D bar in Chapter 2: store cell averages, compute face fluxes, advance conservatively. Only the mesh moves with the flow, refining resolution where gravity collapses gas into galaxies.

For the copper wire, Illustris is irrelevant numerically — but intellectually it matters. **Conservation on control volumes** is not a trick for Sod problems; it is the discretization contract trusted when integrating hydrodynamics over billions of years or cooling air around a heated conductor. Once the integral form is internalized, reading Arepo's documentation or an OpenFOAM manual is recognition, not reinvention.

## Control volumes in 2D and 3D

In 2D, control volumes are polygonal cells; in 3D, polyhedral cells (hexes, tets, general polyhedra in OpenFOAM). The integral balance reads

\[
\frac{d}{dt}\int_{\Omega_i} U\, dV + \sum_{f \in \partial\Omega_i} F_f A_f = \int_{\Omega_i} S\, dV,
\]

where the sum is over faces \(f\) with area \(A_f\) and outward normal. Unstructured FVM stores face–cell connectivity and face normals; the 1D flux-difference logic is unchanged — only geometry bookkeeping grows. A triangular mesh around the copper wire in cross-flow uses the same conservation statement as the 1D shock tube, with face fluxes computed along each edge normal.

## Bridge

Discretizing the integral form on a 1D grid yields the classic FVM update: cell averages change by net flux through faces. The next chapter writes that algorithm explicitly — semi-discrete form, time stepping, CFL stability, and the conservative property that makes global balances exact on any mesh.

| What the integral form established | What [V.2](02-fvm-1d.md) must implement |
|------------------------------------|------------------------------------------|
| \(\frac{d}{dt}\int_{\Omega_i} U\, dV + \oint_{\partial\Omega_i} \mathbf{F}\cdot\mathbf{n}\, dS = 0\) | Semi-discrete flux difference on a 1D grid |
| Rankine–Hugoniot jump conditions for shocks | Numerical flux functions at cell interfaces |
| Discrete conservation vs. Galerkin drift | Exact global balance of mass/energy on any mesh |
| Same contract from shock tubes to Illustris | CFL stability and time marching for the wire's boundary layer |

Return to the prologue's **Act II — Warming**: current switched on, the wire surface runs hot, and air carries heat away by convection. Part IV computed conduction inside the solid from weak forms; this chapter states the **conservation contract** for the fluid side — what enters a control volume must equal what leaves plus what accumulates. [V.2](02-fvm-1d.md) is where that contract becomes an update loop the conjugate heat-transfer scene in [V.4](04-navier-stokes-cfd.md) will handshake with FEM temperature fields.

Part III's weak forms minimized energy on trial spaces; FVM **balances fluxes** on control volumes — the discretization philosophy Part IV's elliptic FEM does not automatically guarantee for advection.

| Prologue act | Conservation object on the wire | FEM partner at the interface | Proof style |
|--------------|--------------------------------|------------------------------|-------------|
| II — Warming | Enthalpy flux from air to wire surface | FEM Robin BC / wall temperature handshake | Céa energy norm (Part IV) + exact flux balance (Part V) |
| III — Pulling (preview) | Momentum flux in cooling jet | Solid traction BC from Part IV | Shared \(\boldsymbol{\sigma}\mathbf{n}\) in Part VI |
| V — Notch (preview) | Shock-capturing if flow separates | Stress concentrator in solid mesh | Limiters + CFL, not finer \(\Delta x\) alone |
| VI — Foundation (preview) | Same integral contract from shock tubes to CFD | Shared \(\boldsymbol{\sigma}\mathbf{n}\) language in Part VI | Conservation as multiscale handshake habit |

| Part IV FEM artifact | Part V FVM counterpart | Interface handshake |
|---------------------|------------------------|---------------------|
| Nodal temperature \(T_i\) | Cell-average enthalpy \(\bar{h}_j\) | Wall Robin BC / flux matching |
| \(\mathbf{K}_T \mathbf{T}=\mathbf{q}\) | Face flux sum \(\sum_f F_f A_f\) | Conjugate heat transfer loop |
| Energy norm convergence (Céa) | Discrete conservation + CFL stability | Same wire, complementary proofs |

Turn the page when the integral balance is clear but no cell-averaged update exists yet — that is the signal that conservation wants a mesh of volumes, not a mesh of trial functions.
