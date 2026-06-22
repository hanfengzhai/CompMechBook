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

The prologue introduces a drawn copper wire under tension. That same specimen reappears in every part — not as a gimmick, but as a check that each mathematical layer answers a physical question. Use the table below as a reading map: when a chapter feels abstract, ask what it would tell you about this wire.

| Part | What the wire becomes | Question answered |
|------|----------------------|-------------------|
| Prologue | A ladder of scales on one specimen | Why do we need so many models for one material? |
| I | A chain of springs; a vibration eigenproblem | How does every simulation reduce to linear algebra? |
| II | A displacement field \(u(x)\), not a finite vector | Why do infinite-dimensional spaces appear before we mesh? |
| III | A bar in equilibrium; a weak form | What is the continuous problem FEM will approximate? |
| IV | A meshed bar; assembled \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | How does Galerkin turn a PDE into sparse algebra? |
| V | Coolant flow around the wire (if heated) | How do conservation laws discretize on cells instead of elements? |
| VI | Cauchy stress, Hooke's law, virtual work | What continuum physics do FEM and FVM actually approximate? |
| VII | A work-hardened forest of dislocations | Why does the stress–strain curve bend upward after yield? |
| VIII | A lattice of copper atoms vibrating in a potential | Where do moduli and mobilities in coarser models come from? |
| IX | Valence electrons binding the crystal | Where does cohesive energy — the baseline for every defect — originate? |
| Epilogue | The full wire in a multiscale workflow | How do DFT, MD, DDD, and FEM compose in practice? |

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

## Bridge

The organization is linear, but the story is not a syllabus — it is one material seen through many lenses. Turn to the prologue and meet the copper wire at every scale at once. From there, each part adds a layer of language until the full ladder from electrons to structures is something you can climb deliberately, not memorize piecemeal.
