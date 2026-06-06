# Part VIII — Atomistic Simulation

Part VII followed dislocation lines through a crystal. Dislocation cores, grain boundaries, crack tips, and diffusion paths are regions where continuum fields are too coarse — the material is better described as a collection of nuclei moving under interatomic forces.

Molecular dynamics (MD) is that description made computational: Newton's equations (or Hamilton's equations) for \(10^4\)–\(10^9\) atoms, interatomic potentials fit to quantum data or experiments, thermostats and barostats for temperature and pressure control, symplectic integrators that respect the geometry of phase space. The copper wire at this scale is a block of FCC lattice with thermal vibrations, vacancies from processing, and perhaps a crack initiated by stretching bonds beyond their cohesive range.

The layout follows the **Atomistic Modeling Notes** in [`writings/md/`](../../writings/md/): numbered chapters on potentials, ensembles, and integrators, with **Bridge** sections toward Part IX, where potentials themselves are derived from electronic structure.
