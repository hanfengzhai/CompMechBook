# Preface

This book grew out of a simple observation: computational mechanics is not a collection of unrelated numerical recipes. It is a single narrative about how we represent physical reality at different scales, and how the mathematical tools at each scale connect to the next.

When we write a finite element code, we solve a linear system assembled from local contributions — linear algebra in disguise. When we prove that a Galerkin approximation converges, we invoke completeness and compactness — functional analysis in disguise. When we coarse-grain a molecular dynamics trajectory or feed a DFT energy landscape into a continuum model, we are asking the same question in a different language: *what information survives when we change scale?*

The chapters that follow are written to be read in order, like a novel with a plot. A copper wire under tension, a turbulent jet, a dislocation network in a crystal, and the electrons that bind the atoms together are not separate homework problems. They are scenes in one story. The mathematics is the thread that stitches them together.

## How this book is organized

The structure follows the arc of the author's personal notes — linear algebra and functional analysis as foundations, partial differential equations and weak forms as the bridge to discretization, finite elements and finite volumes as the two great discretization philosophies for solids and fluids, and atomistic and electronic methods as the descent to finer scales. Each part ends with a short bridge section that explains why the next scale is necessary.

```mermaid
flowchart TB
  subgraph foundations["Foundations"]
    I[Part I: Linear algebra]
    II[Part II: Functional analysis]
    III[Part III: PDEs and weak forms]
  end
  subgraph discretize["Discretization"]
    IV[Part IV: Finite elements]
    V[Part V: Finite volumes and CFD]
  end
  subgraph physics["Continuum physics"]
    VI[Part VI: Continuum mechanics]
  end
  subgraph finer["Finer scales"]
    VII[Part VII: Defects and DDD]
    VIII[Part VIII: Molecular dynamics]
    IX[Part IX: DFT]
  end
  I --> II --> III --> IV
  III --> V
  IV --> VI
  V --> VI
  VI --> VII --> VIII --> IX
  IX --> E[Epilogue: Multiscale coupling]
```

Read straight through from the prologue to the epilogue. Parts IV and V can be swapped if you already know FEM and want CFD first; Part VI then unifies the stress–balance language both discretizations approximate. Parts VII–IX are best read after the continuum vocabulary of Part VI, because dislocation, atomistic, and electronic models explain where continuum parameters originate.

## The copper wire through the book

The prologue introduces a copper wire under tension as the recurring physical thread. Each part revisits the same object at the scale that part owns — not as a repeated example, but as the next scene in one story. The table below is a reading map; every numbered chapter ends with a **Bridge** section that hands off explicitly to the next scene.

| Part | What the wire becomes | Question answered |
|------|------------------------|-------------------|
| Prologue | Specimen pulled in tension | Why do we need a ladder of models at all? |
| I | Nodal displacements and \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | What is the grammar every discretization eventually speaks? |
| II | Fields in \(H^1\) and \(L^2\), not fixed \(\mathbb{R}^N\) | Why do weak forms and convergence theorems exist? |
| III | Poisson/heat/elasticity weak forms on the domain | What PDEs govern the wire before we mesh it? |
| IV | Tetrahedral mesh, Galerkin assembly, stress recovery | How do we compute the wire on a computer (solids)? |
| V | Control volumes, fluxes, thermal convection in air | How do we treat conservation laws and fluids on the same wire? |
| VI | Cauchy stress, virtual work, nonlinear elasticity preview | What continuum physics do FEM and FVM approximate? |
| VII | Dislocation forest from cold drawing, DDD hardening | Why does the stress–strain curve bend upward? |
| VIII | Cu lattice, EAM potential, MD moduli and vacancies | Where do elastic constants and defect energies come from? |
| IX | Valence electrons, cohesive energy, DFT elastic tensor | What binds the crystal before any spring constant is assumed? |
| Epilogue | Full multiscale workflow back to the structural member | How do teams couple the rungs in practice? |

If a chapter feels abstract, return to this table and ask which row you are in. The mathematics changes; the wire does not.

## Source material

The prose synthesizes course notes, teaching materials, and research experience collected over several years. Primary written sources include:

- [Linear Algebra notes](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) (ME 300A)
- [Functional Analysis notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) (ME 412) — layout model for Part II and all `writings/` subtrees
- [Partial Differential Equations notes](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) (ME 300B)
- [Finite Element Analysis notes](https://hanfengzhai.github.io/file/FEA_notes.pdf) and [problem sessions](https://hanfengzhai.github.io/note.html)
- [Elasticity & Inelasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf)
- [Computational Fluid Dynamics notes](https://hanfengzhai.github.io/file/CFD_note.pdf) and [Finite Volume Method notes](https://hanfengzhai.github.io/note/FVM.pdf)
- [Defects & Disorders notes](https://hanfengzhai.github.io/file/defects_notes.pdf)
- [Atomistic Modeling notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf)
- [DFT coursework](https://github.com/hanfengzhai/MSE5720-HW) (MSE 5720)

Canonical source markdown lives under [`writings/`](../writings/) in the **Functional Analysis Notes** layout: one mdBook per part, numbered chapters, and **Bridge** sections at the end of each chapter. Run [`scripts/sync-writings.sh`](../scripts/sync-writings.sh) to refresh `src/` from those sources. When the external `Writings` git submodule is linked, merge upstream changes there and re-run the sync script.

## Disclaimer

These notes represent the author's understanding of the material and are intended for study and reference. They may contain errors. Feedback is welcome at [hzhai@stanford.edu](mailto:hzhai@stanford.edu).

---

*Hanfeng Zhai, 2026*
