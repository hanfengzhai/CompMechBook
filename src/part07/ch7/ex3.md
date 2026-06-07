## 7.3 Link statistics and constitutive laws

### Single-exponential baseline

Earlier work reported link length distribution on slip system $i$:

$$
n_i^S(l) = \frac{N_i}{\bar{l}_i} e^{-l/\bar{l}_i},
$$

with $N_i$ link count and $\bar{l}_i$ mean length.

### Double exponential on active systems

The author's extension for **active** slip systems:

$$
n_i(l) = \frac{N_i^{(1)}}{\bar{l}_i^{(1)}} e^{-l/\bar{l}_i^{(1)}} + \frac{N_i^{(2)}}{\bar{l}_i^{(2)}} e^{-l/\bar{l}_i^{(2)}},
$$

with $\bar{l}_i^{(2)} > \bar{l}_i^{(1)}$ and $N_i^{(2)} \ll N_i^{(1)}$. The first term dominates short links; the second forms a **long tail** from stress-driven bowing of long links.

**Inactive** systems retain single exponentials.

### Generalized Poisson process

A stochastic model with **link splitting and growth** reproduces both distribution shapes—connecting DDD statistics to constitutive parameters (forest hardening, dynamic recovery) without ad hoc fitting alone.

### Impact on multiscale modeling

Graph neural networks trained on polycrystal FEM stress fields (author's CM 2025 work) achieve $150\times$ speedup over full solves—but still need training data grounded in physics. Link statistics constrain what those surrogates must respect at the microscale.

**Closing Part VII.** DDD closes the loop between FEM plasticity parameters and defect physics. When line models miss core reactions, we need atoms—Part VIII.
