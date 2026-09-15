# Navier–Stokes and Computational Fluid Dynamics

Computational fluid dynamics (CFD) solves the Navier–Stokes equations when analytical solutions fail — under nonlinearity, complex geometry, turbulence, or multiphysics coupling. The copper wire heated by current sits in air; the cooling flow determines whether temperature stays below the annealing point. That flow is Navier–Stokes: advection, diffusion, pressure, and possibly turbulence.

Part V built FVM for conservation laws. This chapter adds viscosity, incompressibility, boundary layers, and the practical machinery of production CFD — connecting to the author's [CFD notes](https://hanfengzhai.github.io/file/CFD_note.pdf) and closing the loop toward Part VI's continuum stress and balance language.

## Scene: air decides the wire's fate

Heat the copper wire until it glows softly; air above it rises, pulling cooler flow across the surface. That convection sets whether the mid-span temperature stays below annealing range. Navier–Stokes is the PDE for that air — advection, viscous diffusion, pressure coupling. Part V built conservation on cells; this chapter adds viscosity, Reynolds number, turbulence models, and the practical CFD workflow that connects a wire thermal model to the fluid domain around it.

## Governing equations

For a Newtonian fluid, the **incompressible Navier–Stokes equations** are

\[
\rho\left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla \mathbf{v}\right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}, \qquad \nabla\cdot\mathbf{v} = 0.
\]

Here \(\mathbf{v}\) is velocity, \(p\) is pressure, \(\mu\) is dynamic viscosity, and \(\mathbf{f}\) is body force (gravity, buoyancy from thermal expansion).

In **conservative form** (compressible formulation), mass, momentum, and energy are conserved quantities with convective and viscous fluxes. The incompressible limit \(\rho = \text{const}\) decouples energy in isothermal flows but retains nonlinear advection.

**Reynolds number** \(\text{Re} = \rho U L / \mu\) measures inertial-to-viscous force ratio. Low Re: laminar, diffusion-dominated. High Re: turbulent, advection-dominated, stiff boundary layers. The copper wire in slow natural convection might be Re \(\sim 10^2\); a jet impinging on it might be Re \(\sim 10^4\)–\(10^5\), demanding turbulence modeling or LES.

## Nondimensional groups and similitude

CFD notes emphasize nondimensionalization:

| Group | Definition | Role |
|-------|------------|------|
| Re | \(\rho U L / \mu\) | Laminar vs. turbulent |
| Ma | \(U / c\) | Compressibility |
| Pr | \(\mu c_p / k\) | Thermal vs. momentum diffusion |
| Gr | \(g \beta \Delta T L^3 / \nu^2\) | Natural convection |

Matching similitude groups links experiments to simulations — wind tunnel to full scale, water table to flight.

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

## Multiphysics scene: conjugate heat transfer

Parts IV and V use different discretizations, but the copper wire under current is **one coupled boundary-value problem** split across domains. The solid solves steady conduction; the fluid solves convection with a no-slip wall whose temperature is unknown until both sides agree on heat flux.

**Solid (FEM, Part IV).** On the wire mesh \(\Omega_s\), find temperature \(T_s\) such that

\[
\int_{\Omega_s} k \nabla T_s \cdot \nabla v \, d\Omega + \int_{\Gamma_w} q_w \, v \, dS = \int_{\Omega_s} \dot{q}_{\text{Joule}} \, v \, d\Omega
\]

for all test functions \(v \in H^1(\Omega_s)\). Here \(\dot{q}_{\text{Joule}} = \sigma_e |\mathbf{J}|^2\) is volumetric heating from electrical current, and \(q_w\) is the unknown wall heat flux at the fluid interface \(\Gamma_w\).

**Fluid (FVM, Part V).** In the air domain \(\Omega_f\), steady incompressible flow with energy equation gives cell-averaged \(T_f\) and velocity \(\mathbf{u}\). At the wire surface,

\[
-k \left.\frac{\partial T_s}{\partial n}\right|_{\Gamma_w} = q_w = h\,(T_w - T_\infty) \quad\text{or}\quad q_w = -k_f \left.\frac{\partial T_f}{\partial n}\right|_{\Gamma_w},
\]

