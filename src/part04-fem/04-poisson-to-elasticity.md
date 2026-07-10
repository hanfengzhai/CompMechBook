# From Poisson to Elasticity

Poisson's equation taught us the FEM pipeline: weak form, shape functions, assembly, solve. Linear elasticity is not a new method — it is the same pipeline with vector-valued fields, tensor constitutive laws, and a bilinear form built from strain rather than gradient.

The copper wire under tension illustrates the transition cleanly. Steady Joule heating gives a scalar temperature field governed by \(-\Delta T = q\); mechanical loading gives a vector displacement field governed by \(-\nabla\cdot\boldsymbol{\sigma} = \mathbf{f}\). Both problems assemble into \(\mathbf{K}\mathbf{U} = \mathbf{F}\). The difference is in the size of \(\mathbf{U}\), the block structure of \(\mathbf{K}\), and the physical meaning of the entries.

> **Reader's note:** This chapter uses small-strain kinematics and isotropic Hooke's law in the form a FEM code expects. **Part VI** develops the same objects — deformation, stress, balance laws, and variational elasticity — from continuum mechanics first principles. Read here for assembly; return to Part VI for the physics foundation, or skim Part VI Chapters 1–3 first if you prefer definitions before discretization.

## Scene: one wire, two fields

Run current through the copper wire and two simulations appear on the same mesh: a scalar temperature field from Joule heating, and a vector displacement field from thermal expansion plus tension. Poisson gave us the scalar pipeline; elasticity repeats it threefold — same assembly loop, block stiffness matrix, different physics. The wire does not separate those couplings as cleanly as the FEM deck does, but recognizing the pattern saves a semester of relearning.

## Strong form of linear elasticity

In small-displacement theory, the **strain tensor** is

\[
\boldsymbol{\varepsilon}(\mathbf{u}) = \tfrac{1}{2}(\nabla \mathbf{u} + \nabla \mathbf{u}^T),
\]

and **Hooke's law** relates stress to strain:

\[
\boldsymbol{\sigma} = \mathbb{C} : \boldsymbol{\varepsilon}.
\]

Equilibrium with body force \(\mathbf{f}\) is

\[
-\nabla\cdot\boldsymbol{\sigma} = \mathbf{f} \quad \text{in } \Omega.
\]

Boundary conditions partition the surface:

- **Displacement (Dirichlet)**: \(\mathbf{u} = \mathbf{u}_0\) on \(\Gamma_D\).
- **Traction (Neumann)**: \(\boldsymbol{\sigma}\mathbf{n} = \mathbf{t}\) on \(\Gamma_N\).

For isotropic materials, the **fourth-order elasticity tensor** is

\[
\mathbb{C}_{ijkl} = \lambda \delta_{ij}\delta_{kl} + \mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}),
\]

with **Lamé parameters** \(\lambda\) and \(\mu\) related to Young's modulus \(E\) and Poisson's ratio \(\nu\):

\[
\mu = \frac{E}{2(1+\nu)}, \qquad \lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}.
\]

Copper at room temperature has \(E \approx 120\) GPa and \(\nu \approx 0.34\). These numbers enter every quadrature-point evaluation of \(\mathbb{C}\).

## Weak form: virtual work

Multiply the equilibrium equation by a test function \(\mathbf{v}\) vanishing on \(\Gamma_D\) and integrate by parts. The **principle of virtual work** seeks \(\mathbf{u} \in V\) such that

\[
\int_\Omega \boldsymbol{\varepsilon}(\mathbf{u}) : \mathbb{C} : \boldsymbol{\varepsilon}(\mathbf{v}) \, d\Omega = \int_\Omega \mathbf{f}\cdot\mathbf{v} \, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{v} \, dS
\]

for all \(\mathbf{v} \in V_0\). This is the vector analogue of the Poisson weak form from Part III — a bilinear form \(a(\mathbf{u},\mathbf{v})\) plus linear functional \(\ell(\mathbf{v})\).

For isotropic materials, expanding in terms of \(\lambda\) and \(\mu\):

\[
a(\mathbf{u},\mathbf{v}) = \int_\Omega \left[\lambda (\nabla\cdot\mathbf{u})(\nabla\cdot\mathbf{v}) + 2\mu\, \boldsymbol{\varepsilon}(\mathbf{u}):\boldsymbol{\varepsilon}(\mathbf{v})\right] d\Omega.
\]

The \(\lambda\) term couples volumetric response; it is the source of locking when \(\nu \to 1/2\) on low-order elements (Chapter 3).

## Finite element discretization

Approximate displacement as

\[
\mathbf{u}_h = \sum_{a=1}^{N_{\text{nodes}}} N_a(\xi)\, \mathbf{U}_a,
\]

where \(N_a\) are scalar shape functions and \(\mathbf{U}_a \in \mathbb{R}^d\) are nodal displacement vectors. The strain-displacement matrix at a quadrature point expresses \(\boldsymbol{\varepsilon}(\mathbf{u}_h)\) in terms of nodal DOFs:

