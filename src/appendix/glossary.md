# Glossary and Cross-Scale Index

This appendix is a **reverse index** for reading the book as one continuous story. When a symbol or phrase reappears in a new part, use the tables below to see what it meant earlier — and where the copper wire carries the same idea under new vocabulary.

The layout mirrors the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf): at every scale, four questions organize the material — **object**, **structure**, **theorem**, **failure mode**. Part openings and closing checkpoints state these explicitly; this page collects them in one place.

## Scene: the wire after the epilogue

The epilogue closed with a multiscale afternoon — Quantum ESPRESSO logs, LAMMPS trajectories, OpenDiS hardening curves, and the same copper wire still in the grips. You may have read straight through for weeks, or jumped between parts as a project demanded. Either way, symbols now pile up: \(\mathbf{K}\) was a stiffness matrix, then an operator, then a bilinear form, then an elastic tensor. This glossary is the **reverse index** for that journey — not a dictionary of jargon, but a map of where each habit first appeared and what it meant on the wire.

When \(\rho\) appears, ask whether you mean dislocation density (Part VII) or electron density (Part IX). When "energy" appears, trace the row in the tables below before trusting a number in an input deck.

## The four questions at every scale

| Part | Object | Structure | Theorem / principle | What breaks |
|------|--------|-----------|---------------------|-------------|
| I | \(\mathbf{u}\), \(\mathbf{K}\), eigenmodes | Inner product, symmetry, sparsity | SPD \(\mathbf{K}\) \(\Rightarrow\) unique equilibrium; spectral theorem | Ill-conditioning; \(N\to\infty\) without target space |
| II | Fields \(u\), operators \(A\) | Norm, completeness, Hilbert geometry | Lax–Milgram; Galerkin best approximation | Cauchy sequences leave the space |
| III | \(u(\mathbf{x},t)\) on \(\Omega\) | Strong/weak form, energy functional | Energy minimization; well-posedness in \(H^1\) | Corners, delta loads, non-physical oscillations |
| IV | \(V_h\), shape functions, \(\mathbf{K}\) | Galerkin orthogonality, \(h\)-refinement | Céa lemma; a priori rates | Locking, hourglass modes, pollution |
| V | Cell averages, fluxes | Conservation on control volumes | Godunov/Riemann upwinding | Diffusion instability; wrong wall flux |
| VI | \(\mathbf{F}\), \(\boldsymbol{\sigma}\), \(\mathbb{C}\) | Objectivity, balance laws | Virtual work; hyperelastic energy | Yield, notches — need mesoscale physics |
| VII | Dislocation segments, density | Peach–Köhler, mobility law | Taylor hardening; forest statistics | Polycrystal texture; link-length tails |
| VIII | \(\{\mathbf{r}_i\}\), potential \(V\) | Hamiltonian, thermostats, PBC | Symplectic energy conservation; ergodic sampling | Energy drift; cutoff artifacts |
| IX | \(\rho(\mathbf{r})\), KS orbitals | Hohenberg–Kohn; SCF loop | Variational ground state; force theorem | Wrong functional; k-mesh too coarse |

See the [chapter roadmap](sources.md) for one-line roles of every numbered chapter. After the [epilogue](../epilogue/multiscale.md), the [Final Memory Sheet](memory-sheet.md) collects book-wide habits and traps in the ME 412 style.

## Recurring symbols (same habit, new meaning)

| Symbol | Part I | Part II–III | Part IV–V | Part VI | Part VII–IX |
|--------|--------|-------------|-----------|---------|-------------|
| \(u\) | Nodal displacement vector | Displacement field \(u(x)\) | FEM DOFs; FVM scalar fields | \(\mathbf{u}(\mathbf{X})\) | — |
| \(\mathbf{K}\) | Stiffness matrix | — (operator \(A\)) | Assembled stiffness | Elastic tensor \(\mathbb{C}\) in integrals | — |
| Energy | \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) | \(\|u\|_{H^1}\), bilinear form | Element strain energy | \(\int \boldsymbol{\sigma}:\boldsymbol{\varepsilon}\) | \(E_{\text{coh}}\), stacking fault \(\gamma_{\text{sf}}\) |
| Modes | Eigenvectors of \(\mathbf{K}\) | Orthonormal basis in \(H^1\) | Shape functions \(\phi_i\) | Normal modes of bar | Slip systems; phonon bands (MD) |
| Load | \(\mathbf{f}\) | Linear functional \(\ell(v)\) | Neumann data, body force | Traction \(\mathbf{t}\) | Peach–Köhler force on dislocations |
| Mesh / basis | Spring network | Refinement limit \(h\to 0\) | Elements, quadrature | Same FEM mesh | Supercell (MD/DFT); segment mesh (DDD) |

