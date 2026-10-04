#!/usr/bin/env python3
"""Add row 162 (Handshake 4b meta prelude capstone reunion) from row 142 baseline."""
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


def lift_142_to_162(s: str) -> str:
    s = s.replace(
        "Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        "__ROW162TITLE__",
    )
    s = s.replace("[row 143]", "__ROW143__")
    s = s.replace("[row 142](preface.md#skill-navigation-row-142)", "__ROW142HINGE__")
    s = s.replace(
        "[row 142](prologue/00-many-scales.md#prologue-preview-row-142)",
        "__ROW142PREVIEW__",
    )
    p = [
        ("Row 143 closing loop", "__ROW143_LOOP__"),
        ("skill-navigation-row-123", "skill-navigation-row-143"),
        ("skill-navigation-row-122", "skill-navigation-row-142"),
        ("skill-navigation-row-142", "skill-navigation-row-162"),
        ("Row 142 closing loop", "Row 162 closing loop"),
        ("row-142-closing-loop", "row-162-closing-loop"),
        ("Row 142 closing stitch", "Row 162 closing stitch"),
        ("row-142-closing-stitch", "row-162-closing-stitch"),
        ("prologue-preview-row-142", "prologue-preview-row-162"),
        ("Row 142 preview", "Row 162 preview"),
        ("Row 142 skill checkpoint", "Row 162 skill checkpoint"),
        ("memory sheet row 142", "memory sheet row 162"),
        ("Row 142 baby picture", "Row 162 baby picture"),
        ("Row 142 three-way audit", "Row 162 three-way audit"),
        ("Row 142 does not replace", "Row 162 does not replace"),
        (
            "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142",
            "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162",
        ),
        (
            "row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion",
            "row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("[row 123]", "__ROW123_REF__"),
        ("[row 103]", "[row 123]"),
        ("row 103", "row 123"),
        ("Row 103", "Row 123"),
        ("__ROW123_REF__", "[row 123]"),
        ("[row 102]", "[row 122]"),
        ("row 102", "row 122"),
        ("Row 102", "Row 122"),
        ("(row 142)", "(row 162)"),
        ("__ROW143_LOOP__", "Row 143 closing loop"),
        ("row 121", "row 141"),
        ("Row 121", "Row 141"),
        ("preface.md#skill-navigation-row-121)", "preface.md#skill-navigation-row-141)"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        (
            "verified Handshake 4a meta prelude capstone closure (row 141)",
            "verified Handshake 4a meta prelude capstone closure (row 161)",
        ),
        (
            "Row 68 → Row 62 meta (row 142)",
            "Row 68 → Row 62 meta (row 162)",
        ),
        (
            "when opening [row 143](preface.md#skill-navigation-row-143) before row 63 closes on the capstone path",
            "when opening [row 163](preface.md#skill-navigation-row-163) before row 63 closes on the capstone path",
        ),
        (
            "When row 142 is complete, proceed to [row 143]",
            "When row 162 is complete, proceed to [row 163]",
        ),
        (
            "row 142 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 141)",
            "row 162 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 161)",
        ),
        (
            "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 142 on the capstone path, to [row 123](#row-123-closing-loop) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path",
            "Proceed to [row 163](#row-162-closing-loop) when row 68 closed but orchestration meta prelude capstone still lags after row 162 on the capstone path, "
            "to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 142 on the opening-hinge path, "
            "to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 122 on the opening-hinge path",
        ),
        (
            "when `fe2_notch_comparison.dat` exists after row 141 but crystal plasticity is still trusted at the notch root",
            "when `fe2_notch_comparison.dat` exists on the capstone path after row 161 but crystal plasticity is still trusted at the notch root",
        ),
        (
            "when row 141 closed but row 62",
            "when row 161 closed but row 62",
        ),
        (
            "When row 141 closed — Handshake 4a meta prelude capstone verified, row 140 or row 121 recited on the capstone path",
            "When row 161 closed — Handshake 4a meta prelude capstone verified, row 160 or row 141 recited on the capstone path",
        ),
        (
            "before row 143 orchestration meta prelude capstone or row 63 workflow reunion opens on the capstone path",
            "before row 163 orchestration meta prelude capstone or row 63 workflow reunion opens on the capstone path",
        ),
        (
            "when row 141 and row 62 both verify individually",
            "when row 161 and row 62 both verify individually",
        ),
        (
            "when row 141 closed Handshake 4a meta prelude capstone and row 68 closed the midpoint prelude but **row 62 Handshake 4b meta still opens",
            "when row 161 closed Handshake 4a meta prelude capstone and row 68 closed the midpoint prelude but **row 62 Handshake 4b meta still opens",
        ),
        (
            "rear-view mirror of row 141's Handshake 4a meta → bulk",
            "rear-view mirror of row 161's Handshake 4a meta → bulk",
        ),
        (
            "read row 68 gate + row 141 or row 122 Handshake 4a meta prelude capstone / Handshake 4b meta prelude gate + epilogue FE² cross-links + row 62 meta aloud when bulk hardening matches flow stress on the capstone path after Handshake 4a meta prelude capstone but the notch root under-predicts peak stress without FE² audit",
            "read row 68 gate + row 161 or row 142 Handshake 4a meta prelude capstone / Handshake 4b meta prelude gate + epilogue FE² cross-links + row 62 meta aloud when bulk hardening matches flow stress on the capstone path after Handshake 4a meta prelude capstone but the notch root under-predicts peak stress without FE² audit",
        ),
        (
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path) with row 122 (opening-hinge prelude stitch alone)",
            "Do not conflate row 162 (row 68 ↔ row 62 reunion on the capstone path) with row 142 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 122 names **Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude reunion**; row 142 names",
            "row 142 names **Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude reunion**; row 162 names",
        ),
        (
            "When row 142 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta prelude still lags on the capstone path, to [row 123](preface.md#skill-navigation-row-123) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, to [row 141](preface.md#skill-navigation-row-141) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta capstone on the capstone path, to [row 82](preface.md#skill-navigation-row-82) for the Row 68 ↔ Row 62 opening prelude audit alone, to [row 62](preface.md#skill-navigation-row-62) for the Row 61 ↔ Row 42 meta audit alone, to [row 42](preface.md#skill-navigation-row-42) for the full VII.3 Step 4 → Handshake 4b meta audit, or extend prose only under `writings/` then sync.",
            "When row 162 is complete, proceed to [row 163](preface.md#skill-navigation-row-163) when row 68 closed but orchestration meta prelude still lags on the capstone path, to [row 143](preface.md#skill-navigation-row-143) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, to [row 161](preface.md#skill-navigation-row-161) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta prelude capstone on the capstone path, to [row 62](preface.md#skill-navigation-row-62) when only Handshake 4b meta stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "when opening [row 142](preface.md#skill-navigation-row-142) before row 62 closes on the capstone path",
            "when opening [row 162](preface.md#skill-navigation-row-162) before row 62 closes on the capstone path",
        ),
        (
            "[row 141](preface.md#skill-navigation-row-121) or [row 142](preface.md#skill-navigation-row-102) closed the Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
            "[row 161](preface.md#skill-navigation-row-161) or [row 142](preface.md#skill-navigation-row-142) closed the Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
        ),
        (
            "Row 68 → Row 122 Handshake 4b meta prelude capstone reunion index (row 142)",
            "Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index (row 162)",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW142HINGE__", "[row 142](preface.md#skill-navigation-row-142)")
    s = s.replace(
        "__ROW142PREVIEW__",
        "[row 142](prologue/00-many-scales.md#prologue-preview-row-142)",
    )
    s = s.replace("__ROW143__", "[row 143]")
    s = s.replace(
        "__ROW162TITLE__",
        "Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone",
    )
    s = s.replace(
        "Row 162 does not replace row 68, row 62, row 141, row 142, row 122, row 102, row 82, row 61, or row 42",
        "Row 162 does not replace row 68, row 62, row 161, row 142, row 122, row 102, row 82, row 61, or row 42",
    )
    s = s.replace(
        "When row 162 is complete, proceed to [row 163]",
        "When row 162 is complete, proceed to [row 163](preface.md#skill-navigation-row-163)",
    )
    s = s.replace("prologue row 142 preview", "prologue row 162 preview")
    s = s.replace("prologue row 142 closing stitch", "prologue row 162 closing stitch")
    s = s.replace("epilogue row 142 closing loop", "epilogue row 162 closing loop")
    s = s.replace("Preface row 142", "Preface row 162")
    s = s.replace(
        "per [row 142](../preface.md#skill-navigation-row-162)",
        "per [row 162](../preface.md#skill-navigation-row-162)",
    )
    s = s.replace(
        "([row 142](prologue/00-many-scales.md#prologue-preview-row-162))",
        "([row 162](prologue/00-many-scales.md#prologue-preview-row-162))",
    )
    return s


def fix_row_161_tail(preface: str) -> str:
    trimmed = (
        "When row 161 is complete, proceed to [row 162](preface.md#skill-navigation-row-162) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, "
        "to [row 142](preface.md#skill-navigation-row-142) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, "
        "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, "
        "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, "
        "to [row 160](preface.md#skill-navigation-row-160) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta prelude capstone on the capstone path, "
        "to [row 61](preface.md#skill-navigation-row-61) when only Handshake 4a meta stalls, "
        "or extend prose only under `writings/` then sync."
    )
    bloated_markers = [
        "When row 141 is complete, proceed to [row 142]",
        "to [row 122](preface.md#skill-navigation-row-142) when Handshake 4a",
        "to [row 141](preface.md#skill-navigation-row-101)",
    ]
    if "When row 161 is complete, proceed to [row 162]" in preface:
        for marker in bloated_markers:
            if marker in preface:
                preface = re.sub(
                    r"When row 161 is complete, proceed to \[row 162\].*?or extend prose only under `writings/` then sync\.",
                    trimmed,
                    preface,
                    count=1,
                    flags=re.S,
                )
                break
    old_open = (
        "when opening [row 142](preface.md#skill-navigation-row-142) before row 62 closes on the capstone path"
    )
    new_open = (
        "when opening [row 162](preface.md#skill-navigation-row-162) before row 62 closes on the capstone path"
    )
    preface = preface.replace(old_open, new_open)
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
    if "### Row 162 skill checkpoint" in text:
        print("preface: row 162 already present")
        return
    m = re.search(
        r"(### Row 142 skill checkpoint.*?)(?=\n### Row 143 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 142 checkpoint missing")
    block = lift_142_to_162(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 162")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-162-closing-loop" in text:
        print("epilogue: row 162 loop already present")
        return
    block = lift_142_to_162(
        extract_between(
            text,
            "### Row 142 closing loop",
            "### Row 143 closing loop",
        )
    )
    needle = "### Row 161 closing loop"
    if needle not in text:
        needle = "### Row 142 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 162 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 162) |"
    if compass in text:
        print("prologue: row 162 compass already present")
    else:
        after = "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 161) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 161 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 142) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 142 compass missing")
        new_line = lift_142_to_162(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-142"></span>'
    preview_dst = '| <span id="prologue-preview-row-162"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_142_to_162(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 162 closing stitch" not in text:
        stitch = (
            "**Row 162 closing stitch (Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** {#row-162-closing-stitch} "
            "When row 161 closed — Handshake 4a meta prelude capstone verified, row 160 or row 141 recited on the capstone path, and "
            "[`parse_rate.sh`](../../scripts/parse_rate.sh) archived `rate_export.yaml` with lab grip rate matching "
            "[`fixtures/cht_export.yaml`](../../fixtures/cht_export.yaml) at \\(T_w\\) after verified Handshake 4a meta prelude capstone — "
            "but **row 62 Handshake 4b meta reunion still opens like standalone epilogue coursework after the Handshake 4b opening prelude chapter hinge on the capstone path** — "
            "read [preface row 162](../preface.md#skill-navigation-row-162), the "
            "[Row 68 → Row 142 reunion index](../appendix/sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162), and "
            "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) before row 63 orchestration meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 161 closing stitch", stitch + "**Row 161 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 162 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162"
    if idx_key in text:
        print("sources: row 162 already present")
        return
    block = lift_142_to_162(
        extract_between(
            text,
            "## Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 142)",
            "## Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 123)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162)",
        f"## Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 162) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 162 | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 4a meta prelude capstone ↔ row 62 meta) | "
        f"[Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 162](../preface.md#skill-navigation-row-162) · "
        "[prologue row 162 preview](../prologue/00-many-scales.md#prologue-preview-row-162) · "
        "[prologue row 162 closing stitch](../prologue/00-many-scales.md#row-162-closing-stitch) · "
        "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) · "
        "[memory sheet row 162 baby picture](memory-sheet.md#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 62 Handshake 4b meta reunion still feels disconnected from verified Handshake 4a meta prelude capstone on the capstone path** — "
        "read row 68 + row 161 or row 142 gate + epilogue FE² cross-links + row 62; "
        "[preface row 62](../preface.md#skill-navigation-row-62) |\n"
    )
    text = text.replace(
        "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        table_row + "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 161)",
        block + "## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 161)",
    )
    extra = (
        "[row 162](#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) reunites **Handshake 4a meta prelude capstone with the Handshake 4b meta prelude capstone boundary** "
        "when row 161 closed Handshake 4a meta prelude capstone at verified bulk hardening on the capstone path but epilogue FE² cross-links and Part VII Step 4 still read like separate courses after verified Handshake 4b meta prelude meta;"
    )
    if extra not in text:
        text = text.replace(
            "when row 140 closed Handshake 3 meta prelude capstone at verified thermal pre-stress on the capstone path but epilogue rate cross-links and Part VII still read like separate courses after verified Handshake 4a meta prelude meta;",
            "when row 140 closed Handshake 3 meta prelude capstone at verified thermal pre-stress on the capstone path but epilogue rate cross-links and Part VII still read like separate courses after verified Handshake 4a meta prelude meta; "
            + extra,
        )
    path.write_text(text)
    print("sources: added row 162")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 162 already present")
        return
    baby = lift_142_to_162(
        extract_between(text, "### Row 142 baby picture", "### Row 123 baby picture")
    )
    text = text.replace("### Row 142 baby picture", baby + "### Row 142 baby picture", 1)
    mem_table = (
        "| 162 | Meta | Row 68 → Row 142 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion | "
        "[Row 68 → Row 142 Handshake 4b meta prelude capstone reunion index](sources.md#row68-row142-handshake4b-meta-prelude-capstone-reunion-index-row-162) · "
        "[preface row 162 skill checkpoint](../preface.md#skill-navigation-row-162) · "
        "[prologue row 162 preview](../prologue/00-many-scales.md#prologue-preview-row-162) · "
        "[prologue row 162 closing stitch](../prologue/00-many-scales.md#row-162-closing-stitch) · "
        "[epilogue row 162 closing loop](../epilogue/multiscale.md#row-162-closing-loop) | "
        "Row 68 closed but row 62 Handshake 4b meta reunion feels disconnected from verified Handshake 4a meta prelude capstone on the capstone path — "
        "read row 68 + row 161 or row 142 gate + epilogue FE² cross-links + row 62; "
        "[row 162 baby picture](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 161 | Meta | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion |",
        mem_table + "| 161 | Meta | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion |",
    )
    switch = (
        "When row 161 closed but Handshake 4b meta prelude capstone reunion still lags on the capstone path, switch to [row 162](#row-162-baby-picture-row68-row142-handshake4b-meta-prelude-capstone-reunion)."
    )
    if "When row 161 closed but Handshake 4b meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 160 closed but Handshake 4a meta prelude capstone reunion still lags on the capstone path, switch to [row 161](#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion).",
            "When row 160 closed but Handshake 4a meta prelude capstone reunion still lags on the capstone path, switch to [row 161](#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 162")


def fix_preface_row162() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m142 = re.search(
        r"(### Row 142 skill checkpoint.*?)(?=\n### Row 143 skill checkpoint)",
        text,
        re.S,
    )
    if not m142:
        raise SystemExit("row 142 preface checkpoint missing")
    block162 = lift_142_to_162(m142.group(1))
    start = text.find("### Row 162 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block162 + text[end:]
        path.write_text(text)
        print("preface: repaired row 162")


def fix_epilogue_row162() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-162-closing-loop" not in text:
        return
    block142 = extract_between(
        text, "### Row 142 closing loop", "### Row 143 closing loop"
    )
    block162 = lift_142_to_162(block142)
    start = text.find("### Row 162 closing loop")
    end = text.find("\n### Row 161 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block162 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 162 loop")


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(fix_row_161_tail(preface_path.read_text()))
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row162()
    insert_epilogue_loop()
    fix_epilogue_row162()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
