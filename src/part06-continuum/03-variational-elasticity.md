# Variational Elasticity and Nonlinear Extensions

Static equilibrium of an elastic body is equivalent to minimizing total potential energy — or finding a saddle point when constraints appear. This is where continuum theory and FEM meet on equal footing.

## Principle of minimum potential energy

Among kinematically admissible displacements,

\[
\Pi(\mathbf{u}) = \int_\Omega \psi(\boldsymbol{\varepsilon}(\mathbf{u}))\, d\Omega - \int_\Omega \mathbf{f}\cdot\mathbf{u} \, d\Omega - \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{u} \, dS
\]

is minimized at equilibrium. For linear elasticity, \(\psi = \tfrac{1}{2}\boldsymbol{\varepsilon}:\mathbb{C}:\boldsymbol{\varepsilon}\) and \(\Pi\) is quadratic.

## Weak form = first variation

Setting \(\delta\Pi = 0\) for arbitrary admissible \(\delta\mathbf{u}\) yields the virtual work equation implemented in FEM. **Galerkin** discretization is **Rayleigh–Ritz** on \(\Pi\).

## Nonlinear FEM path

For hyperelastic materials:

1. **Load stepping**: apply load increment \(\Delta\lambda\)
2. **Newton iteration**: solve \(\mathbf{K}_T \Delta\mathbf{u} = \mathbf{R}\) where \(\mathbf{R}\) is residual of weak form
3. **Consistent tangent**: \(\mathbf{K}_T = \partial \mathbf{R}/\partial \mathbf{u}\) for quadratic convergence

Geometric nonlinearity (\(\mathbf{F}\) not ≈ \(\mathbf{I}\)) and material nonlinearity (plasticity, damage) compose in the same framework. The author's [nonlinear FEA notes](https://hanfengzhai.github.io/file/NonlinFEA_note.pdf) document this pipeline for hyperelastic and inelastic problems.

## Contact and constraints

Contact introduces inequality constraints (no penetration) — variational inequalities. Penalty, augmented Lagrangian, and mortar methods weakly enforce contact conditions on interfaces. Each adds structure to the global system beyond sparse symmetric positive definite matrices.

## When continuum breaks down

Singularities at crack tips, dislocation cores, and grain boundaries signal that \(\boldsymbol{\varepsilon}\) is not square-integrable in the classical sense. Regularization (phase-field fracture), enriched bases (XFEM), or **descent to defect-scale models** (Part VII) becomes necessary.

## Bridge

Defects are where the continuum picture admits its limitations — and where mesoscale models take over.
