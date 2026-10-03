#!/usr/bin/env python3
"""Generate scripts/add-row-132.py from add-row-131.py with atomistic capstone transforms."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "scripts/add-row-131.py"
DST = ROOT / "scripts/add-row-132.py"


def transform(text: str) -> str:
    """Homogenization capstone (131) narrative -> atomistic capstone (132)."""
    pairs = [
        (
            "Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion",
            "Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion",
        ),
        (
            "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
            "row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132",
        ),
        (
            "row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion",
            "row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion",
        ),
        ("Row 68 ↔ Row 51 reunion (capstone path)", "Row 68 ↔ Row 52 reunion (capstone path)"),
        ("homogenization meta prelude capstone", "atomistic meta prelude capstone"),
        ("Homogenization meta prelude capstone", "Atomistic meta prelude capstone"),
        (
            "[row 130](preface.md#skill-navigation-row-130) or [row 111](preface.md#skill-navigation-row-111)",
            "[row 131](preface.md#skill-navigation-row-131) or [row 112](preface.md#skill-navigation-row-112)",
        ),
        (
            "closed the DDD meta prelude capstone / homogenization meta prelude hinge (VII.1 Bridge → VII.2 Peach–Köhler recited on the capstone path, forest-density Lab act linked \\(\\tau(\\gamma)\\) to Taylor hardening, one Burgers → segment-network arc under `writings/defects` chapters 01–02 after verified DDD meta prelude capstone)",
            "closed the homogenization meta prelude capstone / atomistic meta prelude hinge (VII.2 Bridge → VII.3 polycrystal recited on the capstone path, handoff Lab act archived `mobility.yaml`, one OpenDiS → spool arc under `writings/defects` chapters 02–03 after verified homogenization meta prelude capstone)",
        ),
        (
            "**row 51 still opens like standalone DAMASK homework after VII.2's forest-density Lab act on the capstone path**",
            "**row 52 still opens like standalone LAMMPS homework after VII.3's handoff Lab act on the capstone path**",
        ),
        (
            "[VII.2 Bridge to VII.3](part07-defects/02-dislocation-dynamics.md#bridge-to-vii3) reads correctly in isolation from [VII.3 polycrystal handoff](part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii2-to-vii3), texture and Voce tables feel disconnected from the post-yield forest Scene, or row 51's five-step audit feels like a duplicate checklist rather than the rear-view mirror of row 130's Peach–Köhler → spool turn",
            "[VII.3 Bridge to Part VIII](part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) reads correctly in isolation from [VIII.1 phase space](part08-md/01-potentials-phase-space.md#opening-hinge-vii3-to-viii1), EAM parameter tables feel disconnected from Peierls thresholds at \\(T_w\\), or row 52's five-step audit feels like a duplicate checklist rather than the rear-view mirror of row 131's polycrystal → atomic ink turn",
        ),
        (
            "[row 51](preface.md#skill-navigation-row-51) (VII.2 → VII.3 meta gate)",
            "[row 52](preface.md#skill-navigation-row-52) (VII.3 → VIII.1 meta gate)",
        ),
        (
            "Row 131 does not replace row 68, row 51, row 130, row 111, row 91, row 71, or row 32 — it reunites **verified DDD meta prelude capstone closure (row 130) with the full-book VII.2 → VII.3 homogenization meta reunion (row 51)** when OpenDiS exports and row 51 meta both read correctly alone but not as one continuous forest → polycrystal afternoon before Part VIII descent opens on the capstone path.",
            "Row 132 does not replace row 68, row 52, row 131, row 112, row 92, row 72, or row 33 — it reunites **verified homogenization meta prelude capstone closure (row 131) with the full-book VII.3 → VIII.1 atomistic meta reunion (row 52)** when `mobility.yaml` and row 52 meta both read correctly alone but not as one continuous spool → screw-core afternoon before EAM minimization at \\(T_w\\) opens on the capstone path.",
        ),
        (
            "2 — DDD meta prelude capstone / homogenization meta prelude gate | Confirm [row 130](preface.md#skill-navigation-row-130) or [Row 68 → Row 91 homogenization meta prelude reunion index (row 111)](appendix/sources.md#row68-row91-homogenization-meta-prelude-reunion-index-row-111) recited | Peach–Köhler DDD before VII.2 Bridge → polycrystal after verified DDD meta prelude capstone",
            "2 — Homogenization meta prelude capstone / atomistic meta prelude gate | Confirm [row 131](preface.md#skill-navigation-row-131) or [Row 68 → Row 92 atomistic meta prelude reunion index (row 112)](appendix/sources.md#row68-row92-atomistic-meta-prelude-reunion-index-row-112) recited | Polycrystal handoff before VII.3 Bridge → phase space after verified homogenization meta prelude capstone",
        ),
        (
            "Read [VII.2 Bridge to VII.3](part07-defects/02-dislocation-dynamics.md#bridge-to-vii3) through [VII.2 opening hinge to VII.3](part07-defects/02-dislocation-dynamics.md#opening-hinge-vii2-to-vii3) aloud | \"One orientation vs cold-drawn spool\"",
            "Read [VII.3 Bridge to Part VIII](part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) through [VII.3 opening hinge to VIII.1](part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii3-to-viii1) aloud | \"Ink is atomic bonding\"",
        ),
        (
            "Open [VII.2 Scene](part07-defects/02-dislocation-dynamics.md#scene-the-forest-grows) then [VII.3 Scene](part07-defects/03-polycrystal-and-fem-handoff.md#scene-from-one-crystal-to-a-spool-of-wire); confirm [VII.2 forest-density Lab act](part07-defects/02-dislocation-dynamics.md#lab-act-read-the-hardening-bend-from-forest-density-act-iv) linked \\(\\tau\\) to \\(\\sqrt{\\rho}\\) | Same wire; single crystal → thousands of grains",
            "Open [VII.3 Scene](part07-defects/03-polycrystal-and-fem-handoff.md#scene-from-one-crystal-to-a-spool-of-wire) then [VIII.1 Scene](part08-md/01-potentials-phase-space.md#scene-the-notch-under-the-microscope); confirm [handoff Lab act step 5](part07-defects/03-polycrystal-and-fem-handoff.md#lab-act-archive-the-opendis--damask--fem-handoff-act-ivv) archived `mobility.yaml` | Same notch; segments → atoms",
        ),
        (
            "5 — Row 51 meta gate | Confirm [VII.2 → VII.3 reunion index (row 51)](appendix/sources.md#vii2-vii3-opening-hinge-reunion-index-row-51) five-step audit | VII.2 → VII.3 before screw-core RVE",
            "5 — Row 52 meta gate | Confirm [VII.3 → VIII.1 reunion index (row 52)](appendix/sources.md#vii3-viii1-opening-hinge-reunion-index-row-52) five-step audit | Handoff → screw-core RVE reads continuous",
        ),
        ("Name DDD meta prelude capstone before VII.2 Bridge", "Name homogenization meta prelude capstone before VII.3 Bridge"),
        ("OpenDiS exports before texture tables on capstone path", "`mobility.yaml` before EAM tables on capstone path"),
        ("Name VII.2 Bridge as chapter exit", "Name VII.3 Bridge as part exit"),
        ("Spool needs statistics", "Cores need atoms"),
        ("Name forest Lab act before polycrystal Scene", "Name handoff Lab act before VIII.1 Scene"),
        ("Drawing dies matter", "Screw-core RVE planned"),
        ("Part VII homogenization reads as one novel act", "VII.3 → VIII.1 reads continuous"),
        (
            "row 130 closed but row 51 VII.2 → VII.3 reunion still feels like DAMASK homework disconnected from verified DDD meta prelude capstone",
            "row 131 closed but row 52 VII.3 → VIII.1 reunion still feels like LAMMPS homework disconnected from verified homogenization meta prelude capstone",
        ),
        ("before the atomistic meta reunion", "before the dynamics meta reunion"),
        (
            "OpenDiS exports are clear on the capstone path but crystal plasticity decks feel disconnected from forest density after row 130",
            "`hardening.yaml` is archived on the capstone path but Hamiltonian notation feels disconnected from Peierls parameters after row 131",
        ),
        (
            "row 130 and row 51 both verify individually but **DDD meta prelude capstone and VII.2 → VII.3 opening hinge still feel like separate stories** — the break is usually skipping [VII.2's opening hinge to VII.3](part07-defects/02-dislocation-dynamics.md#opening-hinge-vii2-to-vii3), not missing Hall–Petch algebra.",
            "row 131 and row 52 both verify individually but **homogenization meta prelude capstone and VII.3 → VIII.1 opening hinge still feel like separate stories** — the break is usually skipping [VII.3's opening hinge to VIII.1](part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii3-to-viii1), not missing Lennard-Jones algebra.",
        ),
        (
            "When row 131 is complete, proceed to [row 112](preface.md#skill-navigation-row-112) when homogenization meta prelude capstone is clean but atomistic meta capstone still lags after verified polycrystal closure on the capstone path, to [row 111](preface.md#skill-navigation-row-111) for the Row 68 ↔ Row 51 homogenization meta prelude audit on the opening-hinge path alone, to [row 130](preface.md#skill-navigation-row-130) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, to [row 51](preface.md#skill-navigation-row-51) for the VII.2 → VII.3 meta audit alone",
            "When row 132 is complete, proceed to [row 113](preface.md#skill-navigation-row-113) when atomistic meta prelude capstone is clean but dynamics meta capstone still lags after verified screw-core closure on the capstone path, to [row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta prelude audit on the opening-hinge path alone, to [row 131](preface.md#skill-navigation-row-131) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path, to [row 52](preface.md#skill-navigation-row-52) for the VII.3 → VIII.1 meta audit alone",
        ),
        ("Row 68 → Row 111 homogenization meta prelude capstone reunion index", "Row 68 → Row 112 atomistic meta prelude capstone reunion index"),
        ("Row 68 → Row 111 reunion index", "Row 68 → Row 112 reunion index"),
        ("read row 68 gate + row 130 or row 111 DDD meta prelude capstone / homogenization meta prelude gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51 meta aloud",
         "read row 68 gate + row 131 or row 112 homogenization meta prelude capstone / atomistic meta prelude gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52 meta aloud"),
        (
            "when Peach–Köhler DDD is clean on the capstone path but DAMASK decks feel like CP homework after verified DDD meta prelude capstone",
            "when polycrystal handoff is clean on the capstone path but LAMMPS decks feel like AtomModel homework after verified homogenization meta prelude capstone",
        ),
        (
            "When row 130 closed — DDD meta prelude capstone verified, row 129 or row 50 recited, and VII.1 Bridge → VII.2 Peach–Köhler recited with forest-density Lab act linked \\(\\tau(\\gamma)\\) to Taylor hardening on the capstone path — but **row 51 VII.2 → VII.3 opening hinge still opens like standalone DAMASK homework after the post-yield forest Scene**",
            "When row 131 closed — homogenization meta prelude capstone verified, row 130 or row 51 recited, and VII.2 Bridge → VII.3 polycrystal recited with handoff Lab act archived `mobility.yaml` on the capstone path — but **row 52 VII.3 → VIII.1 opening hinge still opens like standalone LAMMPS homework after the mesoscale export Scene**",
        ),
        (
            "`writings/defects` chapters 02 and 03 build as separate reading acts, Voce calibration and texture tables feel disconnected from \\(\\tau(\\rho)\\) on the single-crystal RVE, or row 51's Bridge → homogenization audit feels disconnected from row 130's segment-network → spool closure",
            "`writings/defects` chapter 03 and `writings/md` chapter 01 build as separate reading acts, EAM parameter tables feel disconnected from Peierls thresholds at \\(T_w\\), or row 52's Bridge → phase-space audit feels disconnected from row 131's polycrystal → atomic ink closure",
        ),
        ("before row 52 atomistic meta prelude capstone opens", "before row 53 dynamics meta prelude capstone opens"),
        (
            "Explain why midpoint closure (row 68) and VII.2 → VII.3 meta (row 51) must be read together with the Bridge → homogenization chain after verified DDD meta prelude capstone before OpenDiS exports and DAMASK texture tables feel like separate courses on the capstone path",
            "Explain why midpoint closure (row 68) and VII.3 → VIII.1 meta (row 52) must be read together with the Bridge → phase-space chain after verified homogenization meta prelude capstone before polycrystal handoff folders and LAMMPS EAM decks feel like separate courses on the capstone path",
        ),
        (
            "row 130 closed DDD meta prelude capstone and row 68 closed the midpoint prelude but **row 51 VII.2 → VII.3 opening hinge still opens like standalone DAMASK homework after the forest-density Lab act on the capstone path** while VII.2 Bridge and polycrystal handoff sections read correctly in isolation. Row 131 closes the **homogenization meta prelude capstone at the third numbered chapter inside Part VII in reading time on the capstone path**: verified DDD meta prelude capstone closure (row 130) and Row 68 → Row 51 meta (row 111) must read as one OpenDiS → polycrystal afternoon before row 52 atomistic meta prelude opens in workflow time.",
            "row 131 closed homogenization meta prelude capstone and row 68 closed the midpoint prelude but **row 52 VII.3 → VIII.1 opening hinge still opens like standalone LAMMPS homework after the handoff Lab act on the capstone path** while VII.3 Bridge and VIII.1 phase-space sections read correctly in isolation. Row 132 closes the **atomistic meta prelude capstone at the defects → md subtree boundary in reading time on the capstone path**: verified homogenization meta prelude capstone closure (row 131) and Row 68 → Row 52 meta (row 112) must read as one spool → screw-core afternoon before row 53 dynamics meta prelude opens in workflow time.",
        ),
        (
            "When row 51 feels like DAMASK homework after row 130 alone on the capstone path, start at [VII.2 Bridge to VII.3]",
            "When row 52 feels like LAMMPS homework after row 131 alone on the capstone path, start at [VII.3 Bridge to Part VIII]",
        ),
        (
            "read through [VII.2 opening hinge to VII.3]",
            "read through [VII.3 opening hinge to VIII.1]",
        ),
        (
            "then [VII.3 opening hinge from VII.2]",
            "then [VIII.1 opening hinge from VII.3]",
        ),
        (
            "and [VII.3 plot spine]",
            "and [VIII.1 plot spine]",
        ),
        ("before the [row 51 closing loop]", "before the [row 52 closing loop]"),
        ("Open [preface row 51]", "Open [preface row 52]"),
        ("Bridge → homogenization contract per [row 91]", "Bridge → phase-space contract per [row 72]"),
        ("Recite [preface row 130]", "Recite [preface row 131]"),
        ("split DDD meta prelude capstone from homogenization reunion", "split homogenization meta prelude capstone from atomistic reunion"),
        ("Confirm [forest-density Lab act]", "Confirm [handoff Lab act step 5]"),
        ("linked \\(\\tau(\\gamma)\\) to Taylor hardening per [row 50]", "archived `mobility.yaml` before EAM minimize per [row 51]"),
        (
            "Do not conflate row 131 (row 68 ↔ row 51 reunion on the capstone path) with row 111 (opening-hinge prelude stitch alone) — row 111 names **Row 68 → Row 91 Row 68 → Row 51 homogenization meta prelude reunion**; row 131 names **why that reunion must follow verified DDD meta prelude capstone (row 130) and the outer midpoint prelude gate (row 68)**. Proceed to [row 112](#row-112-closing-loop) when row 68 closed but atomistic meta capstone still lags after row 131 on the capstone path, to [row 111](#row-111-closing-loop) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge path alone, to [row 130](#row-130-closing-loop) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, to [row 51](#row-51-closing-loop) when only VII.2 → VII.3 stalls",
            "Do not conflate row 132 (row 68 ↔ row 52 reunion on the capstone path) with row 112 (opening-hinge prelude stitch alone) — row 112 names **Row 68 → Row 92 Row 68 → Row 52 atomistic meta prelude reunion**; row 132 names **why that reunion must follow verified homogenization meta prelude capstone (row 131) and the outer midpoint prelude gate (row 68)**. Proceed to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the capstone path, to [row 112](#row-112-closing-loop) for the Row 68 ↔ Row 52 atomistic meta audit on the opening-hinge path alone, to [row 131](#row-131-closing-loop) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path, to [row 52](#row-52-closing-loop) when only VII.3 → VIII.1 stalls",
        ),
        (
            "| 131 | Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone ↔ row 51 meta) |",
            "| 132 | Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone (midpoint prelude gate ↔ homogenization meta prelude capstone ↔ row 52 meta) |",
        ),
        (
            "Row 68 closed but **row 51 VII.2 → VII.3 opening hinge still feels disconnected from verified DDD meta prelude capstone on the capstone path** — read row 68 + row 130 or row 111 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51",
            "Row 68 closed but **row 52 VII.3 → VIII.1 opening hinge still feels disconnected from verified homogenization meta prelude capstone on the capstone path** — read row 68 + row 131 or row 112 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52",
        ),
        (
            "Row 111 names **Row 68 → Row 91 Row 68 → Row 51 homogenization meta prelude reunion** at opening-prelude depth (midpoint prelude gate + VII.2 Bridge → opening hinge + row 51 meta); row 51 names **VII.2 → VII.3 opening hinge reunion** when texture tables stall after forest-density Lab act; row 130 names **Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion** when taxonomy meta prelude capstone and VII.1 → VII.2 meta must read as one afternoon on the capstone path. Row 131 names",
            "Row 112 names **Row 68 → Row 92 Row 68 → Row 52 atomistic meta prelude reunion** at opening-prelude depth (midpoint prelude gate + VII.3 Bridge → opening hinge + row 52 meta); row 52 names **VII.3 → VIII.1 opening hinge reunion** when EAM tables stall after handoff Lab act; row 131 names **Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion** when DDD meta prelude capstone and VII.2 → VII.3 meta must read as one afternoon on the capstone path. Row 132 names",
        ),
        (
            "when row 68 closed the dual midpoint prelude and row 130 or row 111 closed DDD meta prelude capstone / homogenization meta prelude with VII.1 Bridge → VII.2 Peach–Köhler recited and forest-density Lab act linked \\(\\tau(\\gamma)\\) to Taylor hardening on the capstone path, but **row 51 still opens like standalone DAMASK homework after VII.2's post-yield forest Scene**",
            "when row 68 closed the dual midpoint prelude and row 131 or row 112 closed homogenization meta prelude capstone / atomistic meta prelude with VII.2 Bridge → VII.3 polycrystal recited and handoff Lab act archived `mobility.yaml` on the capstone path, but **row 52 still opens like standalone LAMMPS homework after VII.3's mesoscale export Scene**",
        ),
        (
            "midpoint prelude ↔ homogenization meta prelude capstone path. Read aloud when row 130 verified VII.1 → VII.2 on Peach–Köhler forces on the capstone path but the **Row 68 → Row 51 reunion index** still feels like standalone DAMASK homework",
            "midpoint prelude ↔ atomistic meta prelude capstone path. Read aloud when row 131 verified VII.2 → VII.3 on texture exports on the capstone path but the **Row 68 → Row 52 reunion index** still feels like standalone LAMMPS homework",
        ),
        ("Row 68 → Row 51 move (capstone path)", "Row 68 → Row 52 move (capstone path)"),
        ("Opening row 51 with DDD meta prelude capstone skipped", "Opening row 52 with homogenization meta prelude capstone skipped"),
        (
            "[Row 130 reunion (DDD meta prelude capstone)](#row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130) | DDD meta prelude capstone | \"Row 130 or row 111 gate before VII.2 Bridge\" | Peach–Köhler clean but polycrystal still separate acts",
            "[Row 131 reunion (homogenization meta prelude capstone)](#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131) | Homogenization meta prelude capstone | \"Row 131 or row 112 gate before VII.3 Bridge\" | Polycrystal clean but LAMMPS opens early",
        ),
        (
            "[Row 111 reunion (meta prelude)](#row68-row91-homogenization-meta-prelude-reunion-index-row-111) | Homogenization meta prelude | \"Row 68 gate + capstone before row 51\" | Row 130 only; VII.2 Bridge chain skipped",
            "[Row 112 reunion (meta prelude)](#row68-row92-atomistic-meta-prelude-reunion-index-row-112) | Atomistic meta prelude | \"Row 68 gate + capstone before row 52\" | Row 131 only; VII.3 Bridge chain skipped",
        ),
        (
            "[Row 91 reunion (opening)](#row68-row71-homogenization-meta-prelude-reunion-index-row-91) | Homogenization opening | \"DDD meta prelude capstone before row 51\" | Row 111 only; row 51 meta skipped",
            "[Row 92 reunion (opening)](#row68-row72-atomistic-meta-prelude-reunion-index-row-92) | Atomistic opening | \"Homogenization meta prelude capstone before row 52\" | Row 112 only; row 52 meta skipped",
        ),
        (
            "[Row 51 reunion (meta)](#vii2-vii3-opening-hinge-reunion-index-row-51) | Homogenization prelude meta | \"Row 130 gate + Bridge before VII.3\" | Row 91 only; row 51 meta skipped",
            "[Row 52 reunion (meta)](#vii3-viii1-opening-hinge-reunion-index-row-52) | Atomistic prelude meta | \"Row 131 gate + Bridge before VIII.1\" | Row 92 only; row 52 meta skipped",
        ),
        (
            "[VII.2 Bridge to VII.3](../part07-defects/02-dislocation-dynamics.md#bridge-to-vii3) | Chapter exit | \"One orientation vs cold-drawn spool\" | DAMASK before forest-density Lab act",
            "[VII.3 Bridge to Part VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) | Part exit | \"Ink is atomic bonding\" | Skipping Bridge before EAM tables",
        ),
        (
            "[VII.3 opening hinge from VII.2](../part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii2-to-vii3) | Third chapter entry | \"Texture statistics on same wire as \\(\\tau(\\rho)\\)\" | Part VIII opens before VII.3 landing",
            "[VIII.1 opening hinge from VII.3](../part08-md/01-potentials-phase-space.md#opening-hinge-vii3-to-viii1) | Downstream chapter hinge | \"Segments → atoms at the notch\" | MD read as standalone notes",
        ),
        (
            "[VII.2 forest-density Lab act](../part07-defects/02-dislocation-dynamics.md#lab-act-read-the-hardening-bend-from-forest-density-act-iv) | Forest export gate | \"\\(\\tau(\\gamma)\\), \\(\\rho(\\gamma)\\) before Voce yaml\" | Texture tables without OpenDiS pedigree",
            "[Handoff Lab act step 5](../part07-defects/03-polycrystal-and-fem-handoff.md#lab-act-archive-the-opendis--damask--fem-handoff-act-ivv) | Mobility contract gate | \"`mobility.yaml` before Hamiltonian\" | EAM minimize without OpenDiS pedigree",
        ),
        (
            "[Preface row 131](../preface.md#skill-navigation-row-131) | Competence-time | \"Recite row 68 gate, then DDD meta prelude capstone, then row 51\" | Row 68 only; homogenization meta prelude capstone skipped",
            "[Preface row 132](../preface.md#skill-navigation-row-132) | Competence-time | \"Recite row 68 gate, then homogenization meta prelude capstone, then row 52\" | Row 68 only; atomistic meta prelude capstone skipped",
        ),
        (
            "**Spot audit (Row 68 → Row 51 gate, capstone path).** When [row 68]",
            "**Spot audit (Row 68 → Row 52 gate, capstone path).** When [row 68]",
        ),
        (
            "[row 130](#row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130) or [row 111](#row68-row91-homogenization-meta-prelude-reunion-index-row-111) archived DDD meta prelude capstone / homogenization meta prelude with forest-density Lab act linked \\(\\tau\\) to \\(\\sqrt{\\rho}\\) on the capstone path, but **row 51 VII.2 → VII.3 reunion still feels disconnected from verified DDD meta prelude capstone**, open [VII.2 opening hinge to VII.3]",
            "[row 131](#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131) or [row 112](#row68-row92-atomistic-meta-prelude-reunion-index-row-112) archived homogenization meta prelude capstone / atomistic meta prelude with handoff Lab act step 5 linked `mobility.yaml` at \\(T_w\\) on the capstone path, but **row 52 VII.3 → VIII.1 reunion still feels disconnected from verified homogenization meta prelude capstone**, open [VII.3 opening hinge to VIII.1]",
        ),
        ("then open [row 51](#vii2-vii3-opening-hinge-reunion-index-row-51). Row 131 does not replace", "then open [row 52](#vii3-viii1-opening-hinge-reunion-index-row-52). Row 132 does not replace"),
        (
            "row 51 (meta stitch), row 130 (DDD meta prelude capstone), row 111 (Row 68 ↔ Row 51 opening prelude), row 91 (homogenization gate)",
            "row 52 (meta stitch), row 131 (homogenization meta prelude capstone), row 112 (Row 68 ↔ Row 52 opening prelude), row 92 (atomistic gate)",
        ),
        (
            "it reunites **verified DDD meta prelude capstone closure with the homogenization meta reunion** when DDD capstone and VII.2 Bridge both read correctly in isolation but not as one continuous OpenDiS → polycrystal afternoon before row 52 atomistic meta prelude opens on the capstone path.",
            "it reunites **verified homogenization meta prelude capstone closure with the atomistic meta reunion** when handoff exports and row 52 meta both read correctly in isolation but not as one continuous spool → screw-core afternoon before row 53 dynamics meta prelude opens on the capstone path.",
        ),
        (
            "**Baby picture:** row 130 tells you **why verified DDD meta prelude capstone demands VII.2 Bridge before any texture proof on row 51 on the capstone path**; row 51 tells you **why VII.2 → VII.3 must read as one novel act at the forest Scene after DDD meta prelude capstone closes** — same copper wire, segment networks yield to texture statistics, same Functional Analysis Notes layout, one continuous DDD → homogenization arc.",
            "**Baby picture:** row 131 tells you **why verified homogenization meta prelude capstone demands VII.3 Bridge before any EAM proof on row 52 on the capstone path**; row 52 tells you **why VII.3 → VIII.1 must read as one novel act at the handoff Scene after homogenization meta prelude capstone closes** — same copper wire, texture statistics yield to atomic bonding, same Functional Analysis Notes layout, one continuous homogenization → atomistic arc.",
        ),
        (
            "**Row 131 baby picture:** when row 68 closed the midpoint prelude and row 130 or row 111 closed DDD meta prelude capstone / homogenization meta prelude but **row 51's VII.2 Bridge → polycrystal handoff still feels like separate courses on the capstone path**",
            "**Row 132 baby picture:** when row 68 closed the midpoint prelude and row 131 or row 112 closed homogenization meta prelude capstone / atomistic meta prelude but **row 52's VII.3 Bridge → phase-space handoff still feels like separate courses on the capstone path**",
        ),
        (
            "→ [preface row 130](../preface.md#skill-navigation-row-130) or [preface row 111](../preface.md#skill-navigation-row-111) DDD meta prelude capstone / homogenization meta prelude gate → [VII.2 Bridge to VII.3]",
            "→ [preface row 131](../preface.md#skill-navigation-row-131) or [preface row 112](../preface.md#skill-navigation-row-112) homogenization meta prelude capstone / atomistic meta prelude gate → [VII.3 Bridge to Part VIII]",
        ),
        (
            "→ [preface row 51](../preface.md#skill-navigation-row-51) five-step audit → confirm forest-density Lab act linked \\(\\tau(\\gamma)\\) before row 52 atomistic meta prelude capstone opens.",
            "→ [preface row 52](../preface.md#skill-navigation-row-52) five-step audit → confirm handoff Lab act step 5 archived `mobility.yaml` before row 53 dynamics meta prelude capstone opens.",
        ),
        ("DM[DDD meta prelude capstone row 130]", "HM[Homogenization meta prelude capstone row 131]"),
        ("BR[VII.2 Bridge]", "BR[VII.3 Bridge]"),
        ("R51[row 51 meta gate]", "R52[row 52 meta gate]"),
        (
            "When row 131 feels disconnected from row 130, read them as **DDD meta prelude capstone vs homogenization meta prelude capstones**: row 130 when **VII.1 Bridge and Row 68 → Row 50 meta must read on the same wire before any VII.2 → VII.3 audit on the capstone path**; row 131 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before row 112 atomistic meta capstone or row 52 atomistic reunion opens on the capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous OpenDiS → polycrystal afternoon. When row 130 closed but homogenization meta reunion still lags on the capstone path, switch to [row 131]",
            "When row 132 feels disconnected from row 131, read them as **homogenization meta prelude capstone vs atomistic meta prelude capstones**: row 131 when **VII.2 Bridge and Row 68 → Row 51 meta must read on the same wire before any VII.3 → VIII.1 audit on the capstone path**; row 132 when **VII.3 Bridge and Row 68 → Row 52 meta must read on the same wire before row 113 dynamics meta capstone or row 53 dynamics reunion opens on the capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous spool → screw-core afternoon. When row 131 closed but atomistic meta reunion still lags on the capstone path, switch to [row 132]",
        ),
    ]
    for a, b in pairs:
        text = text.replace(a, b)
    # Row id bumps for the new checkpoint only
    text = re.sub(r"\bRow 131 skill checkpoint", "Row 132 skill checkpoint", text)
    text = re.sub(r"skill-navigation-row-131\b", "skill-navigation-row-132", text)
    text = re.sub(r"prologue-preview-row-131\b", "prologue-preview-row-132", text)
    text = re.sub(r"row-131-closing-stitch\b", "row-132-closing-stitch", text)
    text = re.sub(r"row-131-closing-loop\b", "row-132-closing-loop", text)
    text = re.sub(r"\*\*Row 131 three-way audit", "**Row 132 three-way audit", text)
    text = re.sub(r"\*\*Row 131 baby picture", "**Row 132 baby picture", text)
    text = re.sub(r"### Row 131 baby picture", "### Row 132 baby picture", text)
    text = re.sub(r"### Row 131 closing loop", "### Row 132 closing loop", text)
    text = re.sub(r"\*\*Row 131 closing stitch", "**Row 132 closing stitch", text)
    text = re.sub(r"Row 131 preview", "Row 132 preview", text)
    text = re.sub(r"\| 131 \| Meta \|", "| 132 | Meta |", text)
    text = re.sub(r"memory sheet row 131 baby picture", "memory sheet row 132 baby picture", text)
    text = re.sub(r"prologue row 131 ", "prologue row 132 ", text)
    text = re.sub(r"epilogue row 131 ", "epilogue row 132 ", text)
    text = re.sub(r"preface row 131 skill checkpoint", "preface row 132 skill checkpoint", text)
    text = re.sub(r"\[row 131\]\(prologue", "[row 132](prologue", text)
    text = re.sub(r"Step 5 — row 51 meta gate", "Step 5 — row 52 meta gate", text)
    return text


def main() -> None:
    text = SRC.read_text()
    text = text.replace(
        "Add row 131 meta-stitch (Row 68 → Row 111 ↔ Row 51 homogenization meta prelude capstone on capstone path).",
        "Add row 132 meta-stitch (Row 68 → Row 112 ↔ Row 52 atomistic meta prelude capstone on capstone path).",
    )
    text = text.replace("ROW131_", "ROW132_")
    text = text.replace("fix_row130_prologue", "fix_row131_prologue")
    text = text.replace("PROLOGUE_STITCH_130", "PROLOGUE_STITCH_131")
    text = text.replace("PROLOGUE_PREVIEW_130", "PROLOGUE_PREVIEW_131")

    for const in (
        "ROW132_PREFACE",
        "PROLOGUE_COMPASS",
        "PROLOGUE_STITCH_131",
        "PROLOGUE_PREVIEW_131",
        "EPILOGUE_LOOP",
        "SOURCES_TABLE",
        "SOURCES_INDEX",
        "MEMORY_TABLE",
        "MEMORY_BABY",
    ):
        pat = rf"{const} = (?:r'''|\(\n)(.*?)(?:'''|\n\))"
        m = re.search(pat, text, re.S)
        if not m:
            continue
        block = m.group(1)
        new_block = transform(block)
        if const == "PROLOGUE_STITCH_131":
            # Keep row 131 backfill stitch; add row 132 stitch after it
            stitch132 = transform(
                block.replace("Row 131 closing stitch", "Row 132 closing stitch").replace(
                    "row-131-closing-stitch", "row-132-closing-stitch"
                )
            )
            old = f"PROLOGUE_STITCH_131 = (\n{block}\n)"
            new = f"PROLOGUE_STITCH_131 = (\n{block}\n)\n\nPROLOGUE_STITCH_132 = (\n{stitch132}\n)"
            text = text.replace(old, new)
            continue
        if const.startswith("PROLOGUE_PREVIEW"):
            old = f"PROLOGUE_PREVIEW_131 = (\n{block}\n)"
            new = f"PROLOGUE_PREVIEW_131 = (\n{block}\n)\n\nPROLOGUE_PREVIEW_132 = (\n{transform(block.replace('Row 131 preview', 'Row 132 preview').replace('prologue-preview-row-131', 'prologue-preview-row-132'))}\n)"
            text = text.replace(old, new)
            continue
        if " = r'''" in text[text.find(const) : text.find(const) + 40]:
            text = text.replace(f"{const} = r'''{block}'''", f"{const} = r'''{new_block}'''", 1)
        elif const == "PROLOGUE_COMPASS":
            text = text.replace(f"PROLOGUE_COMPASS = (\n{block}\n)", f"PROLOGUE_COMPASS = (\n{new_block}\n)", 1)

    # main() row 132 logic
    text = text.replace('if "skill-navigation-row-131" not in preface:', 'if "skill-navigation-row-132" not in preface:')
    text = text.replace("ROW131_PREFACE + anchor", "ROW132_PREFACE + anchor")
    text = text.replace('print("preface: added row 131")', 'print("preface: added row 132")')
    text = text.replace('print("preface: row 131 already present")', 'print("preface: row 132 already present")')
    text = text.replace("preface row 130 tail not found", "preface row 131 tail not found")
    text = text.replace(
        "Read the [memory sheet row 130 baby picture](appendix/memory-sheet.md#row-130-baby-picture-row68-row110-ddd-meta-prelude-capstone-reunion) when opening [row 131](preface.md#skill-navigation-row-131) before row 51 closes on the capstone path; read the [epilogue row 130 closing loop](epilogue/multiscale.md#row-130-closing-loop) when the competence loop closes. When row 130 is complete, proceed to [row 131](preface.md#skill-navigation-row-131) when DDD meta prelude capstone is clean but homogenization meta prelude capstone still lags after verified Peach–Köhler closure on the capstone path, to [row 111](preface.md#skill-navigation-row-111) when DDD meta prelude capstone is clean but homogenization meta capstone still lags after verified Peach–Köhler closure on the opening-hinge path, to [row 110](preface.md#skill-navigation-row-110) for the Row 68 ↔ Row 50 DDD meta prelude audit on the opening-hinge path alone, to [row 129](preface.md#skill-navigation-row-129) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the capstone path, to [row 50](preface.md#skill-navigation-row-50) for the VII.1 → VII.2 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
        "Read the [memory sheet row 131 baby picture](appendix/memory-sheet.md#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion) when opening [row 132](preface.md#skill-navigation-row-132) before row 52 closes on the capstone path; read the [epilogue row 131 closing loop](epilogue/multiscale.md#row-131-closing-loop) when the competence loop closes. When row 131 is complete, proceed to [row 132](preface.md#skill-navigation-row-132) when homogenization meta prelude capstone is clean but atomistic meta prelude capstone still lags after verified polycrystal closure on the capstone path, to [row 112](preface.md#skill-navigation-row-112) when homogenization meta prelude capstone is clean but atomistic meta capstone still lags after verified polycrystal closure on the opening-hinge path, to [row 111](preface.md#skill-navigation-row-111) for the Row 68 ↔ Row 51 homogenization meta prelude audit on the opening-hinge path alone, to [row 130](preface.md#skill-navigation-row-130) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, to [row 51](preface.md#skill-navigation-row-51) for the VII.2 → VII.3 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
    )

    text = text.replace("prologue = fix_row130_prologue(prologue)", "prologue = fix_row131_prologue(prologue)")
    text = text.replace('if "prologue-preview-row-131" not in prologue:', 'if \'<span id="prologue-preview-row-132">\' not in prologue:')
    text = text.replace(
        'needle = "| Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion (row 130) |"',
        'needle = "| Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 131) |"',
    )
    text = text.replace('raise SystemExit("prologue compass row 130 not found")', 'raise SystemExit("prologue compass row 131 not found")')
    text = text.replace('if "row-131-closing-stitch" not in prologue:', 'if "row-132-closing-stitch" not in prologue:')
    text = text.replace(
        'prologue = prologue.replace(\n                "**Row 130 closing stitch",\n                PROLOGUE_STITCH_131 + "**Row 130 closing stitch",\n            )',
        'prologue = prologue.replace(\n                "**Row 131 closing stitch",\n                PROLOGUE_STITCH_132 + "**Row 131 closing stitch",\n            )',
    )
    text = text.replace(
        'if "prologue-preview-row-131" not in prologue:',
        'if \'<span id="prologue-preview-row-132">\' not in prologue:',
    )
    text = text.replace(
        '| <span id="prologue-preview-row-130"></span>Row 130 preview',
        '| <span id="prologue-preview-row-131"></span>Row 131 preview',
    )
    text = text.replace(
        "PROLOGUE_PREVIEW_131 + '| <span id=\"prologue-preview-row-130\"></span>Row 130 preview",
        "PROLOGUE_PREVIEW_132 + '| <span id=\"prologue-preview-row-131\"></span>Row 131 preview",
    )
    text = text.replace('print("prologue: added row 131")', 'print("prologue: added row 132")')
    text = text.replace(
        'print("prologue: row 131 already present (row 130 backfill applied if needed)")',
        'print("prologue: row 132 already present (row 131 backfill applied if needed)")',
    )

    text = text.replace('if "row-131-closing-loop" not in epilogue:', 'if "row-132-closing-loop" not in epilogue:')
    text = text.replace(
        "\n### Row 130 closing loop (Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "\n### Row 131 closing loop (Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
    )
    text = text.replace(
        "Proceed to [row 131](#row-131-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 130 on the capstone path, to [row 111](#row-111-closing-loop) when row 68 closed but homogenization meta capstone still lags after row 130 on the opening-hinge path, to [row 110](#row-110-closing-loop) for the Row 68 ↔ Row 50 DDD meta audit on the opening-hinge path alone,",
        "Proceed to [row 132](#row-132-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 131 on the capstone path, to [row 112](#row-112-closing-loop) when row 68 closed but atomistic meta capstone still lags after row 131 on the opening-hinge path, to [row 111](#row-111-closing-loop) for the Row 68 ↔ Row 51 homogenization meta audit on the opening-hinge path alone,",
    )
    text = text.replace('print("epilogue: added row 131")', 'print("epilogue: added row 132")')

    text = text.replace(
        'if "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131" not in sources:',
        'if "row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132" not in sources:',
    )
    text = text.replace(
        "| 130 | Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone",
        "| 131 | Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 130)",
        "## Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 131)",
    )
    text = text.replace(
        "[row 131](#row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131) reunites **DDD meta prelude capstone with the homogenization meta prelude capstone boundary** when row 130 closed DDD meta prelude capstone at verified Peach–Köhler closure on the capstone path but OpenDiS exports and VII.2 → VII.3 opening hinge still read like separate courses after verified homogenization meta prelude meta;",
        "[row 132](#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary** when row 131 closed homogenization meta prelude capstone at verified polycrystal closure on the capstone path but `mobility.yaml` and VII.3 → VIII.1 opening hinge still read like separate courses after verified atomistic meta prelude meta;",
    )
    text = text.replace('print("sources: added row 131")', 'print("sources: added row 132")')

    text = text.replace('if "row-131-baby-picture" not in mem:', 'if "row-132-baby-picture" not in mem:')
    text = text.replace(
        "[row 130 baby picture](#row-130-baby-picture-row68-row110-ddd-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
        "[row 131 baby picture](#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
    )
    text = text.replace("When row 130 feels disconnected from row 129", "When row 131 feels disconnected from row 130")
    text = text.replace("When row 130 closed but homogenization meta reunion still lags", "When row 131 closed but atomistic meta reunion still lags")
    text = text.replace("row 131 homogenization meta prelude capstone or row 51 homogenization reunion", "row 132 atomistic meta prelude capstone or row 52 atomistic reunion")
    text = text.replace("switch to [row 131](#row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion)", "switch to [row 132](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion)")
    text = text.replace('if "row-131-baby-picture-row68-row111" not in mem:', 'if "row-132-baby-picture-row68-row112" not in mem:')
    text = text.replace('print("memory-sheet: added row 131")', 'print("memory-sheet: added row 132")')

    # fix_row131 backfill detection
    text = text.replace(
        'def fix_row131_prologue(prologue: str) -> str:\n    if "row-131-closing-stitch" not in prologue:',
        'def fix_row131_prologue(prologue: str) -> str:\n    if \'<span id="prologue-preview-row-131">\' not in prologue:',
    )
    text = text.replace(
        '    if "row-131-closing-stitch" not in prologue:\n        prologue = prologue.replace(\n            "**Row 130 closing stitch",\n            PROLOGUE_STITCH_131 + "**Row 130 closing stitch",\n        )\n    if \'<span id="prologue-preview-row-131">\' not in prologue:\n        prologue = prologue.replace(\n            \'| <span id="prologue-preview-row-130"></span>Row 129 preview\',\n            PROLOGUE_PREVIEW_131 + \'| <span id="prologue-preview-row-130"></span>Row 129 preview\',\n        )',
        '    if "{#row-131-closing-stitch}" not in prologue:\n        prologue = prologue.replace(\n            "**Row 130 closing stitch",\n            PROLOGUE_STITCH_131 + "**Row 130 closing stitch",\n        )\n    if \'<span id="prologue-preview-row-131">\' not in prologue:\n        prologue = prologue.replace(\n            \'| <span id="prologue-preview-row-130"></span>Row 130 preview\',\n            PROLOGUE_PREVIEW_131 + \'| <span id="prologue-preview-row-130"></span>Row 130 preview\',\n        )',
    )

    DST.write_text(text)
    print(f"Wrote {DST}")


if __name__ == "__main__":
    main()