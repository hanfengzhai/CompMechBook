# Sources and Further Reading

This book synthesizes material from the author's notes, coursework, and teaching. Canonical chapter sources live under [`writings/`](../writings/) (Functional Analysis Notes layout). Run `./scripts/sync-writings.sh` to copy them into `src/`. When the external `Writings` git submodule is linked, prefer upstream content and re-run the sync script.

## Scene: two clocks on the same afternoon

The book reads in **mathematical order** (Part I before Part IX), but the copper wire lives in **laboratory time** (mounting before hardening). The chapter roadmap below follows mathematical order — the order the Functional Analysis Notes layout assumes. When you need to know *which act of the experiment* a chapter belongs to, use the six-act table in the next section or the full narrative in the [prologue](../prologue/00-many-scales.md#the-experiment-as-plot).

## Six acts → parts (laboratory time)

| Act | Lab beat | Primary parts | Opening links |
|-----|----------|---------------|---------------|
| I — Mounting | Grips close; first \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | Prologue, I | [Prologue](../prologue/00-many-scales.md), [I.0](../part01-linear-algebra/00-opening.md) |
| II — Warming | Current on; thermocouple rises | III, IV, V | [III.0](../part03-pdes/00-opening.md), [IV.0](../part04-fem/00-opening.md), [V.0](../part05-fvm/00-opening.md) |
| III — Pulling | Force–displacement ramp | II, III, IV, VI | [II.0](../part02-functional-analysis/00-opening.md), [III.0](../part03-pdes/00-opening.md), [IV.0](../part04-fem/00-opening.md), [VI.0](../part06-continuum/00-opening.md) |
| IV — Hardening | Curve bends upward | VII | [VII.0](../part07-defects/00-opening.md) |
| V — Notch | Stress concentrator | VI, VIII | [VI.0](../part06-continuum/00-opening.md), [VIII.0](../part08-md/00-opening.md) |
| VI — Foundation | Parameters before the run | IX → VIII → VII → IV | [IX.0](../part09-dft/00-opening.md) → [VIII.0](../part08-md/00-opening.md) → [VII.0](../part07-defects/00-opening.md) → [IV.0](../part04-fem/00-opening.md) |

Act VI runs **in parallel** with Acts I–V in real projects: no FEM deck starts without moduli whose pedigree traces to finer models or calibration. The [epilogue](../epilogue/multiscale.md) reunites all six acts in one multiscale afternoon.

## Parameter pedigree path (Act VI reading order)

The book reads **mathematically** from Part I to Part IX — grammar before descent. Real projects often read **downward** when building an input deck: start at electrons, export numbers, climb until FEM has honest moduli. Act VI is that reverse ladder on the same copper wire:

```mermaid
flowchart BT
  DFT[IX.3 DFT workflows: C_ij, gamma_sf, E_coh]
  MD[VIII.2-3 MD: EAM fit, mobility M(tau,T)]
  DDD[VII.2 DDD: tau(rho), hardening laws]
  FEM[IV.4 FEM: Voigt E, nu in assembly]
  DFT --> MD
  MD --> DDD
  DDD --> FEM
```

| Step | Read | Export | Wire-scale consumer |
|------|------|--------|---------------------|
| 1 | [IX.3](../part09-dft/03-dft-workflows.md) | \(C_{ij}\), \(\gamma_{\text{sf}}\), cohesive energy | Elastic constants, partial separation in DDD |
| 2 | [VIII.3](../part08-md/03-ab-initio-and-coarse-graining.md) | EAM table, phonon check | Production MD and mobility fitting |
| 3 | [VIII.2](../part08-md/02-ensembles-integrators.md) | \(M(\tau, T)\) from constrained shear | OpenDiS mobility law |
| 4 | [VII.2](../part07-defects/02-dislocation-dynamics.md) | \(\tau(\gamma)\), \(\rho(\gamma)\), \(\alpha\) | Crystal plasticity / Voce hardening |
| 5 | [IV.4](../part04-fem/04-poisson-to-elasticity.md) | \(\mathbf{K}\) with documented \(E\), \(\nu\) | Load-cell linear regime in Act III |

Each arrow needs a convergence log and a unit check — the epilogue's four-handshake sensitivity table ranks which exports dominate for a given question. **Mathematical order** teaches why the ladder exists; **pedigree order** fills the input deck before the grips close.

## Narrative beat map (mathematical order × lab act)

The book reads in mathematical order (Part I before Part IX), but the copper wire lives in laboratory time. Use this table when you want **both** clocks at once — the story beat that should feel familiar when the symbols change.

| Chapter | Lab act | Narrative beat (one sentence) |
|---------|---------|--------------------------------|
| Prologue | Preview | One wire, eight scales, four questions |
| I.1–I.3 | I — Mounting | Springs, assembly, the wire rings |
| I.4 | I → II | Thermocouples multiply; vectors become fields |
| II.1–II.5 | III (preview) | The room where weak forms live |
| III.1–III.4 | II–III | Strong form fails; energy chooses the solution |
| IV.1–IV.5 | I, III | Mesh the solid; choose FEM or FVM door |
| V.1–V.4 | II | Cool the wire; balance fluxes in air |
| VI.1–VI.3 | II–III | Name stress; virtual work behind \(\mathbf{K}\) |
| VI.4 | II–IV → descent | [Intermission](../part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins): ascent ends; \(J_2\) placeholders await a forest |
| VII.0–VII.3 | IV | Forest hardens; export \(\tau(\gamma)\) |
| VIII.1–VIII.3 | V–VI | Atoms at the notch; fit potential |
| IX.1–IX.3 | VI | Electrons; archive pedigree |
| Epilogue | All six | Wire the rungs; sensitivity ranks |

When a chapter's **Bridge** names the next part, cross-check this table — the laboratory beat may lag or lead the mathematics by one part (Act II warming appears in Part III–V prose while Act III pulling is Part IV–VI). That offset is intentional: the wire heats before it yields.

## Continuity hinges index (when the plot stutters)

The [preface](../preface.md) documents opening, ascent, midpoint, descent, and epilogue hinge tables separately. The [memory sheet](memory-sheet.md#continuity-hinges-master-map) collects all twelve rows in one navigation page. Use this index when you know **which chapter** you are in but cannot feel the handoff to the next:

| Chapter region | Hinge anchor | What should click |
|----------------|--------------|-------------------|
| Prologue → I.0 | [Prologue Bridge](../prologue/00-many-scales.md#bridge-to-part-i) | Panorama ladder becomes explicit \(\mathbf{K}\mathbf{u}=\mathbf{f}\) grammar |
| I.4 → II.0 | [I.4 Bridge](../part01-linear-algebra/04-toward-infinity.md#bridge-to-part-ii) | Nodal vectors become fields; \(\mathbf{K}_N\) becomes an operator |
| II.5 → III.0 | [II.5 Bridge](../part02-functional-analysis/05-spectral-theorem.md#bridge-to-part-iii) | Completeness hands off to weak Poisson and heat |
| III.4 → IV.0 | [III.4 Bridge](../part03-pdes/04-energy-methods.md#bridge-to-part-iv) | Lax–Milgram becomes Galerkin assembly |
| IV.5 / V.4 → VI.0 | [Two doors](../part04-fem/05-convergence.md#bridge-two-doors-from-here) | FEM and FVM converge on Cauchy stress |
| VI.0 / VI.4 → VII.0 | [Midpoint](../part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead), [intermission](../part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) | Ascent complete; \(J_2\) placeholders yield to forest |
| VII.3 → VIII.0 | [VII.3 Bridge](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) | Line cores need atomic bonding |
| VIII.3 → IX.0 | [VIII.3 Bridge](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) | Potentials on trust need SCF audit |
| IX.3 → Epilogue | [IX.3 Bridge](../part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) | Finest rung; upward homogenization begins |
| Epilogue (workflow) | [Six-act reunion](../epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) | Reading order reunites with laboratory time |
| Epilogue → Prologue | [Epilogue Bridge](../epilogue/multiscale.md#bridge) | Four questions restart on the next project |

## Chapter roadmap (one continuous arc)

Read in order for the full narrative. Each row is one chapter; **Bridge** sections at chapter ends explain the handoff to the next row.

| # | Chapter | One-line role in the story |
|---|---------|----------------------------|
| — | [Preface](../preface.md) | Why one book; copper-wire reading map |
| — | [Prologue](../prologue/00-many-scales.md) | Same copper wire at every scale; the ladder |
| I.0 | [Linear algebra opening](../part01-linear-algebra/00-opening.md) | Finite-dimensional grammar shared by all codes |
| I.1 | [Vectors and matrices](../part01-linear-algebra/01-vectors-matrices.md) | \(\mathbf{K}\mathbf{u}=\mathbf{f}\) on the wire as springs |
| I.2 | [Linear maps](../part01-linear-algebra/02-linear-maps.md) | Bases, change of coordinates, stiffness assembly |
| I.3 | [Eigenvalues](../part01-linear-algebra/03-eigenvalues.md) | Vibration modes that decouple complexity |
| I.4 | [Toward infinity](../part01-linear-algebra/04-toward-infinity.md) | \(N\to\infty\); functions, operators, \(L^2\) |
| II.0 | [Functional analysis opening](../part02-functional-analysis/00-opening.md) | Concept map (ME 412 template) |
| II.1 | [Motivation](../part02-functional-analysis/01-motivation.md) | Why weak forms; corners and kinks |
| II.2 | [Normed spaces](../part02-functional-analysis/02-normed-spaces.md) | Completeness; energy norms |
| II.3 | [Hilbert spaces](../part02-functional-analysis/03-hilbert-spaces.md) | Inner products; orthogonality of modes |
| II.4 | [Operators and duality](../part02-functional-analysis/04-operators-duality.md) | Loads as functionals; adjoints |
| II.5 | [Spectral theorem](../part02-functional-analysis/05-spectral-theorem.md) | Compactness; Galerkin convergence |
| III.0 | [PDE opening](../part03-pdes/00-opening.md) | Fields on domains |
| III.1 | [Strong form](../part03-pdes/01-strong-form.md) | Classical PDEs and their limits |
| III.2 | [Weak form](../part03-pdes/02-weak-form.md) | Test functions; integration by parts |
| III.3 | [Sobolev spaces](../part03-pdes/03-sobolev-spaces.md) | Regularity for FEM |
| III.4 | [Energy methods](../part03-pdes/04-energy-methods.md) | Minimum principles; Lax–Milgram |
| IV.0 | [FEM opening](../part04-fem/00-opening.md) | Galerkin as projection |
| IV.1 | [Weighted residuals](../part04-fem/01-weighted-residuals.md) | From PDE to discrete system |
| IV.2 | [Galerkin assembly](../part04-fem/02-galerkin-assembly.md) | Local-to-global \(\mathbf{K}\) |
| IV.3 | [Elements and quadrature](../part04-fem/03-elements-quadrature.md) | Shape functions; patch tests |
| IV.4 | [Poisson to elasticity](../part04-fem/04-poisson-to-elasticity.md) | Vector problems on the wire |
| IV.5 | [Convergence](../part04-fem/05-convergence.md) | Error norms; **two doors** to Parts V or VI |
| V.0 | [FVM opening](../part05-fvm/00-opening.md) | Flux balance philosophy |
| V.1 | [Conservation integral](../part05-fvm/01-conservation-integral.md) | Control volumes |
| V.2 | [FVM in 1D](../part05-fvm/02-fvm-1d.md) | Upwind advection (worked Python) |
| V.3 | [Fluxes and Riemann](../part05-fvm/03-fluxes-riemann.md) | Shock capturing |
| V.4 | [Navier–Stokes and CFD](../part05-fvm/04-navier-stokes-cfd.md) | SIMPLE; conjugate heat transfer |
| VI.0 | [Continuum opening](../part06-continuum/00-opening.md) | Shared stress–strain vocabulary |
| VI.1 | [Kinematics](../part06-continuum/01-kinematics.md) | \(\mathbf{F}\), strain measures |
| VI.2 | [Stress and balance](../part06-continuum/02-stress-balance.md) | Cauchy stress; conservation laws |
| VI.3 | [Variational elasticity](../part06-continuum/03-variational-elasticity.md) | Virtual work; hyperelasticity |
| VI.4 | [Nonlinear plasticity preview](../part06-continuum/04-nonlinear-plasticity-preview.md) | When continuum fields fail |
| VII.0 | [Defects opening](../part07-defects/00-opening.md) | Singularities and mesoscale |
| VII.1 | [Defect taxonomy](../part07-defects/01-defect-taxonomy.md) | Point, line, surface defects |
| VII.2 | [Dislocation dynamics](../part07-defects/02-dislocation-dynamics.md) | DDD; Taylor hardening |
| VII.3 | [Polycrystal handoff](../part07-defects/03-polycrystal-and-fem-handoff.md) | OpenDiS→DAMASK→FEM |
| VIII.0 | [MD opening](../part08-md/00-opening.md) | Atoms when fields break down |
| VIII.1 | [Potentials](../part08-md/01-potentials-phase-space.md) | EAM; phase space |
| VIII.2 | [Ensembles and integrators](../part08-md/02-ensembles-integrators.md) | LAMMPS workflows |
| VIII.3 | [Ab initio MD](../part08-md/03-ab-initio-and-coarse-graining.md) | DeepMD; coarse-graining |
| IX.0 | [DFT opening](../part09-dft/00-opening.md) | Electrons at the finest rung |
| IX.1 | [Born–Oppenheimer](../part09-dft/01-born-oppenheimer.md) | Separating electrons and nuclei |
| IX.2 | [Kohn–Sham](../part09-dft/02-kohn-sham.md) | SCF cycle; convergence |
| IX.3 | [DFT workflows](../part09-dft/03-dft-workflows.md) | Quantum ESPRESSO on Cu |
| — | [Epilogue](../epilogue/multiscale.md) | Coupling DFT→MD→DDD→FEM |
| — | [Final Memory Sheet](../appendix/memory-sheet.md) | Book-wide habits and traps (ME 412 style) |

## Primary notes (hanfengzhai.github.io)

| Topic | Link |
|-------|------|
| Linear Algebra (ME 300A) | [ME300A_LinAlg.pdf](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) |
| Functional Analysis (ME 412) | [ME412_CourseSummary.pdf](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) |
| Partial Differential Equations (ME 300B) | [ME300B_PDE.pdf](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) |
| Finite Element Analysis | [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf) |
| FEA Problem Sessions & Tutorials | [note.html](https://hanfengzhai.github.io/note.html) |
| Elasticity & Inelasticity | [elasticity_notes.pdf](https://hanfengzhai.github.io/file/elasticity_notes.pdf) |
| Nonlinear FEA | [NonlinFEA_note.pdf](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) |
| Computational Fluid Dynamics | [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf) |
| Finite Volume Method | [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) |
| Defects & Disorders | [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf) |
| Atomistic Modeling | [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf) |
| Statistical Mechanics | [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf) |
| Computational Methods (applied mechanics) | [CompMethMechProb.pdf](https://hanfengzhai.github.io/file/CompMethMechProb.pdf) |

## Code and coursework repositories

| Topic | Repository |
|-------|------------|
| DFT (MSE 5720) | [MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW) |
| Dislocation dynamics | [OpenDiS](https://github.com/OpenDiS/OpenDiS) |
| Multiscale graphene fracture | [multiscale-graphene-fracture](https://github.com/hanfengzhai/multiscale-graphene-fracture) |

## Related topics (beyond this book's arc)

The narrative stops at DFT for equilibrium electronic structure, but the author's notes cover adjacent rungs worth climbing after the epilogue:

| Topic | Notes | Connection to the ladder |
|-------|-------|--------------------------|
| Nonlinear FEA | [NonlinFEA_note.pdf](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) | Extends Part IV–VI for finite strain and path-dependent solids |
| Smoothed particle hydrodynamics | [SPH.pdf](https://hanfengzhai.github.io/file/SPH.pdf) | Lagrangian alternative to Part V FVM for free-surface flows |
| Inverse problems & design optimization | [InverseProb.pdf](https://hanfengzhai.github.io/file/InverseProb.pdf), [DesignOpt.pdf](https://hanfengzhai.github.io/file/DesignOpt.pdf) | Uses FEM/MD outputs as forward models for material design |
| Statistical mechanics | [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf) | Bridges Part VIII ensembles to thermodynamic averages |
| Machine learning for multiscale modeling | [MLMultiscale.pdf](https://hanfengzhai.github.io/file/MLMultiscale.pdf) | Surrogate acceleration discussed in the epilogue |

Dislocation **link statistics** during strain hardening — active vs. inactive slip systems, exponential vs. double-exponential link-length distributions — are developed in [Akhondzadeh, Zhai et al., *J. Mech. Phys. Solids* (2026)](https://doi.org/10.1016/j.jmps.2026.106533) and summarized in Part VII.

## Standard references (external)

**Functional analysis & PDEs**

- Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*
- Evans, *Partial Differential Equations*

**Finite elements**

- Brenner & Scott, *The Mathematical Theory of Finite Element Methods*
- Zienkiewicz & Taylor, *The Finite Element Method*

**Finite volumes & CFD**

- LeVeque, *Finite Volume Methods for Hyperbolic Problems*
- Ferziger, Perić, & Street, *Computational Methods for Fluid Dynamics*

**Continuum mechanics**

- Gurtin, *An Introduction to Continuum Mechanics*
- Holzapfel, *Nonlinear Solid Mechanics*

**Atomistic & electronic structure**

- Tuckerman, *Statistical Mechanics: Theory and Molecular Simulation*
- Martin, *Electronic Structure: Basic Theory and Practical Methods*

## Building this book

```bash
# Install mdBook: https://github.com/rust-lang/mdBook/releases
mdbook build
mdbook serve   # local preview at http://localhost:3000
```

Output appears in `book/`. CI can publish to GitHub Pages on merge to `main`.

## Contributing

When integrating `Writings.git`:

1. Add as a git submodule at `writings/`
2. Map existing note paths to `src/` chapters via symlinks or include macros
3. Preserve the Functional Analysis Notes chapter numbering in Part II
4. Run `mdbook build` to verify cross-links

Pull requests that improve narrative flow, fix errors, or add worked examples are welcome at [CompMechBook](https://github.com/hanfengzhai/CompMechBook).

## Bridge

The chapter roadmap is the book in one table — read it when you need orientation, not when you need proofs. For symbol reuse across parts, open the [Glossary and Cross-Scale Index](glossary.md). For habits, traps, and a one-sitting recap in ME 412 style, open the [Final Memory Sheet](memory-sheet.md).

When you edit canonical prose, change files under [`writings/`](../writings/) first, run `./scripts/sync-writings.sh`, then `mdbook build`. The Functional Analysis Notes layout — numbered chapters, concept maps at openings, bridges at closings — is the contract every subtree shares.
