#!/usr/bin/env python3
"""Add row 165 (Row 68 → Row 145 ↔ Row 65 second-pass meta prelude capstone on capstone path)."""
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


def lift_145_to_165(s: str) -> str:
    s = s.replace(
        "[row 145](preface.md#skill-navigation-row-145)",
        "__ROW145_HINGE__",
    )
    s = s.replace("skill-navigation-row-145", "__ROW165_NAV__")
    s = s.replace(
        "Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
        "__ROW165TITLE__",
    )

    p = [
        ("Row 166 closing loop", "__ROW166_LOOP__"),
        ("Row 145 closing loop", "Row 165 closing loop"),
        ("row-166-closing-loop", "__ROW166_LOOP_ANCHOR__"),
        ("row-145-closing-loop", "row-165-closing-loop"),
        ("Row 166 closing stitch", "__ROW166_STITCH__"),
        ("Row 145 closing stitch", "Row 165 closing stitch"),
        ("row-166-closing-stitch", "__ROW166_STITCH_ANCHOR__"),
        ("row-145-closing-stitch", "row-165-closing-stitch"),
        ("prologue-preview-row-166", "__ROW166_PREVIEW__"),
        ("prologue-preview-row-145", "prologue-preview-row-165"),
        ("Row 166 preview", "__ROW166_PREVIEW_TEXT__"),
        ("Row 145 preview", "Row 165 preview"),
        ("Row 166 skill checkpoint", "__ROW166_SKILL__"),
        ("Row 145 skill checkpoint", "Row 165 skill checkpoint"),
        ("skill-navigation-row-166", "__ROW166_SKILL_NAV__"),
        ("skill-navigation-row-145", "skill-navigation-row-165"),
        ("memory sheet row 166", "__ROW166_MEM__"),
        ("memory sheet row 145", "memory sheet row 165"),
        ("Row 166 baby picture", "__ROW166_BABY__"),
        ("Row 145 baby picture", "Row 165 baby picture"),
        ("Row 166 three-way audit", "__ROW166_AUDIT__"),
        ("Row 145 three-way audit", "Row 165 three-way audit"),
        (
            "Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone",
            "Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone",
        ),
        (
            "row68-row125-second-pass-meta-prelude-capstone-reunion-index-row-145",
            "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
        ),
        (
            "row-145-baby-picture-row68-row125-second-pass-meta-prelude-capstone-reunion",
            "row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion",
        ),
        ("[row 166]", "__ROW166_REF__"),
        ("[row 106]", "[row 166]"),
        ("row 106", "row 166"),
        ("Row 106", "Row 166"),
        ("__ROW166_REF__", "[row 166]"),
        ("[row 145]", "__ROW145_REF__"),
        ("[row 125]", "[row 145]"),
        ("row 125", "row 145"),
        ("Row 125", "Row 145"),
        ("__ROW145_REF__", "[row 145]"),
        ("[row 144]", "__ROW144_REF__"),
        ("[row 104]", "[row 144]"),
        ("row 104", "row 144"),
        ("Row 104", "Row 144"),
        ("__ROW144_REF__", "[row 144]"),
        ("[row 123]", "__ROW123_REF__"),
        ("[row 103]", "[row 123]"),
        ("row 103", "row 123"),
        ("Row 103", "Row 123"),
        ("__ROW123_REF__", "[row 123]"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        ("(row 145)", "(row 165)"),
        ("__ROW166_LOOP__", "Row 166 closing loop"),
        ("__ROW166_LOOP_ANCHOR__", "row-166-closing-loop"),
        ("__ROW166_STITCH__", "Row 166 closing stitch"),
        ("__ROW166_STITCH_ANCHOR__", "row-166-closing-stitch"),
        ("__ROW166_PREVIEW__", "prologue-preview-row-166"),
        ("__ROW166_PREVIEW_TEXT__", "Row 166 preview"),
        ("__ROW166_SKILL__", "Row 166 skill checkpoint"),
        ("__ROW166_SKILL_NAV__", "skill-navigation-row-166"),
        ("__ROW166_MEM__", "memory sheet row 166"),
        ("__ROW166_BABY__", "Row 166 baby picture"),
        ("__ROW166_AUDIT__", "Row 166 three-way audit"),
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
            "[Row 68 → Row 85 second-pass meta prelude reunion index (row 125)]",
            "[Row 68 → Row 145 second-pass meta prelude capstone reunion index (row 165)]",
        ),
        (
            "row68-row85-second-pass-meta-prelude-reunion-index-row-125",
            "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165",
        ),
        (
            "verified book-loop meta prelude capstone closure (row 144)",
            "verified book-loop meta prelude capstone closure (row 164)",
        ),
        (
            "Row 68 → Row 65 meta (row 145)",
            "Row 68 → Row 65 meta (row 165)",
        ),
        (
            "before row 46 Writings canonical reunion opens",
            "before row 46 Writings canonical reunion opens on the capstone path",
        ),
        (
            "When row 145 is complete, proceed to [row 166]",
            "When row 165 is complete, proceed to [row 146](preface.md#skill-navigation-row-146) when row 68 closed but Writings canonical meta prelude still lags on the capstone path, "
            "to [row 166](preface.md#skill-navigation-row-166) when second-pass meta prelude capstone is clean but Writings canonical meta prelude still lags on the opening-hinge path, "
            "to [row 106](preface.md#skill-navigation-row-106) for the Row 68 ↔ Row 66 Writings meta prelude audit alone, "
            "to [row 125](preface.md#skill-navigation-row-125) for the Row 68 ↔ Row 65 second-pass meta prelude audit on the opening-hinge path alone, "
            "to [row 164](preface.md#skill-navigation-row-164) when book-loop meta prelude capstone still lags after verified orchestration meta prelude capstone on the capstone path, "
            "to [row 85](preface.md#skill-navigation-row-85) for the Row 68 ↔ Row 65 opening prelude audit alone, "
            "to [row 65](preface.md#skill-navigation-row-65) when only second-pass meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_145",
        ),
        (
            "second-pass meta prelude capstone at the meta-stitch boundary in reading time",
            "second-pass meta prelude capstone at the meta-stitch boundary in reading time on the capstone path",
        ),
        (
            "When row 65 feels like appendix homework after row 144 alone",
            "When row 65 feels like appendix homework after row 164 alone on the capstone path",
        ),
        (
            "When row 65 feels like appendix homework after row 164 alone",
            "When row 65 feels like appendix homework after row 164 alone on the capstone path",
        ),
        ("Recite [preface row 144]", "Recite [preface row 164]"),
        (
            "Proceed to [row 166](#row-166-closing-loop) when row 68 closed but Writings canonical meta still feels disconnected after row 145",
            "Proceed to [row 146](#row-146-closing-loop) when row 68 closed but Writings canonical meta prelude still lags after row 165 on the capstone path, "
            "to [row 166](#row-166-closing-loop) when row 68 closed but Writings canonical meta still feels disconnected after row 145 on the opening-hinge path",
        ),
        (
            "when opening [row 166](preface.md#skill-navigation-row-166) before row 65 closes",
            "when opening [row 146](preface.md#skill-navigation-row-146) before row 66 closes on the capstone path",
        ),
        (
            "when the reopening anchor is complete after row 144 but every chapter boundary still opens a skill checkpoint",
            "when the reopening anchor is complete on the capstone path after row 164 but every chapter boundary still opens a skill checkpoint",
        ),
        (
            "when row 144 closed but row 65 second-pass meta still feels like appendix homework",
            "when row 164 closed but row 65 second-pass meta still feels like appendix homework",
        ),
        (
            "when row 144 and row 65 both verify individually",
            "when row 164 and row 65 both verify individually",
        ),
        (
            "rear-view mirror of row 144's book-loop meta",
            "rear-view mirror of row 164's book-loop meta",
        ),
        (
            "read row 68 gate + row 144 or row 125 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud when the book loop closes on the capstone path but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm",
            "read row 68 gate + row 164 or row 145 book-loop meta prelude capstone / second-pass meta prelude gate + epilogue second-pass cross-links + row 65 meta aloud when the book loop closes on the capstone path after verified book-loop meta prelude capstone but every chapter boundary still opens a skill checkpoint instead of trusting Scene → Bridge rhythm",
        ),
        (
            "before row 166 Writings canonical meta prelude capstone or row 66 workflow reunion opens on the capstone path",
            "before row 146 Writings canonical meta prelude capstone or row 66 workflow reunion opens on the capstone path",
        ),
        (
            "before row 166 Writings canonical meta prelude capstone opens",
            "before row 66 Writings canonical meta prelude opens on the capstone path",
        ),
        (
            "Confirm [row 144](preface.md#skill-navigation-row-144) or [Row 68 → Row 85 second-pass meta prelude reunion index (row 125)]",
            "Confirm [row 164](preface.md#skill-navigation-row-164) or [Row 68 → Row 145 second-pass meta prelude capstone reunion index (row 165)]",
        ),
        (
            "Row 145 does not replace row 68, row 65, row 144, row 125",
            "Row 165 does not replace row 68, row 65, row 164, row 145",
        ),
        (
            "[row 144](preface.md#skill-navigation-row-144) or [row 125](preface.md#skill-navigation-row-125)",
            "[row 164](preface.md#skill-navigation-row-164) or [row 145](preface.md#skill-navigation-row-145)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_145" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_145.*", "", out, flags=re.S)
    out = out.replace("__ROW165TITLE__", "Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone")
    out = out.replace("__ROW165_NAV__", "skill-navigation-row-165")
    out = out.replace("__ROW145_HINGE__", "[row 145](preface.md#skill-navigation-row-145)")
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
    if "### Row 165 skill checkpoint" in text:
        print("preface: row 165 already present")
        return
    m = re.search(
        r"(### Row 145 skill checkpoint.*?)(?=\n### Row 146 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 145 checkpoint missing")
    block = lift_145_to_165(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 165")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-165-closing-loop" in text:
        print("epilogue: row 165 loop already present")
        return
    block = lift_145_to_165(
        extract_between(
            text,
            "### Row 145 closing loop",
            "### Row 150 closing loop",
        )
    )
    needle = "### Row 164 closing loop"
    if needle not in text:
        needle = "### Row 145 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 165 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 165) |"
    if compass in text:
        print("prologue: row 165 compass already present")
    else:
        after = "| Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 164) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 164 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion (row 145) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 145 compass missing")
        new_line = lift_145_to_165(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-145"></span>'
    preview_dst = '| <span id="prologue-preview-row-165"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_145_to_165(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 165 closing stitch" not in text:
        stitch = (
            "**Row 165 closing stitch (Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion).** {#row-165-closing-stitch} "
            "When row 164 closed — book-loop meta prelude capstone verified, row 163 or row 144 recited on the capstone path, and the "
            "[prologue reopening anchor](#prologue-reopening-anchor) received the reader with `./scripts/test-fixtures.sh` green after verified orchestration meta prelude capstone — "
            "but **row 65 second-pass meta reunion still opens like standalone appendix coursework after the second-pass opening prelude chapter hinge on the capstone path** — "
            "the [preface row 165 When-to-pause opening sentence](../preface.md#skill-navigation-row-165) names the dual reunion before Writings canonical meta prelude reunion; "
            "read [preface row 165](../preface.md#skill-navigation-row-165), then the "
            "[Row 68 → Row 145 reunion index](../appendix/sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165), then "
            "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) before row 66 Writings canonical meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 164 closing stitch", stitch + "**Row 164 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 165 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165"
    if idx_key in text:
        print("sources: row 165 already present")
        return
    block = lift_145_to_165(
        extract_between(
            text,
            "## Row 68 → Row 125 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 145)",
            "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 165)",
        f"## Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 165) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 165 | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone "
        "(midpoint prelude gate ↔ book-loop meta prelude capstone ↔ row 65 meta) | "
        f"[Row 68 → Row 145 second-pass meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 165](../preface.md#skill-navigation-row-165) · "
        "[prologue row 165 preview](../prologue/00-many-scales.md#prologue-preview-row-165) · "
        "[prologue row 165 closing stitch](../prologue/00-many-scales.md#row-165-closing-stitch) · "
        "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) · "
        "[memory sheet row 165 baby picture](memory-sheet.md#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 65 second-pass meta reunion still feels disconnected from verified book-loop meta prelude capstone on the capstone path** — "
        "read row 68 + row 164 or row 145 gate + epilogue second-pass cross-links + row 65; "
        "[preface row 65](../preface.md#skill-navigation-row-65) |\n"
    )
    text = text.replace(
        "| 164 | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone",
        table_row + "| 164 | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164)",
        block + "## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164)",
    )
    extra = (
        f"[row 165](#{idx_key}) reunites **book-loop meta prelude capstone with the second-pass meta prelude capstone boundary** "
        "when row 164 closed book-loop meta prelude capstone at verified reopening anchor on the capstone path but epilogue second-pass cross-links and row 17 still read like separate courses after verified second-pass meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 164](#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164) reunites **orchestration meta prelude capstone with the book-loop meta prelude capstone boundary** "
            "when row 163 closed orchestration meta prelude capstone at verified H1→OUT on the capstone path but epilogue book-loop cross-links and row 12 still read like separate courses after verified book-loop meta prelude meta;"
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 165")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 165 already present")
        return
    baby = lift_145_to_165(
        extract_between(text, "### Row 145 baby picture", "### Row 146 baby picture")
    )
    text = text.replace("### Row 145 baby picture", baby + "### Row 145 baby picture", 1)
    mem_table = (
        "| 165 | Meta | Row 68 → Row 145 Row 68 → Row 65 second-pass meta prelude capstone reunion | "
        "[Row 68 → Row 145 second-pass meta prelude capstone reunion index](sources.md#row68-row145-second-pass-meta-prelude-capstone-reunion-index-row-165) · "
        "[preface row 165 skill checkpoint](../preface.md#skill-navigation-row-165) · "
        "[prologue row 165 preview](../prologue/00-many-scales.md#prologue-preview-row-165) · "
        "[prologue row 165 closing stitch](../prologue/00-many-scales.md#row-165-closing-stitch) · "
        "[epilogue row 165 closing loop](../epilogue/multiscale.md#row-165-closing-loop) | "
        "Row 68 closed but row 65 second-pass meta reunion feels disconnected from verified book-loop meta prelude capstone on the capstone path — "
        "read row 68 + row 164 or row 145 gate + epilogue second-pass cross-links + row 65; "
        "[row 165 baby picture](#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 164 | Meta | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion |",
        mem_table + "| 164 | Meta | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion |",
    )
    switch = (
        "When row 164 closed but novel second pass still lags on the capstone path, switch to [row 165](#row-165-baby-picture-row68-row145-second-pass-meta-prelude-capstone-reunion)."
    )
    if "When row 164 closed but novel second pass still lags on the capstone path, switch to [row 165]" not in text:
        text = text.replace(
            "When row 163 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 164](#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion).",
            "When row 163 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 164](#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 165")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
