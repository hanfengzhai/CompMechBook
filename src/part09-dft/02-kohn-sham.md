# Kohn–Sham DFT: Equations, Convergence, and Practice

Kohn–Sham DFT turns the abstract energy functional into a self-consistent field problem — orbitals, eigenvalues, and a cycle that must converge before any property is trusted.

## Kohn–Sham equations

Introduce orthonormal **Kohn–Sham orbitals** \(\psi_i\) and solve

\[
\left[-\tfrac{1}{2}\nabla^2 + V_{\text{eff}}[\rho]\right]\psi_i = \epsilon_i \psi_i,
\]

with

\[
\rho(\mathbf{r}) = \sum_i^{\text{occ}} |\psi_i(\mathbf{r})|^2.
\]

The effective potential includes Hartree, external ionic, and exchange–correlation terms — all depending on \(\rho\). **Self-consistency**: guess \(\rho\), solve for \(\psi_i\), build new \(\rho\), repeat until convergence.

## Plane-wave basis and pseudopotentials

Periodic crystals expand orbitals in **plane waves**:

\[
\psi(\mathbf{r}) = \sum_{\mathbf{G}} c_{\mathbf{G}} e^{i\mathbf{G}\cdot\mathbf{r}}.
\]

**Cutoff energy** truncates the sum — too low, energies are wrong; too high, cost explodes. **k-point sampling** discretizes the Brillouin zone for integration over band structure.

**Pseudopotentials** replace core electrons with smooth effective potentials, reducing plane-wave count. XC functional is often encoded in the pseudopotential file — compare literature using matching functionals.

## Convergence workflow (from practice)

The author's [MSE 5720 DFT coursework](https://github.com/hanfengzhai/MSE5720-HW) walks through standard exercises:

1. **Converge cutoff and k-grid** on total energy and forces
2. **Optimize lattice constants** via equation of state fitting or internal optimizers
3. **Compute bulk modulus** from energy–volume curves
4. **Compare band structures and DOS** with literature on the same k-path
5. **Test pseudopotential / XC sensitivity** against experiment

These steps are not bureaucratic — unconverged DFT is structured noise.

## Properties for multiscale pipelines

| DFT output | Downstream use |
|------------|----------------|
| Cohesive energy | Phase diagrams |
| Elastic constants | Continuum \(\mathbb{C}\) |
| Phonon spectra | Thermal properties, MD validation |
| Surface energies | Crack models, wettability |
| Forces on atoms | Ab initio MD, force-field fitting |

## Bridge to the epilogue

We began with a copper wire and asked how each scale describes it. DFT explains cohesion; MD explains thermal motion and fracture; DDD explains work hardening; FEM explains bending; CFD explains cooling fluid around it. Multiscale computational mechanics is the craft of making those descriptions converse.
