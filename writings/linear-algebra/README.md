# Linear Algebra Notes

Canonical markdown for **Part I — The Grammar of Computation**, aligned with [ME300A_LinAlg.pdf](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf).

## Layout (Functional Analysis Notes style)

```
linear-algebra/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-vectors-matrices.md
│   ├── 02-linear-maps.md
│   ├── 03-eigenvalues.md
│   └── 04-toward-infinity.md
```

Chapter numbering `00`–`04` matches `src/part01-linear-algebra/` in CompMechBook. Each chapter ends with a **Bridge** section that connects the narrative to the next topic; Chapter 04 introduces function spaces and motivates Part II.

## Build standalone

```bash
cd writings/linear-algebra && mdbook build
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
| Part I feels like four separate lectures | [Bridge reunion — Part I (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-i) |
| Row 23 — transitions feel mechanical | [Bridge reunion index](../appendix/chapters/sources.md#bridge-reunion-index-row-23) · [intra-part ascent I–V](../appendix/chapters/sources.md#bridge-reunion-intra-part-ascent-i-v) |
| Mid-chapter abstraction | [Numbered-chapter plot spine index](../appendix/chapters/sources.md#numbered-chapter-plot-spine-index-row-19) |

Upstream: [ME300A_LinAlg.pdf](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf). Book part: [Part I in `src/part01-linear-algebra/`](../../src/part01-linear-algebra/).
