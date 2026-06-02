# Functional Analysis Notes

Canonical markdown for **Part II — Function Spaces**, aligned with the author's computational mechanics notes and standard references (Brezis, Evans).

## Layout (Functional Analysis Notes style)

```
functional-analysis/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-motivation.md
│   ├── 02-normed-spaces.md
│   ├── 03-hilbert-spaces.md
│   ├── 04-operators-duality.md
│   └── 05-spectral-theorem.md
```

Chapter numbering `01`–`05` matches `src/part02-functional-analysis/` in CompMechBook. Bridge sections at the end of each chapter connect normed spaces, Hilbert geometry, operators, and spectral theory to weak forms and finite elements in Parts III–IV.

## Build standalone

```bash
cd writings/functional-analysis && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