with \(T_w = T_s|_{\Gamma_w} = T_f|_{\Gamma_w}\) enforced by **interface coupling**.

**Partitioned coupling loop** (the story both codes tell together):

1. Guess wall temperature \(T_w^{(0)}\) (or flux \(q_w^{(0)}\)).
2. **Fluid step:** solve Navier–Stokes + energy with fixed \(T_w\); extract \(q_w^{(k)} = -k_f \partial T_f / \partial n\).
3. **Solid step:** solve conduction with Neumann data \(q_w^{(k)}\) on \(\Gamma_w\); read updated \(T_w^{(k+1)} = T_s|_{\Gamma_w}\).
4. Repeat until \(|T_w^{(k+1)} - T_w^{(k)}| < \varepsilon\) — a **fixed-point iteration** between sparse linear systems (solid) and nonlinear FVM updates (fluid).

This is not a third method. It is Part IV and Part V **speaking at an interface** — the same weak-form / flux-balance pattern the epilogue later generalizes to DFT→MD→DDD→FEM chains. When the wire runs hot enough to soften, add thermal strain \(\alpha\Delta T\) in the solid weak form (Part VI); when Reynolds number exceeds the laminar regime, swap the RANS closure on the fluid side. The coupling skeleton stays.

### Worked example: Picard iterations on a lumped wire

Strip the full Navier–Stokes mesh for a moment and model the **1 mm copper wire** from Act II as a lumped solid with a single unknown surface temperature \(T_w\). Joule heating holds the volume-averaged core at \(T_{\text{core}} = 400\,\text{K}\); conduction through a thin oxide or varnish layer supplies thermal resistance \(R_s = 5\,\text{K/W}\) from core to wall; natural convection supplies \(hA = 0.05\,\text{W/K}\) (with \(h \approx 20\,\text{W/m}^2\text{K}\) and surface area \(A \approx 2.5 \times 10^{-3}\,\text{m}^2\) on a 10 cm segment).

The partitioned loop reduces to alternating:

\[
q_w^{(k)} = \frac{T_{\text{core}} - T_w^{(k)}}{R_s}, \qquad
T_w^{\text{new}} = T_\infty + \frac{q_w^{(k)}}{hA},
\]

with \(T_\infty = 300\,\text{K}\). At convergence, \(q_w = (T_{\text{core}} - T_w)/R_s = hA\,(T_w - T_\infty)\), giving the exact solution \(T_w = 380\,\text{K}\), \(q_w = 4\,\text{W}\).

Raw Picard iteration **oscillates** when \(R_s hA\) is stiff. Production codes add **under-relaxation** \(\omega \in (0,1]\):

\[
T_w^{(k+1)} = (1-\omega)\, T_w^{(k)} + \omega \, T_w^{\text{new}}.
\]

With \(\omega = 0.3\) and initial guess \(T_w^{(0)} = 350\,\text{K}\):

| Iteration \(k\) | \(T_w^{(k)}\) [K] | \(q_w^{(k)}\) [W] | \(T_w^{\text{new}}\) [K] | Under-relaxed \(T_w^{(k+1)}\) [K] |
|-----------------|-------------------|-------------------|--------------------------|-----------------------------------|
| 0 | 350 | 10.0 | 500 | 395 |
| 1 | 395 | 1.0 | 320 | 373 |
| 2 | 373 | 5.5 | 410 | 384 |
| 3 | 384 | 3.3 | 365 | 378 |
| 4 | 378 | 4.4 | 388 | 381 |
| 5 | 381 | 3.8 | 376 | 380 |
| 6 | 380 | 4.1 | 382 | **380** (converged) |

The lesson transfers directly to production coupling: Part IV's solid solve and Part V's fluid solve are two black boxes exchanging \((T_w, q_w)\); convergence is a fixed-point problem, not a finer mesh. Before trusting Act II's thermocouple reading, verify **energy balance** — integrated Joule input \(\dot{Q}_{\text{Joule}} \approx \int_{\Gamma_w} q_w \, dS\) at the converged row — not merely that each solver converges internally.

## Lab act: natural convection Nusselt number on the heated wire (Act II — Warming)

