# Writings — source index

Canonical mdBook sources for **Computational Mechanics**. Each subtree follows the Functional Analysis Notes layout: `book.toml`, `chapters/SUMMARY.md`, numbered `01`–`NN` chapter files.

| Subtree | Book part | Chapters |
|---------|-----------|----------|
| [linear-algebra](./linear-algebra/chapters/SUMMARY.md) | Part I | 01–04 |
| [functional-analysis](./functional-analysis/chapters/SUMMARY.md) | Part II | 01–05 |
| [pde](./pde/chapters/SUMMARY.md) | Part III | 01–04 |
| [fem](./fem/chapters/SUMMARY.md) | Part IV | 01–05 |
| [fvm](./fvm/chapters/SUMMARY.md) | Part V | 01–04 |
| [continuum](./continuum/chapters/SUMMARY.md) | Part VI | 01–03 |
| [defects](./defects/chapters/SUMMARY.md) | Part VII | 01–02 |
| [md](./md/chapters/SUMMARY.md) | Part VIII | 01–02 |
| [dft](./dft/chapters/SUMMARY.md) | Part IX | 01–02 |

Sync into the main book:

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, replace or merge these subtrees with upstream content and re-run the sync script.
