# Functional Analysis Notes

Canonical markdown for **Part II — Function Spaces**, written as the template for all Writings subtrees in this repository.

## Layout

```
functional-analysis/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── 00-opening.md
│   ├── 01-motivation.md
│   ├── 02-normed-spaces.md
│   ├── 03-hilbert-spaces.md
│   ├── 04-operators-duality.md
│   └── 05-spectral-theorem.md
```

Chapter numbering `00`–`05` matches `src/part02-functional-analysis/` in CompMechBook. Each chapter ends with a **Bridge** section that connects the narrative to the next topic; Chapter 05 hands off to Part III (PDEs and weak forms).

## ME 412 reading map (template for all Writings subtrees)

| Chapter | ME 412 object | Wire beat | Hands off to |
|---------|---------------|-----------|--------------|
| 00 Opening | Concept map: object → structure → theorem → failure | Mesh refines; energy norms replace dot products | 01 |
| 01 Motivation | Infinite-dimensional state; existence / stability | Load cell profile smooths as \(h \to 0\) | 02 |
| 02 Normed spaces | Banach spaces, completeness | Convergence needs a target norm | 03 |
| 03 Hilbert spaces | Inner products, orthogonality | \(L^2\) and energy inner products on the wire | 04 |
| 04 Operators & duality | Weak convergence, compactness preview | Stiffness as Galerkin projection of an operator | 05 |
| 05 Spectral theorem | Compact self-adjoint operators | Vibration modes → Part III weak forms | [Part III](../pde/chapters/00-opening.md) |

Other parts copy this **00 opening + numbered chapters + Bridge** contract; see the [unified arc diagram](../SUMMARY.md#one-diagram-ascent-then-descent).

## Build standalone

```bash
cd writings/functional-analysis && mdbook build
```

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, prefer upstream content here and re-run the sync script.
