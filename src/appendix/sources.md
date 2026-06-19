# Sources and Further Reading

This book synthesizes material from the author's notes, coursework, and teaching. Canonical chapter sources live under [`writings/`](../writings/) (Functional Analysis Notes layout). Run `./scripts/sync-writings.sh` to copy them into `src/`. When the external `Writings` git submodule is linked, prefer upstream content and re-run the sync script.

## Primary notes (hanfengzhai.github.io)

| Topic | Link |
|-------|------|
| Linear Algebra (ME 300A) | [ME300A_LinAlg.pdf](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) |
| Functional Analysis | [FunctionalAnalysis.pdf](https://hanfengzhai.github.io/file/FunctionalAnalysis.pdf) |
| Partial Differential Equations (ME 300B) | [ME300B_PDE.pdf](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) |
| Finite Element Analysis | [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf) |
| FEA Problem Sessions & Tutorials | [note.html](https://hanfengzhai.github.io/note.html) |
| Elasticity & Inelasticity | [elasticity_notes.pdf](https://hanfengzhai.github.io/file/elasticity_notes.pdf) |
| Nonlinear FEA | [NonlinFEA_note.pdf](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) |
| Computational Fluid Dynamics | [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf) |
| Finite Volume Method | [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) |
| Defects & Disorders | [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf) |
| Atomistic Modeling | [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf) |
| Density Functional Theory | [MSE5720 notebooks](https://hanfengzhai.github.io/note.html) · [MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW) |
| Statistical Mechanics | [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf) |
| Computational Methods (applied mechanics) | [CompMethMechProb.pdf](https://hanfengzhai.github.io/file/CompMethMechProb.pdf) |

## Code and coursework repositories

| Topic | Repository |
|-------|------------|
| DFT (MSE 5720) | [MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW) |
| Dislocation dynamics | [OpenDiS](https://github.com/OpenDiS/OpenDiS) |
| Multiscale graphene fracture | [multiscale-graphene-fracture](https://github.com/hanfengzhai/multiscale-graphene-fracture) |

## Related topics (beyond this book's arc)

The narrative stops at DFT for equilibrium electronic structure, but the author's notes cover adjacent rungs worth climbing after the epilogue:

| Topic | Notes | Connection to the ladder |
|-------|-------|--------------------------|
| Nonlinear FEA | [NonlinFEA_note.pdf](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) | Extends Part IV–VI for finite strain and path-dependent solids |
| Smoothed particle hydrodynamics | [SPH.pdf](https://hanfengzhai.github.io/file/SPH.pdf) | Lagrangian alternative to Part V FVM for free-surface flows |
| Inverse problems & design optimization | [InverseProb.pdf](https://hanfengzhai.github.io/file/InverseProb.pdf), [DesignOpt.pdf](https://hanfengzhai.github.io/file/DesignOpt.pdf) | Uses FEM/MD outputs as forward models for material design |
| Statistical mechanics | [StatMechNotes.pdf](https://hanfengzhai.github.io/file/StatMechNotes.pdf) | Bridges Part VIII ensembles to thermodynamic averages |
| Machine learning for multiscale modeling | [MLMultiscale.pdf](https://hanfengzhai.github.io/file/MLMultiscale.pdf) | Surrogate acceleration discussed in the epilogue |

Dislocation **link statistics** during strain hardening — active vs. inactive slip systems, exponential vs. double-exponential link-length distributions — are developed in [Akhondzadeh, Zhai et al., *J. Mech. Phys. Solids* (2026)](https://doi.org/10.1016/j.jmps.2026.106533) and summarized in Part VII.

## Standard references (external)

**Functional analysis & PDEs**

- Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*
- Evans, *Partial Differential Equations*

**Finite elements**

- Brenner & Scott, *The Mathematical Theory of Finite Element Methods*
- Zienkiewicz & Taylor, *The Finite Element Method*

**Finite volumes & CFD**

- LeVeque, *Finite Volume Methods for Hyperbolic Problems*
- Ferziger, Perić, & Street, *Computational Methods for Fluid Dynamics*

**Continuum mechanics**

- Gurtin, *An Introduction to Continuum Mechanics*
- Holzapfel, *Nonlinear Solid Mechanics*

**Atomistic & electronic structure**

- Tuckerman, *Statistical Mechanics: Theory and Molecular Simulation*
- Martin, *Electronic Structure: Basic Theory and Practical Methods*

## Building this book

```bash
# Install mdBook: https://github.com/rust-lang/mdBook/releases
mdbook build
mdbook serve   # local preview at http://localhost:3000
```

Output appears in `book/`. CI can publish to GitHub Pages on merge to `main`.

## Contributing

When integrating `Writings.git`:

1. Add as a git submodule at `writings/`
2. Map existing note paths to `src/` chapters via symlinks or include macros
3. Preserve the Functional Analysis Notes chapter numbering in Part II
4. Run `mdbook build` to verify cross-links

Pull requests that improve narrative flow, fix errors, or add worked examples are welcome at [CompMechBook](https://github.com/hanfengzhai/CompMechBook).
