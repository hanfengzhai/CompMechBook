# Navier–Stokes and Computational Fluid Dynamics

Computational fluid dynamics (CFD) solves the Navier–Stokes equations when analytical solutions fail — under nonlinearity, complex geometry, turbulence, or multiphysics coupling. The copper wire heated by current sits in air; the cooling flow determines whether temperature stays below the annealing point. That flow is Navier–Stokes: advection, diffusion, pressure, and possibly turbulence.

Part V built FVM for conservation laws. This chapter adds viscosity, incompressibility, boundary layers, and the practical machinery of production CFD — connecting to the author's [CFD notes](https://hanfengzhai.github.io/file/CFD_note.pdf) and closing the loop toward Part VI's continuum stress and balance language.

## Governing equations

For a Newtonian fluid, the **incompressible Navier–Stokes equations** are

\[
\rho\left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla \mathbf{v}\right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}, \qquad \nabla\cdot\mathbf{v} = 0.
\]

Here \(\mathbf{v}\) is velocity, \(p\) is pressure, \(\mu\) is dynamic viscosity, and \(\mathbf{f}\) is body force (gravity, buoyancy from thermal expansion).

In **conservative form** (compressible formulation), mass, momentum, and energy are conserved quantities with convective and viscous fluxes. The incompressible limit \(\rho = \text{const}\) decouples energy in isothermal flows but retains nonlinear advection.

**Reynolds number** \(\text{Re} = \rho U L / \mu\) measures inertial-to-viscous force ratio. Low Re: laminar, diffusion-dominated. High Re: turbulent, advection-dominated, stiff boundary layers. The copper wire in slow natural convection might be Re \(\sim 10^2\); a jet impinging on it might be Re \(\sim 10^4\)–\(10^5\), demanding turbulence modeling or LES.

## Conservative vector formulation

Production CFD codes often store a **conservative state vector** \(\mathbf{U}\) and flux vectors \(\mathbf{E}, \mathbf{F}, \mathbf{G}\) so that the Navier–Stokes system matches the FVM machinery of Chapters 1–3. In 2D, following the author's [CFD notes](https://hanfengzhai.github.io/file/CFD_note.pdf),

\[
\frac{\partial \mathbf{U}}{\partial t} + \frac{\partial \mathbf{E}}{\partial x} + \frac{\partial \mathbf{F}}{\partial y} = \frac{\partial \mathbf{E}_v}{\partial x} + \frac{\partial \mathbf{F}_v}{\partial y},
\]

with inviscid fluxes

\[
\mathbf{U} = \begin{bmatrix} \rho \\ \rho u \\ \rho v \\ \rho E \end{bmatrix}, \quad
\mathbf{E} = \begin{bmatrix} \rho u \\ \rho u^2 + p \\ \rho u v \\ \rho u H \end{bmatrix}, \quad
\mathbf{F} = \begin{bmatrix} \rho v \\ \rho u v \\ \rho v^2 + p \\ \rho v H \end{bmatrix},
\]

and viscous fluxes \(\mathbf{E}_v, \mathbf{F}_v\) built from stress components \(\sigma_{ij}\) and heat conduction \(-\kappa \partial T / \partial x_i\). For an ideal gas,

\[
p = \rho R T, \qquad \rho H = \rho E + p, \qquad E = \frac{R}{\gamma - 1},
\]

linking pressure, temperature, and total enthalpy \(H\). The inviscid part is hyperbolic — Riemann solvers from Chapter 3 apply face by face; the viscous part is parabolic — centered differences or implicit treatment as in Chapter 2 of Part V.

This split is why CFD is naturally **operator splitting**: advection by upwind FVM, diffusion by implicit FEM-like stencils, pressure by elliptic Poisson. The copper wire's cooling air, discretized on a structured or unstructured mesh, advances \(\mathbf{U}\) with the same conservative update \(\dot{\mathbf{U}}\,\Delta V + \sum_f \mathbf{F}_f \cdot \mathbf{n}_f \,\Delta S_f = 0\) derived in Chapter 1 — only the flux definitions gain viscous and thermal terms.

## Nondimensionalization and similitude

The CFD notes emphasize that **reference scales** must be chosen before writing a solver. Variables are scaled by freestream or far-field values \([\rho]_\infty, [p]_\infty, [T]_\infty, [l]_\infty\), with velocity reference \([u] = \sqrt{[p]/[\rho]}\) (sound speed) and time \([t] = [l]/[u]\). Substituting \(\rho = \rho' [\rho]\), \(u = u' [u]\), etc., into the 1D viscous momentum equation yields

