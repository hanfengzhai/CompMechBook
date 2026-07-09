# Kinematics: How Bodies Move and Deform

Continuum mechanics describes matter as a continuous map from a **reference configuration** to a **current configuration**. Kinematics is the geometry of that map — how lengths, areas, and volumes change; how lines rotate and stretch — independent of forces and material response.

Parts IV and V discretized PDEs on meshes. Part VI asks what those PDEs mean physically: what is strain, what is stress, and how do balance laws connect them? If you arrived via Part IV, recall the nodal displacement vector \(\mathbf{U}\): each entry \(U_i\) is a sample of a continuous field \(\mathbf{u}(\mathbf{X})\) at a mesh node. If you arrived via Part V, recall the cell-averaged velocity \(\bar{\mathbf{v}}\): it is a piecewise-constant proxy for a smooth \(\mathbf{v}(\mathbf{x})\). Part VI names the continuous objects both proxies approximate.

The copper wire under tension is our recurring specimen — at the continuum scale, it is a cylinder of copper with a displacement field and a deformation gradient that Part IV's elasticity code approximates node by node, while the air cooling it (Part V) carries a velocity field whose gradient enters the rate-of-deformation tensor in the fluid stress.

## Scene: the wire in the tensile frame

Picture a 1 mm diameter copper wire, 100 mm gauge length, gripped at both ends in a tensile frame. A 50 N axial load produces a modest engineering strain \(\varepsilon \approx \sigma/E \sim 10^{-4}\) — well within the linear elastic range Part IV assumed when assembling \(\mathbf{K}\). Every node on the FEM mesh carries a displacement vector; kinematics asks what **continuous map** those nodal values sample.

Fix a material point on the wire axis at reference position \(X = 50\) mm (mid-span). After loading, it moves to \(x = 50.005\) mm — a 5 µm axial displacement. Locally,

\[
\mathbf{F} \approx \mathbf{I} + \varepsilon_{xx}\,\mathbf{e}_x\mathbf{e}_x^T, \qquad \varepsilon_{xx} \approx \frac{\partial u_x}{\partial X} \approx 5\times 10^{-5},
\]

with Poisson contraction \( \varepsilon_{yy} = \varepsilon_{zz} \approx -\nu\varepsilon_{xx}\) shrinking the diameter slightly. Part IV's three-node bar example (Part I, Chapter 1) captured the same physics in one dimension; Part VI now names the **three-dimensional object** \(\mathbf{F}\) that a 3D hex mesh approximates at each Gauss point.

If the load increases until the wire yields, \(\mathbf{F}\) ceases to be infinitesimally close to \(\mathbf{I}\) near necking regions — hyperelastic and plastic formulations track \(\mathbf{F}\) directly. If the wire heats from Joule current, thermal expansion adds a strain increment \(\alpha\Delta T\,\mathbf{I}\) on top of mechanical \(\boldsymbol{\varepsilon}\). Kinematics does not assign causality (that is constitutive law in the next chapter); it records **how** each point moved and stretched so stress and balance laws have geometric input.

```mermaid
flowchart LR
  X[Reference X on wire axis] --> phi[Deformation map phi]
  phi --> x[Current position x]
  x --> F[Deformation gradient F]
  F --> eps[Strain epsilon or E]
  eps --> IV[Part IV B-matrix at Gauss points]
```

## Configurations and the deformation map

Let \(\mathbf{X}\) denote a material point in the **reference configuration** \(\Omega_0\) (typically the undeformed body at \(t = 0\)). Its location in the **current configuration** \(\Omega\) at time \(t\) is

\[
\mathbf{x} = \boldsymbol{\varphi}(\mathbf{X}, t).
\]

The map \(\boldsymbol{\varphi}: \Omega_0 \to \Omega\) is assumed invertible and sufficiently smooth — no tearing or interpenetration. **Displacement** is

\[
\mathbf{u}(\mathbf{X}, t) = \mathbf{x} - \mathbf{X}.
\]

In small-displacement linear elasticity (Part IV), \(\mathbf{u}\) is treated as a vector field on a fixed domain — a linearization of \(\boldsymbol{\varphi}\) about the identity. In finite deformation theory, \(\boldsymbol{\varphi}\) is primary.

## Deformation gradient

The **deformation gradient** is

\[
\mathbf{F} = \frac{\partial \mathbf{x}}{\partial \mathbf{X}} = \mathbf{I} + \frac{\partial \mathbf{u}}{\partial \mathbf{X}}.
\]

Columns of \(\mathbf{F}\) are the images of reference basis vectors in the current configuration. It encodes local stretch, shear, and rotation.

