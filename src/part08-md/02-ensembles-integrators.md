# Ensembles, Integrators, and Practical Molecular Dynamics

MD is not merely integrating Newton's laws — it is controlled sampling of statistical mechanics. The integrator and thermostat determine what physical state the simulation represents.

## Time integration

**Verlet** and **velocity Verlet** are symplectic, second-order schemes preserving phase-space structure approximately:

\[
\mathbf{r}^{n+1} = 2\mathbf{r}^n - \mathbf{r}^{n-1} + \mathbf{a}^n \Delta t^2.
\]

Timestep \(\Delta t\) must resolve the highest vibrational frequency — typically femtoseconds for metals. **Constraint algorithms** (SHAKE, RATTLE) freeze fast bonds when implicit integration is too costly.

## Thermostats and barostats

| Ensemble | Control | Algorithm examples |
|----------|---------|-------------------|
| NVE | Energy fixed | Verlet |
| NVT | Temperature fixed | Nosé–Hoover, Langevin, Berendsen |
| NPT | Temperature + pressure | Parrinello–Rahman |

Choosing the wrong ensemble misrepresents the experiment you compare against.

## Extracting continuum quantities

**Stress**: Irving–Kirkwood or Hardy formulas relate atomic trajectories to Cauchy stress.

**Temperature**: equipartition of kinetic energy.

**Elastic constants**: fluctuation formulas or small-strain deformations.

**Dislocation mobility**: fit velocity–stress curves from constrained MD for input to DDD.

## Software ecosystem

[LAMMPS](https://www.lammps.org/) and [GPUMD](https://github.com/brucefan1983/GPUMD) scale to billions of atoms on GPUs. Workflows often chain:

```
DFT → fit potential → MD → extract parameters → DDD / FEM
```

## Bridge

MD assumes classical nuclei with empirical or fitted potentials. When potentials themselves must be derived from first principles — bond breaking, chemistry, electronic effects — we descend one more rung to density functional theory.
