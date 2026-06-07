## 3.2 Elliptic problems: Poisson and elasticity

### Poisson equation

The model elliptic problem on domain $\Omega$ with boundary $\partial\Omega$:

$$
-\Delta u = f \quad \text{in } \Omega, \qquad u = 0 \quad \text{on } \partial\Omega.
$$

Weak form (from Section 2.6): find $u \in H_0^1(\Omega)$ with

$$
\int_\Omega \nabla u \cdot \nabla v \, d\Omega = \int_\Omega f v \, d\Omega \quad \forall v \in H_0^1(\Omega).
$$

Variable coefficient $-\nabla\cdot(k\nabla u) = f$ models heterogeneous conductivity or orthotropic stiffness in a scalar reduction.

### Linear elasticity

Small-strain elasticity seeks displacement $\mathbf{u} : \Omega \to \mathbb{R}^d$ with

$$
-\nabla \cdot \boldsymbol{\sigma} = \mathbf{f}, \qquad
\boldsymbol{\sigma} = \mathbb{C} : \boldsymbol{\varepsilon}, \qquad
\boldsymbol{\varepsilon} = \tfrac{1}{2}(\nabla \mathbf{u} + \nabla \mathbf{u}^T).
$$

For isotropic material,

$$
\boldsymbol{\sigma} = \lambda (\nabla\cdot\mathbf{u})\mathbf{I} + 2\mu \boldsymbol{\varepsilon},
$$

with Lamé parameters $\lambda, \mu$ from Young's modulus $E$ and Poisson ratio $\nu$.

The weak form uses the **symmetric gradient** and integrates by parts:

$$
\int_\Omega \boldsymbol{\sigma}(\mathbf{u}) : \boldsymbol{\varepsilon}(\mathbf{v}) \, d\Omega = \int_\Omega \mathbf{f} \cdot \mathbf{v} \, d\Omega + \int_{\Gamma_N} \mathbf{t} \cdot \mathbf{v} \, d\Gamma
$$

for all test displacements $\mathbf{v}$ vanishing on Dirichlet boundary $\Gamma_D$.

### Energy viewpoint

Elliptic operators are often **symmetric and coercive**—they minimize an energy functional. FEM for elasticity is not an ad hoc mesh trick; it is Ritz–Galerkin minimization of potential energy on a finite-dimensional subspace.

**Takeaway.** The copper wire in its elastic range is an elliptic BVP. Part IV discretizes exactly this structure.
