# Part VIII — Atomistic Simulation

Parts I–VII treated matter as fields and defects — smooth continua, mesoscale dislocation networks. At nanometers, that picture thins. Individual atoms swap neighbors at grain boundaries; crack tips break bonds one coordination shell at a time; thermal vibrations carry energy that no elliptic PDE resolves without homogenization.

Molecular dynamics puts the atoms back. Nuclei move on a **potential energy surface** that Born–Oppenheimer separation (Part IX) justifies and DFT or experiments supply. The state is not a displacement field but a list of positions and momenta in phase space; the equations are Newton's laws or Hamilton's equations; the discretization is a timestep and a neighbor-list cutoff.

The copper wire's drawn microstructure — dislocation forests, vacancies from processing, thermal motion at room temperature — lives here. MD does not replace FEM for structural design, but it **feeds** FEM: elastic constants, stacking-fault energies, fracture toughness estimates, and potentials for coarse-grained models. The layout follows [`writings/md/`](../../writings/md/). Read the two chapters in order; Chapter 02 hands off to Part IX, where the electrons that bind those atoms are treated explicitly.