\[
\boldsymbol{\varepsilon}(\mathbf{u}_h) = \sum_a \mathbf{B}_a \mathbf{U}_a,
\]

where \(\mathbf{B}_a\) is built from \(\nabla N_a\). The element stiffness is

\[
\mathbf{k}^e = \int_{\Omega_e} \mathbf{B}^T \mathbb{C} \mathbf{B}\, d\Omega,
\]

with \(\mathbf{B}\) stacking the \(\mathbf{B}_a\) blocks. Assembly scatters \(\mathbf{k}^e\) into the global block-sparse matrix exactly as in Chapter 2.

## Example: 1D bar revisited as elasticity

Axial deformation of the copper wire is a 1D reduction: \(\mathbf{u} = u(x)\mathbf{e}_x\), \(\varepsilon_{xx} = du/dx\), \(\sigma_{xx} = E\, du/dx\). The weak form reduces to

\[
\int_0^L EA\, u'\, v'\, dx = \int_0^L f v\, dx + F v(L),
\]

identical to the bar element in Chapter 2. Three-dimensional elasticity is this idea with full tensors — no change to the assembly loop, only to the dimension of \(\mathbf{B}\) and \(\mathbb{C}\).

### Worked example: three-node copper bar

Fix numbers from Part I and Part IV: a \(L = 1\,\text{m}\) copper wire segment, \(A = 1\,\text{mm}^2\), \(E = 120\,\text{GPa}\), fixed at \(x = 0\), tensile load \(F = 1000\,\text{N}\) at \(x = L\). Three equally spaced nodes give two bar elements of length \(h = L/2\).

Each element contributes \(k^e = EA/h = (120 \times 10^9)(10^{-6})/0.5 \approx 2.4 \times 10^8\,\text{N/m}\). The global system (DOFs \(u_1, u_2, u_3\) with \(u_1 = 0\)) is

\[
\begin{bmatrix} 2k & -k \\ -k & k \end{bmatrix}
\begin{bmatrix} u_2 \\ u_3 \end{bmatrix}
=
\begin{bmatrix} 0 \\ F \end{bmatrix}.
\]

Solving gives \(u_3 = F/k \approx 4.17\,\mu\text{m}\) and \(u_2 = F/(2k) \approx 2.08\,\mu\text{m}\) — linear displacement along the bar, as expected for uniform stress \(\sigma = F/A = 1\,\text{GPa}\). Refining to five nodes halves the element length and halves the error in the energy norm at the rate Part IV Chapter 5 predicts for P1 bars.

This is not a new method: it is Poisson's equation with a vector-valued unknown and a tensor stiffness. The copper wire under modest tension lives in this 1D reduction until notches, bending, or multiaxial loading demand full 3D \(\mathbf{B}\) matrices — but the assembly loop, boundary conditions, and convergence story are unchanged.

## Example: 2D plane problems

When geometry and loading have translational symmetry, 3D elasticity reduces to 2D:

**Plane strain** (\(\varepsilon_{zz} = 0\)): suitable for long bodies, e.g., a thick wire cross-section far from the ends. A modified \(3 \times 3\) constitutive matrix \(\mathbb{C}^{\text{ps}}\) replaces the full tensor.

**Plane stress** (\(\sigma_{zz} = 0\)): suitable for thin sheets. A different \(\mathbb{C}^{\text{pt}}\) applies.

For a circular copper wire cross-section under uniform tension, plane strain gives an axisymmetric displacement field; exploiting symmetry reduces the problem further to a 1D radial ODE — but a full 2D FEM mesh validates the implementation and handles non-axisymmetric defects (notches, scratches) that break symmetry.

## Thermal and multiphysics coupling

Joule heating raises temperature; thermal expansion generates strain. The **total strain** splits as

\[
\boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}_{\text{mech}} + \alpha \Delta T\, \mathbf{I},
\]

where \(\alpha\) is the coefficient of thermal expansion and \(\Delta T = T - T_{\text{ref}}\). Stress depends on mechanical strain:

\[
\boldsymbol{\sigma} = \mathbb{C} : (\boldsymbol{\varepsilon} - \alpha \Delta T\, \mathbf{I}).
\]

**Coupled thermoelasticity** alternates or monolithically solves:

1. Heat equation: \(\rho c_p\, \partial T/\partial t - \nabla\cdot(k\nabla T) = q\) (FEM, scalar field).
2. Elasticity with thermal eigenstrain (FEM, vector field).

Each step uses the same assembly infrastructure. The copper wire carrying current heats up, expands, and changes stress — three physics, one discretization philosophy.

## Body forces and initial stress

Gravity enters as \(\mathbf{f} = \rho \mathbf{g}\). Centrifugal loads in rotating machinery appear as body forces in a co-rotating frame. **Initial stress** fields (residual stress from manufacturing) enter the weak form as an additional term:

\[
\int_\Omega \boldsymbol{\sigma}_0 : \boldsymbol{\varepsilon}(\mathbf{v})\, d\Omega,
\]

on the right-hand side — prestress without external load.

## From Poisson to elasticity: a correspondence table

