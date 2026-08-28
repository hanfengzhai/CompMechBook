# Preface

This book grew out of a simple observation: computational mechanics is not a collection of unrelated numerical recipes. It is a single narrative about how we represent physical reality at different scales, and how the mathematical tools at each scale connect to the next.

When we write a finite element code, we solve a linear system assembled from local contributions — linear algebra in disguise. When we prove that a Galerkin approximation converges, we invoke completeness and compactness — functional analysis in disguise. When we coarse-grain a molecular dynamics trajectory or feed a DFT energy landscape into a continuum model, we are asking the same question in a different language: *what information survives when we change scale?*

The chapters that follow are written to be read in order, like a novel with a plot. A copper wire under tension, a turbulent jet, a dislocation network in a crystal, and the electrons that bind the atoms together are not separate homework problems. They are scenes in one story. The mathematics is the thread that stitches them together.

## Scene: before the first chapter

Picture a shared materials lab on a weekday morning. A cold-drawn copper wire — the kind used in power cables and tensile specimens — sits in wedge grips on a small frame. The operator has not yet ramped load or switched on current; the load cell reads zero, the thermocouple at mid-span reports room temperature, and a student at the next bench is already opening a terminal for a meshing script. Nothing in the room announces "functional analysis" or "Kohn–Sham." What is visible is simpler: one cylinder of metal, one experiment waiting to run, and the quiet assumption that a computer model somewhere will eventually agree with what the grips and sensors record.

That wire is the book's protagonist. Every part that follows returns to it — as a chain of springs, as a field in \(H^1\), as a meshed solid, as air cooling its surface, as a crystal carrying a dislocation forest, as an atomic lattice, as valence electrons in a periodic cell. The mathematics changes language; the specimen does not. Read this preface as the jacket copy and the prologue as the opening scene. When a chapter feels abstract, ask which bench in this lab you are standing at, and which of the four questions — state, equations, discretization, upward export — that chapter is answering for the same piece of copper.

## Plot spine: how the story is told

Each part follows the **Functional Analysis Notes** (ME 412) layout — numbered chapters, concept maps at openings, checkpoints at closings — but the book adds four narrative devices so the arc reads as one continuous text rather than a syllabus:

| Device | Role | Where it appears |
|--------|------|------------------|
| **Scene** | Return to the copper wire in concrete detail | Preface, prologue, every part opening, every numbered chapter, epilogue |
| **Bridge** | State why the next chapter must exist | End of every numbered chapter and part opening |
| **Lab act** | Worked example, workflow, or checklist tied to computation | Inside chapters (assembly, LAMMPS, OpenDiS, QE inputs) |
| **Concept map** | Object → structure → theorem → failure mode | Part openings; part closing checkpoints |
| **Representative schematics** | Baby pictures indexed to source notes (ME 300A, ME 412, ME 300B, FEA, FVM, …) | Every part opening (I–IX) |

The dramatic arc is not a surprise twist — it is **scale change with the same specimen**:

```mermaid
flowchart LR
  subgraph act1["Act I: Grammar"]
    A1[Vectors and matrices]
    A2[Function spaces]
    A3[Weak PDEs]
  end
  subgraph act2["Act II: Discretization"]
    B1[FEM mesh]
    B2[FVM fluxes]
    B3[Continuum fields]
  end
  subgraph act3["Act III: Descent"]
    C1[Dislocation forest]
    C2[Atomic lattice]
    C3[Electron density]
  end
  subgraph act4["Act IV: Coupling"]
    D1[Multiscale workflows]
  end
  A1 --> A2 --> A3 --> B1
  A3 --> B2
  B1 --> B3
  B2 --> B3
  B3 --> C1 --> C2 --> C3 --> D1
  D1 -.->|four questions| A1
```

**Act I** teaches the language (Parts I–III). **Act II** makes PDEs computable on meshes and control volumes (Parts IV–VI). **Act III** asks where continuum parameters hide their history (Parts VII–IX). **Act IV** wires the rungs together (epilogue). When a transition feels abrupt, read the **Bridge** at the end of the prior chapter — it is the narrative hinge the plot spine assumes you will use.

## The story in one page

Read this once if you want the plot before the proofs — every chapter below unpacks one beat of the same afternoon.

