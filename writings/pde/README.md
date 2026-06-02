# Partial Differential Equations Notes

Canonical markdown for **Part III — Fields on Domains**, aligned with [ME300B_PDE.pdf](https://hanfengzhai.github.io/file/ME300B_PDE.pdf).

## Layout (Functional Analysis Notes style)

```
pde/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 01-strong-form.md
│   ├── 02-weak-form.md
│   ├── 03-sobolev-spaces.md
│   └── 04-energy-methods.md
```

Chapter numbering `01`–`04` matches `src/part03-pdes/`. Bridge sections connect Part II function spaces to Part IV discretization.

## Build standalone

```bash
cd writings/pde && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
