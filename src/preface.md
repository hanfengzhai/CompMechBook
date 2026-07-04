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

The same specimen — a cold-drawn copper wire under tension, heated by current, cooled by air — reappears in every part. The table below is a reading map: what changes is the **state variable**, not the material.

| Part | What the wire becomes | What we learn to compute |
|------|----------------------|--------------------------|
| Prologue | A ladder of scales | State, equations, discretization, upward exports |
| I | Coupled springs / modes | \(\mathbf{K}\mathbf{u}=\mathbf{f}\), eigenmodes |
| II | Fields in \(H^1\) and \(L^2\) | Norms, operators, Galerkin convergence |
| III | PDEs with weak forms | Strong vs. weak, Sobolev regularity, energy |
| IV | Meshed solid | Galerkin assembly, elements, convergence |
| V | Fluid around the wire | FVM fluxes, Navier–Stokes, conjugate heat transfer |
| VI | Cauchy stress and strain | Kinematics, balance, variational elasticity |
| VII | Dislocation forest | DDD, Taylor hardening, crystal plasticity handoff |
| VIII | Atomic lattice | Potentials, ensembles, LAMMPS workflows |
| IX | Valence electrons | Kohn–Sham, QE inputs, elastic constants upward |
| Epilogue | All scales coupled | Sequential, concurrent, and learned multiscale workflows |

Each numbered chapter ends with a **Bridge** section that states explicitly why the next chapter exists. If you ever feel a jump in abstraction, read the Bridge at the end of the prior chapter first — it is the narrative hinge. For a one-line role of every chapter in reading order, see the [chapter roadmap](appendix/sources.md) in the appendix (also listed as **Sources and Further Reading** in the table of contents).

The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) (ME 412) supply the template for that hinge: not a proof document, but a **concept map** where every idea answers four questions — what object we study, what structure it adds, what theorem that structure enables, and what breaks if the structure is missing. Part II adopts that map explicitly; later parts reuse the same instinct at every scale change.

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

## Bridge

The preface is the table of contents in prose. The **prologue** is the first scene: one copper wire, many scales, and the four questions — state, equations, discretization, upward export — that every chapter will answer in its own language. Read it before Part I if you want the plot before the grammar; read it after Part VI if you prefer to meet the wire first as a meshed solid and then learn why the mesh had to exist.

Turn the page when ready. The ladder begins with a specimen under tension and a question that will not go away: *what is the minimal description at this scale, and what do we pass to the scale above?*

---

*Hanfeng Zhai, 2026*
