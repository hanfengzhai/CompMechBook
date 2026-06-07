## 9.2 Plane waves, pseudopotentials, and practice

### Plane-wave basis

Periodic crystals expand $\psi_i$ in plane waves $\mathbf{G}$ up to cutoff $E_{\text{cut}}$:

$$
\psi_i(\mathbf{r}) = \sum_{\mathbf{G}} c_{i\mathbf{G}} e^{i\mathbf{G}\cdot\mathbf{r}}.
$$

Cutoff and k-point sampling control convergence—analogous to mesh refinement in FEM.

### Pseudopotentials

Core electrons are frozen; **pseudopotentials** (ultrasoft, PAW) reduce active electrons and cutoff cost. Choice affects elastic constants and defect energies—document your pseudopotential in multiscale pipelines.

### Typical workflow (Quantum ESPRESSO)

1. Relax lattice and atomic positions (`vc-relax`)
2. Compute elastic constants (finite strain)
3. Extract surface / generalized stacking fault energies
4. Export to fitting codes for interatomic potentials

The author's MSE5720 notebooks walk through silicon band structures and geometry optimization—template calculations extensible to metals and defects.

### When DFT is not enough

- Strong correlation (some oxides, transition metals) → DFT+U, hybrid functionals, DMFT
- Excited states, spectroscopy → TDDFT, GW
- Large systems → linear scaling, ML surrogates (M3GNet, CHGNet for materials informatics)

**Closing Part IX.** We have reached the bottom of the ladder for ground-state bonding. The Epilogue asks how to climb back up—with verified information flow at each rung.
