## 6.1 Elasticity and beyond

### Hooke's law (recap)

Small-strain isotropic elasticity:

$$
\boldsymbol{\sigma} = \lambda (\mathrm{tr}\,\boldsymbol{\varepsilon})\mathbf{I} + 2\mu\boldsymbol{\varepsilon}.
$$

Hyperelastic formulations use strain energy $W(\boldsymbol{\varepsilon})$ for finite strains—essential for rubber, soft tissue, and large deformations of metals before yield.

### Yield and plastic flow

**J₂ plasticity** (von Mises) introduces yield function $f = \|\boldsymbol{s}\| - \sqrt{2/3}\,\sigma_y \le 0$ on deviatoric stress $\boldsymbol{s}$. Associated flow gives plastic strain increment proportional to $\partial f / \partial \boldsymbol{\sigma}$.

Return-mapping algorithms (radial return in J₂) integrate constitutive updates at Gauss points inside a nonlinear FE loop—local plasticity, global Newton on $K_{\text{tangent}}$.

### Finite strain and objective rates

Large rotations require objective stress rates (Jaumann, Green–Naghdi). Nonlinear FEA tracks deformation gradient $\mathbf{F}$, right Cauchy–Green $\mathbf{C} = \mathbf{F}^T\mathbf{F}$, and work conjugate stress measures.

**Takeaway.** FEM carries the constitutive law at integration points. The wire yields when $\sigma_y$ is reached—continuum phenomenology before we count dislocations.
