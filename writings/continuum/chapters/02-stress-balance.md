# Stress, Balance Laws, and Constitutive Relations

Kinematics describes how bodies move and deform. **Balance laws** relate stress to body forces and acceleration. **Constitutive relations** connect stress to strain — the part continuum mechanics cannot derive from geometry alone; it must be measured, modeled, or computed from atomistic methods (Parts VII–IX).

Part IV assembled \(\int \boldsymbol{\varepsilon}(\mathbf{u}):\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{v})\). Part V balanced fluxes of momentum. This chapter explains what \(\boldsymbol{\sigma}\) and \(\mathbb{C}\) mean, where the equilibrium equation comes from, and how copper, air, and plastic metal differ at the constitutive level.

## Concept map checkpoint

The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) ask four questions at every scale change. At the continuum level they read:

| Question | Answer for this chapter |
|----------|---------------------------|
| What **object**? | Cauchy stress \(\boldsymbol{\sigma}\) — a symmetric tensor field, not a nodal vector |
| What **structure**? | Balance laws (momentum, mass, energy) plus constitutive closure |
| What **theorem**? | Virtual work equivalence: equilibrium \(\Leftrightarrow\) weak form tested against all admissible \(\mathbf{v}\) |
| What **breaks**? | Singular stress at notches; history-dependent yield without mesoscale state; wrong moduli from the wrong scale |

Keep this table in mind as we name the tensors Part IV already integrated.

## Cauchy stress and traction

**Cauchy stress** \(\boldsymbol{\sigma}(\mathbf{x}, t)\) is a symmetric second-order tensor mapping surface normals to traction vectors:

\[
\mathbf{t}(\mathbf{n}) = \boldsymbol{\sigma}\mathbf{n}.
\]

On a surface element with normal \(\mathbf{n}\), traction is the force per unit area exerted **by the material on the positive side of the surface** on the material on the negative side.

Symmetry \(\boldsymbol{\sigma} = \boldsymbol{\sigma}^T\) follows from balance of angular momentum in the absence of couple stresses. In 3D, six independent components; in plane stress, three.

For the copper wire under uniform tension \(T\), traction on a cut perpendicular to the axis is \(\mathbf{t} = T \mathbf{e}_x\) — uniform normal stress \(\sigma_{xx} = T\), other components zero (free lateral surfaces).

## Piola–Kirchhoff stress

FEM on the reference configuration uses **first Piola–Kirchhoff stress** \(\mathbf{P}\), defined so that reference surface traction relates to current force:

\[
\mathbf{P}\mathbf{N}\, dA_0 = \mathbf{t}\, dA.
\]

Relation to Cauchy stress:

\[
\mathbf{P} = J\,\boldsymbol{\sigma}\,\mathbf{F}^{-T}, \qquad \boldsymbol{\sigma} = \frac{1}{J}\mathbf{P}\mathbf{F}^T.
\]

**Second Piola–Kirchhoff stress** \(\mathbf{S} = \mathbf{F}^{-1}\mathbf{P}\) is symmetric and work-conjugate to Green–Lagrange strain — natural for hyperelastic energies \(\psi(\mathbf{E})\).

Static linear FEM typically uses Cauchy stress in the small-strain limit with \(\mathbf{F} \approx \mathbf{I}\); nonlinear hyperelastic FEM uses \(\mathbf{P}\) or \(\mathbf{S}\) on \(\Omega_0\).

## Conservation of mass

**Continuity equation**:

\[
\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{v}) = 0.
\]

In Lagrangian form on the reference configuration:

\[
\rho_0 = J \rho.
\]

Mass conservation is built into incompressible FVM and FEM via divergence-free velocity or \(J = 1\) constraints.

## Balance of linear momentum

**Cauchy's equation** in the current configuration:

\[
\nabla\cdot\boldsymbol{\sigma} + \mathbf{f} = \rho \frac{D\mathbf{v}}{Dt}.
\]

For static solids, \(\mathbf{v} = 0\) and the right-hand side vanishes:

\[
-\nabla\cdot\boldsymbol{\sigma} = \mathbf{f}.
\]

This is the strong form Part IV discretized. Body force \(\mathbf{f}\) includes gravity (\(\rho \mathbf{g}\)) and electromagnetic body forces in Joule-heated copper.

In reference configuration, balance becomes

\[
\nabla_0\cdot\mathbf{P} + \mathbf{f}_0 = 0 \quad \text{(static)},
\]

integrated over \(\Omega_0\) in nonlinear FEM.

## Balance of angular momentum

Without couple stresses, angular momentum balance implies \(\boldsymbol{\sigma} = \boldsymbol{\sigma}^T\). Micropolar and Cosserat theories add couple stress for materials with internal length scales — relevant at microscales (Part VII).

## Energy balance

**First law of thermodynamics** for a continuum:

\[
\rho \frac{De}{Dt} = \boldsymbol{\sigma}:\mathbf{D} + \rho r - \nabla\cdot\mathbf{q},
\]

