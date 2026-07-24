# Strong Formulations and Their Limits

Partial differential equations are the local laws of continuum mechanics written in the language of fields. Before we weaken those laws for computation, we must understand what they demand in the classical sense.

The copper wire in the prologue reappears here as a domain — a one-dimensional interval for axial deformation, a three-dimensional body for full elasticity, a boundary in contact with a cooling fluid. At every point inside the domain, a PDE relates rates of change of field variables to sources and material response. That **strong form** is what physicists write on the blackboard; it is also what fails to have a classical solution when geometry, loads, or material behavior become rough. Understanding both its power and its limits motivates the weak form in the next chapter.

## Scene: heat at every point

The tensile frame from Part I is still running, but the operator has raised the current. A thermal camera shows the copper wire no longer uniform: the center runs hotter than the grips, and the hottest strip follows the narrowest cross-section where Joule heating concentrates. An engineer writes on a whiteboard:

\[
-\nabla\cdot(\kappa \nabla T) = \dot{q}_{\text{Joule}}(\mathbf{x}) \quad \text{in the wire},
\]

with \(\dot{q}_{\text{Joule}} = \rho_e |\mathbf{J}|^2 / \sigma_e\) at **every interior point** \(\mathbf{x}\). That is a strong-form PDE: the equation must hold pointwise, the temperature must be smooth enough that \(\nabla\cdot(\kappa\nabla T)\) exists everywhere, and boundary conditions must be specified on the entire surface — fixed temperature at the water-cooled grips, convective flux to air on the lateral surface.

This scene is the strong form at its most honest. It names a field \(T(\mathbf{x})\), a differential operator acting on it, and sources tied to local physics. It also previews the failure mode: at a sharp corner where the wire meets a ceramic insulator, classical smoothness of \(T\) may break down; at a contact interface, the flux boundary condition itself may be ambiguous until a finer model supplies it. Part III begins with the language that works when the blackboard equation is correct; the next chapter weakens it when corners, point loads, and kinks enter the story.

## Prototype: Poisson's equation

On a bounded domain \(\Omega \subset \mathbb{R}^d\),

\[
-\Delta u = f \quad \text{in } \Omega,
\]

with boundary conditions on \(\partial\Omega\). **Dirichlet** conditions fix \(u = g\) on \(\Gamma_D\). **Neumann** conditions fix \(\partial u / \partial n = h\) on \(\Gamma_N\). Mixed problems partition the boundary: \(\partial\Omega = \Gamma_D \cup \Gamma_N\).

Poisson's equation models:

- Steady heat conduction (\(u\) = temperature)
- Membrane deflection (\(u\) = displacement)
- Electrostatic potential
- Porous flow in the Darcy limit

### 1D steady heat on the copper wire

For a wire of length \(L\) with uniform cross-section, steady conduction with volumetric heat generation \(f(x)\) and thermal conductivity \(k\) gives

\[
-\frac{d}{dx}\left(k \frac{dT}{dx}\right) = f(x), \quad 0 < x < L.
\]

If \(k\) is constant and \(f = 0\), the strong solution is linear in \(x\): temperature drops linearly from the hot end to the cold end. **Worked example**: \(T(0) = T_h\), \(T(L) = T_c\), \(f = 0\) yields \(T(x) = T_h + (T_c - T_h)\, x/L\). No mesh is required to write this down — but a mesh becomes necessary when \(f(x)\) is tabulated, \(k\) varies with temperature, or the cross-section is non-uniform.

## The heat equation: parabolic evolution

Transient heating of the wire satisfies

\[
\rho c_p \frac{\partial T}{\partial t} - \nabla\cdot(k\nabla T) = q \quad \text{in } \Omega \times (0,\infty),
\]

with initial condition \(T(\mathbf{x},0) = T_0(\mathbf{x})\) and boundary conditions as above. Here \(\rho c_p\) is volumetric heat capacity. The equation is **parabolic**: disturbances diffuse infinitely fast in the mathematical model (infinite propagation speed of information), smoothing sharp initial data over time.

Semidiscretization in space (FEM or FVM) produces \(\mathbf{M}\dot{\mathbf{T}} + \mathbf{K}\mathbf{T} = \mathbf{q}\) — the same mass and stiffness structure from Part I, now marching in time. Explicit time stepping faces eigenvalue stability limits; implicit schemes solve linear systems each step.

