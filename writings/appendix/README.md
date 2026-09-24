# Appendix Notes

Canonical markdown for **Appendices** in CompMechBook, following the Functional Analysis Notes layout.

## Layout

```
appendix/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── glossary.md
│   ├── sources.md
│   └── memory-sheet.md
```

## Build standalone

```bash
cd writings/appendix && mdbook build
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
| Chapters feel choppy despite Bridges | [Continuous read-through guide](chapters/sources.md#continuous-read-through-guide) · [continuity hinges master map](chapters/memory-sheet.md#continuity-hinges-master-map) |
| Part boundaries feel like a new syllabus | [Story so far reunion (row 26)](chapters/sources.md#story-so-far-reunion-index-row-26) then [Closing the arc reunion (row 27)](chapters/sources.md#closing-the-arc-reunion-index-row-27) |
| Prior-part symbols do not translate | [Closing the arc reunion index](chapters/sources.md#closing-the-arc-reunion-index-row-27) |
| Cannot place the wire in the narrative arc | [Story so far reunion index](chapters/sources.md#story-so-far-reunion-index-row-26) |
| Transitions feel mechanical | [Bridge reunion index](chapters/sources.md#bridge-reunion-index-row-23) · [intra-part ascent I–V](chapters/sources.md#bridge-reunion-intra-part-ascent-i-v) · [intra-part descent VI–IX](chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
| Parameters crossing scales feel arbitrary | [Scale-boundary reunion (row 28)](chapters/sources.md#scale-boundary-reunion-index-row-28) · [parameter pedigree path](chapters/sources.md#parameter-pedigree-path-act-vi-reading-order) |
| Act II heating and Act III pulling feel like separate FEM homework | [Thermoelastic assembly reunion (row 29)](chapters/sources.md#thermoelastic-assembly-reunion-index-row-29) · [Part IV thermoelastic thread](../../src/part04-fem/00-opening.md#acts-ii-and-iii-together-thermoelastic-assembly-thread) |
| Solid FEM and fluid FVM feel like separate solvers | [CHT outer-loop reunion (row 30)](chapters/sources.md#cht-outer-loop-reunion-index-row-30) · [V.4 Picard + parser](../../src/part05-fvm/04-navier-stokes-cfd.md#parser-checkpoint-archive-cht-export-yaml) |
| Galerkin \(\mathbf{K}\mathbf{U}=\mathbf{F}\) and continuum virtual work feel disconnected | [Twin-ladder → virtual work reunion (row 31)](chapters/sources.md#twin-ladder-virtual-work-reunion-index-row-31) · [VI.3 virtual work Lab act](../../src/part06-continuum/03-variational-elasticity.md#lab-act-virtual-work-equals-load-cell-reading-act-iii--pulling) |
| Virtual work and return-mapping at the yield knee feel disconnected | [Virtual work → plasticity preview reunion (row 32)](chapters/sources.md#virtual-work-plasticity-preview-reunion-index-row-32) · [VI.4 return-mapping Lab act](../../src/part06-continuum/04-nonlinear-plasticity-preview.md#lab-act-return-mapping-on-the-load-cell-knee-act-iv-hardening) |
| Mesoscale DDD and atomistic MD feel like separate courses | [Part VII → VIII descent hinge reunion (row 33)](chapters/sources.md#part-vii-viii-descent-hinge-reunion-index-row-33) · [VII.2 mobility Lab act at \(T_w\)](../../src/part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) · [Part VIII descent hinge](../../src/part08-md/00-opening.md#descent-hinge-cores-mobility-and-tw-pedigree) |
| 0 K EAM minimization and NVT/NPT trajectories feel like separate subjects | [Potentials → ensembles reunion (row 34)](chapters/sources.md#potentials-ensembles-reunion-index-row-34) · [VIII.1 EAM Lab act](../../src/part08-md/01-potentials-phase-space.md#lab-act-eam-lattice-constant-from-energy-minimization-act-v--notch-prelude) · [VIII.2 opening hinge](../../src/part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2) |
| Audited NVT/NPT trajectories and yaml handoff tables feel like separate subjects | [Ensembles → coarse-graining reunion (row 35)](chapters/sources.md#ensembles-coarse-graining-reunion-index-row-35) · [VIII.2 NPT Lab act](../../src/part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) · [VIII.3 opening hinge](../../src/part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3) |
| Pedigree checklist filled but Part IX feels like standalone DFT | [Coarse-graining → electronic audit reunion (row 36)](chapters/sources.md#coarse-graining-electronic-audit-reunion-index-row-36) · [VIII.3 Bridge to Part IX](../../src/part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) · [IX.0 opening hinge](../../src/part09-dft/00-opening.md#opening-hinge-viii3-to-ix) |
| SCF logs exist but Born–Oppenheimer / Hohenberg–Kohn feel like standalone QM | [Electronic audit → Born–Oppenheimer reunion (row 37)](chapters/sources.md#electronic-audit-born-oppenheimer-reunion-index-row-37) · [IX.0 Bridge](../../src/part09-dft/00-opening.md#bridge) · [IX.1 opening hinge](../../src/part09-dft/01-born-oppenheimer.md#opening-hinge-ix0-to-ix1) |
| BO/HK theorems understood but Kohn–Sham SCF feels like standalone QM | [Born–Oppenheimer → Kohn–Sham reunion (row 38)](chapters/sources.md#born-oppenheimer-kohn-sham-reunion-index-row-38) · [IX.1 Bridge](../../src/part09-dft/01-born-oppenheimer.md#bridge) · [IX.2 opening hinge](../../src/part09-dft/02-kohn-sham.md#opening-hinge-ix1-to-ix2) |
| SCF converges but `cu.foundation/` archive is missing | [Kohn–Sham → DFT workflows reunion (row 39)](chapters/sources.md#kohn-sham-dft-workflows-reunion-index-row-39) · [IX.2 Bridge](../../src/part09-dft/02-kohn-sham.md#bridge) · [IX.3 opening hinge](../../src/part09-dft/03-dft-workflows.md#opening-hinge-ix2-to-ix3) |
| `cu.foundation/` complete but handbook \(\alpha\) persists at load cell | [IX.3 → Handshake 3 reunion (row 40)](chapters/sources.md#ix3-handshake3-reunion-index-row-40) · [IX.3 opening hinge to Handshake 3](../../src/part09-dft/03-dft-workflows.md#opening-hinge-ix3-to-handshake3) · [epilogue Handshake 3 opening hinge](../../src/epilogue/multiscale.md#opening-hinge-ix3-handshake3) |
| Need upstream PDFs and ME 412 maps | [Writings source index](../SUMMARY.md) · [Functional Analysis template](../functional-analysis/README.md) |

Book appendices in the unified mdBook: [`src/appendix/`](../../src/appendix/).
