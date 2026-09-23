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

## Appendix reading map (continuity when the plot stutters)

Use these chapters when the copper-wire narrative is correct line-by-line but a **scale change feels abrupt**. They mirror the ME 412 **Bridge** contract at book level: name the hinge, then return to the numbered chapter.

| Chapter | Navigation object | Open when… | Then read |
|---------|-------------------|------------|-----------|
| [glossary](chapters/glossary.md) | Cross-scale symbol index | Notation from an earlier part no longer maps | Matching row in [sources](chapters/sources.md#continuity-hinges-index-when-the-plot-stutters) |
| [sources](chapters/sources.md) | Continuity hinges rows 0–44; reunion indices 17–43 | Scene, Lab act, or Bridge rhythm breaks mid-read | The row’s linked Bridge or part-opening anchor |
| [memory-sheet](chapters/memory-sheet.md) | Baby pictures; six-act tables; handshake map | You want one-page recall before a gate chapter | [Continuous read-through](chapters/sources.md#continuous-read-through-guide) |

**Default path:** start at [continuity hinges index](chapters/sources.md#continuity-hinges-index-when-the-plot-stutters) row **17** (Scene → Bridge rhythm), then row **23** ([Bridge reunion](chapters/sources.md#bridge-reunion-index-row-23)) for part boundaries, or [Part VII intra-part descent bridges](chapters/sources.md#bridge-reunion-intra-part-vii) / [VIII–IX intra-part descent bridges](chapters/sources.md#bridge-reunion-intra-part-viii-ix) when descent chapter turns feel mechanical mid-part.

See the [Writings arc table](../SUMMARY.md#multiscale-story-arc-one-table) for where each part sits in ascent and descent.

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
