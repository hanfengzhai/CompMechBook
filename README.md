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

Chapters synthesize the author's existing notes on [hanfengzhai.github.io](https://hanfengzhai.github.io/note.html) and related repositories.

**Writings integration:** Part II follows the [Functional Analysis Notes](./writings/functional-analysis/) layout (`chapters/01`–`05`). Sync from source to the main book:

```bash
./scripts/sync-writings.sh
```

When `Writings.git` is linked as a submodule at `writings/`, run the same script after `git submodule update --init`.

## Build

```bash
# Install mdBook: https://github.com/rust-lang/mdBook/releases
mdbook build        # output in book/
mdbook serve        # http://localhost:3000
```

## License

Notes-derived content © Hanfeng Zhai. See individual source PDFs for disclaimers.