**Act II** heats the wire until air above it rises. Navier–Stokes plus the energy equation determines whether convection or conduction dominates cooling — and whether the mid-span temperature stays below annealing range before **Act III** ramps load.

Set up a **minimal conjugate heat transfer** problem (no commercial code required for the estimate):

| Parameter | Value | Role |
|-----------|-------|------|
| Wire diameter \(d\) | 1 mm | Length scale \(L\) |
| Wire surface \(T_w\) | 400 K | Hot wall (post-Joule heating) |
| Ambient \(T_\infty\) | 300 K | Far-field air |
| Air properties at 350 K | \(\nu \approx 2.2 \times 10^{-5}\,\text{m}^2/\text{s}\), \(\alpha \approx 3.0 \times 10^{-5}\,\text{m}^2/\text{s}\) | Kinematic viscosity, thermal diffusivity |
| Grashof number | \(\text{Gr} = g \beta \Delta T d^3 / \nu^2 \approx 10^4\) | Natural convection regime |
| Rayleigh number | \(\text{Ra} = \text{Gr} \cdot \text{Pr} \approx 7 \times 10^3\) | Laminar vertical-cylinder correlation applies |

For a vertical cylinder in natural convection, a textbook correlation gives \(\text{Nu}_d = h d / k \approx 0.6\,\text{Ra}_d^{1/4}\) in the laminar range. With \(\text{Ra}_d \sim 10^3\), \(\text{Nu}_d \sim 5\)–\(10\), so \(h \sim 10\)–\(30\,\text{W/m}^2\text{K}\).

**Partitioned coupling checklist** (matches the multiphysics scene above):

1. **Solid FEM:** solve \(-k T'' = q(x)\) with Neumann flux \(q_w = h(T_w - T_\infty)\) on the surface — the wall heat flux the fluid demands.
2. **Fluid estimate:** compute \(\text{Nu}\) from \(\text{Ra}\); update \(h\); repeat until \(T_w\) is consistent.
3. **Sanity check:** compare total heat out \(\int q_w \, dS\) to integrated Joule input \(\int q \, dV\) at steady state — conservation, not grid convergence alone.

If \(\text{Re} > 10^5\) (forced cross-flow over the wire), swap the natural-convection correlation for a cylinder cross-flow \(\text{Nu}(\text{Re}, \text{Pr})\) and note when RANS replaces laminar estimates. Part IV's wire mesh and Part V's air domain share one interface temperature; this Lab act is the hand calculation that tells you whether cooling is fast enough before the load cell ramps in Act III.

### Lab act extension: two-domain Picard loop with a 1D FEM solid

The Nusselt estimate above certifies **fluid-side physics**. Production conjugate heat transfer alternates a **solid conduction solve** (Part IV) with a **fluid energy + momentum solve** (Part V). Strip the geometry to a 1D radial model through the wire cross-section plus a lumped fluid film — enough to practice the **fixed-point loop** before OpenFOAM or ANSYS coupling.

**Geometry and material (Act II segment, 10 cm length).**

| Domain | Model | Key data |
|--------|-------|----------|
| Solid (Cu) | 1D radial conduction, \(k = 390\,\text{W/m·K}\), \(r_i = 0\), \(r_o = 0.5\,\text{mm}\) | Volumetric Joule heat \(\dot{q} = 10^8\,\text{W/m}^3\) (uniform) |
| Fluid film | Lumped convection on \(r = r_o\) | \(h\) from \(\text{Nu}_d\) table above, \(T_\infty = 300\,\text{K}\) |
| Interface \(\Gamma_w\) | \(r = r_o\) | Unknown \(T_w\); flux \(q_w = h(T_w - T_\infty)\) |

**Solid FEM (Part IV pattern).** Weak form on \([r_i, r_o]\): find \(T \in H^1\) such that

\[
\int_{r_i}^{r_o} k \frac{dT}{dr} \frac{dv}{dr}\, 2\pi r\, dr = \int_{r_i}^{r_o} \dot{q}\, v\, 2\pi r\, dr + q_w\, v(r_o)\, 2\pi r_o
\]

