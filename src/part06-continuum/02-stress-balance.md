# Stress, Balance Laws, and Constitutive Relations

Kinematics describes motion. Balance laws say how forces relate to acceleration. Constitutive relations say how materials respond — the part continuum mechanics cannot derive from geometry alone.

## Cauchy stress and traction

Traction on a surface with normal \(\mathbf{n}\) is \(\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}\). Cauchy stress \(\boldsymbol{\sigma}\) is symmetric under angular momentum balance (in the absence of couple stresses).

## Conservation laws

**Mass conservation** (reference configuration):

\[
\rho_0 = J \rho.
\]

**Linear momentum**:

\[
\nabla\cdot\boldsymbol{\sigma} + \mathbf{f} = \rho \frac{D\mathbf{v}}{Dt}.
\]

**Energy balance** couples mechanical work to internal energy and heat flux — essential for thermoelasticity and shock physics.

## Constitutive examples

| Material class | Constitutive relation | Computational note |
|----------------|----------------------|-------------------|
| Linear elastic | \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) | Symmetric stiffness, Hooke's law |
| Hyperelastic | \(\mathbf{P} = \partial\psi/\partial\mathbf{F}\) | Nonlinear Newton FEM |
| Newtonian fluid | \(\boldsymbol{\tau} = 2\mu\mathbf{D}\) | Navier–Stokes viscosity |
| Rate-independent plasticity | Yield + flow rule | Return mapping algorithms |

## Elasticity & inelasticity

The author's [elasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf) develop tensor algebra, Hooke's law, boundary value problems, and extensions to plasticity and fracture mechanics — the continuum backbone of solid simulation.

Plasticity introduces **internal variables** (accumulated slip, hardening) and **KKT conditions** at yield — variational inequalities rather than simple minimization.

## Bridge

Variational statements of elasticity unify static equilibrium with FEM weak forms. Nonlinear extensions preserve the Galerkin structure while changing the tangent operator each Newton step.
