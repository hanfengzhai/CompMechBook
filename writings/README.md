# Writings source integration

This directory holds canonical mdBook sources for every part of **Computational Mechanics**, following the **Functional Analysis Notes** layout (`book.toml`, numbered `chapters/`, **Bridge** sections). When the external [`Writings`](https://github.com/hanfengzhai/Writings) git submodule is linked, merge upstream changes here and re-run `scripts/sync-writings.sh`. Until that remote is available, the full source tree is vendored here.

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

1. Edit canonical chapters under `writings/<topic>/chapters/`.
2. Sync into the main book:

   ```bash
   chmod +x scripts/sync-writings.sh
   ./scripts/sync-writings.sh
   mdbook build
   ```

3. Map numbered chapters to book parts (preserve `01`–`NN` prefixes):

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

4. Book-specific material (prologue, preface, epilogue, appendix) lives only in `src/`.

5. Merge strategy: prefer Writings content as canonical; retain book-specific **Bridge** sections and cross-links when merging from upstream.

6. Book-only pages (prologue, preface, epilogue, appendix) are not overwritten by sync.

## Canonical source workflow

All parts are maintained as standalone mdBooks under `writings/` (Functional Analysis Notes style). The rendered narrative in `src/` is synced from these sources via `scripts/sync-writings.sh`. Re-run sync after editing canonical chapters under `writings/<topic>/chapters/`.

## Build standalone notes

```bash
cd writings/functional-analysis && mdbook build
./scripts/build-all-writings.sh   # all nine parts
```

## Submodule (future)

When the remote repository is available:

```bash
git submodule add <Writings-repo-url> writings
git submodule update --init --recursive
./scripts/sync-writings.sh
```
