# Appendix Notes

Canonical markdown for **Appendices** in CompMechBook, following the Functional Analysis Notes layout.

## Layout

```
appendix/
├── book.toml
├── chapters/
│   ├── SUMMARY.md
│   ├── glossary.md
│   ├── sources.md
│   └── memory-sheet.md
```

## Build standalone

```bash
cd writings/appendix && mdbook build
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
| Chapters feel choppy despite Bridges | [Continuous read-through guide](chapters/sources.md#continuous-read-through-guide) · [continuity hinges master map](chapters/memory-sheet.md#continuity-hinges-master-map) |
| Part boundaries feel like a new syllabus | [Story so far reunion (row 26)](chapters/sources.md#story-so-far-reunion-index-row-26) then [Closing the arc reunion (row 27)](chapters/sources.md#closing-the-arc-reunion-index-row-27) |
| Prior-part symbols do not translate | [Closing the arc reunion index](chapters/sources.md#closing-the-arc-reunion-index-row-27) |
| Cannot place the wire in the narrative arc | [Story so far reunion index](chapters/sources.md#story-so-far-reunion-index-row-26) |
| Transitions feel mechanical | [Bridge reunion index](chapters/sources.md#bridge-reunion-index-row-23) · [intra-part ascent I–V](chapters/sources.md#bridge-reunion-intra-part-ascent-i-v) · [intra-part descent VI–IX](chapters/sources.md#bridge-reunion-intra-part-descent-vi-ix) |
| Parameters crossing scales feel arbitrary | [Scale-boundary reunion (row 28)](chapters/sources.md#scale-boundary-reunion-index-row-28) · [parameter pedigree path](chapters/sources.md#parameter-pedigree-path-act-vi-reading-order) |
| Act II heating and Act III pulling feel like separate FEM homework | [Thermoelastic assembly reunion (row 29)](chapters/sources.md#thermoelastic-assembly-reunion-index-row-29) · [Part IV thermoelastic thread](../../src/part04-fem/00-opening.md#acts-ii-and-iii-together-thermoelastic-assembly-thread) |
| Need upstream PDFs and ME 412 maps | [Writings source index](../SUMMARY.md) · [Functional Analysis template](../functional-analysis/README.md) |

Book appendices in the unified mdBook: [`src/appendix/`](../../src/appendix/).
