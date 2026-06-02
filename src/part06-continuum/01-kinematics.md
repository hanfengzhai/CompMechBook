# Kinematics: How Bodies Move and Deform

Continuum mechanics describes matter as a continuous map from reference configuration to current configuration. Kinematics is the geometry of that map — independent of forces and materials.

## Configurations and displacement

Let \(\mathbf{X}\) be a point in the **reference configuration** \(\Omega_0\) and \(\mathbf{x}\) its location in the **current configuration** \(\Omega\). The **deformation map** is

\[
\mathbf{x} = \boldsymbol{\varphi}(\mathbf{X}).
\]

**Displacement** is \(\mathbf{u}(\mathbf{X}) = \mathbf{x} - \mathbf{X}\).

## Deformation gradient

\[
\mathbf{F} = \frac{\partial \mathbf{x}}{\partial \mathbf{X}} = \mathbf{I} + \frac{\partial \mathbf{u}}{\partial \mathbf{X}}.
\]

Volume change is \(J = \det \mathbf{F}\). Rigid motions have \(\mathbf{F} \in SO(3)\) (proper rotations, no stretch).

## Strain measures

**Small strain** (linear elasticity):

\[
\boldsymbol{\varepsilon} = \tfrac{1}{2}(\nabla \mathbf{u} + \nabla \mathbf{u}^T).
\]

**Green–Lagrange strain** (finite deformation):

\[
\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I}).
\]

**Rate of deformation** (fluids):

\[
\mathbf{D} = \tfrac{1}{2}(\nabla \mathbf{v} + \nabla \mathbf{v}^T).
\]

Different measures suit different regimes; mixing them inconsistently is a common source of bugs in multiphysics codes.

## Stress and balance (preview)

**Cauchy stress** \(\boldsymbol{\sigma}\) acts on area elements in the current configuration. **Piola–Kirchhoff stress** \(\mathbf{P}\) relates reference area elements to forces. Balance of linear momentum:

\[
\nabla\cdot\boldsymbol{\sigma} + \mathbf{f} = \rho \mathbf{a} \quad \text{(current)}.
\]

Static FEM typically works with \(\boldsymbol{\sigma}\) and small strain; hyperelastic FEM uses \(\mathbf{P}\) and \(\mathbf{F}\).

## Bridge

Constitutive laws connect strain to stress; balance laws connect stress to body forces and inertia. The next chapter completes the continuum picture that FEM discretizes.
