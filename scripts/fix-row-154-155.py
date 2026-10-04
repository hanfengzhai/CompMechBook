#!/usr/bin/env python3
"""Finish row 154/155 inserts and repair prologue corruption from partial add-rows run."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fix_prologue() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    bad = (
        "| Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) | "
        "[Preface: row 153 skill checkpoint](../preface.md#skill-navigation-row-153) · "
        "[Row 68 → Row 153 dynamics meta prelude capstone reunion index]"
    )
    if bad in text:
        text = text.replace(
            "| Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) | "
            "[Preface: row 153 skill checkpoint](../preface.md#skill-navigation-row-153) · "
            "[Row 68 → Row 153 dynamics meta prelude capstone reunion index]"
            "(../appendix/sources.md#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153) · "
            "[memory sheet row 153 baby picture](../appendix/memory-sheet.md#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion) · "
            "[prologue row 153 preview row](#prologue-preview-row-153); [prologue row 153 closing stitch](#row-153-closing-stitch); "
            "[epilogue row 153 closing loop](../epilogue/multiscale.md#row-153-closing-loop) — "
            "read row 68 gate + row 152 or row 153 atomistic meta prelude capstone / dynamics meta prelude gate + "
            "VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53 meta aloud when EAM foundation is clean on the capstone path "
            "but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone |\n",
            "",
        )
    line154 = (
        "| Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion (row 154) | "
        "[Preface: row 154 skill checkpoint](../preface.md#skill-navigation-row-154) · "
        "[Row 68 → Row 134 export meta prelude capstone reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) · "
        "[memory sheet row 154 baby picture](../appendix/memory-sheet.md#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion) · "
        "[prologue row 154 preview row](#prologue-preview-row-154); [prologue row 154 closing stitch](#row-154-closing-stitch); "
        "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) — "
        "read row 68 gate + row 153 or row 134 dynamics meta prelude capstone / export meta prelude gate + "
        "VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud when NPT archive is clean on the capstone path "
        "but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone |\n"
    )
    line155 = (
        "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) | "
        "[Preface: row 155 skill checkpoint](../preface.md#skill-navigation-row-155) · "
        "[Row 68 → Row 135 electronic audit meta prelude capstone reunion index](../appendix/sources.md#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155) · "
        "[memory sheet row 155 baby picture](../appendix/memory-sheet.md#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion) · "
        "[prologue row 155 preview row](#prologue-preview-row-155); [prologue row 155 closing stitch](#row-155-closing-stitch); "
        "[epilogue row 155 closing loop](../epilogue/multiscale.md#row-155-closing-loop) — "
        "read row 68 gate + row 154 or row 135 export meta prelude capstone / electronic audit meta prelude gate + "
        "VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud when pedigree checklist is clean on the capstone path "
        "but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone |\n"
    )
    if "row 154) |" not in text.split("reading-compass")[1][:8000] if "reading-compass" in text else "row 154" not in text:
        anchor = "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) |"
        idx = text.find(anchor)
        if idx >= 0:
            line_end = text.find("\n", idx)
            if "row 154) |" not in text[idx : idx + 5000]:
                text = text[: line_end + 1] + line154 + line155 + text[line_end + 1 :]
    if "row-154-closing-stitch" not in text:
        stitch154 = (
            "**Row 154 closing stitch (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-154-closing-stitch} "
            "When row 153 closed — dynamics meta prelude capstone verified, row 152 or row 133 recited on the capstone path, and VIII.1 Bridge → VIII.2 NPT recited with "
            "[NPT Lab act](../part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` — but **row 54 VIII.2 → VIII.3 opening hinge still opens like standalone coarse-graining homework after the thermostat Scene on the capstone path** — "
            "read [preface row 154](../preface.md#skill-navigation-row-154), the "
            "[Row 68 → Row 134 reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154), and "
            "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) before row 55 electronic audit meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 153 closing stitch", stitch154 + "**Row 153 closing stitch", 1)
    if "row-155-closing-stitch" not in text:
        stitch155 = (
            "**Row 155 closing stitch (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-155-closing-stitch} "
            "When row 154 closed — export meta prelude capstone verified, row 153 or row 134 recited on the capstone path, and VIII.2 Bridge → VIII.3 pedigree recited with "
            "[EAM-fit audit Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` — but **row 55 VIII.3 → IX.0 opening hinge still opens like standalone DFT homework after the export Scene on the capstone path** — "
            "read [preface row 155](../preface.md#skill-navigation-row-155), the "
            "[Row 68 → Row 135 reunion index](../appendix/sources.md#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155), and "
            "[epilogue row 155 closing loop](../epilogue/multiscale.md#row-155-closing-loop) before row 56 Born–Oppenheimer meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 154 closing stitch", stitch155 + "**Row 154 closing stitch", 1)
    preview154 = (
        '| <span id="prologue-preview-row-154"></span>Row 154 preview (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and VIII.2 → VIII.3 meta (row 54) must be read together with the Bridge → pedigree chain after verified dynamics meta prelude capstone (row 153) "
        "before coarse-graining and DFT sections feel like separate courses on the capstone path | "
        'One sentence: "read row 68 gate + row 153 or row 134 dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud when NPT archive is clean on the capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone" — '
        "[preface row 154 skill checkpoint](../preface.md#skill-navigation-row-154); [prologue row 154 closing stitch](#row-154-closing-stitch); "
        "[Row 68 → Row 134 reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) |\n"
    )
    preview155 = (
        '| <span id="prologue-preview-row-155"></span>Row 155 preview (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion) | '
        "Explain why midpoint closure (row 68) and VIII.3 → IX.0 meta (row 55) must be read together with the Bridge → SCF audit chain after verified export meta prelude capstone (row 154) "
        "before Born–Oppenheimer and Kohn–Sham sections feel like separate courses on the capstone path | "
        'One sentence: "read row 68 gate + row 154 or row 135 export meta prelude capstone / electronic audit meta prelude gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55 meta aloud when pedigree checklist is clean on the capstone path but Part IX still feels like standalone DFT coursework after verified export meta prelude capstone" — '
        "[preface row 155 skill checkpoint](../preface.md#skill-navigation-row-155); [prologue row 155 closing stitch](#row-155-closing-stitch); "
        "[Row 68 → Row 135 reunion index](../appendix/sources.md#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155) |\n"
    )
    if "prologue-preview-row-154" not in text:
        text = text.replace(
            '| <span id="prologue-preview-row-153"></span>',
            preview154 + preview155 + '| <span id="prologue-preview-row-153"></span>',
            1,
        )
    path.write_text(text)
    print("prologue: fixed")


def fix_preface_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "[prologue row 134 closing stitch](prologue/00-many-scales.md#row-154-closing-stitch)",
        "[prologue row 154 closing stitch](prologue/00-many-scales.md#row-154-closing-stitch)",
    )
    text = text.replace(
        "[prologue row 134 preview](prologue/00-many-scales.md#prologue-preview-row-154)",
        "[prologue row 154 preview](prologue/00-many-scales.md#prologue-preview-row-154)",
    )
    path.write_text(text)
    print("preface: link fixes")


def main() -> None:
    fix_prologue()
    fix_preface_links()
    # Re-run sources/memory if missing
    import add_rows_154_155  # noqa: F401

    src = ROOT / "writings/appendix/chapters/sources.md"
    if "row68-row134-export-meta-prelude-capstone-reunion-index-row-154" not in src.read_text():
        add_rows_154_155.add_sources_row(154, add_rows_154_155.lift_134_to_154, 134, 153)
        add_rows_154_155.add_sources_row(155, add_rows_154_155.lift_135_to_155, 135, 154)
    mem = ROOT / "writings/appendix/chapters/memory-sheet.md"
    if "row-154-baby-picture" not in mem.read_text():
        add_rows_154_155.add_memory_row(154, add_rows_154_155.lift_134_to_154, 134, "Row 133 baby picture")
        add_rows_154_155.add_memory_row(155, add_rows_154_155.lift_135_to_155, 135, "Row 134 baby picture")
    add_rows_154_155.patch_row_153_proceed_links()


if __name__ == "__main__":
    import importlib.util
    spec = importlib.util.spec_from_file_location("add_rows_154_155", ROOT / "scripts/add-rows-154-155.py")
    add_rows_154_155 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add_rows_154_155)
    fix_prologue()
    fix_preface_links()
    src = ROOT / "writings/appendix/chapters/sources.md"
    if "row68-row134-export-meta-prelude-capstone-reunion-index-row-154" not in src.read_text():
        add_rows_154_155.add_sources_row(154, add_rows_154_155.lift_134_to_154, 134, 153)
        add_rows_154_155.add_sources_row(155, add_rows_154_155.lift_135_to_155, 135, 154)
    mem = ROOT / "writings/appendix/chapters/memory-sheet.md"
    if "row-154-baby-picture" not in mem.read_text():
        add_rows_154_155.add_memory_row(154, add_rows_154_155.lift_134_to_154, 134, "Row 133 baby picture")
        add_rows_154_155.add_memory_row(155, add_rows_154_155.lift_135_to_155, 135, "Row 134 baby picture")
    add_rows_154_155.patch_row_153_proceed_links()