where \(e\) is specific internal energy, \(r\) is heat supply, \(\mathbf{q}\) is heat flux. Mechanical power \(\boldsymbol{\sigma}:\mathbf{D}\) couples deformation to heating — negligible for slow copper wire loading, essential for high-strain-rate plasticity and shock physics.

Coupled thermoelasticity (Part IV, Chapter 4) uses simplified energy balance: heat equation with mechanical coupling, mechanical equilibrium with thermal eigenstrain.

## Constitutive relations: the closure problem

Balance laws involve \(\boldsymbol{\sigma}\) but do not specify it. **Constitutive laws** close the system by relating stress to kinematic and thermodynamic variables.

| Material class | Constitutive relation | Computational home |
|----------------|----------------------|-------------------|
| Linear elastic | \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) | Part IV FEM, symmetric \(\mathbf{K}\) |
| Hyperelastic | \(\mathbf{P} = \partial\psi/\partial\mathbf{F}\) | Nonlinear FEM, Newton loops |
| Newtonian fluid | \(\boldsymbol{\tau} = 2\mu\mathbf{D}\), \(\boldsymbol{\sigma} = -p\mathbf{I} + \boldsymbol{\tau}\) | Part V Navier–Stokes |
| Ideal gas | \(p = \rho R T\), \(e = c_v T\) | FVM Euler, Riemann solvers |
| Rate-independent plasticity | Yield \(f(\boldsymbol{\sigma}) \le 0\), flow rule | Return mapping, Part IV nonlinear |
| Viscoelastic | \(\boldsymbol{\sigma} = f(\text{history of }\boldsymbol{\varepsilon})\) | Internal variables, hereditary integrals |

The author's [elasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf) develop Hooke's law in tensor form, boundary value problems, and extensions to plasticity and fracture — the continuum backbone referenced throughout Part IV.

## Isotropic Hooke's law in detail

For isotropic linear elasticity,

\[
\boldsymbol{\sigma} = \lambda (\text{tr}\,\boldsymbol{\varepsilon})\mathbf{I} + 2\mu\boldsymbol{\varepsilon},
\]

or in Voigt notation for implementation:

\[
\begin{bmatrix} \sigma_{xx} \\ \sigma_{yy} \\ \sigma_{zz} \\ \sigma_{yz} \\ \sigma_{xz} \\ \sigma_{xy} \end{bmatrix} = \mathbb{C}_{\text{Voigt}} \begin{bmatrix} \varepsilon_{xx} \\ \varepsilon_{yy} \\ \varepsilon_{zz} \\ 2\varepsilon_{yz} \\ 2\varepsilon_{xz} \\ 2\varepsilon_{xy} \end{bmatrix}.
\]

Plane stress and plane strain modify \(\mathbb{C}\) by eliminating out-of-plane components algebraically — the reductions used in 2D FEM (Part IV, Chapter 4).

## Plasticity and inelasticity

Beyond elastic yield, copper **work-hardens**: dislocations multiply and impede further slip (Part VII). Phenomenological **J2 plasticity** uses

\[
f = \|\text{dev}(\boldsymbol{\sigma})\| - \sqrt{\tfrac{2}{3}} \sigma_y(\alpha) \le 0,
\]

with accumulated plastic strain \(\alpha\) and flow rule \(\dot{\boldsymbol{\varepsilon}}^p = \dot{\lambda}\,\partial f/\partial\boldsymbol{\sigma}\).

Computationally, plasticity is **return mapping** at quadrature points: elastic predictor, plastic corrector if yield violated. The consistent tangent modulates Newton convergence in nonlinear FEM — variational inequalities replace simple energy minimization.

## Fluid vs. solid: unified balance, split constitutive

Both fluids and solids satisfy conservation of mass and momentum. The split is constitutive:

- **Solid (elastic)**: stress depends on strain (or \(\mathbf{F}\)); history may matter through plasticity.
- **Fluid (Newtonian)**: stress depends on rate of deformation \(\mathbf{D}\); pressure enforces incompressibility.

At fluid–solid interfaces (copper wire in air), **kinematic continuity** (\(\mathbf{v}_{\text{fluid}} = \mathbf{v}_{\text{solid}}\) on the wetted surface) and **dynamic continuity** (traction balance \(\boldsymbol{\sigma}_{\text{solid}}\mathbf{n} = \boldsymbol{\sigma}_{\text{fluid}}\mathbf{n}\)) couple Part IV and Part V.

## Weak form as virtual work (connection to Part III)

Integrating static momentum balance against test function \(\mathbf{v}\) and integrating by parts yields Part III's virtual work equation:

\[
\int_\Omega \boldsymbol{\sigma} : \nabla \mathbf{v}\, d\Omega = \int_\Omega \mathbf{f}\cdot\mathbf{v}\, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{v}\, dS.
\]

