# Kinematics: How Bodies Move and Deform

Continuum mechanics describes matter as a continuous map from a **reference configuration** to a **current configuration**. Kinematics is the geometry of that map — how lengths, areas, and volumes change; how lines rotate and stretch — independent of forces and material response.

Parts IV and V discretized PDEs on meshes. Part VI asks what those PDEs mean physically: what is strain, what is stress, and how do balance laws connect them? If you arrived via Part IV, recall the nodal displacement vector \(\mathbf{U}\): each entry \(U_i\) is a sample of a continuous field \(\mathbf{u}(\mathbf{X})\) at a mesh node. If you arrived via Part V, recall the cell-averaged velocity \(\bar{\mathbf{v}}\): it is a piecewise-constant proxy for a smooth \(\mathbf{v}(\mathbf{x})\). Part VI names the continuous objects both proxies approximate.

The copper wire under tension is our recurring specimen — at the continuum scale, it is a cylinder of copper with a displacement field and a deformation gradient that Part IV's elasticity code approximates node by node, while the air cooling it (Part V) carries a velocity field whose gradient enters the rate-of-deformation tensor in the fluid stress.

## Closing the arc from Parts IV and V (discretization fork) {#continuum-opening-hinge-discretization-to-kinematics}

If you walked through [V.4's intermission](../part05-fvm/04-navier-stokes-cfd.md#intermission-discretization-complete-continuum-begins) and [Bridge to Part VI](../part05-fvm/04-navier-stokes-cfd.md#bridge-to-part-vi), or arrived via [IV.5 Door B](../part04-fem/05-convergence.md#bridge-two-doors-from-here) straight to [Part VI opening](../part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead), the copper wire has been solved twice on the computer without yet receiving a unified geometric vocabulary. [Part VI opening — Twin ladders reunite](../part06-continuum/00-opening.md#the-twin-ladders-reunite-galerkin-and-conservation) replays the full FEM↔FVM comparison table and the [midpoint anchor](../part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead); this chapter is the **first rung** — deformation gradient \(\mathbf{F}\) before Cauchy stress or virtual work.

| Parts IV–V (discretization on the wire) | Part VI.1 (kinematics on the wire) |
|----------------------------------------|-------------------------------------|
| Nodal displacements \(\mathbf{U}\) from shape functions | Continuous map \(\boldsymbol{\varphi}(\mathbf{X}, t)\); displacement \(\mathbf{u}(\mathbf{X})\) |
| Assembled \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from Galerkin | Deformation gradient \(\mathbf{F} = \partial\mathbf{x}/\partial\mathbf{X}\) sampled at Gauss points |
| Cell-averaged velocity \(\bar{\mathbf{v}}\) (Part V) | Rate of deformation \(\mathbf{D} = \text{sym}(\nabla\mathbf{v})\) as fluid-side kinematic cousin |
| Face fluxes \(\mathbf{F}\cdot\mathbf{n}\) at the wire surface | Reference and current configurations; stretch and rotation of material lines |
| CHT loop exports \(T_w \approx 379\,\text{K}\) in `cht_export.yaml` | Thermal expansion strain increment \(\alpha\Delta T\,\mathbf{I}\) added to mechanical \(\boldsymbol{\varepsilon}\) |

Parts IV and V answered *how* to discretize PDEs on meshes and control volumes; this chapter asks *what continuous map* those nodal values and cell averages sample. The load cell in **Act III** records force against grip displacement — kinematics names the **stretch** \(\lambda = 1 + u'/L\) behind that displacement before [VI.2](02-stress-balance.md) names the Cauchy stress conjugate to it. When the [preface ascent continuity hinge](../preface.md#ascent-continuity-hinges) lists **discretization fork → continuum**, this section is where sparse arrays become tensor fields — the first chapter where \(\mathbf{F}\) replaces \(\mathbf{U}\) as the primary object.

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

### Worked example: 0.1% axial strain on the wire

Take the prologue specimen: \(L = 1\,\text{m}\), grip displacement \(\Delta = 1\,\text{mm}\) so \(\lambda = 1.001\) and \(\varepsilon_{11} \approx \Delta/L = 10^{-3}\). With copper \(\nu \approx 0.34\), linear kinematics predicts lateral contraction \(\varepsilon_{22} = \varepsilon_{33} \approx -\nu\varepsilon_{11} \approx -3.4 \times 10^{-4}\) — the wire narrows slightly as it lengthens, a geometric fact every tensile test records even when the load cell dominates the display.

In finite strain language, \(F_{11} = 1.001\) and \(F_{22} \approx 1 - \nu(\lambda - 1) \approx 0.99966\), so \(J = \det\mathbf{F} \approx 0.99933 < 1\): the bar loses a small amount of volume in linear theory because Poisson contraction does not fully compensate axial stretch. Part IV's 3D elasticity code computes these contractions from the \(B\)-matrix automatically; this chapter names the \(\mathbf{F}\) those shape-function gradients assemble.

When the grips ramp further and the force–displacement curve bends (**Act IV**), \(\mathbf{F}\) ceases to be close to \(\mathbf{I} + \nabla\mathbf{u}\) and Green–Lagrange \(\mathbf{E}\) replaces the infinitesimal strain — the kinematic handoff [VI.4](04-nonlinear-plasticity-preview.md) develops.

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

## Polar decomposition: stretch and rotation on the wire

The polar decomposition \(\mathbf{F} = \mathbf{R}\mathbf{U}\) separates **how much** a material line stretches from **how much** it rotates. For the copper wire in a tensile frame with negligible grip misalignment, \(\mathbf{R} \approx \mathbf{I}\) and \(\mathbf{U} \approx \mathbf{I} + \boldsymbol{\varepsilon}\) in the linear elastic regime — but the split becomes essential when torsion, bending, or large rigid-body motion enters the story.

Take uniaxial tension along \(\mathbf{e}_1\) with small engineering strain \(\varepsilon_{11} = 10^{-3}\) and Poisson contraction \(\varepsilon_{22} = \varepsilon_{33} = -\nu\varepsilon_{11}\). In matrix form (Voigt-style ordering for intuition):

\[
\mathbf{F} \approx \begin{bmatrix} 1.001 & 0 & 0 \\ 0 & 0.99966 & 0 \\ 0 & 0 & 0.99966 \end{bmatrix}, \qquad \mathbf{R} \approx \mathbf{I}.
\]

The stretch tensor \(\mathbf{U} = \sqrt{\mathbf{F}^T\mathbf{F}}\) has eigenvalues \(\lambda_i = 1 + \varepsilon_{ii}\) on the principal axes — the same numbers Part IV's \(B\)-matrix assembles from shape-function gradients. If the grips introduce a 0.1° misalignment, a small rotation \(\mathbf{R}\) appears; subtracting it before comparing to a 1D bar model prevents attributing geometric tilt to material nonlinearity.

| Object | Role on the wire | FEM/FVM counterpart |
|--------|------------------|----------------------|
| \(\mathbf{R}\) | Rigid rotation of the specimen in the frame | Rigid-body mode removal in assembly |
| \(\mathbf{U}\) | Symmetric stretch from reference to current | Strain at Gauss points from \(\mathbf{F}\) |
| \(J = \det\mathbf{F}\) | Volume ratio | Volumetric locking checks (\(\nu \to 1/2\)) |
| \(\bar{\mathbf{F}} = J^{-1/d}\mathbf{F}\) | Isochoric (shape) part | Split formulations in hyperelasticity |

When the wire necks in **Act IV**, \(\mathbf{F}\) is no longer diagonal: \(\mathbf{U}\) captures the local axial thinning and circumferential contraction, while \(\mathbf{R}\) tracks how material lines rotate into the neck. Part IV's nonlinear extensions evaluate \(\mathbf{F}\) at quadrature points and pass \(\mathbf{U}\) or \(\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F}-\mathbf{I})\) to the constitutive routine — the polar split is the geometric sanity check that rigid motion does not generate spurious stress.

## Lab act: read lateral contraction from grip displacement (Act III)

**Act III** prescribes axial end displacement; a caliper on the wire diameter tells a kinematic story Part IV's 1D bar model ignores. Continuum kinematics names that story before Part VI.2 adds stress.

Take uniaxial tension along the wire axis \(\mathbf{e}_1\), small strain, isotropic copper with \(\nu = 0.34\). The grip holds \(\varepsilon_{11} = \Delta L/L = 10^{-4}\) (10 microstrain on a 1 m gauge length — still in the linear elastic climb before Act IV hardening).

| Object | Formula | Numeric value |
|--------|---------|---------------|
| Axial stretch | \(\lambda_1 = 1 + \varepsilon_{11}\) | \(1.0001\) |
| Lateral strains | \(\varepsilon_{22} = \varepsilon_{33} = -\nu \varepsilon_{11}\) | \(-3.4 \times 10^{-5}\) |
| Diameter change | \(\Delta D/D \approx \varepsilon_{22}\) (small strain) | \(-34\,\mu\text{m}\) on \(D = 1\,\text{mm}\) |
| Volume change (small strain) | \(\varepsilon_v = \varepsilon_{11} + \varepsilon_{22} + \varepsilon_{33} = (1-2\nu)\varepsilon_{11}\) | \(\approx 3.2 \times 10^{-5}\) |

Measure with a micrometer (or simulate a 3D hex mesh with one constrained face): if \(\varepsilon_{22} \approx 0\) while \(\varepsilon_{11} > 0\), the material model is **not** isotropic Hooke — or the \(B\)-matrix is wrong. If \(\varepsilon_{22}/\varepsilon_{11} \approx -\nu\) within experimental noise, the kinematic half of Hooke's law is consistent with the load cell reading from Act III.

For finite strain preview: \(\mathbf{F} = \text{diag}(\lambda_1, \lambda_2, \lambda_2)\) with \(\lambda_2 = 1 + \varepsilon_{22}\) gives \(J = \lambda_1 \lambda_2^2 \approx 1 + (1-2\nu)\varepsilon_{11}\) to first order — the same volume change. When Act IV later ramps into plasticity, \(J\) and deviatoric \(\bar{\mathbf{F}}\) split in [VI.4](04-nonlinear-plasticity-preview.md); this Lab act is the linear elastic baseline those splits generalize.

## Concept map checkpoint (kinematics)

This chapter is where Part IV's nodal displacements acquire geometric meaning. Before stress balance adds forces, summarize what kinematics established:

| Question | Part VI answer (copper wire) |
|----------|------------------------------|
| What **object**? | Deformation gradient \(\mathbf{F}\); strain \(\boldsymbol{\varepsilon}\), \(\mathbf{E}\), rate \(\mathbf{D}\) |
| What **structure**? | Polar decomposition \(\mathbf{F}=\mathbf{R}\mathbf{U}\); volumetric/deviatoric split |
| What **theorem**? | Objectivity: constitutive laws depend on stretch, not rigid rotation |
| What **breaks**? | Infinitesimal \(\boldsymbol{\varepsilon}\) when \(\|\nabla\mathbf{u}\|\) is not small; 1D bar ignores lateral contraction |

The Lab act linked grip displacement to measurable diameter change via \(\varepsilon_{22} = -\nu\varepsilon_{11}\). Part IV's \(B\)-matrix is the discrete shadow of \(\boldsymbol{\varepsilon}(\mathbf{u})\) defined here; Part V's velocity field is the rate counterpart \(\mathbf{D}\).

## Bridge

Kinematics names the geometric objects — \(\mathbf{F}\), \(\boldsymbol{\varepsilon}\), \(\mathbf{E}\), \(\mathbf{D}\). Forces enter through **stress tensors** and **balance laws** that constrain how stress varies in space and time.

| What VI.1 (kinematics) established | What VI.2 (balance laws) must supply |
|------------------------------------|--------------------------------------|
| \(\mathbf{F}\), \(\boldsymbol{\varepsilon}\), \(\mathbf{E}\), \(\mathbf{D}\) | Cauchy stress \(\boldsymbol{\sigma}\); traction \(\boldsymbol{\sigma}\mathbf{n}\) on boundaries |
| Axial stretch \(\lambda\) and lateral contraction from \(\nu\) on the wire | Momentum balance \(\nabla\cdot\boldsymbol{\sigma}+\mathbf{b}=\mathbf{0}\) |
| \(B\)-matrix as discrete shadow of \(\boldsymbol{\varepsilon}(\mathbf{u})\) ([IV.4](../part04-fem/04-poisson-to-elasticity.md)) | Hooke's law \(\boldsymbol{\sigma}=\mathbb{C}:\boldsymbol{\varepsilon}\) closes the system |
| \(\mathbf{D}\) as rate counterpart to FVM velocity ([V.4](../part05-fvm/04-navier-stokes-cfd.md)) | Thermal balance linking **Act II** Joule heating to stress-free strain |

**Scale-boundary handshake (VI.1 → VI.2 → Acts II/III).**

| Kinematic export (this chapter) | Balance consumer ([VI.2](02-stress-balance.md)) | Discretization home (Parts IV–V) | Failure mode |
|-----------------------------------|--------------------------------------------------|----------------------------------|--------------|
| Deformation gradient \(\mathbf{F} = \mathbf{I} + \nabla\mathbf{u}\) | Cauchy stress \(\boldsymbol{\sigma}\); traction \(\boldsymbol{\sigma}\mathbf{n}\) | Part IV \(B\)-matrix in [IV.4](../part04-fem/04-poisson-to-elasticity.md) | Infinitesimal \(\boldsymbol{\varepsilon}\) when \(\|\nabla\mathbf{u}\|\) is not small |
| Lateral contraction \(\varepsilon_{22} = -\nu\varepsilon_{11}\) | Hooke \(\boldsymbol{\sigma}=\mathbb{C}:\boldsymbol{\varepsilon}\) closes equilibrium | Micrometer check on wire diameter (Lab act) | 1D bar model ignoring Poisson effect |
| Objectivity: \(\mathbf{F}=\mathbf{R}\mathbf{U}\) | Constitutive laws depend on stretch, not rotation | Isoparametric Jacobian in [IV.3](../part04-fem/03-elements-quadrature.md) | Mixing rigid rotation into strain measure |
| Rate \(\mathbf{D}\) for transient kinematics | Thermal eigenstrain \(\varepsilon_{\text{th}}=\alpha\Delta T\) | Part V velocity field in [V.4](../part05-fvm/04-navier-stokes-cfd.md) | Thermal stress omitted in pure mechanical run |
| Volumetric/deviatoric split of \(\mathbf{F}\) | Energy balance for Joule heating (Act II) | Coupled thermoelastic assembly | Robin BC at wire surface not passed to FVM |

The micrometer Lab act is the geometric patch test: if \(\varepsilon_{22}/\varepsilon_{11} \approx -\nu\) within experimental noise, the kinematic half of Hooke's law is consistent with the load cell reading from **Act III**. If lateral strain vanishes while axial stretch is nonzero, the fault is not the sensor — it is a constitutive or \(B\)-matrix mismatch between what Part IV assembled and what this chapter defines.

Return to the [prologue](../prologue/00-many-scales.md): **Act III — Pulling** ramps grip displacement while **Act II — Warming** still feeds thermal eigenstrain through \(\alpha\Delta T\). Parts [IV](../part04-fem/04-poisson-to-elasticity.md) and [V](../part05-fvm/04-navier-stokes-cfd.md) already computed temperature and flux fields on their respective meshes; Part IV assembled nodal displacements from shape functions. This chapter explains **what those numbers mean geometrically** — axial stretch \(\lambda = 1 + u'/L\), lateral contraction from \(\nu\), and the finite-strain objects that nonlinear extensions in [VI.4](04-nonlinear-plasticity-preview.md) require.

The [preface continuity hinges](../preface.md#continuity-hinges-ascent-descent) name [Part VI opening](../part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead) as the **mathematical midpoint** where FEM and FVM converge on Cauchy stress. Kinematics is the first half of that reunion: strain tensors both discretizations approximate, now named in continuum language rather than nodal values or cell averages.

[VI.2](02-stress-balance.md) is where the load cell's force in **Act III** acquires a Cauchy stress conjugate — kinematics without balance is geometry without physics. Turn the page when displacement fields need a stress tensor to pair with strain, or when the micrometer and load cell disagree and you suspect missing coupling rather than bad hardware. If the Lab act confirmed Poisson contraction but the load cell reading still lacks a stress tensor behind it, continue to [VI.2's opening hinge](02-stress-balance.md#balance-opening-hinge-kinematics-to-stress), where Cauchy stress \(\boldsymbol{\sigma}\) replaces \(\mathbf{F}\) as the primary object for the first time since Part VI began.
