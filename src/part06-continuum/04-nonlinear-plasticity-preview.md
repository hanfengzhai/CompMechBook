# Nonlinear Elasticity and the Onset of Plasticity

The copper wire from the prologue was never purely elastic. Cold drawing pushed it past yield; Joule heating during current flow changes its modulus slightly with temperature; a notch at a clamp concentrates stress until something gives — slip, void nucleation, or fracture. Parts I–VI built the language of **small-strain linear elasticity**: a quadratic energy, a symmetric bilinear form, a sparse stiffness matrix. That language is the indispensable first approximation. It is also where the continuum story **stops being sufficient** unless we extend it.

This chapter is not a full treatise on plasticity theory — that would require its own book. It is the **bridge** between variational elasticity and the defect mechanics of Part VII: what changes when displacements are large, when energy is no longer quadratic, and when history matters.

## Scene: the curve bends, the model must follow

Return to the force–displacement trace from Part I: linear climb, then yield knee, then hardening plateau. Linear elasticity explains only the first segment. Large strain, necking, and path-dependent hardening live outside the quadratic energy landscape — yet the same wire, same grips, same experiment. This chapter names what changes when the tangent stiffness stops being constant and points toward Part VII's defects as the microscale reason for the knee.

## When linear elasticity breaks down

Linear elasticity assumes:

1. **Small strains**: \(\|\boldsymbol{\varepsilon}\| \ll 1\), so \(\boldsymbol{\sigma} = \mathbb{C}:\boldsymbol{\varepsilon}\) is accurate.
2. **Path independence**: the strain energy \(\psi(\boldsymbol{\varepsilon})\) depends only on the current strain, not on how the material arrived there.
3. **Smooth fields**: no singularities sharper than what weak forms tolerate on a mesh.

The drawn copper wire violates all three at different locations:

- **Bulk of the gauge section**: small strain, nearly path-independent unloading — linear FEM is fine for elastic springback estimates.
- **Necking region after overload**: large strains, geometric nonlinearity mandatory.
- **Work-hardened interior**: path-dependent — the current stress depends on prior plastic strain, not on \(\boldsymbol{\varepsilon}\) alone.
- **Crack tip or notch root**: stress singularity in linear theory; mesh refinement without model change only moves the blow-up to finer elements.

Recognizing which regime we are in is the first task of nonlinear computational mechanics.

## Geometric nonlinearity: the finite deformation gradient

When the wire stretches appreciably, the **deformation gradient** \(\mathbf{F} = \partial \mathbf{x}/\partial \mathbf{X}\) departs from \(\mathbf{I}\). The **Green–Lagrange strain**

\[
\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I})
\]

measures stretch and shear in a way that remains valid for large rotations — unlike the small-strain tensor \(\boldsymbol{\varepsilon} = \mathrm{sym}(\nabla\mathbf{u})\), which treats \(\nabla\mathbf{u}\) as infinitesimal.

Hyperelastic materials define a **strain energy density** \(\Psi(\mathbf{F})\) or \(\Psi(\mathbf{E})\). Equilibrium follows from minimizing total potential energy — the same variational instinct as Part VI, Chapter 3, but on a nonlinear manifold of deformations:

\[
\Pi(\mathbf{u}) = \int_{\Omega_0} \Psi(\mathbf{F})\, d\Omega_0 - \int_{\Omega_0} \mathbf{b}\cdot\mathbf{u}\, d\Omega_0 - \int_{\Gamma_N} \mathbf{t}\cdot\mathbf{u}\, dS.
\]

The **first Piola–Kirchhoff stress** \(\mathbf{P} = \partial\Psi/\partial\mathbf{F}\) and its symmetric counterpart enter weak forms on the reference configuration \(\Omega_0\). Finite element implementations (Abaqus `*STATIC`, FEniCS with nonlinear forms) solve the **discrete nonlinear system** by Newton iteration:

\[
\mathbf{K}_T(\mathbf{U}^{(k)})\,\Delta\mathbf{U} = \mathbf{R}(\mathbf{U}^{(k)}),
\]

where \(\mathbf{K}_T\) is the **consistent tangent stiffness** — the Jacobian of the residual with respect to nodal displacements — and \(\mathbf{R}\) is the out-of-balance force vector.

### Incremental loading and the copper wire

Pull the wire in tension with displacement control. Each load increment solves a nonlinear equilibrium. The force–displacement curve bends downward after ultimate tensile strength — **geometric softening** from necking, not yet plasticity. A purely hyperelastic Neo-Hookean model captures large elastic stretches of rubber; copper departs earlier because **plastic slip** begins at yield.

The Newton loop is the nonlinear FEM analog of the SCF cycle in DFT (Part IX): iterate until residuals fall below tolerance, using a Jacobian that must be **consistent** with the constitutive update for quadratic convergence.

## Material nonlinearity: from Hooke to flow rules

