# Stress, Balance Laws, and Constitutive Relations

Kinematics describes how bodies move and deform. **Balance laws** relate stress to body forces and acceleration. **Constitutive relations** connect stress to strain — the part continuum mechanics cannot derive from geometry alone; it must be measured, modeled, or computed from atomistic methods (Parts VII–IX).

Part IV assembled \(\int \boldsymbol{\varepsilon}(\mathbf{u}):\mathbb{C}:\boldsymbol{\varepsilon}(\mathbf{v})\). Part V balanced fluxes of momentum. This chapter explains what \(\boldsymbol{\sigma}\) and \(\mathbb{C}\) mean, where the equilibrium equation comes from, and how copper, air, and plastic metal differ at the constitutive level.

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

### Scale-boundary handshake: DFT elastic tensor to FEM material card

Part IX computes single-crystal elastic constants \(C_{11}, C_{12}, C_{44}\) in GPa from strained DFT cells. Part IV's `*MATERIAL` card expects isotropic \(E\) and \(\nu\) (or a full anisotropic \(\mathbb{C}_{\text{Voigt}}\)). The wire on the bench is **polycrystalline** — so the handshake has two rungs: **crystal → effective isotropic moduli**, then **effective moduli → assembled \(\mathbf{K}\)**.

**Step 1 — DFT to Voigt matrix (Part IX).** From [IX.3](../part09-dft/03-dft-workflows.md), a converged fcc Cu elastic run might yield (PBE, illustrative):

| Constant | Value (GPa) | Role |
|----------|-------------|------|
| \(C_{11}\) | 168 | Axial stiffness along \(\langle 100\rangle\) |
| \(C_{12}\) | 122 | Transverse coupling |
| \(C_{44}\) | 76 | Shear on \(\{111\}\) planes |

Voigt matrix (6×6) in GPa:

\[
\mathbb{C}_{\text{Voigt}} = \begin{bmatrix}
C_{11} & C_{12} & C_{12} & 0 & 0 & 0 \\
C_{12} & C_{11} & C_{12} & 0 & 0 & 0 \\
C_{12} & C_{12} & C_{11} & 0 & 0 & 0 \\
0 & 0 & 0 & C_{44} & 0 & 0 \\
0 & 0 & 0 & 0 & C_{44} & 0 \\
0 & 0 & 0 & 0 & 0 & C_{44}
\end{bmatrix}.
\]

**Step 2 — polycrystal homogenization (Part VI).** For a texture-free random polycrystal, **Voigt** (strain average) and **Reuss** (stress average) bound the effective moduli:

\[
E_{\text{Voigt}} = \frac{(C_{11}+2C_{12})(C_{11}-C_{12}+3C_{44})}{C_{11}+C_{12}+C_{44}}, \qquad
\nu_{\text{Voigt}} = \frac{C_{11}+4C_{12}-2C_{44}}{2(C_{11}+C_{12}+2C_{44})}.
\]

With the numbers above, \(E_{\text{Voigt}} \approx 140\,\text{GPa}\), \(\nu_{\text{Voigt}} \approx 0.34\) — stiffer than the **120 GPa** often used for cold-drawn wire because (i) DFT is 0 K and defect-free, (ii) drawing introduces texture and dislocation hardening that lower effective stiffness in tension, (iii) the lab card may cite handbook room-temperature polycrystal data rather than quantum single-crystal bounds.

| Source | \(E\) (GPa) | \(\nu\) | Wire context |
|--------|-------------|---------|--------------|
| DFT Voigt (0 K, perfect crystal) | \(\sim 140\) | \(\sim 0.34\) | Upper bound; audit trail from `cu.elastic/` |
| MD NPT at 300 K (Part VIII) | \(\sim 110\)–\(130\) | \(\sim 0.33\)–\(0.35\) | Finite-T anharmonicity |
| Handbook / tensile test (drawn wire) | \(\sim 120\) | \(\sim 0.34\) | What the load cell and FEM deck often use |
| Reuss lower bound | \(\sim 130\) | — | Softer than Voigt; bracket for texture sensitivity |

**Step 3 — FEM material card (Part IV).** Map \((E, \nu)\) to Lamé parameters for the 1D bar Lab act in [I.1](../part01-linear-algebra/01-vectors-matrices.md):

\[
\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}, \qquad \mu = \frac{E}{2(1+\nu)}, \qquad k_{\text{bar}} = \frac{EA}{L}.
\]

For axisymmetric or full 3D meshes, the same \((E,\nu)\) populate \(\mathbb{C}_{\text{Voigt}}\) in the isotropic form — Part IV's B-matrix contraction \(\mathbf{B}^T \mathbb{C} \mathbf{B}\) is the continuum handshake executed at every Gauss point.

**Acceptance test.** Before trusting Act III's linear elastic climb on the load cell:

