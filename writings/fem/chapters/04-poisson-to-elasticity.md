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

## Cubic copper: when isotropic elasticity is enough

Cold-drawn copper wire is **polycrystalline**: thousands of grains with random orientations. At the engineering scale of a tensile test, the wire looks isotropic — Young's modulus \(E \approx 120\,\text{GPa}\) and Poisson's ratio \(\nu \approx 0.34\) enter the Lamé formulas above. At the crystal scale, copper is **cubic** with three independent elastic constants \(C_{11}\), \(C_{12}\), \(C_{44}\) that Part IX's DFT workflows compute from strained unit cells.

The bridge between scales is a **Voigt average** over grain orientations. For a random polycrystal, the isotropic moduli are

\[
E = \frac{9K\mu}{3K + \mu}, \qquad \nu = \frac{3K - 2\mu}{2(3K + \mu)},
\]

with bulk modulus \(K = (C_{11} + 2C_{12})/3\) and shear modulus \(\mu = C_{44}\) for cubic symmetry. Typical DFT values (PBE, room-temperature reference) give \(C_{11} \approx 170\,\text{GPa}\), \(C_{12} \approx 124\,\text{GPa}\), \(C_{44} \approx 76\,\text{GPa}\) — Voigt-averaged \(E \approx 130\,\text{GPa}\), close to but not identical to the 120 GPa used in earlier chapters (cold work, temperature, and functional choice shift the number).

| Modeling choice | Constitutive input | When to use on the wire |
|-----------------|-------------------|-------------------------|
| Isotropic \(E\), \(\nu\) | Two scalars at each Gauss point | Uniform tension, bending, Joule heating on a drawn wire |
| Cubic \(\mathbb{C}\) with texture | \(C_{ijkl}\) + orientation field | Textured cable, drawn single-crystal filament |
| Polycrystal RVE | Grain-level \(\mathbb{C}\) per element | Notch nucleation where grain boundaries matter |

In the FEM assembly loop, the only change for cubic elasticity is the **quadrature-point tensor** \(\mathbb{C}\): instead of contracting with \(\lambda\) and \(\mu\) scalars, \(\mathbf{B}^T \mathbb{C} \mathbf{B}\) uses the full \(6 \times 6\) Voigt form. The weak form, shape functions, and scatter map are unchanged — the same lesson Part I taught when a bar element's stiffness was a \(1 \times 1\) block inside a larger \(\mathbf{K}\).

For the copper wire through Act III, isotropic \(E\) and \(\nu\) are honest: the cold-drawn specimen's texture is weak enough that a 10% spread in local stiffness averages out over the gauge length. When Act V introduces a notch or Act VII activates slip on preferred {111} planes, the isotropic shortcut becomes the **first failure mode** of the multiscale story — and the DFT-derived \(C_{ij}\) from Part IX supply the anisotropic correction. Document which row of the table your input deck uses; the epilogue's sensitivity analysis ranks elastic constants third in the linear regime but first near yield.

## Thermal and multiphysics coupling

Joule heating raises temperature; thermal expansion generates strain. The **total strain** splits as

\[
\boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}_{\text{mech}} + \alpha \Delta T\, \mathbf{I},
\]

where \(\alpha\) is the coefficient of thermal expansion and \(\Delta T = T - T_{\text{ref}}\). Stress depends on mechanical strain:

\[
\boldsymbol{\sigma} = \mathbb{C} : (\boldsymbol{\varepsilon} - \alpha \Delta T\, \mathbf{I}).
\]

<a id="coupled-thermoelasticity"></a>

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

## Lab act: one mesh, two fields (Act II–III on the copper wire)

When current flows through the wire (Act II — warming), Joule heating produces a scalar temperature field; when grips ramp displacement (Act III — pulling), a vector displacement field appears on the **same** mesh. This lab act walks through coupling both on a minimal 1D bar mesh — the same infrastructure Part IV uses for 3D thermoelasticity.

**Setup.** Three-node bar from the worked example above: \(L = 1\,\text{m}\), \(A = 1\,\text{mm}^2\), copper properties \(E = 120\,\text{GPa}\), \(\nu = 0.34\), \(\alpha = 17 \times 10^{-6}\,\text{K}^{-1}\), thermal conductivity \(k_{\text{th}} = 400\,\text{W/(m·K)}\). Uniform Joule heating \(q = 10^7\,\text{W/m}^3\) (order of magnitude for a thin wire carrying a few amperes).

**Pass 1 — scalar heat (Poisson pipeline).** Solve \(-k_{\text{th}} T'' = q\) with \(T(0) = T(L) = 293\,\text{K}\). On three nodes the discrete system is the same tridiagonal pattern as the bar stiffness but with \(k_{\text{th}}/h\) replacing \(EA/h\). The mid-node temperature rises above the grips — parabolic profile, maximum at center.

**Pass 2 — vector elasticity with thermal strain.** Insert thermal eigenstrain \(\varepsilon_{\text{th}} = \alpha \Delta T\) into Hooke's law:

\[
\sigma = E(\varepsilon_{\text{mech}} - \alpha \Delta T).
\]

With grips fixed (\(u = 0\) at both ends), the wire cannot expand freely: thermal strain becomes **compressive stress** even without mechanical load. The weak form right-hand side picks up a thermal load term proportional to \(\int \alpha \Delta T\, \varepsilon(v)\, d\Omega\) — no external force, yet nonzero stress.

