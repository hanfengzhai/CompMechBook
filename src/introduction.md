# Introduction

> *Mechanics is the story of how matter responds to forces. Computation is how we tell that story when pencil and paper run out of room.*

This book is written as a single narrative. We begin where every computational mechanics pipeline secretly begins: with **linear algebra**—the grammar of vectors, matrices, and linear maps. From there we lift our gaze to **functional analysis**, where functions become vectors and differential operators become linear maps on infinite-dimensional spaces. That language is not ornamental; it is exactly what we need to formulate the **weak form** of partial differential equations and to prove that numerical methods approximate the right objects.

Once the mathematical stage is set, we walk through the scales of mechanics:

1. **Continuum mechanics** — balance laws, elasticity, and the boundary-value problems that describe bars, plates, and crystals at the macroscopic level.
2. **Finite element method (FEM)** — turning infinite-dimensional variational statements into finite systems of algebraic equations.
3. **Finite volume method (FVM) and CFD** — conserving fluxes cell by cell, from shock tubes to the Navier–Stokes equations.
4. **Dislocation dynamics** — line defects as the carriers of plasticity between continuum and atomistic descriptions.
5. **Molecular dynamics and density functional theory** — atoms and electrons at the finest scales we routinely simulate.

## How this book is organized

The structure follows the author's personal notes collected in [Writings](https://hanfengzhai.github.io/note.html) and, in Part II, the proof-oriented style of the **Functional Analysis Notes** (metric spaces → normed spaces → operators → functionals, with complete arguments).

Each chapter ends with a short **bridge** paragraph that connects to the next idea, so the book reads continuously rather than as a catalog of methods.

## Prerequisites

Comfort with multivariable calculus and undergraduate linear algebra is assumed. Prior exposure to solid or fluid mechanics is helpful but not required; physical motivation is introduced as we need it.

## A note on sources

Material is drawn from course and teaching notes on linear algebra, finite element analysis, computational fluid dynamics, atomistic modeling, defects in materials, and density functional theory. Where original scanned notes could not be text-extracted, exposition has been rewritten to preserve the ideas and notation while fitting the unified narrative.

## How to read

- **Front-to-back** if you are building foundations for research in computational mechanics.
- **Part IV onward** if you already know functional analysis and want a mechanics-oriented numerical methods track.
- **Parts VI–VII** if you are bridging from FEM to multiscale materials modeling.

Let us begin with a simple observation that will recur on every page: *every discretization is a projection from an infinite-dimensional space to a finite one—and the quality of that projection determines everything.*
