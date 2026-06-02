# Functional Analysis Notes

Canonical markdown for **Part II — Function Spaces**, aligned with the author's graduate coursework and the weak-form / Galerkin thread in CompMechBook.

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

Chapter numbering `01`–`05` matches `src/part02-functional-analysis/` in CompMechBook. Each chapter ends with a **Bridge** section that ties the mathematics back to the copper-wire narrative and points to the next chapter or part.

## Build standalone

```bash
cd writings/functional-analysis && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
