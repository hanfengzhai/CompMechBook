# Writings source integration

This directory is reserved for the [`Writings`](https://github.com/hanfengzhai/Writings) git submodule. When the repository is linked, source markdown — including the **Functional Analysis Notes** — will be mapped into the mdBook chapters under `src/`.

## Expected layout (after submodule add)

```
writings/
├── linear-algebra/          # Linear Algebra Notes (mdBook) → Part I
│   └── chapters/01–04
├── functional-analysis/     # Functional Analysis Notes (mdBook) → Part II
│   └── chapters/01–05
├── pde/                     # Planned: ME300B → Part III
├── fem/                     # Planned: FEA notes → Part IV
├── fvm/                     # Planned: FVM / CFD → Part V
├── continuum/               # Planned: elasticity → Part VI
├── defects/                 # Planned → Part VII
├── md/                      # Planned → Part VIII
└── dft/                     # Planned: MSE 5720 → Part IX
```

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

## Until the submodule is available

Parts I and II are maintained as standalone mdBooks under `writings/linear-algebra/` and `writings/functional-analysis/` (Functional Analysis Notes style: `book.toml`, `chapters/SUMMARY.md`, numbered `01`–`NN` files). Remaining parts live in `src/` until their Writings subtrees are populated; see each subtree's `README.md` for the target layout.

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
