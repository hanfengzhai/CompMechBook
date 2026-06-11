# Statistical mechanics as a bridge

## Why statistical mechanics?

MD produces trajectories \(\mathbf{r}_i(t)\). Experiments measure **averages**—stress, temperature, elastic moduli. **Statistical mechanics** connects microscopic states to macroscopic thermodynamics.

The author's *Statistical Mechanics* notes develop ensembles, partition functions, and fluctuations—the language for interpreting MD and DFT outputs.

## Microscopic vs macroscopic

**Microstate:** complete specification of positions and momenta (classical) or quantum state.

**Macrostate:** few parameters (T, P, volume V) describing equilibrium.

**Boltzmann entropy:**

\[
S = k_B \ln \Omega,
\]

with \(\Omega\) the number of microstates consistent with the macrostate.

## Ensembles (recap with MD)

| Ensemble | Control | MD realization |
|----------|---------|----------------|
| Canonical NVT | T, V fixed | thermostat |
| Microcanonical NVE | E, V fixed | plain Verlet |
| Isothermal–isobaric NPT | T, P fixed | thermostat + barostat |

**Ergodic hypothesis:** time averages equal ensemble averages—justifies extracting modulus from a long MD run.

## Free energy and driving forces

**Helmholtz free energy** \(F = U - TS\) governs equilibrium at fixed T,V.

Phase stability, defect formation energies, and chemical potentials derive from free energies—quantities DFT computes via electronic structure.

## Fluctuation–dissipation

Elastic constants can be computed from stress fluctuations in NVT MD (for small systems, careful finite-size corrections apply).

## Upward coupling

```
  DFT  →  energies, forces for small cells
    ↓
  MD   →  trajectories, RVE stress–strain
    ↓
  DD / crystal plasticity  →  defect-mediated hardening
    ↓
  FEM  →  part-scale deformation
```

Statistical mechanics is the grammar of that upward translation: which averages matter, which ensembles apply, which fluctuations are noise vs signal.

<div class="bridge">

**Bridge.** Electrons determine chemical bonding and stiffness. **Density functional theory** solves for electron density and delivers the energies MD and continuum models inherit.

</div>
