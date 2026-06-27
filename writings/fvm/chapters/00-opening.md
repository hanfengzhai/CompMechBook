# Part V — Conservation on Cells

Parts III and IV developed Galerkin finite elements for elliptic problems — displacement, temperature, potential — where energy minimization and trial functions in \(H^1\) are the natural language. Fluids and hyperbolic conservation laws tell a different story: mass, momentum, and energy are **conserved fluxes** that must balance across control volumes, not variational fields that minimize a quadratic functional.

The finite volume method discretizes those flux balances directly. When the copper wire heats the surrounding air, convection carries energy away at a rate governed by the Navier–Stokes equations and boundary-layer physics that FEM conduction alone cannot resolve. Part V builds the FVM toolkit: integral conservation laws, one-dimensional schemes, Riemann solvers for shocks and contact discontinuities, and the CFD pipeline for incompressible and compressible flow.

The layout follows the **FVM Notes** in [`writings/fvm/`](../../writings/fvm/): four numbered chapters, **Bridge** sections at each handoff, and recurring connections to the weak-form ideas of Part III. Part VI unifies the continuum stress and balance language that both FEM and FVM ultimately approximate.

## The concept map (FVM / CFD notes)

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | Cell-averaged conserved quantities — mass, momentum, energy |
| What **structure** does it add? | Integral conservation; face fluxes; upwind bias |
| What **theorem** becomes possible? | Discrete conservation; Lax equivalence (consistency + stability ⇒ convergence) |
| What **breaks** if structure is missing? | Shock oscillations; loss of mass balance; Courant instability |

```mermaid
flowchart LR
  PDE[Conservation law] --> Int[Integral form on cells]
  Int --> Flux[Face fluxes]
  Flux --> Riemann[Riemann solvers]
  Riemann --> NS[Navier–Stokes / CFD]
  NS --> CHT[Conjugate heat: wire + air]
```

**Baby picture:** balance fluxes in and out of each control volume so the discrete scheme preserves the same invariants as the continuous PDE — then refine the Riemann solver when shocks or steep gradients appear.

## Bridge

Part IV assembled stiffness matrices from shape functions. Part V begins with a different question: given a conservation law in integral form, how do we balance fluxes across cell faces so that discrete solutions respect the same invariants the continuous PDE preserves?
