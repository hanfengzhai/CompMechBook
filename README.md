# CompMechBook

A continuous narrative textbook on **computational mechanics**, from linear algebra and functional analysis through finite element and finite volume methods to dislocation dynamics, molecular dynamics, and density functional theory.

Built with [mdBook](https://github.com/rust-lang/mdBook).

## Read online

After building, open `book/index.html` locally, or deploy the `book/` directory to GitHub Pages.

## Build

```bash
# Install mdBook: https://github.com/rust-lang/mdBook/releases
mdbook build
mdbook serve   # live preview at http://localhost:3000
```

## Structure

| Part | Topic |
|------|-------|
| I | Linear algebra |
| II | Functional analysis (FA Notes style) |
| III | Continuum mechanics & weak forms |
| IV | Finite element method |
| V | Finite volume method & CFD |
| VI | Defects & dislocation dynamics |
| VII | Molecular dynamics, statistical mechanics, DFT |

Source material is drawn from [personal notes](https://hanfengzhai.github.io/note.html). `Writings.git` will be integrated as a submodule when available.

## License

Content © Hanfeng Zhai. Build tooling follows mdBook (MPL-2.0).
