# 4. Galerkin Finite Elements

> *Finite element analysis is not a separate subject from functional analysis—it is Galerkin's method with piecewise polynomial spaces on meshes.*

The **finite element method** (FEM) solves the variational problem of Part II by choosing finite-dimensional trial and test spaces built from **shape functions** on a **mesh**. It is the dominant discretization in computational solid mechanics, heat transfer, and— with appropriate stabilization—in fluid mechanics.

This part follows the ME335A *Finite Element Analysis* storyline: strong form → weak form → Galerkin discretization → assembly → error analysis. Teaching materials (problem sessions, course summary) and the author's *FEA notes* provide the technical spine.

By Section 4.5 you should be able to trace every entry of the global stiffness matrix $K_{IJ}$ to an integral over elements shared by nodes $I$ and $J$—the local-to-global map that makes FEM code work.