| Pass | Unknown | Governing operator | Copper-wire observation |
|------|---------|--------------------|-------------------------|
| 1 (heat) | Scalar \(T\) | \(-k_{\text{th}}\Delta T = q\) | Mid-span hotter than grips |
| 2 (elastic) | Vector \(\mathbf{u}\) | \(-\nabla\cdot\boldsymbol{\sigma} = \mathbf{0}\) with thermal strain | Compressive stress at fixed grips |
| Coupled | Both | Alternating or monolithic solve | Load cell reads tension + thermal compression |

**Pass 3 — mechanical load on top.** Add tensile force \(F = 1000\,\text{N}\) at \(x = L\) (Act III). The total stress is superposition of thermal compression and mechanical tension. If \(F\) is small, the wire remains in net compression; above a threshold, the load cell shows tension — the same superposition Part VI writes as total strain splitting.

**What this lab act teaches:** Poisson and elasticity are not two solvers — they are one assembly loop with different DOF counts and constitutive tensors. Multiphysics codes (CalculiX, FEniCS, MOOSE) alternate Pass 1 and Pass 2 on the same mesh; the copper wire in the lab never separates heating from stretching, and neither should the FEM deck. When Part V adds air cooling at the surface, the heat pass gains a Robin boundary flux; the elastic pass is unchanged — same pattern, richer boundary data.

## Concept map checkpoint (Poisson to elasticity)

This chapter is where the copper wire gains vector degrees of freedom and thermoelastic coupling. Before convergence theory certifies mesh refinement, summarize what the scalar-to-vector jump established:

| Question | Part IV answer (copper wire) |
|----------|------------------------------|
| What **object**? | Displacement \(\mathbf{u}\); strain \(\boldsymbol{\varepsilon}(\mathbf{u})\); stress \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) |
| What **structure**? | Block \(\mathbf{B}^T\mathbb{C}\mathbf{B}\) at quadrature points; \(d\) DOFs per node |
| What **theorem**? | Virtual work = Galerkin weak form; thermal eigenstrain enters as load, not new operator |
| What **breaks**? | Isotropic \(E,\nu\) when texture matters; singular \(\mathbf{K}\) from unconstrained rigid modes |

The one-mesh-two-fields Lab act showed Act II (Joule heating) and Act III (tension) on the same connectivity — the multiphysics pattern conjugate heat transfer in Part V will extend to the fluid boundary. Part IV's closing checkpoint in [IV.5](05-convergence.md) adds Céa's lemma; this chapter supplies the **physics** those error bounds bound.

## Bridge

Poisson's equation and linear elasticity share one assembly loop — scalar versus vector unknowns, gradient versus strain, the same \(\mathbf{K}\mathbf{U}=\mathbf{F}\) pattern Part I introduced on springs. A solver that passes patch tests and looks smooth on the copper wire is not necessarily **accurate**: convergence theory ties mesh size \(h\) and polynomial order \(p\) to quantifiable error bounds in the norms Part II named.

| What this chapter established | What convergence theory (next chapter) supplies |
|--------------------------------|------------------------------------------------|
| Vector P1 elements; block \(\mathbf{B}^T\mathbb{C}\mathbf{B}\) assembly | Céa's lemma: discrete energy tracks continuous minimizer in \(H^1\) |
| 1D bar = Poisson with \(EA\) stiffness; worked three-node wire | Approximation rates \(O(h^p)\) in \(H^1\) and \(L^2\); role of \(H^2\) regularity |
| Thermoelastic coupling: scalar heat + vector displacement on one mesh | A posteriori estimators and adaptive refinement at grip corners |
| Nonlinear hyperelastic preview (Part VI pointer) | When \(p\)-refinement beats \(h\)-refinement; locking at \(\nu \to 1/2\) |

**Scale-boundary handshake (IV.4 → IV.5 → Part V/VI).**

| Vector FEM output (this chapter) | Convergence audit (next chapter) | Downstream consumer | Failure mode |
|----------------------------------|----------------------------------|---------------------|--------------|
| Block \(\mathbf{K}\) from \(\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{v})\) | Céa's lemma in energy norm \(\|u-u_h\|_a\) | Part VI return-mapping on same mesh | Locking at \(\nu \to 1/2\) on Q1 hex |
| Thermoelastic load from \(\alpha \Delta T\) (Lab act Pass 2) | \(h\)-refinement at grip corner | Act III load cell in linear regime | Thermal stress ignored in pure mechanical run |
| Traction BC on grip face | A posteriori error at Neumann boundary | Part V conjugate heat transfer | Wrong traction quadrature on distorted face |
| Isotropic \(E,\nu\) on drawn wire | Texture-aware \(\mathbb{C}\) when rates fail | Part VII polycrystal RVE | Single-crystal moduli on drawn specimen |

Recall the pipeline from [Part III.4](../part03-pdes/04-energy-methods.md#bridge-to-part-iv): weak form → energy minimum → Rayleigh–Ritz on \(V_h\). This chapter extended Rayleigh–Ritz from scalar temperature to vector displacement on the **same** mesh connectivity — the multiphysics habit Part V will reuse when air cooling adds a Robin flux on the wire surface.

Return to the [prologue](../prologue/00-many-scales.md): **Act III** ramps grip displacement on a mesh whose axial displacement field is now a vector-valued Poisson story — three components, one assembly habit. The load cell curve in the linear elastic regime is trustworthy only if refinement studies show the discrete solution converging to the weak solution Part III wrote. [II.3](../part02-functional-analysis/03-hilbert-spaces.md) and [III.3](../part03-pdes/03-sobolev-spaces.md) supplied the norms; [IV.5](05-convergence.md) closes the loop between theory and mesh refinement on the copper wire and beyond.

Turn the page when patch tests pass but the grip displacement still changes when you halve \(h\) — that is the signal that convergence theory, not intuition, must certify the answer.