for all test \(v\). With linear \(P1\) elements on 20 radial cells, the assembled system is \(\mathbf{K}_T \mathbf{T} = \mathbf{f} + q_w \mathbf{b}_\Gamma\) — the same sparse pattern as Part IV thermoelastic, minus mechanics.

**Picard loop (solid ↔ fluid).**

1. Initialize \(T_w^{(0)} = 350\,\text{K}\), set \(q_w^{(0)} = h(T_w^{(0)} - T_\infty)\).
2. **Solid solve:** impose Neumann \(q_w^{(k)}\) on \(r_o\); obtain volume-averaged \(\bar{T}^{(k)}\) and surface \(T_w^{(k,\text{solid})} = T(r_o)\).
3. **Fluid update:** recompute \(\text{Ra}(T_w)\) if properties are temperature-dependent; update \(h^{(k)}\); set \(q_w^{(k+1)} = h^{(k)}(T_w^{(k,\text{solid})} - T_\infty)\).
4. **Under-relax:** \(T_w^{(k+1)} = (1-\omega) T_w^{(k)} + \omega T_w^{(k,\text{solid})}\) with \(\omega = 0.4\)–\(0.6\) when oscillations appear (same lesson as the lumped table in the worked example above).
5. Stop when \(|T_w^{(k+1)} - T_w^{(k)}| < 0.5\,\text{K}\) **and** \(|\dot{Q}_{\text{Joule}} - 2\pi r_o L q_w| / \dot{Q}_{\text{Joule}} < 1\%\).

**Representative convergence (Joule \(\dot{Q} = 4\,\text{W}\) on 10 cm segment).**

| Iteration | \(T_w\) [K] | \(h\) [W/m²K] | \(q_w\) [W/m²] | Energy residual |
|-----------|-------------|---------------|----------------|-----------------|
| 0 | 350 | 22 | 1100 | +38% |
| 1 | 388 | 24 | 2130 | +12% |
| 2 | 376 | 23 | 1748 | −3% |
| 3 | 381 | 23.5 | 1904 | +1% |
| 4 | **379** | **23.2** | **1830** | **< 1%** |

At convergence, mid-radius temperature \(\bar{T} \approx 395\,\text{K}\) — still below typical annealing onset for copper (\(\sim 450\)–\(500\,\text{K}\) for recovery), but close enough that **Act III** load should not assume a cold wire. Export \((T_w, q_w)\) to the Part VII opening table: mobility \(M(\tau, T_w)\) must use \(T_w \approx 379\,\text{K}\), not room temperature.

**Coupling checklist before multiphysics production codes.**

| Check | Pass criterion | Failure mode |
|-------|----------------|--------------|
| Interface continuity | \(|T_s - T_f| < 10^{-3}\,\text{K}\) on \(\Gamma_w\) | Mismatching units (°C vs K) |
| Flux balance | \(|\int q_s - \int q_f| / \dot{Q} < 1\%\) | Solid Neumann sign wrong |
| Relaxation | Picard converges in \(< 20\) iterations | Need Aitken or monolithic coupling |
| Downstream pedigree | Archive \(T_w\) beside mobility yaml | DDD at 300 K while wire runs at 380 K |

This extension closes the loop the prologue promised: Part IV assembles the solid operator, Part V supplies the fluid flux, and the interface handshake is a **fixed-point problem with physics constraints** — the template the epilogue generalizes to DFT → MD → DDD → FEM chains.

### When Picard stalls: monolithic coupling

The Picard loop above is a **partitioned** (staggered) scheme: solve the solid with frozen fluid data, then update the fluid with the new wall temperature, repeat. It is the default in many conjugate heat transfer workflows because each physics domain keeps its native discretization — Part IV's \(\mathbf{K}_T\) and Part V's FVM face fluxes — and legacy codes couple through a thin interface layer.

