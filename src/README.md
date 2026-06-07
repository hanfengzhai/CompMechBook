# From Vectors to Atoms

*A continuous journey through the mathematics and methods of computational mechanics*

---

Imagine holding a copper wire in your hand. Pull it gently: it stretches, then yields, then hardens. That everyday response is the end of a long chain of physics—continuum elasticity, crystal plasticity, dislocation motion, atomic bonding—each layer governed by its own equations, yet all describing the *same* material. Computational mechanics is the art of choosing the right layer, the right approximation, and the right algorithm to answer a question without drowning in detail.

This book tells that story in order. We begin where every simulation ultimately lands: **linear algebra**, the language of matrices and vectors that computers speak fluently. We then climb into **functional analysis**, where solutions to partial differential equations live in infinite-dimensional spaces—and where the *weak form* of a boundary-value problem first becomes precise. From there we meet the two workhorses of continuum computation, the **finite element method** and the **finite volume method**, before descending in scale to **dislocation dynamics**, **molecular dynamics**, and **density functional theory**.

The narrative is intentional. Each chapter closes a gap that the next chapter needs. Vector spaces prepare normed spaces; normed spaces prepare Hilbert spaces; Hilbert spaces prepare Galerkin's method; Galerkin's method prepares finite elements; finite elements on crystals motivate discrete defects; discrete defects motivate atomistic potentials; atomistic potentials motivate electronic structure. By the end, you should see multiscale modeling not as a bag of unrelated codes, but as one plotline with well-marked scene changes.

## How this book is organized

The structure follows the *Functional Analysis Notes* style: each part opens with a chapter overview, then numbered sections develop definitions, examples, and theorems in sequence. Where possible, material is drawn from the author's existing **Writings**—course notes, teaching handouts, and research summaries hosted at [hanfengzhai.github.io/note](https://hanfengzhai.github.io/note.html)—and rewritten into a single voice.

| Part | Title | Central question |
|------|-------|------------------|
| 0 | Prologue | Why do we need so many scales? |
| I | Linear Algebra | How do we represent and solve discrete problems? |
| II | Functional Analysis | Where do PDE solutions live, and what is a weak form? |
| III | Partial Differential Equations | What equations govern continua? |
| IV | Finite Element Method | How do we discretize a weak form on meshes? |
| V | Finite Volume Method | How do we conserve fluxes on control volumes? |
| VI | Defects & Continuum Plasticity | How do microstructure and defects enter macro laws? |
| VII | Dislocation Dynamics | How do line defects move and multiply? |
| VIII | Molecular Dynamics | How do atoms move under empirical or learned potentials? |
| IX | Density Functional Theory | How do electrons determine the bonding? |
| X | Epilogue | How do we bridge scales in practice? |

## Source writings

This edition synthesizes personal notes including:

- *Linear Algebra* (ME300A, Stanford)
- *Finite Element Analysis* course summary and problem sessions (ME335A, Stanford)
- *Computational Fluid Dynamics* and *Finite Volume Method* (Shanghai University)
- *Atomistic Modeling*, *Defects & Disorders*, *Elasticity & Inelasticity*
- Research summaries on dislocation link statistics (DDD, ParaDiS)

Original PDFs remain at [hanfengzhai.github.io](https://hanfengzhai.github.io/note.html). This repository is the unified, narrative edition.

## Build

Install [mdBook](https://github.com/rust-lang/mdBook) and optionally [mdbook-katex](https://github.com/lzanini/mdbook-katex) for faster math rendering:

```bash
mdbook build
mdbook serve   # live preview at http://localhost:3000
```

## Contributing

Corrections and additions are welcome via pull request. When extending a chapter, keep the narrative bridge to the next part explicit—readers should always know *why* the next idea appears.
