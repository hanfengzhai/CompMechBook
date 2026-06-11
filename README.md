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

Chapters synthesize the author's existing notes on [hanfengzhai.github.io](https://hanfengzhai.github.io/note.html) and related repositories. Canonical source markdown lives under [`writings/`](./writings/) in Functional Analysis Notes style (one mdBook per part). Run `./scripts/sync-writings.sh` to refresh `src/` from those sources.

## Scope

Roughly **56,000 words** across **45 sections** (prologue, nine part openings, 36 chapters, epilogue), plus nine standalone Writings mdBooks under `writings/` (~51,000 additional words in canonical source form). Each part opens with a short framing chapter; each numbered chapter ends with a **Bridge** section that hands off to the next topic, following the [Functional Analysis Notes](./writings/functional-analysis/) layout.

## Build

```bash
chmod +x scripts/install-mdbook.sh scripts/sync-writings.sh scripts/build-all-writings.sh
./scripts/install-mdbook.sh   # optional; or use your package manager
./scripts/sync-writings.sh   # refresh src/ from writings/
mdbook build                 # output in book/
mdbook serve                 # http://localhost:3000

# Optional: build each standalone Writings mdBook (Functional Analysis Notes layout)
./scripts/build-all-writings.sh
```

## License

Notes-derived content © Hanfeng Zhai. See individual source PDFs for disclaimers.
