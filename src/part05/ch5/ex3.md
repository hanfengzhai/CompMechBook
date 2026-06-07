## 5.3 CFD in conservation form

### Why conservation form

The author's CFD notes emphasize rewriting Navier–Stokes in **conservation form** for computation:

$$
\frac{\partial \mathbf{U}}{\partial t} + \nabla \cdot \mathbf{F}(\mathbf{U}) = \mathbf{S},
$$

with source $\mathbf{S}$ for body forces and viscous contributions written as divergences where possible.

**Benefits:**

1. **Conservation** of mass, momentum, energy enforced at discrete level
2. **Discontinuities** (shocks, contacts) handled as weak solutions
3. **Nondimensionalization** groups variables consistently (Reynolds, Mach, Prandtl)

### Nondimensionalization

Reference scales $\rho_\infty$, $U_\infty$, $L$, $T_\infty$ produce dimensionless variables. For example, Reynolds number $\mathrm{Re} = \rho U L / \mu$ and Mach number $M = U/c$ control viscous and compressibility effects.

Poor scaling wastes floating-point precision—the same lesson as ill-conditioned stiffness matrices in FEM.

### Unstructured meshes

FVM on triangular/tetrahedral meshes (ocean modeling, mantle convection, reactor thermal hydraulics) uses fluxes across general polygonal/polyhedral faces. Unstructured FVM parallels unstructured FEM connectivity—only the degrees of freedom differ (cell averages vs nodal values).

### Relation to FEM in fluids

- **FEM:** Galerkin weak form, continuous fields, natural for incompressible slow flow (mixed $u$–$p$ elements)
- **FVM:** integral conservation, natural for compressible flow with shocks

Both solve the same Navier–Stokes PDEs; the discretization philosophy follows the dominant physics.

**Takeaway.** Choose conservation form when the question is flux through a face, not energy minimization in a function space.