A cold-drawn copper wire waits in wedge grips: our protagonist through every scale. We first learn the grammar every simulation shares — vectors, stiffness matrices, eigenmodes — and watch mesh refinement send those objects toward functions and operators. Function spaces supply the room where weak forms live; PDEs write the equilibrium and heat equations those forms discretize. Finite elements mesh the solid; finite volumes balance fluxes in the air that cools the wire when current flows. Continuum mechanics names the stress and strain both discretizations approximate; [VI.4's intermission](part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) admits cold drawing wrote yield history the smooth fields cannot see — the hinge where phenomenology ends and pedigree begins. Dislocation dynamics simulates the forest that hardens the wire; molecular dynamics resolves atoms at notches and fits potentials on trust; density functional theory audits those potentials from electron density. The epilogue wires the rungs into handshakes no single code runs alone — the same four questions at every interface: state, equations, discretization, upward export.

The [prologue](prologue/00-many-scales.md) opens the scene; the [chapter roadmap](appendix/sources.md) lists every beat in reading order; the [epilogue](epilogue/multiscale.md) reunites all six lab acts in workflow time. The [opening continuity hinge](#opening-continuity-hinge) names the turn from panoramic ladder to explicit grammar when the prologue ends; the [ascent preview chain](#ascent-preview-chain) and [descent previews](#descent-preview-chain) below summarize each rung before you commit to every proof; the prologue's [reading compass](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) maps mathematical order against laboratory time when the two clocks diverge. The [ascent continuity hinges](#ascent-continuity-hinges) table names four turns within Parts I–V when linear algebra, analysis, and discretization feel like separate subjects; the [continuity hinges](#continuity-hinges-ascent-descent) table names the two turns at Part VI — mathematical midpoint and narrative intermission — before Part VII descends to defects; the [descent continuity hinges](#descent-continuity-hinges) table names the three turns within Parts VII–IX before the epilogue couples every export; the [epilogue continuity hinges](#epilogue-continuity-hinges) table names the three turns that close the loop from DFT exports back to the prologue's four questions on the next project.

## Opening continuity hinge (prologue → Part I) {#opening-continuity-hinge}

The book opens twice — once as a panoramic ladder in the prologue, once as explicit syntax in Part I. When the scale menu feels overwhelming before a single matrix is assembled, pause at this hinge — same copper wire, first finite-dimensional model.

| Hinge | Location | What turns |
|-------|----------|------------|
| **Panorama → grammar** | [Prologue Bridge](prologue/00-many-scales.md#bridge-to-part-i) → [Part I opening](part01-linear-algebra/00-opening.md#opening-hinge-prologue-to-part-i) | Nine-scale ladder becomes \(\mathbf{K}\mathbf{u}=\mathbf{f}\); four questions get their first numeric answers |

Read the [prologue bridge](prologue/00-many-scales.md#bridge-to-part-i) when you want the plot before proofs — it names every rung in one sitting. Read [Part I's opening hinge](part01-linear-algebra/00-opening.md#opening-hinge-prologue-to-part-i) when the ladder feels like a catalog of methods — the wire is already a spring chain waiting for assembly. The [preface bridge](#bridge) below states the same handoff in prose before you turn to Part I.1.

## Ascent preview chain

Read this once if you want the mathematical climb before every proof — each linked part opening unpacks one rung of the same copper wire.

**[Part I](part01-linear-algebra/00-opening.md)** teaches the grammar every simulation shares: the wire as a chain of springs, \(\mathbf{K}\mathbf{u}=\mathbf{f}\), eigenmodes that decouple vibration, and the limit \(N\to\infty\) that sends nodal values toward fields. **[Part II](part02-functional-analysis/00-opening.md)** names the room those fields live in — \(H^1\), \(L^2\), operators, completeness — and proves Galerkin FEM is projection, not guesswork. **[Part III](part03-pdes/00-opening.md)** writes equilibrium and heat as weak PDEs: strong forms fail at corners; Sobolev spaces and energy principles make the boundary value problems well posed. **[Part IV](part04-fem/00-opening.md)** meshes the solid: weighted residuals, Galerkin assembly, elements and quadrature, convergence in energy norm. **[Part V](part05-fvm/00-opening.md)** balances fluxes in the air that cools the wire — conservation on cells, Riemann problems, Navier–Stokes and conjugate heat transfer. **[Part VI](part06-continuum/00-opening.md)** names Cauchy stress and strain behind both discretizations, marks the [midpoint](part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead) where the mathematical climb completes, and closes with [VI.4's intermission](part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) where \(J_2\) placeholders yield to the dislocation forest.

## Ascent continuity hinges (I → VI) {#ascent-continuity-hinges}

Parts I–V climb from finite-dimensional algebra to two discretization philosophies. When a transition feels abrupt mid-climb, pause at one of these four hinges — same copper wire, richer vocabulary at each turn.

| Hinge | Location | What turns |
|-------|----------|------------|
| **Finite → infinite dimensions** | [I.4 Bridge](part01-linear-algebra/04-toward-infinity.md#bridge-to-part-ii) | Mesh refinement sends \(\mathbf{K}_N\) toward an operator; nodal vectors become fields in \(H^1\) and \(L^2\) |
| **Analysis → PDEs** | [II.5 Bridge](part02-functional-analysis/05-spectral-theorem.md#bridge-to-part-iii) | Completeness and spectral theory hand off to weak forms for Poisson, heat, and elasticity |
| **Well-posedness → assembly** | [III.4 Bridge](part03-pdes/04-energy-methods.md#bridge-to-part-iv) | Dirichlet principle and Lax–Milgram become Galerkin assembly on \(V_h\) |
| **Discretization fork → continuum** | [IV.5](part04-fem/05-convergence.md#bridge-two-doors-from-here) / [V.4](part05-fvm/04-navier-stokes-cfd.md#bridge-to-part-vi) | FEM (Door B) and FVM (Door A) converge on Cauchy stress; two languages, one tensor vocabulary in Part VI |

Read the [I.4 hinge](part01-linear-algebra/04-toward-infinity.md#bridge-to-part-ii) when \(\mathbf{K}\mathbf{u}=\mathbf{f}\) feels unrelated to PDEs — refinement already pointed at a function space. Read the [II.5 hinge](part02-functional-analysis/05-spectral-theorem.md#bridge-to-part-iii) when Sobolev norms feel abstract — the weak form is the next line of dialogue for the same wire. Read the [III.4 hinge](part03-pdes/04-energy-methods.md#bridge-to-part-iv) when energy minimization and matrix assembly seem like separate tricks — Rayleigh–Ritz on \(V_h\) is both. Read [IV.5's two doors](part04-fem/05-convergence.md#bridge-two-doors-from-here) when you must choose solids-first versus fluids-first; either path must reach [Part VI](part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead) before the descent begins.

The [ascent preview chain](#ascent-preview-chain) names Parts I–VI in one pass; this table names the **four narrative hinges** within that climb — the moments the plot turns from vectors to fields, from fields to weak PDEs, from weak forms to assembled matrices, and from two discretizations to shared continuum mechanics.

## Descent preview chain

Read this once if you want the scale descent before the mesoscopic and finer proofs — each linked part opening unpacks one rung on the way down.

**[Part VII](part07-defects/00-opening.md)** names the forest cold drawing stored: dislocation lines with Burgers vectors, Peach–Köhler forces, mobility laws, and Taylor hardening that export \(\rho\) and \(\tau(\gamma)\) to crystal plasticity FEM — the mechanism behind the \(J_2\) bend Part VI could only fit. **[Part VIII](part08-md/00-opening.md)** replaces line-core cutoffs with vibrating nuclei on interatomic potentials: NVT and NPT ensembles, velocity-Verlet integration, LAMMPS workflows that fit EAM parameters and export cohesive energy, elastic constants, and stacking-fault energy upward on trust — including the **temperature pedigree chain** from [V.4 conjugate heat transfer](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) (\(T_w\) from the Picard loop) through [VIII.3 WHAM reweighting](part08-md/03-ab-initio-and-coarse-graining.md#wham-part-vii-mobility-hinge-act-ii-temperature-pedigree) to [VII.2 mobility calibration](part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) at the same \(T_w\), not room temperature. **[Part IX](part09-dft/00-opening.md)** audits those potentials from electron density: Born–Oppenheimer separation, Hohenberg–Kohn, Kohn–Sham self-consistency, and Quantum ESPRESSO decks that export \(E_{\text{coh}}\), \(C_{ij}\), and \(\gamma_{\text{sf}}\) with a pedigree traceable to SCF logs — the finest rung on the prologue's ladder. After Part IX, only coupling remains: the [epilogue](epilogue/multiscale.md) reunites every export in workflow time — starting with [Handshake 2](epilogue/multiscale.md#handshake-2--joule-heating--conjugate-heat-transfer-part-iv--v), which reuses the V.4 CHT Lab act iteration table as the template for every downstream temperature export.

Each part opening also carries a one-paragraph preview for readers who pause mid-descent: [mesoscale](part07-defects/00-opening.md#the-descent-in-one-paragraph), [atomistic](part08-md/00-opening.md#the-atomistic-descent-in-one-paragraph), and [electronic floor](part09-dft/00-opening.md#the-electronic-floor-in-one-paragraph).

## Continuity hinges (ascent → descent) {#continuity-hinges-ascent-descent}

The book turns twice at Part VI — once in vocabulary, once in plot. Both hinges keep the same copper wire on the bench; only the state variable and the questions change.

| Hinge | Location | What turns |
|-------|----------|------------|
| **Mathematical midpoint** | [Part VI opening](part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead) | FEM/FVM meet Cauchy stress; the climb from linear algebra through discretization is complete |
| **Narrative intermission** | [VI.4](part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) | Smooth fields and \(J_2\) hardening fit the load cell but not its cause; pedigree replaces phenomenology |
| **First mesoscale chapter** | [Part VII opening](part07-defects/00-opening.md) | Burgers geometry and DDD replace scalar \(\alpha\); the descent preview chain begins in earnest |

Read the [midpoint](part06-continuum/00-opening.md#midpoint-ascent-complete-descent-ahead) when Parts I–V feel like separate subjects — Part VI names the stress tensor both discretizations approximate. Read the [intermission](part06-continuum/04-nonlinear-plasticity-preview.md#intermission-ascent-ends-descent-begins) when the return-mapping loop fits \(H\) and \(\sigma_{y0}\) but cannot explain **why** the curve bent. The prologue's [reading compass](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) maps these hinges against laboratory time (Acts III–IV: pull, then harden).

## Descent continuity hinges (VII → epilogue) {#descent-continuity-hinges}

After Part VI's intermission, the book descends in four deliberate turns — same wire, finer state variable, stricter pedigree at every export.

| Hinge | Location | What turns |
|-------|----------|------------|
| **Mesoscale → atomistic** | [VII.3 Bridge](part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) · [VIII.1 opening hinge](part08-md/01-potentials-phase-space.md#opening-hinge-vii3-to-viii1) | Line cores and mobility tables need atomic bonding; DDD cutoff becomes a vibrating RVE |
| **Potentials → ensembles** | [VIII.1 Bridge](part08-md/01-potentials-phase-space.md#bridge) · [VIII.2 opening hinge](part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2) | EAM minimization at 0 K is not the wire at \(T_w\); phase space must be sampled before mobility or moduli export |
| **Ensembles → coarse-graining** | [VIII.2 Bridge](part08-md/02-ensembles-integrators.md#bridge) · [VIII.3 opening hinge](part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3) | Audited trajectories must compress into handoff tables with DFT pedigree gates before Part IX |
| **Temperature pedigree at \(T_w\)** | [VIII.0 descent hinge](part08-md/00-opening.md#descent-hinge-cores-mobility-and-tw-pedigree) · [memory sheet row 8](appendix/memory-sheet.md#continuity-hinges-master-map) · [preface row 8 skill checkpoint](preface.md#skill-navigation-row-8) | [V.4 CHT](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) converged at \(T_w \approx 379\,\text{K}\); MD mobility, WHAM, and drag tables must not default to 300 K |
| **Atomistic → electronic audit** | [VIII.3 Bridge](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) · [IX.0 electronic audit hinge](part09-dft/00-opening.md#electronic-audit-hinge-descent-pedigree-and-tw-phonon) · [memory sheet row 9](appendix/memory-sheet.md#continuity-hinges-master-map) · [preface row 9 skill checkpoint](preface.md#skill-navigation-row-9) | EAM potentials on trust need SCF audit; [thermal phonon audit at \(T_w\)](part09-dft/00-opening.md#thermal-phonon-audit-at-tw) confirms \(\alpha\) and \(\tau_{\text{ph}}\) are not room-temperature folklore |
| **Electronic → coupling** | [IX.3 Bridge](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) | Finest rung complete; upward homogenization and handshake loops in the epilogue |

Read the [mesoscale hinge](part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) when mobility or \(\gamma_{\text{sf}}\) feel like fitted constants — Peierls stress and core width hide in atomic trajectories, not Taylor hardening alone. Read the [VIII.1 opening hinge](part08-md/01-potentials-phase-space.md#opening-hinge-vii3-to-viii1) when [VII.3's Bridge](part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) named the ink but phase space still feels like a new subject — the same `mobility.yaml` row, now with \(\mathbf{F}_i = -\nabla V\) on a screw-core RVE. Read the [VIII.2 opening hinge](part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2) when the EAM foundation archive exists but `MD_NVT_shear_PartVIII` has not yet run at \(T_w\) — 0 K minimization is not a room-temperature wire. Read the [VIII.3 opening hinge](part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3) when NPT moduli and mobility tables exist but no handoff bundle names DFT audit gates — trajectories without pedigree are multiscale folklore. Read the [temperature pedigree hinge](part08-md/00-opening.md#descent-hinge-cores-mobility-and-tw-pedigree) when Act II warmed the wire but mobility folders still cite 300 K — [memory sheet rows 8–9 baby picture](appendix/memory-sheet.md#rows-8-9-baby-picture-tw-temperature-pedigree) draws the \(T_w\) chain from CHT through MD to DFT phonons. Read the [electronic audit hinge](part09-dft/00-opening.md#electronic-audit-hinge-descent-pedigree-and-tw-phonon) when EAM matches bulk moduli but no one cites the DFT input deck or evaluates \(\alpha(T_w)\) beside `cht_export.yaml`. Read the [coupling hinge](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) when exports exist in separate folders but no workflow connects them — the epilogue's [Closing the arc from Part IX](epilogue/multiscale.md#closing-the-arc-from-part-ix) reunites SCF pedigree with the [thermal phonon audit at \(T_w\)](part09-dft/00-opening.md#thermal-phonon-audit-at-tw) before Handshakes 1–4b run.

The [descent preview chain](#descent-preview-chain) names Parts VII–IX in one pass; this table names the **six narrative hinges** within that descent — the moments the plot turns from forest statistics to vibrating nuclei, from 0 K potentials to finite-\(T\) ensembles, from trajectories to coarse-grained exports, from \(T_w\) pedigree through MD to DFT phonons, from electron density to coupled codes.

## Epilogue continuity hinges (IX → prologue) {#epilogue-continuity-hinges}

The book closes a third loop after ascent and descent: **coupling upward** from the finest rung back to engineering questions — and back to the prologue's four questions on every new project.

| Hinge | Location | What turns |
|-------|----------|------------|
| **Finest rung → workflow** | [IX.3 Bridge](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) | SCF exports archived; pedigree must compose with MD, DDD, and FEM folders |
| **Joule heat → fixed-grip stress** | [Epilogue Handshake 2](epilogue/multiscale.md#handshake-2--joule-heating--conjugate-heat-transfer-part-iv--v) → [IX.3 α Lab act](part09-dft/03-dft-workflows.md#lab-act-quasiharmonic-alpha-handshake-3-pedigree) → [Handshake 3](epilogue/multiscale.md#handshake-3--thermal-strain--mechanical-stiffness-part-vi--iv) | Handshake 2 (Parts IV–V CHT) sets \(\Delta T\); Handshake 3 (quasiharmonic \(\alpha\) from IX.3) sets thermal strain — the [sensitivity table](epilogue/multiscale.md#sensitivity-which-handshake-matters-most) ranks Handshake 2 first for \(T_w\) and Handshake 3 first for load-cell readings; [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks); [memory sheet row 13](appendix/memory-sheet.md#continuity-hinges-master-map) |
| **DDD rate → lab load cell** | [VII.3 rate handshake](part07-defects/03-polycrystal-and-fem-handoff.md#scale-boundary-handshake-ddd-strain-rate-to-quasi-static-fem) → [Epilogue Handshake 4a](epilogue/multiscale.md#handshake-4--rate-dependent-hardening-and-notch-localization-part-vii--vi--viii) | OpenDiS at \(10^3\,\text{s}^{-1}\) sets \(\tau_{\text{flow}}\); power-law \(m\) extrapolates to lab grip speed — the [sensitivity table](epilogue/multiscale.md#sensitivity-which-handshake-matters-most) ranks Handshake 4a next for Act IV hardening; [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks) (4a column); [memory sheet row 14](appendix/memory-sheet.md#continuity-hinges-master-map); [row 14 skill checkpoint](#skill-navigation-row-14) |
| **FE² notch → Act V localization** | [VII.3 Step 4 FE²](part07-defects/03-polycrystal-and-fem-handoff.md#step-4--when-offline-calibration-fails-fe-at-the-notch) → [Epilogue Handshake 4b](epilogue/multiscale.md#4b--when-continuum-fails-at-the-notch-md-subdomain-act-v--notch) | Scalar hardening from 4a matches bulk flow stress but may under-predict notch-root peak stress by 10–15% — the [sensitivity table](epilogue/multiscale.md#sensitivity-which-handshake-matters-most) activates 4b only with Act V; [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks) (4b column); [memory sheet row 15](appendix/memory-sheet.md#continuity-hinges-master-map); [row 15 skill checkpoint](#skill-navigation-row-15); upstream rate from [row 14](#skill-navigation-row-14) |
| **Coupling → laboratory time** | [Epilogue: six-act reunion](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) | Mathematical order (I→IX) reunites with the six acts the operator actually runs |
| **Act VI orchestration** | [IX.3 Bridge](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) → [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh) | Individual handshake exports need orchestrated pedigree — [`multiscale_export.yaml`](../scripts/parse_multiscale_workflow.sh) links Handshakes 1–4b in dependency order; [IX.3 epilogue pedigree table](part09-dft/03-dft-workflows.md#ix3-epilogue-pedigree-table) (orchestrated chain row); [script audit trail All — orchestrated chain row](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes); [sensitivity worksheet closing](epilogue/multiscale.md#worked-example-sensitivity-ranks) (row 16 stitch); [memory sheet row 16](appendix/memory-sheet.md#continuity-hinges-master-map); [one-page recap Act VI column](appendix/memory-sheet.md#one-page-copper-wire-recap); [row 16 skill checkpoint](#skill-navigation-row-16) |
| **Workflow → next project** | [Epilogue Bridge](epilogue/multiscale.md#bridge) → [Prologue](prologue/00-many-scales.md) | Four questions restart on a new material; the ladder is reusable, not copper-specific |

Read the [coupling hinge](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) when DFT, MD, and FEM outputs live in separate directories with no README at the arrows. Read the [Handshake 2 → 3 chain](epilogue/multiscale.md#handshake-2--joule-heating--conjugate-heat-transfer-part-iv--v) when the load cell sees thermal compression but the FEM deck still cites handbook \(\alpha\) beside an orphan `pw.x` log — [IX.3's quasiharmonic \(\alpha\) Lab act](part09-dft/03-dft-workflows.md#lab-act-quasiharmonic-alpha-handshake-3-pedigree) is where \(\alpha\) earns the same pedigree as \(C_{ij}\). Read the [VII.3 → Handshake 4a chain](part07-defects/03-polycrystal-and-fem-handoff.md#scale-boundary-handshake-ddd-strain-rate-to-quasi-static-fem) when the hardening knee looks right on a DDD plot but the load cell yield arrives early — direct import at \(10^3\,\text{s}^{-1}\) without extrapolation overpredicts flow stress by 5–35%. Read the [VII.3 Step 4 → Handshake 4b chain](part07-defects/03-polycrystal-and-fem-handoff.md#step-4--when-offline-calibration-fails-fe-at-the-notch) when bulk hardening from 4a looks credible but the optional notch concentrates stress the scalar law cannot capture — [`parse_fe2.sh`](../scripts/parse_fe2.sh) on fixture data reports a 10–15% root-stress uplift FE² resolves that crystal plasticity alone misses. Read the [Act VI orchestration chain](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) → [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh) when Handshakes 1–4b exist in separate folders but no orchestrated `multiscale_export.yaml` links them — [row 16 skill checkpoint](#skill-navigation-row-16), the [script audit trail All — orchestrated chain row](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes), [prologue reading compass row 16](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire), and [memory sheet Act VI baby picture](appendix/memory-sheet.md#act-vi-baby-picture-me-412-coupling-ladder) name the same stitch. Read the [six-act reunion](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) when you know each part in isolation but cannot name which handshake runs before the grips close tomorrow. Return to the [prologue](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when the specimen changes — the continuity hinges table in the [memory sheet](appendix/memory-sheet.md#continuity-hinges-master-map) collects all sixteen narrative hinges plus the opening and closing loops in one navigation page.

The [story in one page](#the-story-in-one-page) ends at multiscale coupling; this table names the **six narrative hinges** within that closing act — exports become workflows, temperature and expansion become fixed-grip stress, rate extrapolation becomes Act IV hardening, FE² becomes Act V localization, Act VI orchestration becomes `multiscale_export.yaml` ([memory sheet Act VI baby picture](appendix/memory-sheet.md#act-vi-baby-picture-me-412-coupling-ladder); [prologue row 16 preview](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue)), laboratory time becomes the compass for the next wire.

## How this book is organized

The structure follows the arc of the author's personal notes — linear algebra and functional analysis as foundations, partial differential equations and weak forms as the bridge to discretization, finite elements and finite volumes as the two great discretization philosophies for solids and fluids, and atomistic and electronic methods as the descent to finer scales. Each part ends with a short bridge section that explains why the next scale is necessary.

```mermaid
flowchart TB
  subgraph foundations["Foundations"]
    I[Part I: Linear algebra]
    II[Part II: Functional analysis]
    III[Part III: PDEs and weak forms]
  end
  subgraph discretize["Discretization"]
    IV[Part IV: Finite elements]
    V[Part V: Finite volumes and CFD]
  end
  subgraph physics["Continuum physics"]
    VI[Part VI: Continuum mechanics]
  end
  subgraph finer["Finer scales"]
    VII[Part VII: Defects and DDD]
    VIII[Part VIII: Molecular dynamics]
    IX[Part IX: DFT]
  end
  I --> II --> III --> IV
  III --> V
  IV --> VI
  V --> VI
  VI --> VII --> VIII --> IX
  IX --> E[Epilogue: Multiscale coupling]
```

Read straight through from the prologue to the epilogue. Parts IV and V can be swapped if you already know FEM and want CFD first; Part VI then unifies the stress–balance language both discretizations approximate. Parts VII–IX are best read after the continuum vocabulary of Part VI, because dislocation, atomistic, and electronic models explain where continuum parameters originate.

## Three reading paths

The book is one continuous story, but not every reader enters at the same rung:

| Path | Start here | Route | Best for |
|------|------------|-------|----------|
| **Full arc** | [Prologue](prologue/00-many-scales.md) | I → II → III → IV → V → VI → VII → VIII → IX → [Epilogue](epilogue/multiscale.md) | First read; builds every concept in order |
| **Analysis first** | Part I, then Part II | Skip to Part III when function spaces feel familiar; return to IV–V for discretization | Students who know FEM but want weak-form foundations |
| **Scale descent** | Part VI after skimming I–III | VI → VII → VIII → IX, then back to IV–V for how continuum codes mesh and flux | Researchers asking where moduli and hardening laws originate |

On every path, read the **Bridge** at the end of the prior chapter when a jump feels abrupt. Part openings add **Story so far** recaps, **concept map** tables (object → structure → theorem → failure mode), **How Part X connects to…** cross-part tables, **skill checkpoint** tables (minimal artifacts on the copper wire), and **representative schematics** indexed to the source notes — all following the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) layout. Part closings add **concept map checkpoints** that summarize what the part exported to the next scale. The **prologue** and **epilogue** add matching **concept map checkpoints** that frame the whole ladder at the bookends. The [skill navigation](#skill-navigation) table below collects every checkpoint in one compass.

## Reading rhythm

Each chapter uses a deliberate rhythm so the book reads as one continuous story rather than a stack of lecture notes:

| Section | Role | Where it appears |
|---------|------|------------------|
| **Scene** | Places the mathematics in the lab — grips tightening, current switching on, a notch concentrating stress | Preface, prologue, every part opening, every numbered chapter, epilogue, appendix glossary and sources |
| **Lab act** | Links the part to one act of the [six-act lab session](prologue/00-many-scales.md#the-experiment-as-plot) | Part openings I–IX and epilogue reunion |
| **Concept map** | Four questions: object, structure, theorem, failure mode | Part openings; epilogue closing lens |
| **Representative schematics** | Baby pictures indexed to source notes (ME 300A, ME 412, ME 300B, FEA, FVM, …) | Every part opening (I–IX) |
| **Bridge** | States why the next chapter exists — the narrative hinge | End of every numbered chapter, part opening, preface, prologue, epilogue, appendix glossary and sources |
| **Skill checkpoint** | Minimal artifact you can produce on the copper wire before turning the page | Prologue; every part opening (I–IX); epilogue |

When abstraction rises, read in this order: **Lab act** (which experiment am I in?) → **Scene** (what is the operator watching?) → **Concept map** (what structure makes the theorem possible?) → **Representative schematics** (which baby picture matches this chapter?) → **Skill checkpoint** (what can I do on paper or in a terminal?) → **Bridge** (why turn the page?).

## Skill navigation

The book is one continuous story, but mastery is checked at **milestones** — not only at the end. Each milestone lists skills on the copper wire and a **minimal artifact** (a matrix, a plot, a convergence log, a pedigree row) you can produce before moving on. Use this table as a compass when you want practice without rereading every proof:

| Milestone | When to pause | Skill checkpoint |
|-----------|---------------|------------------|
| After the panoramic ladder | Before Part I assembles the first matrix | [Prologue](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) |
| After Part I | Before fields replace vectors in Part II | [Part I opening](part01-linear-algebra/00-opening.md#what-you-should-be-able-to-do-after-part-i) |
| After Part II | Before weak PDEs in Part III | [Part II opening](part02-functional-analysis/00-opening.md#what-you-should-be-able-to-do-after-part-ii) |
| After Part III | Before Galerkin assembly in Part IV | [Part III opening](part03-pdes/00-opening.md#what-you-should-be-able-to-do-after-part-iii) |
| After Part IV | Before FVM fluxes or continuum stress | [Part IV opening](part04-fem/00-opening.md#what-you-should-be-able-to-do-after-part-iv) |
| After Part V | Before Cauchy tensors in Part VI | [Part V opening](part05-fvm/00-opening.md#what-you-should-be-able-to-do-after-part-v) |
| After Part VI | Before the mesoscale descent in Part VII | [Part VI opening](part06-continuum/00-opening.md#what-you-should-be-able-to-do-after-part-vi) |
| After Part VII | Before atomic trajectories in Part VIII | [Part VII opening](part07-defects/00-opening.md#what-you-should-be-able-to-do-after-part-vii) |
| After Part VIII | Before Kohn–Sham in Part IX | [Part VIII opening](part08-md/00-opening.md#what-you-should-be-able-to-do-after-part-viii) |
| After Part IX | Before multiscale coupling in the epilogue | [Part IX opening](part09-dft/00-opening.md#what-you-should-be-able-to-do-after-part-ix) |
| Row 8 — \(T_w\) pedigree (Act II → MD/DDD) | When MD mobility, WHAM, or OpenDiS drag folders cite 300 K but [V.4 CHT](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) converged at \(T_w\) | [Row 8 skill checkpoint](#skill-navigation-row-8) |
| Row 9 — phonon audit at \(T_w\) (MD → DFT) | When EAM matches bulk moduli but `alpha_export.yaml` lacks \(\alpha(T_w)\) beside SCF logs | [Row 9 skill checkpoint](#skill-navigation-row-9) |
| Row 13 — Joule heat → fixed-grip stress | When CHT converges but the FEM deck still cites handbook \(\alpha\) | [Row 13 skill checkpoint](#skill-navigation-row-13) |
| Row 14 — DDD rate → lab load cell | When DDD exports feed the plasticity deck but the hardening knee arrives early | [Row 14 skill checkpoint](#skill-navigation-row-14) |
| Row 15 — FE² notch → Act V localization | When bulk hardening from 4a looks right but the notch root under-predicts peak stress | [Row 15 skill checkpoint](#skill-navigation-row-15) |
| Row 16 — Act VI orchestration → multiscale export | When Handshakes 1–4b exist in separate folders but no single pedigree file links them | [Row 16 skill checkpoint](#skill-navigation-row-16) |
| After the full arc | Before starting a new project on a different material | [Epilogue](epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book) |

Each part-opening table breaks skills down **by chapter** (e.g. I.1–I.4, II.1–II.5). The prologue and epilogue tables frame the whole ladder at the bookends — navigation discipline before proofs, workflow exam after coupling. When a chapter feels abstract, skip to the matching row in the part opening and produce the minimal artifact; when the artifact is in hand, return to the **Bridge** at the end of the prior chapter for the narrative hinge.

The [reading compass](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) in the prologue maps **continuity hinges** (when the plot turns); this table maps **skill checkpoints** (when you should be able to do something concrete on the wire). Both tables describe the same afternoon — one in narrative time, one in competence time. [Memory sheet row 8](appendix/memory-sheet.md#continuity-hinges-master-map) is the narrative stitch for the Act II temperature pedigree; the [Row 8 skill checkpoint](#skill-navigation-row-8) below is the competence-time mirror — run [`parse_cht.sh`](../scripts/parse_cht.sh) before any NVT shear, WHAM ladder, or OpenDiS mobility fit, and archive `cht_export.yaml` with an explicit \(T_w\) column. [Memory sheet row 9](appendix/memory-sheet.md#continuity-hinges-master-map) is the narrative stitch for the electronic phonon audit; the [Row 9 skill checkpoint](#skill-navigation-row-9) mirrors it — run [`parse_alpha.sh`](../scripts/parse_alpha.sh) and [`parse_lifetime.sh`](../scripts/parse_lifetime.sh) at converged \(T_w\), not 300 K alone, before Handshakes 3 and 4a inherit thermal exports. [Memory sheet row 13](appendix/memory-sheet.md#continuity-hinges-master-map) is the narrative stitch for thermal expansion; the [Row 13 skill checkpoint](#skill-navigation-row-13) below is the competence-time mirror — run [`parse_alpha.sh`](../scripts/parse_alpha.sh) after Handshake 2's CHT loop, then verify the load cell against the [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks). [Memory sheet row 14](appendix/memory-sheet.md#continuity-hinges-master-map) is the narrative stitch for rate extrapolation; the [Row 14 skill checkpoint](#skill-navigation-row-14) mirrors it for Act IV hardening — run [`parse_rate.sh`](../scripts/parse_rate.sh) on OpenDiS sweeps before the crystal-plasticity deck inherits \(\tau_{\text{lab}}\). [Memory sheet row 15](appendix/memory-sheet.md#continuity-hinges-master-map) is the narrative stitch for notch localization; the [Row 15 skill checkpoint](#skill-navigation-row-15) mirrors it for Act V — run [`parse_fe2.sh`](../scripts/parse_fe2.sh) after completing [row 14](#skill-navigation-row-14), then verify root-stress uplift against the [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks) (Handshake 4b column). [Memory sheet row 16](appendix/memory-sheet.md#continuity-hinges-master-map) is the **ME 412 coupling ladder** stitch for Act VI; the [Row 16 skill checkpoint](#skill-navigation-row-16) mirrors it — run [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh) after rows 13–15 are understood individually, then archive `multiscale_export.yaml` beside the Act VI folder. The [prologue row 16 preview](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) named this orchestration stitch before Part I — the [row 16 When-to-pause opening sentence](#skill-navigation-row-16) below is the competence-time mirror of that preview when narrative time (Act VI foundation) and mathematical order (Part IX → epilogue) diverge on the same afternoon; the [memory sheet Act VI baby picture](appendix/memory-sheet.md#act-vi-baby-picture-me-412-coupling-ladder) draws the foundation → handshake diagram when the [epilogue continuity hinges](#epilogue-continuity-hinges) table above feels abstract; the [epilogue sensitivity worksheet closing](epilogue/multiscale.md#worked-example-sensitivity-ranks) (row 16 orchestration stitch) closes the quantitative audit when Handshakes 1–4b are understood individually but the orchestrated pedigree is still missing.

### Row 8 skill checkpoint — \(T_w\) pedigree (Act II → MD/DDD) {#skill-navigation-row-8}

This checkpoint closes the **V.4 CHT → VIII.0 descent hinge → VIII.3 WHAM → VII.2 mobility** chain — the descent stitch when Act II warmed the wire but MD mobility folders, WHAM replica ladders, or OpenDiS drag tables still cite 300 K by default. [V.4's Picard loop](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) and the [VIII.0 descent hinge](part08-md/00-opening.md#descent-hinge-cores-mobility-and-tw-pedigree) are the **upstream halves**; [VIII.3 WHAM at \(T_w\)](part08-md/03-ab-initio-and-coarse-graining.md#wham-part-vii-mobility-hinge-act-ii-temperature-pedigree) and [VII.2 mobility calibration](part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) at \(T_w\) are the downstream halves. It pairs [memory sheet row 8](appendix/memory-sheet.md#continuity-hinges-master-map) (narrative hinge) with a concrete artifact (competence hinge). Row 9 audits the phonon layer beneath this chain — complete row 8 before evaluating \(\alpha(T_w)\) or \(\tau_{\text{ph}}(T_w)\) in Part IX.

| Step | Skill on the copper wire | Minimal artifact |
|------|--------------------------|------------------|
| 1 — Handshake 2 | Run FEM solid ↔ FVM fluid until wall flux matches Joule source | `cht_export.yaml` via [`parse_cht.sh`](../scripts/parse_cht.sh); converged \(T_w \approx 379\,\text{K}\), \(\Delta T = T_w - T_\infty\) |
| 2 — NVT shear at \(T_w\) | Calibrate screw mobility from constrained shear at converged wall temperature, not 300 K | `mobility_cu_screw_{T_w}K.yaml` beside `cht_export.yaml` — [VII.2 Lab act](part07-defects/02-dislocation-dynamics.md#lab-act-calibrate-screw-mobility-from-md-shear-act-iv--mobility-prelude) |
| 3 — WHAM reweight | Run parallel tempering with replica node at \(T_w \pm 5\,\text{K}\); reweight with WHAM | `wham_export.yaml` via [`parse_wham.sh`](../scripts/parse_wham.sh) at `--target-t` from `cht_export.yaml` |
| 4 — OpenDiS pedigree | Verify DDD mobility table references \(M(\tau, T_w)\), not room-temperature default | OpenDiS input cites `mobility_cu_screw_{T_w}K.yaml`; cross-slip counts at \(T_w\) archived beside WHAM export |

**When to pause.** Read the [prologue row 8 preview](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) and the [reading compass row 8](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when narrative time (Act II warming) and mathematical order (Part V → Part VIII) diverge on the same afternoon. Return to [V.4's Picard loop](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) before opening any NVT shear folder — `cht_export.yaml` is the temperature contract every finer rung inherits. Do not conflate handbook 300 K drag with Joule-heated \(T_w\) — phonon softening shifts Act IV hardening before Part IX audits the phonon curve; the [memory sheet rows 8–9 baby picture](appendix/memory-sheet.md#rows-8-9-baby-picture-tw-temperature-pedigree) draws the chain. When row 8 is complete, proceed to [row 9](#skill-navigation-row-9) before Handshakes 3 and 4a inherit thermal exports in the epilogue.

### Row 9 skill checkpoint — phonon audit at \(T_w\) (MD → DFT) {#skill-navigation-row-9}

This checkpoint closes the **VIII.3 Bridge → IX.0 electronic audit → thermal phonon audit at \(T_w\)** chain — the descent stitch when EAM potentials match bulk moduli on trust but no DFT input deck is cited and \(\alpha\), \(\tau_{\text{ph}}\) still default to 300 K folklore. [VIII.3's Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) and the [IX.0 electronic audit hinge](part09-dft/00-opening.md#electronic-audit-hinge-descent-pedigree-and-tw-phonon) are the **upstream halves**; the [thermal phonon audit table](part09-dft/00-opening.md#thermal-phonon-audit-at-tw) and [epilogue opening hinge from Part IX](epilogue/multiscale.md#opening-hinge-ix3-to-epilogue) are the downstream halves. It pairs [memory sheet row 9](appendix/memory-sheet.md#continuity-hinges-master-map) (narrative hinge) with a concrete artifact (competence hinge). Upstream \(T_w\) must come from [row 8](#skill-navigation-row-8) first — phonon audits inherit the same `cht_export.yaml` column that MD mobility used.

| Step | Skill on the copper wire | Minimal artifact |
|------|--------------------------|------------------|
| 1 — Row 8 complete | Verify `cht_export.yaml` exists with converged \(T_w\) before phonon evaluation | `T_wall_K` field from [`parse_cht.sh`](../scripts/parse_cht.sh) on `cht_wire.conf` |
| 2 — SCF audit | Archive DFT functional, pseudopotential, cutoff, k-mesh beside elastic exports | `foundation_export.yaml` via [`parse_dft_workflow.sh`](../scripts/parse_dft_workflow.sh) on `cu.foundation/` |
| 3 — \(\alpha(T_w)\) | Evaluate quasiharmonic thermal expansion at converged wall temperature | [`parse_alpha.sh`](../scripts/parse_alpha.sh) on `cu.phonon/a_vs_T.dat` with `--target-t` from `cht_export.yaml` → `alpha_export.yaml` with explicit \(T_w\) column |
| 4 — \(\tau_{\text{ph}}(T_w)\) | Interpolate phonon lifetime at \(T_w\) for Handshake 4a drag pedigree | [`parse_lifetime.sh`](../scripts/parse_lifetime.sh) on `cu.phonon/phonon_lifetime_vs_T.dat` at converged \(T_w\) → lifetime row beside `mobility_cu_screw_{T_w}K.yaml` |

**When to pause.** Read the [prologue row 9 preview](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) and the [reading compass row 9](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when EAM fits look credible but the foundation folder lacks an explicit **`T_w` column** — illustrative fixtures such as [`fixtures/cu.foundation/`](../fixtures/cu.foundation/README.md) archive SCF metadata and phonon tables at 300 K but omit converged wall temperature until `cht_export.yaml` sits beside the DFT deck. Return to the [IX.0 thermal phonon audit table](part09-dft/00-opening.md#thermal-phonon-audit-at-tw) before trusting Handshake 3 thermal strain or Handshake 4a drag. Do not conflate \(\alpha(300\,\text{K})\) handbook comparison with \(\alpha(T_w)\) production export — SCF audits moduli; the phonon audit audits thermal eigenstrain at the same \(T_w\) Act II converged. When rows 8–9 are complete, [row 13](#skill-navigation-row-13) inherits honest \(\alpha(T_w)\Delta T\) on fixed grips in the epilogue.

### Row 13 skill checkpoint — Joule heat → fixed-grip stress {#skill-navigation-row-13}

This checkpoint closes the **Handshake 2 → IX.3 \(\alpha\) → Handshake 3** chain — the epilogue-only stitch when conjugate heat transfer has converged but fixed-grip stress still cites handbook thermal expansion. [V.4's Picard loop](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) and [IX.3's quasiharmonic \(\alpha\) Lab act](part09-dft/03-dft-workflows.md#lab-act-quasiharmonic-alpha-handshake-3-pedigree) are the **upstream halves**; [Handshake 3](epilogue/multiscale.md#handshake-3--thermal-strain--mechanical-stiffness-part-vi--iv) and the [six-act reunion Act III paragraph](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) are the downstream halves. It pairs [memory sheet row 13](appendix/memory-sheet.md#continuity-hinges-master-map) (narrative hinge) with a concrete artifact (competence hinge).

| Step | Skill on the copper wire | Minimal artifact |
|------|--------------------------|------------------|
| 1 — Handshake 2 | Run FEM solid ↔ FVM fluid until wall flux matches Joule source | `cht_export.yaml` via [`parse_cht.sh`](../scripts/parse_cht.sh); converged \(\Delta T = T_w - T_\infty\) |
| 2 — IX.3 \(\alpha\) | Export quasiharmonic \(\alpha(300\,\text{K})\) beside `cu.elastic/` | [`parse_alpha.sh`](../scripts/parse_alpha.sh) on `cu.phonon/a_vs_T.dat` → `alpha_export.yaml`, `alpha_cu_300K.dat` |
| 3 — Handshake 3 | Verify fixed-grip \(\sigma_{\text{th}} = E\alpha\Delta T\) against load-cell reading | Match epilogue [worked load-cell example](epilogue/multiscale.md#handshake-3--thermal-strain--mechanical-stiffness-part-vi--iv) within handbook tolerance |
| 4 — Sensitivity audit | Derive why Handshake 3 ranks first for fixed-grip stress | Complete [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks) first-order table |

**When to pause.** Read the [prologue row 13 preview](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) and the [reading compass row 13](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when narrative time (Acts II–III) and mathematical order (Parts IV–V → IX → epilogue) diverge on the same afternoon. Return to [V.4's Picard loop](part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) for Handshake 2 before opening the epilogue's [Handshake 3 worked load-cell example](epilogue/multiscale.md#handshake-3--thermal-strain--mechanical-stiffness-part-vi--iv). Do not conflate Handshake 2 (\(\Delta T\)) with Handshake 3 (\(\alpha\Delta T\)) — the [preface epilogue hinge row](#epilogue-continuity-hinges) names the full chain in workflow order; the [Act III reunion paragraph](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) states the same thermal pre-stress stitch when Act III activates in workflow time.

### Row 14 skill checkpoint — DDD rate → lab load cell {#skill-navigation-row-14}

This checkpoint closes the **VII.3 rate handshake → Handshake 4a** chain — the epilogue-only stitch when OpenDiS exports a plausible hardening curve but the load cell yield arrives early because DDD ran at \(10^3\,\text{s}^{-1}\) and the lab grip runs at \(10^{-3}\,\text{s}^{-1}\). It pairs [memory sheet row 14](appendix/memory-sheet.md#continuity-hinges-master-map) (narrative hinge) with a concrete artifact (competence hinge).

| Step | Skill on the copper wire | Minimal artifact |
|------|--------------------------|------------------|
| 1 — VII.2 forest | Export \(\tau(\gamma)\) and \(\rho(\gamma)\) from OpenDiS at accessible strain rates | `opendis.restart` + \(\tau\)–\(\gamma\) curve at \(\dot\varepsilon \in \{10^2, 10^3, 10^4\}\,\text{s}^{-1}\) |
| 2 — VII.3 rate fit | Fit power-law sensitivity \(m\) and extrapolate \(\tau_{\text{flow}}\) to lab grip speed | [`parse_rate.sh`](../scripts/parse_rate.sh) on `ddd_tau_vs_rate.dat` → `rate_export.yaml` |
| 3 — Handshake 4a | Verify crystal-plasticity FEM inherits extrapolated \(\tau_{\text{lab}}\), not raw DDD curve | Match epilogue [Handshake 4a worked example](epilogue/multiscale.md#handshake-4--rate-dependent-hardening-and-notch-localization-part-vii--vi--viii) within 5% on yield |
| 4 — Sensitivity audit | Derive why Handshake 4a ranks next for Act IV hardening | Complete [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks) Handshake 4a column; confirm direct-import overprediction on fixture data |

**When to pause.** Read the [prologue reading compass row for Handshake 4a](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when narrative time (Act IV) and mathematical order (Part VII → epilogue) diverge on the same afternoon. Do not conflate DDD timestep strain rate with lab grip speed — the [preface epilogue hinge row](#epilogue-continuity-hinges) names the full chain in workflow order. When Joule heating is active (Act II), evaluate mobility and \(m\) at the converged \(T_w\) from Handshake 2, not at 300 K by default. When Act V activates the optional notch, complete [row 15](#skill-navigation-row-15) after row 14 — bulk \(\tau_{\text{lab}}\) from 4a is necessary but not sufficient for notch-root localization.

### Row 15 skill checkpoint — FE² notch → Act V localization {#skill-navigation-row-15}

This checkpoint closes the **VII.3 Step 4 FE² → Handshake 4b** chain — the epilogue-only stitch when crystal plasticity with scalar hardening from 4a matches bulk flow stress but under-predicts peak von Mises stress at the notch root by 10–15%. [VII.3 Step 4](part07-defects/03-polycrystal-and-fem-handoff.md#step-4--when-offline-calibration-fails-fe-at-the-notch) is the **upstream half**; [Handshake 4b](epilogue/multiscale.md#4b--when-continuum-fails-at-the-notch-md-subdomain-act-v--notch) and the [six-act reunion Act V row](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon) are the downstream halves. It pairs [memory sheet row 15](appendix/memory-sheet.md#continuity-hinges-master-map) (narrative hinge) with a concrete artifact (competence hinge). Upstream rate extrapolation must come from [row 14](#skill-navigation-row-14) first — FE² inherits the same `hardening.yaml` that 4a calibrated.

| Step | Skill on the copper wire | Minimal artifact |
|------|--------------------------|------------------|
| 1 — Row 14 complete | Verify bulk \(\tau_{\text{lab}}\) from rate extrapolation before notch analysis | `rate_export.yaml` from [`parse_rate.sh`](../scripts/parse_rate.sh) |
| 2 — VII.3 Step 4 | Run crystal plasticity and FE² on the same notch mesh ([VII.3 Step 4](part07-defects/03-polycrystal-and-fem-handoff.md#step-4--when-offline-calibration-fails-fe-at-the-notch)) | `fe2_notch_comparison.dat` with bulk and root stress columns |
| 3 — Handshake 4b | Compare FE² root stress to crystal plasticity; decide if offline calibration suffices | [`parse_fe2.sh`](../scripts/parse_fe2.sh) on `fe2_notch_comparison.dat` → `fe2_export.yaml` |
| 4 — Sensitivity audit | Derive why Handshake 4b activates only with Act V | Complete [sensitivity derivation worksheet](epilogue/multiscale.md#worked-example-sensitivity-ranks) Handshake 4b column; confirm 10–15% uplift on fixture data |

**When to pause.** Read the [prologue Handshake 4b preview row](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) and the [reading compass row for Handshake 4b](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when narrative time (Act V) and mathematical order (Part VII → epilogue) diverge on the same afternoon. Return to [VII.3 Step 4](part07-defects/03-polycrystal-and-fem-handoff.md#step-4--when-offline-calibration-fails-fe-at-the-notch) for the FE² procedure before opening the epilogue's [FE² worked example](epilogue/multiscale.md#worked-example-fe-at-the-wire-notch-act-v--notch). Do not conflate bulk hardening adequacy with notch-root localization — scalar \(H\) from 4a can match the load-cell knee while missing pile-up physics at \(K_t \approx 3\). When FE² and crystal plasticity agree within 5%, offline calibration from [row 14](#skill-navigation-row-14) suffices and Act V does not require concurrent DDD.

### Row 16 skill checkpoint — Act VI orchestration → multiscale export {#skill-navigation-row-16}

This checkpoint closes the **IX.3 foundation → [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh)** chain — the epilogue-only stitch when individual handshake exports exist in separate folders but no orchestrated pedigree links Handshakes 1–4b in dependency order. [IX.3's Bridge to the epilogue](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) and the [Act VI foundation folder](part09-dft/03-dft-workflows.md#lab-act-quasiharmonic-alpha-handshake-3-pedigree) are the **upstream halves**; the [six-act reunion Act VI paragraph](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon), the [epilogue script audit trail](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes) (per-handshake parsers), and [`multiscale_export.yaml`](../scripts/parse_multiscale_workflow.sh) are the downstream halves. It pairs [memory sheet row 16](appendix/memory-sheet.md#continuity-hinges-master-map) (ME 412 coupling ladder narrative hinge) with a concrete artifact (competence hinge). Rows [8](#skill-navigation-row-8)–[9](#skill-navigation-row-9) and [13](#skill-navigation-row-13)–[15](#skill-navigation-row-15) must be understood individually first — row 16 orchestrates them with Handshake 2's \(\Delta T\) feeding Handshake 3 and phonon lifetime at converged \(T_w\) feeding Handshake 4a drag.

| Step | Skill on the copper wire | Minimal artifact |
|------|--------------------------|------------------|
| 1 — Rows 8–9 and 13–15 understood | Name Handshakes 2, 3, 4a, 4b and the \(T_w\) pedigree individually before orchestrating | Completed skill rows 8–9 and 13–15 or equivalent artifacts |
| 2 — Foundation folder | Archive DFT, phonon, DDD, and CHT inputs under `cu.foundation/` | `foundation_export.yaml` via [`parse_dft_workflow.sh`](../scripts/parse_dft_workflow.sh) |
| 3 — Orchestrated chain | Run full multiscale workflow in dependency order | [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh) on `cu.foundation/` + `cht_wire.conf` → `multiscale_export.yaml`; per-handshake parsers in [epilogue script audit trail](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes) |
| 4 — Pedigree audit | Verify Handshake 3 uses \(\Delta T\) from Handshake 2 (not handbook default) and Handshake 4a uses lifetime at \(T_w\) | `multiscale_export.yaml` fields `delta_T_from_handshake_2` and `target_T_K` match converged CHT |

**Row 16 three-way audit (prologue preview ↔ this checkpoint ↔ workflow exam).** Each step below must agree across narrative time (prologue), competence time (this table), and workflow time (epilogue exam):

| Step | Prologue preview ([row 16](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue)) | This checkpoint (above) | Workflow exam ([Act VI row](epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book)) |
|------|-------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------|
| 1 | Upstream [rows 8–9](#skill-navigation-row-8) and [13–15](#skill-navigation-row-13) named before Part I | Step 1 — individual handshakes understood | Rows 8–9, 13–15 completed in workflow exam table |
| 2 | [IX.3 foundation checklist](part09-dft/03-dft-workflows.md#ix3-foundation-checklist) + [coupling ladder](part09-dft/00-opening.md#the-coupling-ladder-me-412-reunion) | Step 2 — `cu.foundation/` archived | [IX.3 foundation checklist](part09-dft/03-dft-workflows.md#ix3-foundation-checklist) cited in Act VI row |
| 3 | [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh) sketch → `multiscale_export.yaml` | Step 3 — orchestrated chain | [`parse_multiscale_workflow.sh`](../scripts/parse_multiscale_workflow.sh) in Act VI minimal artifact column |
| 4 | [IX.3 epilogue pedigree table](part09-dft/03-dft-workflows.md#ix3-epilogue-pedigree-table) + [subgraph node audit](appendix/memory-sheet.md#act-vi-subgraph-node-audit) + [per-node anchors](appendix/memory-sheet.md#act-vi-subgraph-node-audit) | Step 4 — `delta_T_from_handshake_2`, `target_T_K` audit | `./scripts/test-fixtures.sh`; [script audit trail](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes) closing paragraph; [Act VI minimal artifacts](epilogue/multiscale.md#act-vi-foundation-minimal-artifacts) Step 4 column |

**When to pause.** The [prologue row 16 closing stitch](prologue/00-many-scales.md#row-16-closing-stitch) names this divergence in narrative time — read it first when Act VI foundation runs in parallel with Acts I–V but mathematical order says Part IX → epilogue. Then read the [prologue row 16 preview](prologue/00-many-scales.md#what-you-should-be-able-to-do-after-the-prologue) and the [reading compass row 16](prologue/00-many-scales.md#reading-compass-two-clocks-on-one-wire) when narrative time (Act VI foundation) and mathematical order (Part IX → epilogue) diverge on the same afternoon — this skill checkpoint is the competence-time mirror; the compass row is the narrative-time mirror; the [skill navigation row 16 intro](#skill-navigation) above named the ME 412 coupling ladder stitch before this checkpoint's four steps. Read the [Part IX coupling ladder](part09-dft/00-opening.md#the-coupling-ladder-me-412-reunion) (ME 412 reunion) when the ascent grammar (Parts I–III) and the descent pedigree (Parts VII–IX) feel like separate books — row 16 is where the ME 412 coupling ladder reunites them in workflow time. Return to [IX.3's Bridge](part09-dft/03-dft-workflows.md#bridge-to-the-epilogue) and the [IX.3 epilogue pedigree table](part09-dft/03-dft-workflows.md#ix3-epilogue-pedigree-table) for the foundation checklist before running the orchestrator. Do not archive individual exports without the orchestrated `multiscale_export.yaml` — the [epilogue Act VI foundation table row](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon), [workflow exam Act VI row](epilogue/multiscale.md#what-you-should-be-able-to-do-after-the-book), [Act VI reunion paragraph](epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon), [script audit trail](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes) closing paragraph (orchestrated chain row), [memory sheet Act VI baby picture closing paragraph](appendix/memory-sheet.md#act-vi-baby-picture-closing), and [one-page recap Act VI column](appendix/memory-sheet.md#one-page-copper-wire-recap) name the same stitch when Act VI activates in workflow time. Verify the chain with `./scripts/test-fixtures.sh` before trusting a new parser version — the same check the [script audit trail](epilogue/multiscale.md#script-audit-trail-parse-scripts-handshakes) closing paragraph cites when auditing `delta_T_from_handshake_2` and `target_T_K`.

## The copper wire through the book

The same specimen — a cold-drawn copper wire under tension, heated by current, cooled by air — reappears in every part. The table below is a reading map: what changes is the **state variable**, not the material.

| Part | What the wire becomes | What we learn to compute |
|------|----------------------|--------------------------|
| Prologue | A ladder of scales | State, equations, discretization, upward exports |
| I | Coupled springs / modes | \(\mathbf{K}\mathbf{u}=\mathbf{f}\), eigenmodes |
| II | Fields in \(H^1\) and \(L^2\) | Norms, operators, Galerkin convergence |
| III | PDEs with weak forms | Strong vs. weak, Sobolev regularity, energy |
| IV | Meshed solid | Galerkin assembly, elements, convergence |
| V | Fluid around the wire | FVM fluxes, Navier–Stokes, conjugate heat transfer |
| VI | Cauchy stress and strain | Kinematics, balance, variational elasticity |
| VII | Dislocation forest | DDD, Taylor hardening, crystal plasticity handoff |
| VIII | Atomic lattice | Potentials, ensembles, LAMMPS workflows |
| IX | Valence electrons | Kohn–Sham, QE inputs, elastic constants upward |
| Epilogue | All scales coupled | Sequential, concurrent, and learned multiscale workflows |

Each numbered chapter ends with a **Bridge** section that states explicitly why the next chapter exists. If you ever feel a jump in abstraction, read the Bridge at the end of the prior chapter first — it is the narrative hinge. The [prologue](prologue/00-many-scales.md#the-experiment-as-plot) also maps the wire to **six acts** of one lab session (mounting through foundation) when you need laboratory time rather than part number. For a one-line role of every chapter in reading order, see the [chapter roadmap](appendix/sources.md) in the appendix (also listed as **Sources and Further Reading** in the table of contents). When a symbol reappears under new vocabulary — \(\mathbf{K}\) becoming an operator, then a bilinear form, then an elastic tensor — consult the [Glossary and Cross-Scale Index](appendix/glossary.md).

The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) (ME 412) supply the template for that hinge: not a proof document, but a **concept map** where every idea answers four questions — what object we study, what structure it adds, what theorem that structure enables, and what breaks if the structure is missing. Part II adopts that map explicitly; later parts reuse the same instinct at every scale change.

## Source material

The prose synthesizes course notes, teaching materials, and research experience collected over several years. Primary written sources include:

- [Linear Algebra notes](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) (ME 300A)
- [Functional Analysis notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) (ME 412) — layout model for Part II and all `writings/` subtrees
- [Partial Differential Equations notes](https://hanfengzhai.github.io/file/ME300B_PDE.pdf) (ME 300B)
- [Finite Element Analysis notes](https://hanfengzhai.github.io/file/FEA_notes.pdf) and [problem sessions](https://hanfengzhai.github.io/note.html)
- [Elasticity & Inelasticity notes](https://hanfengzhai.github.io/file/elasticity_notes.pdf)
- [Computational Fluid Dynamics notes](https://hanfengzhai.github.io/file/CFD_note.pdf) and [Finite Volume Method notes](https://hanfengzhai.github.io/note/FVM.pdf)
- [Defects & Disorders notes](https://hanfengzhai.github.io/file/defects_notes.pdf)
- [Atomistic Modeling notes](https://hanfengzhai.github.io/file/AtomModel_note.pdf)
- [DFT coursework](https://github.com/hanfengzhai/MSE5720-HW) (MSE 5720)

Canonical source markdown lives under [`writings/`](../writings/) in the **Functional Analysis Notes** layout: one mdBook per part, numbered chapters, and **Bridge** sections at the end of each chapter. Run [`scripts/sync-writings.sh`](../scripts/sync-writings.sh) to refresh `src/` from those sources. When the external `Writings` git submodule is linked, merge upstream changes there and re-run the sync script.

## Disclaimer

These notes represent the author's understanding of the material and are intended for study and reference. They may contain errors. Feedback is welcome at [hzhai@stanford.edu](mailto:hzhai@stanford.edu).

## Bridge {#bridge}

The preface is the table of contents in prose. The **prologue** is the first scene: one copper wire, many scales, and the four questions — state, equations, discretization, upward export — that every chapter will answer in its own language. Read it before Part I if you want the plot before the grammar; read it after Part VI if you prefer to meet the wire first as a meshed solid and then learn why the mesh had to exist.

The [opening continuity hinge](#opening-continuity-hinge) names the handoff from prologue panorama to Part I syntax — turn there when the ladder feels like a menu before the first matrix is assembled.

Turn the page when ready. The ladder begins with a specimen under tension and a question that will not go away: *what is the minimal description at this scale, and what do we pass to the scale above?*

---

*Hanfeng Zhai, 2026*
