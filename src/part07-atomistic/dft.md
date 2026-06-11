# Density functional theory

## The electronic structure problem

Atoms bond because electrons obey quantum mechanics. Solving the many-electron Schrödinger equation exactly is intractable for large systems. **Density functional theory (DFT)** maps the problem to the electron density \(n(\mathbf{r})\).

**Hohenberg–Kohn theorems (statement):**

1. Ground-state energy is a functional of density \(E[n]\).
2. The minimizing density gives the true ground state.

**Kohn–Sham equations:** practical DFT introduces orbitals \(\psi_i\) solving

\[
\left[-\frac{1}{2}\nabla^2 + V_{\mathrm{eff}}[n](\mathbf{r})\right]\psi_i = \varepsilon_i \psi_i,
\]

with effective potential including Hartree, exchange–correlation \(V_{xc}\), and external ionic terms.

## Plane-wave pseudopotential workflow

The author's MSE 5720 homework (Cornell, Quantum ESPRESSO) illustrates the standard workflow for crystals like boron arsenide (BAs):

### 1. Convergence studies

**Plane-wave cutoff:** total energy must converge as the Fourier basis expands. Example criterion: successive cutoffs differ by less than ~5 meV/formula unit.

**k-point mesh:** Brillouin zone integration via Monkhorst–Pack grids; denser meshes reduce discretization error at higher cost.

### 2. Lattice constant optimization

Self-consistent field (`scf`) calculations at varied lattice parameters \(a\); fit \(E_{\mathrm{tot}}(a)\) (polynomial or equation of state); minimize to find equilibrium \(a_0\).

Compare \(a_0\) to experiment and literature **using the same exchange–correlation (XC) functional** (e.g. PBE)—functional choice shifts absolute lattice constants.

### 3. Bulk modulus

Fit energy vs volume near equilibrium:

\[
E(V) \approx E_0 + B_0 \frac{(V-V_0)^2}{2V_0},
\]

extracting bulk modulus \(B_0\).

### 4. XC functional sensitivity

Changing from LDA to PBE alters bond lengths and moduli—**functional validation** is part of every DFT study.

## Outputs for multiscale modeling

| DFT output | Downstream use |
|------------|----------------|
| Cohesive energy | phase diagrams |
| Elastic constants | continuum \(\mathbb{C}\) |
| Forces on atoms | MD potentials (DeePMD) |
| Phonon spectra | thermal properties |

The author's DeePMD-Graphene project trains neural potentials on Quantum ESPRESSO DFT data—closing the loop from electrons to MD.

## Practical notes

- **Pseudopotentials** replace core electrons with effective potentials.
- **Periodic boundary conditions** idealize infinite crystals; surfaces need slabs.
- **Spin polarization** matters for magnetic materials.

DFT is not "more accurate MD"—it is a different rung on the multiscale ladder, usually at 0 K or finite T via quasi-harmonic approximations, with electron correlation approximated by \(V_{xc}\).

<div class="bridge">

**Bridge (end of Part VII).** We have reached electrons. The **epilogue** steps back to narrate the full journey and what remains open.

</div>
