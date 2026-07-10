# Stress, Balance Laws, and Constitutive Relations

Kinematics describes how bodies move and deform. **Balance laws** relate stress to body forces and acceleration. **Constitutive relations** connect stress to strain — the part continuum mechanics cannot derive from geometry alone; it must be measured, modeled, or computed from atomistic methods (Parts VII–IX).

Part IV assembled \(\int \boldsymbol{\varepsilon}(\mathbf{u}):\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{v})\). Part V balanced fluxes of momentum. This chapter explains what \(\boldsymbol{\sigma}\) and \(\mathbb{C}\) mean, where the equilibrium equation comes from, and how copper, air, and plastic metal differ at the constitutive level.

Part I's \(\mathbf{K}\mathbf{u}=\mathbf{f}\) was always a discrete force balance; [VI.1](01-kinematics.md) named the deformation that produces strain. This chapter completes the mechanical vocabulary: the **Cauchy stress tensor** whose weak divergence Part IV's assembly approximates, and the **constitutive map** \(\mathbb{C}\) that Parts VII–IX will trace from dislocation forests and electron density back to the numbers typed into the mesh script.

## Scene: three balances on one wire

The tensile frame from Part I is still running, but the operator has raised the current. Three instruments watch the same copper cylinder:

- A **load cell** reads axial force \(T\) — mechanical equilibrium in the solid.
- A **thermocouple** at the grip reads temperature — thermal boundary data for conduction inside the wire.
- A **thermal camera** shows a hot stripe along the narrowest cross-section — Joule heating balanced by conduction and convection to the surrounding air.

None of these measurements belongs to a single code. Part IV's FEM mesh carries mechanical equilibrium; Part V's FVM mesh carries enthalpy flux in the cooling air; Part VI names the **Cauchy stress** \(\boldsymbol{\sigma}\) and **Fourier flux** \(\mathbf{q} = -\kappa \nabla T\) that tie the two discretizations together at the wire surface. This scene is continuum mechanics at the engineering scale: not one PDE in isolation, but **balance laws** — momentum, energy, charge — coupled through **constitutive relations** that say how copper responds to strain and temperature. The chapter below makes those balances precise enough to export moduli upward from DFT and hardening laws downward from DDD.

## Copper wire: one specimen, three balance laws

Take the cold-drawn copper wire under tension \(T\), carrying current \(I\) and cooled by air:

1. **Mechanical:** static equilibrium \(\nabla\cdot\boldsymbol{\sigma} + \mathbf{f} = \mathbf{0}\) with \(\boldsymbol{\sigma}\mathbf{n} = T\mathbf{e}_x\) on the loaded end and traction-free lateral surfaces. Part IV's mesh approximates this weak form.
2. **Thermal:** steady \(\nabla\cdot(\kappa\nabla T) + \dot{q}_{\text{Joule}} = 0\) with \(\dot{q}_{\text{Joule}} = \rho_e | \mathbf{J}|^2 / \sigma_e\). Part V's FVM balances enthalpy flux in the surrounding air; Robin coupling at the wire surface sets the heat transfer coefficient.
3. **Constitutive:** for small strain and room temperature, \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) with isotropic \(\mathbb{C}(E, \nu)\). Thermal strain adds \(\boldsymbol{\varepsilon}_{\text{th}} = \alpha (T - T_0)\mathbf{I}\); the total strain in virtual work is \(\boldsymbol{\varepsilon}(\mathbf{u}) - \boldsymbol{\varepsilon}_{\text{th}}\).

None of these three problems is independent. Temperature shifts \(E\) and yield stress; tension shifts electrical resistance and Joule heating. Multiphysics is not a software feature — it is the same balance laws with coupled constitutive closures.

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

## Concept map checkpoint (balance laws)

Parts I–V built the same four-question discipline the Functional Analysis Notes use — object, structure, theorem, failure mode. At the balance-law scale the answers split across the three instruments in the opening scene:

| Question | Mechanical (solid wire) | Thermal (Joule heating) | Constitutive (copper) |
|----------|-------------------------|-------------------------|------------------------|
| **Object** | Displacement \(\mathbf{u}\), Cauchy stress \(\boldsymbol{\sigma}\) | Temperature \(T\) | Strain \(\boldsymbol{\varepsilon}\), stress \(\boldsymbol{\sigma}\) |
| **Structure** | Balance of momentum; symmetry of \(\boldsymbol{\sigma}\) | Energy balance; Fourier law | Hooke's law \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) |
| **Theorem** | Virtual work ↔ equilibrium (Lax–Milgram for linear elasticity) | Steady diffusion with Robin BC at the fluid interface | Positive-definite \(\mathbb{C}\) ⇒ elliptic operator |
| **Breaks if missing** | Rigid-body modes, singular \(\mathbf{K}\) | Wrong heat flux at the air boundary | Plasticity, anisotropy, temperature-dependent moduli |

**Part I recap:** the wire's FEM solve is still \(\mathbf{K}\mathbf{u}=\mathbf{f}\). The entries of \(\mathbf{K}\) are integrals of \(\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{N}_I):\boldsymbol{\varepsilon}(\mathbf{N}_J)\) — the continuum tensors above, projected onto shape functions. Part VI.4 closes the part-level checkpoint with hyperelasticity, yield, and the doorway to dislocations.

## Bridge

Balance laws, stress, and constitutive relations complete the **field vocabulary** Part IV and Part V approximated on meshes and control volumes — but the copper wire's elastic response is not finished with naming tensors. Static equilibrium is also a **minimum principle**.

| What balance laws supplied | What variational elasticity (next chapter) adds |
|------------------------------|------------------------------------------------|
| Momentum balance \(\nabla\cdot\boldsymbol{\sigma}+\mathbf{f}=\mathbf{0}\) | Total potential energy \(\Pi[\mathbf{u}]\) whose stationarity is equilibrium |
| Cauchy stress and symmetry from angular balance | Virtual work as the weak form Part III derived — now with physical \(\boldsymbol{\sigma}\) |
| Hooke's law \(\boldsymbol{\sigma}=\mathbb{C}:\boldsymbol{\varepsilon}\) | Why Part IV's \(\mathbf{K}\) integrates \(\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{N}_I):\boldsymbol{\varepsilon}(\mathbf{N}_J)\) |
| Thermal balance and Fourier law for Joule heating | Coupled energy functional when temperature feeds moduli (preview) |

The virtual work equation in this chapter is the same balance Part IV assembled — continuum mechanics **names** the tensors the FEM code already integrated. The load cell's linear elastic climb (prologue **Act III**) measures stress derived here; when the curve bends (**Act IV**), smooth fields and isotropic \(\mathbb{C}\) stop being enough.

Prologue **Act II — Warming** re-enters here as the thermal partner of the mechanical balance: Joule heating supplies a volumetric source in the energy equation; the Robin condition at the air interface is the flux handshake Part V's Navier–Stokes chapter will compute. Parts IV and V discretized those balances; Part VI states them as field laws before Part VII asks what microstructure hides inside \(\mathbb{C}\) and \(\sigma_{y0}\).

[VI.3](03-variational-elasticity.md) makes the energy statement explicit, closes the upward arc from Part I's spring network, and previews when hyperelasticity and yield force a descent to Part VII. Turn the page when \(\boldsymbol{\sigma}=\mathbb{C}:\boldsymbol{\varepsilon}\) feels like a constitutive plug-in rather than the consequence of minimizing elastic energy — variational elasticity reunifies the story.
