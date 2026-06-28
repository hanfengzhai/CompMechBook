# Part V — Conservation on Cells

Parts III and IV developed Galerkin finite elements for elliptic problems — displacement, temperature, potential — where energy minimization and trial functions in \(H^1\) are the natural language. Fluids and hyperbolic conservation laws tell a different story: mass, momentum, and energy are **conserved fluxes** that must balance across control volumes, not variational fields that minimize a quadratic functional.

The finite volume method discretizes those flux balances directly. When the copper wire heats the surrounding air, convection carries energy away at a rate governed by the Navier–Stokes equations and boundary-layer physics that FEM conduction alone cannot resolve. Part V builds the FVM toolkit: integral conservation laws, one-dimensional schemes, Riemann solvers for shocks and contact discontinuities, and the CFD pipeline for incompressible and compressible flow.

The layout follows the **FVM Notes** in [`writings/fvm/`](../../writings/fvm/): four numbered chapters, **Bridge** sections at each handoff, and recurring connections to the weak-form ideas of Part III. Part VI unifies the continuum stress and balance language that both FEM and FVM ultimately approximate.

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

## Bridge

Part IV assembled stiffness matrices from shape functions. Part V begins with a different question: given a conservation law in integral form, how do we balance fluxes across cell faces so that discrete solutions respect the same invariants the continuous PDE preserves?
