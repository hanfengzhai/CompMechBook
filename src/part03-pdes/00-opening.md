# Part III — Fields on Domains

Part II gave us function spaces, norms, and operators — the vocabulary in which infinite-dimensional mechanics is well posed. Part III applies that vocabulary to the **partial differential equations** that encode conservation and constitutive physics on continua.

The copper wire from the prologue enters this part as a domain with boundary conditions: steady heat conduction along its length, transient heating when current flows, elastic equilibrium under tension. Each scenario begins as a **strong form** — a PDE satisfied pointwise — and is rewritten as a **weak form** suitable for computation. Sobolev spaces supply the regularity theory; energy methods package existence and uniqueness as minimization principles that Part IV will discretize.

The layout follows the **PDE Notes** in [`writings/pde/`](../../writings/pde/): four numbered chapters, mechanics examples throughout, and a **Bridge** at the end of each chapter pointing forward. Read them in order; they hand off directly to finite elements (Part IV) and finite volumes (Part V).

## The concept map (ME 300B)

At every step, ask the four questions the Functional Analysis Notes use — now applied to fields on domains:

| Question | Example in this part |
|----------|----------------------|
| What **object** are we studying? | A field \(u(x)\) on \(\Omega\) — displacement, temperature, pressure |
| What **structure** does it add? | Strong form (pointwise PDE); weak form (variational pairing in \(H^1\)) |
| What **theorem** becomes possible? | Lax–Milgram existence; energy minimization; integration by parts |
| What **breaks** if structure is missing? | Reentrant corners without classical \(C^2\) solutions; inconsistent BCs |

```mermaid
flowchart LR
  Strong[Strong form PDE] --> Weak[Weak form / test functions]
  Weak --> Sob[Sobolev regularity H¹]
  Sob --> Energy[Energy minimization]
  Energy --> FEM[Part IV: FEM assembly]
  Energy --> FVM[Part V: conservation laws]
```

**Baby picture:** write the physics as a PDE, multiply by a test function and integrate by parts, land in \(H^1\) where Lax–Milgram guarantees a solution — then ask which discretization (Galerkin or flux balance) fits the physics.

## Bridge

Part II promised that the copper wire's displacement and temperature live in Sobolev spaces, not in \(\mathbb{R}^N\) for any fixed mesh. The first chapter below writes the strong forms that describe those fields — and shows where classical pointwise solutions fail, motivating the weak formulations that follow.
