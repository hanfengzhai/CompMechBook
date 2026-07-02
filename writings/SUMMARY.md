# Writings — source index

Canonical mdBook sources for **Computational Mechanics**. Each subtree follows the Functional Analysis Notes layout: `book.toml`, `chapters/SUMMARY.md`, `00-opening.md`, numbered `01`–`NN` chapter files.

| Subtree | Book section | Chapters |
|---------|--------------|----------|
| [preface](./preface/chapters/SUMMARY.md) | Preface | 00 |
| [prologue](./prologue/chapters/SUMMARY.md) | Prologue | 00 |
| [linear-algebra](./linear-algebra/chapters/SUMMARY.md) | Part I | 00, 01–04 |
| [functional-analysis](./functional-analysis/chapters/SUMMARY.md) | Part II | 00, 01–05 |
| [pde](./pde/chapters/SUMMARY.md) | Part III | 00, 01–04 |
| [fem](./fem/chapters/SUMMARY.md) | Part IV | 00, 01–05 |
| [fvm](./fvm/chapters/SUMMARY.md) | Part V | 00, 01–04 |
| [continuum](./continuum/chapters/SUMMARY.md) | Part VI | 00, 01–04 |
| [defects](./defects/chapters/SUMMARY.md) | Part VII | 00, 01–03 |
| [md](./md/chapters/SUMMARY.md) | Part VIII | 00, 01–03 |
| [dft](./dft/chapters/SUMMARY.md) | Part IX | 00, 01–03 |
| [epilogue](./epilogue/chapters/SUMMARY.md) | Epilogue | 00 |

Sync into the main book:

```bash
./scripts/sync-writings.sh
mdbook build
```

When the external `Writings` git submodule is linked, replace or merge these subtrees with upstream content and re-run the sync script.
