# Writings — source index

Canonical mdBook sources for **Computational Mechanics**. Each subtree follows the Functional Analysis Notes layout: `book.toml`, `chapters/SUMMARY.md`, `00-opening.md`, numbered `01`–`NN` chapter files.

## Continuous reading order

The unified book in [`src/`](../src/SUMMARY.md) reads like one novel: a copper wire in wedge grips is the through-line from linear algebra to DFT. Start at [preface](./preface/chapters/preface.md) (plot spine and four narrative devices — **Scene**, **Bridge**, **Lab act**, **Concept map**), then [prologue](./prologue/chapters/00-many-scales.md), then Parts I–IX in table order, and close with [epilogue](./epilogue/chapters/multiscale.md). Every numbered chapter ends with a **Bridge** explaining why the next chapter exists; part openings mirror the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) discipline (object → structure → theorem → failure mode). When a jump feels abrupt, read the prior chapter's Bridge — that hinge is the intentional stitch between scales.

| Subtree | Book part | Chapters |
|---------|-----------|----------|
| [preface](./preface/chapters/SUMMARY.md) | Preface | preface |
| [prologue](./prologue/chapters/SUMMARY.md) | Prologue | 00 |
| [epilogue](./epilogue/chapters/SUMMARY.md) | Epilogue | multiscale |
| [linear-algebra](./linear-algebra/chapters/SUMMARY.md) | Part I | 00, 01–04 |
| [functional-analysis](./functional-analysis/chapters/SUMMARY.md) | Part II | 00, 01–05 |
| [pde](./pde/chapters/SUMMARY.md) | Part III | 00, 01–04 |
| [fem](./fem/chapters/SUMMARY.md) | Part IV | 00, 01–05 |
| [fvm](./fvm/chapters/SUMMARY.md) | Part V | 00, 01–04 |
| [continuum](./continuum/chapters/SUMMARY.md) | Part VI | 00, 01–04 |
| [defects](./defects/chapters/SUMMARY.md) | Part VII | 00, 01–03 |
| [md](./md/chapters/SUMMARY.md) | Part VIII | 00, 01–03 |
| [dft](./dft/chapters/SUMMARY.md) | Part IX | 00, 01–03 |
| [appendix](./appendix/chapters/SUMMARY.md) | Appendices | glossary, sources, memory-sheet ([reading map](./appendix/README.md#reading-map-continuous-book)) |

Sync into the main book:

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, replace or merge these subtrees with upstream content and re-run the sync script.

## Multiscale story arc (one table)

The book climbs **up** from discrete algebra to continuum PDEs and FEM/FVM (Parts I–V), then **across** constitutive mechanics (Part VI), then **down** through defects, atoms, and electrons (Parts VII–IX). The copper wire stays the protagonist; only the ruler changes.

| Read order | Scale / question | Method & math | Wire beat (lab time) |
|------------|------------------|---------------|----------------------|
| Preface → Prologue | Why one story? | Plot spine, two clocks (I→IX vs Acts I–VI) | Mount wire; name the six acts |
| **I** | Nodal DOFs | Linear algebra, \(\mathbf{K}\mathbf{u}=\mathbf{f}\), modes | Springs in tension; first load cell reading |
| **II** | Fields in \(H^1, L^2\) | Functional analysis (ME 412 layout) | Mesh refines; energy norms replace dot products |
| **III** | Weak PDEs | Sobolev spaces, energy methods | Corners break strong forms; weak form appears |
| **IV** | Solid mesh | FEM / Galerkin | Assemble stiffness; thermoelastic \(h\)-study |
| **V** | Fluid & CHT | FVM, fluxes, Navier–Stokes | Air cools the wire; Robin \(h\) → resolved convection |
| **VI** | Continuum body | Kinematics, stress, variational elasticity | Joule heat + grip strain; \(J_2\) preview before descent |
| **VII** | Mesoscale defects | DDD, GSF, polycrystal handoff | Forest replaces fitted \(H\); OpenDiS mobility |
| **VIII** | Atoms | MD, ensembles, coarse-graining | NVT shear calibrates rates; phonon lifetimes |
| **IX** | Electrons | DFT, Kohn–Sham, workflows | Quasiharmonic \(\alpha(T_w)\); foundation folder |
| Epilogue | Coupled codes | Handshakes 1–4, pedigree YAML | Same afternoon: DFT → MD → DDD → FEM reunion |
| Appendix | Reference | Glossary, sources, memory sheet | When the plot stutters, use continuity-hinge rows |

**Smooth reading rule:** never skip a chapter **Bridge** — it is the hinge that explains why the next scale (or the next discretization) is forced by the physics, not by the syllabus. At part openings, read **Story so far** → **Closing the arc** ([rows 26–27](./appendix/chapters/sources.md#story-so-far-reunion-index-row-26)); at chapter Bridges where symbols translate but input-deck numbers feel arbitrary, read the **Scale-boundary handshake** ([row 28](./appendix/chapters/sources.md#scale-boundary-reunion-index-row-28) · [appendix reading map](./appendix/README.md#reading-map-continuous-book)); in **Part IV**, when Acts II–III feel like separate FEM homework despite restored export pedigree, read the **thermoelastic assembly thread** ([row 29](./appendix/chapters/sources.md#thermoelastic-assembly-reunion-index-row-29) · [IV.0 thread](./fem/chapters/00-opening.md#acts-ii-and-iii-together-thermoelastic-assembly-thread)); in **Part IV–V**, when solid FEM and fluid FVM still feel like separate solvers despite row 29, read the **CHT outer-loop thread** ([row 30](./appendix/chapters/sources.md#cht-outer-loop-reunion-index-row-30) · [V.4 Picard + parser](./fvm/chapters/04-navier-stokes-cfd.md#parser-checkpoint-archive-cht-export-yaml)); in **Part VI**, when Galerkin assembly and virtual work still feel like separate subjects despite row 30, read the **twin-ladder → virtual work thread** ([row 31](./appendix/chapters/sources.md#twin-ladder-virtual-work-reunion-index-row-31) · [VI.3 virtual work Lab act](./continuum/chapters/03-variational-elasticity.md#lab-act-virtual-work-equals-load-cell-reading-act-iii--pulling)); when virtual work and return-mapping still feel like separate subjects despite row 31, read the **virtual work → plasticity preview thread** ([row 32](./appendix/chapters/sources.md#virtual-work-plasticity-preview-reunion-index-row-32) · [VI.3 opening hinge → VI.4](./continuum/chapters/03-variational-elasticity.md#opening-hinge-vi3-to-vi4) · [VI.4 return-mapping Lab act](./continuum/chapters/04-nonlinear-plasticity-preview.md#lab-act-return-mapping-on-the-load-cell-knee-act-iv-hardening)); when mesoscale DDD and atomistic MD still feel like separate courses despite row 32, read the **Part VII → VIII descent hinge thread** ([row 33](./appendix/chapters/sources.md#part-vii-viii-descent-hinge-reunion-index-row-33) · [VII.2 mobility Lab act at \(T_w\)](./defects/chapters/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) · [Part VIII descent hinge](./md/chapters/00-opening.md#descent-hinge-cores-mobility-and-tw-pedigree)); when 0 K EAM minimization and NVT/NPT at \(T_w\) still feel like separate subjects despite row 33, read the **potentials → ensembles thread** ([row 34](./appendix/chapters/sources.md#potentials-ensembles-reunion-index-row-34) · [VIII.1 Bridge](./md/chapters/01-potentials-phase-space.md#bridge) · [VIII.2 opening hinge](./md/chapters/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2)); when audited NVT/NPT trajectories and yaml handoff tables still feel like separate subjects despite row 34, read the **ensembles → coarse-graining thread** ([row 35](./appendix/chapters/sources.md#ensembles-coarse-graining-reunion-index-row-35) · [VIII.2 Bridge](./md/chapters/02-ensembles-integrators.md#bridge) · [VIII.3 opening hinge](./md/chapters/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3)); when the pedigree checklist has consumer rows filled but Part IX still feels like standalone DFT coursework despite row 35, read the **coarse-graining → electronic audit thread** ([row 36](./appendix/chapters/sources.md#coarse-graining-electronic-audit-reunion-index-row-36) · [VIII.3 Bridge to Part IX](./md/chapters/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) · [IX.0 opening hinge](./dft/chapters/00-opening.md#opening-hinge-viii3-to-ix)); when `cu.relax.out` and \(\alpha(T_w)\) exist but Born–Oppenheimer and Hohenberg–Kohn still feel like standalone quantum chemistry despite row 36, read the **electronic audit → Born–Oppenheimer thread** ([row 37](./appendix/chapters/sources.md#electronic-audit-born-oppenheimer-reunion-index-row-37) · [IX.0 Bridge](./dft/chapters/00-opening.md#bridge) · [IX.1 opening hinge](./dft/chapters/01-born-oppenheimer.md#opening-hinge-ix0-to-ix1)); when Born–Oppenheimer and Hohenberg–Kohn are understood but Kohn–Sham SCF still feels like standalone quantum chemistry despite row 37, read the **Born–Oppenheimer → Kohn–Sham thread** ([row 38](./appendix/chapters/sources.md#born-oppenheimer-kohn-sham-reunion-index-row-38) · [IX.1 Bridge](./dft/chapters/01-born-oppenheimer.md#bridge) · [IX.2 opening hinge](./dft/chapters/02-kohn-sham.md#opening-hinge-ix1-to-ix2)); when Kohn–Sham SCF is understood but DFT workflows still feel like standalone coursework despite row 38, read the **Kohn–Sham → DFT workflows thread** ([row 39](./appendix/chapters/sources.md#kohn-sham-dft-workflows-reunion-index-row-39) · [IX.2 Bridge](./dft/chapters/02-kohn-sham.md#bridge) · [IX.3 opening hinge](./dft/chapters/03-dft-workflows.md#opening-hinge-ix2-to-ix3)). When a turn feels mechanical **inside** Parts I–V, use the [intra-part ascent Bridge reunion tables](./appendix/chapters/sources.md#bridge-reunion-intra-part-ascent-i-v); **inside** Parts VI–IX, use the [intra-part descent Bridge reunion tables](./appendix/chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) (each part `README.md` links its row).

## Functional Analysis Notes layout (Writings.git parity)

Every subtree under `writings/` mirrors the [**Functional Analysis Notes**](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) (ME 412) discipline — not by copying proofs, but by repeating the same **reading contract**:

| Template element | Role in the continuous book |
|------------------|-----------------------------|
| `book.toml` + `chapters/SUMMARY.md` | Standalone mdBook; same numbering as `src/partNN-*` |
| `00-opening.md` | **Scene**, chapter guide, **concept map** (object → structure → theorem → failure mode), representative schematics |
| `01`–`NN` chapters | Mechanics-first prose, **Lab act** workflows, **plot spine (one line)** at chapter open |
| **Bridge** (end of each chapter) | Narrative hinge — why the next chapter or part is forced by the wire, not the syllabus |

Upstream course notes (vendored here until the `Writings` submodule links) supply the baby pictures each part opening indexes:

| Part | Writings subtree | Upstream note (ME 412-style map) | Numbered chapters |
|------|------------------|----------------------------------|-------------------|
| I | [linear-algebra](./linear-algebra/chapters/SUMMARY.md) | [ME 300A Linear Algebra](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) | 01–04 |
| II | [functional-analysis](./functional-analysis/chapters/SUMMARY.md) | [ME 412 Functional Analysis](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) | 01–05 |
| III | [pde](./pde/chapters/SUMMARY.md) | [ME 300B PDE](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) | 01–04 |
| IV | [fem](./fem/chapters/SUMMARY.md) | [FEA notes](https://hanfengzhai.github.io/file/FEA_notes.pdf) | 01–05 |
| V | [fvm](./fvm/chapters/SUMMARY.md) | [FVM](https://hanfengzhai.github.io/note/FVM.pdf) · [CFD](https://hanfengzhai.github.io/file/CFD_note.pdf) | 01–04 |
| VI | [continuum](./continuum/chapters/SUMMARY.md) | [Elasticity & inelasticity](https://hanfengzhai.github.io/file/elasticity_notes.pdf) | 01–04 |
| VII | [defects](./defects/chapters/SUMMARY.md) | [Defects & disorders](https://hanfengzhai.github.io/file/defects_notes.pdf) | 01–03 |
| VIII | [md](./md/chapters/SUMMARY.md) | [Atomistic modeling](https://hanfengzhai.github.io/file/AtomModel_note.pdf) | 01–03 |
| IX | [dft](./dft/chapters/SUMMARY.md) | MSE 5720 coursework / QE workflows (see [IX.0 schematics](./dft/chapters/00-opening.md)) | 01–03 |

**Edit workflow:** change markdown under `writings/<topic>/chapters/`, run `./scripts/sync-writings.sh`, then `mdbook build`. The [multiscale story arc](#multiscale-story-arc-one-table) table above is the one-page plot; the [appendix sources chapter](./appendix/chapters/sources.md#continuity-hinges-index-when-the-plot-stutters) is the full continuity-hinge index when a transition still feels abrupt.
