# From DDD to Crystal Plasticity and FEM

Dislocation dynamics resolves individual lines in an elastic medium — powerful for single-crystal shear, insufficient for a full polycrystalline wire without homogenization. This chapter closes Part VII by asking how mesoscale simulations **export** their statistics to the crystal plasticity and finite element models of Parts IV and VI, and where **Peierls barriers** and **grain boundaries** force us to borrow parameters from finer scales.

The cold-drawn copper wire is not a single crystal. It is thousands of grains, each with its own slip systems, dislocation content, and orientation. DDD on one crystal explains one mechanism; engineering FEM needs **texture**, **hardening laws**, and **internal state variables** that summarize what DDD (or experiment) teaches.

## Peierls stress and lattice resistance

Before external load moves a dislocation, the lattice itself resists glide. The **Peierls–Nabarro** model estimates the stress required to move a straight screw or edge dislocation through a perfect lattice:

\[
\tau_P \approx \frac{2\mu}{1-\nu} \exp\!\left(-\frac{2\pi w}{b}\right),
\]

where \(\mu\) is shear modulus, \(\nu\) is Poisson's ratio, \(b\) is Burgers vector magnitude, and \(w\) is dislocation core half-width. The exponential sensitivity to \(w\) explains why **core structure** — resolved in MD, not in linear elasticity — matters for mobility at low temperature.

For copper, \(\tau_P\) is small compared to flow stress in work-hardened wire; the forest dominates. In annealed single crystals near yield, Peierls and **lattice friction** set the onset of plasticity. DDD codes often add a Peierls threshold to mobility laws so segments do not glide under arbitrarily small resolved shear.

| Quantity | Typical source | Role in DDD |
|----------|----------------|-------------|
| Core width \(w\) | MD / DFT stacking-fault energy | Sets \(\tau_P\) scale |
| Mobility \(M(\tau, T)\) | MD drag experiments | Velocity at \(\tau > \tau_P\) |
| Junction strength | MD / rules databases | Network topology evolution |

When DDD under-predicts yield stress in annealed copper, the first suspect is not the elastic Green's function — it is **mobility and Peierls parameters** fit at the wrong temperature or slip system.

## Polycrystal extensions

Single-crystal DDD imposes periodic or free surfaces around one orientation. Polycrystals add:

- **Grain boundaries** as obstacles (transmission, absorption, nucleation of dislocations).
- **Orientation fields** so each grain carries its own slip-system Schmid factors.
- **Compatibility** at interfaces: dislocations that cannot transmit deposit **geometrically necessary** content at boundaries.

Polycrystal DDD (and related **discrete dislocation plasticity** on FEM meshes) remains expensive at wire-scale volumes. Practical workflows run DDD on **representative volume elements** (RVEs) — \(1\)–\(10\) µm cubes — with boundary conditions matched to macroscopic strain rate, then **homogenize** stress–strain and dislocation density evolution.

```text
RVE DDD (single or few grains)  →  τ(γ), ρ(γ), back-stress evolution
        ↓
Crystal plasticity constitutive update (per Gauss point)
        ↓
Polycrystal FEM of wire (texture, drawing direction)
```

The arrow is not automatic file conversion. It is **calibration**: identifying parameters in a phenomenological law so that RVE DDD and macroscopic test data agree on the observables that matter for the wire — yield, hardening rate, Bauschinger effect after reverse loading.

## Crystal plasticity as the mesoscale–continuum bridge

**Crystal plasticity** treats each grain as a continuum with slip on crystallographic systems \(s\):

\[
\dot{\gamma}^{(s)} = f\!\left(\tau^{(s)}_{\text{resolved}}, \text{state variables}, T\right).
\]

State variables may include:

- **Forest density** \(\rho_f\) (Taylor hardening),
- **Back stress** \(\boldsymbol{\alpha}\) (kinematic hardening from pile-ups),
- **Slip resistance** \(g^{(s)}\) (isotropic hardening).

DDD supplies time histories of \(\rho\), link-length distributions, and internal stress fluctuations that inform how \(f\) should evolve — not just the scalar \(\sqrt{\rho}\) law, but whether **dynamic recovery** (annihilation, cross-slip) keeps pace with multiplication during wire drawing.

FEM implementations (Abaqus UMATs, FEniCS with constitutive plugins, DAMASK) evaluate crystal plasticity at quadrature points. The mesh from Part IV is unchanged; the **constitutive update** at each point becomes the export target for Part VII physics.

## Coupling strategies

| Strategy | What DDD provides | What FEM consumes |
|----------|-------------------|-------------------|
| **Offline calibration** | Hardening curves, yield surface evolution | Scalar parameters in J₂ or crystal plasticity |
| **Tabulated laws** | \(\tau(\gamma)\) lookup from RVE ensembles | Piecewise flow rules |
| **Two-scale FE²** | DDD RVE embedded at selected Gauss points | Macro strain drives RVE BCs; homogenized stress returns |
| **DDD-informed GND** | Geometrically necessary dislocation density | Gradient plasticity / strain-gradient FEM |

For the copper wire, **offline calibration** dominates industry practice: tensile tests plus electron backscatter diffraction (EBSD) texture inform crystal plasticity parameters, while DDD validates whether those parameters are consistent with dislocation mechanisms.

Two-scale FE² is research-grade: powerful for notches and grain clusters, costly when every element hosts an RVE. The epilogue returns to when concurrent coupling is worth the price.

## Verification and validation

DDD-to-FEM handoff fails silently when units, rates, or temperatures mismatch:

1. **Strain rate**: DDD at \(10^3\) s\(^{-1}\) does not calibrate quasi-static wire tests at \(10^{-3}\) s\(^{-1}\) without rate-dependent mobility.
2. **Temperature**: Drawing heats the wire; mobility and recovery are thermal. Room-temperature DDD parameters mis-predict hot stages of processing.
3. **Elastic constants**: DDD elasticity must match DFT/MD values used in Part VI — same \(\mu\), same anisotropy if orthotropic crystal plasticity follows.
4. **Size effects**: RVEs too small freeze dislocations artificially; too large become intractable. Convergence studies mirror FEM mesh refinement.

Validation hierarchy for the wire:

- **DDD vs. TEM** on deformed single crystals (dislocation structures),
- **Crystal plasticity FEM vs. tensile test** (texture + hardening),
- **Continuum FEM vs. structural deflection** (Part IV elasticity with plasticity when needed).

Agreement at each level does not guarantee predictive extrapolation to new processing routes — only that the ladder is internally consistent at tested conditions.

## What remains for atomistics

DDD assumes **closed cores** and empirical short-range rules. When dislocations meet grain boundaries, crack tips, or chemistry (oxygen at copper surfaces), cores interact with **atomic structure** DDD cannot resolve. Part VIII supplies stacking-fault energies, cross-slip rates, and nucleation barriers. Part IX supplies formation energies when even those atomistic parameters need first-principles validation.

The wire's strength is a story written in dislocation lines; the **ink** is atomic bonding. We have named the lines and their statistics. Next we resolve the atoms that give those lines their mobility.

## Bridge

Crystal plasticity and calibrated DDD close the mesoscale chapter: they explain why the copper wire yields and hardens without resolving every atom. But mobility laws, stacking-fault energies, and crack-tip bond breaking are not adjustable forever — they are measured or computed at the atomic scale. Part VIII follows the same copper lattice with Newton's equations and empirical or fitted potentials, supplying the parameters DDD and FEM inherit.
