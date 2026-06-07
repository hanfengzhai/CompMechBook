## 8.1 Potentials, ensembles, and integrators

### Interatomic potentials

| Class | Examples | Cost | Accuracy |
|-------|----------|------|----------|
| Empirical | EAM, Tersoff, Stillinger–Weber | Low | Chemistry-limited |
| Machine-learned | DeePMD, MACE, NequIP | Medium | Near-DFT if trained |
| Reactive | ReaxFF | Medium | Bond breaking |

Potentials approximate Born–Oppenheimer energy surfaces from DFT (Part IX) or experiment.

### Boundary conditions

- **Periodic:** bulk crystal, RVE
- **Fixed:** substrate clamping
- **Free surface:** vacuum slab

Artificial size effects require increasing $N$ until the property converges.

### Thermostats and barostats

**NVE** conserves energy (microcanonical). **NVT** (Nosé–Hoover, Langevin) and **NPT** (Parrinello–Rahman) sample ensembles relevant to experiment—essential when comparing MD moduli to room-temperature measurements.

### Time integration

**Velocity Verlet** is standard:

$$
\mathbf{v}^{n+1/2} = \mathbf{v}^n + \frac{\Delta t}{2m}\mathbf{F}^n, \quad
\mathbf{r}^{n+1} = \mathbf{r}^n + \Delta t\,\mathbf{v}^{n+1/2}, \quad
\mathbf{v}^{n+1} = \mathbf{v}^{n+1/2} + \frac{\Delta t}{2m}\mathbf{F}^{n+1}.
$$

Stability requires $\Delta t$ below the highest vibrational period—femtoseconds for metals. Implicit schemes exist for stiff bonds but are rare in production MD.

**Takeaway.** MD is explicit time stepping with a force law. Accuracy is potential accuracy; speed is parallelism (GPUMD, Kokkos LAMMPS).
