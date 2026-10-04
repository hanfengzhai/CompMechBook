#!/usr/bin/env python3
"""Add row 163 (Row 68 → Row 143 ↔ Row 63 orchestration meta prelude capstone on capstone path)."""
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


def lift_143_to_163(s: str) -> str:
    s = s.replace(
        "[row 143](preface.md#skill-navigation-row-143)",
        "__ROW143_HINGE__",
    )
    s = s.replace("skill-navigation-row-143", "__ROW163_NAV__")
    s = s.replace(
        "Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone",
        "__ROW163TITLE__",
    )
    p = [
        ("Row 144 closing loop", "__ROW144_LOOP__"),
        ("Row 143 closing loop", "Row 163 closing loop"),
        ("row-144-closing-loop", "__ROW144_LOOP_ANCHOR__"),
        ("row-143-closing-loop", "row-163-closing-loop"),
        ("Row 144 closing stitch", "__ROW144_STITCH__"),
        ("Row 143 closing stitch", "Row 163 closing stitch"),
        ("row-144-closing-stitch", "__ROW144_STITCH_ANCHOR__"),
        ("row-143-closing-stitch", "row-163-closing-stitch"),
        ("prologue-preview-row-144", "__ROW144_PREVIEW__"),
        ("prologue-preview-row-143", "prologue-preview-row-163"),
        ("Row 144 preview", "__ROW144_PREVIEW_TEXT__"),
        ("Row 143 preview", "Row 163 preview"),
        ("Row 144 skill checkpoint", "__ROW144_SKILL__"),
        ("Row 143 skill checkpoint", "Row 163 skill checkpoint"),
        ("skill-navigation-row-144", "__ROW144_SKILL_NAV__"),
        ("skill-navigation-row-142", "skill-navigation-row-162"),
        ("skill-navigation-row-123", "skill-navigation-row-143"),
        ("memory sheet row 144", "__ROW144_MEM__"),
        ("memory sheet row 143", "memory sheet row 163"),
        ("Row 144 baby picture", "__ROW144_BABY__"),
        ("Row 143 baby picture", "Row 163 baby picture"),
        ("Row 144 three-way audit", "__ROW144_AUDIT__"),
        ("Row 143 three-way audit", "Row 163 three-way audit"),
        (
            "row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143",
            "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163",
        ),
        (
            "row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion",
            "row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion",
        ),
        ("[row 144]", "__ROW144_REF__"),
        ("[row 124]", "[row 144]"),
        ("row 124", "row 144"),
        ("Row 124", "Row 144"),
        ("__ROW144_REF__", "[row 144]"),
        ("[row 143]", "__ROW143_REF__"),
        ("[row 123]", "[row 143]"),
        ("row 123", "row 143"),
        ("Row 123", "Row 143"),
        ("__ROW143_REF__", "[row 143]"),
        ("[row 142]", "[row 162]"),
        ("row 142", "row 162"),
        ("Row 142", "Row 162"),
        ("(row 143)", "(row 163)"),
        ("__ROW144_LOOP__", "Row 144 closing loop"),
        ("__ROW144_LOOP_ANCHOR__", "row-144-closing-loop"),
        ("__ROW144_STITCH__", "Row 144 closing stitch"),
        ("__ROW144_STITCH_ANCHOR__", "row-144-closing-stitch"),
        ("__ROW144_PREVIEW__", "prologue-preview-row-144"),
        ("__ROW144_PREVIEW_TEXT__", "Row 144 preview"),
        ("__ROW144_SKILL__", "Row 144 skill checkpoint"),
        ("__ROW144_SKILL_NAV__", "skill-navigation-row-144"),
        ("__ROW144_MEM__", "memory sheet row 144"),
        ("__ROW144_BABY__", "Row 144 baby picture"),
        ("__ROW144_AUDIT__", "Row 144 three-way audit"),
        (
            "verified Handshake 4b meta prelude capstone closure (row 142)",
            "verified Handshake 4b meta prelude capstone closure (row 162)",
        ),
        (
            "Row 68 → Row 63 meta (row 143)",
            "Row 68 → Row 63 meta (row 163)",
        ),
        (
            "When row 143 is complete, proceed to [row 144](preface.md#skill-navigation-row-144) when row 68 closed but book-loop meta prelude still lags on the capstone path, "
            "to [row 124](preface.md#skill-navigation-row-124) when orchestration meta prelude capstone is clean but book-loop meta prelude still lags on the opening-hinge path, "
            "to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 book-loop meta prelude audit alone, "
            "to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit on the opening-hinge path alone, "
            "to [row 142](preface.md#skill-navigation-row-142) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the capstone path, "
            "to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, "
            "to [row 63](preface.md#skill-navigation-row-63) when only orchestration meta stalls, "
            "or extend prose only under `writings/` then sync.",
            "When row 163 is complete, proceed to [row 164](preface.md#skill-navigation-row-164) when row 68 closed but book-loop meta prelude still lags on the capstone path, "
            "to [row 144](preface.md#skill-navigation-row-144) when orchestration meta prelude capstone is clean but book-loop meta prelude still lags on the opening-hinge path, "
            "to [row 124](preface.md#skill-navigation-row-124) for the Row 68 ↔ Row 64 book-loop meta prelude audit alone, "
            "to [row 123](preface.md#skill-navigation-row-123) for the Row 68 ↔ Row 63 orchestration meta prelude audit on the opening-hinge path alone, "
            "to [row 162](preface.md#skill-navigation-row-162) when Handshake 4b meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the capstone path, "
            "to [row 83](preface.md#skill-navigation-row-83) for the Row 68 ↔ Row 63 opening prelude audit alone, "
            "to [row 63](preface.md#skill-navigation-row-63) when only orchestration meta stalls, "
            "or extend prose only under `writings/` then sync.",
        ),
        (
            "When row 63 feels like epilogue homework after row 142 alone on the capstone path",
            "When row 63 feels like epilogue homework after row 162 alone on the capstone path",
        ),
        ("Recite [preface row 142]", "Recite [preface row 162]"),
        (
            "Proceed to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta prelude still lags after row 143 on the capstone path, "
            "to [row 124](#row-124-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 123 on the opening-hinge path",
            "Proceed to [row 164](#row-164-closing-loop) when row 68 closed but book-loop meta prelude still lags after row 163 on the capstone path, "
            "to [row 144](#row-144-closing-loop) when row 68 closed but book-loop meta still feels disconnected after row 143 on the opening-hinge path",
        ),
        (
            "when opening [row 144](preface.md#skill-navigation-row-144) before row 64 closes on the capstone path",
            "when opening [row 164](preface.md#skill-navigation-row-164) before row 64 closes on the capstone path",
        ),
        (
            "when individual export yamls are verified on the capstone path after row 142 but no orchestrated pedigree links them",
            "when individual export yamls are verified on the capstone path after row 162 but no orchestrated pedigree links them",
        ),
        (
            "when row 142 closed but row 63 orchestration meta still feels like epilogue homework",
            "when row 162 closed but row 63 orchestration meta still feels like epilogue homework",
        ),
        (
            "when row 142 and row 63 both verify individually",
            "when row 162 and row 63 both verify individually",
        ),
        (
            "rear-view mirror of row 142's Handshake 4b meta → notch",
            "rear-view mirror of row 162's Handshake 4b meta → notch",
        ),
        (
            "read row 68 gate + row 142 or row 123 Handshake 4b meta prelude capstone / orchestration meta prelude gate + epilogue orchestration cross-links + row 63 meta aloud when Handshakes 1–4b verify individually on the capstone path after Handshake 4b meta prelude capstone but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml`",
            "read row 68 gate + row 162 or row 143 Handshake 4b meta prelude capstone / orchestration meta prelude gate + epilogue orchestration cross-links + row 63 meta aloud when Handshakes 1–4b verify individually on the capstone path after Handshake 4b meta prelude capstone but Act V notch and Act VI foundation still feel like separate afternoons without orchestrated `multiscale_export.yaml`",
        ),
        (
            "before row 144 book-loop meta prelude capstone or row 64 workflow reunion opens on the capstone path",
            "before row 164 book-loop meta prelude capstone or row 64 workflow reunion opens on the capstone path",
        ),
        (
            "before row 64 book-loop meta prelude opens on the capstone path",
            "before row 64 book-loop meta prelude opens on the capstone path",
        ),
        (
            "Row 143 does not replace row 68, row 63, row 142, row 123, row 83, row 62, or row 43",
            "Row 163 does not replace row 68, row 63, row 162, row 143, row 83, row 62, or row 43",
        ),
        (
            "[Row 68 → Row 123 orchestration meta prelude capstone reunion index (row 143)]",
            "[Row 68 → Row 143 orchestration meta prelude capstone reunion index (row 163)]",
        ),
        (
            "Row 68 → Row 123 orchestration meta prelude capstone reunion index (row 143)",
            "Row 68 → Row 143 orchestration meta prelude capstone reunion index (row 163)",
        ),
        (
            "Row 68 → Row 123 reunion index",
            "Row 68 → Row 143 reunion index",
        ),
        (
            "when row 142 closed — Handshake 4b meta prelude capstone verified, row 141 or row 122 recited on the capstone path",
            "when row 162 closed — Handshake 4b meta prelude capstone verified, row 161 or row 142 recited on the capstone path",
        ),
    ]
    out = tx(s, p)
    out = out.replace("__ROW163TITLE__", "Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone")
    out = out.replace("__ROW163_NAV__", "skill-navigation-row-163")
    out = out.replace("__ROW143_HINGE__", "[row 143](preface.md#skill-navigation-row-143)")
    return out


