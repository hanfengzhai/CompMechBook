# Writings source integration

This directory holds canonical mdBook sources for every part of **Computational Mechanics**, following the **Functional Analysis Notes** layout (`book.toml`, numbered `chapters/`, **Bridge** sections). When the external [`Writings`](https://github.com/hanfengzhai/Writings) git submodule is linked, merge upstream changes here and re-run `scripts/sync-writings.sh`.

## Layout

```
writings/
├── linear-algebra/          # Linear Algebra Notes (mdBook) → Part I
│   └── chapters/01–04
├── functional-analysis/     # Functional Analysis Notes (mdBook) → Part II
│   └── chapters/01–05
├── pde/                     # ME300B → Part III
├── fem/                     # FEA notes → Part IV
├── fvm/                     # FVM / CFD → Part V
├── continuum/               # Elasticity → Part VI
├── defects/                 # Defects & dislocations → Part VII
├── md/                      # Atomistic modeling → Part VIII
└── dft/                     # MSE 5720 → Part IX
```

Each subtree has `book.toml`, `chapters/SUMMARY.md`, and numbered markdown files. See [SUMMARY.md](./SUMMARY.md) for the full index.

## Integration workflow

1. Add the submodule:

   ```bash
   git submodule add <Writings-repo-url> writings
   git submodule update --init --recursive
   ```

2. Map numbered chapters to book parts (preserve `01`–`NN` prefixes):

   | Writings path | Book destination |
   |---------------|------------------|
   | `linear-algebra/chapters/01–04` | `src/part01-linear-algebra/` |
   | `functional-analysis/chapters/01–05` | `src/part02-functional-analysis/` |
   | `pde/chapters/01–04` (planned) | `src/part03-pdes/` |
   | `fem/chapters/01–05` (planned) | `src/part04-fem/` |
   | … | … |

3. Merge strategy: prefer Writings content as canonical; retain book-specific **Bridge** sections and cross-links to Parts III–IV at the end of each chapter.

4. Verify the build:

   ```bash
   mdbook build
   ```

## Canonical source workflow

All parts are maintained as standalone mdBooks under `writings/` (Functional Analysis Notes style). The rendered narrative in `src/` is synced from these sources via `scripts/sync-writings.sh`. Book-specific **Bridge** sections at chapter ends may be edited in either location; re-run sync after updating canonical chapters.

Sync canonical chapters into the main book with:

```bash
chmod +x scripts/sync-writings.sh
./scripts/sync-writings.sh
mdbook build
```

Build the standalone FA notes:

```bash
cd writings/functional-analysis && mdbook build
```
