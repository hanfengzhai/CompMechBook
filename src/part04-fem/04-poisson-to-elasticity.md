# From Poisson to Elasticity

The jump from a scalar Poisson problem to vector elasticity is not a new method — it is the same Galerkin pipeline with tensor-valued fields and a different bilinear form.

## Weak form of linear elasticity

Find \(\mathbf{u} \in V\) such that

\[
\int_\Omega \boldsymbol{\varepsilon}(\mathbf{u}) : \mathbb{C} : \boldsymbol{\varepsilon}(\mathbf{v}) \, d\Omega = \int_\Omega \mathbf{f}\cdot\mathbf{v} \, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{v} \, dS
\]

for all \(\mathbf{v} \in V_0\). For isotropic Hooke's law,

\[
\mathbb{C}_{ijkl} = \lambda \delta_{ij}\delta_{kl} + \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}),
\]

with Lamé parameters \(\lambda, \mu\) related to Young's modulus \(E\) and Poisson's ratio \(\nu\).

## Finite element discretization

Vector shape functions \(\mathbf{N}_a = N_a \mathbf{e}_i\) give

\[
\mathbf{u}_h = \sum_a N_a \mathbf{U}_a.
\]

The global stiffness has block structure coupling displacement components. Plane stress, plane strain, and axisymmetric problems reduce dimension with modified constitutive matrices.

## Thermal and multiphysics coupling

Temperature fields enter as eigenstrains:

\[
\boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}_{\text{mech}} + \alpha \Delta T \mathbf{I}.
\]

Coupled thermoelasticity alternates or monolithically solves heat and elasticity — each step is FEM on linked meshes.

## Nonlinear elasticity (preview)

Hyperelastic materials define strain energy \(\psi(\mathbf{F})\) with \(\mathbf{F} = \mathbf{I} + \nabla\mathbf{u}\). Stress is

\[
\mathbf{P} = \frac{\partial \psi}{\partial \mathbf{F}}.
\]

Newton iterations use the **tangent stiffness** — the derivative of weak residuals with respect to displacements. Nonlinear FEA is Galerkin plus incremental loading and consistent linearization.

## Bridge

Convergence theorems tie mesh size \(h\) to error in \(H^1\) and \(L^2\). Understanding those norms — from Part I and Part II — closes the loop between theory and mesh refinement studies.