def fix_row_162_tail(preface: str) -> str:
    trimmed = (
        "When row 162 is complete, proceed to [row 163](preface.md#skill-navigation-row-163) when row 68 closed but orchestration meta prelude still lags on the capstone path, "
        "to [row 143](preface.md#skill-navigation-row-143) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, "
        "to [row 123](preface.md#skill-navigation-row-123) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, "
        "to [row 122](preface.md#skill-navigation-row-122) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, "
        "to [row 161](preface.md#skill-navigation-row-161) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the capstone path, "
        "to [row 62](preface.md#skill-navigation-row-62) when only Handshake 4b meta stalls, "
        "or extend prose only under `writings/` then sync."
    )
    preface = re.sub(
        r"When row 142 is complete, proceed to \[row 143\].*?or extend prose only under `writings/` then sync\.",
        trimmed,
        preface,
        count=1,
        flags=re.S,
    )
    preface = preface.replace(
        "when opening [row 143](preface.md#skill-navigation-row-143) before row 63 closes on the capstone path",
        "when opening [row 163](preface.md#skill-navigation-row-163) before row 63 closes on the capstone path",
    )
    return preface


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
    if "### Row 163 skill checkpoint" in text:
        print("preface: row 163 already present")
        return
    m = re.search(
        r"(### Row 143 skill checkpoint.*?)(?=\n### Row 144 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 143 checkpoint missing")
    block = lift_143_to_163(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 163")


def fix_preface_row163() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m143 = re.search(
        r"(### Row 143 skill checkpoint.*?)(?=\n### Row 144 skill checkpoint)",
        text,
        re.S,
    )
    if not m143:
        raise SystemExit("row 143 preface checkpoint missing")
    block163 = lift_143_to_163(m143.group(1))
    start = text.find("### Row 163 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block163 + text[end:]
        path.write_text(text)
        print("preface: repaired row 163")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-163-closing-loop" in text:
        print("epilogue: row 163 loop already present")
        return
    block = lift_143_to_163(
        extract_between(
            text,
            "### Row 143 closing loop",
            "### Row 144 closing loop",
        )
    )
    needle = "### Row 162 closing loop"
    if needle not in text:
        needle = "### Row 143 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 163 loop")


def fix_epilogue_row163() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-163-closing-loop" not in text:
        return
    block143 = extract_between(
        text, "### Row 143 closing loop", "### Row 144 closing loop"
    )
    block163 = lift_143_to_163(block143)
    start = text.find("### Row 163 closing loop")
    end = text.find("\n### Row 162 closing loop", start)
    if end < 0:
        end = text.find("\n### Row 143 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block163 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 163 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 163) |"
    if compass in text:
        print("prologue: row 163 compass already present")
    else:
        after = "| Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 162) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 162 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 143) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 143 compass missing")
        new_line = lift_143_to_163(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-143"></span>'
    preview_dst = '| <span id="prologue-preview-row-163"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_143_to_163(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 163 closing stitch" not in text:
        stitch = (
            "**Row 163 closing stitch (Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion).** {#row-163-closing-stitch} "
            "When row 162 closed — Handshake 4b meta prelude capstone verified, row 161 or row 142 recited on the capstone path, and "
            "[`parse_fe2.sh`](../../scripts/parse_fe2.sh) archived `fe2_export.yaml` with enrichment when uplift exceeds 10% after verified Handshake 4b meta prelude capstone — "
            "but **row 63 orchestration meta reunion still opens like standalone epilogue coursework after the orchestration opening prelude chapter hinge on the capstone path** — "
            "the [preface row 163 When-to-pause opening sentence](../preface.md#skill-navigation-row-163) names the dual reunion before book-loop meta prelude reunion; "
            "read [preface row 163](../preface.md#skill-navigation-row-163), then the "
            "[Row 68 → Row 143 reunion index](../appendix/sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163), then "
            "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) before row 64 book-loop meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 162 closing stitch", stitch + "**Row 162 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 163 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163"
    if idx_key in text:
        print("sources: row 163 already present")
        return
    block = lift_143_to_163(
        extract_between(
            text,
            "## Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 143)",
            "## Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 144)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163)",
        f"## Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 163) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 163 | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 4b meta prelude capstone ↔ row 63 meta) | "
        f"[Row 68 → Row 143 orchestration meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 163](../preface.md#skill-navigation-row-163) · "
        "[prologue row 163 preview](../prologue/00-many-scales.md#prologue-preview-row-163) · "
        "[prologue row 163 closing stitch](../prologue/00-many-scales.md#row-163-closing-stitch) · "
        "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) · "
        "[memory sheet row 163 baby picture](memory-sheet.md#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 63 orchestration meta reunion still feels disconnected from verified Handshake 4b meta prelude capstone on the capstone path** — "
        "read row 68 + row 162 or row 143 gate + epilogue orchestration cross-links + row 63; "
        "[preface row 63](../preface.md#skill-navigation-row-63) |\n"
    )
    text = text.replace(
        "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        table_row + "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162)",
        block + "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162)",
    )
    extra = (
        f"[row 163](#{idx_key}) reunites **Handshake 4b meta prelude capstone with the orchestration meta prelude capstone boundary** "
        "when row 162 closed Handshake 4b meta prelude capstone at verified notch-root stress on the capstone path but epilogue orchestration cross-links and row 16 still read like separate courses after verified orchestration meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 162](#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) reunites **Handshake 4a meta prelude capstone with the Handshake 4b meta prelude capstone boundary** "
            "when row 161 closed Handshake 4a meta prelude capstone at verified bulk hardening on the capstone path but epilogue FE² cross-links and Part VII Step 4 still read like separate courses after verified Handshake 4b meta prelude meta;"
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 163")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 163 already present")
        return
    baby = lift_143_to_163(
        extract_between(text, "### Row 143 baby picture", "### Row 144 baby picture")
    )
    text = text.replace("### Row 143 baby picture", baby + "### Row 143 baby picture", 1)
    mem_table = (
        "| 163 | Meta | Row 68 → Row 143 Row 68 → Row 63 orchestration meta prelude capstone reunion | "
        "[Row 68 → Row 143 orchestration meta prelude capstone reunion index](sources.md#row68-row143-orchestration-meta-prelude-capstone-reunion-index-row-163) · "
        "[preface row 163 skill checkpoint](../preface.md#skill-navigation-row-163) · "
        "[prologue row 163 preview](../prologue/00-many-scales.md#prologue-preview-row-163) · "
        "[prologue row 163 closing stitch](../prologue/00-many-scales.md#row-163-closing-stitch) · "
        "[epilogue row 163 closing loop](../epilogue/multiscale.md#row-163-closing-loop) | "
        "Row 68 closed but row 63 orchestration meta reunion feels disconnected from verified Handshake 4b meta prelude capstone on the capstone path — "
        "read row 68 + row 162 or row 143 gate + epilogue orchestration cross-links + row 63; "
        "[row 163 baby picture](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 162 | Meta | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion |",
        mem_table + "| 162 | Meta | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion |",
    )
    switch = (
        "When row 162 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 163](#row-163-baby-picture-row68-row143-orchestration-meta-prelude-capstone-reunion)."
    )
    if "When row 162 closed but orchestration meta prelude reunion still lags" not in text:
        text = text.replace(
            "When row 161 closed but Handshake 4b meta prelude capstone reunion still lags on the capstone path, switch to [row 162](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion).",
            "When row 161 closed but Handshake 4b meta prelude capstone reunion still lags on the capstone path, switch to [row 162](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 163")


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(fix_row_162_tail(preface_path.read_text()))
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row163()
    insert_epilogue_loop()
    fix_epilogue_row163()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
