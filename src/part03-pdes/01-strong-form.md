# Strong Formulations and Their Limits

Partial differential equations are the local laws of continuum mechanics written in the language of fields. Before we weaken those laws for computation, we must understand what they demand in the classical sense.

## Prototype: Poisson's equation

On a bounded domain \(\Omega \subset \mathbb{R}^d\),

\[
-\Delta u = f \quad \text{in } \Omega,
\]

with boundary conditions on \(\partial\Omega\). **Dirichlet** conditions fix \(u = g\). **Neumann** conditions fix \(\partial u / \partial n = h\). Mixed problems partition the boundary.

Poisson's equation models:

- Steady heat conduction (\(u\) = temperature)
- Membrane deflection (\(u\) = displacement)
- Electrostatic potential
- Porous flow in the Darcy limit

## Elasticity: vector PDEs

Linear elasticity seeks displacement \(\mathbf{u}: \Omega \to \mathbb{R}^d\) satisfying

\[
-\nabla \cdot \boldsymbol{\sigma} = \mathbf{f}, \qquad \boldsymbol{\sigma} = \mathbb{C} : \boldsymbol{\varepsilon}, \qquad \boldsymbol{\varepsilon} = \tfrac{1}{2}(\nabla \mathbf{u} + \nabla \mathbf{u}^T).
\]

This is a **system** of elliptic PDEs. Nonlinear elasticity replaces Hooke's law with a nonlinear constitutive map; hyperelasticity derives stress from a strain energy density \(\psi(\mathbf{F})\).

## Fluid mechanics: Navier–Stokes

For incompressible flow,

\[
\rho\left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla \mathbf{v}\right) = -\nabla p + \mu \Delta \mathbf{v} + \mathbf{f}, \qquad \nabla\cdot \mathbf{v} = 0.
\]

The momentum equation is **parabolic** (viscous) with **hyperbolic** advection; the incompressibility constraint is an algebraic coupling. This mixed structure foreshadows stabilized finite elements and pressure–velocity splittings in CFD.

## When classical solutions fail

Strong solutions require enough smoothness — typically \(u \in C^2\) for Poisson. Corners, reentrant geometries, discontinuous loads, and nonlinear material laws produce singularities. A crack tip has infinite strain in linear elasticity; a shock in gas dynamics has discontinuous velocity.

**Computational mechanics does not abandon the PDE.** It seeks a weaker notion of solution that still respects conservation and constitutive laws. That is the weak form.

## Classification and character

Second-order linear PDEs classify by their principal part:

| Type | Prototype | Character | FEM/FVM flavor |
|------|-----------|-----------|----------------|
| Elliptic | \(-\Delta u = f\) | Global coupling, instant equilibrium | FEM natural |
| Parabolic | \(u_t - \Delta u = f\) | Diffusive smoothing in time | FEM + time stepping |
| Hyperbolic | \(u_{tt} - c^2\Delta u = 0\) | Wave propagation | FVM, DG, specialized FEM |

Real applications mix types: thermoelasticity couples elliptic displacement with parabolic temperature; fluid–structure interaction couples hyperbolic–parabolic fluids with elliptic solids.

## Bridge

The strong form is what physicists write. The weak form is what variational algorithms implement. The next chapter derives the weak form of Poisson's equation — the template for essentially all FEM codes.
