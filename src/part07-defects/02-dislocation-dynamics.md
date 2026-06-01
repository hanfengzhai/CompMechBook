# Dislocation Dynamics and Strain Hardening

When metal yields, dislocations multiply and tangle. **Dislocation dynamics (DDD)** tracks their motion and interactions — the mesoscale engine of strain hardening.

## Discrete dislocation dynamics

Each dislocation is a curve (or network of segments) in a elastic medium. Motion follows **Peach–Köhler** forces from the stress field; reactions occur when segments collide or annihilate. Elastic interactions are long-ranged; efficient algorithms use fast multipole or precomputed Green's functions.

Open-source frameworks such as [OpenDiS](https://github.com/OpenDiS/OpenDiS) and ParaDiS implement these algorithms at scale — enabling simulations of work hardening in single crystals and polycrystals.

## Strain hardening and link statistics

Classical models relate flow stress to dislocation density \(\rho\):

\[
\tau = \alpha \mu b \sqrt{\rho},
\]

(Taylor hardening). Recent work on **link statistics** — how dislocation lines form connected networks during loading — refines how \(\rho\) and topology co-evolve. The author's research on [link statistics during strain hardening](https://doi.org/10.1016/j.jmps.2026.106533) sits at this interface: using large-scale DDD to extract statistical laws that continuum models can adopt.

## Coupling scales

| Scale | Method | Output to next scale |
|-------|--------|---------------------|
| DDD | Line defect motion | Hardening law, stress–strain |
| Crystal plasticity FEM | Slip systems | Polycrystal texture |
| Continuum FEM | Homogenized \(\mathbb{C}\) | Engineering design |

Machine learning (e.g., graph neural networks on polycrystal meshes) accelerates the FEM step by learning stress fields from microstructure — but still needs DDD or experiments for training data at the mesoscale.

## Bridge

Dislocations are lines of missing registry in a lattice — but atoms still matter at the core. Molecular dynamics resolves the core structure and provides mobility laws DDD calibrates against.