**Volume change**: an infinitesimal reference volume \(dV_0\) maps to \(dV = J\, dV_0\) with \(J = \det \mathbf{F}\). Incompressibility (rubber-like materials, liquid metals in certain regimes) requires \(J = 1\).

**Polar decomposition**: \(\mathbf{F} = \mathbf{R}\mathbf{U} = \mathbf{V}\mathbf{R}\), with orthogonal rotation \(\mathbf{R}\) and symmetric positive-definite stretch \(\mathbf{U}\) (or \(\mathbf{V}\)). Rigid motion has \(\mathbf{F} = \mathbf{R}\), \(\mathbf{U} = \mathbf{I}\).

For the copper wire in modest tension, \(|\mathbf{u}| \ll L\) and \(\mathbf{F} \approx \mathbf{I} + \varepsilon_{xx}\mathbf{e}_x\mathbf{e}_x^T\) with \(\varepsilon_{xx} = \partial u_x/\partial X \ll 1\).

## Strain measures

Different strain tensors suit different regimes. Mixing them inconsistently — using small strain in a hyperelastic energy while \(\mathbf{F}\) deviates strongly from identity — is a common source of bugs in multiphysics codes.

**Infinitesimal strain** (linear elasticity, Part IV):

\[
\boldsymbol{\varepsilon} = \tfrac{1}{2}(\nabla \mathbf{u} + \nabla \mathbf{u}^T).
\]

Valid when \(|\nabla \mathbf{u}| \ll 1\). The copper wire below yield in uniaxial tension lives here.

**Green–Lagrange strain** (finite deformation, reference configuration):

\[
\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I}).
\]

Measures stretch from reference to current; zero under rigid motion. Used in hyperelastic FEM with constitutive laws \(\psi(\mathbf{E})\) or \(\psi(\mathbf{F})\).

**Almansi strain** (current configuration):

\[
\mathbf{e} = \tfrac{1}{2}(\mathbf{I} - \mathbf{F}^{-T}\mathbf{F}^{-1}).
\]

**Rate of deformation** (fluids, Eulerian description, Part V):

\[
\mathbf{D} = \tfrac{1}{2}(\nabla \mathbf{v} + \nabla \mathbf{v}^T),
\]

where \(\mathbf{v}\) is velocity in the current configuration. Navier–Stokes viscous stress uses \(\mathbf{D}\); solid mechanics uses \(\boldsymbol{\varepsilon}\) or \(\mathbf{E}\). The copper wire's cooling air is \(\mathbf{D}\); the wire itself under slow loading is \(\boldsymbol{\varepsilon}\).

## Material vs. spatial descriptions

**Lagrangian (material)**: fields are functions of \(\mathbf{X}\) and \(t\). Time derivatives follow material particles. Natural for solid mechanics and FEM on the reference mesh.

**Eulerian (spatial)**: fields are functions of \(\mathbf{x}\) and \(t\). Natural for fluids and FVM on a fixed or moving spatial grid.

The **material derivative** connects them:

\[
\frac{D(\cdot)}{Dt} = \frac{\partial (\cdot)}{\partial t} + \mathbf{v}\cdot\nabla (\cdot).
\]

Fluid balance laws in Part V use \(D/Dt\); solid balance laws in Lagrangian form integrate over \(\Omega_0\).

## Compatibility and integrability

For a simply connected body, a symmetric strain field derives from a displacement field if **Saint-Venant's compatibility equations** hold (curl of strain vanishes in an appropriate sense). In 2D:

\[
\frac{\partial^2 \varepsilon_{xx}}{\partial y^2} + \frac{\partial^2 \varepsilon_{yy}}{\partial x^2} = 2\frac{\partial^2 \varepsilon_{xy}}{\partial x \partial y}.
\]

FEM shape functions that interpolate displacement automatically produce compatible strains — a hidden benefit of the displacement-based formulation in Part IV.

Incompatible strain fields (e.g., from direct strain interpolation without potential) can violate geometry and produce spurious locking or non-convergence.

## Example: uniform uniaxial stretch

Stretch a copper wire uniformly in the axial direction by factor \(\lambda = 1 + \delta/L\):

\[
x_1 = \lambda X_1, \qquad x_2 = X_2, \qquad x_3 = X_3.
\]

Then \(\mathbf{F} = \text{diag}(\lambda, 1, 1)\), \(J = \lambda\). Green–Lagrange strain \(E_{11} = \tfrac{1}{2}(\lambda^2 - 1)\). For small \(\lambda - 1\), \(E_{11} \approx \lambda - 1 = \varepsilon_{11}\).

Poisson contraction in real copper gives \(F_{22} = F_{33} = \sqrt{1/\lambda}\) approximately for incompressible limit — or \(F_{22} = 1 - \nu(\lambda - 1)\) in linear theory.

## Example: simple shear