**Reading tip:** When Part IX writes a self-consistent **eigenvalue loop**, read it as Part I's \(\mathbf{K}\mathbf{u}=\mathbf{f}\) with the operator replaced by the Kohn–Sham Hamiltonian and the basis replaced by plane waves — the [Part IX opening](../part09-dft/00-opening.md) states this parallel explicitly.

## The copper wire: state variable by part

| Part | What we track on the wire | Typical code / method |
|------|---------------------------|------------------------|
| Prologue | All scales at once (preview) | — |
| I | Spring displacements, vibration modes | Hand calculation, NumPy |
| II | \(u(x)\), \(T(x)\) as limits of refinement | Analysis only |
| III | Weak forms for elasticity and heat | Pen-and-paper → FEM input |
| IV | Nodal \(\mathbf{U}\) on a solid mesh | FEniCS, Abaqus-style assembly |
| V | Air velocity, pressure, enthalpy flux | OpenFOAM-style FVM |
| VI | \(\mathbf{F}\), \(\boldsymbol{\sigma}\), yield preview | Continuum post-processing |
| VII | Dislocation density, link statistics | OpenDiS, ParaDiS → DAMASK |
| VIII | Atomic positions, stresses from EAM | LAMMPS |
| IX | \(\rho(\mathbf{r})\), total energy, \(C_{ij}\) | Quantum ESPRESSO, VASP |
| Epilogue | Coupled workflows across rows | Sequential / concurrent multiscale |

## Narrative hinges (where to look if the story jumps)

