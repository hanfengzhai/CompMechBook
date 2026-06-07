## 8.2 From atomic motion to continuum properties

### Stress from virial

The **virial stress** at temperature $T$:

$$
\sigma_{\alpha\beta} = \frac{1}{V}\left[ \sum_i m v_{i\alpha} v_{i\beta} + \sum_{i<j} r_{ij\alpha} F_{ij\beta} \right].
$$

Time-averaged $\langle \boldsymbol{\sigma} \rangle$ gives Cauchy stress for comparison with FEM/continuum.

### Elastic constants

Small strain fluctuations or direct strain–stress probes yield $C_{ijkl}$—inputs for DDD and crystal plasticity.

### Defect energetics

Dislocation core structure, stacking fault energies, and crack tip emission sequences are measured in MD and fed upward:

$$
\text{DFT} \to \text{potential fit} \to \text{MD} \to \text{DDD parameters} \to \text{FEM constitutive law}
$$

### Limits

- **Time:** nanoseconds routine, microseconds heroic
- **Length:** nanometers to microns
- **Electrons:** no bond breaking without reactive ML potentials or QM/MM

**Closing Part VIII.** MD resolves atomic configurations DDD and FEM smooth over. When potentials fail—new chemistry, odd oxidation states—we need electrons: Part IX.
