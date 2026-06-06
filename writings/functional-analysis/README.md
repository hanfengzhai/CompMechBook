# Functional Analysis Notes

Canonical markdown for **Part II — Function Spaces**, the template layout for all Writings subtrees and the mathematical foundation for weak forms, Galerkin FEM, and convergence analysis in CompMechBook.

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

Chapter numbering `01`–`05` matches `src/part02-functional-analysis/` in CompMechBook. Each chapter ends with a **Bridge** section that connects the narrative to the next topic — from function spaces to PDE weak forms in Part III.

## Build standalone

```bash
cd writings/functional-analysis && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
