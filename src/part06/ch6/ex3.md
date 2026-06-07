## 6.3 Crystal plasticity and homogenization

### Crystal plasticity FEM

Each grain has orientation $R$ mapping crystal frame to sample frame. Slip rate $\dot{\gamma}^\alpha$ on system $\alpha$ follows Schmid law $\tau^\alpha = \boldsymbol{\sigma} : \mathbf{S}^\alpha$ with flow rule $\dot{\gamma}^\alpha = f(\tau^\alpha, \text{history})$.

The **velocity gradient** decomposes into symmetric stretch and slips:

$$
\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1} = \sum_\alpha \dot{\gamma}^\alpha \mathbf{s}^\alpha \otimes \mathbf{m}^\alpha + \cdots
$$

FEM integrates this over grains in a polycrystal—expensive but predictive for texture and anisotropic hardening.

### Strain hardening laws

Phenomenological laws $\sigma_y = \sigma_0 + H(\bar{\varepsilon}^p)$ fit data but do not explain microstructure. **Dislocation density** models $\rho$ evolve by multiplication and annihilation:

$$
\dot{\rho} = k_1 \sqrt{\rho}\,\dot{\bar{\varepsilon}}^p - k_2 \rho.
$$

DDD (Part VII) supplies statistics that calibrate such laws.

### Multiscale coupling

| Scale | Method | Provides |
|-------|--------|----------|
| Continuum | FEM + crystal plasticity | Macro stress–strain |
| Mesoscale | DDD | Link statistics, forest hardening |
| Atomistic | MD | Core energies, cross-slip barriers |
| Electronic | DFT | Elastic constants, generalized stacking faults |

**Closing Part VI.** Continuum inelasticity is the macro language. When parameters must be measured—not fitted—we descend to Parts VII–IX.
