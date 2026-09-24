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

## Reading map (continuous book)

| When the plot stutters | Open |
|------------------------|------|
| Part II feels like disconnected theorems | [Bridge reunion — Part II (intra-part)](../appendix/chapters/sources.md#bridge-reunion-intra-part-ii) |
| Proofs need structure | [Concept map reunion — Part II](../appendix/chapters/sources.md#concept-map-reunion-index-row-24) |
| Proofs need a diagram | [Schematic reunion — ME 412](../appendix/chapters/sources.md#schematic-reunion-index-row-25) |

Template subtree for all `writings/` folders. Upstream: [ME412 Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf). Book part: [Part II in `src/part02-functional-analysis/`](../../src/part02-functional-analysis/).
