#!/usr/bin/env python3
"""Add row 146 (Row 68 → Row 126 ↔ Row 66 Writings canonical meta prelude capstone on capstone path)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]



def lift_126_to_146(s: str) -> str:
    p = [
        ("Row 127 closing loop", "__ROW127_LOOP__"),
        ("Row 126 closing loop", "Row 146 closing loop"),
        ("row-127-closing-loop", "__ROW127_LOOP_ANCHOR__"),
        ("row-126-closing-loop", "row-146-closing-loop"),
        ("Row 127 closing stitch", "__ROW127_STITCH__"),
        ("Row 126 closing stitch", "Row 146 closing stitch"),
        ("row-127-closing-stitch", "__ROW127_STITCH_ANCHOR__"),
        ("row-126-closing-stitch", "row-146-closing-stitch"),
        ("prologue-preview-row-127", "__ROW127_PREVIEW__"),
        ("prologue-preview-row-126", "prologue-preview-row-146"),
        ("Row 127 preview", "__ROW127_PREVIEW_TEXT__"),
        ("Row 126 preview", "Row 146 preview"),
        ("Row 127 skill checkpoint", "__ROW127_SKILL__"),
        ("Row 126 skill checkpoint", "Row 146 skill checkpoint"),
        ("skill-navigation-row-127", "__ROW127_SKILL_NAV__"),
        ("skill-navigation-row-126", "skill-navigation-row-146"),
        ("memory sheet row 127", "__ROW127_MEM__"),
        ("memory sheet row 126", "memory sheet row 146"),
        ("Row 127 baby picture", "__ROW127_BABY__"),
        ("Row 126 baby picture", "Row 146 baby picture"),
        ("Row 127 three-way audit", "__ROW127_AUDIT__"),
        ("Row 126 three-way audit", "Row 146 three-way audit"),
        (
            "Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone",
            "Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
        ),
        (
            "row68-row106-writings-meta-prelude-capstone-reunion-index-row-126",
            "row68-row126-writings-meta-prelude-capstone-reunion-index-row-146",
        ),
        (
            "row-126-baby-picture-row68-row106-writings-meta-prelude-capstone-reunion",
            "row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion",
        ),
        ("[row 127]", "__ROW127_REF__"),
        ("[row 107]", "[row 127]"),
        ("row 107", "row 127"),
        ("Row 107", "Row 127"),
        ("__ROW127_REF__", "[row 127]"),
        ("[row 126]", "__ROW126_REF__"),
        ("[row 106]", "[row 126]"),
        ("row 106", "row 126"),
        ("Row 106", "Row 126"),
        ("__ROW126_REF__", "[row 126]"),
        ("[row 125]", "__ROW125_REF__"),
        ("__ROW125_REF__", "[row 125]"),
        ("(row 126)", "(row 146)"),
        ("__ROW127_LOOP__", "Row 127 closing loop"),
        ("__ROW127_LOOP_ANCHOR__", "row-127-closing-loop"),
        ("__ROW127_STITCH__", "Row 127 closing stitch"),
        ("__ROW127_STITCH_ANCHOR__", "row-127-closing-stitch"),
        ("__ROW127_PREVIEW__", "prologue-preview-row-127"),
        ("__ROW127_PREVIEW_TEXT__", "Row 127 preview"),
        ("__ROW127_SKILL__", "Row 127 skill checkpoint"),
        ("__ROW127_SKILL_NAV__", "skill-navigation-row-127"),
        ("__ROW127_MEM__", "memory sheet row 127"),
        ("__ROW127_BABY__", "Row 127 baby picture"),
        ("__ROW127_AUDIT__", "Row 127 three-way audit"),
        ("Row 68 ↔ Row 66 reunion (capstone path) |", "Row 68 ↔ Row 66 reunion (capstone path) |"),
        (
            "second-pass meta prelude capstone / Writings canonical meta prelude hinge",
            "second-pass meta prelude capstone / Writings canonical meta prelude hinge on the capstone path",
        ),
        (
            "at the Writings canonical meta prelude capstone boundary inside the coupling gate",
            "at the Writings canonical meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        (
            "verified second-pass meta prelude capstone closure (row 125)",
            "verified second-pass meta prelude capstone closure (row 145)",
        ),
        (
            "When row 126 is complete, proceed to [row 127]",
            "When row 146 is complete, proceed to [row 127](preface.md#skill-navigation-row-127) when row 68 closed but part-boundary meta prelude capstone still lags on the capstone path, "
            "to [row 126](preface.md#skill-navigation-row-126) when second-pass meta prelude capstone is clean but Writings canonical meta prelude still lags on the opening-hinge path, "
            "to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 Writings meta prelude audit alone, "
            "to [row 145](preface.md#skill-navigation-row-145) when second-pass meta prelude capstone still lags after verified book-loop meta prelude capstone on the capstone path, "
            "to [row 86](preface.md#skill-navigation-row-86) for the Row 68 ↔ Row 66 opening prelude audit alone, "
            "to [row 66](preface.md#skill-navigation-row-66) when only Writings canonical meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_126",
        ),
        (
            "Proceed to [row 127](#row-127-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the capstone path",
            "Proceed to [row 127](#row-127-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 146 on the capstone path, "
            "to [row 126](#row-126-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 127](preface.md#skill-navigation-row-127) before row 67 closes on the capstone path",
            "when opening [row 127](preface.md#skill-navigation-row-127) before row 67 closes on the capstone path",
        ),
        (
            "When row 66 feels like build-script homework after row 125 alone",
            "When row 66 feels like build-script homework after row 145 alone on the capstone path",
        ),
        ("Recite [preface row 125]", "Recite [preface row 145]"),
        (
            "when row 125 closed but row 66 Writings canonical meta still feels like build-script homework disconnected from verified second-pass meta prelude capstone",
            "when row 145 closed but row 66 Writings canonical meta still feels like build-script homework disconnected from verified second-pass meta prelude capstone",
        ),
        (
            "when row 125 and row 66 both verify individually",
            "when row 145 and row 66 both verify individually",
        ),
        (
            "rear-view mirror of row 125's second-pass meta → novel rhythm → canonical tree turn",
            "rear-view mirror of row 145's second-pass meta → novel rhythm → canonical tree turn",
        ),
        (
            "read row 68 gate + row 125 or row 106 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud when second pass reads as a novel on the capstone path but the next edit opens src/part* instead of writings/",
            "read row 68 gate + row 145 or row 126 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud when second pass reads as a novel on the capstone path after verified second-pass meta prelude capstone but the next edit opens src/part* instead of writings/",
        ),
        (
            "Confirm [row 125](preface.md#skill-navigation-row-125) or [Row 68 → Row 86 Writings meta prelude reunion index (row 106)](appendix/sources.md#row68-row86-writings-meta-prelude-reunion-index-row-106) recited",
            "Confirm [row 145](preface.md#skill-navigation-row-145) or [Row 68 → Row 126 Writings canonical meta prelude capstone reunion index (row 146)](appendix/sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146) recited",
        ),
        (
            "Row 126 does not replace row 68, row 66, row 125, row 106, row 86, row 65, or row 46",
            "Row 146 does not replace row 68, row 66, row 145, row 126, row 86, row 65, or row 46",
        ),
        (
            "[row 125](preface.md#skill-navigation-row-125) or [row 106](preface.md#skill-navigation-row-106)",
            "[row 145](preface.md#skill-navigation-row-145) or [row 126](preface.md#skill-navigation-row-126)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_126" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_126.*", "", out, flags=re.S)
    return out


def add_row_146() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-146" in preface and "### Row 146 skill checkpoint" in preface:
        print("preface: row 146 already present")
    else:
        m126 = re.search(
            r"(### Row 126 skill checkpoint.*?)(?=\n### Row 127 skill checkpoint)",
            preface,
            re.S,
        )
        if not m126:
            raise SystemExit("row 126 preface checkpoint missing")
        row146 = lift_126_to_146(m126.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row146 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 146")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-146-closing-loop" not in ep:
        block126 = extract_between(ep, "### Row 126 closing loop", "### Row 127 closing loop")
        block146 = lift_126_to_146(block126)
        ep = ep.replace("### Row 125 closing loop", block146 + "### Row 125 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 146 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 146) |"
    )
    if compass_line not in pro:
        line145 = (
            "| Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 145) |"
        )
        idx145 = pro.find(line145)
        if idx145 < 0:
            raise SystemExit("prologue compass row 145 not found")
        line_end145 = pro.find("\n", idx145)
        line126 = (
            "| Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 126) |"
        )
        idx126 = pro.find(line126)
        if idx126 < 0:
            raise SystemExit("prologue compass row 126 not found")
        line_end126 = pro.find("\n", idx126)
        compass146 = lift_126_to_146(pro[idx126:line_end126]) + "\n"
        pro = pro[: line_end145 + 1] + compass146 + pro[line_end145 + 1 :]
        preview126 = extract_between(
            pro,
            '| <span id="prologue-preview-row-127"></span>',
            '\n| <span id="prologue-preview-row-127">',
        )
        preview146 = lift_126_to_146(preview126)
        pro = pro.replace(
            '| <span id="prologue-preview-row-127"></span>',
            preview146 + '| <span id="prologue-preview-row-127"></span>',
            1,
        )
        if "row-146-closing-stitch" not in pro:
            stitch = (
                "**Row 145 closing stitch (Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-146-closing-stitch} "
                "When row 145 closed — second-pass meta prelude capstone verified, row 144 or row 126 recited on the capstone path, and Scene → Bridge rhythm trusted after verified book-loop meta prelude capstone — "
                ""
                "but **row 66 Writings canonical meta reunion still opens like standalone maintainer coursework after the Writings canonical opening prelude chapter hinge on the capstone path** — "
                "the [preface row 145 When-to-pause opening sentence](../preface.md#skill-navigation-row-146) names the dual reunion before Writings canonical meta prelude reunion; "
                "read [preface row 145](../preface.md#skill-navigation-row-146), then the "
                "[Row 68 → Row 126 reunion index](../appendix/sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146), then "
                "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-146-closing-loop) before row 66 Writings canonical meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 126 closing stitch", stitch + "**Row 126 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 146 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row126-writings-meta-prelude-capstone-reunion-index-row-146" not in src:
        idx126 = src.find(
            "## Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 127)"
        )
        idx126 = src.find(
            "## Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 127)"
        )
        if idx126 < 0 or idx126 < 0:
            raise SystemExit("row 126/127 sources anchors missing")
        block = src[idx126:idx126]
        block146 = lift_126_to_146(block)
        table_row = (
            "| 146 | Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone (midpoint prelude gate ↔ book-loop meta prelude capstone ↔ row 65 meta) | "
            "[Row 68 → Row 125 second-pass meta prelude capstone reunion index](#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146) · "
            "[preface row 145](../preface.md#skill-navigation-row-146) · "
            "[prologue row 145 preview](../prologue/00-many-scales.md#prologue-preview-row-145) · "
            "[prologue row 145 closing stitch](../prologue/00-many-scales.md#row-146-closing-stitch) · "
            "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-146-closing-loop) · "
            "[memory sheet row 145 baby picture](memory-sheet.md#row-146-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 66 Writings canonical meta reunion still feels disconnected from verified second-pass meta prelude capstone on the capstone path** — "
            "read row 68 + row 145 or row 126 gate + epilogue writings cross-links + row 66; "
            "[preface row 66](../preface.md#skill-navigation-row-65) |\n"
        )
        src = src.replace(
            "| 145 | Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
            table_row + "| 145 | Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 127)",
            block146
            + "## Row 68 → Row 107 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 127)",
        )
        extra = (
            "[row 145](#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146) reunites **book-loop meta prelude capstone with the second-pass meta prelude capstone boundary** "
            "when row 145 closed second-pass meta prelude capstone at verified novel rhythm on the capstone path but epilogue writings cross-links and row 46 still read like separate courses after verified Writings canonical meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 145](#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145) reunites **orchestration meta prelude capstone with the book-loop meta prelude capstone boundary** "
                "when row 143 closed orchestration meta prelude capstone at verified H1→OUT on the capstone path but epilogue book-loop cross-links and row 12 still read like separate courses after verified book-loop meta prelude meta;"
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 146 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-146-baby-picture" not in mem:
        baby126 = extract_between(mem, "### Row 126 baby picture", "### Row 127 baby picture")
        baby146 = lift_126_to_146(baby126)
        mem = mem.replace("### Row 126 baby picture", baby146 + "### Row 126 baby picture", 1)
        mem_table = (
            "| 146 | Meta | Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion | "
            "[Row 68 → Row 125 second-pass meta prelude capstone reunion index](sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146) · "
            "[preface row 145 skill checkpoint](../preface.md#skill-navigation-row-146) · "
            "[prologue row 145 preview](../prologue/00-many-scales.md#prologue-preview-row-145) · "
            "[prologue row 145 closing stitch](../prologue/00-many-scales.md#row-146-closing-stitch) · "
            "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-146-closing-loop) | "
            "Row 68 closed but row 65 second-pass meta reunion feels disconnected from verified book-loop meta prelude capstone on the capstone path — "
            "read row 68 + row 145 or row 126 gate + epilogue writings cross-links + row 66; "
            "[row 145 baby picture](#row-146-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 126 | Meta | Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion |",
            mem_table + "| 126 | Meta | Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion |",
        )
        if "When row 145 closed but canonical tree discipline still lags" not in mem:
            mem = mem.replace(
                "When row 143 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 144](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion).",
                "When row 143 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 144](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion). "
                "When row 145 closed but canonical tree discipline still lags on the capstone path, switch to [row 145](#row-146-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 146")
    else:
        print("memory-sheet: row 146 baby already present")


def main() -> None:
    add_row_146()


if __name__ == "__main__":
    main()
