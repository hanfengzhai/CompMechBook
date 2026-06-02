# CompMechBook

**Computational Mechanics: From Linear Algebra to Density Functional Theory**

An mdBook-style narrative covering the mathematical and numerical foundations of computational mechanics — written as one continuous story from vectors and function spaces through finite elements and finite volumes, down to dislocation dynamics, molecular dynamics, and DFT.

## Read online

Build locally (see below) or open the rendered site once GitHub Pages is enabled.

## Structure

| Part | Topics |
|------|--------|
| Prologue | Multiscale motivation |
| I | Linear algebra |
| II | Functional analysis |
| III | PDEs & weak forms |
| IV | Finite element method |
| V | Finite volume method & CFD |
| VI | Continuum mechanics |
| VII | Defects & dislocation dynamics |
| VIII | Molecular dynamics |
| IX | Density functional theory |
| Epilogue | Multiscale coupling |

The table of contents lives in [`src/SUMMARY.md`](src/SUMMARY.md).

## Source material

Chapters synthesize the author's existing notes on [hanfengzhai.github.io](https://hanfengzhai.github.io/note.html) and related repositories. Canonical markdown lives in [`writings/`](./writings/) — nine standalone mdBooks (Linear Algebra through DFT) in the **Functional Analysis Notes** style. Sync into the main book with `./scripts/sync-writings.sh`.

## Build

```bash
# Install mdBook: https://github.com/rust-lang/mdBook/releases
mdbook build                  # main book → book/
mdbook serve                  # http://localhost:3000
./scripts/sync-writings.sh    # copy writings/ chapters into src/
./scripts/build-all-writings.sh  # build all nine standalone note mdBooks
```

## License

Notes-derived content © Hanfeng Zhai. See individual source PDFs for disclaimers.
