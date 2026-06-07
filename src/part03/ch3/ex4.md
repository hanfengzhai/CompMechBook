## 3.4 Boundary conditions and energy estimates

### Types of boundary conditions

| Name | Condition | FEM treatment |
|------|-----------|---------------|
| Dirichlet (essential) | $u = g$ on $\Gamma_D$ | Strongly imposed on trial space |
| Neumann (natural) | $\mathbf{n}\cdot(k\nabla u) = h$ | Appears in $\ell(v)$ boundary integral |
| Robin | $\mathbf{n}\cdot(k\nabla u) + \alpha u = \beta$ | Boundary mass/stiffness contribution |

Essential conditions must be **admissible** in the trial space ($\gamma u = g$). Natural conditions need not be—approximate solutions satisfy them only weakly, improving with mesh refinement.

### Energy estimates

For coercive $a(\cdot,\cdot)$,

$$
\alpha \|u\|_V^2 \le a(u,u) = \ell(u) \le \|\ell\|_{V'} \|u\|_V,
$$

hence $\|u\|_V \le \alpha^{-1}\|\ell\|_{V'}$. This **a priori** bound survives discretization with constants depending on mesh geometry—**Céa's lemma** in Part IV.

### Multiphysics coupling

Thermal stress couples heat (parabolic) to elasticity (elliptic) through eigenstrain $\boldsymbol{\varepsilon}^{\text{th}} = \alpha_{\text{CTE}} \Delta T \,\mathbf{I}$. Fluid–structure interaction couples Navier–Stokes to elasticity through interface traction. Each field has its own PDE character; monolithic or partitioned coupling strategies mirror the operator splitting used in time.

**Closing Part III.** We now have the continuum equations and the weak forms that make them computable. Part IV chooses finite-dimensional subspaces and assembles matrices; Part V addresses conservation laws where fluxes, not energies, are primary.
