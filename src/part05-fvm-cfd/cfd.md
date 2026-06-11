# Computational fluid dynamics

## Governing equations in conservative form

From the author's CFD notes, the 3D compressible Navier–Stokes system in conservative variables \(\mathbf{U} = (\rho, \rho u, \rho v, \rho w, \rho E)^\top\) takes

\[
\frac{\partial \mathbf{U}}{\partial t} + \frac{\partial \mathbf{E}}{\partial x} + \frac{\partial \mathbf{F}}{\partial y} + \frac{\partial \mathbf{G}}{\partial z} - \frac{\partial \mathbf{E}_v}{\partial x} - \frac{\partial \mathbf{F}_v}{\partial y} - \frac{\partial \mathbf{G}_v}{\partial z} = \mathbf{P},
\]

with inviscid fluxes \(\mathbf{E}, \mathbf{F}, \mathbf{G}\), viscous fluxes \(\mathbf{E}_v, \mathbf{F}_v, \mathbf{G}_v\), and source \(\mathbf{P}\) (body forces, heat deposition).

**Inviscid flux example (x-direction):**

\[
\mathbf{E} = \begin{pmatrix} \rho u \\ \rho u^2 + p \\ \rho u v \\ \rho u w \\ \rho u H \end{pmatrix},
\]

with enthalpy \(H = E + p/\rho\).

## Nondimensionalization

CFD practice nondimensionalizes equations with reference length, velocity, density, and temperature—reducing round-off error and clarifying which terms dominate (Reynolds, Mach, Prandtl numbers).

| Number | Ratio | Effect |
|--------|-------|--------|
| Re | inertial / viscous | turbulence, boundary layers |
| Ma | flow speed / sound speed | compressibility |
| Pr | momentum / thermal diffusivity | heat transfer |

## Discretization families

1. **Finite volume** — cell averages, face fluxes (this book's focus in Part V).
2. **Finite difference** — pointwise derivatives on structured grids.
3. **Finite element / DG** — weak forms with discontinuous bases.
4. **Spectral methods** — high-order global bases for smooth flows.

The author's course notes progress: introduction → nondimensionalization → FVM → finite differences → boundary conditions → artificial dissipation → mesh transforms → implicit schemes.

## Implicit vs explicit time stepping

Explicit schemes are simple but CFL-limited. **Implicit** schemes solve coupled systems each step—essential for stiff viscous terms or low-Mach flows, at the cost of linear algebra.

## Turbulence and multiphysics

Engineering CFD rarely solves laminar Navier–Stokes alone. **RANS**, **LES**, and **DNS** trade resolution for modeling. Coupled solvers add combustion, phase change, and fluid–structure interaction.

## SPH and meshfree alternatives

The author's notes also cover **smoothed particle hydrodynamics (SPH)**—Lagrangian particles carrying mass and momentum without a fixed mesh. Useful for free-surface and fragmenting flows where Eulerian meshes struggle.

## Verification and validation

- **Verification:** is the code solving the equations correctly? (manufactured solutions, grid convergence)
- **Validation:** does the model match experiment? (wind tunnel, PIV, pressure taps)

Computational mechanics is not finished when the residual is small—it is finished when the right equations were solved for the right purpose.

<div class="bridge">

**Bridge (end of Part V).** Continuum CFD and FEM describe fields on domains. **Crystalline defects**—dislocations, vacancies, grain boundaries—live between continuum and atomistic descriptions. Part VI descends to the mesoscale.

</div>