Beyond yield, copper does not return to its original microstructure when unloaded. A **plastic strain** \(\boldsymbol{\varepsilon}^p\) accumulates; elastic strain is \(\boldsymbol{\varepsilon}^e = \boldsymbol{\varepsilon} - \boldsymbol{\varepsilon}^p\). Stress depends on \(\boldsymbol{\varepsilon}^e\) through Hooke's law, but \(\boldsymbol{\varepsilon}^p\) evolves with history.

### Von Mises yield and J₂ plasticity

For metals, the **von Mises yield criterion** is

\[
f = \|\mathbf{s}\| - \sqrt{\tfrac{2}{3}}\,\sigma_y = 0,
\]

where \(\mathbf{s} = \boldsymbol{\sigma} - \tfrac{1}{3}(\mathrm{tr}\,\boldsymbol{\sigma})\mathbf{I}\) is the deviatoric stress and \(\sigma_y\) is yield stress. Inside the yield surface (\(f < 0\)), response is elastic; on the surface, plastic flow may occur.

**Associated plastic flow** postulates

\[
\dot{\boldsymbol{\varepsilon}}^p = \dot{\lambda}\,\frac{\partial f}{\partial \boldsymbol{\sigma}},
\]

with \(\dot{\lambda} \ge 0\) and **Kuhn–Tucker complementarity** conditions enforcing loading/unloading logic. This is constrained optimization at each Gauss point — the return-mapping algorithm projects trial elastic stress back to the yield surface in each time increment.

### Isotropic hardening and cold work

Cold-drawn copper has elevated \(\sigma_y\) because dislocation density increased — an **internal state variable** \(\alpha\) (or equivalent) tracks accumulated plastic strain:

\[
\sigma_y = \sigma_{y0} + H\,\alpha, \qquad \dot{\alpha} = \|\dot{\boldsymbol{\varepsilon}}^p\|.
\]

This **isotropic hardening** law is phenomenological. Part VII explains the mesoscale mechanism: dislocation multiplication and entanglement. Part VIII explains atomistic slip. Part IX supplies cohesive energies that bound how much work hardening can cost energetically.

Without hardening, J₂ plasticity predicts perfect plastic flow at constant stress — useful for idealized forming, not for the drawn wire's load–extension curve.

## The finite element plasticity loop

At each load increment and each quadrature point, the nonlinear FEM algorithm:

1. **Predict** trial stress from elastic guess: \(\boldsymbol{\sigma}^{tr} = \mathbb{C}:(\boldsymbol{\varepsilon} - \boldsymbol{\varepsilon}^p_n)\).
2. **Check** yield: if \(f(\boldsymbol{\sigma}^{tr}) \le 0\), elastic step; else plastic correction.
3. **Return-map** to yield surface, updating \(\boldsymbol{\varepsilon}^p_{n+1}\) and consistent tangent \(\mathbb{C}^{ep}\).
4. **Assemble** global \(\mathbf{K}_T\) from element contributions using \(\mathbb{C}^{ep}\), not \(\mathbb{C}\).
5. **Solve** Newton system; repeat until equilibrium.

The **consistent algorithmic tangent** is essential. Using only the elastic modulus \(\mathbb{C}\) in the global Jacobian when the material is yielding slows Newton convergence to a crawl or causes divergence — the same lesson as using an approximate Hessian in optimization.

### Finite elements and the weak form revisited

Plasticity does not abandon virtual work. It replaces the elastic energy functional with an incremental variational structure (or a rate form) that is not globally minimizable — **dissipation** breaks pure energy minimization. The weak form becomes: find \(\mathbf{u}\) and internal variables such that momentum balance holds with \(\boldsymbol{\sigma}(\boldsymbol{\varepsilon}^e, \text{history})\).

This is where Parts II–IV pay off: the function spaces, assembly loops, and solver infrastructure are unchanged. The constitutive update at Gauss points is what changes — exactly as DFT changes the energy functional but keeps the SCF linear algebra pattern.

## Where continuum plasticity ends

Even sophisticated crystal plasticity FEM — one slip system per Gauss point, hardening from internal variables — does not resolve **individual dislocations**. It homogenizes their effect into \(\sigma_y(\alpha)\) and texture evolution. That is appropriate for wire bending at millimeter scale; it fails when:

- **Dislocation spacing** approaches the mesh size (single-crystal micro-pillar compression).
- **Crack tips** require atomic bond breaking (not continuum damage alone).
- **Grain boundaries** emit dislocations in patterns that mean-field hardening cannot capture.

The continuum plasticity chapter in a standard course stops at phenomenological laws. Our ladder continues downward because the copper wire's strength **is** dislocation physics written into \(\sigma_y\).

| Phenomenon | Continuum J₂ / crystal plasticity | Finer model |
|------------|-----------------------------------|-------------|
| Yield stress elevation after drawing | Fit \(H\), \(\sigma_{y0}\) | DDD \(\rho \rightarrow \tau(\gamma)\) |
| Texture after rolling | CPFEM with slip systems | Polycrystal MD or EBSD-informed RVE |
| Notch root failure | Damage mechanics, XFEM | MD + cohesive zone |
| Rate dependence | Viscoplastic \(\dot{\varepsilon}^p(\sigma)\) | Phonon drag, MD thermostats |