\[
x_1 = X_1 + \gamma X_2, \qquad x_2 = X_2.
\]

\(\mathbf{F} = \begin{bmatrix} 1 & \gamma & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\), \(J = 1\). Infinitesimal shear strain \(\varepsilon_{12} = \gamma/2\). Pure shear tests material models and FEM implementations (constant strain triangle reproduces exactly).

## Connection to Part IV FEM

Part IV's linear elasticity uses \(\boldsymbol{\varepsilon}(\mathbf{u})\) from infinitesimal strain. The **B-matrix** in assembly is built from \(\nabla N_a\); it assumes small displacement. Nonlinear elasticity (Part IV, Chapter 4 preview) uses \(\mathbf{F}\) at quadrature points:

\[
\mathbf{F}_h = \mathbf{I} + \sum_a \mathbf{U}_a \otimes \nabla_{X} N_a.
\]

Hyperelastic stress \(\mathbf{P} = \partial\psi/\partial\mathbf{F}\) enters the weak form integrated over \(\Omega_0\). Kinematics is not optional metadata — it defines the constitutive input at every quadrature call.

## Connection to Parts I–III

- Part I: displacement on a mesh is a vector \(\mathbf{U} \in \mathbb{R}^{dN}\); \(\mathbf{F}\) at a point is a \(3 \times 3\) matrix — a linear map from Part I's Chapter 2.
- Part II: displacement fields live in \(H^1\); \(\mathbf{F}\) requires \(W^{1,p}\) regularity for finite energy in nonlinear elasticity.
- Part III: weak form of elasticity uses \(\boldsymbol{\varepsilon}(\mathbf{u})\), derived from kinematics via the chain rule of differentiation.

## Objectivity and frame indifference

Constitutive laws must be **frame-indifferent** (objective): rigid superposed motion should not generate stress. Strain measures built from \(\mathbf{F}\) (Green–Lagrange, left Cauchy–Green \(\mathbf{B} = \mathbf{F}\mathbf{F}^T\)) satisfy this; naive use of \(\partial u_i / \partial x_j\) in Eulerian form does not without careful transport.

The author's [elasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf) develop tensor algebra and coordinate transformations — essential reading for implementing 3D constitutive routines.

## Volumetric and deviatoric split

Many constitutive laws separate deformation into **volumetric** (volume-changing) and **deviatoric** (shape-changing) parts:

\[
J = \det \mathbf{F}, \qquad \mathbf{F} = J^{1/d}\,\bar{\mathbf{F}}, \qquad \det \bar{\mathbf{F}} = 1.
\]

Nearly incompressible materials respond stiffly to volumetric strain — the kinematic split motivates mixed \(u\)–\(p\) formulations in Part IV and explains why \(\mathbf{F}\) is evaluated in both its isochoric and volumetric parts in modern hyperelastic models.

For small strain, the trace \(\text{tr}(\boldsymbol{\varepsilon}) = \nabla\cdot\mathbf{u}\) plays the same volumetric role. Poisson's ratio \(\nu\) controls how axial stretch of the copper wire couples to lateral contraction — a kinematic constraint encoded in the elastic tensor.

## Bridge

Kinematics names the geometric objects — \(\mathbf{F}\), \(\boldsymbol{\varepsilon}\), \(\mathbf{E}\), \(\mathbf{D}\). Forces enter through **stress tensors** and **balance laws** that constrain how stress varies in space and time.

| What Parts IV–V computed | What this chapter names |
|--------------------------|-------------------------|
| Nodal displacements \(\mathbf{U}\) on a mesh | \(\mathbf{u}(\mathbf{x})\) and deformation gradient \(\mathbf{F}\) |
| Strain from the \(B\)-matrix | \(\boldsymbol{\varepsilon}\), \(\mathbf{E}\), rate \(\mathbf{D}\) |
| Thermal expansion in the Joule-heating scene | Volumetric part \(J = \det\mathbf{F}\); Poisson lateral contraction |
| FVM velocity field in the cooling air | \(\mathbf{D}\) as symmetric part of \(\nabla\mathbf{v}\) |

Return to the prologue's **Act III — Pulling**: grip displacement ramps, and the load cell records force. Parts IV and VI already computed that curve from weak forms and assembly; this chapter explains **what was being measured** — axial stretch \(\lambda = 1 + u'/L\), lateral contraction from \(\nu\), and the finite-strain objects that nonlinear extensions in [VI.4](04-nonlinear-plasticity-preview.md) require. The next chapter completes the continuum picture: Cauchy stress, Piola–Kirchhoff stress, conservation of mass and momentum, and constitutive relations that FEM and FVM discretize. Turn the page when displacement fields need a stress conjugate — kinematics without balance is geometry without physics.