## Elasticity: vector PDEs

Linear elasticity seeks displacement \(\mathbf{u}: \Omega \to \mathbb{R}^d\) satisfying

\[
-\nabla \cdot \boldsymbol{\sigma} = \mathbf{f}, \qquad \boldsymbol{\sigma} = \mathbb{C} : \boldsymbol{\varepsilon}, \qquad \boldsymbol{\varepsilon} = \tfrac{1}{2}(\nabla \mathbf{u} + \nabla \mathbf{u}^T).
\]

This is a **system** of elliptic PDEs (three components in 3D, coupled through constitutive law). For isotropic copper in small strain,

\[
\sigma_{ij} = \lambda \varepsilon_{kk}\delta_{ij} + 2\mu \varepsilon_{ij},
\]

with Lamé parameters \(\lambda, \mu\) derived from Young's modulus \(E\) and Poisson's ratio \(\nu\). Uniaxial tension of the wire reduces to a scalar problem if ends remain plane and uniform: \(\sigma = E \varepsilon\), recoverable from the 1D bar equation \(-EA u'' = 0\).

Nonlinear elasticity replaces Hooke's law with a nonlinear constitutive map; hyperelasticity derives stress from a strain energy density \(\psi(\mathbf{F})\). Large stretch of the copper wire eventually leaves the linear regime — the strong form still holds, but the system becomes nonlinear and may lose ellipticity at extreme deformation.

## Fluid mechanics: Navier–Stokes

For incompressible flow around a heated wire or through a surrounding channel,

\[
\rho\left(\frac{\partial \mathbf{v}}{\partial t} + \mathbf{v}\cdot\nabla \mathbf{v}\right) = -\nabla p + \mu \Delta \mathbf{v} + \mathbf{f}, \qquad \nabla\cdot \mathbf{v} = 0.
\]

The momentum equation is **parabolic** (viscous) with **hyperbolic** advection; the incompressibility constraint is an algebraic coupling. This mixed structure foreshadows stabilized finite elements and pressure–velocity splittings in CFD (Part V).

Coupled **thermoelastic** or **conjugate heat transfer** problems stack elliptic or parabolic solids with Navier–Stokes fluids — different PDE types on different subdomains, coupled through interface conditions (continuity of temperature and heat flux, no-slip or slip velocity).

## Boundary conditions: classification

| Type | Formula | Physical example | FEM enforcement |
|------|---------|------------------|-----------------|
| Dirichlet (essential) | \(u = g\) | Fixed temperature, clamped end | Strongly on trial space |
| Neumann (natural) | \(\partial u/\partial n = h\) | Prescribed heat flux, traction | Appears in weak boundary integral |
| Robin (mixed) | \(\alpha u + \beta \partial u/\partial n = \gamma\) | Convective cooling | Boundary integral + stiffness |
| Interface | Jump conditions | Contact, imperfect bond | Constraint or mortar |

Convective cooling of the copper wire in air often appears as Robin data: \(-k\,\partial T/\partial n = h(T - T_\infty)\) on the lateral surface, coupling the solid to an ambient fluid temperature.

## When classical solutions fail

Strong solutions require enough smoothness — typically \(u \in C^2(\Omega)\) for Poisson, \(\mathbf{u} \in C^2\) for linear elasticity on smooth domains. Corners, reentrant geometries, discontinuous loads, and nonlinear material laws produce singularities. A crack tip has infinite strain in linear elasticity; a shock in gas dynamics has discontinuous velocity.

Consider Poisson on an L-shaped domain with Dirichlet data: the reentrant corner at the inner angle typically reduces regularity so that \(u \notin C^2\) near the corner, even though a **weak** solution exists in \(H^1\). Adaptive mesh refinement (Part IV) concentrates elements where singularities live — guided by error indicators tied to Sobolev regularity (Part III, Chapter 3).

**Computational mechanics does not abandon the PDE.** It seeks a weaker notion of solution that still respects conservation and constitutive laws. That is the weak form.

## Classification and character

Second-order linear PDEs classify by their principal part:

