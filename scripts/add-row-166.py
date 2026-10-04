#!/usr/bin/env python3
"""Add row 166 (Row 68 → Row 146 ↔ Row 66 Writings canonical meta prelude capstone on capstone path)."""
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


def lift_146_to_166(s: str) -> str:
    s = s.replace(
        "[row 146](preface.md#skill-navigation-row-146)",
        "__ROW146_HINGE__",
    )
    s = s.replace(
        "[row 145](preface.md#skill-navigation-row-145)",
        "[row 165](preface.md#skill-navigation-row-165)",
    )
    s = s.replace("skill-navigation-row-126", "__ROW126_NAV__")
    s = s.replace("skill-navigation-row-146", "__ROW166_NAV__")
    s = s.replace(
        "Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
        "__ROW166TITLE__",
    )

    p = [
        ("Row 167 closing loop", "__ROW167_LOOP__"),
        ("Row 146 closing loop", "Row 166 closing loop"),
        ("row-167-closing-loop", "__ROW167_LOOP_ANCHOR__"),
        ("row-146-closing-loop", "row-166-closing-loop"),
        ("Row 167 closing stitch", "__ROW167_STITCH__"),
        ("Row 146 closing stitch", "Row 166 closing stitch"),
        ("row-167-closing-stitch", "__ROW167_STITCH_ANCHOR__"),
        ("row-146-closing-stitch", "row-166-closing-stitch"),
        ("prologue-preview-row-167", "__ROW167_PREVIEW__"),
        ("prologue-preview-row-146", "prologue-preview-row-166"),
        ("Row 167 preview", "__ROW167_PREVIEW_TEXT__"),
        ("Row 146 preview", "Row 166 preview"),
        ("Row 167 skill checkpoint", "__ROW167_SKILL__"),
        ("Row 146 skill checkpoint", "Row 166 skill checkpoint"),
        ("skill-navigation-row-167", "__ROW167_SKILL_NAV__"),
        ("memory sheet row 167", "__ROW167_MEM__"),
        ("memory sheet row 146", "memory sheet row 166"),
        ("Row 167 baby picture", "__ROW167_BABY__"),
        ("Row 146 baby picture", "Row 166 baby picture"),
        ("Row 167 three-way audit", "__ROW167_AUDIT__"),
        ("Row 146 three-way audit", "Row 166 three-way audit"),
        (
            "Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone",
            "Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone",
        ),
        (
            "row68-row126-writings-meta-prelude-capstone-reunion-index-row-146",
            "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166",
        ),
        (
            "row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion",
            "row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion",
        ),
        ("[row 167]", "__ROW167_REF__"),
        ("[row 147]", "[row 167]"),
        ("row 147", "row 167"),
        ("Row 147", "Row 167"),
        ("__ROW167_REF__", "[row 167]"),
        ("[row 146]", "__ROW146_REF__"),
        ("[row 126]", "[row 146]"),
        ("row 126", "row 146"),
        ("Row 126", "Row 146"),
        ("__ROW146_REF__", "[row 146]"),
        ("[row 145]", "__ROW145_REF__"),
        ("[row 125]", "[row 145]"),
        ("row 125", "row 145"),
        ("Row 125", "Row 145"),
        ("__ROW145_REF__", "[row 145]"),
        ("(row 146)", "(row 166)"),
        ("__ROW167_LOOP__", "Row 167 closing loop"),
        ("__ROW167_LOOP_ANCHOR__", "row-167-closing-loop"),
        ("__ROW167_STITCH__", "Row 167 closing stitch"),
        ("__ROW167_STITCH_ANCHOR__", "row-167-closing-stitch"),
        ("__ROW167_PREVIEW__", "prologue-preview-row-167"),
        ("__ROW167_PREVIEW_TEXT__", "Row 167 preview"),
        ("__ROW167_SKILL__", "Row 167 skill checkpoint"),
        ("__ROW167_SKILL_NAV__", "skill-navigation-row-167"),
        ("__ROW167_MEM__", "memory sheet row 167"),
        ("__ROW167_BABY__", "Row 167 baby picture"),
        ("__ROW167_AUDIT__", "Row 167 three-way audit"),
        (
            "second-pass meta prelude capstone / Writings canonical meta prelude hinge",
            "second-pass meta prelude capstone / Writings canonical meta prelude hinge on the capstone path",
        ),
        (
            "at the Writings canonical meta prelude capstone boundary inside the coupling gate",
            "at the Writings canonical meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        (
            "verified second-pass meta prelude capstone closure (row 145)",
            "verified second-pass meta prelude capstone closure (row 165)",
        ),
        (
            "When row 146 is complete, proceed to [row 147]",
            "When row 166 is complete, proceed to [row 167](preface.md#skill-navigation-row-167) when row 68 closed but part-boundary meta prelude capstone still lags on the capstone path, "
            "to [row 146](preface.md#skill-navigation-row-146) when second-pass meta prelude capstone is clean but Writings canonical meta prelude still lags on the opening-hinge path, "
            "to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 Writings meta prelude audit alone, "
            "to [row 165](preface.md#skill-navigation-row-165) when second-pass meta prelude capstone still lags after verified book-loop meta prelude capstone on the capstone path, "
            "to [row 86](preface.md#skill-navigation-row-86) for the Row 68 ↔ Row 66 opening prelude audit alone, "
            "to [row 66](preface.md#skill-navigation-row-66) when only Writings canonical meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_146",
        ),
        (
            "Proceed to [row 147](#row-147-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 146 on the capstone path",
            "Proceed to [row 167](#row-167-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after row 166 on the capstone path, "
            "to [row 146](#row-146-closing-loop) when row 68 closed but part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 147](preface.md#skill-navigation-row-147) before row 67 closes on the capstone path",
            "when opening [row 167](preface.md#skill-navigation-row-167) before row 67 closes on the capstone path",
        ),
        (
            "When row 66 feels like build-script homework after row 145 alone on the capstone path",
            "When row 66 feels like build-script homework after row 165 alone on the capstone path",
        ),
        (
            "When row 66 feels like build-script homework after row 145 alone",
            "When row 66 feels like build-script homework after row 165 alone on the capstone path",
        ),
        ("Recite [preface row 145]", "Recite [preface row 165]"),
        (
            "when row 145 closed but row 66 Writings canonical meta still feels like build-script homework disconnected from verified second-pass meta prelude capstone",
            "when row 165 closed but row 66 Writings canonical meta still feels like build-script homework disconnected from verified second-pass meta prelude capstone",
        ),
        (
            "when row 145 and row 66 both verify individually",
            "when row 165 and row 66 both verify individually",
        ),
        (
            "rear-view mirror of row 145's second-pass meta → novel rhythm → canonical tree turn",
            "rear-view mirror of row 165's second-pass meta → novel rhythm → canonical tree turn",
        ),
        (
            "read row 68 gate + row 145 or row 126 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud when second pass reads as a novel on the capstone path after verified second-pass meta prelude capstone but the next edit opens src/part* instead of writings/",
            "read row 68 gate + row 165 or row 146 second-pass meta prelude capstone / Writings canonical meta prelude gate + epilogue writings cross-links + row 66 meta aloud when second pass reads as a novel on the capstone path after verified second-pass meta prelude capstone but the next edit opens src/part* instead of writings/",
        ),
        (
            "Confirm [row 145](preface.md#skill-navigation-row-145) or [Row 68 → Row 126 Writings canonical meta prelude capstone reunion index (row 146)](appendix/sources.md#row68-row126-writings-meta-prelude-capstone-reunion-index-row-146) recited",
            "Confirm [row 165](preface.md#skill-navigation-row-165) or [Row 68 → Row 146 Writings canonical meta prelude capstone reunion index (row 166)](appendix/sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) recited",
        ),
        (
            "Row 146 does not replace row 68, row 66, row 145, row 126, row 86, row 65, or row 46",
            "Row 166 does not replace row 68, row 66, row 165, row 146, row 86, row 65, or row 46",
        ),
        (
            "[row 145](preface.md#skill-navigation-row-145) or [row 126](preface.md#skill-navigation-row-126)",
            "[row 165](preface.md#skill-navigation-row-165) or [row 146](preface.md#skill-navigation-row-146)",
        ),
        (
            "When row 145 closed — second-pass meta prelude capstone verified, row 144 or row 126 recited on the capstone path",
            "When row 165 closed — second-pass meta prelude capstone verified, row 164 or row 146 recited on the capstone path",
        ),
        (
            "Row 68 → Row 66 meta (row 146)",
            "Row 68 → Row 66 meta (row 166)",
        ),
        (
            "before row 67 part-boundary meta prelude opens on the capstone path",
            "before row 67 part-boundary meta prelude opens on the capstone path",
        ),
        (
            "When row 145 closed but canonical tree discipline still lags on the capstone path, switch to [row 166](#row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion)",
            "When row 165 closed but canonical tree discipline still lags on the capstone path, switch to [row 166](#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion)",
        ),
        (
            "Proceed to [row 166](#row-166-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 145 on the capstone path",
            "Proceed to [row 166](#row-166-closing-loop) when row 68 closed but Writings canonical meta prelude capstone still lags after row 165 on the capstone path",
        ),
        (
            "when opening [row 166](preface.md#skill-navigation-row-146) before row 66 closes on the capstone path",
            "when opening [row 166](preface.md#skill-navigation-row-166) before row 67 closes on the capstone path",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_146" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_146.*", "", out, flags=re.S)
    out = out.replace("__ROW166TITLE__", "Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone")
    out = out.replace("__ROW166_NAV__", "skill-navigation-row-166")
    out = out.replace("__ROW126_NAV__", "skill-navigation-row-146")
    out = out.replace("__ROW146_HINGE__", "[row 146](preface.md#skill-navigation-row-146)")
    out = out.replace("on the capstone path on the capstone path", "on the capstone path")
    return out


def dedupe_epilogue_closing_loops() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    seen: set[str] = set()

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        if anchor in seen:
            return ""
        seen.add(anchor)
        return m.group(0)

    text = re.sub(
        r"(?ms)^### Row \d+ closing loop[^\n]*\{#(row-\d+-closing-loop)\}.*?(?=^### Row |\Z)",
        repl,
        text,
    )
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    path.write_text(text)
    print(f"epilogue: deduped closing loops ({len(seen)} unique anchors kept)")


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 166 skill checkpoint" in text:
        print("preface: row 166 already present")
        return
    m = re.search(
        r"(### Row 146 skill checkpoint.*?)(?=\n### Row 147 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 146 checkpoint missing")
    block = lift_146_to_166(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 166")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 166 closing loop" in text:
        print("epilogue: row 166 loop already present")
        return
    block = lift_146_to_166(
        extract_between(
            text,
            "### Row 146 closing loop",
            "### Row 126 closing loop",
        )
    )
    needle = "### Row 165 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 166 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 166) |"
    if compass in text:
        print("prologue: row 166 compass already present")
    else:
        after = "| Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 165) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 165 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 146) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 146 compass missing")
        new_line = lift_146_to_166(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-146"></span>'
    preview_dst = '| <span id="prologue-preview-row-166"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_146_to_166(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 166 closing stitch" not in text:
        stitch = (
            "**Row 166 closing stitch (Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion).** {#row-166-closing-stitch} "
            "When row 165 closed — second-pass meta prelude capstone verified, row 164 or row 146 recited on the capstone path, and Scene → Bridge rhythm trusted after verified book-loop meta prelude capstone — "
            "but **row 66 Writings canonical meta reunion still opens like standalone maintainer coursework after the Writings canonical opening prelude chapter hinge on the capstone path** — "
            "the [preface row 166 When-to-pause opening sentence](../preface.md#skill-navigation-row-166) names the dual reunion before part-boundary meta prelude reunion; "
            "read [preface row 166](../preface.md#skill-navigation-row-166), then the "
            "[Row 68 → Row 146 reunion index](../appendix/sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166), then "
            "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) before row 67 part-boundary meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 165 closing stitch", stitch + "**Row 165 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 166 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row146-writings-meta-prelude-capstone-reunion-index-row-166"
    if idx_key in text:
        print("sources: row 166 already present")
        return
    start = "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 146 index missing")
    block = lift_146_to_166(text[i:])
    block = block.replace(
        "## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 166)",
        f"## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 166) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 166 | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone "
        "(midpoint prelude gate ↔ second-pass meta prelude capstone ↔ row 66 meta) | "
        f"[Row 68 → Row 146 Writings canonical meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 166](../preface.md#skill-navigation-row-166) · "
        "[prologue row 166 preview](../prologue/00-many-scales.md#prologue-preview-row-166) · "
        "[prologue row 166 closing stitch](../prologue/00-many-scales.md#row-166-closing-stitch) · "
        "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) · "
        "[memory sheet row 166 baby picture](memory-sheet.md#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 66 Writings canonical meta reunion still feels disconnected from verified second-pass meta prelude capstone on the capstone path** — "
        "read row 68 + row 165 or row 146 gate + epilogue writings cross-links + row 66; "
        "[preface row 66](../preface.md#skill-navigation-row-66) |\n"
    )
    text = text.replace(
        "| 165 | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone",
        table_row + "| 165 | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)",
        block + "## Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion index (row 146)",
    )
    extra = (
        f"[row 166](#{idx_key}) reunites **second-pass meta prelude capstone with the Writings canonical meta prelude capstone boundary** "
        "when row 165 closed second-pass meta prelude capstone at verified novel rhythm on the capstone path but epilogue writings cross-links and row 46 still read like separate courses after verified Writings canonical meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 165](#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165) reunites **book-loop meta prelude capstone with the second-pass meta prelude capstone boundary** "
            "when row 164 closed book-loop meta prelude capstone at verified reopening anchor on the capstone path but epilogue second-pass cross-links and row 17 still read like separate courses after verified second-pass meta prelude meta;"
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 166")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 166 already present")
        return
    baby = lift_146_to_166(
        extract_between(
            text,
            "### Row 146 baby picture (Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion}",
            "### Row 147 baby picture",
        )
    )
    anchor = "### Row 146 baby picture (Row 68 → Row 126 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion}"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 166 | Meta | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion | "
        "[Row 68 → Row 146 Writings canonical meta prelude capstone reunion index](sources.md#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) · "
        "[preface row 166 skill checkpoint](../preface.md#skill-navigation-row-166) · "
        "[prologue row 166 preview](../prologue/00-many-scales.md#prologue-preview-row-166) · "
        "[prologue row 166 closing stitch](../prologue/00-many-scales.md#row-166-closing-stitch) · "
        "[epilogue row 166 closing loop](../epilogue/multiscale.md#row-166-closing-loop) | "
        "Row 68 closed but row 66 Writings canonical meta reunion feels disconnected from verified second-pass meta prelude capstone on the capstone path — "
        "read row 68 + row 165 or row 146 gate + epilogue writings cross-links + row 66; "
        "[row 166 baby picture](#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 165 | Meta | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion |",
        mem_table + "| 165 | Meta | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion |",
    )
    switch = (
        "When row 165 closed but canonical tree discipline still lags on the capstone path, switch to [row 166](#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion)."
    )
    if switch not in text:
        text = text.replace(
            "When row 145 closed but canonical tree discipline still lags on the capstone path, switch to [row 166](#row-146-baby-picture-row68-row126-writings-meta-prelude-capstone-reunion).",
            "When row 165 closed but canonical tree discipline still lags on the capstone path, switch to [row 166](#row-166-baby-picture-row68-row146-writings-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 166")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
