# Writings — Source Index

Canonical markdown sources for **Computational Mechanics** (CompMechBook). When this directory is a git submodule from `Writings.git`, each subtree maps to book parts as documented in [`README.md`](./README.md).

| Subtree | Book destination | Status |
|---------|------------------|--------|
| [`linear-algebra/`](./linear-algebra/) | Part I — The Grammar of Computation | Present (mdBook) |
| [`functional-analysis/`](./functional-analysis/) | Part II — Function Spaces | Present (mdBook) |
| [`pde/`](./pde/) | Part III — Fields on Domains | Present (mdBook) |
| [`fem/`](./fem/) | Part IV — Finite Element Method | Present (mdBook) |
| [`fvm/`](./fvm/) | Part V — Conservation on Cells | Present (mdBook) |
| [`continuum/`](./continuum/) | Part VI — Continuum Mechanics | Present (mdBook) |
| [`defects/`](./defects/) | Part VII — Defects & Dislocations | Present (mdBook) |
| [`md/`](./md/) | Part VIII — Atomistic Simulation | Present (mdBook) |
| [`dft/`](./dft/) | Part IX — Electronic Structure | Present (mdBook) |

Each subtree follows the **Functional Analysis Notes** layout: `book.toml`, `chapters/SUMMARY.md`, and numbered chapter files `01-*.md` … synced into matching `src/partNN-*` directories via `./scripts/sync-writings.sh`.
