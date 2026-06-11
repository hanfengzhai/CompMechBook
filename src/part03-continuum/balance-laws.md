# Balance laws and constitutive theory

## The continuum viewpoint

A **continuum body** \(\mathcal{B}\) occupies a region \(\Omega \subset \mathbb{R}^d\). We describe its state with fields: density \(\rho\), velocity \(\mathbf{v}\), temperature \(T\), stress \(\boldsymbol{\sigma}\), and so on.

At every material point and time, **balance laws** express conservation of mass, linear momentum, angular momentum, and energy. **Constitutive relations** connect kinematic quantities to stress and heat flux.

Computational mechanics solves these PDEs—or their weak forms—on domains ranging from turbine blades to polycrystal aggregates.

## Mass conservation

\[
\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{v}) = 0.
\]

For incompressible solids, \(\rho\) is often constant and the kinematic focus shifts to displacement \(\mathbf{u}\).

## Linear momentum

\[
\rho \frac{D\mathbf{v}}{Dt} = \nabla\cdot\boldsymbol{\sigma} + \rho \mathbf{b},
\]

where \(D/Dt\) is the material derivative and \(\mathbf{b}\) body force per unit mass.

In small-displacement static elasticity, \(\mathbf{v}\) is absent and we solve

\[
\nabla\cdot\boldsymbol{\sigma} + \mathbf{f} = \mathbf{0}
\]

with \(\mathbf{f}\) body force per unit volume.

## Angular momentum

Symmetry of Cauchy stress \(\boldsymbol{\sigma} = \boldsymbol{\sigma}^\top\) ensures balance of angular momentum in the absence of couple stresses.

## Energy balance

\[
\rho \frac{De}{Dt} = \boldsymbol{\sigma}:\mathbf{D} - \nabla\cdot\mathbf{q} + r,
\]

with internal energy \(e\), strain rate \(\mathbf{D}\), heat flux \(\mathbf{q}\), and heat source \(r\).

Coupled thermo-mechanical problems (e.g. chip thermal estimation) use both mechanical equilibrium and heat equation.

## Constitutive modeling

Balance laws are universal; materials differ through constitutive laws:

- **Linear elasticity:** \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\).
- **Plasticity:** yield criteria and flow rules constrain \(\boldsymbol{\sigma}\) history.
- **Fluid:** \(\boldsymbol{\tau} = 2\mu \mathbf{D}\) for Newtonian viscosity.

Constitutive choices determine which function spaces and which numerical methods are appropriate.

## Boundary and initial data

- **Dirichlet:** prescribed displacement or velocity.
- **Neumann:** prescribed traction \(\boldsymbol{\sigma}\mathbf{n} = \mathbf{t}\).
- **Initial conditions** for transient problems.

Well-posedness ties to Lax–Milgram coercivity (elliptic) or energy estimates (hyperbolic).

## From CompMethMechProb: multiphysics motivation

The author's undergraduate survey *Computation Methods for Applied Mechanics Problems* threads solid and fluid problems through a common computational lens: analytical solutions where possible, algorithms where necessary—from smartphone chip thermal fields to composite constitutive updates and bioinspired microstructures.

That survey's moral applies here: **the model chooses the method**.

<div class="bridge">

**Bridge.** With balance laws in hand, we specialize to **elasticity and inelasticity**—the workhorse theories of solid computational mechanics.

</div>