Partitioned coupling fails when the interface Jacobian is stiff. For the lumped model \(q_w = (T_{\text{core}} - T_w)/R_s = hA\,(T_w - T_\infty)\), Picard oscillates when \(R_s hA\) is large (the table in [Lab act: natural convection Nusselt number](#lab-act-natural-convection-nusselt-number-on-the-heated-wire-act-ii--warming) already showed under-relaxation curing the oscillation). In production multiphysics, the same symptom appears when:

| Symptom | Physical cause | First remedy |
|---------|----------------|--------------|
| \(T_w\) oscillates iteration to iteration | Strong two-way coupling; comparable solid and fluid thermal resistances | Under-relaxation \(\omega \in [0.3, 0.6]\) |
| Picard needs \(> 20\) outer iterations | Stiff interface; temperature-dependent \(h(T_w)\) | Aitken \(\Delta^2\) acceleration on \(T_w\) |
| Outer loop diverges despite relaxation | Comparable time scales (transient CHT) or equal-order equal-interpolation without inf–sup | **Monolithic** coupled solve |

**Monolithic coupling** assembles one sparse system for solid and fluid unknowns simultaneously. Strip the wire problem to its algebraic skeleton: unknowns \(\mathbf{x} = [T_{\text{solid}}, T_w]^\top\). The coupled steady conduction–convection problem is

\[
\begin{bmatrix}
  \mathbf{K}_T & \mathbf{b}_\Gamma \\
  \mathbf{c}^\top & d
\end{bmatrix}
\begin{bmatrix}
  \mathbf{T} \\ T_w
\end{bmatrix}
=
\begin{bmatrix}
  \mathbf{f}_J + \mathbf{0} \\
  hA\, T_\infty
\end{bmatrix},
\]

where \(\mathbf{K}_T\) is the solid conduction stiffness from Part IV, \(\mathbf{b}_\Gamma\) distributes the interface flux to surface nodes, \(\mathbf{c}\) extracts the wall temperature from the solid solution, and \(d\) collects the fluid-side conductance \(hA\) plus any solid-side interface row. One linear solve replaces the Picard loop; for this linear steady problem the monolithic answer **is** the fixed point.

Nonlinear Navier–Stokes coupling is the same idea with a Newton outer loop on the monolithic residual instead of Picard on interface data alone:

\[
\mathbf{R}(\mathbf{x}) =
\begin{bmatrix}
  \mathbf{K}_T \mathbf{T} - \mathbf{f}_J - q_w \mathbf{b}_\Gamma \\
  q_w - h(\|\mathbf{u}\|, T_w)\, A\,(T_w - T_\infty) \\
  \mathbf{F}_{\text{NS}}(\mathbf{u}, p, T) - \mathbf{0}
\end{bmatrix}
= \mathbf{0}.
\]

Each Newton step solves \(\mathbf{J}\,\delta\mathbf{x} = -\mathbf{R}\) with block structure — the same block-sparse pattern Part I.4 previewed for coupled thermoelasticity ([IV.4 monolithic thermoelasticity](../part04-fem/04-poisson-to-elasticity.md#coupled-thermoelasticity)). OpenFOAM `chtMultiRegionFoam`, ANSYS System Coupling, and FEniCS `MixedElement` implementations differ in mesh and discretization, but the **structure** is identical: one residual, one Jacobian, interface rows enforcing continuity of temperature and heat flux.

| Strategy | Unknowns per step | Interface guarantee | Typical use |
|----------|-------------------|---------------------|-------------|
| Picard (partitioned) | One domain at a time | Converged only at outer fixed point | Legacy codes, weak coupling, prototyping |
| Aitken-accelerated Picard | One domain at a time | Faster fixed point, same limit | Moderate CHT stiffness |
| Monolithic Newton | All domains | Enforced each Newton step | Strong coupling, transient CHT, equal-order schemes |

**When to reach for monolithic coupling on the copper wire.** Act II steady Joule heating with laminar natural convection rarely needs it — the Picard table above converges in four iterations with mild under-relaxation. Monolithic coupling earns its keep when (i) **transient** heating competes with fluid response time, (ii) **temperature-dependent** properties make \(h = h(T_w)\) strongly nonlinear, or (iii) **equal-order** \(P1\)–\(P1\) fluid–solid interpolation violates inf–sup without a stabilized monolithic form. The epilogue's multiscale handshakes inherit the same decision rule: partitioned DFT→MD→DDD chains are Picard at the workflow level; when one interface carries exponential sensitivity (barrier heights, unit mismatches), tighten the coupling — monolithic in code, or converged reweighting in WHAM — before exporting numbers downstream.

The Part VIII.3 [parallel tempering Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-parallel-tempering-for-screw-cross-slip-at-joule-heated-temperature-act-ii--iv-bridge) is the atomistic analogue: raw cold-replica samples are a **partitioned** estimate of the \(380\,\text{K}\) distribution; WHAM reweighting is the monolithic correction that enforces detailed balance across the full replica ladder before cross-slip counts feed Part VII.

## Concept map checkpoint (Part V)

Part V followed the FVM Notes from integral conservation through Navier–Stokes CFD. The four questions summarize the fluid discretization arc:

| Question | Part V answer (copper wire) |
|----------|----------------------------|
| What **object**? | Cell-averaged states, face fluxes \(\mathbf{F}\cdot\mathbf{n}\), Riemann data |
| What **structure**? | Integral conservation, upwind bias, CFL-limited time stepping |
| What **theorem**? | Godunov-type stability; Lax–Friedrichs entropy conditions (conceptually) |
| What **breaks**? | Shock smearing without limiters; equal-order \(P1\)–\(P1\) without inf–sup |

The conjugate heat transfer scene above is Part IV and Part V **speaking at an interface** — the same pattern the epilogue generalizes to DFT→MD→DDD→FEM chains. Fluids and solids share conservation of mass and momentum; they differ in constitutive response. Part VI names the Cauchy stress and rate of deformation both discretizations approximate.

## Bridge to Part VI

Part V discretized conservation on control volumes for fluids. Part VI develops the **kinematics and stress measures** that both FEM solid codes and FVM fluid codes ultimately approximate — deformation gradient and strain for solids, rate of deformation for fluids, Cauchy stress and balance laws for both. The copper wire under tension and the air cooling it are one multiphysics story told in two discretization languages; Part VI supplies the shared continuum vocabulary.

| What Part V completed | What Part VI opens |
|-----------------------|-------------------|
| Cell-averaged \(T_f\), \(\mathbf{u}\) on the fluid mesh | Temperature and velocity fields \(T(\mathbf{x})\), \(\mathbf{v}(\mathbf{x})\) |
| Face fluxes \(\mathbf{F}\cdot\mathbf{n}\) balancing enthalpy transport | Cauchy traction \(\boldsymbol{\sigma}\mathbf{n}\) on boundaries |
| Conjugate heat transfer loop with Part IV FEM | Thermal strain \(\alpha\Delta T\) in virtual work; coupled multiphysics vocabulary |
| Navier–Stokes + energy (this chapter) | Balance laws \(\nabla\cdot\boldsymbol{\sigma}+\mathbf{b}=\mathbf{0}\) and constitutive response |
| RANS/LES closures for engineering heat transfer | Rate of deformation \(\mathbf{D}\); objectivity and frame indifference |

Return to the prologue's **Act II — Warming**: current flows, the wire heats, air cools the surface. Part V named the fluxes that carry enthalpy away; Part VI names the **stress and deformation** fields that govern mechanical response when the wire yields in Acts III–IV. If you arrived via **Door A** from [IV.5](../part04-fem/05-convergence.md#bridge-two-doors-from-here), you have discretized both solids and fluids; Part VI unifies their physics in one tensor language. If you took **Door B** (FEM straight to continuum), read the conjugate heat transfer scene above as the handshake pattern Part VI generalizes — wall temperature and flux must agree before mechanical softening enters the story.

The [prologue](../../prologue/00-many-scales.md) promised one specimen in two discretization languages. Part IV's \(\mathbf{K}\mathbf{U}=\mathbf{F}\) and Part V's flux balances are not competing methods; they are **adjacent chapters** in the same afternoon. Part VI is where the load cell's force–displacement curve acquires Cauchy stress behind it, and where cold-drawn strength stops being a fitted parameter and becomes a question for dislocations in Part VII. See [VI opening](../part06-continuum/00-opening.md#closing-the-arc-from-parts-iv-and-v) **Closing the arc from Parts IV and V** for the full handoff table.

Turn the page when sparse linear systems and face fluxes feel like the whole story — continuum mechanics is what makes \(\mathbf{K}\mathbf{U}=\mathbf{F}\) a force-balance statement rather than an array exercise.
