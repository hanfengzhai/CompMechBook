# Dislocation Dynamics and Strain Hardening

When metal yields, dislocations multiply and tangle. **Dislocation dynamics (DDD)** tracks their motion and interactions — the mesoscale engine of strain hardening. Pull a copper wire beyond its elastic limit and the stress–strain curve bends upward not because the lattice stiffens, but because an evolving **forest** of dislocation lines impedes further slip. DDD is how we simulate that forest without resolving every atom.

## Scene: the forest grows

Resume the tensile test where Part VI left it — load increasing, stress beyond yield. Inside the copper crystal, dislocation lines **glide** on {111} planes, **multiply** at Frank–Read sources, and **tangle** into a forest whose density rises with plastic strain. The load cell registers hardening: more stress needed for the next increment of stretch. No phenomenological law was typed in by hand; the curve bends because moving lines must push through a thickening forest.

A DDD simulation represents that forest as a network of segments, each feeling Peach–Köhler forces from external load and from every other segment. Timestep by timestep, the network evolves; the accumulated obstacle strength passes upward as a **hardening law** for crystal plasticity and, eventually, for continuum FEM. This scene is why Part VII exists: the wire's cold-drawn strength and its post-yield curve are **histories written in line defects**, not numbers we may choose arbitrarily at the continuum scale.

## Story so far (Parts I–VI → VII)

| Part | What the load cell saw | What Part VII now resolves |
|------|------------------------|---------------------------|
| I–IV | Linear elastic climb; \(\mathbf{K}\mathbf{u}=\mathbf{f}\) | Stiffness before yield; mesh habits unchanged |
| VI | J₂ plasticity; hardening modulus \(H\) | \(H\) hides in dislocation density \(\rho\) and link statistics |
| VII.1 | Taxonomy: point, line, surface defects | Which defect class carries each phenomenological knob |
| **VII.2 (here)** | Post-yield bend in **Act IV — Hardening** | Moving segments, not fitted Voce slopes alone |

The [prologue](../../prologue/00-many-scales.md) table promised that **upward export** at every scale carries units and pedigree; DDD's export is \(\tau(\gamma)\) and \(\rho(\gamma)\) — internal variables a crystal plasticity or FEM run can consume only if mobility and elastic constants from Parts VIII–IX are archived with convergence logs.

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

Taylor's \(\sqrt{\rho}\) law uses a **scalar** measure of defect content. Large-scale DDD campaigns show that **topology** — how line length is distributed across the network — carries information the square root alone does not.

A **link** is a continuous segment between two nodes (junctions or endpoints). Its length distribution \(P(\ell)\), mean link length \(\bar{\ell}\), and network connectivity affect hardening in ways \(\rho\) alone cannot capture. Long links glide freely; short links in dense tangles contribute disproportionately to obstacle strength.

Recent work on fcc metals under monotonic loading tracks **link length distributions** on each slip system: segments between junctions, classified as active or inactive under the current stress state. Two patterns emerge across more than a hundred DDD simulations:

- **Inactive slip systems** maintain link lengths that follow a **single exponential** distribution — a memoryless Poisson-like picture of random forest structure left behind when slip ceases on that system.
- **Active slip systems** evolve toward **double-exponential** distributions whose shape responds to resolved shear stress — consistent with a generalized Poisson process in which stress accelerates creation and annihilation of links on the active system.

For the copper wire, this distinction matters when cold work activates only a subset of slip systems while others remain latent. Exporting a single \(\rho\) to crystal plasticity collapses that structure. Exporting **link statistics** — mean link length \(\bar\ell\), active-system fractions, distribution shape parameters — gives constitutive models internal variables with clearer physical meaning than a fitted Voce law alone.

The author's research on [link statistics during strain hardening](https://doi.org/10.1016/j.jmps.2026.106533) sits at this interface: using large-scale DDD to extract statistical laws that continuum models can adopt as **internal state variables** beyond scalar dislocation density. For copper wire, where conductivity depends on defect scattering, link-length statistics may correlate with both mechanical strength and electrical resistivity — a reminder that mesoscale structure carries multiple property footprints.

