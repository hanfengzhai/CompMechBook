## 1.3 Vector spaces and subspaces

### Definition

A **vector space** $V$ over $\mathbb{R}$ is a set closed under addition and scalar multiplication, satisfying the usual axioms (associativity, commutativity, distributivity, existence of zero and inverses). Elements of $V$ are **vectors** in the abstract sense—functions will qualify in Part II.

A **subspace** $W \subset V$ is a subset that is itself a vector space under the same operations. To verify $W$ is a subspace, it suffices to check:

1. $\mathbf{0} \in W$
2. $\mathbf{u}, \mathbf{v} \in W \implies \mathbf{u} + \mathbf{v} \in W$
3. $\mathbf{u} \in W, c \in \mathbb{R} \implies c\mathbf{u} \in W$

### Examples that matter for mechanics

**$\mathbb{R}^n$.** The prototype. Displacement vectors in multi-DOF systems live here.

**Matrices with a constraint.** The set of $2 \times 2$ matrices with $a_{11} = -a_{22}$ is a subspace of $\mathbb{R}^{2 \times 2}$—a trace-free diagonal pattern reminiscent of deviatoric stress tensors.

**Polynomials of bounded degree.** The space $\mathcal{P}_2 = \{a_0 + a_1 x + a_2 x^2\}$ is a **finite-dimensional** subspace of the infinite-dimensional space of all continuous functions on $[a,b]$. FEM approximates $u(x)$ by functions in $\mathcal{P}_1$ or $\mathcal{P}_2$ on each element—this is the first bridge from linear algebra to function approximation.

**Not every set is a subspace.** The set of solutions to $A\mathbf{x} = \mathbf{b}$ for $\mathbf{b} \neq \mathbf{0}$ is an **affine space**, not a subspace (it does not contain $\mathbf{0}$). The *homogeneous* system $A\mathbf{x} = \mathbf{0}$ defines the **null space** $\mathcal{N}(A)$, which *is* a subspace—the modes of deformation that produce no residual force.

### Span, basis, dimension

The **span** of vectors $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is all linear combinations $\sum c_i \mathbf{v}_i$. A **basis** is a minimal spanning set; its size is the **dimension** $\dim V$.

In FEM with $N$ nodes and $d$ DOFs per node, the discrete solution lives in a space of dimension $dN$ (before boundary constraints). The columns of the global stiffness matrix span the range of the stiffness operator restricted to that discrete space.

### Column space and row space

For $A \in \mathbb{R}^{m \times n}$:

- $\mathcal{C}(A) \subset \mathbb{R}^m$: outputs reachable by $A$
- $\mathcal{C}(A^T) \subset \mathbb{R}^n$: directions that couple to rows of $A$
- $\mathcal{N}(A)$: inputs mapped to zero

The **rank–nullity theorem** $\text{rank}(A) + \dim \mathcal{N}(A) = n$ is the algebraic statement of "rigid body modes plus deformable modes."

**Takeaway.** When we later define trial space $\mathcal{S}$ and test space $\mathcal{V}$ for a weak form, we are choosing subspaces of a function space. The finite-dimensional case you master here is the template.
