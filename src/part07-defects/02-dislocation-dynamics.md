# Dislocation Dynamics and Strain Hardening

When metal yields, dislocations multiply and tangle. **Dislocation dynamics (DDD)** tracks their motion and interactions — the mesoscale engine of strain hardening. Pull a copper wire beyond its elastic limit and the stress–strain curve bends upward not because the lattice stiffens, but because an evolving **forest** of dislocation lines impedes further slip. DDD is how we simulate that forest without resolving every atom.

## From elasticity to line defects

In Part VI, equilibrium satisfied a virtual work equation with smooth displacement fields. Dislocations introduce **topological** content: the displacement field is multi-valued, and the Burgers vector \(\mathbf{b}\) quantifies the jump. DDD replaces the singular continuum field with a **discrete network** of line segments, each carrying \(\mathbf{b}\) and a line direction \(\boldsymbol{\xi}\).

The long-range elastic stress from a segment is computed via **isotropic or anisotropic elasticity** (often precomputed Green's functions). Short-range **core** interactions — when segments pass within ~1–5 nm — require empirical rules or tables from molecular dynamics. The mesoscale model lives in the gap: elastic everywhere else, phenomenological at the core.

## Peach–Köhler forces and mobility

Each dislocation segment experiences a **Peach–Köhler** force per unit length:

\[
\mathbf{f} = (\boldsymbol{\sigma} \cdot \mathbf{b}) \times \boldsymbol{\xi},
\]

where \(\boldsymbol{\sigma}\) is the local stress tensor (external load plus stress from all other segments). The segment velocity \(\mathbf{v}\) follows a **mobility law**:

\[
\mathbf{v} = M(\boldsymbol{\sigma}, \mathbf{b}, \boldsymbol{\xi}, T)\, \mathbf{f},
\]

where \(M\) may be anisotropic and thermally activated. In fcc crystals, screw dislocations on {111} planes glide under resolved shear stress; **cross-slip** onto other {111} planes enables recovery and affects hardening at elevated temperature.

Mobility parameters for copper are fit to MD simulations or experiments. A DDD simulation is only as credible as its mobility table — another instance of the ladder: fine scale informs coarse scale.

## Discrete dislocation dynamics algorithms

Each dislocation is a curve (or network of segments) in an elastic medium. Time integration proceeds:

1. Compute stress field at each segment from superposition (direct summation, **fast multipole**, or precomputed influence matrices).
2. Evaluate Peach–Köhler forces.
3. Update segment positions via mobility laws.
4. Handle **topology changes**: annihilation when opposite segments meet, junction formation when segments intersect, Frank–Read source multiplication when pinned segments bow out.

Open-source frameworks such as [OpenDiS](https://github.com/OpenDiS/OpenDiS) and ParaDiS implement these algorithms at scale — enabling simulations of work hardening in single crystals and polycrystals. Typical simulations track \(10^3\)–\(10^6\) segments over strain intervals that would take years in full MD, at computational cost orders of magnitude lower than atomistic resolution of the same volume.

For the copper wire, a representative **single-crystal slip** simulation might impose shear at constant strain rate and record how dislocation density and flow stress co-evolve — output that feeds crystal plasticity constitutive laws used in polycrystal FEM.

## Taylor hardening and dislocation density

Classical models relate flow stress to total dislocation density \(\rho\):

\[
\tau = \alpha \mu b \sqrt{\rho},
\]

known as **Taylor hardening**. Here \(\mu\) is shear modulus, \(b\) is Burgers vector magnitude, and \(\alpha \approx 0.3\) is an empirical constant. The square-root scaling arises from treating other dislocations as random obstacles whose stress fields superpose incoherently.

During deformation, **storage** (multiplication at sources, junction formation) competes with **recovery** (annihilation, cross-slip, dynamic recovery at high temperature). The net evolution

\[
\frac{d\rho}{d\gamma} = k_1 \sqrt{\rho} - k_2 \rho
\]

(with strain \(\gamma\)) produces the familiar hardening then saturation shape. Parameters \(k_1, k_2\) depend on temperature, strain rate, and crystal structure — DDD extracts them from first-principles mesoscale physics rather than curve fitting alone.

For copper at room temperature, initial yield corresponds to \(\rho \sim 10^{10}\) m\(^{-2}\) (as-received); cold work can push \(\rho\) toward \(10^{15}\) m\(^{-2}\) before saturation effects dominate.

## Link statistics: beyond scalar density

Taylor's \(\sqrt{\rho}\) law uses a **scalar** measure of defect content. Recent work on **link statistics** asks a finer question: how do dislocation lines form **connected networks** during loading, and how does network **topology** — loop sizes, junction connectivity, line-length distribution — co-evolve with stress?

A **link** is a continuous segment between two nodes (junctions or endpoints). Its length distribution \(P(\ell)\), mean link length \(\bar{\ell}\), and network connectivity affect hardening in ways \(\rho\) alone cannot capture. Long links glide freely; short links in dense tangles contribute disproportionately to obstacle strength.

The author's research on [link statistics during strain hardening](https://doi.org/10.1016/j.jmps.2026.106533) sits at this interface: using large-scale DDD to extract statistical laws that continuum models can adopt as **internal state variables** beyond scalar dislocation density. For copper wire, where conductivity depends on defect scattering, link-length statistics may correlate with both mechanical strength and electrical resistivity — a reminder that mesoscale structure carries multiple property footprints.

## Frank–Read sources and multiplication

When a pinned dislocation segment bows under stress, it may spontaneously double: each bowed half-loop expands and closes, leaving two loops and regenerating the pinned segment — a **Frank–Read source**. Multiplication is the exponential engine of work hardening: a few initial dislocations become a forest.

The critical condition for bow-out balances line tension \(T \sim \mu b^2\) against applied stress. DDD captures this geometry explicitly; continuum models approximate it through a **source density** term in the \(\rho\) evolution equation.

In drawn copper wire, pre-existing dislocation sources from prior processing determine the initial hardening rate. DDD sensitivity to initial microstructure mirrors experimental batch-to-batch variability — another reason mesoscale simulation complements macroscale testing.

## Boundary conditions and finite domains

Infinite-medium Green's functions simplify bulk single-crystal studies. Real wires have **surfaces** where dislocations can **escape** (reducing \(\rho\) and softening) or **pile up** (raising local stress and potentially nucleating cracks). Image stress methods or finite-domain elastic solvers enforce traction-free or periodic boundary conditions on bounded volumes.

Coupling DDD to continuum FEM — passing dislocation density or back stress as internal variables — is an active research area. The wire's surface is not merely a geometric constraint; it is a **sink and source** for line defects.

## Coupling scales

| Scale | Method | State variable | Output to next scale |
|-------|--------|----------------|----------------------|
| DFT / MD | Core structure, \(\gamma_{\text{sf}}\), mobility | Atomic positions | Segment rules, \(M(\boldsymbol{\sigma})\) |
| DDD | Line network | Segment coordinates, \(\rho\), link stats | Hardening law, texture drivers |
| Crystal plasticity FEM | Slip systems | Slip rates, \(\rho\) (internal) | Polycrystal texture, anisotropic flow |
| Continuum FEM | Homogenized \(\mathbb{C}\), J2 | Stress, strain | Engineering design, wire sag |
| CFD (if heated) | Navier–Stokes | Velocity, temperature | Thermal softening input |

Machine learning accelerates the FEM step: graph neural networks on polycrystal meshes learn stress fields from microstructure — but still need DDD or experiments for training data at the mesoscale. Surrogates do not remove the ladder; they climb it faster.

## Strain-rate and temperature effects

Copper wire experiments run at strain rates \(\dot\varepsilon \sim 10^{-3}\)–\(10^{-1}\) s\(^{-1}\); DDD can access similar rates in stress-controlled tests. MD often exceeds \(10^7\) s\(^{-1}\), requiring extrapolation or **strain-rate sensitivity** parameters in mobility:

\[
v \propto \exp\!\left(-\frac{\Delta G(\tau)}{k_B T}\right),
\]

with activation free energy \(\Delta G\) decreasing under stress — thermally activated glide.

Temperature raises recovery rates (cross-slip, climb via vacancies). Annealing simulations couple DDD to vacancy diffusion models: dislocations climb when vacancies arrive at jogs. Wire conductivity recovery during anneal is partly **dislocation annihilation** — mesoscale structure relaxing toward lower \(\rho\).

## Comparison to continuum hardening models

| Model | Captures | Omits |
|-------|----------|-------|
| Isotropic J2 + Voce hardening | Macro \(\sigma\)–\(\varepsilon\) curve | Texture, anisotropy, Bauschinger |
| Crystal plasticity | Slip system activity, texture | Individual dislocation topology |
| DDD | Line geometry, junctions, link stats | Fast core reactions, chemistry |
| MD | Core, nucleation | Time/length scale of wire |

Calibration path: DDD → extract \( \tau(\gamma), \dot\rho(\gamma), \bar\ell(\gamma) \) → fit crystal plasticity or simplified J2 internal variables → FEM of wire. Each hop loses detail but gains domain size.

## Validation and limitations

DDD validates against:

- **TEM measurements** of dislocation structures post-mortem
- **In situ diffraction** during loading (pattern evolution)
- **MD** on small volumes with matching boundary conditions
- **Macroscopic stress–strain curves** when homogenized

Limitations include:

- **Core physics** approximated, not resolved
- **Short-range reactions** (junction types, cross-slip rates) empirically parameterized
- **Phonon drag** and **solute pinning** require extensions for alloyed or high-temperature copper
- **Polycrystal** DDD with full grain-boundary physics remains expensive

Unvalidated DDD is animated elasticity with pretty lines. Convergence studies on segment length and time step — analogous to FEM mesh refinement — are mandatory.

## OpenDiS workflow (conceptual)

A typical OpenDiS-style workflow for copper single-crystal shear:

1. **Initialize** a dislocation network (Frank–Read sources, random loops, or imported structure).
2. **Set material properties**: \(\mu\), \(b\), anisotropic elastic constants from DFT or experiment.
3. **Load** via applied strain rate or stress boundary conditions.
4. **Integrate** equations of motion for segments; remesh when curvature exceeds threshold.
5. **Post-process**: \(\rho(\gamma)\), \(\tau(\gamma)\), link-length distributions, dislocation velocity histograms.
6. **Export** hardening parameters to crystal plasticity or phenomenological flow laws.

The copper wire's cold-worked strength is, in part, a snapshot of step 4 frozen by manufacturing — DDD helps explain what that snapshot contains.

## Bridge

Dislocations are lines of missing registry in a lattice — but atoms still matter at the core. Molecular dynamics resolves core structure, stacking-fault energies, and mobility laws that DDD calibrates against. When bonds break at a crack tip in the wire, we leave line-defect elasticity entirely and descend to atoms — Part VIII.