\[
\frac{\partial \rho' u'}{\partial t'} + \frac{M\sqrt{\gamma}}{\text{Re}} \frac{\partial^2 u'}{\partial x'^2} = 0,
\]

where \(\text{Re} = \rho_\infty u_\infty l_\infty / \mu_\infty\) and \(M = u_\infty / c\) is the Mach number. **One equation, two dimensionless groups** — the entire laminar–turbulent and compressible–incompressible landscape is encoded in Re and Ma.

The same scaling philosophy organizes the full system through dimensionless groups:

| Group | Definition | Role |
|-------|------------|------|
| Re | \(\rho U L / \mu\) | Laminar vs. turbulent |
| Ma | \(U / c\) | Compressibility |
| Pr | \(\mu c_p / k\) | Thermal vs. momentum diffusion |
| Gr | \(g \beta \Delta T L^3 / \nu^2\) | Natural convection |

Practical consequences:

- **Magnitude matching**: storing \(\rho \sim 1\) kg/m³ and \(p \sim 10^5\) Pa in the same array without scaling loses floating-point precision; nondimensionalization keeps all primed variables \(\mathcal{O}(1)\).
- **Similitude**: a wind-tunnel experiment matches a full-scale wire in cross-flow when Re, Ma, Pr, and Gr coincide — not when raw velocities match.
- **Code input decks**: OpenFOAM and SU2 expect reference values explicitly; botched unit conversion at this step is the most common multiscale workflow failure (see the prologue on units).

## Finite volume discretization of Navier–Stokes

On a cell-centered FVM mesh:

1. Store \(\mathbf{v}\) and \(p\) (or \(\rho\), \(\mathbf{v}\), \(E\) for compressible).
2. **Convective fluxes**: upwind or Riemann-based (Chapters 2–3) for \(\mathbf{v}\otimes\mathbf{v}\) and energy advection.
3. **Diffusive fluxes**: centered differences for viscous stress \(\boldsymbol{\tau} = 2\mu\mathbf{D}\), heat conduction \(-k\nabla T\).
4. **Pressure–velocity coupling**: enforce \(\nabla\cdot\mathbf{v} = 0\) via fractional-step or coupled solvers.

**Staggered grids** (MAC layout) store normal velocity components at face centers — natural divergence and pressure gradient operators. **Collocated grids** store all variables at cell centers but require **Rhie–Chow interpolation** to avoid checkerboard pressure modes.

## Pressure–velocity splitting: SIMPLE and PISO

Incompressibility is a constraint, not an evolution equation. **Projection methods** advance velocity, then project onto the divergence-free subspace:

**SIMPLE (Semi-Implicit Method for Pressure-Linked Equations)**:

1. Guess pressure \(p^*\).
2. Solve momentum equations for intermediate velocity \(\mathbf{v}^*\) (treating \(p^*\) explicitly).
3. Solve a **Poisson equation** for pressure correction \(p'\): \(\nabla^2 p' = \frac{\rho}{\Delta t}\nabla\cdot\mathbf{v}^*\).
4. Update \(\mathbf{v}^{n+1} = \mathbf{v}^* - \Delta t/\rho\, \nabla p'\), correct pressure.

**PISO** repeats the correction step for tighter coupling within a time step — common in transient flows.

The Poisson solve is elliptic — FEM or multigrid FVM handles it efficiently (Part IV's territory). CFD is inherently **mixed**: hyperbolic advection + elliptic pressure.

## Finite element for Stokes and Navier–Stokes

Part IV's mixed FEM applies directly to **Stokes flow** (\(\mathbf{v}\cdot\nabla\mathbf{v} = 0\)):

Find \((\mathbf{v}, p) \in V \times Q\) such that

\[
\int \mu \nabla \mathbf{v} : \nabla \mathbf{w} - \int p \nabla\cdot\mathbf{w} - \int q \nabla\cdot\mathbf{v} = \int \mathbf{f}\cdot\mathbf{w}
\]

for all \((\mathbf{w}, q)\). **Taylor–Hood** elements (\(P2\) velocity, \(P1\) pressure) satisfy the LBB inf–sup condition from Part III.

For Navier–Stokes, convective term \(\mathbf{v}\cdot\nabla\mathbf{v}\) is handled by Newton linearization or explicit advection. **Stabilized equal-order** elements (SUPG/PSPG) avoid inf–sup restrictions at the cost of user-tuned stabilization parameters.

FEM CFD excels on complex geometries and viscous-dominated flows; FVM CFD excels on high-Re compressible flows with shocks. Modern codes offer both.

## Boundary conditions

| Boundary | Condition | CFD note |
|----------|-----------|----------|
| Inflow | \(\mathbf{v} = \mathbf{v}_{\text{in}}\) or total pressure | Specify turbulence quantities for RANS |
| Outflow | \(\partial \mathbf{v}/\partial n = 0\), \(p = p_{\text{ref}}\) | Convective outflow for vortices leaving domain |
| Wall (no-slip) | \(\mathbf{v} = 0\) | Resolves boundary layer if mesh fine enough |
| Wall (slip) | \(\mathbf{v}\cdot\mathbf{n} = 0\) | Free surfaces, symmetry |
| Symmetry | \(\mathbf{v}\cdot\mathbf{n} = 0\), \(\partial(\mathbf{v}\cdot\mathbf{t})/\partial n = 0\) | Half-domain savings |

The copper wire surface: no-slip on the solid, specified or convective conditions at far-field boundaries for the air domain.

## Turbulence modeling

Direct numerical simulation (DNS) resolves all scales — feasible only at low Re. Engineering CFD uses:

- **RANS** (Reynolds-averaged Navier–Stokes): time-averaged equations with closure models (k–ε, k–ω, SST). Eddy viscosity \(\mu_t\) augments laminar viscosity.
- **LES** (large eddy simulation): resolves large eddies, models subgrid stress. Expensive but more accurate for unsteady separation.
- **DNS**: no model; grid must resolve Kolmogorov scale — research tool.

Turbulence models add transport equations for \(k\), \(\varepsilon\), or \(\omega\), discretized by the same FVM machinery as momentum.

## Heat transfer and buoyancy

Coupled energy equation:

\[
\rho c_p\left(\frac{\partial T}{\partial t} + \mathbf{v}\cdot\nabla T\right) = \nabla\cdot(k\nabla T) + \Phi,
\]

where \(\Phi\) is viscous dissipation. **Boussinesq approximation** for natural convection: density varies only in buoyancy term, \(\mathbf{f} = \rho_0 \mathbf{g} \beta (T - T_0)\).

Thermoelastic coupling on the copper wire: CFD supplies surface heat flux; FEM solves thermal stress (Part IV, Chapter 4). Monolithic or partitioned coupling exchanges boundary data each time step or iteration.

## Verification and validation

The CFD notes distinguish:

**Verification** — Is the code solving the equations correctly?

- Method of manufactured solutions (MMS): insert a source term so a known \(\mathbf{v}\) is exact.
- Grid convergence study: refine mesh; check that error decreases at expected rate in smooth regions.
- Conservation checks: mass flux in equals mass flux out at steady state.

**Validation** — Does the model match reality?

- Benchmark cases: lid-driven cavity, backward-facing step, flat-plate boundary layer.
- Experimental data: PIV velocity fields, pressure taps, heat transfer coefficients.

Both are necessary. A converged simulation of the wrong equations — wrong turbulence model, wrong boundary condition — is worthless.

## From shock tubes to cosmological hydrodynamics

The same FVM kernel that passes Sod's shock tube scales to problems with vastly larger domains. The **Illustris** and **IllustrisTNG** cosmological simulations solve magnetohydrodynamics on moving Voronoi meshes with second-order finite-volume discretization — storing volume-averaged \(\rho\), \(\mathbf{u}\), and magnetic field at cell centers, as described in the author's FVM notes. The update for a primitive variable \(\phi \in \{\rho, \mathbf{u}, p\}\) at second order takes the schematic form

\[
\phi^{n+1} = \phi^n - \tfrac{1}{2}\Delta t\left(\phi^n \nabla\cdot\mathbf{u} + \mathbf{u}\cdot\nabla\phi^n\right),
\]

with analogous pressure and momentum terms. The copper wire's cooling jet and a galaxy cluster's intracluster medium share the same conservation structure; only the Reynolds number, geometry, and closure models change. Passing Sod on a 200-cell grid is the sanity check before trusting any of it.

## Software landscape

Open-source: **OpenFOAM** (FVM, C++), **SU2** (FVM, adjoints), **FEniCS/Firedrake** (FEM, Stokes/Navier–Stokes). Commercial: Fluent, STAR-CCM+, COMSOL. Choice depends on physics (compressible vs. incompressible), geometry, HPC needs, and coupling to structural FEM for the wire problem.

## Connection to Parts I–III and Part VI

- Part I: discrete systems from FVM are sparse ODEs; pressure Poisson is a sparse linear system.
- Part II: weak form of Stokes connects FEM CFD to Hilbert space theory.
- Part III: mixed formulations, LBB stability, energy methods for parabolic energy decay.
- Part VI: Cauchy stress, rate of deformation \(\mathbf{D}\), and balance laws are the continuum objects that Navier–Stokes discretizes.

Fluids and solids share conservation of mass and momentum; they differ in constitutive response — \(\boldsymbol{\tau} = 2\mu\mathbf{D}\) for Newtonian fluids vs. \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) for linear elastic solids.

## A copper-wire cooling scenario

Picture the heated copper wire in cross-flow air. A minimal CFD setup requires:

1. **Fluid domain**: channel or external flow with far-field boundaries.
2. **Solid domain** (optional conjugate heat transfer): wire mesh with conduction, coupled to fluid via interface heat flux continuity.
3. **No-slip** on the wire surface; **inflow** temperature and velocity specified upstream.
4. **Re** based on wire diameter sets laminar vs. turbulent regime; natural convection adds Grashof number via Boussinesq buoyancy if the wire is hot enough.

Steady RANS with a k–ω SST model might suffice for engineering heat transfer coefficients. LES resolves vortex shedding behind the wire at higher cost. FEM conduction in the wire (Part IV) plus FVM convection in the air (Part V) exchanges wall heat flux each iteration — the multiphysics loop the book's ladder is built to support.

## Bridge to Part VI

Part V discretized conservation on control volumes for fluids. Part VI develops the **kinematics and stress measures** that both FEM solid codes and FVM fluid codes ultimately approximate — deformation gradient and strain for solids, rate of deformation for fluids, Cauchy stress and balance laws for both. The copper wire under tension and the air cooling it are one multiphysics story told in two discretization languages; Part VI supplies the shared continuum vocabulary.