| Poisson | Linear elasticity |
|---------|-------------------|
| Scalar \(u\) | Vector \(\mathbf{u}\) |
| \(\int \nabla u\cdot\nabla v\) | \(\int \boldsymbol{\varepsilon}(\mathbf{u}):\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{v})\) |
| Source \(f\) | Body force \(\mathbf{f}\) |
| Dirichlet \(u = g\) | Displacement \(\mathbf{u} = \mathbf{u}_0\) |
| Neumann \(\partial u/\partial n = h\) | Traction \(\boldsymbol{\sigma}\mathbf{n} = \mathbf{t}\) |
| Scalar P1 elements | Vector P1 (same shapes, \(d\) DOFs per node) |

The FEA teaching notes treat heat transfer (Problem Session 9) and structural problems with the same P1 triangle machinery — the student implements Poisson once and reuses the mesh for elasticity.

## Nonlinear elasticity (preview)

Large deformation of the copper wire — or rubber-like materials — requires **hyperelastic** constitutive laws derived from a strain energy density \(\psi(\mathbf{F})\), where \(\mathbf{F} = \mathbf{I} + \nabla\mathbf{u}\) is the deformation gradient (Part VI, Chapter 1). First Piola–Kirchhoff stress is

\[
\mathbf{P} = \frac{\partial \psi}{\partial \mathbf{F}}.
\]

The weak form uses \(\mathbf{P}\) in place of \(\boldsymbol{\sigma}\), integrated over the reference configuration. Newton iterations assemble **tangent stiffness** from \(\partial \mathbf{P}/\partial \mathbf{F}\). Nonlinear FEA is Galerkin plus load stepping and consistent linearization — documented in the author's [Nonlinear FEA notes](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf).

Plasticity adds internal variables and variational inequalities; contact adds constraints. The assembly loop persists; the constitutive update at quadrature points grows richer.

## Implementation checklist

When extending a Poisson solver to elasticity:

1. Expand DOF map: \(d\) components per node.
2. Form \(\mathbf{B}\) matrix from \(\nabla N_a\) at quadrature points.
3. Contract \(\mathbf{B}^T \mathbb{C} \mathbf{B}\) with material properties.
4. Add traction surface integrals on \(\Gamma_N\).
5. Verify patch test with uniform strain fields.
6. Compare against analytical solutions (Kirsch hole, Timoshenko beam) before trusting the mesh.

## Bridge

Poisson's equation and linear elasticity share one assembly loop — scalar versus vector unknowns, gradient versus strain, the same \(\mathbf{K}\mathbf{U}=\mathbf{F}\) pattern Part I introduced on springs. A solver that passes patch tests and looks smooth on the copper wire is not necessarily **accurate**: convergence theory ties mesh size \(h\) and polynomial order \(p\) to quantifiable error bounds in the norms Part II named.

| What this chapter established | What convergence theory (next chapter) supplies |
|--------------------------------|------------------------------------------------|
| Vector P1 elements; block \(\mathbf{B}^T\mathbb{C}\mathbf{B}\) assembly | Céa's lemma: discrete energy tracks continuous minimizer in \(H^1\) |
| 1D bar = Poisson with \(EA\) stiffness; worked three-node wire | Approximation rates \(O(h^p)\) in \(H^1\) and \(L^2\); role of \(H^2\) regularity |
| Thermoelastic coupling: scalar heat + vector displacement on one mesh | A posteriori estimators and adaptive refinement at grip corners |
| Nonlinear hyperelastic preview (Part VI pointer) | When \(p\)-refinement beats \(h\)-refinement; locking at \(\nu \to 1/2\) |

Return to the [prologue](../../prologue/00-many-scales.md): **Act III** ramps grip displacement on a mesh whose axial displacement field is now a vector-valued Poisson story — three components, one assembly habit. The load cell curve in the linear elastic regime is trustworthy only if refinement studies show the discrete solution converging to the weak solution Part III wrote. [II.3](../part02-functional-analysis/03-hilbert-spaces.md) and [III.3](../part03-pdes/03-sobolev-spaces.md) supplied the norms; the next chapter closes the loop between theory and mesh refinement on the copper wire and beyond.

| Prologue act | FEM output on the wire | Convergence question the next chapter answers |
|--------------|------------------------|-----------------------------------------------|
| II — Warming | Scalar temperature field on the same mesh | Does \(\|T-T_h\|_{H^1}\to 0\) as \(h\to 0\)? |
| III — Pulling | Vector \(\mathbf{U}\) from block \(\mathbf{K}\) assembly | Céa's lemma: energy error \(\le C h^p \|u\|_{H^{p+1}}\) |
| IV — Hardening (preview) | Linear elastic slope before yield | When does \(p\)-refinement beat \(h\)-refinement at the grip corner? |
| V — Notch (preview) | Refined mesh at stress concentrator | A posteriori estimators and adaptive \(h\)-refinement |

Turn the page when patch tests pass but the grip displacement still changes when you halve \(h\) — that is the signal that convergence theory, not intuition, must certify the answer.
