# Part II — Function Spaces

Part I showed that every mesh reduces mechanics to \(\mathbf{K}\mathbf{u}=\mathbf{f}\). That reduction is honest only if the limit as the mesh refines is well defined. The limit lives in a space of functions — displacements, temperatures, pressures — not in \(\mathbb{R}^N\) for any fixed \(N\).

This part builds the language of those spaces: norms that measure energy and mean square error, inner products that define orthogonality of modes, operators that generalize matrices, and compactness that makes spectral theory and Galerkin convergence possible. The copper wire from the prologue reappears throughout as a bar in \(H^1\), a thermal field in \(L^2\), and a problem whose discrete stiffness matrix is a projection of an operator we can now name.

The layout follows the **Functional Analysis Notes** in [`writings/functional-analysis/`](../../writings/functional-analysis/): numbered chapters, worked examples tied to mechanics, and a **Bridge** at the end of each chapter pointing to the next idea. Read the five chapters in order; they hand off directly to Part III, where weak forms of boundary value problems are written in the spaces defined here.

## Where we left the wire

Part I ended with a limit: as the spring network refines, the copper wire's displacement and temperature are no longer vectors in \(\mathbb{R}^N\) for any fixed \(N\). They become **fields** — functions of position along the bar — and the stiffness matrix is a finite-dimensional shadow of an operator we have not yet named.

The wire at this scale is still one-dimensional for intuition: axial displacement \(u(x)\) under tension, temperature \(T(x)\) along its length when current flows. Part II supplies the room those fields live in — norms that measure elastic energy, inner products that define orthogonality of vibration modes, completeness so mesh refinement has a target to converge toward. Every FEM code in later parts is linear algebra inside \(H^1\); this part explains why that claim is honest.

## The concept map (ME 412)

The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) are organized as a concept map, not a proof stack. At every step, ask:

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | A displacement field \(u\), not a vector \(\mathbf{u}\in\mathbb{R}^N\) |
| What **structure** does it add? | A norm (energy), an inner product (orthogonality), completeness (limits stay inside) |
| What **theorem** becomes possible? | Lax–Milgram existence, Galerkin best approximation, spectral convergence |
| What **breaks** if structure is missing? | Cauchy sequences leaving the space; corners with no classical \(C^2\) solution |

The master roadmap those notes draw — and this part follows — is:

```mermaid
flowchart LR
  LA[Linear algebra] --> Op[Operators]
  Op --> Norm[Norm / topology]
  Norm --> Ban[Completeness]
  Ban --> Hil[Hilbert geometry]
  Hil --> Dual[Duality]
  Dual --> Sob[Sobolev L² H¹]
  Sob --> Weak[Weak PDE / FEM]
```

**Baby picture:** first build the room (vector space), then add a ruler (norm), then close the holes (Banach/Hilbert completeness), then add angles (inner product), then write weak PDEs and trust that FEM is projection, not guesswork. The copper wire's displacement lives in that room long before any mesh assigns it node values.

## Representative schematics (ME 412)

Section A of the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) collects eight **representative schematics** — baby pictures of the same machine this part builds. Use them as a visual index while reading:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1a–1b | Master roadmap: linear algebra → operators → weak PDE/FEM | This opening; [II.5](05-spectral-theorem.md) Bridge |
| 2 | Norms define topology; equivalent norms, same convergence | [II.2](02-normed-spaces.md) |
| 3 | Completeness hierarchy: normed → Banach → Hilbert | [II.2](02-normed-spaces.md), [II.3](03-hilbert-spaces.md) |
| 4 | Sequence spaces \(\ell^p\), \(\ell^\infty\), closure under norms | [II.2](02-normed-spaces.md) |
| 5 | \(L^p\), \(H^1\), \(H^1_0\), weak derivatives | [II.3](03-hilbert-spaces.md); Part III.3 |
| 6 | Orthogonal projection; best approximation in Hilbert space | [II.3](03-hilbert-spaces.md) |
| 7 | Duality, Riesz representation, weak convergence | [II.4](04-operators-duality.md) |
| 8a–8b | PDE → weak form → FEM; well-posedness triangle | [II.5](05-spectral-theorem.md) → Part III |

Each schematic answers the four concept-map questions for one layer of structure. When a proof feels abstract, return to the matching row: *what object, what structure, what theorem, what breaks?*

## Lab act (prologue map)

You are in **Act III — Pulling** in slow motion — the mathematical front end. Before the grip displacement ramps, Part II answers why mesh refinement has a target: the displacement field \(u(x)\) lives in \(H^1\), not in \(\mathbb{R}^N\) for any fixed mesh. The load-cell curve you will read in Parts IV and VI is measured in the laboratory; this part explains what "convergence" means before any tetrahedron is meshed. Acts II (warming) and VI (foundation) bracket this part; return to the [prologue table](../prologue/00-many-scales.md#the-experiment-as-plot) when the function-space vocabulary feels removed from the tensile frame.

## Story so far (Prologue & Part I)

The prologue introduced the copper wire as a **ladder of scales** — continuum, dislocations, atoms, electrons — and the four questions every rung answers: state, equations, discretization, upward export. Part I made the bottom rung of that ladder explicit in finite dimensions:

| Stage | What we learned | What the wire became |
|-------|-----------------|----------------------|
| Prologue | One specimen, many scales; weak forms as recurring character | Cold-drawn copper under tension and current |
| I.1–I.2 | \(\mathbf{K}\mathbf{u}=\mathbf{f}\), bases, assembly | A chain of coupled springs under end load |
| I.3 | Eigenmodes decouple vibration | Normal modes of the same spring network |
| I.4 | \(N\to\infty\); fields replace vectors; operators replace matrices | Axial \(u(x)\) and \(T(x)\) as limits of mesh refinement |

Part I ended with a question Part II must answer: if every mesh gives a matrix \(\mathbf{K}_N\), what object does \(\mathbf{K}_N\) approximate as \(N\) grows? The answer is not "a bigger matrix" — it is an **operator** on a space of functions. Part II builds that space, names the norms that measure elastic energy, and proves that Galerkin FEM is honest projection rather than ad hoc linear algebra.

## Bridge

Part I ended with a promise: as the mesh refines, the copper wire's displacement and temperature fields live in infinite-dimensional spaces, not in \(\mathbb{R}^N\) for any fixed \(N\). The first chapter below makes that promise precise — why weak forms appear, why classical smoothness fails at corners, and why the stiffness matrix is a Galerkin projection rather than an arbitrary sparse array.
