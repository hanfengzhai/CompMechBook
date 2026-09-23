# Partial Differential Equations Notes

Canonical markdown for **Part III — Fields on Domains**, aligned with [ME300B_PDE.pdf](https://hanfengzhai.github.io/file/ME300B_PDE.pdf).

## Layout (Functional Analysis Notes style)

```
pde/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-strong-form.md
│   ├── 02-weak-form.md
│   ├── 03-sobolev-spaces.md
│   └── 04-energy-methods.md
```

Chapter numbering `00`–`04` matches `src/part03-pdes/` in CompMechBook. Bridge sections connect Part II function spaces to Part IV discretization; Chapter 04 hands off to the finite element method.

When III.1–III.4 feel like a PDE catalog, use [Bridge reunion intra-part III](chapters/00-opening.md#bridge-reunion-intra-part-iii) — [appendix ascent index](../appendix/chapters/sources.md#bridge-reunion-intra-part-ascent-i-v).

## Build standalone

```bash
cd writings/pde && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
