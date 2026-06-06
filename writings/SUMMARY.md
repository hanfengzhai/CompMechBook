# Writings — Source Index

Canonical markdown sources for **Computational Mechanics** (CompMechBook). Each subtree is a standalone mdBook in the **Functional Analysis Notes** style (`book.toml`, `chapters/SUMMARY.md`, numbered `01`–`NN` files). Sync into the main book with `./scripts/sync-writings.sh`.

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

The vendored tree mirrors the intended `Writings.git` submodule layout. When the remote repository is linked, replace this directory with the submodule and re-run `./scripts/sync-writings.sh` — chapter numbering and **Bridge** sections stay the same.
