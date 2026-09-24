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
| Pedigree checklist filled but IX.0 feels disconnected from VIII.3 | [Coarse-graining → electronic audit reunion (row 36)](../appendix/chapters/sources.md#coarse-graining-electronic-audit-reunion-index-row-36) · [VIII.3 Bridge to Part IX](../md/chapters/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) · [IX.0 opening hinge](chapters/00-opening.md#opening-hinge-viii3-to-ix) · [thermal phonon audit at \(T_w\)](chapters/00-opening.md#thermal-phonon-audit-at-tw) |
| `cu.relax.out` exists but IX.1 feels like standalone quantum chemistry | [Electronic audit → Born–Oppenheimer reunion (row 37)](../appendix/chapters/sources.md#electronic-audit-born-oppenheimer-reunion-index-row-37) · [IX.0 Bridge](chapters/00-opening.md#bridge) · [IX.1 opening hinge](chapters/01-born-oppenheimer.md#opening-hinge-ix0-to-ix1) · [Murnaghan Lab act](chapters/01-born-oppenheimer.md#lab-act-murnaghan-fit-on-fcc-cu-act-vi--foundation) |
| Murnaghan \(a_0\) exists but IX.2 SCF feels like standalone quantum chemistry | [Born–Oppenheimer → Kohn–Sham reunion (row 38)](../appendix/chapters/sources.md#born-oppenheimer-kohn-sham-reunion-index-row-38) · [IX.1 Bridge](chapters/01-born-oppenheimer.md#bridge) · [IX.2 opening hinge](chapters/02-kohn-sham.md#opening-hinge-ix1-to-ix2) · [cutoff-sweep Lab act](chapters/02-kohn-sham.md#lab-act-cutoff-sweep-on-fcc-cu-act-vi--convergence-certificate) |
| SCF converges but `cu.foundation/` archive is missing | [Kohn–Sham → DFT workflows reunion (row 39)](../appendix/chapters/sources.md#kohn-sham-dft-workflows-reunion-index-row-39) · [IX.2 Bridge](chapters/02-kohn-sham.md#bridge) · [IX.3 opening hinge](chapters/03-dft-workflows.md#opening-hinge-ix2-to-ix3) |
| Row 23 — transitions feel mechanical | [Bridge reunion index](../appendix/chapters/sources.md#bridge-reunion-index-row-23) · [intra-part descent VI–IX](../appendix/chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
| `foundation_export.yaml` without SCF or \(\alpha(T_w)\) pedigree | [Scale-boundary reunion (row 28)](../appendix/chapters/sources.md#scale-boundary-reunion-index-row-28) · [IX.3 foundation checklist](chapters/03-dft-workflows.md#ix3-foundation-checklist) |
