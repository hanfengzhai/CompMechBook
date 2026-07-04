# Point, Line, and Surface Defects

Perfect crystals exist in textbooks. Real materials carry **defects** — localized disruptions of order that control strength, diffusion, conductivity, and optical properties. A copper wire drawn through dies and annealed for electrical use is a catalog of defect physics: dislocation forests from cold work, vacancy clusters from thermal recovery, grain boundaries from polycrystalline structure, and oxide surfaces from environmental exposure.

Continuum elasticity in Part VI describes smooth displacement fields. Defects are where that smoothness fails — and where mesoscale models begin.

## Scene: the wire yields

The force–displacement curve from Part I finally bends. The load cell still reads force, but the slope drops: the wire is **plastic**. A polished surface that was mirror-smooth now shows faint **slip lines** — traces of dislocation motion on {111} planes. Continuum FEM with isotropic elasticity predicted a straight elastic segment forever; the experiment crossed a yield point that lives not in \(\mathbb{C}\) alone but in a **forest of line defects** stored by cold drawing.

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

### Worked example: Burgers circuit on Cu {111}

Trace a rectangular Burgers circuit on the (111) close-packed plane of fcc copper — the plane on which slip lines appear when the wire yields. Start at lattice point \(A\), walk four nearest-neighbor steps along \(\langle 110 \rangle\) directions in the plane, and close the loop at \(A\). In a perfect crystal the circuit closes with zero closure failure.

Now insert an extra half-plane of atoms along one edge of the circuit — an edge dislocation with line direction \(\boldsymbol{\xi} \parallel [110]\) and Burgers vector \(\mathbf{b} = \tfrac{a}{2}[110]\). Re-walk the circuit: the path that used to close now fails by exactly one lattice translation. That failure vector **is** \(\mathbf{b}\), with magnitude \(|\mathbf{b}| \approx 2.55\) Å for copper.

The elastic displacement field winds by \(|\mathbf{b}|\) around the core; the Peach–Köhler force on this segment under axial tension is \(\mathbf{f} = (\boldsymbol{\sigma}\cdot\mathbf{b}) \times \boldsymbol{\xi}\). When the wire's load cell registers yield, thousands of such segments move on {111} planes — the mesoscale mechanism behind the knee Part VI's J₂ law fitted with a single \(\sigma_y\).

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

## Bridge

Dislocation dynamics simulates line defects directly — too coarse for every atom, too fine for pure FEM. It is the mesoscale chapter of our copper wire story: the place where work hardening becomes geometry and statistics rather than a fitted curve. The next chapter follows dislocation lines as they move, multiply, and tangle under load.
