# Variational Elasticity and Nonlinear Extensions

Static equilibrium of an elastic body is equivalent to minimizing total potential energy — or finding a saddle point when constraints appear. This is where continuum theory and FEM meet on equal footing: the weak form Part III derived is the first variation of an energy; the assembly loop Part IV implemented is Rayleigh–Ritz on that energy.

The copper wire under tension minimizes (or rather, stationarizes) elastic energy stored in its stretched atomic lattice — a minimization FEM approximates on a mesh. When the load exceeds yield, minimization gives way to incremental variational inequalities; when deformation grows large, the energy depends on \(\mathbf{F}\), not \(\boldsymbol{\varepsilon}\). This chapter walks that path.


## Plot spine (one line) {#plot-spine-one-line}

> **VI.3 — Act II — Continuum reunion:** Virtual work is the weak form of elasticity; hyperelastic energy closes the FEM loop.

When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the [chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter reading stalls despite a Bridge from the prior chapter.

## Scene: energy stored in the stretch

Return to the tensile frame with the load cell climbing. Below yield, the wire lengthens elastically: each increment of grip displacement adds work, and most of that work is **stored** as elastic strain energy recoverable on unloading. Plot \(\Pi(\mathbf{u})\) — total potential energy as a functional of the displacement field — and the equilibrium path is the trajectory that keeps \(\Pi\) stationary under admissible variations.

Part IV assembled \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from element matrices; Part VI now explains **why** that linear system is the discrete first variation of an energy. Virtual work and minimum potential energy are two views of the same equilibrium; variational elasticity makes the connection explicit before Part VII asks what happens when the stored-energy landscape develops singularities at dislocation cores.

## Principle of minimum potential energy

Among **kinematically admissible** displacements \(\mathbf{u}\) — satisfying \(\mathbf{u} = \mathbf{u}_0\) on \(\Gamma_D\) — define the **total potential energy**

\[
\Pi(\mathbf{u}) = \int_{\Omega_0} \psi(\boldsymbol{\varepsilon}(\mathbf{u}))\, dV - \int_{\Omega_0} \mathbf{f}\cdot\mathbf{u}\, dV - \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{u}\, dS.
\]

For **linear elasticity**, strain energy density is

\[
\psi = \tfrac{1}{2}\boldsymbol{\varepsilon}:\mathbb{C}:\boldsymbol{\varepsilon},
\]

and \(\Pi\) is **quadratic** in \(\mathbf{u}\). Equilibrium displacement minimizes \(\Pi\):

\[
\mathbf{u}^* = \arg\min_{\mathbf{u} \in \mathcal{A}} \Pi(\mathbf{u}),
\]

where \(\mathcal{A}\) is the set of admissible fields.

**Uniqueness** follows from strict convexity of \(\psi\) (positive-definite \(\mathbb{C}\)) and coercivity on displacements modulo rigid modes — fixed by essential BCs.

## Weak form as first variation

Variation \(\mathbf{u} \to \mathbf{u} + \eta\,\delta\mathbf{u}\) with admissible \(\delta\mathbf{u}\) gives

\[
\delta\Pi = \int_{\Omega_0} \boldsymbol{\sigma} : \delta\boldsymbol{\varepsilon}\, dV - \int_{\Omega_0} \mathbf{f}\cdot\delta\mathbf{u}\, dV - \int_{\Gamma_N} \mathbf{t}\cdot\delta\mathbf{u}\, dS,
\]

with \(\boldsymbol{\sigma} = \partial\psi/\partial\boldsymbol{\varepsilon}\). Setting \(\delta\Pi = 0\) for all \(\delta\mathbf{u}\) yields the **principle of virtual work** — the weak form implemented in Part IV.

**Galerkin FEM** is **Rayleigh–Ritz**: minimize \(\Pi\) over \(V_h \subset \mathcal{A}\). For quadratic \(\Pi\), this equals solving \(\mathbf{K}\mathbf{U} = \mathbf{F}\). Part III's energy methods chapter promised this equivalence; Part IV delivered the algorithm.

## Example: 1D bar as energy minimization

Axial energy density \(\psi = \tfrac{1}{2} E \varepsilon_{xx}^2\). Total energy on \([0,L]\):

\[
\Pi(u) = \int_0^L \tfrac{1}{2} E (u')^2\, dx - \int_0^L f u\, dx - F u(L).
\]

Euler–Lagrange equation: \(-(Eu')' = f\), with natural BC \(Eu'(L) = F\). FEM minimization on piecewise linears reproduces the same system as Galerkin — the copper wire as a 1D energy well.

## Hyperelastic materials

Finite deformation uses strain energy \(\psi(\mathbf{F})\) or \(\psi(\mathbf{E})\). Examples:

- **Neo-Hookean**: \(\psi = \tfrac{\mu}{2}(I_1 - 3) - \mu\ln J + \tfrac{\lambda}{2}(\ln J)^2\), with invariants \(I_1 = \text{tr}(\mathbf{C})\), \(J = \det\mathbf{F}\).
- **Mooney–Rivlin**, **Ogden**: different stretch penalties for rubber and soft tissues.

Stress derives from \(\mathbf{P} = \partial\psi/\partial\mathbf{F}\). **Polyconvexity** of \(\psi\) ensures existence of minimizers in nonlinear elasticity theory — a continuum analog of coercivity.

Copper at large stretch requires crystal plasticity, not rubber models — but hyperelasticity illustrates the nonlinear variational framework that [Nonlinear FEA notes](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) document in detail.

## Nonlinear FEM path

For nonlinear \(\Pi\) or non-quadratic virtual work:

1. **Load stepping**: apply load increment \(\Delta\lambda\) on a reference load vector.
2. **Newton–Raphson**: at each step, solve \(\mathbf{K}_T\,\Delta\mathbf{U} = \mathbf{R}\), where \(\mathbf{R}\) is the **residual** of the weak form (out-of-balance force) and \(\mathbf{K}_T = \partial\mathbf{R}/\partial\mathbf{U}\) is the **consistent tangent stiffness**.
3. **Update**: \(\mathbf{U} \leftarrow \mathbf{U} + \Delta\mathbf{U}\) until \(\|\mathbf{R}\|\) is below tolerance.

**Consistent tangent** — not a numerical perturbation of \(\mathbf{K}\), but the exact derivative of the discretized residual — yields quadratic Newton convergence. Inconsistent tangents converge slowly or stall.

Geometric nonlinearity (\(\mathbf{F}\) far from \(\mathbf{I}\)) and material nonlinearity (plasticity, damage) compose in the same loop. Plasticity adds **internal variables** updated at quadrature points alongside stress.

## Incremental variational principles

Plasticity and viscoplasticity often use **incremental energy potentials** over a time step: minimize or stationarize a functional involving incremental displacement and updated internal variables. **Variational consistency** ensures that the discrete update inherits stability properties of the continuum formulation.

Rate-independent perfect plasticity is not a simple minimization — it is a **variational inequality**. Algorithms (return mapping, active-set methods) project trial stresses onto the yield surface.

## Mixed and constrained formulations

**Incompressibility** (\(J = 1\)) in finite elasticity or Stokes flow leads to saddle-point problems:

\[
\min_{\mathbf{u}} \max_p \Pi(\mathbf{u}, p) \quad \text{subject to } \nabla\cdot\mathbf{u} = 0.
\]

Mixed \(u\)–\(p\) elements (Part III LBB, Part IV locking chapter) discretize the saddle point. **Augmented Lagrangian** and **penalty** methods approximate constraints with penalties — trading exact satisfaction for simpler systems.

## Contact and friction

When the copper wire grips contact a rigid jaw, **non-penetration** constraints apply:

\[
g(\mathbf{u}) = (\mathbf{x}_{\text{contact}} - \mathbf{x}_{\text{body}})\cdot\mathbf{n} \ge 0.
\]

Contact is a **variational inequality**: equilibrium among admissible configurations that satisfy inequalities. Implementation options:

- **Penalty**: add stiffness when penetration detected — simple, conditioning issues.
- **Augmented Lagrangian**: iterate multipliers on contact forces.
- **Mortar methods**: weakly enforce continuity on non-matching interfaces — high accuracy for multibody contact.

Friction adds Coulomb constraints: \(|\mathbf{t}_T| \le \mu t_N\). Non-smooth optimization and active-set strategies select sticking vs. sliding.

## Stability and buckling

Compression of a slender copper wire may **buckle** — equilibrium becomes a saddle point, not a minimum. **Linear buckling analysis** solves the eigenvalue problem \((\mathbf{K} + \lambda \mathbf{K}_g)\mathbf{v} = 0\) for critical load factor \(\lambda\) and mode shape \(\mathbf{v}\), where \(\mathbf{K}_g\) is the geometric stiffness from initial stress.

Post-buckling requires arc-length continuation — tracing equilibrium paths through limit points where tangent stiffness is singular.

## When continuum theory breaks down

Variational elasticity assumes smooth enough fields. **Crack tips** in linear elasticity have \(|\nabla u| \sim r^{-1/2}\): strain is not square-integrable in the classical \(H^1\) sense on a domain containing the tip. **Dislocation cores** have singular lattice distortion over atomic scales.

Remedies:

- **Regularized models**: phase-field fracture smears cracks over a diffuse interface with length scale \(\ell_0\).
- **Enriched bases**: XFEM adds discontinuous or near-tip functions to \(V_h\).
- **Descent to defect models**: Part VII dislocation dynamics; Part VIII molecular dynamics at the core.

The continuum variational framework remains valid **outside** singular sets; enrichment or homogenization patches the failure.

## Worked example: the copper wire as Rayleigh–Ritz

Return to the tensile frame one last time in the elastic range. A cold-drawn copper wire of length \(L = 100\,\text{mm}\), cross-section \(A = 0.785\,\text{mm}^2\) (1 mm diameter), and Young's modulus \(E = 117\,\text{GPa}\) is fixed at \(x = 0\) and stretched to \(u(L) = \delta = 0.10\,\text{mm}\). In 1D linear elasticity the strain energy density is \(\psi = \tfrac{1}{2}E (u')^2\), and the admissible field that minimizes \(\Pi\) under the essential boundary conditions is the linear profile

\[
u(x) = \frac{\delta x}{L}, \qquad \varepsilon_{xx} = \frac{\delta}{L} = 10^{-3}.
\]

The stored elastic energy is

\[
\Pi_{\text{exact}} = \int_0^L \tfrac{1}{2} E \left(\frac{\delta}{L}\right)^2 A\, dx = \tfrac{1}{2}\frac{EA\delta^2}{L} \approx 4.6\,\text{mJ},
\]

and the reaction force at the grip is \(F = EA\delta/L \approx 92\,\text{N}\) — the slope of the early linear region on the load–displacement curve from the prologue.

Now discretize with **three equal bar elements** — the same assembly pattern Part I introduced and Part IV automated. Nodes at \(x_0 = 0, x_1 = L/3, x_2 = 2L/3, x_3 = L\); unknown displacements \(U_2, U_3\) with \(U_0 = 0\) and \(U_3 = \delta\) prescribed. Each element of length \(h = L/3\) contributes

\[
\mathbf{k}_e = \frac{EA}{h}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}.
\]

Assembly gives the \(2 \times 2\) system for the free DOFs,

\[
\frac{EA}{h}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
\begin{bmatrix} U_2 \\ U_3 \end{bmatrix}
=
\begin{bmatrix} 0 \\ F_3 \end{bmatrix},
\]

with \(U_3 = \delta\) enforced. Solving yields \(U_2 = \tfrac{2}{3}\delta\) and \(U_3 = \delta\) — **exact at every node**, because the true solution is linear and three linear elements reproduce any affine field on a uniform mesh.

The discrete energy at the minimizing \(\mathbf{U}\) equals the continuum \(\Pi_{\text{exact}}\). That is not luck: Rayleigh–Ritz on a potential whose minimizer lies in \(V_h\) returns the **exact** energy in one solve. Refine to a nonlinear displacement profile (a wire with a notch, or thermal strain \(\alpha\Delta T\) varying along \(x\)) and the same assembly returns an approximate \(\Pi_h \ge \Pi_{\text{exact}}\) — the discrete solution sits at the bottom of a finite-dimensional energy bowl inside the infinite-dimensional one Part II defined.

This example closes the loop the book has been tracing since Part I:

| Step | Part | What happened on the wire |
|------|------|---------------------------|
| Spring network | I | \(\mathbf{K}\mathbf{U}=\mathbf{F}\) from bar elements |
| Limit \(h \to 0\) | I–II | \(u(x)\) replaces \(\mathbf{U}\); energy norm replaces \(\|\mathbf{U}\|\) |
| Weak form | III | Minimizing \(\Pi\) \(\Leftrightarrow\) virtual work |
| Assembly | IV | Shape functions and quadrature build \(\mathbf{K}\) from \(\psi\) |
| Continuum naming | VI (here) | \(\psi(\boldsymbol{\varepsilon})\) is why the matrix existed |

When the load cell curve bends upward — work hardening, necking, rate effects — the energy is no longer a simple quadratic in \(\mathbf{u}\). The next chapter follows that history-dependent path to yield and explains why Part VII must introduce dislocations to supply the hardening law.

## Multiscale variational coupling

Modern workflows **embed** atomistic or DFT domains inside continuum FEM via **bridging methods**:

- **Quasi-continuum**: FEM with energies from atomistic potentials on refined patches.
- **Concurrent coupling**: handshake between MD and FEM regions with blended forces.

Variational structure (conservative forces from potentials) aids stable coupling — ad hoc force blending without power consistency leaks energy.

## Connection to the full book arc

| Part | Role in variational elasticity |
|------|-------------------------------|
| I | \(\mathbf{K}\mathbf{U} = \mathbf{F}\) as discrete minimization |
| II | \(H^1\) admissible fields, coercivity, best approximation |
| III | Weak form, Lax–Milgram, Rayleigh–Ritz, mixed LBB |
| IV | Assembly, elements, convergence |
| V | Fluid counterpart: saddle points for pressure, not energy minimization |
| VI (this chapter) | Energy and virtual work as unified principle |
| VII+ | When \(\psi\) and \(\mathbb{C}\) must be derived from defects and atoms |

The prologue's copper wire: DFT gives cohesion; MD gives thermal motion; DDD gives work hardening; FEM (Part IV) gives bending and tension; CFD (Part V) gives cooling; Part VI explains why those simulations are minimizing energy or balancing virtual work — until they are not, and we descend further.

## Scale-boundary handshake: \(\mathbb{C}\) from DFT/MD to variational elasticity

Part VI writes \(\Pi[\mathbf{u}] = \int_\Omega \psi(\boldsymbol{\varepsilon})\, d\Omega\). The elastic tensor \(\mathbb{C} = \partial^2 \psi / \partial \boldsymbol{\varepsilon}^2\) is not a free parameter — it is the object Parts VIII–IX derive and Part IV consumes in \(\mathbf{B}^T \mathbb{C} \mathbf{B}\). Variational elasticity is where **pedigree meets physics**: the same \(\mathbb{C}\) must appear in the energy functional, the virtual work integrand, and the FEM material card.

| Rung | Delivers | Requires |
|------|----------|----------|
| DFT (IX) | \(C_{11}, C_{12}, C_{44}\) for single-crystal fcc Cu | Converged SCF + small-strain cells (±0.5% uniaxial) |
| MD (VIII) | Polycrystal-averaged \(E\), \(\nu\) from NPT stress fluctuations | Audited EAM; optional grain structure if texture matters |
| Continuum (VI) | \(\psi(\boldsymbol{\varepsilon})\) or isotropic \(\mathbb{C}\) in virtual work | Documented Voigt/Reuss reduction from crystal data |
| FEM (IV) | Element stiffness from \(\mathbf{B}^T \mathbb{C} \mathbf{B}\) | **Same** \(\mathbb{C}\) as VI.3 energy functional |

**Isotropic reduction for the wire.** Cold-drawn copper is polycrystalline; a single-crystal DFT cell gives moduli that bracket but do not equal the engineering wire. Standard practice:

| Source | Typical \(E\) (GPa) | Typical \(\nu\) | Wire context |
|--------|----------------------|-----------------|--------------|
| DFT (PBE, fcc Cu) | 110–130 | 0.33–0.36 | Single crystal along [100] |
| MD NPT (256–500 atom fcc) | 105–125 | 0.32–0.35 | Same; potential-dependent |
| Handbook (OFHC polycrystal) | 110–130 | 0.34 | Engineering design value |
| Tensile test (Act III) | Secant slope before yield | From transverse strain | **Measured** on the specimen |

Voigt and Reuss bounds on \(E\) for a random polycrystal lie between single-crystal extremes. If Part IV's elastic step uses \(E = 120\,\text{GPa}\) from a handbook but Part VIII's NPT average on a 500-atom fcc box gives \(E = 95\,\text{GPa}\), the fault is **scale mismatch** (single crystal vs drawn wire), not necessarily a bad potential — but the mismatch must be documented in the foundation folder, not silently ignored.

### Thermal coupling (Act II) {#thermal-coupling-act-ii}

Variational elasticity with thermal strain writes \(\boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}_{\text{mech}} + \alpha \Delta T \mathbf{I}\). The thermal stress estimate \(\sigma \approx E \alpha \Delta T\) from [VI.2](02-stress-balance.md#scale-boundary-handshake-thermal-expansion-alpha) inherits the same \(E\) as \(\Pi\). Mixing DFT \(E\) in the mechanical block and handbook \(\alpha\) without cross-checking against DFT quasi-harmonic expansion (Part IX) is a **pedigree fracture** at the continuum scale.

**What breaks without the handshake.** Fitting \(\psi\) from a tensile test while using DFT moduli in a coupled thermoelastic run couples two different material definitions. A 10% modulus error is a 10% force error at the same grip displacement — visible on the load cell before yield. Archive `elastic_constants/` beside `kappa_md_300K.txt` and `cu.phonon/` in the foundation folder: one row per source (handbook, DFT, MD, tensile test), one \(\mathbb{C}\) chosen for production FEM with a citation. Part VI.3's virtual work is only honest when that row exists.

## Lab act: virtual work equals load cell reading (Act III — Pulling)

**Act III** ramps grip displacement and the load cell reports force. Variational elasticity states that equilibrium is \(\delta \Pi = 0\) — virtual work done by internal stress equals virtual work done by external loads. This Lab act verifies that statement on the same three-element bar Part IV will mesh.

Fixed end at \(x = 0\), prescribed displacement \(\delta = 0.1\,\text{mm}\) at \(x = L = 1\,\text{m}\), \(EA = 120\,\text{GPa} \times 10^{-6}\,\text{m}^2 = 120\,\text{kN}\). The exact axial force is \(F = EA\,\delta/L = 12\,\text{N}\).

| Virtual work check | Statement | Numeric |
|--------------------|-----------|---------|
| External virtual work | \(\delta W_{\text{ext}} = F_{\text{applied}} \,\delta u(L)\) with virtual \(\delta u(L) = 1\) | \(F = 12\,\text{N}\) |
| Internal virtual work | \(\delta W_{\text{int}} = \int_0^L \sigma \,\delta\varepsilon \, A \, dx = \sigma A \,\delta u(L)\) for uniform bar | Same \(12\,\text{N}\) when \(\sigma = E\delta/L\) |
| Energy minimizer | \(\Pi = \tfrac{1}{2}EA(\delta/L)^2 L - F\delta\); \(\partial \Pi / \partial \delta = 0\) | \(F = EA\delta/L\) |
| Discrete (3 P1 elements) | Rayleigh–Ritz on \(V_h\) from [VI.3 worked example](#worked-example-three-element-bar) | **Exact** at nodes because \(u(x)\) is linear |

Plot force versus \(\delta\) from the load cell against the analytical line — slope \(EA/L\). Before yield (Act IV), the curve should be straight; variational elasticity explains **why** Part IV's \(\mathbf{K}\mathbf{U}=\mathbf{F}\) is force balance, not merely matrix algebra. When thermal strain \(\alpha \Delta T\) from Act II is present, subtract it from mechanical strain in \(\Pi\): the load cell reads lower force at the same grip displacement because the wire already expanded.

## Lab act: finite strain versus small strain on the same grip (Act III — Pulling, finite-strain preview)

**Act III** keeps the wire in the linear elastic regime, but the prologue's grip displacement \(\delta = 0.10\,\text{mm}\) on \(L = 100\,\text{mm}\) is not infinitesimal — it is \(\delta/L = 10^{-3}\), large enough that the **Green–Lagrange strain** and the small-strain tensor \(\varepsilon_{xx} = \delta/L\) disagree at the third decimal. This Lab act compares the two energy functionals on the same specimen before [VI.4](04-nonlinear-plasticity-preview.md) turns on Newton–Raphson and plastic history.

**Setup.** Uniaxial tension of the 1 mm copper wire; reference length \(L_0 = 100\,\text{mm}\), current length \(L = L_0 + \delta\). Stretch \(\lambda = L/L_0 = 1 + \delta/L_0\). For \(\delta = 0.10\,\text{mm}\): \(\lambda = 1.001\).

**Small-strain energy (Part VI.3 quadratic \(\Pi\)).** With \(\varepsilon_{xx} = \lambda - 1 = 10^{-3}\):

\[
\Pi_{\text{small}} = \tfrac{1}{2} E \varepsilon_{xx}^2 A L_0 = \tfrac{1}{2} E A L_0 (\lambda - 1)^2.
\]

**Finite-strain energy (Saint-Venant–Kirchhoff preview).** Green–Lagrange strain \(E_{11} = \tfrac{1}{2}(\lambda^2 - 1)\). For \(\lambda = 1.001\): \(E_{11} = 1.0005 \times 10^{-3}\) — **0.05% larger** than \(\varepsilon_{xx}\). Strain energy \(\Pi_{\text{GL}} = \tfrac{1}{2} E E_{11}^2 A L_0\) integrated on the reference domain (valid while \(\lambda\) stays near unity):

| Strain measure | Value at \(\lambda = 1.001\) | Stored energy \(\Pi\) (mJ) | Reaction force \(F = \partial\Pi/\partial\delta\) (N) |
|----------------|------------------------------|----------------------------|--------------------------------------------------------|
| Small \(\varepsilon = \lambda - 1\) | \(1.000 \times 10^{-3}\) | 4.60 | 92.0 |
| Green–Lagrange \(E_{11} = \tfrac{1}{2}(\lambda^2-1)\) | \(1.0005 \times 10^{-3}\) | 4.61 | 92.1 |
| True neo-Hookean (1D) \(\Pi = \tfrac{1}{2}E A L_0 (\ln\lambda)^2\) | — | 4.60 | 92.0 |

At \(\delta/L = 10^{-3}\), the three models agree within **0.1%** — linear FEM and variational elasticity are honest for Act III. The table becomes a **convergence study in strain measure**, not in mesh size:

| \(\delta/L\) | Relative error: small strain vs GL energy | Wire context |
|--------------|------------------------------------------|--------------|
| \(10^{-4}\) | \(< 0.01\%\) | Elastic climb on load cell |
| \(10^{-3}\) | \(\sim 0.05\%\) | Prologue Act III setpoint |
| \(10^{-2}\) | \(\sim 0.5\%\) | Still elastic; nonlinear FEM advisable |
| \(5 \times 10^{-2}\) | \(\sim 2.5\%\) | Approaching necking; geometric nonlinearity mandatory |

**Finite-element check.** On the three-element bar from the [worked example](#worked-example-the-copper-wire-as-rayleigh-ritz), small-displacement FEM uses \(\mathbf{B}\) with \(\partial u/\partial x\). A **Updated Lagrangian** step with the same mesh and \(\lambda = 1.001\) updates \(\mathbf{F}\) at each Gauss point:

\[
F_{11} = \frac{\partial x}{\partial X} = \lambda, \qquad E_{11} = \tfrac{1}{2}(F_{11}^2 - 1),
\]

and assembles \(\mathbf{K}_T\) from \(\partial^2 \psi / \partial \mathbf{F}^2\). One Newton iteration from \(\lambda = 1\) should recover the GL force within 0.1% — if not, the tangent is inconsistent with the energy (the same lesson as return-mapping in [VI.4](04-nonlinear-plasticity-preview.md)).

**Bridge to VI.4.** Act III's straight load-cell line used quadratic \(\Pi\). When Act IV bends the curve, part of the bend is **material** (plasticity) and part is **geometric** (necking, \(\lambda\) far from 1). This Lab act separates the geometric branch: at prologue displacements, geometry is still negligible; at ultimate tensile strength, \(\Pi_{\text{small}}\) and \(\Pi_{\text{GL}}\) diverge and only hyperelastic or Updated Lagrangian FEM is credible. Archive `strain_measure_check.dat` with columns \((\delta/L, \Pi_{\text{small}}, \Pi_{\text{GL}}, F_{\text{small}}, F_{\text{GL}})\) beside the Act III load-cell trace — the epilogue's Handshake 4 uses the same discipline when rate-dependent plasticity enters the story.

## Concept map checkpoint (variational elasticity)

This chapter is where FEM's matrix equation receives its continuum philosophical source. Before nonlinear plasticity admits history, summarize what variational elasticity established:

| Question | Part VI answer (copper wire) |
|----------|------------------------------|
| What **object**? | Strain energy density \(\psi(\boldsymbol{\varepsilon})\); total potential \(\Pi\) |
| What **structure**? | Virtual work \(\delta\Pi=0\); path independence in hyperelasticity |
| What **theorem**? | Dirichlet principle: equilibrium = energy minimum in \(H^1\) |
| What **breaks**? | Dissipation (plasticity, viscosity); non-conservative loading; fitted \(H\) without dislocations |

The three-element bar worked example closed the loop from Part I's springs through Part IV's assembly: Rayleigh–Ritz on a quadratic energy returns exact linear solutions when \(u(x)\in V_h\). Act IV's upward bend signals the energy is no longer a simple quadratic in \(\mathbf{u}\) — the cue for [VI.4](04-nonlinear-plasticity-preview.md) and Part VII's forest.

## Bridge

Variational elasticity closes the loop the book has traced since Part I's spring network: minimize energy in \(H^1\), derive virtual work, assemble \(\mathbf{K}\) — and recognize the discrete solve as Rayleigh–Ritz on the same functional Part III named.

| What VI.3 established | What VI.4 opens |
|-------------------------|-----------------|
| Hyperelastic energy \(\psi(\boldsymbol{\varepsilon})\); path-independent response | Geometric nonlinearity when strains are large |
| Virtual work \(\delta\Pi = 0\) as FEM's philosophical source | J₂ plasticity when history matters (cold-drawn wire) |
| Worked 1D bar: exact linear solution on P1 mesh | Newton–Raphson at every load increment |
| Elastic springback before yield | Honest admission: smooth fields break at defects |

**Scale-boundary handshake (VI.2 → VI.3 → VI.4).**

| Balance-law export ([VI.2](02-stress-balance.md)) | Variational output (this chapter) | Nonlinear consumer ([VI.4](04-nonlinear-plasticity-preview.md)) | Failure mode |
|---------------------------------------------------|-----------------------------------|----------------------------------------------------------------|--------------|
| Momentum balance \(\nabla\cdot\boldsymbol{\sigma}+\mathbf{f}=\mathbf{0}\) | Stationarity \(\delta\Pi=0\) of total potential energy | J₂ plasticity when history matters | Treating yield as a fitted \(H\) without dislocation forest |
| Hooke's law \(\boldsymbol{\sigma}=\mathbb{C}:\boldsymbol{\varepsilon}\) | Quadratic \(\Pi\) on small-strain bar | Geometric nonlinearity at large \(\lambda\) | Small-displacement FEM past necking onset |
| Virtual work from Part III weak form | Rayleigh–Ritz on P1 bar returns exact linear solution | Newton–Raphson at every load increment | Inconsistent tangent vs. energy in Updated Lagrangian step |
| Thermal strain \(\varepsilon_{\text{th}}=\alpha\Delta T\) from Act II | Coupled energy functional (preview) | Phenomenological hardening without internal variables | Handbook \(\alpha\) beside converged CHT \(T_w\) |
| Act III load-cell linear climb | Three-element bar worked example closes Part I→IV loop | Act IV upward bend signals mesoscale descent | Smooth \(\Pi\) explains curve that cold-drawn history bent |

Return to the [prologue](../prologue/00-many-scales.md): **Act III** measured the linear elastic climb on the load cell; **Act IV** is the upward bend that variational elasticity cannot explain with a quadratic \(\psi\) alone. Part IV assembled \(\mathbf{K}\) from bilinear forms; this chapter named the stress and strain those forms integrate. [VI.4](04-nonlinear-plasticity-preview.md) is the last continuum stop — phenomenological hardening without dislocations, a fitted curve waiting for Part VII's forest to supply \(\sigma_{y0}\) and \(H\).

Turn the page when the wire's stress–strain curve bends upward after cold drawing but your elastic energy minimization still returns a straight line — that is the signal history and mesoscale defects have entered the story.
