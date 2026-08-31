# Computational Mechanics

A continuous narrative book — from linear algebra through functional analysis, finite elements and volumes, continuum mechanics, dislocation dynamics, molecular dynamics, and density functional theory — told through one copper wire under tension and current.

**~222k words** · **35 numbered chapters** · **mdBook** · canonical sources in [`writings/`](writings/)

## Read the book

```bash
./scripts/install-mdbook.sh   # once
export PATH="/usr/local/cargo/bin:$HOME/.local/bin:$PATH"
mdbook build
mdbook serve                 # http://localhost:3000
```

Built HTML lands in `book/`.

## Story and structure

The book follows the **Functional Analysis Notes** (ME 412) layout — numbered chapters, concept maps (object → structure → theorem → failure mode), and **Bridge** sections linking each chapter to the next — extended with narrative devices so the arc reads as one novel:

| Device | Purpose |
|--------|---------|
| **Scene** | Return to the copper wire in the lab |
| **Bridge** | State why the next chapter must exist |
| **Lab act** | Worked computation (assembly, LAMMPS, OpenDiS, QE) |
| **Concept map** | ME 412 four-question checkpoint at part openings |

### Reading order

| Part | Topic | Chapters |
|------|-------|----------|
| Preface / Prologue | Plot spine, one wire many scales | — |
| **I** | Linear algebra | 4 |
| **II** | Functional analysis | 5 |
| **III** | PDEs and weak forms | 4 |
| **IV** | Finite element method | 5 |
| **V** | Finite volume method / CFD | 4 |
| **VI** | Continuum mechanics | 4 |
| **VII** | Defects and dislocation dynamics | 3 |
| **VIII** | Molecular dynamics | 3 |
| **IX** | Density functional theory | 3 |
| Epilogue | Multiscale coupling | — |
| Appendices | Glossary, sources, memory sheet | — |

See [`src/SUMMARY.md`](src/SUMMARY.md) for the full table of contents.

## Writings source integration

Canonical chapter markdown lives under [`writings/`](writings/) (vendored from the author's **Writings** repository). Each subtree is a standalone mdBook mirroring the Functional Analysis Notes structure.

```bash
# Edit canonical sources, then sync into src/
./scripts/sync-writings.sh
mdbook build

# Verify sync
./scripts/sync-writings.sh --check
```

Build all standalone note books:

```bash
./scripts/build-all-writings.sh
```

## Multiscale workflow scripts

The epilogue wires DFT → MD → DDD → FEM handshakes for the copper wire. Parser scripts audit foundation folders and export YAML pedigree files:

```bash
./scripts/test-fixtures.sh                              # CI smoke test
./scripts/parse_multiscale_workflow.sh fixtures/cu.foundation fixtures/cht_wire.conf
```

Handshake 3 evaluates quasiharmonic \(\alpha(T_w)\) at the **converged wall temperature** from Handshake 2 (CHT), not a 300 K default — the temperature pedigree chain documented in [memory sheet rows 8–9](src/appendix/memory-sheet.md#rows-8-9-baby-picture-tw-temperature-pedigree).

## License and sources

Teaching notes and course materials are cited in [`src/appendix/sources.md`](src/appendix/sources.md). The [Functional Analysis Notes PDF](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) is the structural template for Parts II–III and the concept-map discipline throughout.
