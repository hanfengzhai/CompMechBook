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

## Sync into CompMechBook

```bash
./scripts/sync-writings.sh
mdbook build
```
