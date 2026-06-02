# Writings source integration

This directory is reserved for the [`Writings`](https://github.com/hanfengzhai/Writings) git submodule. When the repository is linked, source markdown — including the **Functional Analysis Notes** — will be mapped into the mdBook chapters under `src/`.

## Expected layout (after submodule add)

```
writings/
├── functional-analysis/     # Functional Analysis Notes (mdBook)
│   ├── SUMMARY.md
│   └── chapters/
├── linear-algebra/          # Optional: ME300A source markdown
├── pde/                     # Optional: ME300B source markdown
└── ...
```

## Integration workflow

1. Add the submodule:

   ```bash
   git submodule add <Writings-repo-url> writings
   git submodule update --init --recursive
   ```

2. Map Functional Analysis Notes to Part II (preserve chapter numbering `01`–`05`):

   | Writings path | Book chapter |
   |---------------|--------------|
   | `functional-analysis/01-*.md` | `src/part02-functional-analysis/01-motivation.md` |
   | `functional-analysis/02-*.md` | `src/part02-functional-analysis/02-normed-spaces.md` |
   | `functional-analysis/03-*.md` | `src/part02-functional-analysis/03-hilbert-spaces.md` |
   | `functional-analysis/04-*.md` | `src/part02-functional-analysis/04-operators-duality.md` |
   | `functional-analysis/05-*.md` | `src/part02-functional-analysis/05-spectral-theorem.md` |

3. Merge strategy: prefer Writings content as canonical; retain book-specific **Bridge** sections and cross-links to Parts III–IV at the end of each chapter.

4. Verify the build:

   ```bash
   mdbook build
   ```

## Until the submodule is available

Part II chapters in `src/part02-functional-analysis/` are written in the same mdBook style and at the same level of detail as the planned Functional Analysis Notes. They synthesize the author's course materials and standard references (Brezis, Evans) with a computational mechanics focus.
