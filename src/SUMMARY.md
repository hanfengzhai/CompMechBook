# Summary

Read in order from the **Preface** through the **Epilogue** for the full narrative. Each numbered chapter ends with a **Bridge** that explains why the next chapter exists; part openings add a **concept map** (object, structure, theorem, failure mode) following the Functional Analysis Notes (ME 412) layout. Parts IV and V may be swapped if you already know FEM and want CFD first — both paths converge at Part VI.

**One arc in one breath:** A copper wire in wedge grips teaches linear algebra as \(\mathbf{K}\mathbf{u}=\mathbf{f}\), then functional analysis as fields in \(H^1\) and \(L^2\), then weak PDEs and Sobolev regularity, then FEM on the solid and FVM in the cooling air, then continuum stress and virtual work at the midpoint; when fitted hardening fails, the same specimen descends through dislocation dynamics, molecular dynamics, and Kohn–Sham DFT until the epilogue reunites every export in one multiscale pedigree — always the same afternoon, only the ruler changes.

**Navigation when a transition feels abrupt:** [Preface — story & continuity hinges](./preface.md) (sections *The story in one page*, *Ascent continuity hinges*, *Descent continuity hinges*) · [Appendix — continuity hinges index](./appendix/sources.md) · [Writings synopsis](../writings/SUMMARY.md) (canonical source index; see *Synopsis*).

[Preface](./preface.md)

---

# Prologue

- [The Same Material, Many Scales](./prologue/00-many-scales.md)

---

# Part I — The Grammar of Computation

- [Opening](./part01-linear-algebra/00-opening.md)
- [Vectors, Matrices, and the Language We Already Speak](./part01-linear-algebra/01-vectors-matrices.md)
- [Linear Maps, Bases, and Change of Coordinates](./part01-linear-algebra/02-linear-maps.md)
- [Eigenvalues: Modes That Decouple Complexity](./part01-linear-algebra/03-eigenvalues.md)
- [From \(\mathbb{R}^n\) to Functions: The First Step Up](./part01-linear-algebra/04-toward-infinity.md)

---

# Part II — Function Spaces

- [Opening](./part02-functional-analysis/00-opening.md)
- [Why Infinite Dimensions Appear in Mechanics](./part02-functional-analysis/01-motivation.md)
- [Normed Spaces and Completeness](./part02-functional-analysis/02-normed-spaces.md)
- [Inner Products and Hilbert Spaces](./part02-functional-analysis/03-hilbert-spaces.md)
- [Operators, Duality, and Weak Convergence](./part02-functional-analysis/04-operators-duality.md)
- [Compactness and the Spectral Theorem](./part02-functional-analysis/05-spectral-theorem.md)

---

# Part III — Fields on Domains

- [Opening](./part03-pdes/00-opening.md)
- [Strong Formulations and Their Limits](./part03-pdes/01-strong-form.md)
- [Weak Formulations and Test Functions](./part03-pdes/02-weak-form.md)
- [Sobolev Spaces: Regularity for Computation](./part03-pdes/03-sobolev-spaces.md)
- [Energy Methods and Minimum Principles](./part03-pdes/04-energy-methods.md)

---

# Part IV — The Finite Element Method

- [Opening](./part04-fem/00-opening.md)
- [The Method of Weighted Residuals](./part04-fem/01-weighted-residuals.md)
- [Galerkin's Method and Global Assembly](./part04-fem/02-galerkin-assembly.md)
- [Elements, Shape Functions, and Quadrature](./part04-fem/03-elements-quadrature.md)
- [From Poisson to Elasticity](./part04-fem/04-poisson-to-elasticity.md)
- [Convergence, Norms, and Error Estimates](./part04-fem/05-convergence.md)

---

# Part V — Conservation on Cells

- [Opening](./part05-fvm/00-opening.md)
- [Integral Forms of Conservation Laws](./part05-fvm/01-conservation-integral.md)
- [The Finite Volume Method in One Dimension](./part05-fvm/02-fvm-1d.md)
- [Fluxes, Riemann Problems, and Shock Capturing](./part05-fvm/03-fluxes-riemann.md)
- [Navier–Stokes and Computational Fluid Dynamics](./part05-fvm/04-navier-stokes-cfd.md)

---

# Part VI — Continuum Mechanics

- [Opening](./part06-continuum/00-opening.md)
- [Kinematics: How Bodies Move and Deform](./part06-continuum/01-kinematics.md)
- [Stress, Balance Laws, and Constitutive Relations](./part06-continuum/02-stress-balance.md)
- [Variational Elasticity and Nonlinear Extensions](./part06-continuum/03-variational-elasticity.md)
- [Nonlinear Elasticity and the Onset of Plasticity](./part06-continuum/04-nonlinear-plasticity-preview.md)

---

# Part VII — Defects and Dislocations

- [Opening](./part07-defects/00-opening.md)
- [Point, Line, and Surface Defects](./part07-defects/01-defect-taxonomy.md)
- [Dislocation Dynamics and Strain Hardening](./part07-defects/02-dislocation-dynamics.md)
- [From DDD to Crystal Plasticity and FEM](./part07-defects/03-polycrystal-and-fem-handoff.md)

---

# Part VIII — Atomistic Simulation

- [Opening](./part08-md/00-opening.md)
- [Interatomic Potentials and Phase Space](./part08-md/01-potentials-phase-space.md)
- [Ensembles, Integrators, and Practical Molecular Dynamics](./part08-md/02-ensembles-integrators.md)
- [Ab Initio MD, Coarse-Graining, and the Ladder Upward](./part08-md/03-ab-initio-and-coarse-graining.md)

---

# Part IX — Electronic Structure

- [Opening](./part09-dft/00-opening.md)
- [Born–Oppenheimer and the Hohenberg–Kohn Theorems](./part09-dft/01-born-oppenheimer.md)
- [Kohn–Sham DFT: Equations, Convergence, and Practice](./part09-dft/02-kohn-sham.md)
- [DFT Workflows: From Input Files to Multiscale Numbers](./part09-dft/03-dft-workflows.md)

---

# Epilogue

- [Multiscale Computational Mechanics](./epilogue/multiscale.md)

---

# Appendices

- [Glossary and Cross-Scale Index](./appendix/glossary.md)
- [Sources and Further Reading](./appendix/sources.md)
- [Final Memory Sheet](./appendix/memory-sheet.md)
