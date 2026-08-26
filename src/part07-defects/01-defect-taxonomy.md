# Point, Line, and Surface Defects

Perfect crystals exist in textbooks. Real materials carry **defects** — localized disruptions of order that control strength, diffusion, conductivity, and optical properties. A copper wire drawn through dies and annealed for electrical use is a catalog of defect physics: dislocation forests from cold work, vacancy clusters from thermal recovery, grain boundaries from polycrystalline structure, and oxide surfaces from environmental exposure.

Continuum elasticity in Part VI describes smooth displacement fields. Defects are where that smoothness fails — and where mesoscale models begin.

## Closing the arc from VI.4 (plasticity complete, defects enter) {#defect-taxonomy-opening-hinge-plasticity-to-forest}

If you walked through [VI.4's Bridge](../part06-continuum/04-nonlinear-plasticity-preview.md#bridge-to-part-vii) and the [Lab act: return mapping on the load cell knee](../part06-continuum/04-nonlinear-plasticity-preview.md#lab-act-return-mapping-on-the-load-cell-knee-act-iv-hardening), the copper wire has J₂ plasticity, isotropic hardening \(\sigma_y = \sigma_{y0} + H\alpha\), and Perzyna rate sensitivity — but **Act IV** still bends because cold drawing stored a forest the continuum cannot see. [Part VII opening — Chapter guide](../part07-defects/00-opening.md#chapter-guide) lists VII.1 as the rung where Burgers geometry enters; [VI.4's opening hinge](../part06-continuum/04-nonlinear-plasticity-preview.md#plasticity-opening-hinge-energy-to-yield) replaced path-independent \(\Pi[\mathbf{u}]\) with internal variable \(\alpha\); this chapter is the **first rung inside Part VII** — defect taxonomy before Peach–Köhler motion or DDD time integration.

| VI.4 (J₂ plasticity on the wire) | VII.1 (defect taxonomy on the wire) |
|----------------------------------|-------------------------------------|
| Scalar internal variable \(\alpha\); fitted \(H\), \(\sigma_{y0}\) | Burgers vector \(\mathbf{b}\); point, line, surface defect catalog |
| Return mapping: elastic predictor, plastic corrector at Gauss points | Burgers circuit closure failure: \(\mathbf{b} = \oint d\mathbf{u} \neq \mathbf{0}\) |
| Isotropic hardening law homogenizes forest statistics | Dislocation density \(\rho\); Taylor \(\tau \propto \sqrt{\rho}\) preview |
| Slip invisible on polished surface until yield knee | Slip lines on {111} planes trace line-defect motion |
| Cutoff at notch root regularizes singularity | Core structure where linear elasticity breaks (\(r < 1\) nm) |
| Perzyna \((N,\eta)\) and rate sensitivity \(m\) | Thermally activated kink-pair nucleation preview → Part VIII MD |

VI.4 answered *how* to fit the load cell knee with phenomenological plasticity; this chapter asks *what* cold drawing wrote into the wire before the test — vacancies from annealing, grain boundaries from polycrystal structure, dislocation lines whose density makes drawn copper stronger than annealed copper. When the [preface continuity hinge](../preface.md#continuity-hinges-ascent-descent) lists **ascent → descent** at [VI.4 intermission](../part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins), and [Part VII opening](../part07-defects/00-opening.md#ascent-hinge-midpoint-and-twin-ladders) replays the twin-ladder thermal pedigree, this section is where scalar \(\alpha\) yields to Burgers geometry for the first time since Part VI began.

The specimen on the bench has not moved since [VI.4's Scene](../part06-continuum/04-nonlinear-plasticity-preview.md#scene-the-curve-bends-the-model-must-follow). The load cell still records force versus grip displacement; return mapping still fits \(H\) at one strain rate. What changes on this page is **naming** the objects J₂ homogenized: edge and screw segments, stacking faults, grain boundaries — the catalog cold drawing stored before Act IV began.

## Scene: the wire yields

Part VI ended with J₂ plasticity and isotropic hardening — \(\sigma_y = \sigma_{y0} + H\alpha\) — parameters that made the return-mapping loop converge but did not explain **where** \(H\) and \(\sigma_{y0}\) came from. The force–displacement curve from Part I finally bends at the same yield knee those parameters were fitted to mimic. The load cell still reads force, but the slope drops: the wire is **plastic**. A polished surface that was mirror-smooth now shows faint **slip lines** — traces of dislocation motion on {111} planes. Continuum FEM with isotropic elasticity predicted a straight elastic segment forever; the experiment crossed a yield point that lives not in \(\mathbb{C}\) alone but in a **forest of line defects** stored by cold drawing.

Zoom in mentally. Where Part VI saw a smooth displacement field \(\mathbf{u}(\mathbf{x})\), the mesoscale sees **Burgers circuits that fail to close** — each failure quantified by a vector \(\mathbf{b}\) and carried along a curve through the crystal. Vacancies from prior annealing cycles sit at point defects; grain boundaries from polycrystal structure block slip; the drawn wire's extra strength is not magic stiffness in \(\mathbf{K}\) but **dislocation density** \(\rho\) that Part VI's J₂ preview fitted with a single hardening modulus \(H\). This scene is the handoff from continuum to mesoscale: the same copper cylinder, now read as a catalog of defects rather than a homogeneous bar. The taxonomy below names what broke the smooth picture.

## Taxonomy by dimension

Defects are classified by the dimension of the region they disrupt relative to the perfect lattice:

| Defect | Dimension | Example | Mechanical role |
|--------|-----------|---------|-----------------|
| Vacancy | 0 (point) | Missing atom | Diffusion, creep, resistivity |
| Interstitial | 0 (point) | Extra atom in void or crowdion | Hardening, swelling, radiation damage |
| Substitutional | 0 (point) | Foreign atom on lattice site | Solid-solution strengthening |
| Dislocation | 1 (line) | Extra half-plane of atoms | Plasticity, work hardening |
| Stacking fault | 2 (surface) | Wrong stacking sequence (hcp in fcc) | Twinning, partial dislocations |
| Grain boundary | 2 (surface) | Misoriented crystals meeting | Hall–Petch strengthening, fracture paths |
| Phase boundary | 2 (surface) | Different crystal structure | Transformations, composites |
| Void / crack | 3 (volume) | Missing material region | Nucleation, failure |

The author's [defects notes](https://hanfengzhai.github.io/file/defects_notes.pdf) develop thermodynamics and mechanics of these structures — the conceptual bridge between atomistic lattices and continuum plasticity.

**Point defects** break local stoichiometry but not long-range orientational order. A vacancy in copper lowers the local coordination number from twelve to eleven; the surrounding atoms relax inward, storing elastic energy on the order of 1–2 eV per defect. At finite temperature, vacancies migrate by thermally activated hops — the atomistic basis of **diffusion** and **creep** at high homologous temperature.

**Line defects** (dislocations) break translational symmetry along a curve. They are the primary carriers of **plastic strain** in crystalline metals: when the copper wire yields, it does so by dislocation motion, not by breaking every bond at once.

**Surface defects** (grain boundaries, stacking faults, free surfaces) break order across a two-dimensional manifold. A drawn wire's **texture** — preferred grain orientation along the draw direction — is a polycrystalline consequence of boundary-mediated deformation.

## Burgers vector and closure failure

The fundamental measure of a dislocation is the **Burgers vector** \(\mathbf{b}\), defined by the closure failure of a Burgers circuit:

\[
\mathbf{b} = \oint_\mathcal{C} d\mathbf{u},
\]

where \(\mathcal{C}\) is a path encircling the dislocation core and \(\mathbf{u}\) is the elastic displacement field. For a perfect crystal, \(\mathbf{b} = \mathbf{0}\). For a dislocation, \(\mathbf{b}\) equals one lattice translation vector (or a fraction thereof for partial dislocations).

In fcc copper, the shortest perfect dislocations have \(|\mathbf{b}| = a/\sqrt{2}\) along \(\langle 110 \rangle\) directions, where \(a \approx 3.61\) Å is the lattice constant. **Edge** dislocations have \(\mathbf{b}\) perpendicular to the line direction; **screw** dislocations have \(\mathbf{b}\) parallel. Real dislocations are mixed — neither pure edge nor pure screw.

## Elastic fields and singularities

Linear isotropic elasticity gives closed-form stress fields around straight dislocations. For a screw dislocation along the \(z\)-axis,

\[
u_z = \frac{b}{2\pi}\theta, \qquad \sigma_{xz} = -\frac{\mu b}{2\pi}\frac{y}{r^2}, \qquad \sigma_{yz} = \frac{\mu b}{2\pi}\frac{x}{r^2},
\]

where \(\theta\) is the polar angle and \(\mu\) is the shear modulus. The displacement winds by \(b\) around a circuit enclosing the core — a **singularity** at \(r = 0\) where linear elasticity breaks down.

Stress decays as \(1/r\) — slow compared to point defects (\(\sim 1/r^3\)). Dislocations **interact over long ranges**, making many-body simulations essential. Two parallel screw dislocations of the same sign repel; opposite signs attract and may **annihilate** when they meet — a mesoscale event that reduces stored energy and softens the material locally.

Within a continuum FEM model of the copper wire, these singular fields are invisible. The wire mesh sees homogenized moduli and yield criteria. Part VII exists because that homogenization is not arbitrary: it must reflect the physics of defects we deliberately omit.

## Grain boundaries and the Hall–Petch relation

Polycrystalline copper wire contains **grain boundaries** — interfaces where crystals of different orientation meet. Boundaries impede dislocation motion: a dislocation approaching a boundary may transmit, reflect, or be absorbed, depending on misorientation angle and boundary structure.

Empirically, the yield stress increases with decreasing grain size \(d\):

\[
\sigma_y = \sigma_0 + \frac{k}{\sqrt{d}},
\]

the **Hall–Petch** relation. The inverse-square-root scaling reflects the increased boundary area per unit volume that dislocations must traverse. Nanocrystalline copper is strong but brittle — boundaries dominate plasticity when grains shrink below roughly 100 nm.

High-angle boundaries are disordered; low-angle boundaries can be modeled as arrays of dislocations (**Read–Shockley** model). The mesoscale picture connects naturally to the line-defect dynamics of the next chapter.

## Stacking faults and partial dislocations

Fcc copper has a close-packed stacking sequence …ABCABC…. A **stacking fault** inserts an extra plane (…ABC**B**ABC…) or removes one, creating a thin hcp-like layer. The **stacking-fault energy** \(\gamma_{\text{sf}}\) (J/m²) sets the energy cost of such a fault.

Low \(\gamma_{\text{sf}}\) favors **partial dislocations** — dislocations whose Burgers vector is a fraction of a lattice vector, trailing a stacking fault ribbon between them. In copper, \(\gamma_{\text{sf}}\) is relatively high (~45 mJ/m²), so perfect dislocations dominate at room temperature. In other fcc metals (Ag, Al), partials and twinning play larger roles.

When the wire undergoes severe cold work, **deformation twins** may appear as lamellae bounded by coherent twin boundaries — another two-dimensional defect with distinct mechanical and electrical consequences (twin boundaries scatter electrons differently than random high-angle boundaries).

## Thermodynamics: formation energy and chemical potential

Each defect type carries a **formation energy** \(E_f\): the cost to introduce the defect into an otherwise perfect crystal. Vacancies in copper have \(E_f^v \approx 1.3\) eV; interstitials cost more because they crowd neighbors.

At temperature \(T\), the equilibrium vacancy concentration follows from minimizing free energy:

\[
c_v = \exp\!\left(-\frac{E_f^v}{k_B T}\right),
\]

to leading order in dilute limit. Near copper's melting point (~1358 K), \(c_v\) is still only ~\(10^{-4}\) — but enough to matter for diffusion-controlled processes during wire annealing.

Defects also have **chemical potentials** in open systems. When the wire surface oxidizes, copper vacancies may be injected into the bulk to balance stoichiometry at the interface — coupling electronic, chemical, and mechanical scales beyond pure elasticity.

## Defects in the copper wire processing chain

Tracing defects through wire manufacturing clarifies why taxonomy matters:

1. **Casting / initial solidification**: dendrites, voids, large angle boundaries.
2. **Drawing**: multiplication of dislocations, texture development, stored work hardening.
3. **Intermediate annealing**: vacancy migration, dislocation recovery and recrystallization.
4. **Final annealing for conductivity**: grain growth, reduction of electron-scattering defects.
5. **Service**: fatigue crack nucleation at surface defects; creep at elevated temperature via vacancy diffusion.

Each step changes the **defect population** — not merely the average stress or strain. Continuum plasticity captures some of this history through internal variables; atomistic methods resolve individual events. The taxonomy tells us which defect class dominates which phenomenon.

## Connection to continuum plasticity

Continuum models (J2 flow, **crystal plasticity**) **homogenize** defect motion into yield surfaces and hardening laws. The initial yield stress \(\sigma_0\), hardening modulus \(H\), and saturation stress \(\sigma_{\text{sat}}\) are not fundamental constants — they emerge from underlying **dislocation density** \(\rho\), grain size \(d\), and solute content.

| Continuum parameter | Defect-scale origin |
|---------------------|---------------------|
| \(\sigma_0\) | Friction stress, grain boundaries (Hall–Petch) |
| \(H\) | Dislocation storage vs. recovery (Taylor hardening) |
| Rate sensitivity | Thermally activated barrier crossing (kink-pair nucleation) |
| Damage | Void nucleation at inclusions, crack growth |

Part VI gave us the weak form of elasticity. Part VII explains why, beyond the elastic limit, we need mesoscale structure — and why parameters in flow laws must be **calibrated**, not assumed.

## Characterization tools

Defects are observed and measured by complementary probes:

| Probe | Defect sensitivity | Typical resolution |
|-------|-------------------|-------------------|
| **TEM** | Dislocations, boundaries, stacking faults | nm |
| **EBSD** | Grain orientation, texture, boundary character | µm |
| **X-ray diffraction** | Lattice strain, dislocation density averages | µm–mm |
| **Atom probe tomography** | Solute clusters, composition at boundaries | nm |
| **Electrical resistivity** | Vacancies, solutes, dislocations (indirect) | mm sample |

A copper wire's **conductivity specification** after anneal reflects reduced vacancy and dislocation scattering — defect taxonomy linked to electrical engineering requirements, not only mechanical strength.

Simulation validates against these probes at the scale each method resolves. DDD compares to TEM post-mortems; MD compares to diffuse scattering; continuum compares to macroscopic stress–strain. Mismatch diagnoses missing physics (wrong mobility, incomplete recovery) rather than "bad numerics" alone.

## Dislocation density as a state variable

Even before DDD simulation, engineers parameterized hardening with **dislocation density** \(\rho\) as an internal variable in continuum models. The taxonomy clarifies what \(\rho\) counts: line length per unit volume, regardless of orientation — a scalar summary of one-dimensional defects.

Finer descriptors (forest vs. cell-wall structure, link-length distributions) become necessary when scalar \(\rho\) fails to distinguish microstructures with identical density but different connectivity — as in recent link-statistics work. The taxonomy tells you **when** a scalar suffices and **when** topology matters.

## Radiation and non-equilibrium defects

The taxonomy extends to **non-equilibrium** populations: irradiation produces vacancy–interstitial pairs; quenched-in vacancies exceed equilibrium concentration; shock loading creates dislocation avalanches faster than thermal recovery.

Copper used in high-radiation environments (accelerators, nuclear systems) accumulates defect structures absent in commercial wire processing — same taxonomy, different kinetics. Non-equilibrium requires **rate equations** or **kinetic Monte Carlo** atop static formation energies from DFT.

## When to descend further

Elastic fields of dislocations assume a known **core structure** — the arrangement of atoms within ~1 nm of the line. Linear elasticity is invalid there. **Molecular dynamics** resolves the core and provides **mobility laws** (velocity vs. stress) that dislocation dynamics codes calibrate against. **DFT** resolves core energies and stacking-fault energies when empirical potentials are uncertain.

The scale hierarchy is not a one-way street. Coarse models suggest where fine models must focus; fine models supply parameters coarse models cannot compute from first principles alone.

## Lab act: read the slip lines before the load cell bends (Act IV — Hardening)

**Act IV** in the lab is when the force–displacement trace bends upward after yield. Part VI fitted that bend with phenomenological \(H\) and \(\sigma_{y0}\); this chapter names the **objects** that bend was homogenizing.

Before running DDD, inspect the cold-drawn copper wire under a low-power microscope (or a published EBSD micrograph of drawn copper):

| Defect class | What to look for on the wire | What the taxonomy calls it |
|--------------|----------------------------|----------------------------|
| **Line** | Faint parallel streaks on the surface — slip traces on {111} planes | Edge/screw dislocations; forest density \(\rho\) |
| **Surface** | Grain boundaries visible as etched lines if polycrystalline | Barriers to slip; sources for new segments |
| **Point** | Not visible optically; inferred from resistivity drop after anneal | Vacancies frozen by drawing; recovery on heating |

Counting lines is not required — **classifying** is. Ask: which defect type carries the history cold drawing wrote into the wire before the test began? The answer is **line defects**: a forest whose density \(\rho\) makes Taylor hardening \(\tau \propto \sqrt{\rho}\) the mesoscale origin of the \(H\) that Part VI borrowed without derivation.

When \(\rho\) is only a label on an FEM input deck, the taxonomy has not yet become geometry. [VII.2](02-dislocation-dynamics.md) is where the forest becomes computable lines.

## Concept map checkpoint (defect taxonomy)

This chapter is where Part VI's fitted hardening parameters receive a geometric inventory. Before DDD simulates moving lines, summarize what the taxonomy established:

| Question | Part VII answer (copper wire) |
|----------|-------------------------------|
| What **object**? | Point (vacancy, interstitial), line (dislocation), surface (GB, SF) defects |
| What **structure**? | Burgers vector \(\mathbf{b}\); slip systems {111}\(\langle 110 \rangle\) in FCC Cu |
| What **theorem**? | Taylor hardening \(\tau \propto \sqrt{\rho}\) from forest statistics |
| What **breaks**? | Scalar \(\rho\) when link topology matters; continuum elasticity at the core (\(<1\) nm) |

The Act IV Lab act classified slip traces on cold-drawn copper before the load cell bent — line defects carry the history drawing wrote into the wire. When \(\rho\) is only a label on an input deck, the taxonomy has not yet become geometry; [VII.2](02-dislocation-dynamics.md) is where the forest becomes computable lines.

## Bridge

Dislocation dynamics simulates line defects directly — too coarse for every atom, too fine for pure FEM. It is the mesoscale chapter of our copper wire story: the place where work hardening becomes geometry and statistics rather than a fitted curve.

| What VII.1 (taxonomy) named | What VII.2 (dislocation dynamics) will simulate |
|-----------------------------|------------------------------------------------|
| Point defects (vacancies, interstitials) | Thermal recovery and climb kinetics feeding forest evolution |
| Line defects (edge, screw, mixed) | Peach–Köhler motion, multiplication, junction reactions |
| Surface defects (GBs, stacking faults) | Barriers to slip; sources for new segments |
| Scalar \(\rho\) as internal variable | Taylor \(\tau \propto \sqrt{\rho}\) from line statistics, not fitted \(H\) |
| Part VI J₂ parameters \(\sigma_{y0}\), \(H\) ([VI.4](../part06-continuum/04-nonlinear-plasticity-preview.md)) | Mesoscale origin of yield and hardening from forest density |

**Scale-boundary handshake (Part VI → VII.1 → VII.2).**

| Continuum parameter (Part VI) | Defect-scale origin (this chapter) | DDD input (next chapter) | Failure mode |
|-------------------------------|-----------------------------------|--------------------------|--------------|
| \(\sigma_0\) (initial yield) | Hall–Petch grain boundaries; friction stress | Source density, obstacle spacing | Fitted \(\sigma_0\) with no \(\rho\) or \(d\) |
| \(H\) (isotropic hardening) | Taylor forest \(\tau \propto \sqrt{\rho}\) | Line length statistics from motion | Phenomenological \(H\) with no forest geometry |
| Rate sensitivity | Thermally activated kink-pair nucleation | MD mobility tables ([VIII.2](../part08-md/02-ensembles-integrators.md)) | Rate-independent J₂ at high strain rate |
| Core energy / \(\gamma_{\text{sf}}\) | Stacking faults, partial dislocations | DFT or MD exports ([IX.3](../part09-dft/03-dft-workflows.md)) | Linear elasticity at \(r < 1\) nm |

The taxonomy above named what broke the smooth continuum picture: point defects (vacancies from annealing), line defects (dislocations from cold drawing), and surface defects (grain boundaries, stacking faults). The next chapter follows those **lines** as they move under Peach–Köhler forces, multiply through Frank–Read sources, and tangle into the forest whose density \(\rho\) makes Taylor hardening \(\tau \propto \sqrt{\rho}\) — the mesoscale origin of the \(H\) and \(\sigma_{y0}\) that Part VI's J₂ preview borrowed without derivation.

Return to the [prologue](../prologue/00-many-scales.md): **Act IV — Hardening** is when the load cell curve bends upward after yield. Part VI fitted that bend with phenomenological plasticity; Part VII explains the **geometry** cold drawing wrote into the wire before the test began. When mobility laws or core energies are still adjustable knobs, the signal to descend further is Part VIII — atomistics at the notch root and dislocation core.

Turn the page when \(\rho\) is a label on an input deck rather than a count of moving lines — dislocation dynamics is where the forest becomes computable geometry. If the taxonomy Lab act classified slip traces and Burgers circuits but \(\rho\) still sits on the input deck without segment motion, continue to [VII.2's opening hinge](02-dislocation-dynamics.md#ddd-opening-hinge-taxonomy-to-motion), where Peach–Köhler forces and OpenDiS time integration replace static defect catalog as the primary object for the first time since Part VII began.