Substituting \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{u})\) gives the bilinear form of linear elasticity. Continuum mechanics **is** the weak form before discretization — Part III derived it from PDEs; this chapter identifies the physical tensors.

## Boundary value problems

A complete solid mechanics problem specifies:

1. Domain \(\Omega\) (or \(\Omega_0\)) and geometry.
2. Constitutive law (\(\mathbb{C}\), or \(\psi(\mathbf{F})\)).
3. Body force \(\mathbf{f}\).
4. BCs: \(\mathbf{u} = \mathbf{u}_0\) on \(\Gamma_D\), \(\boldsymbol{\sigma}\mathbf{n} = \mathbf{t}\) on \(\Gamma_N\).

Well-posedness requires ellipticity of the operator (Lax–Milgram for linear elasticity) or coercivity of the energy in nonlinear settings. Ill-posed problems (insufficient constraints, soft mechanisms) produce singular \(\mathbf{K}\) in FEM.

## Worked example: one wire, three balance laws

Return to the copper wire from the prologue — diameter \(d = 1\,\text{mm}\), gauge length \(L = 50\,\text{mm}\), cold-drawn, carrying current \(I = 5\,\text{A}\) in still air. Three balance laws run in parallel; only the constitutive closure differs.

**Mechanical equilibrium (static).** In the gauge section, end traction \(T = F/A\) with \(A = \pi d^2/4\). For \(F = 10\,\text{N}\), \(T \approx 13\,\text{MPa}\) — well below bulk yield for annealed copper (\(\sigma_y \sim 70\,\text{MPa}\)) but not for heavily drawn wire (\(\sigma_y\) can exceed \(300\,\text{MPa}\)). Linear elasticity gives \(\varepsilon_{xx} = T/E\); with \(E = 120\,\text{GPa}\) (polycrystalline room-temperature value), \(\varepsilon_{xx} \approx 1.1 \times 10^{-4}\). Part IV's \(\mathbf{K}\mathbf{U}=\mathbf{F}\) is the discrete version of \(-\nabla\cdot\boldsymbol{\sigma}=\mathbf{0}\) with \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\).

**Thermal coupling.** Joule heating supplies volumetric rate \(\rho r = \eta J^2\) (electrical resistivity \(\eta\)). Steady conduction in the wire obeys \(-\nabla\cdot\mathbf{q} = \rho r\) with Fourier law \(\mathbf{q} = -k\nabla T\). The air-side boundary condition is not a fixed temperature: Part V's FVM supplies a convective flux \(q_w = h(T_w - T_\infty)\) from the Navier–Stokes solution around the cylinder. Mechanical equilibrium sees the temperature rise as **thermal eigenstrain** \(\boldsymbol{\varepsilon}^{\text{th}} = \alpha (T - T_0)\mathbf{I}\), which modifies \(\boldsymbol{\sigma} = \mathbb{C}:(\boldsymbol{\varepsilon} - \boldsymbol{\varepsilon}^{\text{th}})\). Two discretizations, one interface — the conjugate heat transfer loop from Part V, Chapter 4, is balance-law coupling in software.

**Where \(\mathbb{C}\) comes from.** The table above lists \(\mathbb{C}\) as a constitutive input. For copper at this scale, \(E\) and \(\nu\) are homogenized polycrystal averages. Part IX will show how DFT on a perfect lattice gives \(C_{ijkl}\) that reduce to these engineering constants after Voigt averaging; Part VII explains why drawn wire needs a **hardening law**, not a single \(\sigma_y\), because dislocation storage is missing from linear elasticity alone.

This example is deliberately multi-physics: it is the same specimen Part IV meshed, Part V cooled, and Part VI now interprets in tensor language. The narrative does not fork — the physics stacks.

## From balance law to matrix equation (Part I revisited)

The handoff from continuum to code is worth stating once in full. Static momentum balance tested against FEM shape functions \(\mathbf{N}_a\):

\[
\sum_b \left(\int_\Omega \mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{N}_a):\boldsymbol{\varepsilon}(\mathbf{N}_b)\, d\Omega\right) U_b = \int_\Omega \mathbf{f}\cdot\mathbf{N}_a\, d\Omega + \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{N}_a\, dS.
\]

The bracket is \(K_{ab}\); the right-hand side is \(F_a\). Part I taught \(\mathbf{K}\mathbf{u}=\mathbf{f}\); Part III derived the integral identity; Part IV assembled \(K_{ab}\); this chapter names \(\boldsymbol{\sigma}\) and \(\mathbb{C}\) inside the integral. Reading upward, the matrix is not a black box — it is a Galerkin projection of a balance law. Reading downward, every entry in \(\mathbb{C}\) eventually asks for a finer-scale origin.

## Bridge

Static equilibrium of an elastic body is equivalent to minimizing total potential energy — or finding a saddle point when incompressibility or contact constraints appear. The next chapter makes that variational statement explicit, traces the nonlinear FEM path, and explains when continuum theory itself admits defeat at crack tips and dislocation cores — the doorway to Part VII.
