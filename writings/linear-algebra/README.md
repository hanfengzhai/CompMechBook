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

Chapter numbering `01`–`04` matches `src/part01-linear-algebra/` in CompMechBook. Bridge sections at the end of each chapter connect the narrative to the next topic; Chapter 04 introduces function spaces and motivates Part II.

## Build standalone

```bash
cd writings/linear-algebra && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
