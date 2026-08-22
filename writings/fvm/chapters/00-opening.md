# Part V — Conservation on Cells

Parts III and IV developed Galerkin finite elements for elliptic problems — displacement, temperature, potential — where energy minimization and trial functions in \(H^1\) are the natural language. Fluids and hyperbolic conservation laws tell a different story: mass, momentum, and energy are **conserved fluxes** that must balance across control volumes, not variational fields that minimize a quadratic functional.

The finite volume method discretizes those flux balances directly. When the copper wire heats the surrounding air, convection carries energy away at a rate governed by the Navier–Stokes equations and boundary-layer physics that FEM conduction alone cannot resolve. Part V builds the FVM toolkit: integral conservation laws, one-dimensional schemes, Riemann solvers for shocks and contact discontinuities, and the CFD pipeline for incompressible and compressible flow.

The layout follows the **FVM Notes** in [`writings/fvm/`](../../writings/fvm/): four numbered chapters, **Bridge** sections at each handoff, and recurring connections to the weak-form ideas of Part III. Part VI unifies the continuum stress and balance language that both FEM and FVM ultimately approximate.

## Chapter guide

| Chapter | Wire story beat | Core object | Handoff |
|---------|-----------------|-------------|---------|
| [V.1](01-conservation-integral.md) | Heat leaves the wire by convection | Integral conservation, flux through faces, divergence theorem | 1D schemes and CFL → stability in V.2 |
| [V.2](02-fvm-1d.md) | Upwind cooling along the wire axis | Cell averages, face fluxes, Godunov-type updates | Discontinuities and shocks → Riemann solvers in V.3 |
| [V.3](03-fluxes-riemann.md) | Steep gradients at the hot surface | Approximate Riemann solvers, limiters, TVD property | Incompressible flow → Navier–Stokes in V.4 |
| [V.4](04-navier-stokes-cfd.md) | Air boundary layer around the wire | Pressure–velocity coupling, SIMPLE/PISO, turbulence preview | [Bridge to Part VI](04-navier-stokes-cfd.md#bridge-to-part-vi) |

Read in order. Each chapter ends with a **Bridge** that states why the next chapter must exist; applying FVM to Navier–Stokes without mastering 1D fluxes is like meshing a solid before understanding conservation.

## Scene

Part IV meshed the copper wire as a solid: stiffness matrices from Galerkin assembly, convergence rates in the energy norm, and the two-door bridge at the end of Chapter 5 — either continue here to fluids or jump ahead to Part VI for stress and strain. If you chose Door A, you arrive with a mesh in hand and a question Part IV did not fully answer: *what happens outside the wire?*

Current heats the copper; air carries that heat away by convection. Inside the wire, conduction is elliptic and FEM-friendly. In the surrounding fluid, momentum and energy are **transported**, not minimized — mass and enthalpy move with the flow, boundary layers steepen near the hot surface, and at high Reynolds number vortices shed downstream. The strong form is still Navier–Stokes and the energy equation from Part III, but the discretization philosophy shifts from trial functions in \(H^1\) to **flux balance on control volumes**. Part V is where the wire meets the wind.

## The concept map

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Cell averages, face fluxes, conserved quantities |
| What **structure** does it add? | Integral balance, upwind bias, Riemann solvers |
| What **theorem** becomes possible? | Discrete conservation, Lax equivalence, TVD limiters |
| What **breaks** if structure is missing? | Mass loss, spurious oscillations at shocks, instability at high CFL |

```mermaid
flowchart LR
  I[Integral conservation] --> D[1D FVM]
  D --> R[Riemann / fluxes]
  R --> N[Navier-Stokes CFD]
  N --> CHT[Conjugate heat on wire]
```

**Baby picture:** divide the domain into cells, balance fluxes across faces, resolve discontinuities with a Riemann problem, then extend to Navier–Stokes for the air cooling the copper wire. FVM complements FEM: conservation-first where Galerkin energy principles are awkward.

## How Part V connects to Parts IV and VI

Part V is the **transport discretization contract** conjugate heat transfer and CFD workflows inherit:

| Part V chapter | Structure or theorem | Where it reappears |
|----------------|---------------------|-------------------|
| V.1 Integral conservation | Discrete balance on cells | Epilogue multiscale flux handshakes |
| V.2 1D FVM | Upwind bias; CFL stability | Part V.4 boundary layers on hot wire |
| V.3 Riemann fluxes | TVD limiters; shock capturing | High-speed flows; numerical diffusion audit |
| V.4 Navier–Stokes | SIMPLE coupling; conjugate heat | Act II thermocouple; epilogue FEM↔FVM loop |

Part IV meshed the wire's interior; Part V resolves the air that carries heat away. Part VI names the Cauchy stress and rate-of-deformation tensors both discretizations approximate — the continuum floor where the fork reunites.

## Representative schematics (FVM / CFD Notes)

The [Finite Volume Method Notes](https://hanfengzhai.github.io/note/FVM.pdf) and [Computational Fluid Dynamics Notes](https://hanfengzhai.github.io/file/CFD_note.pdf) mirror Part II's concept-map layout: each schematic is a baby picture of the conservation pipeline. Use them as a visual index while reading:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Integral conservation: cell averages, face fluxes, discrete balance | [V.1](01-conservation-integral.md) |
| 2 | One-dimensional FVM: upwind advection, CFL stability (worked Python) | [V.2](02-fvm-1d.md) |
| 3 | Riemann problems, numerical fluxes, TVD limiters at shocks | [V.3](03-fluxes-riemann.md) |
| 4 | Navier–Stokes, SIMPLE pressure–velocity coupling, conjugate heat on the wire | [V.4](04-navier-stokes-cfd.md) |

Each schematic answers the four concept-map questions for one transport layer. When a mesh converges in FEM but a fluid run loses mass or oscillates at a shock, return to the matching row: *what object, what structure, what theorem, what breaks?* Part III wrote the PDEs; Part IV discretized elliptic solids; Part V discretizes **fluxes** for the air that cools the wire.

## Story so far (Parts I–IV)

The ladder from the prologue now has a **computational spine** — not only equations, but algorithms:

| Part | Method | Wire instance |
|------|--------|---------------|
| I–III | Analysis: weak forms, energy, Sobolev spaces | Conduction and elasticity PDEs on the bar |
| IV | FEM: Galerkin assembly, elements, convergence | Meshed solid; \(\mathbf{K}\mathbf{U}=\mathbf{F}\) for tension and heating |

Part IV answered *how* to discretize elliptic problems on complex geometry. Part V asks a complementary question: when the physics is **transport** — momentum and enthalpy carried by a moving fluid — does minimizing energy still lead? Often not. Conservation laws in integral form balance **fluxes** across cell faces; shocks and boundary layers need upwind bias and Riemann solvers, not trial functions alone.

The copper wire you meshed in Part IV still carries current and heat. The air around it was implicit in boundary conditions — a convection coefficient, perhaps a Robin flux. Part V makes that air **explicit**: a fluid domain with cell-averaged velocity and temperature, coupled back to the solid at the interface. Same wire, second discretization dialect; Part VI will name the stress and flux tensors both dialects approximate.

## Closing the arc from Part IV

If you arrived through [IV.5 Door A](../part04-fem/05-convergence.md#bridge-two-doors-from-here), Part IV's closing checkpoint just proved Céa lemma and named two exit doors. Part V is **Door A** — the complementary discretization for the air Part IV left as a Robin boundary condition:

| Part IV (FEM on the wire) | Part V (FVM on the wire) |
|-----------------------------|--------------------------|
| Meshed solid; \(\mathbf{K}\mathbf{T}=\mathbf{q}\) for Joule heat | Fluid domain around the solid; cell-averaged \(T_f\), \(\mathbf{v}\) |
| Shape functions in \(H^1\); energy-minimizing conduction | Flux-balanced transport; upwind bias at steep gradients |
| Robin flux \(q = h(T_w - T_\infty)\) as boundary data | Resolved convection; \(h\) emerges from the boundary layer |
| Céa: discrete tracks continuous minimizer in energy norm | CFL + limiters: discrete fluxes respect conservation invariants |
| Convergence as \(h \to 0\) on the solid mesh | Convergence as \(\Delta x \to 0\) on the fluid grid |

Part IV made the wire's interior computable; Part V makes its **surroundings** honest. The thermocouple from Act II does not respond to conductivity alone — it responds to how fast air carries heat away from the hot surface. [IV.5](../part04-fem/05-convergence.md#bridge-two-doors-from-here) promised that conjugate heat transfer would couple both meshes at an interface; the section below delivers that handshake.

## Closing the arc from Part III

If you have read linearly since the prologue, Part III's closing checkpoint completed the analytical pipeline — strong form, weak form, Sobolev regularity, energy minimum. Part V is the **second discretization dialect** for the same PDEs:

| Part III (PDEs on the wire) | Part V (FVM on the wire) |
|-----------------------------|--------------------------|
| Strong form at every point | Integral balance over each control volume |
| Weak form \(a(u,v)=\ell(v)\) | Flux balance \(\sum_{\text{faces}} \mathbf{F}\cdot\mathbf{n} = 0\) |
| Energy minimization (elliptic) | Entropy conditions (hyperbolic); dissipation (parabolic) |
| Test functions in \(H^1\) | Cell averages and face fluxes |
| Lax–Milgram well-posedness | Discrete conservation; CFL stability for explicit steps |
| [III.4 Bridge](04-energy-methods.md#bridge-to-part-iv) defers FVM fork to IV.5 | [IV.5](../part04-fem/05-convergence.md#bridge-two-doors-from-here) Door A arrives here |

Part III wrote the Navier–Stokes and energy equations the air around the wire satisfies; Part IV discretized the **solid** with Galerkin trial functions. Part V discretizes the **fluid** with conservation-first flux balances — not because the physics changed, but because transport and shocks favor a different computational instinct. The conjugate heat transfer loop below is Part III's weak forms and Part V's flux balances **speaking at an interface**; Part VI will name the Cauchy stress and rate-of-deformation tensors both sides approximate.

## Conjugate heat transfer: the wire meets the wind

The prologue promised that the copper wire and the air around it are one story told in two discretizations. **Conjugate heat transfer** makes that promise concrete:

1. Part IV (or Part III's heat weak form) solves conduction in the solid: \(-\nabla\cdot(k\nabla T) = q_{\text{Joule}}\) with a trial-function mesh on the wire.
2. Part V solves Navier–Stokes and the energy equation in the fluid domain with FVM fluxes.
3. At the fluid–solid interface, **wall temperature** and **heat flux** must agree: \(T_{\text{solid}} = T_{\text{fluid}}\) and \(k\nabla T\cdot\mathbf{n} = -k_f\nabla T_f\cdot\mathbf{n}\).

No single matrix assembles both sides. A **fixed-point or monolithic coupling loop** alternates: given a wall temperature, update the fluid boundary layer; given the resulting flux, update the solid temperature; repeat until the interface residuals fall below tolerance. The epilogue generalizes this handshake from two meshes on one specimen to DFT→MD→DDD→FEM chains — but the intellectual habit is identical: export consistent interface data, document units, and verify convergence of the outer loop, not only of each inner solve.

Chapter 4 closes the loop on the wire: Joule heating in the solid, convection in the air, and the SIMPLE-type pressure–velocity coupling that makes incompressible CFD tractable.

## Closing the arc from Part I

If you have read linearly since the prologue, notice how the **same four questions** from the opening table reappear here with transport vocabulary — and how the **same mathematical habits** from Part I return on a grid of control volumes:

| Part I (springs on the wire) | Part V (fluid around the wire) |
|------------------------------|--------------------------------|
| State vector \(\mathbf{u}\) | Cell-averaged \(\bar{u}_i\), \(\bar{T}_i\) on each control volume |
| Local coupling in \(\mathbf{K}\) | Face fluxes \(F_{i+1/2}\) coupling neighboring cells |
| \(\mathbf{K}\mathbf{u}=\mathbf{f}\) at equilibrium | \(\sum_i \frac{d}{dt}(\bar{u}_i V_i) + \sum_{\text{faces}} F = 0\) (discrete conservation) |
| Eigenmodes and natural frequencies | Wave speeds and Riemann fan structure at interfaces |
| Mesh refinement sends \(N\to\infty\) | Finer cells resolve boundary layers; CFL limit ties \(\Delta t\) to \(\Delta x\) |

Part IV assembled \(\mathbf{K}\) from shape-function integrals; Part V assembles **flux balances** from face quadrature — still sparse linear algebra at each implicit step, but the governing principle is conservation rather than energy minimization. Part III's weak forms asked us to multiply by test functions and integrate; FVM asks us to integrate the PDE over each cell and balance what crosses the faces. The copper wire that began as a spring network now heats the air around it; the interface handshake (wall temperature, heat flux) is the same **export discipline** the prologue promised at every scale — only here the two meshes speak different discretization dialects before Part VI names the stress and flux tensors both approximate.

## Lab act: II — Warming

**Act II** switches on current. The narrowest cross-section heats; air cools the surface; the thermocouple responds while the grips still hold fixed displacement. Part V is the **wind** in that scene — Navier–Stokes and FVM fluxes for the fluid domain coupled to FEM conduction in the solid from Part IV. Conjugate heat transfer is Act II's handshake: wall temperature and heat flux must agree at the interface. When Riemann solvers feel distant from the copper wire, return to the operator watching the thermocouple climb — the same specimen, second discretization dialect.

### What you should be able to do after Part V

Each chapter adds one move to a conservation-first workflow that complements Part IV's Galerkin habit:

| After chapter | Skill on the copper wire | Minimal artifact |
|---------------|--------------------------|------------------|
| V.1 | Write integral balance over a control volume; identify fluxes | \(\frac{d}{dt}\int_V \rho E\, dV + \oint_{\partial V} \mathbf{F}\cdot\mathbf{n}\, dS = 0\) |
| V.2 | Discretize 1D advection–diffusion; read upwind bias | Three-cell stencil; CFL limit \(\Delta t \lesssim \Delta x / |c|\) |
| V.3 | Evaluate a Riemann flux at a face; explain shock capturing | Godunov or Lax–Friedrichs on a step initial condition |
| V.4 | Sketch conjugate heat transfer loop: solid FEM ↔ fluid FVM | Wall \(T\) and flux handshake until interface residual \(< \varepsilon\) |

None of these require a full CFD code — but each one is the transport dialect the air around the wire demands. If you can balance fluxes on three cells, state a CFL limit, and explain why wall temperature must match at a solid–fluid interface, you have the core of Act II's conjugate heat transfer before Part VI names the stress and flux tensors both sides approximate.

## Bridge

Part IV assembled stiffness matrices from shape functions; [IV.5](../part04-fem/05-convergence.md#bridge-two-doors-from-here) named **Door A** — conservation on control volumes for fluids, shocks, and steep advection fronts. Part V walks through that door. The physics of the copper wire did not change; the **computational instinct** did.

| What Part IV gave (solid, Galerkin) | What Part V adds (fluid, FVM) |
|-------------------------------------|-------------------------------|
| Trial functions in \(H^1\) on the wire mesh | Cell-averaged states and face fluxes in the air domain |
| Energy minimization / weak residuals | Integral conservation \(\sum_i \frac{d}{dt}(\bar{u}_i V_i) + \sum_{\text{faces}} F = 0\) |
| \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from assembly | Riemann fluxes, CFL limits, upwind bias for transport |
| Error estimates as \(h \to 0\) | Entropy conditions and shock capturing on coarse grids |

**Scale-boundary handshake (Part IV → Part V → Part VI).**

| FEM export ([Part IV](../part04-fem/00-opening.md)) | FVM output (this part) | Continuum consumer ([Part VI](../part06-continuum/00-opening.md)) | Failure mode |
|-----------------------------------------------------|------------------------|-------------------------------------------------------------------|--------------|
| Meshed solid; \(\mathbf{K}\mathbf{T}=\mathbf{q}\) for Joule heat | Cell flux balances in the air domain | Cauchy stress and rate-of-deformation tensors | Wall temperature mismatch at solid–fluid interface |
| Robin BC \(q = h(T_w - T_\infty)\) as boundary data | Resolved convection boundary layer | Act II thermocouple response to cooling rate | Mass loss or spurious oscillations in fluid run |
| Céa: energy-norm convergence as \(h \to 0\) on solid | CFL stability + TVD limiters on fluid grid | Conjugate heat fixed-point loop until interface residual \(< \varepsilon\) | Outer coupling not converged; only inner solves trusted |
| Galerkin trial functions in \(H^1\) | Upwind bias and Riemann fluxes at steep gradients | Part VI names the flux tensors both discretizations approximate | Shock captured without entropy audit |

The conjugate heat transfer scene above is the numerical face of this handshake: Joule heating in the solid (Part IV) and convection in the air (Part V) exchange wall temperature and heat flux until both sides agree — the same fixed-point discipline the [epilogue](../epilogue/multiscale.md) later generalizes to DFT→MD→DDD→FEM chains. Part VI reunites the fork by naming the Cauchy stress and flux tensors both dialects approximate. Part III wrote the Navier–Stokes and energy equations; Part V discretizes them with flux balances that respect the invariants Galerkin cannot guarantee at high Reynolds number.

The first chapter below begins with **integral forms of conservation laws** — the FVM dialect of the same balance laws Part VI will name in Cauchy stress and rate-of-deformation language. Turn the page when the thermocouple climbs and the air around the wire needs a discretization philosophy of its own.