1. Archive the DFT `README.md` with functional, cutoff, and converged \(C_{ij}\) ([IX.3 Lab act](../part09-dft/03-dft-workflows.md#lab-act-archive-the-foundation-run-before-the-wire-scale-solve-act-vi--foundation)).
2. Compute \(E_{\text{Voigt}}\) and \(E_{\text{Reuss}}\); confirm the FEM value \(E = 120\,\text{GPa}\) lies between them or document why drawing texture shifts it outside the bracket.
3. Run the three-node bar from Part I with both \(E = 140\) and \(E = 120\,\text{GPa}\); the 17% stiffness gap predicts a 17% force gap at the same grip displacement — the same sensitivity Part I.1's condition-number table warned about for material contrast.

**What breaks without the handshake.** A wire FEM model that imports \(E = 120\,\text{GPa}\) from a handbook without citing whether it came from DFT Voigt averaging, MD at 300 K, or a tensile test on cold-drawn stock carries **silent temperature, texture, and defect assumptions**. When DDD (Part VII) or MD (Part VIII) export moduli that disagree with the FEM card by 15%, the fault is usually missing homogenization — not a bug in OpenDiS or LAMMPS. This section is the engineering-scale counterpart of Part VIII's phonon handshake: two discretizations of the same copper lattice must agree on the observable the load cell measures before coarser models inherit the numbers.

### Scale-boundary handshake: thermal expansion coefficient \(\alpha\) (DFT phonons → MD NPT → FEM thermal strain)

The elastic handshake above sets \(E\) and \(\nu\) on the FEM card. **Act II — Warming** also needs the **coefficient of thermal expansion** \(\alpha\) that converts Joule-heated temperature rise into thermal strain \(\varepsilon_{\text{th}} = \alpha \Delta T\) and, with fixed grips, into compressive stress \(\sigma_{\text{th}} \approx E \alpha \Delta T\). That number appears in every coupled thermoelastic deck — yet teams often import \(\alpha = 17 \times 10^{-6}\,\text{K}^{-1}\) from a handbook without tracing it to the same DFT foundation run that supplied \(C_{ij}\).

**Step 1 — DFT phonon Grüneisen route (Part IX).** From converged bulk Cu with `ph.x` output, extract the **Grüneisen parameter** \(\gamma\) relating phonon frequency shifts to volume strain, or compute \(\alpha\) directly from the quasiharmonic approximation: run `vc-relax` at several volumes (or temperatures via phonon free energy), fit the equilibrium lattice parameter \(a(T)\), and differentiate:

\[
\alpha = \frac{1}{a}\frac{da}{dT}\Big|_{P=0}.
\]

Typical PBE results for fcc Cu: \(\alpha \approx 15\)–\(18 \times 10^{-6}\,\text{K}^{-1}\) at 300 K (anharmonic corrections matter; 0 K DFT alone underestimates \(\alpha\)). Archive the phonon DOS and the \(a(T)\) table beside `cu.elastic/` — the epilogue's **Handshake 3** sensitivity analysis assumes this pedigree.

**Step 2 — MD NPT validation (Part VIII).** Equilibrate a bulk Cu supercell in **NPT** at 300 K and 600 K (Joule-heated wire mid-span order-of-magnitude). Measure \(\alpha_{\text{MD}} = \frac{1}{L}\frac{dL}{dT}\) from the mean box length in production runs:

| Source | \(\alpha\) (\(10^{-6}\,\text{K}^{-1}\)) | Temperature | Wire context |
|--------|------------------------------------------|-------------|--------------|
| Experiment (polycrystal Cu) | \(\sim 16.5\)–\(17.0\) | 300 K | Handbook default |
| DFT quasiharmonic (PBE) | \(\sim 15\)–\(18\) | 300 K | Foundation run export |
| MD NPT with Mishin EAM | \(\sim 16\)–\(19\) | 300–600 K | Finite-T anharmonicity |
| FEM deck (often uncited) | \(\sim 17\) | 300 K | Act II thermal strain load |

**Step 3 — FEM thermal strain (Part IV).** Map \(\alpha\) into the coupled block system from [I.4](../part01-linear-algebra/04-toward-infinity.md): thermal load vector \(\mathbf{f}_u^{\text{th}} = \int \alpha E (T - T_{\text{ref}}) \mathbf{B}^T \mathbf{1}\, d\Omega\) on the wire mesh. For the Lab act in this chapter (\(\Delta T \approx 35\,^\circ\text{C}\), fixed grips):

\[
\varepsilon_{\text{th}} = \alpha \Delta T \approx 17 \times 10^{-6} \times 35 \approx 6 \times 10^{-4}, \qquad
\sigma_{\text{th}} \approx E \varepsilon_{\text{th}} \approx 120 \times 10^9 \times 6 \times 10^{-4} \approx 72\,\text{MPa}.
\]

A **10% error in \(\alpha\)** shifts \(\sigma_{\text{th}}\) by \(\sim 7\,\text{MPa}\) — comparable to the 6.4 MPa tensile stress from a 50 N load on the 1 mm wire. When the load cell drifts during Act II without applied force change, the first suspect is missing or inconsistent thermal expansion, not a bad sensor.

**Acceptance test** (archive beside the elastic handshake checklist):

1. DFT phonon or quasiharmonic \(\alpha\) within 10% of experiment at 300 K.
2. MD NPT \(\alpha\) within 10% of DFT at the same potential used for production runs.
3. FEM `*EXPANSION` or equivalent card cites the same \(\alpha\) with temperature reference \(T_{\text{ref}}\) matching the pre-heating state (Act I mounting temperature).

**What breaks without the handshake.** Importing handbook \(\alpha\) while using DFT-derived \(E\) mixes pedigree levels: the thermal stress scale is wrong even when elastic stiffness is right. Fixed-grip multiphysics runs then over- or under-predict load-cell drift during Joule heating — the epilogue ranks this among the **dominant sensitivities** when mechanical strain is small compared to thermal strain. The phonon handshake in Part VIII validates the potential; this handshake validates the **thermal eigenstrain** that potential implies at finite temperature.

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

## Lab act: three instruments, one wire (Act II — Warming)

**Act II** is the moment the operator raises current through the mounted wire. Three instruments read three balance laws on the same specimen — mechanical, thermal, and constitutive — and Part VI is where those readings become tensors instead of dashboard numbers.

**Setup.** Copper cylinder: gauge length \(L = 0.5\,\text{m}\), diameter \(d = 1\,\text{mm}\), resistivity \(\rho_e \approx 1.7\times 10^{-8}\,\Omega\cdot\text{m}\), thermal conductivity \(\kappa \approx 400\,\text{W/(m·K)}\), Young's modulus \(E = 120\,\text{GPa}\), coefficient of thermal expansion \(\alpha \approx 17\times 10^{-6}\,\text{K}^{-1}\). Current \(I = 5\,\text{A}\); ambient air \(T_\infty = 25\,^\circ\text{C}\); heat transfer coefficient \(h \approx 10\,\text{W/(m}^2\cdot\text{K)}\) on the lateral surface.

**Step 1 — mechanical balance (load cell).** Before current, axial tension \(T\) gives \(\sigma_{xx} = T/A\) with \(A = \pi d^2/4\). The load cell reads force; Cauchy stress is the continuum name for that reading divided by area. Part IV's FEM mesh assembles the same equilibrium weak form this section wrote in tensor notation.

**Step 2 — thermal balance (thermocouple + camera).** Joule heating per unit volume is \(\dot{q} = \rho_e J^2 = \rho_e (I/A)^2 \approx 1.1\times 10^8\,\text{W/m}^3\). For a long thin wire in steady state with lateral convection, a lumped estimate gives mid-span excess temperature \(\Delta T \sim \dot{q} d / (4 h) \approx 30\)–\(40\,^\circ\text{C}\) — order-of-magnitude consistent with the hot stripe the thermal camera shows. The thermocouple at the grip reads boundary data; the 1D profile \(T(x)\) is what Part III's weak heat equation and Part V's FVM air mesh approximate on either side of the interface.

**Step 3 — constitutive coupling (why one code is not enough).** Thermal strain \(\varepsilon_{\text{th}} = \alpha \Delta T\) adds to mechanical strain. If the grips are fixed, \(\sigma_{xx} \approx E \alpha \Delta T \approx 60\)–\(80\,\text{MPa}\) of compressive thermal stress — enough to shift the load cell reading even without changing the applied end load. Multiphysics is this coupling: temperature from energy balance changes stress through Hooke's law; stress changes resistance and therefore Joule heating.

| Instrument | Balance law | Continuum object | Part that discretizes |
|------------|-------------|------------------|------------------------|
| Load cell | Momentum | Cauchy stress \(\boldsymbol{\sigma}\) | Part IV FEM |
| Thermocouple | Energy (boundary) | Temperature \(T\) | Part IV coupled / Part V FVM |
| Thermal camera | Energy (field) | Heat flux \(\mathbf{q} = -\kappa \nabla T\) | Part V FVM on air domain |

**Step 4 — export discipline.** Write down which quantities pass between codes: Robin BC \( - \kappa \partial T / \partial n = h(T - T_\infty)\) at the wire surface links Part IV's solid mesh to Part V's fluid mesh; \(\varepsilon_{\text{th}}(T)\) links the thermal solution back to mechanical equilibrium. This is the same upward/downward contract the epilogue will formalize — here at the engineering scale, before dislocations or atoms enter the story.

When the three instruments disagree (hot stripe but cold grip, or load cell drift without applied force change), the fault is usually **missing coupling**, not a bad sensor. That diagnostic habit survives every scale descent in Parts VII–IX.

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

[VI.3](03-variational-elasticity.md) makes the energy statement explicit, closes the upward arc from Part I's spring network, and previews when hyperelasticity and yield force a descent to Part VII. Turn the page when \(\boldsymbol{\sigma}=\mathbb{C}:\boldsymbol{\varepsilon}\) feels like a constitutive plug-in rather than the consequence of minimizing elastic energy — variational elasticity reunifies the story.
