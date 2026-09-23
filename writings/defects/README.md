# Defects & Dislocations Notes

Canonical markdown for **Part VII — Defects and Dislocations**, aligned with [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf) and [OpenDiS](https://github.com/OpenDiS/OpenDiS).

## Layout (Functional Analysis Notes style)

```
defects/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-defect-taxonomy.md
│   ├── 02-dislocation-dynamics.md
│   └── 03-polycrystal-and-fem-handoff.md
```

Chapter numbering `00`–`03` matches `src/part07-defects/` in CompMechBook. Bridge sections connect continuum elasticity to mesoscale plasticity; Chapter 03 hands off to Part VIII (molecular dynamics).

## Defects & DDD reading map (template for Part VII)

| Chapter | Defects Notes object | Wire beat | Hands off to |
|---------|----------------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure; descent begins | VI.4 knee was fitted \(H\); slip lines appear at yield | 01 |
| 01 Defect taxonomy | Point, line, surface defects; Burgers vector \(\mathbf{b}\) | Cold-drawn forest before the test; \(T_w\) from CHT softens glide | 02 |
| 02 Dislocation dynamics | Peach–Köhler, mobility, Taylor hardening, OpenDiS | Lines multiply under FEM stress; GSF ribbon links to DFT | 03 |
| 03 Polycrystal & FEM handoff | RVE homogenization, crystal plasticity, DAMASK | OpenDiS \(\rho(\gamma)\) exports replace phenomenological \(H\) | [Part VIII](../md/chapters/00-opening.md) |

See the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent) for where Part VII begins the descent after Part VI closes the ascent.

**Intra-part Bridge reunion (row 23).** When VII.1–VII.3 feel like separate courses despite correct Scene prose, use the [Part VII intra-part bridge table](../appendix/chapters/sources.md#bridge-reunion-intra-part-vii) — read the prior chapter's Bridge one-liner, then the next chapter's opening hinge (`#opening-hinge-vii0-to-vii1`, `#opening-hinge-vii1-to-vii2`, `#opening-hinge-vii2-to-vii3`).

## Build standalone

```bash
cd writings/defects && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