The table is not a menu of unrelated codes. It is the same question — what state variable carries history upward? — with different answers at different scales.

## Coupling back to Parts IV and V

**Part IV** assembled linear \(\mathbf{K}\). Nonlinear solid mechanics replaces it with \(\mathbf{K}_T\) that changes every iteration and every increment. Mesh refinement studies from Part IV still apply: h-adaptivity near notches, p-refinement for smooth bulk fields, error indicators based on energy norms — now on incremental work conjugates rather than quadratic energy alone.

**Part V** solved hyperbolic conservation laws with Riemann fluxes. Plastic shock waves in solids — rarefaction and shock fronts in impact — couple hyperbolic structure with yielding. Split schemes treat advection and plastic source separately; operator splitting errors mirror the multiscale coupling issues of the epilogue.

The copper wire heated by current couples **all three**: nonlinear elasticity (thermal expansion), plasticity (if clamped plastically), and CFD (Part V) for air cooling. Multiphysics is not a separate subject; it is the natural state of the wire.

## Preview: what Part VII supplies

Part VII introduces **dislocations** as explicit mesoscale objects — lines with Burgers vector, Peach–Köhler forces, mobility laws. Dislocation dynamics (DDD) does not replace J₂ plasticity; it **calibrates** it:

- Forest hardening \(\Delta\tau \propto \sqrt{\rho}\) from Taylor links to \(\sigma_y\).
- Back stress from pile-ups enters kinematic hardening tensors in advanced constitutive models.
- Link-length statistics from DDD simulations (OpenDiS, ParaDiS) inform what phenomenological laws miss.

When we later fit an EAM potential in Part VIII or compute stacking-fault energy in Part IX, we are closing the loop: electronic structure sets the energy landscape; MD sets mobility and cross-slip; DDD sets hardening; FEM sets structural response. Nonlinear continuum mechanics is the **lowest rung that still speaks the language of stress and strain tensors** familiar to structural engineers.

## Concept map checkpoint (Part VI)

Part VI named the fields that Parts IV and V already approximated on meshes. Before descending to defects, the four questions summarize the continuum scale:

| Question | Part VI answer (copper wire) |
|----------|------------------------------|
| What **object**? | Deformation \(\mathbf{F}\), strain measures, Cauchy stress \(\boldsymbol{\sigma}\) |
| What **structure**? | Balance laws; hyperelastic energy \(\psi\); yield surface and flow rules |
| What **theorem**? | Virtual work equivalence; polyconvexity (existence in hyperelasticity); Drucker's stability postulate |
| What **breaks**? | Crack tips and dislocation cores (singular gradients); hardening without mesoscale physics |

The copper wire under rising load follows this arc: Part IV's mesh computes \(\mathbf{u}\); Part VI explains that \(\mathbf{u}\) minimizes energy until yield; this chapter adds Newton–Raphson and \(J_2\) plasticity when the load cell curve bends. When the mesh is refined but the hardening law is wrong, the fault is not discretization — it is **constitutive physics** that lives at the dislocation scale. Part VII supplies that physics.

## Bridge to Part VII

Linear and nonlinear elasticity — geometric and material — exhaust what a **continuum field** can say before its assumptions fail at defects. The copper wire's cold-worked strength is not in \(\mathbb{C}\); it is in the dislocation forest frozen by manufacturing. Part VII names those defects, simulates their motion, and exports the hardening laws that make nonlinear FEM honest.

Return to the prologue's **Act IV — Hardening**: the load cell curve bent upward after yield, and Part VI's J₂ preview fitted that bend with phenomenological \(H\) and \(\sigma_{y0}\). Those parameters worked in a return-mapping loop — but they were **placeholders**. When the mesh is refined and the hardening law is still wrong, the fault is not discretization; it is **constitutive physics** that lives at the mesoscale. That is the signal to descend.

| What Part VI gave | What Part VII must supply |
|-------------------|---------------------------|
| Isotropic hardening \(\sigma_y = \sigma_{y0} + H\alpha\) | Forest density \(\rho\) and Taylor \(\tau \propto \sqrt{\rho}\) |
| Yield knee on the force–displacement trace | Slip lines on the wire surface; Burgers circuits that fail to close |
| Cutoff-regularized singularities at notches | Line defects with Peach–Köhler forces and mobility laws |
| Fitted \(H\) from macroscopic calibration | DDD link statistics exportable to crystal plasticity |

Part VII opens with the same specimen at the yield point: polished copper showing faint **slip lines** on {111} planes — the visible trace of dislocation motion that J₂ plasticity homogenized into a scalar \(\alpha\). Remember also that the drawn wire is not a single crystal: cold drawing leaves a **polycrystal with grain boundaries** that homogenized \(H\) cannot see — the spool of wire in [VII.3](03-polycrystal-and-fem-handoff.md) is the same specimen at a finer organizational scale. [VII.1](01-defect-taxonomy.md) names the defect catalog; [VII.2](02-dislocation-dynamics.md) follows the forest as it moves, multiplies, and tangles under load. Turn the page when the mesh is fine enough but the physics still wrong — that is the hinge between continuum and mesoscale.
