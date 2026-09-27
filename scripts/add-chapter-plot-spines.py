#!/usr/bin/env python3
"""Insert plot-spine (one line) sections into numbered chapter files (row 19)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WRITINGS = ROOT / "writings"

# chapter_id -> (relative path from writings/<part>/chapters/, plot spine sentence)
CHAPTERS: dict[str, tuple[str, str]] = {
    "I.1": ("linear-algebra/chapters/01-vectors-matrices.md",
            r"The grips tighten; the wire is still a spring chain and equilibrium is \(\mathbf{K}\mathbf{u}=\mathbf{f}\) before any field appears."),
    "I.2": ("linear-algebra/chapters/02-linear-maps.md",
            r"Element by element the stiffness assembles — bases and change of coordinates turn local springs into a global matrix."),
    "I.3": ("linear-algebra/chapters/03-eigenvalues.md",
            r"Tap the wire and it rings; eigenmodes decouple what the full stiffness matrix entangles."),
    "I.4": ("linear-algebra/chapters/04-toward-infinity.md",
            r"Refine the mesh until nodal values become a field — \(N\to\infty\) is the gate where grammar becomes analysis."),
    "II.1": ("functional-analysis/chapters/01-motivation.md",
             r"The mesh refines forever; weak forms exist because corners and kinks break classical smoothness on the wire."),
    "II.2": ("functional-analysis/chapters/02-normed-spaces.md",
             r"Energy norms need a complete room — Cauchy sequences must converge before we trust the limit solution."),
    "II.3": ("functional-analysis/chapters/03-hilbert-spaces.md",
             r"Inner products make orthogonality precise; modal decoupling from Part I survives the passage to \(H^1\)."),
    "II.4": ("functional-analysis/chapters/04-operators-duality.md",
             r"Loads are functionals; adjoints pair operators with the physics they represent on the specimen."),
    "II.5": ("functional-analysis/chapters/05-spectral-theorem.md",
             r"Compactness and spectra prove Galerkin approximations have a target to converge toward as \(h\to 0\)."),
    "III.1": ("pde/chapters/01-strong-form.md",
              r"Strong forms hold at interior points; welds and interfaces are where pointwise physics fails first."),
    "III.2": ("pde/chapters/02-weak-form.md",
              r"Test functions and integration by parts rewrite physics as pairings, not pointwise derivatives."),
    "III.3": ("pde/chapters/03-sobolev-spaces.md",
              r"Sobolev membership is the regularity contract every FEM shape function on the wire must satisfy."),
    "III.4": ("pde/chapters/04-energy-methods.md",
              r"Minimum energy and Lax–Milgram prove existence before any mesh is drawn on the heated bar."),
    "IV.1": ("fem/chapters/01-weighted-residuals.md",
             r"Weighted residuals turn PDEs into finite averages — Galerkin is the family FEM inherits."),
    "IV.2": ("fem/chapters/02-galerkin-assembly.md",
             r"Local element matrices sum to global \(\mathbf{K}\) — assembly is Part I's grammar on a mesh."),
    "IV.3": ("fem/chapters/03-elements-quadrature.md",
             r"Shape functions and quadrature are the geometry of approximation on each bar element."),
    "IV.4": ("fem/chapters/04-poisson-to-elasticity.md",
             r"Poisson's scalar problem becomes vector elasticity on the same wire mesh under tension."),
    "IV.5": ("fem/chapters/05-convergence.md",
             r"Céa's lemma names the error; two doors open — fluids (Part V) or continuum reunion (Part VI)."),
    "V.1": ("fvm/chapters/01-conservation-integral.md",
            r"Conservation laws start as integrals over control volumes, not pointwise PDEs in the air gap."),
    "V.2": ("fvm/chapters/02-fvm-1d.md",
            r"One-dimensional FVM with upwind flux is the honest first CFD code cooling the wire."),
    "V.3": ("fvm/chapters/03-fluxes-riemann.md",
            r"Riemann solvers capture shocks when characteristic speeds cross on the mesh."),
    "V.4": ("fvm/chapters/04-navier-stokes-cfd.md",
            r"Navier–Stokes and conjugate heat transfer set \(T_w\) — the temperature every descent rung inherits."),
    "VI.1": ("continuum/chapters/01-kinematics.md",
             r"Deformation gradient \(\mathbf{F}\) tracks how the wire stretches — kinematics precedes stress."),
    "VI.2": ("continuum/chapters/02-stress-balance.md",
             r"Cauchy stress and balance laws reunite what FEM assembled and FVM conserved."),
    "VI.3": ("continuum/chapters/03-variational-elasticity.md",
             r"Virtual work is the weak form of elasticity; hyperelastic energy closes the FEM loop."),
    "VI.4": ("continuum/chapters/04-nonlinear-plasticity-preview.md",
             r"Plasticity preview names where continuum fields fail — ascent ends, descent begins at the knee."),
    "VII.1": ("defects/chapters/01-defect-taxonomy.md",
              r"Point, line, and surface defects are the singularities continuum models smooth away."),
    "VII.2": ("defects/chapters/02-dislocation-dynamics.md",
              r"Dislocation lines move, multiply, and harden the wire — Taylor's forest explains the load curve knee."),
    "VII.3": ("defects/chapters/03-polycrystal-and-fem-handoff.md",
              r"OpenDiS to DAMASK to FEM is the polycrystal handoff when texture and hardening matter."),
    "VIII.1": ("md/chapters/01-potentials-phase-space.md",
               r"Interatomic potentials and phase space replace fields with coordinates and forces at dislocation cores."),
    "VIII.2": ("md/chapters/02-ensembles-integrators.md",
               r"Ensembles and integrators make MD reproducible — LAMMPS is the wire at atomic timestep."),
    "VIII.3": ("md/chapters/03-ab-initio-and-coarse-graining.md",
               r"Coarse-graining compresses trajectories into yaml tables DDD and FEM can consume with pedigree."),
    "IX.1": ("dft/chapters/01-born-oppenheimer.md",
             r"Born–Oppenheimer separates fast electrons from slow nuclei — the finest scale split on copper."),
    "IX.2": ("dft/chapters/02-kohn-sham.md",
             r"Kohn–Sham SCF is the self-consistent loop that makes DFT computationally tractable."),
    "IX.3": ("dft/chapters/03-dft-workflows.md",
             r"Quantum ESPRESSO workflows export pedigree numbers upward — the epilogue's Handshake 1 anchor."),
}

ACT_LABEL = {
    "I": "Act I — Grammar",
    "II": "Act I — Grammar",
    "III": "Act I — Grammar",
    "IV": "Act II — Discretization",
    "V": "Act II — Discretization",
    "VI": "Act II — Continuum reunion",
    "VII": "Act III — Descent",
    "VIII": "Act III — Descent",
    "IX": "Act III — Descent",
}


def act_for(chapter_id: str) -> str:
    part = chapter_id.split(".")[0]
    return ACT_LABEL[part]


def plot_spine_block(chapter_id: str, sentence: str) -> str:
    act = act_for(chapter_id)
    return (
        f"## Plot spine (one line) {{#plot-spine-one-line}}\n\n"
        f"> **{chapter_id} — {act}:** {sentence}\n\n"
        f"When this chapter feels abstract, read the sentence above aloud — it is this chapter's role in the "
        f"[chapter roadmap](../appendix/sources.md#chapter-roadmap-one-continuous-arc). "
        f"See the [numbered-chapter plot spine index](../appendix/sources.md#numbered-chapter-plot-spine-index-row-19) "
        f"for all 35 rungs; [row 19](../preface.md#skill-navigation-row-19) closes the audit when mid-chapter "
        f"reading stalls despite a Bridge from the prior chapter.\n"
    )


def insert_plot_spine(text: str, block: str) -> str:
    if "plot-spine-one-line" in text:
        return text

    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Expected markdown title on line 1")

    insert_at = 1
    # Skip blank lines after title
    while insert_at < len(lines) and lines[insert_at].strip() == "":
        insert_at += 1

    # Include intro paragraphs until first ## heading
    while insert_at < len(lines) and not lines[insert_at].startswith("## "):
        insert_at += 1

    return "".join(lines[:insert_at]) + "\n" + block + "\n" + "".join(lines[insert_at:])


def main() -> None:
    updated = 0
    for chapter_id, (relpath, sentence) in CHAPTERS.items():
        path = WRITINGS / relpath
        if not path.exists():
            raise FileNotFoundError(path)
        original = path.read_text(encoding="utf-8")
        new_text = insert_plot_spine(original, plot_spine_block(chapter_id, sentence))
        if new_text != original:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"updated: {relpath}")
        else:
            print(f"skip (exists): {relpath}")
    print(f"Done. {updated} files updated.")


if __name__ == "__main__":
    main()
