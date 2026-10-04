#!/usr/bin/env python3
"""Add row 145 (Row 68 → Row 125 ↔ Row 65 second-pass meta prelude capstone on capstone path)."""
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


def lift_125_to_145(s: str) -> str:
    p = [
        ("Row 126 closing loop", "__ROW126_LOOP__"),
        ("Row 125 closing loop", "Row 145 closing loop"),
        ("row-126-closing-loop", "__ROW126_LOOP_ANCHOR__"),
        ("row-125-closing-loop", "row-145-closing-loop"),
        ("Row 126 closing stitch", "__ROW126_STITCH__"),
        ("Row 125 closing stitch", "Row 145 closing stitch"),
        ("row-126-closing-stitch", "__ROW126_STITCH_ANCHOR__"),
        ("row-125-closing-stitch", "row-145-closing-stitch"),
        ("prologue-preview-row-126", "__ROW126_PREVIEW__"),
        ("prologue-preview-row-125", "prologue-preview-row-145"),
        ("Row 126 preview", "__ROW126_PREVIEW_TEXT__"),
        ("Row 125 preview", "Row 145 preview"),
        ("Row 126 skill checkpoint", "__ROW126_SKILL__"),
        ("Row 125 skill checkpoint", "Row 145 skill checkpoint"),
        ("skill-navigation-row-126", "__ROW126_SKILL_NAV__"),
        ("skill-navigation-row-125", "skill-navigation-row-145"),
        ("memory sheet row 126", "__ROW126_MEM__"),
        ("memory sheet row 125", "memory sheet row 145"),
        ("Row 126 baby picture", "__ROW126_BABY__"),
        ("Row 125 baby picture", "Row 145 baby picture"),
        ("Row 126 three-way audit", "__ROW126_AUDIT__"),
        ("Row 125 three-way audit", "Row 145 three-way audit"),
        (
            "Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone",
            "Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
        ),
        (
            "row68-row105-second-pass-meta-prelude-capstone-reunion-index-row-125",
            "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
        ),
        (
            "row-125-baby-picture-row68-row105-second-pass-meta-prelude-capstone-reunion",
            "row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion",
        ),
        ("[row 126]", "__ROW126_REF__"),
        ("[row 106]", "[row 126]"),
        ("row 106", "row 126"),
        ("Row 106", "Row 126"),
        ("__ROW126_REF__", "[row 126]"),
        ("[row 125]", "__ROW125_REF__"),
        ("[row 105]", "[row 125]"),
        ("row 105", "row 125"),
        ("Row 105", "Row 125"),
        ("__ROW125_REF__", "[row 125]"),
        ("[row 124]", "__ROW124_REF__"),
        ("[row 104]", "[row 124]"),
        ("row 104", "row 124"),
        ("Row 104", "Row 124"),
        ("__ROW124_REF__", "[row 124]"),
        ("[row 123]", "__ROW123_REF__"),
        ("[row 103]", "[row 123]"),
        ("row 103", "row 123"),
        ("Row 103", "Row 123"),
        ("__ROW123_REF__", "[row 123]"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        ("(row 125)", "(row 145)"),
        ("__ROW126_LOOP__", "Row 126 closing loop"),
        ("__ROW126_LOOP_ANCHOR__", "row-126-closing-loop"),
        ("__ROW126_STITCH__", "Row 126 closing stitch"),
        ("__ROW126_STITCH_ANCHOR__", "row-126-closing-stitch"),
        ("__ROW126_PREVIEW__", "prologue-preview-row-126"),
        ("__ROW126_PREVIEW_TEXT__", "Row 126 preview"),
        ("__ROW126_SKILL__", "Row 126 skill checkpoint"),
        ("__ROW126_SKILL_NAV__", "skill-navigation-row-126"),
        ("__ROW126_MEM__", "memory sheet row 126"),
        ("__ROW126_BABY__", "Row 126 baby picture"),
        ("__ROW126_AUDIT__", "Row 126 three-way audit"),
        (
            "book-loop meta prelude capstone / second-pass meta prelude hinge",
            "book-loop meta prelude capstone / second-pass meta prelude hinge on the capstone path",
        ),
        (
            "at the second-pass meta prelude capstone boundary inside the coupling gate",
            "at the second-pass meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 65 reunion |", "Row 68 ↔ Row 65 reunion (capstone path) |"),
        (
            "[Row 68 → Row 85 second-pass meta prelude reunion index (row 105)]",
            "[Row 68 → Row 125 second-pass meta prelude capstone reunion index (row 145)]",
        ),
        (
            "row68-row85-second-pass-meta-prelude-reunion-index-row-105",
            "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
        ),
        (
            "verified book-loop meta prelude capstone closure (row 124)",
            "verified book-loop meta prelude capstone closure (row 144)",
        ),
        (
            "Row 68 → Row 65 meta (row 125)",
            "Row 68 → Row 65 meta (row 145)",
        ),
        (
            "before row 46 Writings canonical reunion opens",
            "before row 46 Writings canonical reunion opens on the capstone path",
        ),
        (
            "When row 125 is complete, proceed to [row 126]",
            "When row 145 is complete, proceed to [row 146](preface.md#skill-navigation-row-146) when row 68 closed but Writings canonical meta prelude still lags on the capstone path, "
            "to [row 126](preface.md#skill-navigation-row-126) when second-pass meta prelude capstone is clean but Writings canonical meta prelude still lags on the opening-hinge path, "
            "to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 Writings meta prelude audit alone, "
            "to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 second-pass meta prelude audit on the opening-hinge path alone, "
            "to [row 144](preface.md#skill-navigation-row-144) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the capstone path, "
            "to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, "
            "to [row 65](preface.md#skill-navigation-row-65) when only second-pass meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_125",
        ),
        (
            "second-pass meta prelude capstone at the meta-stitch boundary in reading time",
            "second-pass meta prelude capstone at the meta-stitch boundary in reading time on the capstone path",
        ),
        (
            "When row 65 feels like appendix homework after row 124 alone",
            "When row 65 feels like appendix homework after row 144 alone on the capstone path",
        ),
        (
            "When row 65 feels like appendix homework after row 144 alone",
            "When row 65 feels like appendix homework after row 144 alone on the capstone path",
        ),
        ("Recite [preface row 124]", "Recite [preface row 144]"),
        (
            "Proceed to [row 126](#row-126-closing-loop) when row 68 closed but Writings canonical meta still feels disconnected after row 125",
            "Proceed to [row 146](#row-146-closing-loop) when row 68 closed but Writings canonical meta prelude still lags after row 145 on the capstone path, "
            "to [row 126](#row-126-closing-loop) when row 68 closed but Writings canonical meta still feels disconnected after row 125 on the opening-hinge path",
        ),
        (
            "when opening [row 126](preface.md#skill-navigation-row-126) before row 65 closes",
            "when opening [row 146](preface.md#skill-navigation-row-146) before row 66 closes on the capstone path",
        ),
        (
            "when the reopening anchor is complete after row 124 but every chapter boundary still opens a skill checkpoint",
            "when the reopening anchor is complete on the capstone path after row 144 but every chapter boundary still opens a skill checkpoint",
        ),
        (
            "when row 124 closed but row 65 second-pass meta still feels like appendix homework",
            "when row 144 closed but row 65 second-pass meta still feels like appendix homework",
        ),
        (
            "when row 124 and row 65 both verify individually",
            "when row 144 and row 65 both verify individually",
        ),
        (
            "rear-view mirror of row 124's book-loop meta",
            "rear-view mirror of row 144's book-loop meta",
        ),
        (
            "read row 68 gate + row 124 or row 105 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud when the book loop closes on the capstone path but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm",
            "read row 68 gate + row 144 or row 125 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud when the book loop closes on the capstone path after verified book-loop meta prelude capstone but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm",
        ),
        (
            "before row 126 Writings canonical meta prelude capstone or row 66 workflow reunion opens on the capstone path",
            "before row 146 Writings canonical meta prelude capstone or row 66 workflow reunion opens on the capstone path",
        ),
        (
            "before row 126 Writings canonical meta prelude capstone opens",
            "before row 66 Writings canonical meta prelude opens on the capstone path",
        ),
        (
            "Confirm [row 124](preface.md#skill-navigation-row-124) or [Row 68 → Row 85 second-pass meta prelude reunion index (row 105)]",
            "Confirm [row 144](preface.md#skill-navigation-row-144) or [Row 68 → Row 125 second-pass meta prelude capstone reunion index (row 145)]",
        ),
        (
            "Row 125 does not replace row 68, row 65, row 124, row 105",
            "Row 145 does not replace row 68, row 65, row 144, row 125",
        ),
        (
            "[row 124](preface.md#skill-navigation-row-124) or [row 105](preface.md#skill-navigation-row-105)",
            "[row 144](preface.md#skill-navigation-row-144) or [row 125](preface.md#skill-navigation-row-125)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_125" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_125.*", "", out, flags=re.S)
    return out


def add_row_145() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-145" in preface and "### Row 145 skill checkpoint" in preface:
        print("preface: row 145 already present")
    else:
        m125 = re.search(
            r"(### Row 125 skill checkpoint.*?)(?=\n### Row 126 skill checkpoint)",
            preface,
            re.S,
        )
        if not m125:
            raise SystemExit("row 125 preface checkpoint missing")
        row145 = lift_125_to_145(m125.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row145 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 145")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-145-closing-loop" not in ep:
        block125 = extract_between(ep, "### Row 125 closing loop", "### Row 126 closing loop")
        block145 = lift_125_to_145(block125)
        ep = ep.replace("### Row 125 closing loop", block145 + "### Row 125 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 145 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 145) |"
    )
    if compass_line not in pro:
        line144 = (
            "| Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 144) |"
        )
        idx144 = pro.find(line144)
        if idx144 < 0:
            raise SystemExit("prologue compass row 144 not found")
        line_end144 = pro.find("\n", idx144)
        line125 = (
            "| Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 125) |"
        )
        idx125 = pro.find(line125)
        if idx125 < 0:
            raise SystemExit("prologue compass row 125 not found")
        line_end125 = pro.find("\n", idx125)
        compass145 = lift_125_to_145(pro[idx125:line_end125]) + "\n"
        pro = pro[: line_end144 + 1] + compass145 + pro[line_end144 + 1 :]
        preview125 = extract_between(
            pro,
            '| <span id="prologue-preview-row-125"></span>',
            '\n| <span id="prologue-preview-row-126">',
        )
        preview145 = lift_125_to_145(preview125)
        pro = pro.replace(
            '| <span id="prologue-preview-row-125"></span>',
            preview145 + '| <span id="prologue-preview-row-125"></span>',
            1,
        )
        if "row-145-closing-stitch" not in pro:
            stitch = (
                "**Row 145 closing stitch (Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-145-closing-stitch} "
                "When row 144 closed — book-loop meta prelude capstone verified, row 143 or row 124 recited on the capstone path, and the "
                "[prologue reopening anchor](#prologue-reopening-anchor) received the reader with `./scripts/test-fixtures.sh` green after verified orchestration meta prelude capstone — "
                "but **row 65 second-pass meta reunion still opens like standalone appendix coursework after the second-pass opening prelude chapter hinge on the capstone path** — "
                "the [preface row 145 When-to-pause opening sentence](../preface.md#skill-navigation-row-145) names the dual reunion before Writings canonical meta prelude reunion; "
                "read [preface row 145](../preface.md#skill-navigation-row-145), then the "
                "[Row 68 → Row 125 reunion index](../appendix/sources.md#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145), then "
                "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop) before row 66 Writings canonical meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 125 closing stitch", stitch + "**Row 125 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 145 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145" not in src:
        idx125 = src.find(
            "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)"
        )
        idx126 = src.find(
            "## Row 68 → Row 106 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 126)"
        )
        if idx125 < 0 or idx126 < 0:
            raise SystemExit("row 125/126 sources anchors missing")
        block = src[idx125:idx126]
        block145 = lift_125_to_145(block)
        table_row = (
            "| 145 | Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone (midpoint prelude gate ↔ book-loop meta prelude capstone ↔ row 65 meta) | "
            "[Row 68 → Row 125 second-pass meta prelude capstone reunion index](#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145) · "
            "[preface row 145](../preface.md#skill-navigation-row-145) · "
            "[prologue row 145 preview](../prologue/00-many-scales.md#prologue-preview-row-145) · "
            "[prologue row 145 closing stitch](../prologue/00-many-scales.md#row-145-closing-stitch) · "
            "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop) · "
            "[memory sheet row 145 baby picture](memory-sheet.md#row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 65 second-pass meta reunion still feels disconnected from verified book-loop meta prelude capstone on the capstone path** — "
            "read row 68 + row 144 or row 125 gate + epilogue second-pass cross-links + row 65; "
            "[preface row 65](../preface.md#skill-navigation-row-65) |\n"
        )
        src = src.replace(
            "| 144 | Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone",
            table_row + "| 144 | Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)",
            block145
            + "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)",
        )
        extra = (
            "[row 145](#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145) reunites **book-loop meta prelude capstone with the second-pass meta prelude capstone boundary** "
            "when row 144 closed book-loop meta prelude capstone at verified reopening anchor on the capstone path but epilogue second-pass cross-links and row 17 still read like separate courses after verified second-pass meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 144](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144) reunites **orchestration meta prelude capstone with the book-loop meta prelude capstone boundary** "
                "when row 143 closed orchestration meta prelude capstone at verified H1→OUT on the capstone path but epilogue book-loop cross-links and row 12 still read like separate courses after verified book-loop meta prelude meta;"
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 145 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-145-baby-picture" not in mem:
        baby125 = extract_between(mem, "### Row 125 baby picture", "### Row 126 baby picture")
        baby145 = lift_125_to_145(baby125)
        mem = mem.replace("### Row 126 baby picture", baby145 + "### Row 126 baby picture", 1)
        mem_table = (
            "| 145 | Meta | Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion | "
            "[Row 68 → Row 125 second-pass meta prelude capstone reunion index](sources.md#row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145) · "
            "[preface row 145 skill checkpoint](../preface.md#skill-navigation-row-145) · "
            "[prologue row 145 preview](../prologue/00-many-scales.md#prologue-preview-row-145) · "
            "[prologue row 145 closing stitch](../prologue/00-many-scales.md#row-145-closing-stitch) · "
            "[epilogue row 145 closing loop](../epilogue/multiscale.md#row-145-closing-loop) | "
            "Row 68 closed but row 65 second-pass meta reunion feels disconnected from verified book-loop meta prelude capstone on the capstone path — "
            "read row 68 + row 144 or row 125 gate + epilogue second-pass cross-links + row 65; "
            "[row 145 baby picture](#row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 125 | Meta | Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion |",
            mem_table + "| 125 | Meta | Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion |",
        )
        if "When row 144 closed but novel second pass still lags" not in mem:
            mem = mem.replace(
                "When row 143 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 144](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion).",
                "When row 143 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 144](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion). "
                "When row 144 closed but novel second pass still lags on the capstone path, switch to [row 145](#row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 145")
    else:
        print("memory-sheet: row 145 baby already present")


def main() -> None:
    add_row_145()


if __name__ == "__main__":
    main()