The [prologue](../prologue/00-many-scales.md#the-experiment-as-plot) maps the same copper wire to **six acts** of one lab session (mounting → warming → pulling → hardening → notch → foundation). Each act links directly to the part openings where that laboratory beat is developed — use the table when you need laboratory time rather than part number.

| If you feel a jump between… | Read first… |
|-----------------------------|-------------|
| Springs and function spaces | [I.4 Bridge](../part01-linear-algebra/04-toward-infinity.md) → [II.0 opening](../part02-functional-analysis/00-opening.md) |
| Analysis and meshing | [III.4 Bridge](../part03-pdes/04-energy-methods.md) → [IV.0 opening](../part04-fem/00-opening.md) |
| FEM and fluids | [IV.5 Bridge](../part04-fem/05-convergence.md) (two doors) or [V.0 opening](../part05-fvm/00-opening.md) |
| PDE codes and stress tensors | [VI.0 Story so far](../part06-continuum/00-opening.md) |
| Smooth elasticity and dislocations | [VI.4 Bridge](../part06-continuum/04-nonlinear-plasticity-preview.md) → [VII.0](../part07-defects/00-opening.md) |
| Continuum moduli and atoms | [VII.3 Bridge](../part07-defects/03-polycrystal-and-fem-handoff.md) → [VIII.0](../part08-md/00-opening.md) |
| Potentials and electrons | [VIII.3 Bridge](../part08-md/03-ab-initio-and-coarse-graining.md) → [IX.0](../part09-dft/00-opening.md) |
| DFT and full multiscale | [IX.3 Bridge](../part09-dft/03-dft-workflows.md) → [Epilogue](../epilogue/multiscale.md) |

Every numbered chapter also ends with its own **Bridge** section — the primary narrative hinge within a part.

## Symbol collision guide

The same letter often means different physics in adjacent parts. Before trusting a number in an input deck, locate the row below and read the **first appearance** link — the book reuses symbols deliberately, but never without a Bridge explaining the handoff.

| Symbol | Collision | Disambiguation rule | First appearance |
|--------|-----------|---------------------|------------------|
| \(\rho\) | Dislocation density (Part VII) vs mass density (Part V/VI) vs electron density (Part IX) | Check subscript and part: \(\rho_{\text{disl}}\), \(\rho\) kg/m³, \(\rho(\mathbf{r})\) e/Å³ | [VII.2](../part07-defects/02-dislocation-dynamics.md) vs [IX.0](../part09-dft/00-opening.md) |
| \(\mathbf{K}\) | Stiffness matrix vs thermal conductivity vs kinetic energy | Stiffness is a matrix; conductivity is a scalar field \(k\) or \(\kappa\); kinetic energy is \(K\) in Hamiltonian | [I.1](../part01-linear-algebra/01-vectors-matrices.md) |
| \(\gamma\) | Surface energy / GSF (Part IX) vs shear strain (Part VI) vs heat capacity ratio (Part V) | GSF is \(\gamma_{\text{sf}}\) in mJ/m²; strain is tensor component; CFD \(\gamma\) is \(c_p/c_v\) | [IX.3](../part09-dft/03-dft-workflows.md) vs [VI.1](../part06-continuum/01-kinematics.md) |
| \(E\) | Young's modulus vs total energy vs electric field | Modulus has GPa units; DFT energy is eV/cell; field is V/m in Joule heating | [IV.4](../part04-fem/04-poisson-to-elasticity.md) vs [IX.1](../part09-dft/01-born-oppenheimer.md) |
| \(\alpha\) | Thermal expansion coefficient vs Rayleigh–Ritz parameter vs dislocation–dislocation spacing factor | Thermal \(\alpha\) is K⁻¹; Taylor hardening uses \(\alpha\) in \(\Delta\tau = \alpha \mu b \sqrt{\rho}\) | [VI.2](../part06-continuum/02-stress-balance.md) vs [VII.2](../part07-defects/02-dislocation-dynamics.md) |
| \(a(u,v)\) | Bilinear form (Part II–IV) vs lattice parameter (Part VIII–IX) | Weak-form \(a(\cdot,\cdot)\) takes two functions; lattice \(a_0\) is Å | [II.3](../part02-functional-analysis/03-hilbert-spaces.md) vs [IX.3](../part09-dft/03-dft-workflows.md) |
| \(\psi\) | Test function (Part III) vs wavefunction (Part IX) vs strain energy density (Part VI) | Test functions are \(v\) or \(\psi\) in weighted residuals; KS orbitals are \(\psi_i(\mathbf{r})\) | [III.2](../part03-pdes/02-weak-form.md) vs [IX.2](../part09-dft/02-kohn-sham.md) |
| \(\tau\) | Shear stress (Part VI–VII) vs autocorrelation time (Part VIII) vs resolved shear on slip systems (DDD) | Stress has Pa; autocorrelation time has ps; hardening \(\tau(\gamma)\) is a curve | [VI.2](../part06-continuum/02-stress-balance.md) vs [VIII.2](../part08-md/02-ensembles-integrators.md) |

**Habit:** when a symbol feels overloaded, ask the four concept-map questions for the **current part** before searching the whole book. The collision is usually a feature — the same mathematical move (inner product, minimization, eigenvalue loop) wearing different physical units.

## Continuity threads (same story, new vocabulary)

Three threads stitch Parts I–IX into one novel rather than nine courses. Follow a thread when a chapter feels disconnected from the copper wire:

| Thread | Opens | Recurs | Closes | Wire beat |
|--------|-------|--------|--------|-----------|
| **Equilibrium as linear solve** | [I.1](../part01-linear-algebra/01-vectors-matrices.md) \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | [IV.2](../part04-fem/02-galerkin-assembly.md) assembly; [IX.2](../part09-dft/02-kohn-sham.md) SCF | [Epilogue](../epilogue/multiscale.md) pedigree | Load cell reading at every scale |
| **Weak form / virtual work** | [II.1](../part02-functional-analysis/01-motivation.md) corners break strong form | [III.2](../part03-pdes/02-weak-form.md); [VI.3](../part06-continuum/03-variational-elasticity.md) | [IV.1](../part04-fem/01-weighted-residuals.md) Galerkin | Grips apply traction without pointwise smoothness |
| **Energy minimization** | [I.1](../part01-linear-algebra/01-vectors-matrices.md) \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) | [III.4](../part03-pdes/04-energy-methods.md) Dirichlet principle | [IX.1](../part09-dft/01-born-oppenheimer.md) Hohenberg–Kohn | Wire settles to a minimum (elastic, thermal, electronic) |
| **Refinement / convergence** | [I.4](../part01-linear-algebra/04-toward-infinity.md) \(N\to\infty\) | [IV.5](../part04-fem/05-convergence.md) mesh; [V.2](../part05-fvm/02-fvm-1d.md) CFL | [VIII.2](../part08-md/02-ensembles-integrators.md) autocorrelation; [IX.2](../part09-dft/02-kohn-sham.md) cutoff/k-mesh | Thermocouples multiply until profile stops changing |
| **Export upward** | [Prologue](../prologue/00-many-scales.md) four questions | [VII.3](../part07-defects/03-polycrystal-and-fem-handoff.md) hardening law | [IX.3](../part09-dft/03-dft-workflows.md) → [Epilogue](../epilogue/multiscale.md) handshakes | Act VI foundation before Act III pull |

