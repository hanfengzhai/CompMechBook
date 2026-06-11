# Elasticity and inelasticity

## Kinematics of deformation

A body maps reference position \(\mathbf{X}\) to current position \(\mathbf{x} = \boldsymbol{\varphi}(\mathbf{X})\). The **deformation gradient** is

\[
\mathbf{F} = \frac{\partial \mathbf{x}}{\partial \mathbf{X}}.
\]

**Green–Lagrange strain:**

\[
\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^\top\mathbf{F} - \mathbf{I}).
\]

For small displacements \(\mathbf{u}\),

\[
\varepsilon_{ij} = \tfrac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right).
\]

## Linear isotropic elasticity

**Hooke's law:**

\[
\sigma_{ij} = \lambda \varepsilon_{kk}\delta_{ij} + 2\mu \varepsilon_{ij},
\qquad
\mu = \frac{E}{2(1+\nu)},\;
\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}.
\]

**Navier equation** (displacement form):

\[
\mu \nabla^2 \mathbf{u} + (\lambda+\mu)\nabla(\nabla\cdot\mathbf{u}) + \mathbf{f} = \mathbf{0}.
\]

## Weak form of linear elasticity

Find \(\mathbf{u} \in [H^1_0(\Omega)]^d\) such that

\[
\int_\Omega \boldsymbol{\varepsilon}(\mathbf{u}) : \mathbb{C} : \boldsymbol{\varepsilon}(\mathbf{v})\, dx
= \int_\Omega \mathbf{f}\cdot\mathbf{v}\, dx + \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{v}\, dS
\]

for all \(\mathbf{v} \in [H^1_0(\Omega)]^d\) with appropriate boundary splitting.

This is the starting point for FEM in Part IV.

## Inelasticity (outline)

**Plasticity** introduces internal variables (yield function, hardening). Stress lies on or inside a yield surface; plastic strain evolves when loading exceeds yield.

**Viscoplasticity** adds rate dependence—relevant to high-temperature creep and polymer flows.

**Finite strain** requires objective stress rates and hyperelastic potentials for nonlinear FEM.

The author's notes on *Elasticity & Inelasticity* develop tensor forms, yield criteria, and finite-element implementation paths; the narrative here emphasizes that **inelasticity changes the operator** (history-dependent, possibly nonsmooth) but not the overall workflow: weak form → discretize → solve.

## Polycrystals and homogenization (preview)

At the mesoscale, each grain may have distinct orientation and slip activity. Homogenization averages grain-level fields to effective properties—connecting FEM at the continuum scale to dislocation and crystal plasticity models in Part VI.

<div class="bridge">

**Bridge.** Strong forms are PDEs; computers prefer algebraic systems. The **weak form** is the deliberate passage from classical to variational statements.

</div>
