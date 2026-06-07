## 3.1 Classification and well-posedness

### Second-order linear prototype

The general second-order linear PDE in two independent variables is

$$
a u_{xx} + 2b u_{xy} + c u_{yy} + \text{lower order} = 0.
$$

The discriminant $\Delta = b^2 - ac$ classifies the equation at each point:

| Type | Condition | Prototype | Physical example |
|------|-----------|-----------|------------------|
| Elliptic | $\Delta < 0$ | $-\Delta u = f$ | Equilibrium elasticity, steady heat |
| Parabolic | $\Delta = 0$ (one zero eigenvalue) | $u_t - \kappa \Delta u = 0$ | Transient diffusion |
| Hyperbolic | $\Delta > 0$ | $u_{tt} - c^2 \Delta u = 0$ | Wave propagation |

### Well-posedness (Hadamard)

A problem is **well-posed** if:

1. A solution exists
2. The solution is unique
3. The solution depends continuously on data

Ill-posed problems (inverse identification without regularization, naive continuation past bifurcation) blow up in computation even when formally stated. Well-posedness in the right function space is what Lax–Milgram and energy estimates supply for elliptic problems.

### Nonlinearity

Real mechanics is nonlinear: $-\nabla \cdot \boldsymbol{\sigma}(\boldsymbol{\varepsilon})$ with nonlinear $\boldsymbol{\sigma}$, convective terms $\mathbf{u}\cdot\nabla\mathbf{u}$ in Navier–Stokes, hyperelastic strain energy. Linear classification still guides local stability and preconditioning; global solution uses Newton iterations on sequences of linearized PDEs.

**Takeaway.** Know the PDE character before choosing FEM vs FVM vs explicit time stepping.
