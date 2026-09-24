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

## Reading map (continuous book)

| When the plot stutters | Open |
|------------------------|------|
| Part IX feels like three disconnected QM lectures | [Bridge reunion — Part IX (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-ix) |
| SCF theory exists without `cu.foundation/` archive | [Kohn–Sham → DFT workflows reunion](../appendix/chapters/sources.md#kohn-sham-dft-workflows-reunion-index-row-39) |
| Row 23 — transitions feel mechanical | [Bridge reunion index](../appendix/chapters/sources.md#bridge-reunion-index-row-23) · [intra-part descent VI–IX](../appendix/chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
