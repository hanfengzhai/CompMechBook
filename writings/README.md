# Writings source integration

This directory holds canonical markdown for **Computational Mechanics** (CompMechBook). It is structured for eventual linking as a [`Writings`](https://github.com/hanfengzhai/Writings) git submodule; until that remote is available, the full source tree is vendored here.

## Layout (Functional Analysis Notes style)

Each part is a standalone mdBook:

```
writings/
├── linear-algebra/          # Part I  — chapters 01–04
├── functional-analysis/     # Part II — chapters 01–05
├── pde/                     # Part III — chapters 01–04
├── fem/                     # Part IV — chapters 01–05
├── fvm/                     # Part V  — chapters 01–04
├── continuum/               # Part VI — chapters 01–03
├── defects/                 # Part VII — chapters 01–02
├── md/                      # Part VIII — chapters 01–02
└── dft/                     # Part IX — chapters 01–02
```

Every subtree contains:

- `book.toml` — standalone mdBook configuration with MathJax
- `chapters/SUMMARY.md` — table of contents
- `chapters/NN-*.md` — numbered chapters with **Bridge** sections linking to the next part

## Integration workflow

1. Edit canonical chapters under `writings/<topic>/chapters/`.
2. Sync into the main book:

   ```bash
   chmod +x scripts/sync-writings.sh
   ./scripts/sync-writings.sh
   mdbook build
   ```

3. Chapter mapping (numbering preserved):

   | Writings path | Book destination |
   |---------------|------------------|
   | `linear-algebra/chapters/01–04` | `src/part01-linear-algebra/` |
   | `functional-analysis/chapters/01–05` | `src/part02-functional-analysis/` |
   | `pde/chapters/01–04` | `src/part03-pdes/` |
   | `fem/chapters/01–05` | `src/part04-fem/` |
   | `fvm/chapters/01–04` | `src/part05-fvm/` |
   | `continuum/chapters/01–03` | `src/part06-continuum/` |
   | `defects/chapters/01–02` | `src/part07-defects/` |
   | `md/chapters/01–02` | `src/part08-md/` |
   | `dft/chapters/01–02` | `src/part09-dft/` |

4. Merge strategy: prefer Writings content as canonical; retain book-specific **Bridge** sections and cross-links at chapter ends.

5. Verify the build:

   ```bash
   mdbook build
   ./scripts/build-all-writings.sh   # optional: all standalone mdBooks
   ```

## Canonical source workflow

All parts are maintained as standalone mdBooks under `writings/` (Functional Analysis Notes layout). The rendered narrative in `src/` is synced from these sources via `scripts/sync-writings.sh`. Book-specific **Bridge** sections at chapter ends may be edited in either location; re-run sync after updating canonical chapters.

Build the standalone Functional Analysis Notes:

```bash
cd writings/functional-analysis && mdbook build
```

When the external `Writings` git submodule is linked, replace or merge these subtrees with upstream content and re-run the sync script.
