#!/usr/bin/env python3
"""Apply row 136 meta-stitch (Born–Oppenheimer meta capstone) from row 135 baseline."""
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(ROOT / "scripts/add-row-135.py"))


def tx(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


P_NUM = [
    ("135", "136"),
    ("134", "135"),
    ("115", "116"),
    ("55", "56"),
    ("Row 115", "Row 116"),
    ("row 115", "row 116"),
    (
        "electronic audit meta prelude capstone reunion (row 135)",
        "Born–Oppenheimer meta capstone reunion (row 136)",
    ),
    (
        "Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone",
        "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
    ),
    (
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
        "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
    ),
    (
        "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
        "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
    ),
]

P_BO = [
    ("Row 68 ↔ Row 55 reunion (capstone path)", "Row 68 ↔ Row 56 reunion (capstone path)"),
    ("before electronic audit meta prelude capstone", "before Born–Oppenheimer meta capstone"),
    (
        "export meta prelude capstone / electronic audit meta prelude hinge",
        "electronic audit meta prelude capstone / Born–Oppenheimer opening prelude hinge",
    ),
    (
        "export meta prelude capstone / electronic audit meta prelude gate",
        "electronic audit meta prelude capstone / Born–Oppenheimer opening gate",
    ),
    (
        "export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 56",
        "electronic audit meta prelude capstone / Born–Oppenheimer opening gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56",
    ),
    (
        "pedigree checklist is clean on the capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone",
        "foundation SCF logs are clean on the capstone path but IX.1 still feels like standalone quantum chemistry after verified electronic audit meta prelude capstone",
    ),
    (
        "standalone DFT coursework after VIII.3's EAM-fit audit Lab act",
        "standalone quantum chemistry after IX.0's foundation SCF audit Lab act",
    ),
    (
        "[EAM-fit audit Lab act](part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` and `eam_fit_audit.log` beside [coarse-graining export manifest](part08-md/03-ab-initio-and-coarse-graining.md#coarse-graining-export-manifest-handoff-to-ix)",
        "[foundation SCF audit Lab act](part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` and `alpha_export.yaml` beside [electronic audit export manifest](part09-dft/00-opening.md#electronic-audit-export-manifest-handoff-to-ix1)",
    ),
    (
        "one pedigree → foundation SCF arc under `writings/md` chapter 03 and `writings/dft` chapter 00",
        "one dft arc under `writings/dft` chapters 00–01",
    ),
    (
        "[VIII.3 Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) reads correctly in isolation from [IX.0 opening hinge from VIII.3](part09-dft/00-opening.md#opening-hinge-viii3-to-ix)",
        "[IX.0 Bridge](part09-dft/00-opening.md#bridge) reads correctly in isolation from [IX.1 opening hinge from IX.0](part09-dft/01-born-oppenheimer.md#opening-hinge-ix0-to-ix1)",
    ),
    (
        "plane-wave tables feel disconnected from the DFT evidence column",
        "Hohenberg–Kohn theorems feel disconnected from `cu.relax.out`",
    ),
    (
        "rear-view mirror of row 134's yaml pedigree → foundation SCF turn at the electronic audit meta prelude capstone boundary",
        "rear-view mirror of row 135's foundation SCF → theorem vocabulary turn at the Born–Oppenheimer meta capstone boundary",
    ),
    ("(VIII.3 → IX.0 meta gate)", "(IX.0 → IX.1 meta gate)"),
    (
        "verified export meta prelude capstone closure (row 134) with the full-book VIII.3 → IX.0 electronic audit meta reunion (row 56)",
        "verified electronic audit meta prelude capstone closure (row 135) with the full-book IX.0 → IX.1 Born–Oppenheimer meta reunion (row 56)",
    ),
    (
        "`pedigree_checklist.yaml` and row 56 meta both read correctly alone but not as one continuous pedigree → SCF afternoon before row 56 Born–Oppenheimer meta prelude opens",
        "`cu.relax.out` and row 56 meta both read correctly alone but not as one continuous SCF → BO afternoon before row 57 Kohn–Sham meta prelude opens",
    ),
    (
        "[Row 68 → Row 95 electronic audit meta prelude reunion index (row 116)](appendix/sources.md#row68-row95-electronic-audit-meta-prelude-reunion-index-row-115)",
        "[Row 68 → Row 96 Born–Oppenheimer meta capstone reunion index (row 116)](appendix/sources.md#row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116)",
    ),
    (
        "Pedigree yaml at \\(T_w\\) before VIII.3 Bridge → SCF after verified export meta prelude capstone",
        "SCF log + `alpha_export.yaml` at \\(T_w\\) before IX.0 Bridge → BO after verified electronic audit meta prelude capstone",
    ),
    (
        "Read [VIII.3 Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) through [IX.0 opening hinge from VIII.3](part09-dft/00-opening.md#opening-hinge-viii3-to-ix) aloud",
        "Read [IX.0 Bridge](part09-dft/00-opening.md#bridge) through [IX.1 opening hinge from IX.0](part09-dft/01-born-oppenheimer.md#opening-hinge-ix0-to-ix1) aloud",
    ),
    (
        '"EAM on trust needs Born–Oppenheimer re-derivation"',
        '"Separate electrons from nuclei; density alone determines energy"',
    ),
    (
        "Open [VIII.3 Scene](part08-md/03-ab-initio-and-coarse-graining.md#scene-when-eam-is-not-enough) then [IX.0 Scene](part09-dft/00-opening.md#scene); confirm [EAM-fit audit Lab act steps 1–6](part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch)",
        "Open [IX.0 Scene](part09-dft/00-opening.md#scene) then [IX.1 Scene](part09-dft/01-born-oppenheimer.md#scene-electrons-adjust-in-a-blink); confirm [foundation SCF audit Lab act steps 1–6](part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation)",
    ),
    ("Same wire; yaml pedigree → \\(\\rho(\\mathbf{r})\\) audit", "Same wire; SCF log → femtosecond/picosecond split"),
    (
        "Confirm [VIII.3 → IX.0 reunion index (row 56)](appendix/sources.md#viii3-ix0-opening-hinge-reunion-index-row-55) five-step audit",
        "Confirm [IX.0 → IX.1 reunion index (row 56)](appendix/sources.md#ix0-ix1-opening-hinge-reunion-index-row-56) five-step audit",
    ),
    ("Pedigree yaml → SCF reads continuous", "SCF log → \\(V_{\\text{BO}}\\) reads continuous"),
    ("Name export meta prelude capstone before VIII.3 Bridge", "Name electronic audit meta prelude capstone before IX.0 Bridge"),
    ("Checklist + audit at \\(T_w\\) before SCF on capstone path", "SCF log + `alpha_export.yaml` at \\(T_w\\) before BO on capstone path"),
    ("Name VIII.3 Bridge as part exit", "Name IX.0 Bridge as theorem request"),
    ("EAM trust → \\(\\rho(\\mathbf{r})\\)", "Audit → vocabulary handoff"),
    ("Name EAM-fit Lab act before IX.0 Scene", "Name foundation SCF Lab act before IX.1 Scene"),
    ("Same specimen, electrons visible", "Same specimen, BO surface visible"),
    ("VIII.3 → IX.0 reads continuous", "IX.0 → IX.1 reads continuous"),
    (
        "row 134 closed but row 56 VIII.3 → IX.0 reunion still feels like DFT homework disconnected from verified export meta prelude capstone",
        "row 135 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone",
    ),
    ("before the Born–Oppenheimer meta reunion", "before the Kohn–Sham meta reunion"),
    (
        "when `pedigree_checklist.yaml` exists on the capstone path but `cu.relax.out` is missing after row 134",
        "when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 135",
    ),
    (
        "export meta prelude capstone and VIII.3 → IX.0 opening hinge still feel like separate stories",
        "electronic audit meta prelude capstone and IX.0 → IX.1 opening hinge still feel like separate stories",
    ),
    (
        "skipping [VIII.3's Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix), not missing k-mesh algebra",
        "skipping [IX.0's Bridge](part09-dft/00-opening.md#bridge), not missing Murnaghan algebra",
    ),
    (
        "when opening [row 116](preface.md#skill-navigation-row-116) before row 56 closes on the capstone path",
        "when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes on the capstone path",
    ),
    ("row 134, row 115, row 95, row 75, or row 36", "row 135, row 116, row 96, row 76, or row 37"),
    ("row 56", "row 56"),  # noop anchor
]

ROW136_PREFACE = tx(tx(ns["ROW135_PREFACE"], P_NUM), P_BO)
PROLOGUE_COMPASS = tx(tx(ns["PROLOGUE_COMPASS"], P_NUM), P_BO)
PROLOGUE_PREVIEW_136 = tx(tx(ns["PROLOGUE_PREVIEW_135"], P_NUM), P_BO)
EPILOGUE_LOOP = tx(tx(ns["EPILOGUE_LOOP"], P_NUM), P_BO)
EPILOGUE_LOOP = EPILOGUE_LOOP.replace("Row 135 closing loop", "Row 136 closing loop").replace(
    "row-135-closing-loop", "row-136-closing-loop"
)
SOURCES_TABLE = tx(tx(ns["SOURCES_TABLE"], P_NUM), P_BO)

PROLOGUE_STITCH_136 = (
    "**Row 136 closing stitch (Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion).** {#row-136-closing-stitch} "
    "When row 135 closed — electronic audit meta prelude capstone verified, row 134 or row 115 recited on the capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
    "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` and `alpha_export.yaml` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the capstone path** — "
    "`writings/dft` chapters 00 and 01 build as separate reading acts, Hohenberg–Kohn theorems feel disconnected from [electronic audit export manifest](../part09-dft/00-opening.md#electronic-audit-export-manifest-handoff-to-ix1) and `cu.relax.out`, or row 56's Bridge → BO gate feels disconnected from row 135's foundation SCF → theorem vocabulary turn while the unified HTML reads smoothly — "
    "the [preface row 136 When-to-pause opening sentence](../preface.md#skill-navigation-row-136) names the dual reunion before Kohn–Sham meta reunion; read [preface row 136](../preface.md#skill-navigation-row-136), then the "
    "[Row 68 → Row 116 reunion index](../appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136), then "
    "[epilogue row 136 closing loop](../epilogue/multiscale.md#row-136-closing-loop) before row 57 Kohn–Sham meta capstone opens.\n\n"
)


def main():
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    anchor = "\n## The copper wire through the book"
    row135_tail_old = (
        "When row 134 is complete, proceed to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone is clean but electronic audit meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 115](preface.md#skill-navigation-row-115) when export meta capstone is clean but electronic audit meta capstone still lags on the opening-hinge path, to [row 95](preface.md#skill-navigation-row-95) for the Row 68 ↔ Row 55 electronic audit opening prelude audit alone, to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync."
    )
    row135_tail_new = (
        "When row 135 is complete, proceed to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta capstone still lags after verified foundation SCF archive on the capstone path, to [row 116](preface.md#skill-navigation-row-116) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 96](preface.md#skill-navigation-row-96) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
    )
    if "skill-navigation-row-136" not in preface:
        if row135_tail_old in preface:
            preface = preface.replace(row135_tail_old, row135_tail_new)
        preface = preface.replace(anchor, ROW136_PREFACE + anchor)
        preface_path.write_text(preface)
        print("preface: row 136")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if '<span id="prologue-preview-row-136">' not in prologue:
        needle = "| Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 135) |"
        idx = prologue.find(needle)
        if idx < 0:
            raise SystemExit("prologue compass row 135 not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + PROLOGUE_COMPASS + prologue[line_end + 1 :]
        if "row-136-closing-stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 116 closing stitch",
                PROLOGUE_STITCH_136 + "**Row 116 closing stitch",
            )
        prologue = prologue.replace(
            '| <span id="prologue-preview-row-135"></span>Row 135 preview',
            PROLOGUE_PREVIEW_136 + '| <span id="prologue-preview-row-135"></span>Row 135 preview',
        )
        print("prologue: row 136")
    prologue_path.write_text(prologue)

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "row-136-closing-loop" not in epilogue:
        epilogue = epilogue.replace(
            "\n### Row 135 closing loop (Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
            EPILOGUE_LOOP
            + "\n### Row 135 closing loop (Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        )
        epilogue = epilogue.replace(
            "Proceed to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            "Proceed to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path, to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 113](#row-113-closing-loop) when row 68 closed but dynamics meta capstone still lags after row 132 on the opening-hinge path,",
            1,
        )
        epilogue_path.write_text(epilogue)
        print("epilogue: row 136")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136" not in sources:
        block = sources.split(
            "## Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 135)"
        )[1].split("## Row 68 → Row 114")[0]
        block136 = tx(
            block,
            P_NUM
            + P_BO
            + [
                ("row 135", "row 136"),
                ("Row 135", "Row 136"),
                ("row 134", "row 135"),
                ("Row 134", "Row 135"),
                (
                    "electronic audit meta prelude capstone reunion index (row 136)",
                    "Born–Oppenheimer meta capstone reunion index (row 136)",
                ),
                ("skill-navigation-row-136", "skill-navigation-row-136"),
                (
                    "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion",
                    "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion",
                ),
                ("row 134 or row 115", "row 135 or row 116"),
                (
                    "VIII.3 Bridge → IX.0 SCF recited on the capstone path",
                    "IX.0 Bridge → IX.1 BO/HK recited on the capstone path",
                ),
                (
                    "electronic audit meta prelude capstone boundary",
                    "Born–Oppenheimer meta capstone boundary",
                ),
                (
                    "Row 134 reunion (export meta prelude capstone)",
                    "Row 135 reunion (electronic audit meta prelude capstone)",
                ),
                (
                    "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
                    "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
                ),
                (
                    "Row 115 reunion (meta prelude)",
                    "Row 116 reunion (meta capstone)",
                ),
                (
                    "row68-row95-electronic-audit-meta-prelude-reunion-index-row-115",
                    "row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116",
                ),
                (
                    "Row 134 gate + Bridge before IX.0",
                    "Row 135 gate + Bridge before IX.1",
                ),
                (
                    "Recite row 68 gate, then export meta prelude capstone, then row 56",
                    "Recite row 68 gate, then electronic audit meta prelude capstone, then row 56",
                ),
                (
                    "verified export meta prelude capstone closure with the electronic audit meta reunion",
                    "verified electronic audit meta prelude capstone closure with the Born–Oppenheimer meta reunion",
                ),
                (
                    "row 134 verified VIII.2 → VIII.3 on pedigree at \\(T_w\\) on the capstone path",
                    "row 135 verified VIII.3 → IX.0 on SCF log at \\(T_w\\) on the capstone path",
                ),
                (
                    "Row 68 → Row 56 move (capstone path) |",
                    "Row 68 → Row 56 move (capstone path) |",
                ),
            ],
        )
        block136 = (
            "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136) {#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136}"
            + block136.split("{#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135}", 1)[-1]
        )
        sources = sources.replace(
            "| 135 | Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone",
            SOURCES_TABLE + "| 135 | Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone",
        )
        sources = sources.replace(
            "## Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 135)",
            block136
            + "## Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 135)",
        )
        extra = (
            "[row 136](#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136) reunites **electronic audit meta prelude capstone with the Born–Oppenheimer meta capstone boundary** "
            "when row 135 closed electronic audit meta prelude capstone at verified foundation SCF on the capstone path but `cu.relax.out` and IX.0 → IX.1 opening hinge still read like separate courses after verified Born–Oppenheimer meta prelude meta;"
        )
        if extra not in sources:
            sources = sources.replace(
                "when row 134 closed export meta prelude capstone at verified pedigree checklist on the capstone path but `pedigree_checklist.yaml` and VIII.3 → IX.0 opening hinge still read like separate courses after verified electronic audit meta prelude meta;",
                "when row 134 closed export meta prelude capstone at verified pedigree checklist on the capstone path but `pedigree_checklist.yaml` and VIII.3 → IX.0 opening hinge still read like separate courses after verified electronic audit meta prelude meta; "
                + extra,
            )
        sources_path.write_text(sources)
        print("sources: row 136")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "### Row 135 baby picture" not in mem:
        raise SystemExit("memory sheet row 135 baby picture not found")
    start = mem.index("### Row 135 baby picture")
    end = mem.index("### Act VI baby picture", start)
    memory_baby_135 = mem[start:end]

    memory_baby_136 = tx(
        memory_baby_135,
        P_NUM
        + P_BO
        + [
            ("Row 135 baby picture", "Row 136 baby picture"),
            ("Export meta prelude capstone row 134", "Electronic audit meta prelude capstone row 135"),
            ("VIII.3 Bridge to Part IX", "IX.0 Bridge"),
            ("row 56 meta gate", "row 56 meta gate"),
            (
                "row 56's VIII.3 Bridge → SCF handoff",
                "row 56's IX.0 Bridge → BO handoff",
            ),
            (
                "export meta prelude capstone / electronic audit meta prelude",
                "electronic audit meta prelude capstone / Born–Oppenheimer meta capstone",
            ),
            ("preface row 134", "preface row 135"),
            ("preface row 115", "preface row 116"),
            ("preface row 56", "preface row 56"),
            ("EAM-fit audit Lab act steps 1–6", "foundation SCF audit Lab act steps 1–6"),
            (
                "`pedigree_checklist.yaml` before row 56 Born–Oppenheimer meta prelude capstone opens",
                "`cu.relax.out` before row 57 Kohn–Sham meta capstone opens",
            ),
            (
                "row 116 Born–Oppenheimer meta capstone or row 56 BO reunion",
                "row 117 Kohn–Sham meta capstone or row 57 KS reunion",
            ),
            ("pedigree → foundation SCF afternoon", "SCF → Born–Oppenheimer afternoon"),
            (
                "export meta prelude capstone vs electronic audit meta prelude capstones",
                "electronic audit meta prelude capstone vs Born–Oppenheimer meta capstones",
            ),
            (
                "row 135 feels disconnected from row 134",
                "row 136 feels disconnected from row 135",
            ),
        ],
    )
    if "### Row 136 baby picture" not in mem:
        mem = mem.replace(
            "### Act VI baby picture (ME 412 coupling ladder)",
            memory_baby_136 + "\n\n### Act VI baby picture (ME 412 coupling ladder)",
        )
    if "| 136 | Meta |" not in mem:
        mem_table_136 = tx(
            "| 135 | Meta | Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion | "
            "[Row 68 → Row 115 electronic audit meta prelude capstone reunion index](sources.md#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135) · "
            "[preface row 135 skill checkpoint](../preface.md#skill-navigation-row-135) · "
            "[prologue row 135 preview](../prologue/00-many-scales.md#prologue-preview-row-135) · "
            "[prologue row 135 closing stitch](../prologue/00-many-scales.md#row-135-closing-stitch) · "
            "[epilogue row 135 closing loop](../epilogue/multiscale.md#row-135-closing-loop) | "
            "Row 68 closed but row 56 VIII.3 → IX.0 opening hinge feels disconnected from verified export meta prelude capstone on the capstone path — "
            "read row 68 + row 134 or row 115 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 56; "
            "[row 135 baby picture](#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion) |\n",
            P_NUM + P_BO,
        )
        mem = mem.replace(
            "[row 135 baby picture](#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
            "[row 135 baby picture](#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion) |\n"
            + mem_table_136
            + "| 93 | Meta |",
        )
    if "When row 135 closed but Born–Oppenheimer meta reunion still lags" not in mem:
        mem = mem.replace(
            "When row 134 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 135](#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 134 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 135](#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion). When row 135 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 136](#row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion).",
        )
    mem_path.write_text(mem)
    print("memory: row 136")


if __name__ == "__main__":
    main()
