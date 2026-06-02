# Writings — Source Index

Canonical markdown sources for **Computational Mechanics** (CompMechBook). When this directory is a git submodule from `Writings.git`, each subtree maps to book parts as documented in [`README.md`](./README.md).

| Subtree | Book destination | Status |
|---------|------------------|--------|
| [`linear-algebra/`](./linear-algebra/) | Part I — The Grammar of Computation | Present (mdBook) |
| [`functional-analysis/`](./functional-analysis/) | Part II — Function Spaces | Present (mdBook) |
| [`pde/`](./pde/) | Part III — Fields on Domains | Stub (ME 300B) |
| [`fem/`](./fem/) | Part IV — Finite Element Method | Stub (FEA notes) |
| [`fvm/`](./fvm/) | Part V — Conservation on Cells | Stub (FVM / CFD notes) |
| [`continuum/`](./continuum/) | Part VI — Continuum Mechanics | Stub (elasticity) |
| [`defects/`](./defects/) | Part VII — Defects & Dislocations | Stub |
| [`md/`](./md/) | Part VIII — Atomistic Simulation | Stub |
| [`dft/`](./dft/) | Part IX — Electronic Structure | Stub (MSE 5720) |

Each present subtree follows the **Functional Analysis Notes** layout: `book.toml`, `chapters/SUMMARY.md`, and numbered chapter files `01-*.md` … synced into matching `src/partNN-*` directories via `./scripts/sync-writings.sh`.
