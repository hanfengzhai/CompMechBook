# Finite Volume Method — source stub

Canonical markdown for **Part V — Conservation on Cells** will live here when synced from `Writings.git`.

## Current mapping

| Source | Book chapter |
|--------|----------------|
| [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf) (SHU HW #2) | `src/part05-fvm/01-conservation-integral.md` through `03-fluxes-riemann.md` |
| [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf) | `src/part05-fvm/04-navier-stokes-cfd.md` |

## Topics covered in FVM.pdf

- Euler system in conservation form \(\partial_t U + \partial_x F(U) = 0\)
- Cell-average definition and flux differencing
- Eigenstructure \(J = S^{-1}\Lambda S\) with \(\lambda \in \{u-c, u, u+c\}\)
- Shock tube Problems I and II (verification cases)
- Illustris–TNG / Arepo second-order FVM on moving Voronoi meshes

Run `./scripts/sync-writings.sh` after adding markdown here to refresh Part II; Part V sync will follow the same pattern once source files are committed to Writings.
