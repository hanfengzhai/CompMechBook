#!/usr/bin/env python3
"""Repair row 154 inserts and add missing epilogue closing loop."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def main() -> None:
    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "### Row 154 closing loop" not in ep:
        start = ep.find("### Row 134 closing loop")
        end = ep.find("\n### Row 153 closing loop", start)
        if start < 0 or end < 0:
            raise SystemExit("row 134 epilogue block missing")
        block134 = ep[start:end]
        block154 = tx(
            block134,
            [
                ("Row 134 closing loop", "Row 154 closing loop"),
                ("row-134-closing-loop", "row-154-closing-loop"),
                ("memory sheet row 134", "memory sheet row 154"),
                ("preface row 134", "preface row 154"),
                ("skill-navigation-row-134", "skill-navigation-row-154"),
                ("Row 68 → Row 114", "Row 68 → Row 134"),
                (
                    "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
                    "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
                ),
                ("prologue-preview-row-134", "prologue-preview-row-154"),
                ("row-134-closing-stitch", "row-154-closing-stitch"),
                ("row 133 closed dynamics", "row 153 closed dynamics"),
                ("closure (row 133)", "closure (row 153)"),
                ("Row 68 → Row 54 meta (row 114)", "Row 68 → Row 54 meta (row 134)"),
                ("after row 133 alone", "after row 153 alone"),
                ("row 134 (row 68 ↔ row 54", "row 154 (row 68 ↔ row 54"),
                ("row 114 (opening-hinge", "row 134 (opening-hinge"),
                ("row 134 names **why", "row 154 names **why"),
                ("verified dynamics meta prelude capstone (row 133)", "verified dynamics meta prelude capstone (row 153)"),
                (
                    "Proceed to [row 115](#row-115-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134",
                    "Proceed to [row 155](#row-155-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 154 on the capstone path",
                ),
                (
                    "to [row 133](#row-153-closing-loop) when dynamics meta prelude capstone still lags after row 151",
                    "to [row 153](#row-153-closing-loop) when dynamics meta prelude capstone still lags after row 152 on the capstone path",
                ),
                (
                    "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
                    "row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion",
                ),
            ],
        )
        ep = ep[:start] + block154 + "\n\n" + ep[start:]
        ep_path.write_text(ep)
        print("epilogue: inserted row 154 closing loop")

    ep = ep_path.read_text()
    ep = ep.replace(
        "after row 153 on the capstone path on the capstone path",
        "after row 153 on the capstone path",
    )
    ep_path.write_text(ep)

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = tx(
        preface,
        [
            ("[row 153](preface.md#skill-navigation-row-133)", "[row 153](preface.md#skill-navigation-row-153)"),
            (
                "row68-row134-export-meta-prelude-capstone-reunion-index-row-154) recited",
                "row68-row94-export-meta-prelude-reunion-index-row-114) recited",
            ),
            ("([row 134](prologue/00-many-scales.md#prologue-preview-row-154)", "([row 154](prologue/00-many-scales.md#prologue-preview-row-154)"),
            (
                "When row 134 is complete, proceed to [row 135]",
                "When row 154 is complete, proceed to [row 155]",
            ),
        ],
    )
    preface_path.write_text(preface)
    print("preface: fixed row 154 links")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    pro = pro.replace(
        "export meta prelude capstone reunion (row 134) | [Preface: row 134 skill checkpoint](../preface.md#skill-navigation-row-154)",
        "export meta prelude capstone reunion (row 154) | [Preface: row 154 skill checkpoint](../preface.md#skill-navigation-row-154)",
    )
    if "prologue-preview-row-154" not in pro:
        preview = (
            '| <span id="prologue-preview-row-154"></span>Row 154 preview (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion) | '
            "Explain why midpoint closure (row 68) and VIII.2 → VIII.3 meta (row 54) must be read together with the Bridge → pedigree chain "
            "after verified dynamics meta prelude capstone (row 153) before dynamics manifest and coarse-graining sections feel like separate courses on the capstone path | "
            'One sentence: "read row 68 gate + row 153 or row 134 dynamics meta prelude capstone / export meta prelude gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54 meta aloud '
            'when NPT dynamics is clean on the capstone path but yaml exports feel like standalone post-processing after verified dynamics meta prelude capstone" — '
            "[preface row 154 skill checkpoint](../preface.md#skill-navigation-row-154); [prologue row 154 closing stitch](#row-154-closing-stitch); "
            "[Row 68 → Row 134 reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154); "
            "[memory sheet row 154 baby picture](../appendix/memory-sheet.md#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion); "
            "[VIII.2 Bridge](../part08-md/02-ensembles-integrators.md#bridge); "
            "[VIII.3 opening hinge from VIII.2](../part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3); "
            "[preface row 54 skill checkpoint](../preface.md#skill-navigation-row-54); "
            "[preface row 153 skill checkpoint](../preface.md#skill-navigation-row-153); "
            "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) |\n"
        )
        pro = pro.replace(
            '| <span id="prologue-preview-row-153"></span>',
            preview + '| <span id="prologue-preview-row-153"></span>',
            1,
        )
    pro_path.write_text(pro)
    print("prologue: fixed compass/preview")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    src = src.replace(
        "export meta prelude capstone reunion index (row 134) {#row68-row134-export-meta-prelude-capstone-reunion-index-row-154}",
        "export meta prelude capstone reunion index (row 154) {#row68-row134-export-meta-prelude-capstone-reunion-index-row-154}",
    )
    src = src.replace(
        "[Preface row 134](../preface.md#skill-navigation-row-154)",
        "[Preface row 154](../preface.md#skill-navigation-row-154)",
    )
    src_path.write_text(src)

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    mem = tx(
        mem,
        [
            ("[preface row 153](../preface.md#skill-navigation-row-133)", "[preface row 153](../preface.md#skill-navigation-row-153)"),
            (
                "Row 68 → Row 114 export meta prelude capstone reunion index",
                "Row 68 → Row 134 export meta prelude capstone reunion index",
            ),
            ("When row 134 feels disconnected from row 153", "When row 154 feels disconnected from row 153"),
            ("row 134 when **VIII.2 Bridge", "row 154 when **VIII.2 Bridge"),
            ("switch to [row 134](#row-154-baby-picture", "switch to [row 154](#row-154-baby-picture"),
            ("When row 153 closed but export meta reunion still lags on the capstone path, switch to [row 134](#row-154-baby-picture", "When row 153 closed but export meta reunion still lags on the capstone path, switch to [row 154](#row-154-baby-picture"),
        ],
    )
    mem_path.write_text(mem)
    print("sources/memory: fixed row 154 labels")


if __name__ == "__main__":
    main()
