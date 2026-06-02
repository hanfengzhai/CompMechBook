# Writings — canonical sources for CompMechBook

This directory is the **Writings** corpus: markdown derived from the author's course notes ([hanfengzhai.github.io](https://hanfengzhai.github.io/note.html)) and organized like the **Functional Analysis Notes** — each topic is a small mdBook with numbered chapters that sync into the main narrative under `src/`.

## Layout (Functional Analysis Notes style)

Every populated subtree follows the same pattern:

```
writings/<topic>/
├── book.toml              # standalone mdBook metadata
└── chapters/
    ├── SUMMARY.md         # chapter list
    ├── 01-….md
    ├── 02-….md
    └── …
```

| Subtree | CompMechBook destination | Source PDF / notes |
|---------|--------------------------|-------------------|
| `linear-algebra/` | `src/part01-linear-algebra/` | [ME300A_LinAlg.pdf](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) |
| `functional-analysis/` | `src/part02-functional-analysis/` | Functional Analysis Notes |
| `pde/` | `src/part03-pdes/` | [ME300B_PDE.pdf](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) |
| `fem/` | `src/part04-fem/` | [FEA_notes.pdf](https://hanfengzhai.github.io/file/FEA_notes.pdf) |
| `fvm/` | `src/part05-fvm/` | [FVM.pdf](https://hanfengzhai.github.io/note/FVM.pdf), [CFD_note.pdf](https://hanfengzhai.github.io/file/CFD_note.pdf) |
| `continuum/` | `src/part06-continuum/` | [elasticity_notes.pdf](https://hanfengzhai.github.io/file/elasticity_notes.pdf) |
| `defects/` | `src/part07-defects/` | [defects_notes.pdf](https://hanfengzhai.github.io/file/defects_notes.pdf) |
| `md/` | `src/part08-md/` | [AtomModel_note.pdf](https://hanfengzhai.github.io/file/AtomModel_note.pdf) |
| `dft/` | `src/part09-dft/` | [MSE5720-HW](https://github.com/hanfengzhai/MSE5720-HW) |

The **main book** (`book.toml` at repo root) adds the copper-wire narrative: preface, prologue, epilogue, cross-part bridges, and `src/SUMMARY.md` as the reading order.

## Integration workflow

1. Edit canonical prose in `writings/<topic>/chapters/`.
2. Sync into the main book:

   ```bash
   ./scripts/sync-writings.sh
   ```

3. Add or adjust **Bridge** sections and prologue/epilogue links in `src/` when the narrative arc needs book-specific glue (not duplicated in Writings).
4. Verify:

   ```bash
   mdbook build
   ```

## Optional: external `Writings.git` submodule

If a separate `Writings` repository is published later, replace this directory with:

```bash
git submodule add <Writings-repo-url> writings
git submodule update --init --recursive
```

The sync script and chapter numbering (`01`–`NN`) are unchanged.

## Merge policy

- **Writings** = canonical technical content aligned with course notes.
- **`src/`** = narrative frame (prologue, epilogue, bridges, SUMMARY) plus synced chapters.
- Prefer editing `writings/` first, then run `./scripts/sync-writings.sh`.
