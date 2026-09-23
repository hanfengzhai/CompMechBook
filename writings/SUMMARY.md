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
