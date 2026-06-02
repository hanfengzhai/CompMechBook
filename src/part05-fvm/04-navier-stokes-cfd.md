# Navier–Stokes and Computational Fluid Dynamics

Computational fluid dynamics (CFD) solves the Navier–Stokes equations — the governing equations of fluid motion — when analytical solutions fail under nonlinearity, complex geometry, or turbulence.

## Governing equations

For a Newtonian fluid,

\[
\rho\left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla \mathbf{v}\right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}, \qquad \nabla\cdot\mathbf{v} = 0.
\]

In conservative form, mass and momentum are conserved quantities with convective and diffusive fluxes. **Reynolds number** \(\text{Re} = \rho U L / \mu\) measures the ratio of inertial to viscous forces — high Re means turbulence and stiff numerics.

## Discretization strategies

**Finite volume** on structured or unstructured meshes:

- Store cell-centered or staggered velocities
- Compute convective fluxes with upwind or Riemann schemes
- Diffusive fluxes with centered differences
- Pressure–velocity coupling via SIMPLE, PISO, or projection methods

**Finite element** for Stokes/Navier–Stokes:

- Mixed elements for \(\mathbf{v}\) and \(p\) with LBB stability
- Stabilized equal-order elements (SUPG/PSPG) for convenience
- Variational multiscale for turbulence modeling

## Boundary conditions and practical CFD

- **Inflow**: specify velocity profile or total pressure
- **Outflow**: traction-free or convective outflow
- **Walls**: no-slip (\(\mathbf{v} = 0\)) or slip for free surfaces
- **Turbulence**: RANS models (k–ε, k–ω), LES, or DNS at increasing cost

The author's [CFD notes](https://hanfengzhai.github.io/file/CFD_note.pdf) introduce these concepts from a fluid mechanics perspective: governing equations, nondimensional groups, and the goal of replacing experiments with simulation where validated.

## Verification and validation

**Verification** asks: does the code solve the equations correctly? (Manufactured solutions, grid convergence, conservation checks.)

**Validation** asks: does the model match reality? (Wind tunnel, PIV, benchmark cases.)

Both are necessary. A converged simulation of the wrong equations is worthless.

## Bridge to Part VI

Fluids and solids share conservation laws but differ in constitutive response. Part VI develops the kinematics and stress measures that FEM solid codes implement — and that multiphysics couplings must pass consistently across interfaces.
