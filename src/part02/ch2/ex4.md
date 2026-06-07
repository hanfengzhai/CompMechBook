## 2.4 Banach and Hilbert space theorems

Three theorems form the backbone of variational PDE theory. We state them for intuition; proofs appear in standard texts (e.g., Brezis, *Functional Analysis*).

### Hahn–Banach (extension of functionals)

A bounded linear functional on a subspace of a Banach space extends to the whole space without increasing its norm. **Consequence:** there are enough continuous linear functionals to separate points—dual spaces are rich enough to test convergence.

### Uniform Boundedness (Banach–Steinhaus)

Pointwise bounded families of bounded operators on a Banach space are uniformly bounded. **Consequence:** stability of FE formulations can be studied operator-wise without blow-up hidden in fine print.

### Open Mapping and Closed Graph

Bounded bijections have bounded inverses; closed graphs characterize continuous operators. **Consequence:** well-posed continuum problems have discrete analogues that do not secretly amplify data.

### Lax–Milgram (the workhorse)

Let $V$ be a Hilbert space and $a : V \times V \to \mathbb{R}$ a bilinear form that is:

1. **Continuous:** $|a(u,v)| \le C \|u\| \|v\|$
2. **Coercive:** $a(u,u) \ge \alpha \|u\|^2$ for some $\alpha > 0$

Then for every $\ell \in V'$ there exists a **unique** $u \in V$ with

$$
a(u, v) = \ell(v) \quad \forall v \in V,
$$

and $\|u\| \le \frac{1}{\alpha}\|\ell\|$.

**Mechanics translation.** For Poisson $-\Delta u = f$ with homogeneous Dirichlet data on $\Omega$,

$$
a(u,v) = \int_\Omega \nabla u \cdot \nabla v \, d\Omega, \qquad \ell(v) = \int_\Omega f v \, d\Omega,
$$

coercivity is Poincaré's inequality and continuity is Cauchy–Schwarz. Lax–Milgram guarantees existence and uniqueness of the weak solution before any mesh exists.

**Takeaway.** Lax–Milgram is the abstract theorem your FE code implements. SPD stiffness matrix + load vector = discrete Lax–Milgram.
