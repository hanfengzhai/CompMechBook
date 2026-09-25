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

## Book-loop reunion rows (12, 52–53) {#book-loop-reunion-rows-52-53}

Late in the arc, four **meta rows** sound similar — they all mention the epilogue, the prologue, and restarting on a new specimen. They differ by **which stitch broke**:

| Row | What broke | Read first | Closes with |
|-----|------------|------------|-------------|
| [12](../preface.md#skill-navigation-row-12) | Copper tutorial finished; next material feels like a scale menu | [Prologue reopening anchor](../prologue/00-many-scales.md#prologue-reopening-anchor) four-step table | New specimen rung sketch + [row 0](../preface.md#opening-continuity-hinge) grammar restart |
| [52](../preface.md#skill-navigation-row-52) | `writings/epilogue` and `writings/prologue` each build as standalone mdBooks | [Writings canonical hinge](../epilogue/multiscale.md#writings-canonical-hinge-epilogue-to-prologue) → [prologue landing](../prologue/00-many-scales.md#writings-canonical-landing-epilogue-to-prologue) | ME 412 summary → portable ladder on new material |
| [53](../preface.md#skill-navigation-row-53) | Handshakes 3–4b inside the epilogue read as separate ME sections | [Intra-epilogue handshake bridge chain](../epilogue/multiscale.md#intra-epilogue-handshake-bridge-chain) | [Row 12 closing loop](../epilogue/multiscale.md#row-12-closing-loop) ME 412 summary, then row 52 landing |
| [54](../preface.md#skill-navigation-row-54) | Rows 52–53 narrative reunions verify but workflow exam columns blur row 12 / 52 / 53 | [Glossary table (this section)](#book-loop-reunion-rows-52-53) + [Rows 52–53 workflow exam reunion index](sources.md#rows52-53-workflow-exam-three-way-audit-reunion-index-row-54) | Preface three-way audits aligned with [row 52 row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) and [row 53 row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) |
| [55](../preface.md#skill-navigation-row-55) | Row 54 closed columns but row 12 preface audit disagrees with epilogue closing loop, or reopening anchor opens before row 52 landing | [Row 54 → Row 12 copper-arc reunion index](sources.md#row54-row12-copper-arc-three-way-audit-reunion-index-row-55) + [preface row 12 three-way audit](../preface.md#skill-navigation-row-12) | Copper arc **row 53 → row 12 → row 52** before Part I on new material |
| [56](../preface.md#skill-navigation-row-56) | Row 55 closed copper arc but Part I opens without opening continuity hinge or `writings/prologue` → `writings/linear-algebra` feels like two courses | [Row 55 → Opening continuity reunion index](sources.md#row55-opening-continuity-reunion-index-row-56) + [opening continuity hinge](../preface.md#opening-continuity-hinge) | **row 55 → row 0 → I.1 mounting** on new specimen — not copied copper decks |
| [57](../preface.md#skill-navigation-row-57) | Row 56 closed prologue → I.0 but I.0 syllabus and I.1 inner products feel disconnected or `00-opening` → `01-vectors-matrices` feels like two mdBooks | [Row 56 → I.0 → I.1 reunion index](sources.md#row56-i0-i1-mounting-reunion-index-row-57) + [I.0 Bridge](../part01-linear-algebra/00-opening.md#bridge) | **row 56 → I.0 Bridge → three-node Lab act** — concept map before NumPy |

**Reading order on the copper arc (workflow exam):** [row 53 row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) (intra-epilogue bridges) → [row 12 row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) Step 4 inside row 53 (next-specimen audit) → [row 52 row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) (Writings subtree landing). Row 12 **defers** to [row 53 closing loop](../epilogue/multiscale.md#row-53-closing-loop) when Handshakes 3–4b stutter. Row 55 **confirms** [preface row 12](../preface.md#skill-navigation-row-12) matches [row 12 closing loop](../epilogue/multiscale.md#row-12-closing-loop) after row 54. Row 56 **confirms** [row 0](../preface.md#skill-navigation-row-0) grammar restart after row 55 before I.1. Row 57 **confirms** [I.0 Bridge](../part01-linear-algebra/00-opening.md#bridge) and [row 21](../preface.md#skill-navigation-row-21) Lab act reunion after row 56 before I.1 numbers.

**Workflow exam cross-links:** the [row 12 workflow row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) defers to row 53 when the four-step audit feels disconnected from Handshakes 3–4b; the [row 53 workflow row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) ends at row 12 Step 4 before prologue restart; the [row 52 workflow row](../epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) defers to row 12 for next-specimen audit, not replaces it. Index cards: [memory sheet row 52](../appendix/memory-sheet.md#row-52-baby-picture-epilogue-prologue-writings-canonical-reunion), [row 53](../appendix/memory-sheet.md#row-53-baby-picture-row52-row12-intra-epilogue-bridge-reunion), [row 54](../appendix/memory-sheet.md#row-54-baby-picture-rows52-53-workflow-exam-three-way-audit-reunion), [row 55](../appendix/memory-sheet.md#row-55-baby-picture-row54-row12-copper-arc-three-way-audit-reunion), [row 56](../appendix/memory-sheet.md#row-56-baby-picture-row55-opening-continuity-reunion), and [row 57](../appendix/memory-sheet.md#row-57-baby-picture-row56-i0-i1-mounting-reunion) baby pictures; full reunion maps in [sources row 52](sources.md#epilogue-prologue-writings-canonical-reunion-index-row-52), [sources row 53](sources.md#row52-row12-intra-epilogue-handshake-bridge-reunion-index-row-53), [sources row 54](sources.md#rows52-53-workflow-exam-three-way-audit-reunion-index-row-54), [sources row 55](sources.md#row54-row12-copper-arc-three-way-audit-reunion-index-row-55), [sources row 56](sources.md#row55-opening-continuity-reunion-index-row-56), and [sources row 57](sources.md#row56-i0-i1-mounting-reunion-index-row-57).

## Canonical sources

Chapter markdown is authored under [`writings/`](../../writings/) (Functional Analysis Notes layout) and synced into `src/` via [`scripts/sync-writings.sh`](../../scripts/sync-writings.sh). For PDF links, repositories, and the full chapter roadmap, see [Sources and Further Reading](sources.md).

## Bridge

This page answers *what did that symbol mean last time?* The [chapter roadmap](sources.md) answers *where does each chapter sit in reading order?* The [Final Memory Sheet](memory-sheet.md) answers *what habits and traps should I carry to the next project?*

Return to the [prologue](../prologue/00-many-scales.md) when a new specimen replaces copper — the four questions and six-act lab table apply to any material. Return to the [epilogue](../epilogue/multiscale.md) when you need to wire codes together rather than recall vocabulary.
