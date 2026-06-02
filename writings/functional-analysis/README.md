# Functional Analysis Notes

Canonical markdown for **Part II — Function Spaces**, aligned with the author's functional-analysis lecture notes and the weak-form theory used in ME 300B / FEA coursework.

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

Chapter numbering `01`–`05` matches `src/part02-functional-analysis/` in CompMechBook. Bridge sections at the end of each chapter connect the narrative to PDEs (Part III) and the Galerkin theory of FEM (Part IV). Chapter 01 opens with the copper-wire thread from the CompMechBook prologue.

## Build standalone

```bash
cd writings/functional-analysis && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
