# Writings — Source Index

Canonical markdown sources for **Computational Mechanics** (CompMechBook). This directory holds the author's note corpus in **Functional Analysis Notes** layout: each topic is a standalone mdBook with `book.toml`, `chapters/SUMMARY.md`, and numbered `01-*.md` … files.

| Subtree | Book destination | Status |
|---------|------------------|--------|
| [`linear-algebra/`](./linear-algebra/) | Part I — The Grammar of Computation | mdBook (4 chapters) |
| [`functional-analysis/`](./functional-analysis/) | Part II — Function Spaces | mdBook (5 chapters) |
| [`pde/`](./pde/) | Part III — Fields on Domains | mdBook (4 chapters) |
| [`fem/`](./fem/) | Part IV — Finite Element Method | mdBook (5 chapters) |
| [`fvm/`](./fvm/) | Part V — Conservation on Cells | mdBook (4 chapters) |
| [`continuum/`](./continuum/) | Part VI — Continuum Mechanics | mdBook (3 chapters) |
| [`defects/`](./defects/) | Part VII — Defects & Dislocations | mdBook (2 chapters) |
| [`md/`](./md/) | Part VIII — Atomistic Simulation | mdBook (2 chapters) |
| [`dft/`](./dft/) | Part IX — Electronic Structure | mdBook (2 chapters) |

Narrative-only material (preface, prologue, epilogue, appendix) lives only under `src/` in the main book.

## Sync into CompMechBook

```bash
chmod +x scripts/sync-writings.sh
./scripts/sync-writings.sh
mdbook build
```

## Build a standalone note set

```bash
cd writings/functional-analysis && mdbook build
cd writings/pde && mdbook build
# … any subtree with book.toml
```
