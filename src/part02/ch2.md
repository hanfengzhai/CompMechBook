# 2. Metric, Normed, and Hilbert Spaces

> *A PDE solution is not a vector in $\mathbb{R}^n$—it is a function. Functional analysis supplies the spaces, norms, and convergence notions that make "approximate solution" a precise statement.*

In Part I we worked in finite dimensions. A mesh with $N$ nodes lives in $\mathbb{R}^{dN}$. But the *exact* solution $u(x)$ of an elliptic boundary-value problem belongs to an infinite-dimensional space of functions. We cannot store $u$ exactly; we can only store its values on a mesh, or coefficients in a basis, and ask whether these approximations **converge** to $u$ as the mesh refines.

Convergence requires a **metric** or **norm**. Functional analysis organizes this into a ladder:

$$
\text{metric spaces} \;\subset\; \text{normed spaces} \;\subset\; \text{inner product spaces} \;\subset\; \text{Hilbert spaces}.
$$

This part follows the structure of the *Functional Analysis Notes* (metric spaces → normed spaces → Hilbert spaces → fundamental theorems → applications to BVPs), but each section emphasizes the questions computational mechanics will ask: What is $H^1(\Omega)$? Why does integration by parts work? What does "find $u \in \mathcal{S}$ such that $a(u,v) = \ell(v)$ for all $v \in \mathcal{V}$" mean?

By the end of Section 2.6 you will have the **variational formulation** in hand—the exact starting point of the finite element method in Part IV.