The mesoscale lesson matches the book's ladder theme: DDD does not only produce \(\tau(\gamma)\); it produces **distributional** outputs that homogenization must decide whether to keep or discard.

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
| DDD | Line geometry, junctions, link-length statistics | Fast core reactions, chemistry |
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

## Worked example: Taylor hardening on drawn copper

Cold-drawn copper wire carries a dislocation forest frozen by manufacturing. A scalar Taylor estimate links that forest to the extra shear stress needed for further slip — the upward bend the load cell records after yield.

Take representative values for fcc Cu at room temperature:

| Quantity | Symbol | Value | Source rung |
|----------|--------|-------|-------------|
| Shear modulus | \(\mu\) | \(\approx 48\,\mathrm{GPa}\) | Experiment / DFT (Part IX) |
| Burgers vector magnitude | \(b\) | \(2.56\,\mathrm{\AA}\) | Crystal geometry |
| Taylor factor | \(\alpha\) | \(\approx 0.3\) | Literature / DDD calibration |
| Dislocation density (cold-drawn) | \(\rho\) | \(\sim 10^{14}\,\mathrm{m}^{-2}\) | TEM / DDD post-mortem |

Taylor hardening gives

\[
\Delta\tau = \alpha\,\mu\,b\,\sqrt{\rho}
\approx 0.3 \times 48\times10^9 \times 2.56\times10^{-10} \times \sqrt{10^{14}}
\approx 37\,\mathrm{MPa}.
\]

Converting to uniaxial stress with Taylor factor \(M \approx 3.06\) for fcc polycrystal texture gives \(\Delta\sigma \approx 110\,\mathrm{MPa}\) — order-of-magnitude consistent with the gap between annealed and half-hard copper yield strengths. Part VI's Voce law can fit the macroscopic curve; this calculation shows **where the fitted hardening modulus hides its physics**: in \(\sqrt{\rho}\), not in an arbitrary slope typed into the input deck.

A DDD run should reproduce \(\rho(\gamma)\) and \(\tau(\gamma)\) from which \(\alpha\) and the \(k_1, k_2\) evolution law are extracted — not merely match one stress–strain point.

## OpenDiS workflow

A reproducible OpenDiS-style workflow for copper single-crystal shear, modeled on the LAMMPS checklist in Part VIII:

1. **Initialize** a dislocation network — Frank–Read sources on one active {111}\(\langle 110\rangle\) system, or an imported post-mortem structure from TEM.
2. **Material table** — anisotropic elastic constants \(C_{ij}\) from DFT (Part IX) or experiment; Burgers vector and slip systems for fcc Cu; mobility law \(M(\tau, T)\) from MD (Part VIII) or literature tables.
3. **Load protocol** — constant strain rate \(\dot\gamma\) matched to the prologue tensile frame (\(\dot\varepsilon \sim 10^{-3}\)–\(10^{-1}\,\mathrm{s}^{-1}\)); temperature \(T\) fixed or coupled to Joule heating later.
4. **Integrate** — segment timestep constrained by mobility and remeshing when curvature exceeds threshold; log \(\rho\), \(\tau\), and link-length histograms each strain increment.
5. **Convergence** — refine segment length and timestep until \(\tau(\gamma)\) at fixed \(\gamma\) changes by less than 5%; compare inactive slip systems for single-exponential link statistics.
6. **Export** — write \(\tau(\gamma)\), \(d\rho/d\gamma\), \(\bar\ell(\gamma)\), and calibrated \(\alpha\) to a yaml or table for crystal plasticity (foreshadow Part VII.3 DAMASK handoff).

The copper wire's cold-worked strength is, in part, a snapshot of step 4 frozen by manufacturing — DDD explains what that snapshot contains.

## Reproducibility checklist

Before exporting DDD hardening laws to crystal plasticity or FEM:

1. Cite mobility table provenance (MD potential, temperature, strain rate).
2. Converge segment length and timestep on \(\tau(\gamma)\) at fixed plastic strain.
3. Document initial network topology (random loops vs. Frank–Read sources).
4. Compare \(\rho\) and link-length distributions to TEM or in situ diffraction when available.
5. Cross-check \(\alpha\) and \(C_{ij}\) against independent MD volumes on matching boundary conditions.
6. Archive input decks, material tables, and random seeds for network initialization.

Unvalidated DDD is animated elasticity with pretty lines — the same warning Part VIII repeats for unconverged MD and Part IX repeats for unconverged plane-wave cutoff.

## Concept map checkpoint (dislocation dynamics)

This chapter's four questions — scoped to **segment-network simulation**, not the full Part VII arc:

| Question | DDD answer (copper wire) |
|----------|--------------------------|
| What **object**? | Segment network with Burgers vector \(\mathbf{b}\) and line direction \(\boldsymbol{\xi}\) |
| What **structure**? | Peach–Köhler forces; mobility law \(M\); elastic superposition |
| What **theorem**? | Taylor \(\tau \propto \sqrt{\rho}\); link-statistics evolution on active slip systems |
| What **breaks**? | Core cutoff artifacts; wrong mobility; scalar \(\rho\) collapsing texture |

The load cell's post-yield bend is not a fitted Voce slope alone — it is a forest whose density and link statistics DDD can measure. The **full Part VII** checkpoint — taxonomy through crystal plasticity handoff — closes in [VII.3](03-polycrystal-and-fem-handoff.md). Parts VIII–IX supply the mobility and elastic constants this chapter consumes.

## Bridge

Single-crystal DDD explains how lines move, multiply, and harden a crystal — but the copper wire is polycrystalline and structural models speak crystal plasticity and FEM, not segment networks alone. The next chapter follows how DDD statistics export upward to constitutive laws and where Peierls barriers and grain boundaries still demand finer-scale input.

| What VII.2 simulated | What [VII.3](03-polycrystal-and-fem-handoff.md) must homogenize |
|------------------------|----------------------------------------------------------------|
| Segment network on one slip system | Texture and grain orientation across thousands of crystals |
| \(\tau(\gamma)\), \(\rho(\gamma)\), link-length histograms | Internal state variables on a crystal plasticity mesh |
| Mobility \(M(\tau,T)\) from MD tables | Peierls thresholds and grain-boundary barriers |
| OpenDiS export yaml for one crystal | DAMASK / FEM handoff for the full wire spool |

Return to the prologue's **Act IV — Hardening**: the load cell curve bent upward after yield because lines multiplied and tangled — DDD made that forest visible as moving segments. Part VI's J₂ plasticity fitted the bend with a scalar hardening modulus \(H\); this chapter showed where \(H\) hides its physics in \(\rho\) and link statistics. [VII.3](03-polycrystal-and-fem-handoff.md) closes the mesoscale arc by asking how those statistics survive **drawing dies and grain boundaries** — the organizational scale the cold-drawn wire on the bench actually has.

| DDD input | Typical source in the book | What breaks if pedigree is missing |
|-----------|---------------------------|-----------------------------------|
| Elastic constants \(C_{ij}\) | Part VI continuum or DFT export (Part IX) | Wrong image forces on segments |
| Mobility \(M(\tau,T)\) | MD at 300–600 K (Part VIII.2) | Spurious forest evolution rates |
| Core cutoff radius | MD core structure (Part VIII.1) | Artificial junction reactions |
| Initial \(\rho\) | Cold-drawn microstructure / TEM stats | Wrong hardening slope on the load cell |

Parts VIII–IX supply the mobility and elastic constants this chapter consumed; VII.3 is where DDD stops being a single-crystal movie and becomes **input for the same FEM mesh Part IV taught us to assemble**. Turn the page when OpenDiS converges on one orientation but the wire's macroscopic hardening still disagrees with experiment — that is the signal that polycrystal texture, not segment timestep, is the missing physics.
