# Density Functional Theory Notes

Canonical markdown for **Part IX — Electronic Structure**, aligned with [MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW) coursework and Martin, *Electronic Structure*.

## Layout (Functional Analysis Notes style)

```
dft/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-born-oppenheimer.md
│   ├── 02-kohn-sham.md
│   └── 03-dft-workflows.md
```

Chapter numbering `00`–`03` matches `src/part09-dft/` in CompMechBook. Bridge sections connect atomistic potentials to Born–Oppenheimer separation and the Kohn–Sham equations; Chapter 02 hands off to reproducible QE workflows; Chapter 03 hands off to the epilogue on multiscale coupling.

## DFT & electronic structure reading map (template for Part IX)

| Chapter | MSE 5720 / Martin object | Wire beat | Hands off to |
|---------|--------------------------|-----------|--------------|
| 00 Opening | Concept map; electronic audit hinge | EAM hides \(\rho(\mathbf{r})\); phonon audit at \(T_w\) | 01 |
| 01 Born–Oppenheimer | BO separation, Hohenberg–Kohn | Fast electrons justify classical nuclei in VIII | 02 |
| 02 Kohn–Sham | SCF, XC, k-points, convergence | Unit-cell stress tensor before export | 03 |
| 03 DFT workflows | QE decks, Murnaghan, slabs, quasiharmonic \(\alpha(T)\) | Foundation folder with SCF pedigree | [Epilogue](../epilogue/chapters/multiscale.md) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part IX closes the descent before the epilogue reunites every handshake.

## Build standalone

```bash
cd writings/dft && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