When two parts feel adjacent but unrelated — say FEM (IV) and DDD (VII) — trace the **export upward** thread: Part IV's yield stress is a number in a constitutive file; Part VII explains why that number bends with strain; Part IX explains where elastic constants in the file originated.

## Abbreviations

| Term | Meaning | First major appearance |
|------|---------|------------------------|
| FEM | Finite element method | Part IV |
| FVM | Finite volume method | Part V |
| CFD | Computational fluid dynamics | Part V.4 |
| PDE | Partial differential equation | Part III |
| DDD | Dislocation dynamics | Part VII |
| MD | Molecular dynamics | Part VIII |
| DFT | Density functional theory | Part IX |
| SCF | Self-consistent field | Part IX |
| EAM | Embedded atom method | Part VIII |
| PBC | Periodic boundary conditions | Part VIII |
| CHT | Conjugate heat transfer | Part V.4, Epilogue |
| WHAM | Weighted histogram analysis method — reweights parallel-tempering replica samples to a target temperature (e.g. Joule-heated \(T_w\)) before exporting cross-slip or mobility statistics | [VIII.3](../part08-md/03-ab-initio-and-coarse-graining.md#wham-part-vii-mobility-hinge-act-ii-temperature-pedigree) |

## Lab-act cross-reference (by act) {#lab-act-cross-reference-by-act}

The book reads in **mathematical order** (Part I before Part IX) but the copper wire lives in **laboratory time** (mounting before hardening). When proofs flow but the afternoon feels episodic, use this table — the full index with chapter links is in [Sources (row 21)](sources.md#lab-act-cross-reference-index-row-21).

| Act | What happens on the wire | First Lab act to run | Reunion |
|-----|--------------------------|----------------------|---------|
| I — Mounting | Grips close; load cell at zero | [I.1 three-node bar](../part01-linear-algebra/01-vectors-matrices.md#lab-act-three-nodes-one-load-cell-reading-act-i--mounting) | [Epilogue Act I](../epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) |
| II — Warming | Current on; thermocouple rises | [III.2 weak form](../part03-pdes/02-weak-form.md#lab-act-integrate-by-parts-on-the-heated-wire-act-ii--warming) or [V.4 CHT](../part05-fvm/04-navier-stokes-cfd.md#lab-act-natural-convection-nusselt-number-on-the-heated-wire-act-ii--warming) | Handshake 2 in [epilogue](../epilogue/multiscale.md#handshake-2--joule-heating--conjugate-heat-transfer-part-iv--v) |
| III — Pulling | Grip displacement ramps | [IV.2 assembly](../part04-fem/02-galerkin-assembly.md#lab-act-scatter-one-bar-element-into-global-mathbfk-act-iii--pulling) | [VI.3 virtual work](../part06-continuum/03-variational-elasticity.md#lab-act-virtual-work-equals-load-cell-reading-act-iii--pulling) |
| IV — Hardening | Force–displacement curve bends | [VII.2 forest density](../part07-defects/02-dislocation-dynamics.md#lab-act-read-the-hardening-bend-from-forest-density-act-iv) | Handshake 4a in [epilogue](../epilogue/multiscale.md#4a--ddd-strain-rate-to-quasi-static-load-cell-act-iv--hardening) |
| V — Notch | Stress concentrator | [VIII.3 EAM audit](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) | Handshake 4b in [epilogue](../epilogue/multiscale.md#4b--when-continuum-fails-at-the-notch-md-subdomain-act-v--notch) |
| VI — Foundation | DFT/MD exports (parallel) | [IX.3 archive](../part09-dft/03-dft-workflows.md#lab-act-archive-the-foundation-run-before-the-wire-scale-solve-act-vi--foundation) | [`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) |

**Reading tip:** Act VI runs **in parallel** with Acts I–V in real projects — foundation folders populate while the grips are still at zero. Row 21 is the laboratory-time mirror of row 17's mathematical read-through guide.

## Representative schematics (by part) {#representative-schematics-by-part}

Each part opening indexes baby pictures from its source notes (ME 300A, ME 412, ME 300B, FEA, FVM/CFD, Elasticity, Defects, Atomistic, DFT). When a proof feels abstract despite Scene and Bridge, open the schematic row for your part — the full map with chapter links is in [Sources (row 22)](sources.md#representative-schematics-cross-reference-index-row-22).

| Part | Source notes | Schematics | Key spine | Part-opening table |
|------|--------------|------------|-----------|-------------------|
| I | ME 300A | 1–4 | Finite grammar → \(N\to\infty\) | [I.0](../part01-linear-algebra/00-opening.md#representative-schematics-me-300a) |
| II | ME 412 | 1a–14 | **Schematic 14** variational + FEM ladder | [II.0](../part02-functional-analysis/00-opening.md#representative-schematics-me-412) |
| III | ME 300B | 1–4 | Strong → weak → Sobolev → energy | [III.0](../part03-pdes/00-opening.md#representative-schematics-me-300b) |
| IV | FEA | 1–5 | Galerkin assembly; two doors at IV.5 | [IV.0](../part04-fem/00-opening.md#representative-schematics-fea-notes) |
| V | FVM / CFD | 1–4 | Conservation ladder (transport twin) | [V.0](../part05-fvm/00-opening.md#representative-schematics-fvm--cfd-notes) |
| VI | Elasticity | 1–4 | Virtual work reunites FEM and FVM | [VI.0](../part06-continuum/00-opening.md#representative-schematics-elasticity-notes) |
| VII | Defects | 1–3 | DDD forest replaces fitted \(H\) | [VII.0](../part07-defects/00-opening.md#representative-schematics-defects-notes) |
| VIII | Atomistic | 1–3 | Potentials → LAMMPS → coarse-graining | [VIII.0](../part08-md/00-opening.md#representative-schematics-atomistic-modeling-notes) |
| IX | DFT coursework | 1–3 | Kohn–Sham SCF → QE export pedigree | [IX.0](../part09-dft/00-opening.md#representative-schematics-dft-coursework) |

**Reading tip:** Schematic **14** in Part II is the plot spine for Acts I–II — existence climbs through Parts III–IV; the conservation ladder in Part V is its transport twin for Act II warming. Row 22 is the visual-vocabulary mirror of row 19's plot-spine one-liners.

## Canonical sources

Chapter markdown is authored under [`writings/`](../../writings/) (Functional Analysis Notes layout) and synced into `src/` via [`scripts/sync-writings.sh`](../../scripts/sync-writings.sh). For PDF links, repositories, and the full chapter roadmap, see [Sources and Further Reading](sources.md).

## Bridge

This page answers *what did that symbol mean last time?* The [chapter roadmap](sources.md) answers *where does each chapter sit in reading order?* The [lab-act cross-reference (row 21)](sources.md#lab-act-cross-reference-index-row-21) answers *which worked example belongs to which act of the wire's afternoon?* The [representative schematics index (row 22)](sources.md#representative-schematics-cross-reference-index-row-22) answers *which baby picture matches this chapter's confusion?* The [Final Memory Sheet](memory-sheet.md) answers *what habits and traps should I carry to the next project?*

Return to the [prologue](../prologue/00-many-scales.md) when a new specimen replaces copper — the four questions and six-act lab table apply to any material. Return to the [epilogue](../epilogue/multiscale.md) when you need to wire codes together rather than recall vocabulary.
