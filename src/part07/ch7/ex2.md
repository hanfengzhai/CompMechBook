## 7.2 Discrete dislocation dynamics (DDD)

### Simulation setup

Typical workflow (ParaDiS, OpenDiS):

1. Initialize Frank–Read sources or random networks
2. Apply loading rate $\dot{\gamma}$ on remote boundary
3. Evolve segments: velocity $\propto$ Peach–Köhler force with mobility law
4. Handle topological events (reconnect, merge, split)
5. Output stress–strain and dislocation density vs time

The author's copper single-crystal study uses **118 loading orientations** across the stereographic triangle between [001], [011], and [111], with $\sim 2\times 10^4$ links per configuration averaged over strain windows $\gamma \in [0.9, 1.05]\%$.

### Mobility and drag

Mobility $B$ relates velocity to force: $\mathbf{v} = B \mathbf{f}$. Phonon drag, radiation damping, and obstacle pinning enter $B$. MD can calibrate $B(\mathbf{T})$; DFT can calibrate core energies that set short-range barriers.

### Bridging to FEM

**Discrete dislocation plasticity (DDP)** superposes analytically computed dislocation fields on a FEM mesh—continuum elasticity with discrete carriers. Full DDD replaces the constitutive update with explicit line evolution—feasible for RVE-sized volumes, not full engineering parts.

**Takeaway.** DDD answers mesoscale questions: Which slip systems activate? How do link lengths evolve? What hardening law is physically justified?