| Type | Prototype | Character | FEM/FVM flavor |
|------|-----------|-----------|----------------|
| Elliptic | \(-\Delta u = f\) | Global coupling, instant equilibrium | FEM natural |
| Parabolic | \(u_t - \Delta u = f\) | Diffusive smoothing in time | FEM + time stepping |
| Hyperbolic | \(u_{tt} - c^2\Delta u = 0\) | Wave propagation | FVM, DG, specialized FEM |

Real applications mix types: thermoelasticity couples elliptic displacement with parabolic temperature; fluid–structure interaction couples hyperbolic–parabolic fluids with elliptic solids.

### Characteristics and domain of dependence (hyperbolic preview)

For \(u_{tt} - c^2 u_{xx} = 0\) on the wire, information travels along characteristics \(x \pm ct = \text{const}\). Explicit finite volume schemes (Part V) respect upwind directions along characteristics; elliptic FEM schemes do not — choosing the wrong discretization family for the PDE type produces useless results even when the code runs without error.

## Strong form as local balance

Every second-order PDE in mechanics can be read as a **balance law**. Poisson is equilibrium of a diffusive flux; elasticity is balance of Cauchy stress; heat is balance of enthalpy with diffusive transport. Finite volume methods (Part V) discretize this balance directly on control volumes — flux in minus flux out equals source — without ever writing \(-\Delta u\) at a point. Finite element methods (Part IV) prefer the weak form derived in the next chapter. Both start from the same physics; they diverge at discretization.

## Worked example: variable conductivity

Suppose \(k(x) = k_0(1 + x/L)\) on the wire with \(T(0)=1\), \(T(L)=0\), \(f=0\). The strong form

\[
-\frac{d}{dx}\left(k(x)\frac{dT}{dx}\right) = 0
\]

integrates once to \(k(x) T'(x) = \text{const}\). Solving gives \(T(x) = 1 - \int_0^x k_0^{-1}(1+s/L)^{-1}\, ds / \int_0^L k_0^{-1}(1+s/L)^{-1}\, ds\). Variable coefficients are routine in strong form; FEM handles them by evaluating \(k\) at quadrature points inside each element.

## Linear elasticity as a system of Poisson-like equations

In components, linear isotropic elasticity on the copper wire (3D body) reads

\[
-\mu \Delta u_i - (\lambda + \mu)\frac{\partial}{\partial x_i}(\nabla\cdot\mathbf{u}) = f_i, \quad i = 1,2,3.
\]

Each displacement component satisfies a Poisson-like equation coupled to the others through \(\nabla\cdot\mathbf{u}\). Incompressible limits (\(\nu \to 1/2\), \(\lambda \to \infty\)) stress the elliptic system and require mixed or penalized formulations — the strong form still holds, but standard displacement-only FEM loses stability. Part III's saddle-point energy methods and Part IV's mixed elements address this failure mode.

## Maximum principle and physical bounds (elliptic)

For \(-\Delta u = f\) with \(f \ge 0\) and \(u = 0\) on \(\partial\Omega\), the **maximum principle** gives \(u \ge 0\) in \(\Omega\). Temperature and displacement potentials inherit such sign properties under appropriate data — a sanity check for codes. Violating the maximum principle in a numerical solution usually signals a sign error in source assembly, wrong boundary tags, or an unstable scheme — not a failure of the continuum model.

## Strong versus weak: a decision table

| Question | Strong form answer | Weak form answer (next chapter) |
|----------|-------------------|--------------------------------|
| How smooth must \(u\) be? | Typically \(C^2\) | \(H^1\) suffices |
| Pointwise flux at boundary? | Defined classically | Emerges as natural BC |
| Point load at a point? | Requires delta source | Functional on test space |
| FEM assembly entry point? | Differentiate twice | One integration by parts |

## Bridge

The strong form is what physicists write. The weak form is what variational algorithms implement. Multiplying by a test function, integrating over \(\Omega\), and integrating by parts moves derivatives from the unknown onto smooth test functions — trading pointwise \(C^2\) requirements for integral balance in \(H^1\).

The next chapter derives the weak form of Poisson's equation — the template for essentially all FEM codes — and states the Lax–Milgram theorem that guarantees a unique weak solution. The copper wire's temperature and displacement, too rough for classical derivatives at corners and kinks, will find a home there.
