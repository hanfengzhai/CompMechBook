#!/usr/bin/env python3
"""Add row 164 (Row 68 → Row 144 ↔ Row 64 book-loop meta prelude capstone on capstone path)."""
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


def lift_144_to_164(s: str) -> str:
    s = s.replace(
        "[row 144](preface.md#skill-navigation-row-144)",
        "__ROW144_HINGE__",
    )
    s = s.replace("skill-navigation-row-124", "__OPEN124_NAV__")
    s = s.replace("skill-navigation-row-143", "skill-navigation-row-163")
    s = s.replace("skill-navigation-row-144", "skill-navigation-row-164")
    s = s.replace("__OPEN124_NAV__", "skill-navigation-row-144")
    s = s.replace(
        "Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone",
        "__ROW164TITLE__",
    )
    s = s.replace(
        "[row 143](preface.md#skill-navigation-row-163)",
        "[row 163](preface.md#skill-navigation-row-163)",
    )
    s = s.replace(
        "[row 124](preface.md#skill-navigation-row-144)",
        "[row 144](preface.md#skill-navigation-row-144)",
    )
    p = [
        ("Row 165 closing loop", "__ROW165_LOOP__"),
        ("Row 144 closing loop", "Row 164 closing loop"),
        ("row-165-closing-loop", "__ROW165_LOOP_ANCHOR__"),
        ("row-144-closing-loop", "row-164-closing-loop"),
        ("Row 165 closing stitch", "__ROW165_STITCH__"),
        ("Row 144 closing stitch", "Row 164 closing stitch"),
        ("row-165-closing-stitch", "__ROW165_STITCH_ANCHOR__"),
        ("row-144-closing-stitch", "row-164-closing-stitch"),
        ("prologue-preview-row-165", "__ROW165_PREVIEW__"),
        ("prologue-preview-row-144", "prologue-preview-row-164"),
        ("Row 165 preview", "__ROW165_PREVIEW_TEXT__"),
        ("Row 144 preview", "Row 164 preview"),
        ("Row 165 skill checkpoint", "__ROW165_SKILL__"),
        ("Row 144 skill checkpoint", "Row 164 skill checkpoint"),
        ("skill-navigation-row-165", "__ROW165_SKILL_NAV__"),
        ("memory sheet row 165", "__ROW165_MEM__"),
        ("memory sheet row 144", "memory sheet row 164"),
        ("Row 165 baby picture", "__ROW165_BABY__"),
        ("Row 144 baby picture", "Row 164 baby picture"),
        ("Row 165 three-way audit", "__ROW165_AUDIT__"),
        ("Row 144 three-way audit", "Row 164 three-way audit"),
        (
            "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144",
            "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164",
        ),
        (
            "row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion",
            "row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion",
        ),
        ("[row 165]", "__ROW165_REF__"),
        ("[row 145]", "[row 165]"),
        ("row 145", "row 165"),
        ("Row 145", "Row 165"),
        ("__ROW165_REF__", "[row 165]"),
        ("[row 144]", "__ROW144_REF__"),
        ("[row 124]", "[row 144]"),
        ("row 124", "row 144"),
        ("Row 124", "Row 144"),
        ("__ROW144_REF__", "[row 144]"),
        ("row 143", "row 163"),
        ("Row 143", "Row 163"),
        ("[row 142]", "[row 162]"),
        ("row 142", "row 162"),
        ("Row 142", "Row 162"),
        ("(row 144)", "(row 164)"),
        ("__ROW165_LOOP__", "Row 165 closing loop"),
        ("__ROW165_LOOP_ANCHOR__", "row-165-closing-loop"),
        ("__ROW165_STITCH__", "Row 165 closing stitch"),
        ("__ROW165_STITCH_ANCHOR__", "row-165-closing-stitch"),
        ("__ROW165_PREVIEW__", "prologue-preview-row-165"),
        ("__ROW165_PREVIEW_TEXT__", "Row 165 preview"),
        ("__ROW165_SKILL__", "Row 165 skill checkpoint"),
        ("__ROW165_SKILL_NAV__", "skill-navigation-row-165"),
        ("__ROW165_MEM__", "memory sheet row 165"),
        ("__ROW165_BABY__", "Row 165 baby picture"),
        ("__ROW165_AUDIT__", "Row 165 three-way audit"),
        (
            "verified orchestration meta prelude capstone closure (row 143)",
            "verified orchestration meta prelude capstone closure (row 163)",
        ),
        (
            "Row 68 → Row 64 meta (row 144)",
            "Row 68 → Row 64 meta (row 164)",
        ),
        (
            "When row 144 is complete, proceed to [row 145](preface.md#skill-navigation-row-145) when row 68 closed but second-pass meta prelude still lags on the capstone path, "
            "to [row 125](preface.md#skill-navigation-row-125) when book-loop meta prelude capstone is clean but second-pass meta prelude still lags on the opening-hinge path, "
            "to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 second-pass meta prelude audit alone, "
            "to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 book-loop meta prelude audit on the opening-hinge path alone, "
            "to [row 143](preface.md#skill-navigation-row-143) when orchestration meta prelude capstone still lags after verified Handshake 4b meta prelude capstone on the capstone path, "
            "to [row 84](preface.md#skill-navigation-row-84) for the Row 68 ↔ Row 64 opening prelude audit alone, "
            "to [row 64](preface.md#skill-navigation-row-64) when only book-loop meta stalls, "
            "or extend prose only under `writings/` then sync.",
            "When row 164 is complete, proceed to [row 165](preface.md#skill-navigation-row-165) when row 68 closed but second-pass meta prelude still lags on the capstone path, "
            "to [row 145](preface.md#skill-navigation-row-145) when book-loop meta prelude capstone is clean but second-pass meta prelude still lags on the opening-hinge path, "
            "to [row 125](preface.md#skill-navigation-row-125) for the Row 68 ↔ Row 65 second-pass meta prelude audit alone, "
            "to [row 124](preface.md#skill-navigation-row-124) for the Row 68 ↔ Row 64 book-loop meta prelude audit on the opening-hinge path alone, "
            "to [row 163](preface.md#skill-navigation-row-163) when orchestration meta prelude capstone still lags after verified Handshake 4b meta prelude capstone on the capstone path, "
            "to [row 84](preface.md#skill-navigation-row-84) for the Row 68 ↔ Row 64 opening prelude audit alone, "
            "to [row 64](preface.md#skill-navigation-row-64) when only book-loop meta stalls, "
            "or extend prose only under `writings/` then sync.",
        ),
        (
            "When row 64 feels like epilogue homework after row 143 alone on the capstone path",
            "When row 64 feels like epilogue homework after row 163 alone on the capstone path",
        ),
        ("Recite [preface row 143]", "Recite [preface row 163]"),
        (
            "Proceed to [row 145](#row-145-closing-loop) when row 68 closed but second-pass meta prelude still lags after row 144 on the capstone path, "
            "to [row 125](#row-125-closing-loop) when row 68 closed but second-pass meta still feels disconnected after row 124 on the opening-hinge path",
            "Proceed to [row 165](#row-165-closing-loop) when row 68 closed but second-pass meta prelude still lags after row 164 on the capstone path, "
            "to [row 145](#row-145-closing-loop) when row 68 closed but second-pass meta still feels disconnected after row 144 on the opening-hinge path",
        ),
        (
            "when opening [row 145](preface.md#skill-navigation-row-145) before row 65 closes on the capstone path",
            "when opening [row 165](preface.md#skill-navigation-row-165) before row 65 closes on the capstone path",
        ),
        (
            "when `multiscale_export.yaml` exists on the capstone path after row 143 but the next terminal still opens with copper decks copied blindly",
            "when `multiscale_export.yaml` exists on the capstone path after row 163 but the next terminal still opens with copper decks copied blindly",
        ),
        (
            "when row 143 closed but row 64 book-loop meta still feels like epilogue homework",
            "when row 163 closed but row 64 book-loop meta still feels like epilogue homework",
        ),
        (
            "when row 143 and row 64 both verify individually",
            "when row 163 and row 64 both verify individually",
        ),
        (
            "rear-view mirror of row 143's orchestration meta → H1→OUT",
            "rear-view mirror of row 163's orchestration meta → H1→OUT",
        ),
        (
            "read row 68 gate + row 143 or row 124 orchestration meta prelude capstone / book-loop meta prelude gate + epilogue book-loop cross-links + row 64 meta aloud when orchestration verifies on the capstone path after orchestration meta prelude capstone but the next terminal opens with copper decks copied blindly without reopening anchor rung audit",
            "read row 68 gate + row 163 or row 144 orchestration meta prelude capstone / book-loop meta prelude gate + epilogue book-loop cross-links + row 64 meta aloud when orchestration verifies on the capstone path after orchestration meta prelude capstone but the next terminal opens with copper decks copied blindly without reopening anchor rung audit",
        ),
        (
            "before row 145 second-pass meta prelude capstone or row 65 workflow reunion opens on the capstone path",
            "before row 165 second-pass meta prelude capstone or row 65 workflow reunion opens on the capstone path",
        ),
        (
            "before row 145 second-pass meta prelude capstone opens",
            "before row 65 second-pass meta prelude opens on the capstone path",
        ),
        (
            "Confirm [row 143](preface.md#skill-navigation-row-143) or [Row 68 → Row 124 book-loop meta prelude capstone reunion index (row 144)]",
            "Confirm [row 163](preface.md#skill-navigation-row-163) or [Row 68 → Row 144 book-loop meta prelude capstone reunion index (row 164)]",
        ),
        (
            "Row 144 does not replace row 68, row 64, row 143, row 124, row 84, row 63, or row 44",
            "Row 164 does not replace row 68, row 64, row 163, row 144, row 84, row 63, or row 44",
        ),
        (
            "[Row 68 → Row 124 book-loop meta prelude capstone reunion index (row 144)]",
            "[Row 68 → Row 144 book-loop meta prelude capstone reunion index (row 164)]",
        ),
        (
            "Row 68 → Row 124 book-loop meta prelude capstone reunion index (row 144)",
            "Row 68 → Row 144 book-loop meta prelude capstone reunion index (row 164)",
        ),
        (
            "Row 68 → Row 124 reunion index",
            "Row 68 → Row 144 reunion index",
        ),
        (
            "when row 143 closed — orchestration meta prelude capstone verified, row 142 or row 123 recited on the capstone path",
            "when row 163 closed — orchestration meta prelude capstone verified, row 162 or row 143 recited on the capstone path",
        ),
    ]
    out = tx(s, p)
    out = out.replace("__ROW164TITLE__", "Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone")
    out = out.replace("__ROW144_HINGE__", "[row 144](preface.md#skill-navigation-row-144)")
    out = out.replace("Row 164 does not replace row 68, row 64, row 163, row 144", "Row 164 does not replace row 68, row 64, row 163, row 144")
    out = out.replace(
        "Row 144 does not replace row 68, row 64, row 163, row 144",
        "Row 164 does not replace row 68, row 64, row 163, row 144, row 84, row 63, or row 44",
    )
    out = out.replace("Row 144 closes the **book-loop", "Row 164 closes the **book-loop")
    out = out.replace("Do not conflate row 144 (row 68 ↔ row 64 reunion on the capstone path)", "Do not conflate row 164 (row 68 ↔ row 64 reunion on the capstone path)")
    out = out.replace("; row 144 names **why that reunion", "; row 164 names **why that reunion")
    out = out.replace("verified orchestration meta prelude capstone (row 163)", "verified orchestration meta prelude capstone (row 163)")
    out = out.replace("after row 144 on the capstone path", "after row 164 on the capstone path")
    out = out.replace(
        "When row 144 is complete, proceed to [row 165]",
        "When row 164 is complete, proceed to [row 165]",
    )
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
    if "### Row 164 skill checkpoint" in text:
        print("preface: row 164 already present")
        return
    m = re.search(
        r"(### Row 144 skill checkpoint.*?)(?=\n### Row 145 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 144 checkpoint missing")
    block = lift_144_to_164(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 164")


def fix_preface_row164() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m144 = re.search(
        r"(### Row 144 skill checkpoint.*?)(?=\n### Row 145 skill checkpoint)",
        text,
        re.S,
    )
    if not m144:
        raise SystemExit("row 144 preface checkpoint missing")
    block164 = lift_144_to_164(m144.group(1))
    start = text.find("### Row 164 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block164 + text[end:]
        path.write_text(text)
        print("preface: repaired row 164")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-164-closing-loop" in text:
        print("epilogue: row 164 loop already present")
        return
    block = lift_144_to_164(
        extract_between(
            text,
            "### Row 144 closing loop",
            "### Row 145 closing loop",
        )
    )
    needle = "### Row 163 closing loop"
    if needle not in text:
        needle = "### Row 144 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 164 loop")


def fix_epilogue_row164() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-164-closing-loop" not in text:
        return
    block144 = extract_between(
        text, "### Row 144 closing loop", "### Row 145 closing loop"
    )
    block164 = lift_144_to_164(block144)
    start = text.find("### Row 164 closing loop")
    end = text.find("\n### Row 163 closing loop", start)
    if end < 0:
        end = text.find("\n### Row 144 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block164 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 164 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 164) |"
    if compass in text:
        print("prologue: row 164 compass already present")
    else:
        after = "| Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 163) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 163 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 144) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 144 compass missing")
        new_line = lift_144_to_164(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-144"></span>'
    preview_dst = '| <span id="prologue-preview-row-164"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_144_to_164(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 164 closing stitch" not in text:
        stitch = (
            "**Row 164 closing stitch (Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-164-closing-stitch} "
            "When row 163 closed — orchestration meta prelude capstone verified, row 162 or row 143 recited on the capstone path, and "
            "[`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) archived `multiscale_export.yaml` with H1→H2→H3→H4a→H4b→OUT after verified Handshake 4b meta prelude capstone — "
            "but **row 64 book-loop meta reunion still opens like standalone epilogue coursework after the book-loop opening prelude chapter hinge on the capstone path** — "
            "the [preface row 164 When-to-pause opening sentence](../preface.md#skill-navigation-row-164) names the dual reunion before second-pass meta prelude reunion; "
            "read [preface row 164](../preface.md#skill-navigation-row-164), then the "
            "[Row 68 → Row 144 reunion index](../appendix/sources.md#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164), then "
            "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) before row 65 second-pass meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 163 closing stitch", stitch + "**Row 163 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 164 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164"
    if idx_key in text:
        print("sources: row 164 already present")
        return
    block = lift_144_to_164(
        extract_between(
            text,
            "## Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 144)",
            "## Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 124)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164)",
        f"## Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 164) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 164 | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone "
        "(midpoint prelude gate ↔ orchestration meta prelude capstone ↔ row 64 meta) | "
        f"[Row 68 → Row 144 book-loop meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 164](../preface.md#skill-navigation-row-164) · "
        "[prologue row 164 preview](../prologue/00-many-scales.md#prologue-preview-row-164) · "
        "[prologue row 164 closing stitch](../prologue/00-many-scales.md#row-164-closing-stitch) · "
        "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) · "
        "[memory sheet row 164 baby picture](memory-sheet.md#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 64 book-loop meta reunion still feels disconnected from verified orchestration meta prelude capstone on the capstone path** — "
        "read row 68 + row 163 or row 144 gate + epilogue book-loop cross-links + row 64; "
        "[preface row 64](../preface.md#skill-navigation-row-64) |\n"
    )
    text = text.replace(
        "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone",
        table_row + "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163)",
        block + "## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163)",
    )
    extra = (
        f"[row 164](#{idx_key}) reunites **orchestration meta prelude capstone with the book-loop meta prelude capstone boundary** "
        "when row 163 closed orchestration meta prelude capstone at verified H1→OUT on the capstone path but epilogue book-loop cross-links and row 12 still read like separate courses after verified book-loop meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 163](#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163) reunites **Handshake 4b meta prelude capstone with the orchestration meta prelude capstone boundary** "
            "when row 162 closed Handshake 4b meta prelude capstone at verified notch-root stress on the capstone path but epilogue orchestration cross-links and row 16 still read like separate courses after verified orchestration meta prelude meta;"
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 164")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 164 already present")
        return
    baby = lift_144_to_164(
        extract_between(text, "### Row 144 baby picture", "### Row 145 baby picture")
    )
    text = text.replace("### Row 144 baby picture", baby + "### Row 144 baby picture", 1)
    mem_table = (
        "| 164 | Meta | Row 68 → Row 144 Row 68 → Row 64 book-loop meta prelude capstone reunion | "
        "[Row 68 → Row 144 book-loop meta prelude capstone reunion index](sources.md#row68-row144-book-loop-meta-prelude-capstone-reunion-index-row-164) · "
        "[preface row 164 skill checkpoint](../preface.md#skill-navigation-row-164) · "
        "[prologue row 164 preview](../prologue/00-many-scales.md#prologue-preview-row-164) · "
        "[prologue row 164 closing stitch](../prologue/00-many-scales.md#row-164-closing-stitch) · "
        "[epilogue row 164 closing loop](../epilogue/multiscale.md#row-164-closing-loop) | "
        "Row 68 closed but row 64 book-loop meta reunion feels disconnected from verified orchestration meta prelude capstone on the capstone path — "
        "read row 68 + row 163 or row 144 gate + epilogue book-loop cross-links + row 64; "
        "[row 164 baby picture](#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 163 | Meta | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion |",
        mem_table + "| 163 | Meta | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion |",
    )
    switch = (
        "When row 163 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 164](#row-164-baby-picture-row68-row144-book-loop-meta-prelude-capstone-reunion)."
    )
    if "When row 163 closed but book-loop meta prelude reunion still lags" not in text:
        text = text.replace(
            "When row 162 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 163](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion).",
            "When row 162 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 163](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 164")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
