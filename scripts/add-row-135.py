#!/usr/bin/env python3
"""Apply row 135 meta-stitch and backfill incomplete row 134 prologue/memory pieces."""
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(ROOT / "scripts/add-row-134.py"))


def tx(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


P = [
    ("134", "135"),
    ("133", "134"),
    ("114", "115"),
    ("54", "55"),
    ("Row 114", "Row 115"),
    ("row 114", "row 115"),
    (
        "export meta prelude capstone reunion (row 134)",
        "electronic audit meta prelude capstone reunion (row 135)",
    ),
    (
        "Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone",
        "Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone",
    ),
    (
        "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
    ),
    (
        "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
        "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
    ),
    (
        "dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54",
        "export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55",
    ),
    (
        "NPT dynamics is clean on the capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone",
        "pedigree checklist is clean on the capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone",
    ),
]

ROW135_PREFACE = tx(
    ns["ROW134_PREFACE"],
    P
    + [
        ("dynamics meta prelude capstone", "export meta prelude capstone"),
        ("export meta prelude capstone", "electronic audit meta prelude capstone"),
        (
            "dynamics meta prelude capstone / export meta prelude hinge",
            "export meta prelude capstone / electronic audit meta prelude hinge",
        ),
        (
            "dynamics meta prelude capstone / export meta prelude gate",
            "export meta prelude capstone / electronic audit meta prelude gate",
        ),
        (
            "standalone coarse-graining homework after VIII.2's NPT Lab act",
            "standalone DFT coursework after VIII.3's EAM-fit audit Lab act",
        ),
        (
            "[NPT Lab act](part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` and `mobility_cu_screw_{T_w}K.yaml` beside [dynamics export manifest](part08-md/02-ensembles-integrators.md#dynamics-export-manifest-handoff-to-viii3)",
            "[EAM-fit audit Lab act](part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` and `eam_fit_audit.log` beside [coarse-graining export manifest](part08-md/03-ab-initio-and-coarse-graining.md#coarse-graining-export-manifest-handoff-to-ix)",
        ),
        ("one NPT → pedigree arc under `writings/md` chapters 02–03", "one pedigree → foundation SCF arc under `writings/md` chapter 03 and `writings/dft` chapter 00"),
        (
            "[VIII.2 Bridge](part08-md/02-ensembles-integrators.md#bridge) reads correctly in isolation from [VIII.3 pedigree checklist](part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3)",
            "[VIII.3 Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) reads correctly in isolation from [IX.0 opening hinge from VIII.3](part09-dft/00-opening.md#opening-hinge-viii3-to-ix)",
        ),
        (
            "consumer columns in the checklist feel disconnected from NVE drift certificates",
            "plane-wave tables feel disconnected from the DFT evidence column",
        ),
        (
            "rear-view mirror of row 133's finite-\\(T\\) dynamics → yaml handoff turn at the export meta prelude capstone boundary",
            "rear-view mirror of row 134's yaml pedigree → foundation SCF turn at the electronic audit meta prelude capstone boundary",
        ),
        ("(VIII.2 → VIII.3 meta gate)", "(VIII.3 → IX.0 meta gate)"),
        (
            "verified dynamics meta prelude capstone closure (row 133) with the full-book VIII.2 → VIII.3 export meta reunion (row 54)",
            "verified export meta prelude capstone closure (row 134) with the full-book VIII.3 → IX.0 electronic audit meta reunion (row 55)",
        ),
        (
            "`cu.elastic/` and row 54 meta both read correctly alone but not as one continuous NPT afternoon → pedigree checklist before row 55 electronic audit meta prelude opens",
            "`pedigree_checklist.yaml` and row 55 meta both read correctly alone but not as one continuous pedigree → SCF afternoon before row 56 Born–Oppenheimer meta prelude opens",
        ),
        ("Row 68 ↔ Row 54 reunion (capstone path)", "Row 68 ↔ Row 55 reunion (capstone path)"),
        ("before export meta prelude capstone", "before electronic audit meta prelude capstone"),
        (
            "[Row 68 → Row 94 export meta prelude reunion index (row 114)](appendix/sources.md#row68-row94-export-meta-prelude-reunion-index-row-114)",
            "[Row 68 → Row 95 electronic audit meta prelude reunion index (row 115)](appendix/sources.md#row68-row95-electronic-audit-meta-prelude-reunion-index-row-115)",
        ),
        (
            "NPT archive at \\(T_w\\) before VIII.2 Bridge → pedigree after verified dynamics meta prelude capstone",
            "Pedigree yaml at \\(T_w\\) before VIII.3 Bridge → SCF after verified export meta prelude capstone",
        ),
        (
            "Read [VIII.2 Bridge](part08-md/02-ensembles-integrators.md#bridge) through [VIII.3 opening hinge from VIII.2](part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3) aloud",
            "Read [VIII.3 Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) through [IX.0 opening hinge from VIII.3](part09-dft/00-opening.md#opening-hinge-viii3-to-ix) aloud",
        ),
        (
            '"Trajectories compress into handoff tables with DFT pedigree gates"',
            '"EAM on trust needs Born–Oppenheimer re-derivation"',
        ),
        (
            "Open [VIII.2 Scene](part08-md/02-ensembles-integrators.md#scene-thermometers-in-a-nanoscale-lab) then [VIII.3 Scene](part08-md/03-ab-initio-and-coarse-graining.md#scene-when-eam-is-not-enough); confirm [NPT Lab act steps 1–7](part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment)",
            "Open [VIII.3 Scene](part08-md/03-ab-initio-and-coarse-graining.md#scene-when-eam-is-not-enough) then [IX.0 Scene](part09-dft/00-opening.md#scene); confirm [EAM-fit audit Lab act steps 1–6](part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch)",
        ),
        ("Same wire; bulk NPT → notch EAM trust", "Same wire; yaml pedigree → \\(\\rho(\\mathbf{r})\\) audit"),
        (
            "Confirm [VIII.2 → VIII.3 reunion index (row 54)](appendix/sources.md#viii2-viii3-opening-hinge-reunion-index-row-54) five-step audit",
            "Confirm [VIII.3 → IX.0 reunion index (row 55)](appendix/sources.md#viii3-ix0-opening-hinge-reunion-index-row-55) five-step audit",
        ),
        ("Dynamics → pedigree reads continuous", "Pedigree yaml → SCF reads continuous"),
        ("before export meta prelude capstone", "before electronic audit meta prelude capstone"),
        ("Name dynamics meta prelude capstone before VIII.2 Bridge", "Name export meta prelude capstone before VIII.3 Bridge"),
        (
            "`cu.elastic/` before pedigree checklist on capstone path",
            "Checklist + audit at \\(T_w\\) before SCF on capstone path",
        ),
        ("Name VIII.2 Bridge as chapter exit", "Name VIII.3 Bridge as part exit"),
        ("Dumps ≠ handoff tables", "EAM trust → \\(\\rho(\\mathbf{r})\\)"),
        ("Name dynamics manifest before VIII.3 Scene", "Name EAM-fit Lab act before IX.0 Scene"),
        ("EAM fails at notch root", "Same specimen, electrons visible"),
        ("VIII.2 → VIII.3 reads continuous", "VIII.3 → IX.0 reads continuous"),
        (
            "row 133 closed but row 54 VIII.2 → VIII.3 reunion still feels like export homework disconnected from verified dynamics meta prelude capstone",
            "row 134 closed but row 55 VIII.3 → IX.0 reunion still feels like DFT homework disconnected from verified export meta prelude capstone",
        ),
        ("before the electronic audit meta reunion", "before the Born–Oppenheimer meta reunion"),
        (
            "when `cu.elastic/` exists on the capstone path but consumer columns in the checklist are empty after row 133",
            "when `pedigree_checklist.yaml` exists on the capstone path but `cu.relax.out` is missing after row 134",
        ),
        (
            "dynamics meta prelude capstone and VIII.2 → VIII.3 opening hinge still feel like separate stories",
            "export meta prelude capstone and VIII.3 → IX.0 opening hinge still feel like separate stories",
        ),
        (
            "skipping [VIII.2's Bridge](part08-md/02-ensembles-integrators.md#bridge), not missing EAM-fit algebra",
            "skipping [VIII.3's Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix), not missing k-mesh algebra",
        ),
        (
            "when opening [row 115](preface.md#skill-navigation-row-115) before row 55 closes on the capstone path",
            "when opening [row 116](preface.md#skill-navigation-row-116) before row 56 closes on the capstone path",
        ),
        ("row 133, row 114, row 94, row 74, or row 35", "row 134, row 115, row 95, row 75, or row 36"),
        ("row 54", "row 55"),
        ("row 133", "row 134"),
    ],
)

PROLOGUE_COMPASS = tx(ns["PROLOGUE_COMPASS"], P)
PROLOGUE_PREVIEW_135 = tx(
    ns["PROLOGUE_PREVIEW_134"],
    P
    + [
        ("Row 134 preview", "Row 135 preview"),
        ("prologue-preview-row-134", "prologue-preview-row-135"),
        ("VIII.2 → VIII.3 meta (row 54)", "VIII.3 → IX.0 meta (row 55)"),
        ("Bridge → pedigree chain", "Bridge → SCF audit chain"),
        (
            "dynamics manifest and coarse-graining sections",
            "pedigree checklist and Part IX sections",
        ),
        ("row-134-closing-stitch", "row-135-closing-stitch"),
        (
            "part08-md/02-ensembles-integrators.md#bridge",
            "part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix",
        ),
        (
            "part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3",
            "part09-dft/00-opening.md#opening-hinge-viii3-to-ix",
        ),
        ("preface row 54", "preface row 55"),
        ("preface row 133", "preface row 134"),
    ],
)
PROLOGUE_STITCH_135 = (
    "**Row 135 closing stitch (Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-135-closing-stitch} "
    "When row 134 closed — export meta prelude capstone verified, row 133 or row 54 recited on the capstone path, and VIII.2 Bridge → VIII.3 pedigree recited with "
    "[EAM-fit audit Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` and `eam_fit_audit.log` — but **row 55 VIII.3 → IX.0 opening hinge still opens like standalone DFT homework after the export Scene on the capstone path** — "
    "`writings/md` chapter 03 and `writings/dft` chapter 00 build as separate reading acts, plane-wave tables feel disconnected from [coarse-graining export manifest](../part08-md/03-ab-initio-and-coarse-graining.md#coarse-graining-export-manifest-handoff-to-ix) and the DFT evidence column at \\(T_w\\), or row 55's Bridge → SCF audit feels disconnected from row 134's yaml pedigree → electronic audit turn while the unified HTML reads smoothly — "
    "the [preface row 135 When-to-pause opening sentence](../preface.md#skill-navigation-row-135) names the dual reunion before Born–Oppenheimer meta reunion; read [preface row 135](../preface.md#skill-navigation-row-135), then the "
    "[Row 68 → Row 115 reunion index](../appendix/sources.md#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135), then "
    "[epilogue row 135 closing loop](../epilogue/multiscale.md#row-135-closing-loop) before row 56 Born–Oppenheimer meta prelude capstone opens.\n\n"
)

EPILOGUE_LOOP = tx(
    ns["EPILOGUE_LOOP"],
    P
    + [
        ("ensembles → coarse-graining", "coarse-graining → foundation SCF"),
        (
            "dynamics meta prelude capstone closure (row 133)",
            "export meta prelude capstone closure (row 134)",
        ),
        ("Row 68 → Row 54 meta (row 114)", "Row 68 → Row 55 meta (row 115)"),
        ("NPT → pedigree afternoon", "pedigree → foundation SCF afternoon"),
        ("row 55 electronic audit meta prelude opens", "row 56 Born–Oppenheimer meta prelude opens"),
        (
            "coarse-graining homework after the NPT Lab act on the capstone path",
            "DFT homework after the EAM-fit Lab act on the capstone path",
        ),
        (
            "VIII.2 Bridge and VIII.3 pedigree",
            "VIII.3 Bridge and IX.0 SCF",
        ),
        ("row 133 closed dynamics meta prelude", "row 134 closed export meta prelude"),
        (
            "row 54 feels like export homework after row 133",
            "row 55 feels like DFT homework after row 134",
        ),
        ("VIII.2 Bridge", "VIII.3 Bridge to Part IX"),
        ("VIII.3 plot spine", "IX.0 plot spine"),
        ("pedigree checklist", "foundation SCF audit Lab act"),
        ("row 54 closing loop", "row 55 closing loop"),
        ("row 74", "row 75"),
        ("export reunion", "electronic audit reunion"),
        (
            "dynamics meta prelude capstone",
            "export meta prelude capstone",
        ),
        ("NPT Lab act steps 1–7", "EAM-fit audit Lab act steps 1–6"),
        (
            "`cu.elastic/` and `mobility_cu_screw_{T_w}K.yaml` beside [dynamics export manifest](../part08-md/02-ensembles-integrators.md#dynamics-export-manifest-handoff-to-viii3)",
            "`pedigree_checklist.yaml` and `eam_fit_audit.log` beside [coarse-graining export manifest](../part08-md/03-ab-initio-and-coarse-graining.md#coarse-graining-export-manifest-handoff-to-ix)",
        ),
        (
            "row 68 ↔ row 54 reunion on the capstone path) with row 114 (opening-hinge prelude stitch alone) — row 114 names **Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion**; row 134 names **why that reunion must follow verified dynamics meta prelude capstone (row 133)",
            "row 68 ↔ row 55 reunion on the capstone path) with row 115 (opening-hinge prelude stitch alone) — row 115 names **Row 68 → Row 95 Row 68 → Row 55 electronic audit meta prelude reunion**; row 135 names **why that reunion must follow verified export meta prelude capstone (row 134)",
        ),
        (
            "Proceed to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 133](#row-133-closing-loop) when dynamics meta prelude capstone still lags after row 132 on the capstone path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            "Proceed to [row 116](#row-116-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 135 on the capstone path, to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta capstone still lags after row 114 on the opening-hinge path, to [row 134](#row-134-closing-loop) when export meta prelude capstone still lags after row 133 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path,",
        ),
    ],
)
EPILOGUE_LOOP = EPILOGUE_LOOP.replace("Row 134 closing loop", "Row 135 closing loop").replace(
    "row-134-closing-loop", "row-135-closing-loop"
)

SOURCES_TABLE = tx(
    ns["SOURCES_TABLE"],
    P
    + [
        (
            "dynamics meta prelude capstone ↔ row 54 meta",
            "export meta prelude capstone ↔ row 55 meta",
        ),
        ("row 54 VIII.2 → VIII.3", "row 55 VIII.3 → IX.0"),
        (
            "dynamics meta prelude capstone on the capstone path",
            "export meta prelude capstone on the capstone path",
        ),
        (
            "VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54",
            "VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55",
        ),
        ("preface row 54", "preface row 55"),
    ],
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    row134_tail_old = (
        "When row 133 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 114](preface.md#skill-navigation-row-114) when dynamics meta capstone is clean but export meta capstone still lags on the opening-hinge path, to [row 94](preface.md#skill-navigation-row-94) for the Row 68 ↔ Row 54 export opening prelude audit alone, to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone still lags after verified EAM foundation on the capstone path, to [row 54](preface.md#skill-navigation-row-54) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync."
    )
    row134_tail_new = (
        "When row 134 is complete, proceed to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone is clean but electronic audit meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 115](preface.md#skill-navigation-row-115) when export meta capstone is clean but electronic audit meta capstone still lags on the opening-hinge path, to [row 95](preface.md#skill-navigation-row-95) for the Row 68 ↔ Row 55 electronic audit opening prelude audit alone, to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync."
    )
    if "skill-navigation-row-135" not in preface:
        preface = preface.replace(row134_tail_old, row134_tail_new)
        preface = preface.replace(anchor, ROW135_PREFACE + anchor)
        preface_path.write_text(preface)
        print("preface: row 135")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if '<span id="prologue-preview-row-135">' not in prologue:
        needle = "| Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion (row 134) |"
        idx = prologue.find(needle)
        if idx < 0:
            raise SystemExit("prologue compass row 134 not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-135-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 115 closing stitch",
                PROLOGUE_STITCH_135 + "**Row 115 closing stitch",
            )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-134"></span>Row 134 preview',
            PROLOGUE_PREVIEW_135 + '| <span id="prologue-preview-row-134"></span>Row 134 preview',
        )
        print("prologue: row 135")
    prologue_path.write_text(prologue)

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-135-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "\n### Row 134 closing loop (Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion)",
            EPILOGUE_LOOP
            + "\n### Row 134 closing loop (Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion)",
        )
        epilogue = epilogue.replace(
            "Proceed to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            "Proceed to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            1,
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: row 135")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135" not in sources:
        block = sources.split(
            "## Row 68 → Row 95 Row 68 → Row 55 electronic audit meta prelude reunion index (row 115)"
        )[1].split("## Row 68 → Row 96")[0]
        block135 = tx(
            block,
            [
                ("row 115", "row 135"),
                ("Row 115", "Row 135"),
                ("row 114", "row 134"),
                ("Row 114", "Row 134"),
                ("export meta capstone", "export meta prelude capstone"),
                ("electronic audit meta capstone", "electronic audit meta prelude capstone"),
                (
                    "electronic audit meta prelude reunion index (row 115)",
                    "electronic audit meta prelude capstone reunion index (row 135)",
                ),
                (
                    "row68-row95-electronic-audit-meta-prelude-reunion-index-row-115",
                    "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
                ),
                (
                    "row-115-baby-picture-row68-row95-electronic-audit-meta-prelude-reunion",
                    "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
                ),
                ("skill-navigation-row-115", "skill-navigation-row-135"),
                (
                    "Row 68 → Row 95 Row 68 → Row 55 electronic audit meta prelude reunion",
                    "Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion",
                ),
                ("row 114 or row 95", "row 134 or row 115"),
                (
                    "VIII.2 Bridge → VIII.3 pedigree recited",
                    "VIII.3 Bridge → IX.0 SCF recited on the capstone path",
                ),
                (
                    "electronic audit meta capstone boundary",
                    "electronic audit meta prelude capstone boundary",
                ),
                (
                    "Row 114 reunion (export meta capstone)",
                    "Row 134 reunion (export meta prelude capstone)",
                ),
                (
                    "row68-row94-export-meta-prelude-reunion-index-row-114",
                    "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
                ),
                (
                    "Row 95 reunion (opening prelude)",
                    "Row 115 reunion (meta prelude)",
                ),
                (
                    "row68-row75-electronic-audit-meta-prelude-reunion-index-row-95",
                    "row68-row95-electronic-audit-meta-prelude-reunion-index-row-115",
                ),
                (
                    "Row 114 gate + Bridge before IX.0",
                    "Row 134 gate + Bridge before IX.0",
                ),
                (
                    "Recite row 68 gate, then export meta capstone, then row 55",
                    "Recite row 68 gate, then export meta prelude capstone, then row 55",
                ),
                (
                    "verified export meta capstone closure with the electronic audit meta reunion",
                    "verified export meta prelude capstone closure with the electronic audit meta reunion",
                ),
                (
                    "row 114 verified VIII.2 → VIII.3 on pedigree at \\(T_w\\)",
                    "row 134 verified VIII.2 → VIII.3 on pedigree at \\(T_w\\) on the capstone path",
                ),
                (
                    "Row 68 → Row 55 move |",
                    "Row 68 → Row 55 move (capstone path) |",
                ),
            ],
        )
        block135 = (
            "## Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 135) {#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135}"
            + block135.split("{#row68-row95-electronic-audit-meta-prelude-reunion-index-row-115}", 1)[-1]
        )
        sources = sources.replace(
            "| 134 | Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone",
            SOURCES_TABLE + "| 134 | Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion index (row 134)",
            block135
            + "## Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion index (row 134)",
        )
        extra = (
            "[row 135](#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135) reunites **export meta prelude capstone with the electronic audit meta prelude capstone boundary** "
            "when row 134 closed export meta prelude capstone at verified pedigree checklist on the capstone path but `pedigree_checklist.yaml` and VIII.3 → IX.0 opening hinge still read like separate courses after verified electronic audit meta prelude meta;"
        )
        if extra not in sources:
            sources = sources.replace(
                "when row 133 closed dynamics meta prelude capstone at verified NPT archive on the capstone path but `cu.elastic/` and VIII.2 → VIII.3 opening hinge still read like separate courses after verified export meta prelude meta;",
                "when row 133 closed dynamics meta prelude capstone at verified NPT archive on the capstone path but `cu.elastic/` and VIII.2 → VIII.3 opening hinge still read like separate courses after verified export meta prelude meta; "
                + extra,
            )
        sources_path.write_text(sources)
        print("sources: row 135")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "### Row 134 baby picture" not in mem:
        raise SystemExit("memory sheet row 134 baby picture not found")
    start = mem.index("### Row 134 baby picture")
    end = mem.index("### Act VI baby picture", start)
    memory_baby_134 = mem[start:end]

    memory_baby_135 = tx(
        memory_baby_134,
        P
        + [
            ("Row 134 baby picture", "Row 135 baby picture"),
            ("Dynamics meta prelude capstone row 133", "Export meta prelude capstone row 134"),
            ("VIII.2 Bridge", "VIII.3 Bridge to Part IX"),
            ("row 54 meta gate", "row 55 meta gate"),
            (
                "row 54's VIII.2 Bridge → pedigree handoff",
                "row 55's VIII.3 Bridge → SCF handoff",
            ),
            (
                "dynamics meta prelude capstone / export meta prelude",
                "export meta prelude capstone / electronic audit meta prelude",
            ),
            ("preface row 133", "preface row 134"),
            ("preface row 114", "preface row 115"),
            ("preface row 54", "preface row 55"),
            ("NPT Lab act steps 1–7", "EAM-fit audit Lab act steps 1–6"),
            (
                "`cu.elastic/` before row 55 electronic audit meta prelude capstone opens",
                "`pedigree_checklist.yaml` before row 56 Born–Oppenheimer meta prelude capstone opens",
            ),
            (
                "row 115 electronic audit meta capstone or row 55 electronic audit reunion",
                "row 116 Born–Oppenheimer meta capstone or row 56 BO reunion",
            ),
            ("NPT → pedigree afternoon", "pedigree → foundation SCF afternoon"),
            (
                "dynamics meta prelude capstone vs export meta prelude capstones",
                "export meta prelude capstone vs electronic audit meta prelude capstones",
            ),
            (
                "row 134 feels disconnected from row 133",
                "row 135 feels disconnected from row 134",
            ),
        ],
    )
    if "### Row 135 baby picture" not in mem:
        mem = mem.replace(
            "### Act VI baby picture (ME 412 coupling ladder)",
            memory_baby_135 + "\n\n### Act VI baby picture (ME 412 coupling ladder)",
        )
    if "| 135 | Meta |" not in mem:
        mem_table_135 = tx(
            "| 134 | Meta | Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion | "
            "[Row 68 → Row 114 export meta prelude capstone reunion index](sources.md#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) · "
            "[preface row 134 skill checkpoint](../preface.md#skill-navigation-row-134) · "
            "[prologue row 134 preview](../prologue/00-many-scales.md#prologue-preview-row-134) · "
            "[prologue row 134 closing stitch](../prologue/00-many-scales.md#row-134-closing-stitch) · "
            "[epilogue row 134 closing loop](../epilogue/multiscale.md#row-134-closing-loop) | "
            "Row 68 closed but row 54 VIII.2 → VIII.3 opening hinge feels disconnected from verified dynamics meta prelude capstone on the capstone path — "
            "read row 68 + row 133 or row 114 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
            "[row 134 baby picture](#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion) |\n",
            P
            + [
                ("row 54 VIII.2 → VIII.3", "row 55 VIII.3 → IX.0"),
                ("dynamics meta prelude capstone", "export meta prelude capstone"),
                ("VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54", "VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55"),
                ("row 133 or row 114", "row 134 or row 115"),
            ],
        )
        mem = mem.replace(
            "[row 134 baby picture](#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
            "[row 134 baby picture](#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion) |\n"
            + mem_table_135
            + "| 93 | Meta |",
        )
    if "When row 134 closed but electronic audit meta reunion still lags" not in mem:
        mem = mem.replace(
            "When row 133 closed but export meta reunion still lags on the capstone path, switch to [row 134](#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion).",
            "When row 133 closed but export meta reunion still lags on the capstone path, switch to [row 134](#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion). When row 134 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 135](#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion).",
        )
    mem_path.write_text(mem)
    print("memory: row 135")


if __name__ == "__main__":
    main()
