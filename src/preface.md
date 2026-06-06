# Preface

This book grew out of a simple observation: computational mechanics is not a collection of unrelated numerical recipes. It is a single narrative about how we represent physical reality at different scales, and how the mathematical tools at each scale connect to the next.

When we write a finite element code, we solve a linear system assembled from local contributions — linear algebra in disguise. When we prove that a Galerkin approximation converges, we invoke completeness and compactness — functional analysis in disguise. When we coarse-grain a molecular dynamics trajectory or feed a DFT energy landscape into a continuum model, we are asking the same question in a different language: *what information survives when we change scale?*

The chapters that follow are written to be read in order, like a novel with a plot. A copper wire under tension, a turbulent jet, a dislocation network in a crystal, and the electrons that bind the atoms together are not separate homework problems. They are scenes in one story. The mathematics is the thread that stitches them together.

## How this book is organized

The structure follows the arc of the author's personal notes — linear algebra and functional analysis as foundations, partial differential equations and weak forms as the bridge to discretization, finite elements and finite volumes as the two great discretization philosophies for solids and fluids, and atomistic and electronic methods as the descent to finer scales. Each chapter ends with a **Bridge** section that explains why the next topic is necessary, so the book reads as one continuous narrative rather than a shelf of separate courses.

## Reading the story

A copper wire under tension opens the prologue and reappears in every part. The plot is not a gimmick; it is the organizing question of multiscale mechanics: *at this scale, what is the state, what equations govern it, and what do we export upward?*

| Part | What happens in the story |
|------|---------------------------|
| **I** | The wire becomes a vector of nodal displacements and a stiffness matrix — the grammar every later method speaks. |
| **II** | Those vectors become functions; we learn the spaces where weak forms and convergence theorems live. |
| **III** | PDEs and weak forms translate physics into variational statements the computer can approximate. |
| **IV** | Galerkin finite elements assemble the wire's elasticity problem element by element. |
| **V** | Finite volumes balance fluxes when the wire heats in cross-flow air — conservation on cells, not trial functions. |
| **VI** | Continuum kinematics and stress give physical meaning to the fields Parts III–V discretized. |
| **VII** | Dislocations explain why the drawn wire work-hardens — mesoscale lines where elasticity fails. |
| **VIII** | Atoms and potentials resolve cores, fracture, and thermal motion below the continuum. |
| **IX** | Electrons and DFT supply cohesive energy and elastic constants that every coarser model inherits. |
| **Epilogue** | Sequential and concurrent coupling stitch the rungs into workflows no single code runs alone. |

Read straight through for the full arc. Jump to a part when you need a specific tool — the bridges and the prologue keep the ladder coherent.

## Source material

The prose synthesizes course notes, teaching materials, and research experience collected over several years. Primary written sources include:

- [Linear Algebra notes](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) (ME 300A)
- [Partial Differential Equations notes](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) (ME 300B)
- [Finite Element Analysis notes](https://hanfengzhai.github.io/file/FEA_notes.pdf) and [problem sessions](https://hanfengzhai.github.io/note.html)
- [Elasticity & Inelasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf)
- [Computational Fluid Dynamics notes](https://hanfengzhai.github.io/file/CFD_note.pdf) and [Finite Volume Method notes](https://hanfengzhai.github.io/note/FVM.pdf)
- [Defects & Disorders notes](https://hanfengzhai.github.io/file/defects_notes.pdf)
- [Atomistic Modeling notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf)
- [DFT coursework](https://github.com/hanfengzhai/MSE5720-HW) (MSE 5720)

Canonical chapter sources live under [`writings/`](../writings/) in the **Functional Analysis Notes** layout: each part is a standalone mdBook (`book.toml`, numbered chapters, MathJax, **Bridge** sections). Run `./scripts/sync-writings.sh` to copy them into `src/`. When the external `Writings` git submodule is linked, that directory becomes the upstream; the sync workflow stays the same.

## Disclaimer

These notes represent the author's understanding of the material and are intended for study and reference. They may contain errors. Feedback is welcome at [hzhai@stanford.edu](mailto:hzhai@stanford.edu).

---

*Hanfeng Zhai, 2026*
