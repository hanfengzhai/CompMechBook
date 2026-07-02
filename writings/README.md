# Writings source integration

This directory holds canonical markdown for **Computational Mechanics** (CompMechBook). It is structured for eventual linking as a [`Writings`](https://github.com/hanfengzhai/Writings) git submodule; until that remote is available, the full source tree is vendored here.

## Layout (Functional Analysis Notes style)

Each part is a standalone mdBook:

```
writings/
├── preface/                 # Preface
├── prologue/                # Prologue — one wire, many scales
├── linear-algebra/          # Part I  — opening + chapters 01–04
├── functional-analysis/     # Part II — opening + chapters 01–05
├── pde/                     # Part III — opening + chapters 01–04
├── fem/                     # Part IV — opening + chapters 01–05
├── fvm/                     # Part V  — opening + chapters 01–04
├── continuum/               # Part VI — opening + chapters 01–04
├── defects/                 # Part VII — opening + chapters 01–03
├── md/                      # Part VIII — opening + chapters 01–03
├── dft/                     # Part IX — opening + chapters 01–03
└── epilogue/                # Epilogue — multiscale coupling
```

Every subtree contains:

- `book.toml` — standalone mdBook configuration with MathJax
- `chapters/SUMMARY.md` — table of contents
- `chapters/00-opening.md` — part framing (synced to `src/partNN-*/00-opening.md`)
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
   | `linear-algebra/chapters/00, 01–04` | `src/part01-linear-algebra/` |
   | `functional-analysis/chapters/00, 01–05` | `src/part02-functional-analysis/` |
   | `pde/chapters/00, 01–04` | `src/part03-pdes/` |
   | `fem/chapters/00, 01–05` | `src/part04-fem/` |
   | `fvm/chapters/00, 01–04` | `src/part05-fvm/` |
   | `continuum/chapters/00, 01–04` | `src/part06-continuum/` |
   | `defects/chapters/00, 01–03` | `src/part07-defects/` |
   | `md/chapters/00, 01–03` | `src/part08-md/` |
   | `dft/chapters/00, 01–03` | `src/part09-dft/` |

4. Book-specific material (prologue, preface, epilogue, appendix) lives only in `src/`.

## Build standalone notes

```bash
cd writings/functional-analysis && mdbook build
cd writings/linear-algebra && mdbook build
# … any other subtree, or:
./scripts/build-all-writings.sh
```

## Submodule (future)

When the remote repository is available:

```bash
git submodule add <Writings-repo-url> writings
git submodule update --init --recursive
./scripts/sync-writings.sh
```

See [SUMMARY.md](./SUMMARY.md) for the full index of subtrees.
