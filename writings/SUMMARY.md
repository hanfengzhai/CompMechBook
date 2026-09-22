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
| [appendix](./appendix/chapters/SUMMARY.md) | Appendices | glossary, sources, memory-sheet |

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

**Smooth reading rule:** never skip a chapter **Bridge** — it is the hinge that explains why the next scale (or the next discretization) is forced by the physics, not by the syllabus.

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

**Edit workflow:** change markdown under `writings/<topic>/chapters/`, run `./scripts/sync-writings.sh`, then `mdbook build`. The [multiscale story arc](#multiscale-story-arc-one-table) table above is the one-page plot; the [appendix sources chapter](./appendix/chapters/sources.md) (*Continuity hinges index*) is the full continuity-hinge index when a transition still feels abrupt.

## Synopsis — computational mechanics as one story

The book is written to read cover-to-cover like a novel, not a stack of course notes. A single copper wire in wedge grips carries tension and current; every part changes the **ruler** (nodes, mesh, control volume, continuum field, dislocation line, atom, electron density) while the **specimen** stays the same afternoon in the lab.

**One arc in one breath:** Equilibrium begins as sparse linear algebra, becomes completeness and Galerkin projection in function spaces, splits into weak PDEs and twin discretizations (FEM on the wire, FVM in the air), reunites in Cauchy stress and virtual work, then descends through dislocation forests, atomic trajectories, and self-consistent electron density until the epilogue wires DFT → MD → DDD → FEM with filenames and units — the continuous story the Functional Analysis Notes layout (object → structure → theorem → failure mode) repeats at every part opening, with **Bridge** sections stitching each chapter to the next.

**Ascent (Parts I–VI).** [Linear algebra](./linear-algebra/chapters/SUMMARY.md) names the grammar every simulator shares: state vector, sparse stiffness, modes that decouple vibration, and the limit \(N\to\infty\) that sends nodal values toward fields. [Functional analysis](./functional-analysis/chapters/SUMMARY.md) replays that grammar in \(H^1\) and \(L^2\) using the same **Functional Analysis Notes** layout as ME 412 — object, structure, theorem, failure mode at every opening. [PDEs and Sobolev spaces](./pde/chapters/SUMMARY.md) write equilibrium and heat as weak forms when strong forms fail at corners. [FEM](./fem/chapters/SUMMARY.md) and [FVM](./fvm/chapters/SUMMARY.md) are twin discretizations on the wire: Galerkin assembly on the solid, flux balance in the air that sets the wall temperature \(T_w\). [Continuum mechanics](./continuum/chapters/SUMMARY.md) reunites those outputs in \(\mathbf{F}\), \(\boldsymbol{\sigma}\), and virtual work — the midpoint where ascent ends and the load cell curve can still lie.

**Descent (Parts VII–IX).** When fitted hardening cannot survive mesh refinement, the story descends: [dislocation dynamics](./defects/chapters/SUMMARY.md) explains the knee with forests and OpenDiS mobility; [molecular dynamics](./md/chapters/SUMMARY.md) resolves cores and exports rates and phonon lifetimes at atomic timestep; [DFT](./dft/chapters/SUMMARY.md) grounds moduli and \(\alpha(T_w)\) in Kohn–Sham self-consistency. The [epilogue](./epilogue/chapters/multiscale.md) documents handshakes from Quantum ESPRESSO → LAMMPS → DDD → FEM so macro inputs carry **pedigree**, not handbook defaults.

**Smooth reading contract:** each numbered chapter ends with a **Bridge** (why the next chapter is forced by the wire). Part openings add **Scene**, **Lab act**, and **concept map** checkpoints in ME 412 style. If a jump still feels abrupt, use the [appendix sources chapter](./appendix/chapters/sources.md) (*Chapter roadmap* and *Continuity hinges index*) — the navigation layer the Functional Analysis Notes template assumes at book scale.

| Topic you need | Where it lives in this book | Upstream note (vendored in `writings/`) |
|----------------|----------------------------|----------------------------------------|
| Linear algebra | Part I | [ME 300A](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) |
| Functional analysis | Part II | [ME 412](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) |
| Weak PDEs / Sobolev | Part III | [ME 300B](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) |
| Finite element method | Part IV | [FEA notes](https://hanfengzhai.github.io/file/FEA_notes.pdf) |
| Finite volume / CFD | Part V | [FVM](https://hanfengzhai.github.io/note/FVM.pdf) · [CFD](https://hanfengzhai.github.io/file/CFD_note.pdf) |
| Continuum / plasticity preview | Part VI | [Elasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf) |
| Dislocation dynamics | Part VII | [Defects notes](https://hanfengzhai.github.io/file/defects_notes.pdf) |
| Molecular dynamics | Part VIII | [Atomistic modeling](https://hanfengzhai.github.io/file/AtomModel_note.pdf) |
| DFT / workflows | Part IX | MSE 5720 / QE (see [IX.0](./dft/chapters/00-opening.md)) |
