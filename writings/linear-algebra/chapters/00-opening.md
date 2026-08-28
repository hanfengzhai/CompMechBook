# Part I — The Grammar of Computation

Every scale in computational mechanics eventually reduces to **finite-dimensional algebra**: a state vector, a system matrix, a load vector, an eigenvalue problem. Molecular dynamics integrates Newton's equations with a timestep loop that is matrix–vector multiplication in disguise. Density functional theory solves a self-consistent field cycle that ends in linear algebra on orbital coefficients. Finite element codes assemble sparse stiffness matrices and call a solver. The pattern is universal; Part I makes it explicit.

We begin where most readers already have intuition: vectors, matrices, linear maps, and eigenvalues. The copper wire from the prologue appears first as a chain of coupled springs — a stiffness matrix and a load — then as a vibration problem whose modes decouple in an eigenbasis. By the final chapter, finite meshes suggest the limit \(N \to \infty\) and the function spaces of Part II.

Four chapters follow the **Linear Algebra Notes** in [`writings/linear-algebra/`](../../writings/linear-algebra/): numbered files, mechanics examples, and **Bridge** sections at each handoff. Nothing here requires functional analysis; everything here prepares for it.

## Chapter guide

| Chapter | Wire story beat | Core object | Handoff |
|---------|-----------------|-------------|---------|
| [I.1](01-vectors-matrices.md) | Grips fixed, load cell at zero | \(\mathbf{u}\), \(\mathbf{K}\), \(\mathbf{f}\); energy \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) | Sparsity from local coupling → assembly in I.2 |
| [I.2](02-linear-maps.md) | Element local axes vs global numbering | Linear maps, bases, \(\mathbf{L}_e^T \mathbf{k}_e \mathbf{L}_e\) | Symmetry and SPD → eigenmodes in I.3 |
| [I.3](03-eigenvalues.md) | Tap the wire; it rings at discrete pitches | \(\mathbf{K}\mathbf{v} = \omega^2 \mathbf{M}\mathbf{v}\); modal superposition | Decoupled modes → limit \(N\to\infty\) in I.4 |
| [I.4](04-toward-infinity.md) | Mesh refines; fields replace nodal values | Operators, Gram matrices, preview of \(L^2\), \(H^1\) | [Bridge to Part II](04-toward-infinity.md#bridge-to-part-ii) |

Read in order. Each chapter ends with a **Bridge** that states why the next chapter must exist; skipping ahead to eigenvalues without assembly is like listening to the wire's vibration modes before naming the springs that carry tension.

## Scene

The prologue placed a cold-drawn copper wire under tension — heated by current, cooled by air, strengthened by a dislocation forest invisible at the engineering scale. Before we climb that ladder rung by rung, we need the **syntax** every rung shares: states collected into vectors, equilibrium written as linear systems, complexity decoupled by eigenmodes.

At this first scale the wire is not yet a PDE or a mesh. It is a chain of coupled springs: each node carries a displacement, each bond contributes a stiffness entry, and tension at the grips becomes a load vector. Finite element assembly, molecular dynamics force evaluation, and Kohn–Sham orbital solves all reduce to the same pattern — \(\mathbf{K}\mathbf{u}=\mathbf{f}\) or its eigenvalue cousin. Part I makes that pattern explicit before Part II asks what happens when the number of springs grows without bound.

## The concept map

At every step in this part, ask the same four questions the [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) later formalize for infinite dimensions:

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | A state vector \(\mathbf{u}\), a stiffness matrix \(\mathbf{K}\), an eigenmode |
| What **structure** does it add? | Inner product (energy), symmetry (reciprocity), sparsity (local coupling) |
| What **theorem** becomes possible? | Spectral decomposition, positive-definiteness \(\Rightarrow\) unique equilibrium |
| What **breaks** if structure is missing? | Ill-conditioning, spurious modes, non-convergence as \(N \to \infty\) |

The roadmap this part follows:

```mermaid
flowchart LR
  V[Vectors / norms] --> M[Matrices / maps]
  M --> E[Eigenvalues / modes]
  E --> L[Limit N to infinity]
  L --> FA[Function spaces Part II]
```

**Baby picture:** collect degrees of freedom into a vector, write equilibrium as \(\mathbf{K}\mathbf{u}=\mathbf{f}\), decouple complexity with eigenmodes, then ask what happens when the mesh — and \(N\) — grows without bound. The copper wire's tension test begins as a spring network long before it becomes a PDE.

## Representative schematics (ME 300A)

The [Linear Algebra Notes](https://hanfengzhai.github.io/file/ME300A_LinAlg.pdf) (ME 300A) collect the same baby pictures Part II later lifts into infinite dimensions. Use them as a visual index while reading:

| Schematic | Idea | Chapter in this part |
|-----------|------|----------------------|
| 1 | Vectors, norms, inner products; energy as \(\mathbf{u}^T\mathbf{K}\mathbf{u}\) | [I.1](01-vectors-matrices.md) |
| 2 | Linear maps, bases, change of coordinates; assembly as coordinate change | [I.2](02-linear-maps.md) |
| 3 | Eigenvalues, eigenvectors, modal decoupling; vibration of the spring chain | [I.3](03-eigenvalues.md) |
| 4 | \(N\to\infty\); operators, Gram matrices, preview of \(L^2\) and \(H^1\) | [I.4](04-toward-infinity.md) |

Each schematic answers the four concept-map questions for one layer of finite-dimensional structure. When assembly or eigenmodes feel like bookkeeping, return to the matching row: *what object, what structure, what theorem, what breaks?* Part II will replay the same table with function spaces instead of vectors.

### ME 300A → ME 412 master roadmap (preview) {#me-300a--me-412-master-roadmap-preview}

The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) (ME 412) open with **Schematic 1a–1b** — a master roadmap from linear algebra through weak PDEs and FEM. Part I covers the **left half** of that diagram in finite dimensions; Part II replays it with operators and Hilbert spaces:

```mermaid
flowchart LR
  subgraph me300a["Part I (ME 300A schematics 1–4)"]
    V[Vectors / norms]
    M[Matrices / maps]
    E[Eigenvalues / modes]
    L[Limit N to infinity]
  end
  subgraph me412["Part II+ (ME 412 schematics 1a–14)"]
    Op[Operators]
    Hil[Hilbert geometry]
    Weak[Weak PDE / FEM]
  end
  V --> M --> E --> L --> Op --> Hil --> Weak
```

**Baby picture:** ME 300A teaches you to collect DOFs, write \(\mathbf{K}\mathbf{u}=\mathbf{f}\), and decouple with eigenmodes. ME 412 asks what happens when \(N\) grows without bound — the same four concept-map questions, now with \(u \in H^1\) instead of \(\mathbf{u} \in \mathbb{R}^N\). The copper wire's spring chain in Part I is the **discrete shadow** every mesh in Part IV refines toward the limit Part II names. When Part III's variational ladder ([Schematic 14](../part03-pdes/00-opening.md#the-variational-ladder-me-412-schematic-14)) or the full-book [coupling ladder](../part09-dft/00-opening.md#the-coupling-ladder-me-412-reunion) ([row 16](../appendix/memory-sheet.md#continuity-hinges-master-map); [epilogue Act VI reunion](../epilogue/multiscale.md#lab-act-reunion-six-acts-one-afternoon)) feel distant, return here: the grammar is already in hand — only the room grows.

## Story so far (Prologue)

The prologue introduced a single copper wire as a **ladder of scales** — from continuum stress and FEM meshes down through dislocations, atoms, and electrons — and the four questions every rung answers: state, equations, discretization, upward export. Before climbing that ladder mathematically, Part I pauses at the rung every simulation shares:

| Prologue stage | What we saw | What Part I will make explicit |
|----------------|-------------|--------------------------------|
| Engineering scale | Tension, heating, sagging | States as vectors; equilibrium as \(\mathbf{K}\mathbf{u}=\mathbf{f}\) |
| Finer scales (preview) | Dislocations, atoms, electrons | The same linear-algebraic pattern in disguise |
| Four questions | State / equations / discretization / export | Here: state = vector, equations = linear system, discretization = assembly |

The wire at this scale is still a chain of coupled springs — not yet a PDE, not yet a mesh of tetrahedra. Part I supplies the syntax every later part generalizes: collect degrees of freedom, write balance as a linear system, decouple complexity with eigenmodes, then ask what happens when \(N \to \infty\) in Chapter 4.

## Closing the arc from the Prologue {#opening-hinge-prologue-to-part-i}

If you have read the prologue straight through, the copper wire has already appeared as a continuum member, a dislocation forest, an atomic lattice, and a sea of electrons. Part I does not repeat those scenes — it **grounds** them in the grammar every later scale inherits:

| Prologue image | Part I vocabulary |
|----------------|-------------------|
| Ladder of scales | Every rung eventually ends in \(\mathbf{A}\mathbf{x}=\mathbf{b}\) or an eigenproblem |
| Four questions (state, equations, discretization, export) | State = vector; equations = linear system; discretization = assembly; export = moduli or modes extracted from solves |
| Six-act lab session | Act I (mounting) = first \(\mathbf{K}\mathbf{u}=\mathbf{f}\) before current or ramp |
| One specimen, many scales | Same wire as \(N\) coupled springs — the discrete shadow every mesh refines |

The prologue asked *what is the minimal description at each scale?* Part I answers for the rung every code shares: **finite-dimensional algebra** with energy norms, symmetry, and sparsity. When Part II replaces vectors with functions, the moves learned here remain — inner products become \(L^2\) pairings, stiffness matrices become operators, and eigenmodes become normal modes in \(H^1\). The [Functional Analysis Notes](https://hanfengzhai.github.io/file/teaching/notes/ME412_CourseSummary.pdf) replay this same table in infinite dimensions; Part I is the finite-dimensional rehearsal.

## How Part I connects to the full ladder

The prologue's ladder is not nine unrelated subjects — it is one specimen with the same computational skeleton repeated at every scale:

| Later part | Part I move it inherits | Copper wire instance |
|------------|-------------------------|----------------------|
| Part II (function spaces) | \(N \to \infty\); eigenmodes → normal modes | Axial \(u(x)\) as limit of nodal values |
| Part IV (FEM) | \(\mathbf{K}\mathbf{u}=\mathbf{f}\) assembly | Meshed bar under end load |
| Part VII (dislocations) | Sparse local coupling; eigenstructure of stiffness | Forest stiffens effective \(\mathbf{K}\) |
| Part VIII (MD) | State vector + time-step update | Atomic positions as a long vector |
| Part IX (DFT) | Self-consistent linear solve on coefficients | Kohn–Sham as repeated \(\mathbf{H}\psi = \varepsilon\mathbf{S}\psi\) |

Reading Part I is therefore not a detour before "real" mechanics — it is the **grammar** every later chapter speaks. When molecular dynamics integrates forces or DFT diagonalizes a Hamiltonian, the pattern is still: collect degrees of freedom, apply a linear map, iterate until balance.

## Lab act: I — Mounting

In [laboratory time](../prologue/00-many-scales.md#the-experiment-as-plot), the operator has not yet switched on current or ramped grip displacement. The wire sits in wedge jaws; the load cell reads zero; the first honest model is a chain of bar elements with boundary conditions at the grips. **Act I** is where every later scale hides its linear algebra: \(\mathbf{K}\mathbf{u}=\mathbf{f}\) before fields, weak forms, or electrons enter the story. When a chapter in Part I feels abstract, return to the mounting scene — a cylinder gripped, a sparse matrix waiting to be assembled.

### What you should be able to do after Part I

Each chapter adds one move to a minimal workflow you can run on paper or in NumPy before opening Part II:

| After chapter | Skill on the copper wire | Minimal artifact |
|---------------|--------------------------|------------------|
| I.1 | Name state, stiffness, load for a spring chain | \(\mathbf{K}\mathbf{u}=\mathbf{f}\) with numbers |
| I.2 | Rotate a bar element; assemble a global matrix | \(4 \times 4\) block from \(\mathbf{R}^T\mathbf{k}\mathbf{R}\) |
| I.3 | Tap the wire; read fundamental frequency | `eigh(K, M)` → Hz, compare to \(f_1 \approx 4.6\,\text{kHz}\) |
| I.4 | Refine mesh; watch nodal values become a field | \(N = 5, 20, 100\) → plot \(u(x)\) approaching smooth curve |

None of these require functional analysis — but each one is the finite-dimensional shadow of something Part II names rigorously. If you can assemble a three-node bar, solve for displacement, and extract a fundamental frequency, you have already done 80% of what a linear static/dynamic FEM code does on the first timestep. Parts II–IV replace vectors with functions and loops with weak forms; the **moves** stay the same.

## Bridge

The prologue introduced the copper wire at every scale and named the four questions every rung must answer. Part I begins at the rung every simulation shares — degrees of freedom collected into vectors, evolution and equilibrium written as linear systems — before the wire becomes a field, a mesh, or an electron density.

| What the prologue established | What Part I (opening → I.1) opens |
|-------------------------------|-----------------------------------|
| Copper wire specimen; six-act lab arc | **Act I — Mounting**: first honest \(\mathbf{K}\mathbf{u}=\mathbf{f}\) before yield |
| Four questions: state / equations / discretization / export | Finite DOFs: \(\mathbf{u}\in\mathbb{R}^N\), sparse \(\mathbf{K}\), load cell as \(\mathbf{f}\) |
| Ladder preview (FEM, FVM, DFT…) | Same grammar under every rung — matrices before fields |
| Weak form named, not yet spoken | [I.4 Bridge](04-toward-infinity.md#bridge-to-part-ii): \(N\to\infty\) handoff to Part II |

Return to the [prologue](../prologue/00-many-scales.md): the drawn Cu wire (\(L=1\,\text{m}\), \(EA=2.4\times10^8\,\text{N·m}\) from [I.1](01-vectors-matrices.md)) is still unstrained — load cell reads zero, grips fixed. Every later part generalizes the same object: Part [IV](../part04-fem/00-opening.md) meshes it, Part [V](../part05-fvm/00-opening.md) cools it, Part [IX](../part09-dft/00-opening.md) audits its elastic constants. Part I is the rung where that story is still a **small sparse matrix** you can write by hand.

The first chapter refreshes the language — inner products, norms, matrix structure — that Parts II through IX will generalize to functions and operators.

Turn the page when the prologue's ladder feels like a menu of methods — Part I is where every later scale reveals the same \(\mathbf{A}\mathbf{x}=\mathbf{b}\) grammar underneath.
