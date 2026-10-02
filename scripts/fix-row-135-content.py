#!/usr/bin/env python3
"""Repair row 135 sections corrupted by naive tx() in add-row-135.py."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def capstone134_to_135(text: str) -> str:
    """Transform row-134 capstone block into row-135 electronic-audit capstone block."""
    pairs = [
        ("Row 134 closing loop", "Row 135 closing loop"),
        ("row-134-closing-loop", "row-135-closing-loop"),
        ("skill-navigation-row-134", "skill-navigation-row-135"),
        ("prologue-preview-row-134", "prologue-preview-row-135"),
        ("row-134-closing-stitch", "row-135-closing-stitch"),
        ("row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
         "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion"),
        ("row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
         "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135"),
        ("Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion",
         "Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion"),
        ("Row 68 → Row 114 export meta prelude capstone reunion index",
         "Row 68 → Row 115 electronic audit meta prelude capstone reunion index"),
        ("Row 134 skill checkpoint", "Row 135 skill checkpoint"),
        ("Row 134 three-way audit", "Row 135 three-way audit"),
        ("Row 134 baby picture", "Row 135 baby picture"),
        ("Dynamics meta prelude capstone row 133", "Export meta prelude capstone row 134"),
        ("VIII.2 Bridge", "VIII.3 Bridge to Part IX"),
        ("row 54 meta gate", "row 55 meta gate"),
        ("R54[row 54 meta gate]", "R55[row 55 meta gate]"),
        ("dynamics meta prelude capstone / export meta prelude",
         "export meta prelude capstone / electronic audit meta prelude"),
        ("dynamics meta prelude capstone / export meta prelude gate",
         "export meta prelude capstone / electronic audit meta prelude gate"),
        ("verified dynamics meta prelude capstone closure (row 133)",
         "verified export meta prelude capstone closure (row 134)"),
        ("Row 68 → Row 54 meta (row 114)", "Row 68 → Row 55 meta (row 115)"),
        ("export meta prelude capstone at the ensembles → coarse-graining chapter boundary",
         "electronic audit meta prelude capstone at the coarse-graining → foundation SCF chapter boundary"),
        ("one NPT → pedigree afternoon before row 55 electronic audit meta prelude opens",
         "one pedigree → foundation SCF afternoon before row 56 Born–Oppenheimer meta prelude opens"),
        ("before export meta prelude capstone", "before electronic audit meta prelude capstone"),
        ("Name dynamics meta prelude capstone before VIII.2 Bridge",
         "Name export meta prelude capstone before VIII.3 Bridge to Part IX"),
        ("Name VIII.2 Bridge as chapter exit", "Name VIII.3 Bridge to Part IX as part exit"),
        ("Name dynamics manifest before VIII.3 Scene", "Name EAM-fit Lab act before IX.0 Scene"),
        ("`cu.elastic/` before pedigree checklist on capstone path", "Checklist + audit at \\(T_w\\) before SCF on capstone path"),
        ("Dumps ≠ handoff tables", "EAM trust → \\(\\rho(\\mathbf{r})\\)"),
        ("EAM fails at notch root", "Same specimen, electrons visible"),
        ("VIII.2 → VIII.3 reads continuous", "VIII.3 → IX.0 reads continuous"),
        ("row 54 VIII.2 → VIII.3 opening hinge still opens like standalone export homework after the NPT Lab act",
         "row 55 VIII.3 → IX.0 opening hinge still opens like standalone DFT homework after the EAM-fit Lab act"),
        ("VIII.2 Bridge and VIII.3 pedigree sections", "VIII.3 Bridge to Part IX and IX.0 SCF sections"),
        ("row 133 closed dynamics meta prelude capstone", "row 134 closed export meta prelude capstone"),
        ("When row 54 feels like export homework after row 133 alone",
         "When row 55 feels like DFT homework after row 134 alone"),
        ("part08-md/02-ensembles-integrators.md#bridge", "part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix"),
        ("VIII.3 opening hinge from VIII.2", "IX.0 opening hinge from VIII.3"),
        ("part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3",
         "part09-dft/00-opening.md#opening-hinge-viii3-to-ix"),
        ("VIII.3 plot spine", "IX.0 plot spine"),
        ("part08-md/03-ab-initio-and-coarse-graining.md#plot-spine-one-line",
         "part09-dft/00-opening.md#plot-spine-one-line"),
        ("pedigree checklist", "foundation SCF audit Lab act"),
        ("part08-md/03-ab-initio-and-coarse-graining.md#pedigree-checklist-before-the-epilogue",
         "part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation"),
        ("row 54 closing loop", "row 55 closing loop"),
        ("preface row 54", "preface row 55"),
        ("row 74", "row 75"),
        ("Bridge → export contract", "Bridge → SCF contract"),
        ("preface row 133", "preface row 134"),
        ("split dynamics meta prelude capstone from export reunion",
         "split export meta prelude capstone from electronic audit reunion"),
        ("NPT Lab act steps 1–7", "EAM-fit audit Lab act steps 1–6"),
        ("part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment",
         "part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch"),
        ("archived `cu.elastic/` and `mobility_cu_screw_{T_w}K.yaml` beside [dynamics export manifest]",
         "archived `pedigree_checklist.yaml` and `eam_fit_audit.log` beside [coarse-graining export manifest]"),
        ("part08-md/02-ensembles-integrators.md#dynamics-export-manifest-handoff-to-viii3",
         "part08-md/03-ab-initio-and-coarse-graining.md#coarse-graining-export-manifest-handoff-to-ix"),
        ("dual export meta prelude capstone", "dual electronic audit meta prelude capstone"),
        ("row 134 (row 68 ↔ row 54 reunion on the capstone path) with row 114",
         "row 135 (row 68 ↔ row 55 reunion on the capstone path) with row 115"),
        ("row 114 names **Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion**; row 134 names **why that reunion must follow verified dynamics meta prelude capstone (row 133)",
         "row 115 names **Row 68 → Row 95 Row 68 → Row 55 electronic audit meta prelude reunion**; row 135 names **why that reunion must follow verified export meta prelude capstone (row 134)"),
        ("Proceed to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path, to [row 114](#row-114-closing-loop) when row 68 closed but export meta capstone still lags after row 113 on the opening-hinge path, to [row 133](#row-133-closing-loop) when dynamics meta prelude capstone still lags after row 132 on the capstone path, to [row 54](#row-54-closing-loop) when only VIII.2 → VIII.3 stalls",
         "Proceed to [row 116](#row-116-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 135 on the capstone path, to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta capstone still lags after row 114 on the opening-hinge path, to [row 134](#row-134-closing-loop) when export meta prelude capstone still lags after row 133 on the capstone path, to [row 55](#row-55-closing-loop) when only VIII.3 → IX.0 stalls"),
        ("row 133 or row 114", "row 134 or row 115"),
        ("row 133", "row 134"),
        ("row 114", "row 115"),
        ("row 54", "row 55"),
        ("Row 68 ↔ Row 54 reunion (capstone path)", "Row 68 ↔ Row 55 reunion (capstone path)"),
        ("before electronic audit meta prelude capstone", "before electronic audit meta prelude capstone"),
        ("Row 68 → Row 94 export meta prelude reunion index (row 115)",
         "Row 68 → Row 95 electronic audit meta prelude reunion index (row 115)"),
        ("row68-row94-export-meta-prelude-reunion-index-row-115",
         "row68-row95-electronic-audit-meta-prelude-reunion-index-row-115"),
        ("NPT archive at \\(T_w\\) before VIII.2 Bridge → pedigree after verified dynamics meta prelude capstone",
         "Pedigree yaml at \\(T_w\\) before VIII.3 Bridge → SCF after verified export meta prelude capstone"),
        ("Read [VIII.3 Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) through [IX.0 opening hinge from VIII.3](part09-dft/00-opening.md#opening-hinge-viii3-to-ix) aloud",
         "Read [VIII.3 Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) through [IX.0 opening hinge from VIII.3](part09-dft/00-opening.md#opening-hinge-viii3-to-ix) aloud"),
        ("Open [VIII.2 Scene]", "Open [VIII.3 Scene]"),
        ("part08-md/02-ensembles-integrators.md#scene-thermometers-in-a-nanoscale-lab",
         "part08-md/03-ab-initio-and-coarse-graining.md#scene-when-eam-is-not-enough"),
        ("then [VIII.3 Scene]", "then [IX.0 Scene]"),
        ("part08-md/03-ab-initio-and-coarse-graining.md#scene-when-eam-is-not-enough",
         "part09-dft/00-opening.md#scene"),
        ("Same wire; bulk NPT → notch EAM trust", "Same wire; yaml pedigree → \\(\\rho(\\mathbf{r})\\) audit"),
        ("VIII.2 → VIII.3 reunion index (row 55)", "VIII.3 → IX.0 reunion index (row 55)"),
        ("viii2-viii3-opening-hinge-reunion-index-row-55", "viii3-ix0-opening-hinge-reunion-index-row-55"),
        ("Dynamics → pedigree reads continuous", "Pedigree yaml → SCF reads continuous"),
        ("row 133 closed but row 54 VIII.2 → VIII.3 reunion still feels like export homework disconnected from verified dynamics meta prelude capstone",
         "row 134 closed but row 55 VIII.3 → IX.0 reunion still feels like DFT homework disconnected from verified export meta prelude capstone"),
        ("before the Born–Oppenheimer meta reunion", "before the Born–Oppenheimer meta reunion"),
        ("when `cu.elastic/` exists on the capstone path but consumer columns in the checklist are empty after row 133",
         "when `pedigree_checklist.yaml` exists on the capstone path but `cu.relax.out` is missing after row 134"),
        ("dynamics meta prelude capstone and VIII.2 → VIII.3 opening hinge still feel like separate stories",
         "export meta prelude capstone and VIII.3 → IX.0 opening hinge still feel like separate stories"),
        ("skipping [VIII.3 Bridge to Part IX]", "skipping [VIII.3's Bridge to Part IX]"),
        ("not missing EAM-fit algebra", "not missing k-mesh algebra"),
        ("when opening [row 115]", "when opening [row 116]"),
        ("before row 55 closes on the capstone path", "before row 56 closes on the capstone path"),
        ("When row 133 is complete, proceed to [row 134]",
         "When row 134 is complete, proceed to [row 135]"),
        ("When row 134 is complete, proceed to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone is clean but electronic audit meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 115](preface.md#skill-navigation-row-115) when export meta capstone is clean but electronic audit meta capstone still lags on the opening-hinge path, to [row 95](preface.md#skill-navigation-row-95) for the Row 68 ↔ Row 55 electronic audit opening prelude audit alone, to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls",
         "When row 134 is complete, proceed to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone is clean but electronic audit meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 115](preface.md#skill-navigation-row-115) when export meta capstone is clean but electronic audit meta capstone still lags on the opening-hinge path, to [row 95](preface.md#skill-navigation-row-95) for the Row 68 ↔ Row 55 electronic audit opening prelude audit alone, to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls"),
    ]
    for a, b in pairs:
        text = text.replace(a, b)
    return text


def main():
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 134 skill checkpoint — Row 68 → Row 114")
    end = preface.index("\n## The copper wire through the book")
    row134_preface = preface[start:preface.index("### Row 135 skill checkpoint", start)]
    row135_preface = capstone134_to_135(row134_preface)
    row135_preface = row135_preface.replace("### Row 134 skill checkpoint", "### Row 135 skill checkpoint", 1)
    # Preface body tweaks not covered by epilogue-oriented pairs
    row135_preface = row135_preface.replace(
        "electronic audit meta prelude capstone / export meta prelude hinge",
        "export meta prelude capstone / electronic audit meta prelude hinge",
    )
    row135_preface = row135_preface.replace(
        "VIII.2 Bridge → VIII.3 pedigree recited",
        "VIII.3 Bridge → IX.0 SCF recited on the capstone path",
    )
    row135_preface = row135_preface.replace(
        "one pedigree → foundation SCF arc under `writings/md` chapters 02–03 after verified electronic audit meta prelude capstone",
        "one pedigree → foundation SCF arc under `writings/md` chapter 03 and `writings/dft` chapter 00 after verified export meta prelude capstone",
    )
    row135_preface = row135_preface.replace(
        "rear-view mirror of row 134's finite-\\(T\\) dynamics → yaml handoff turn",
        "rear-view mirror of row 134's yaml pedigree → foundation SCF turn",
    )
    row135_preface = row135_preface.replace(
        "row 134, row 115, row 94, row 74, or row 35",
        "row 134, row 115, row 95, row 75, or row 36",
    )
    row135_preface = row135_preface.replace(
        "verified electronic audit meta prelude capstone closure (row 134) with the full-book VIII.3 Bridge to Part IX → IX.0 export meta reunion (row 55)",
        "verified export meta prelude capstone closure (row 134) with the full-book VIII.3 → IX.0 electronic audit meta reunion (row 55)",
    )
    row135_preface = row135_preface.replace(
        "`cu.elastic/` and row 55 meta both read correctly alone but not as one continuous NPT afternoon → pedigree checklist before row 55 electronic audit meta prelude opens",
        "`pedigree_checklist.yaml` and row 55 meta both read correctly alone but not as one continuous pedigree → SCF afternoon before row 56 Born–Oppenheimer meta prelude opens",
    )
    row135_preface = row135_preface.replace(
        "row 134 closed but row 55 VIII.3 → IX.0 reunion still feels like export homework",
        "row 134 closed but row 55 VIII.3 → IX.0 reunion still feels like DFT homework",
    )
    row135_preface = row135_preface.replace(
        "electronic audit meta prelude capstone and VIII.3 Bridge to Part IX → IX.0 opening hinge still feel like separate stories",
        "export meta prelude capstone and VIII.3 → IX.0 opening hinge still feel like separate stories",
    )
    row135_preface = row135_preface.replace(
        "Name electronic audit meta prelude capstone before VIII.3 Bridge to Part IX",
        "Name export meta prelude capstone before VIII.3 Bridge to Part IX",
    )
    row135_preface = row135_preface.replace(
        "Step 2 — electronic audit meta prelude capstone / export meta prelude gate",
        "Step 2 — export meta prelude capstone / electronic audit meta prelude gate",
    )
    row135_preface = row135_preface.replace(
        "row68-row115-export-meta-prelude-capstone-reunion-index-row-135",
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
    )
    row135_preface = row135_preface.replace(
        "row-135-baby-picture-row68-row115-export-meta-prelude-capstone-reunion",
        "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
    )
    when_tail = (
        "**When to pause.** Read the [prologue row 135 closing stitch](prologue/00-many-scales.md#row-135-closing-stitch) first when row 134 closed but row 55 VIII.3 → IX.0 reunion still feels like DFT homework disconnected from verified export meta prelude capstone on the capstone path — it names the dual reunion before the Born–Oppenheimer meta reunion. Then read the [prologue row 135 preview](prologue/00-many-scales.md#prologue-preview-row-135) when `pedigree_checklist.yaml` exists on the capstone path but `cu.relax.out` is missing after row 134. Return to the [Row 68 → Row 115 reunion index](appendix/sources.md#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135) when row 134 and row 55 both verify individually but **export meta prelude capstone and VIII.3 → IX.0 opening hinge still feel like separate stories** — the break is usually skipping [VIII.3's Bridge to Part IX](part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix), not missing k-mesh algebra. Read the [memory sheet row 135 baby picture](appendix/memory-sheet.md#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion) when opening [row 116](preface.md#skill-navigation-row-116) before row 56 closes on the capstone path; read the [epilogue row 135 closing loop](epilogue/multiscale.md#row-135-closing-loop) when the competence loop closes. When row 134 is complete, proceed to [row 135](preface.md#skill-navigation-row-135) when export meta prelude capstone is clean but electronic audit meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 115](preface.md#skill-navigation-row-115) when export meta capstone is clean but electronic audit meta capstone still lags on the opening-hinge path, to [row 95](preface.md#skill-navigation-row-95) for the Row 68 ↔ Row 55 electronic audit opening prelude audit alone, to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 55](preface.md#skill-navigation-row-55) when only VIII.3 → IX.0 stalls, or extend prose only under `writings/` then sync.\n"
    )
    if "**When to pause.**" in row135_preface:
        row135_preface = row135_preface[: row135_preface.index("**When to pause.**")] + when_tail

    preface = preface[: preface.index("### Row 135 skill checkpoint")] + row135_preface + preface[end:]
    (ROOT / "writings/preface/chapters/preface.md").write_text(preface)

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    s = epilogue.index("### Row 134 closing loop")
    e = epilogue.index("### Row 133 closing loop", s)
    row134_loop = epilogue[s:e]
    row135_loop = capstone134_to_135(row134_loop)
    row135_loop = row135_loop.replace("### Row 134 closing loop", "### Row 135 closing loop", 1)
    row135_loop = row135_loop.replace(
        "row68-row115-export-meta-prelude-capstone-reunion-index-row-135",
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
    )
    bad = epilogue.index("### Row 135 closing loop")
    bad_end = epilogue.index("### Row 134 closing loop", bad)
    epilogue = epilogue[:bad] + row135_loop + epilogue[bad_end:]
    (ROOT / "writings/epilogue/chapters/multiscale.md").write_text(epilogue)

    mem = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    ms = mem.index("### Row 134 baby picture")
    me = mem.index("### Row 135 baby picture", ms)
    row134_baby = mem[ms:me]
    row135_baby = capstone134_to_135(row134_baby)
    row135_baby = row135_baby.replace("### Row 134 baby picture", "### Row 135 baby picture", 1)
    row135_baby = row135_baby.replace(
        "row 54's VIII.3 Bridge to Part IX → pedigree handoff",
        "row 55's VIII.3 Bridge to Part IX → SCF handoff",
    )
    row135_baby = row135_baby.replace(
        "Row 68 → Row 115 export meta prelude capstone reunion index",
        "Row 68 → Row 115 electronic audit meta prelude capstone reunion index",
    )
    row135_baby = row135_baby.replace(
        "row68-row115-export-meta-prelude-capstone-reunion-index-row-135",
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
    )
    row135_baby = row135_baby.replace(
        "dynamics meta prelude capstone / export meta prelude",
        "export meta prelude capstone / electronic audit meta prelude",
    )
    row135_baby = row135_baby.replace(
        "VIII.3 Bridge to Part IX](../part08-md/02-ensembles-integrators.md#bridge)",
        "VIII.3 Bridge to Part IX](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix)",
    )
    row135_baby = row135_baby.replace(
        "through [VIII.3 opening hinge from VIII.2]",
        "through [IX.0 opening hinge from VIII.3]",
    )
    row135_baby = row135_baby.replace(
        "part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3",
        "part09-dft/00-opening.md#opening-hinge-viii3-to-ix",
    )
    row135_baby = row135_baby.replace(
        "archived `pedigree_checklist.yaml` before row 56 Born–Oppenheimer meta prelude capstone opens.",
        "archived `pedigree_checklist.yaml` and `eam_fit_audit.log` before row 56 Born–Oppenheimer meta prelude capstone opens.",
    )
    row135_baby = row135_baby.replace("preface row 55", "preface row 55")
    row135_baby = row135_baby.replace(
        "Dynamics meta prelude capstone row 134",
        "Export meta prelude capstone row 134",
    )
    row135_baby = row135_baby.replace(
        "dynamics meta prelude capstone vs export meta prelude capstones",
        "export meta prelude capstone vs electronic audit meta prelude capstones",
    )
    row135_baby = row135_baby.replace(
        "row 134 when **VIII.1 Bridge and Row 68 → Row 53 meta must read on the same wire before any VIII.2 → VIII.3 audit on the capstone path**",
        "row 134 when **VIII.2 Bridge and Row 68 → Row 54 meta must read on the same wire before any VIII.3 → IX.0 audit on the capstone path**",
    )
    row135_baby = row135_baby.replace(
        "row 135 when **VIII.3 Bridge to Part IX and Row 68 → Row 55 meta must read on the same wire before row 116 Born–Oppenheimer meta capstone or row 56 BO reunion opens on the capstone path**",
        "row 135 when **VIII.3 Bridge to Part IX and Row 68 → Row 55 meta must read on the same wire before row 116 Born–Oppenheimer meta capstone or row 56 BO reunion opens on the capstone path**",
    )
    row135_baby = row135_baby.replace("NPT → pedigree afternoon", "pedigree → foundation SCF afternoon")
    row135_baby = row135_baby.replace(
        "When row 134 closed but export meta reunion still lags on the capstone path, switch to [row 135](#row-135-baby-picture-row68-row115-export-meta-prelude-capstone-reunion).",
        "",
    )
    row135_baby = row135_baby.replace(
        "row-135-baby-picture-row68-row115-export-meta-prelude-capstone-reunion",
        "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
    )
    mem = mem[: mem.index("### Row 135 baby picture")] + row135_baby + mem[mem.index("### Act VI baby picture", mem.index("### Row 135 baby picture")):]
    (ROOT / "writings/appendix/chapters/memory-sheet.md").write_text(mem)

    prologue = (ROOT / "writings/prologue/chapters/00-many-scales.md").read_text()
    preview134 = prologue.split('| <span id="prologue-preview-row-134"></span>')[1].split("\n|")[0]
    preview135 = capstone134_to_135(
        '| <span id="prologue-preview-row-134"></span>' + preview134
    )
    preview135 = preview135.replace("prologue-preview-row-134", "prologue-preview-row-135")
    preview135 = preview135.replace("Row 134 preview", "Row 135 preview")
    preview135 = preview135.replace(
        "dynamics meta prelude capstone reunion",
        "electronic audit meta prelude capstone reunion",
    )
    preview135 = preview135.replace("VIII.2 → VIII.3 meta (row 55)", "VIII.3 → IX.0 meta (row 55)")
    preview135 = preview135.replace("Bridge → pedigree chain", "Bridge → SCF audit chain")
    preview135 = preview135.replace(
        "dynamics manifest and coarse-graining sections",
        "pedigree checklist and Part IX sections",
    )
    preview135 = preview135.replace(
        "dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 55",
        "export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55",
    )
    preview135 = preview135.replace(
        "NPT dynamics is clean on the capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone",
        "pedigree checklist is clean on the capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone",
    )
    preview135 = preview135.replace(
        "row68-row115-dynamics-meta-prelude-capstone-reunion-index-row-135",
        "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
    )
    preview135 = preview135.replace(
        "row-135-baby-picture-row68-row115-dynamics-meta-prelude-capstone-reunion",
        "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
    )
    preview135 = preview135.replace(
        "[VIII.2 Bridge](../part08-md/02-ensembles-integrators.md#bridge)",
        "[VIII.3 Bridge to Part IX](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix)",
    )
    preview135 = preview135.replace(
        "[VIII.3 opening hinge from VIII.2]",
        "[IX.0 opening hinge from VIII.3]",
    )
    old_prev = prologue.split('| <span id="prologue-preview-row-135"></span>')[1].split("\n|")[0]
    prologue = prologue.replace(
        '| <span id="prologue-preview-row-135"></span>' + old_prev,
        preview135.rstrip(),
        1,
    )
    compass_old = "| Row 68 → Row 115 Row 68 → Row 55 dynamics meta prelude capstone reunion (row 135) |"
    compass_new = (
        "| Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 135) | "
        "[Preface: row 135 skill checkpoint](../preface.md#skill-navigation-row-135) · "
        "[Row 68 → Row 115 electronic audit meta prelude capstone reunion index](../appendix/sources.md#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135) · "
        "[memory sheet row 135 baby picture](../appendix/memory-sheet.md#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion) · "
        "[prologue row 135 preview row](#prologue-preview-row-135); [prologue row 135 closing stitch](#row-135-closing-stitch); "
        "[epilogue row 135 closing loop](../epilogue/multiscale.md#row-135-closing-loop) — "
        "read row 68 gate + row 134 or row 115 export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud "
        "when pedigree checklist is clean on the capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone |\n"
    )
    if compass_old in prologue:
        idx = prologue.index(compass_old)
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + compass_new + prologue[line_end + 1 :]

    stitch = (
        "**Row 135 closing stitch (Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-135-closing-stitch} "
        "When row 134 closed — export meta prelude capstone verified, row 133 or row 114 recited on the capstone path, and VIII.2 Bridge → VIII.3 pedigree recited with "
        "[EAM-fit audit Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` and `eam_fit_audit.log` — but **row 55 VIII.3 → IX.0 opening hinge still opens like standalone DFT homework after the export Scene on the capstone path** — "
        "`writings/md` chapter 03 and `writings/dft` chapter 00 build as separate reading acts, plane-wave tables feel disconnected from [coarse-graining export manifest](../part08-md/03-ab-initio-and-coarse-graining.md#coarse-graining-export-manifest-handoff-to-ix) and the DFT evidence column at \\(T_w\\), or row 55's Bridge → SCF audit feels disconnected from row 134's yaml pedigree → electronic audit turn while the unified HTML reads smoothly — "
        "the [preface row 135 When-to-pause opening sentence](../preface.md#skill-navigation-row-135) names the dual reunion before Born–Oppenheimer meta reunion; read [preface row 135](../preface.md#skill-navigation-row-135), then the "
        "[Row 68 → Row 115 reunion index](../appendix/sources.md#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135), then "
        "[epilogue row 135 closing loop](../epilogue/multiscale.md#row-135-closing-loop) before row 56 Born–Oppenheimer meta prelude capstone opens.\n\n"
    )
    if "row-135-closing-stitch" in prologue:
        a = prologue.index("**Row 135 closing stitch")
        b = prologue.index("\n\n", a) + 2
        prologue = prologue[:a] + stitch + prologue[b:]

    (ROOT / "writings/prologue/chapters/00-many-scales.md").write_text(prologue)

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    sources = sources.replace(
        "{#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135} {#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135}",
        "{#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135}",
    )
    sources = sources.replace(
        "row 134 or row 95 closed export meta prelude capstone / electronic audit opening prelude",
        "row 134 or row 115 closed export meta prelude capstone / electronic audit meta prelude",
    )
    sources = sources.replace(
        "[row 134](#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) or [row 95](#row68-row95-electronic-audit-meta-prelude-reunion-index-row-115)",
        "[row 134](#row68-row114-export-meta-prelude-capstone-reunion-index-row-134) or [row 115](#row68-row95-electronic-audit-meta-prelude-reunion-index-row-115)",
    )
    row135_table = (
        "| 135 | Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone ↔ row 55 meta) | "
        "[Row 68 → Row 115 electronic audit meta prelude capstone reunion index](#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135) · "
        "[preface row 135](../preface.md#skill-navigation-row-135) · "
        "[prologue row 135 preview](../prologue/00-many-scales.md#prologue-preview-row-135) · "
        "[prologue row 135 closing stitch](../prologue/00-many-scales.md#row-135-closing-stitch) · "
        "[epilogue row 135 closing loop](../epilogue/multiscale.md#row-135-closing-loop) · "
        "[memory sheet row 135 baby picture](memory-sheet.md#row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 55 VIII.3 → IX.0 opening hinge still feels disconnected from verified export meta prelude capstone on the capstone path** — "
        "read row 68 + row 134 or row 115 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; [preface row 55](../preface.md#skill-navigation-row-55) |\n"
    )
    if "| 135 | Row 68 → Row 115 Row 68 → Row 55 dynamics meta" in sources:
        idx = sources.index("| 135 | Row 68 → Row 115 Row 68 → Row 55 dynamics meta")
        line_end = sources.find("\n", idx)
        sources = sources[:idx] + row135_table + sources[line_end + 1 :]

    (ROOT / "writings/appendix/chapters/sources.md").write_text(sources)
    print("fixed row 135 content")


if __name__ == "__main__":
    main()
