# Part V — Conservation on Cells

Parts III and IV developed Galerkin finite elements for elliptic problems — displacement, temperature, potential — where energy minimization and trial functions in \(H^1\) are the natural language. Fluids and hyperbolic conservation laws tell a different story: mass, momentum, and energy are **conserved fluxes** that must balance across control volumes, not variational fields that minimize a quadratic functional.

The finite volume method discretizes those flux balances directly. When the copper wire heats the surrounding air, convection carries energy away at a rate governed by the Navier–Stokes equations and boundary-layer physics that FEM conduction alone cannot resolve. Part V builds the FVM toolkit: integral conservation laws, one-dimensional schemes, Riemann solvers for shocks and contact discontinuities, and the CFD pipeline for incompressible and compressible flow.

The layout follows the **FVM Notes** in [`writings/fvm/`](../../writings/fvm/): four numbered chapters, **Bridge** sections at each handoff, and recurring connections to the weak-form ideas of Part III. Part VI unifies the continuum stress and balance language that both FEM and FVM ultimately approximate.

## Where we left the wire

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

## Representative schematics (FVM / CFD)

The [Finite Volume Method notes](https://hanfengzhai.github.io/note/FVM.pdf) and [CFD notes](https://hanfengzhai.github.io/file/CFD_note.pdf) collect the flux-balance machine this part builds:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Control volume; integral conservation; flux through faces | [V.1](01-conservation-integral.md) |
| 2 | 1D FVM: cell averages; upwind advection; CFL stability | [V.2](02-fvm-1d.md) |
| 3 | Flux splitting; Godunov / Roe Riemann solvers | [V.3](03-fluxes-riemann.md) |
| 4 | TVD limiters; shock capturing without spurious oscillations | [V.3](03-fluxes-riemann.md) |
| 5 | Navier–Stokes: pressure–velocity coupling; SIMPLE loop | [V.4](04-navier-stokes-cfd.md) |
| 6 | Conjugate heat transfer: wire (FEM) ↔ air (FVM) interface | [V.4](04-navier-stokes-cfd.md) |
| 7 | Lax equivalence: consistency + stability \(\Rightarrow\) convergence | [V.2](02-fvm-1d.md), [V.3](03-fluxes-riemann.md) |

When a flux formula feels arbitrary, return to the matching row: discrete conservation is the structure FVM adds that Galerkin energy alone does not guarantee for transport.

## Lab act (prologue map)

You are in **Act II — Warming**, outside the wire. Current heats the copper; air decides how fast that heat leaves — convection, boundary layers, perhaps vortices at high Reynolds number. Part V is the second discretization on the same afternoon: FEM solved conduction inside (Part IV or Part III); FVM balances enthalpy flux in the fluid domain. The [prologue](../prologue/00-many-scales.md#the-experiment-as-plot) calls this conjugate heat transfer; Chapter 4 closes the loop.

## Story so far (Parts I–IV)

The ladder from the prologue now has a **computational spine** — not only equations, but algorithms:

| Part | Method | Wire instance |
|------|--------|---------------|
| I–III | Analysis: weak forms, energy, Sobolev spaces | Conduction and elasticity PDEs on the bar |
| IV | FEM: Galerkin assembly, elements, convergence | Meshed solid; \(\mathbf{K}\mathbf{U}=\mathbf{F}\) for tension and heating |

Part IV answered *how* to discretize elliptic problems on complex geometry. Part V asks a complementary question: when the physics is **transport** — momentum and enthalpy carried by a moving fluid — does minimizing energy still lead? Often not. Conservation laws in integral form balance **fluxes** across cell faces; shocks and boundary layers need upwind bias and Riemann solvers, not trial functions alone.

The copper wire you meshed in Part IV still carries current and heat. The air around it was implicit in boundary conditions — a convection coefficient, perhaps a Robin flux. Part V makes that air **explicit**: a fluid domain with cell-averaged velocity and temperature, coupled back to the solid at the interface. Same wire, second discretization dialect; Part VI will name the stress and flux tensors both dialects approximate.

## Conjugate heat transfer: the wire meets the wind

The prologue promised that the copper wire and the air around it are one story told in two discretizations. **Conjugate heat transfer** makes that promise concrete:

1. Part IV (or Part III's heat weak form) solves conduction in the solid: \(-\nabla\cdot(k\nabla T) = q_{\text{Joule}}\) with a trial-function mesh on the wire.
2. Part V solves Navier–Stokes and the energy equation in the fluid domain with FVM fluxes.
3. At the fluid–solid interface, **wall temperature** and **heat flux** must agree: \(T_{\text{solid}} = T_{\text{fluid}}\) and \(k\nabla T\cdot\mathbf{n} = -k_f\nabla T_f\cdot\mathbf{n}\).

No single matrix assembles both sides. A **fixed-point or monolithic coupling loop** alternates: given a wall temperature, update the fluid boundary layer; given the resulting flux, update the solid temperature; repeat until the interface residuals fall below tolerance. The epilogue generalizes this handshake from two meshes on one specimen to DFT→MD→DDD→FEM chains — but the intellectual habit is identical: export consistent interface data, document units, and verify convergence of the outer loop, not only of each inner solve.

Chapter 4 closes the loop on the wire: Joule heating in the solid, convection in the air, and the SIMPLE-type pressure–velocity coupling that makes incompressible CFD tractable.

## Bridge

Part IV assembled stiffness matrices from shape functions. Part V begins with a different question: given a conservation law in integral form, how do we balance fluxes across cell faces so that discrete solutions respect the same invariants the continuous PDE preserves?
