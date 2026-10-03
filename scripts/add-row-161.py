#!/usr/bin/env python3
"""Add row 161 (Handshake 4a meta prelude capstone reunion) from row 141 baseline."""
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


def lift_141_to_161(s: str) -> str:
    s = s.replace(
        "Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        "__ROW161TITLE__",
    )
    s = s.replace("[row 142]", "__ROW142__")
    s = s.replace("[row 141](preface.md#skill-navigation-row-141)", "__ROW141HINGE__")
    s = s.replace(
        "[row 141](prologue/00-many-scales.md#prologue-preview-row-141)",
        "__ROW141PREVIEW__",
    )
    p = [
        ("Row 142 closing loop", "__ROW142_LOOP__"),
        ("skill-navigation-row-122", "skill-navigation-row-142"),
        ("skill-navigation-row-121", "skill-navigation-row-141"),
        ("skill-navigation-row-141", "skill-navigation-row-161"),
        ("Row 141 closing loop", "Row 161 closing loop"),
        ("row-141-closing-loop", "row-161-closing-loop"),
        ("Row 141 closing stitch", "Row 161 closing stitch"),
        ("row-141-closing-stitch", "row-161-closing-stitch"),
        ("prologue-preview-row-141", "prologue-preview-row-161"),
        ("Row 141 preview", "Row 161 preview"),
        ("Row 141 skill checkpoint", "Row 161 skill checkpoint"),
        ("memory sheet row 141", "memory sheet row 161"),
        ("Row 141 baby picture", "Row 161 baby picture"),
        ("Row 141 three-way audit", "Row 161 three-way audit"),
        ("Row 141 does not replace", "Row 161 does not replace"),
        (
            "row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141",
            "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161",
        ),
        (
            "row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion",
            "row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("[row 122]", "__ROW122_REF__"),
        ("[row 102]", "[row 122]"),
        ("row 102", "row 122"),
        ("Row 102", "Row 122"),
        ("__ROW122_REF__", "[row 122]"),
        ("[row 101]", "[row 121]"),
        ("row 101", "row 121"),
        ("Row 101", "Row 121"),
        ("(row 141)", "(row 161)"),
        ("__ROW142_LOOP__", "Row 142 closing loop"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("preface.md#skill-navigation-row-120)", "preface.md#skill-navigation-row-140)"),
        ("[row 121]", "[row 141]"),
        ("row 121", "row 141"),
        ("Row 121", "Row 141"),
        (
            "verified Handshake 3 meta prelude capstone closure (row 140)",
            "verified Handshake 3 meta prelude capstone closure (row 160)",
        ),
        (
            "Row 68 → Row 61 meta (row 141)",
            "Row 68 → Row 61 meta (row 161)",
        ),
        (
            "when opening [row 142](preface.md#skill-navigation-row-142) before row 62 closes on the capstone path",
            "when opening [row 162](preface.md#skill-navigation-row-162) before row 62 closes on the capstone path",
        ),
        (
            "When row 141 is complete, proceed to [row 142]",
            "When row 161 is complete, proceed to [row 162]",
        ),
        (
            "row 141 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 140)",
            "row 161 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 160)",
        ),
        (
            "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 141 on the capstone path, to [row 122](#row-122-closing-loop) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path",
            "Proceed to [row 162](#row-161-closing-loop) when row 68 closed but Handshake 4b meta prelude capstone still lags after row 161 on the capstone path, "
            "to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 141 on the opening-hinge path, "
            "to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 121 on the opening-hinge path",
        ),
        (
            "when `rate_export.yaml` is missing after row 140 but OpenDiS exports already sit in the plasticity deck",
            "when `rate_export.yaml` is missing on the capstone path after row 160 but OpenDiS exports already sit in the plasticity deck",
        ),
        (
            "when row 140 closed but row 61",
            "when row 160 closed but row 61",
        ),
        (
            "When row 140 closed — Handshake 3 meta prelude capstone verified, row 139 or row 120 recited on the capstone path",
            "When row 160 closed — Handshake 3 meta prelude capstone verified, row 159 or row 140 recited on the capstone path",
        ),
        (
            "before row 142 Handshake 4b meta prelude capstone or row 62 workflow reunion opens on the capstone path",
            "before row 162 Handshake 4b meta prelude capstone or row 62 workflow reunion opens on the capstone path",
        ),
        (
            "when row 140 and row 61 both verify individually",
            "when row 160 and row 61 both verify individually",
        ),
        (
            "when row 140 closed Handshake 3 meta prelude capstone and row 68 closed the midpoint prelude but **row 61 Handshake 4a meta still opens",
            "when row 160 closed Handshake 3 meta prelude capstone and row 68 closed the midpoint prelude but **row 61 Handshake 4a meta still opens",
        ),
        (
            "rear-view mirror of row 140's Handshake 3 meta → forest → power-law",
            "rear-view mirror of row 160's Handshake 3 meta → forest → power-law",
        ),
        (
            "read row 68 gate + row 140 or row 121 Handshake 3 meta prelude capstone / Handshake 4a meta prelude gate + epilogue rate cross-links + row 61 meta aloud when thermal pre-stress is verified on the capstone path after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation",
            "read row 68 gate + row 160 or row 141 Handshake 3 meta prelude capstone / Handshake 4a meta prelude gate + epilogue rate cross-links + row 61 meta aloud when thermal pre-stress is verified on the capstone path after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation",
        ),
        (
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path) with row 121 (opening-hinge prelude stitch alone)",
            "Do not conflate row 161 (row 68 ↔ row 61 reunion on the capstone path) with row 141 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 121 names **Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude reunion**; row 141 names",
            "row 141 names **Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude reunion**; row 161 names",
        ),
        (
            "When row 141 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, to [row 122](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta capstone on the capstone path, to [row 62](preface.md#skill-navigation-row-62) when only Handshake 4b meta stalls, or extend prose only under `writings/` then sync.",
            "When row 161 is complete, proceed to [row 162](preface.md#skill-navigation-row-162) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, to [row 142](preface.md#skill-navigation-row-142) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, to [row 160](preface.md#skill-navigation-row-160) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta prelude capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-61) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "when opening [row 141](preface.md#skill-navigation-row-141) before row 61 closes on the capstone path",
            "when opening [row 161](preface.md#skill-navigation-row-161) before row 61 closes on the capstone path",
        ),
        (
            "[row 140](preface.md#skill-navigation-row-140) or [row 121](preface.md#skill-navigation-row-121) closed the Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
            "[row 160](preface.md#skill-navigation-row-160) or [row 141](preface.md#skill-navigation-row-141) closed the Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
        ),
        (
            "Row 68 → Row 121 Handshake 4a meta prelude capstone reunion index (row 141)",
            "Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index (row 161)",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW141HINGE__", "[row 141](preface.md#skill-navigation-row-141)")
    s = s.replace(
        "__ROW141PREVIEW__",
        "[row 141](prologue/00-many-scales.md#prologue-preview-row-141)",
    )
    s = s.replace("__ROW142__", "[row 142]")
    s = s.replace(
        "__ROW161TITLE__",
        "Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone",
    )
    s = s.replace(
        "Row 161 does not replace row 68, row 61, row 140, row 141, row 121, row 101, row 81, row 60, or row 41",
        "Row 161 does not replace row 68, row 61, row 160, row 141, row 121, row 101, row 81, row 60, or row 41",
    )
    s = s.replace(
        "When row 161 is complete, proceed to [row 162]",
        "When row 161 is complete, proceed to [row 162](preface.md#skill-navigation-row-162)",
    )
    s = s.replace("prologue row 141 preview", "prologue row 161 preview")
    s = s.replace("prologue row 141 closing stitch", "prologue row 161 closing stitch")
    s = s.replace("epilogue row 141 closing loop", "epilogue row 161 closing loop")
    s = s.replace("Preface row 141", "Preface row 161")
    s = s.replace(
        "per [row 141](../preface.md#skill-navigation-row-161)",
        "per [row 161](../preface.md#skill-navigation-row-161)",
    )
    s = s.replace(
        "([row 141](prologue/00-many-scales.md#prologue-preview-row-161))",
        "([row 161](prologue/00-many-scales.md#prologue-preview-row-161))",
    )
    return s


def fix_row_160_tail(preface: str) -> str:
    old_open = (
        "when opening [row 141](preface.md#skill-navigation-row-141) before row 61 closes on the capstone path"
    )
    new_open = (
        "when opening [row 161](preface.md#skill-navigation-row-161) before row 61 closes on the capstone path"
    )
    return preface.replace(old_open, new_open)


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
    if "### Row 161 skill checkpoint" in text:
        print("preface: row 161 already present")
        return
    m = re.search(
        r"(### Row 141 skill checkpoint.*?)(?=\n### Row 142 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 141 checkpoint missing")
    block = lift_141_to_161(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 161")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-161-closing-loop" in text:
        print("epilogue: row 161 loop already present")
        return
    block = lift_141_to_161(
        extract_between(
            text,
            "### Row 141 closing loop",
            "### Row 142 closing loop",
        )
    )
    needle = "### Row 160 closing loop"
    if needle not in text:
        needle = "### Row 141 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 161 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 161) |"
    if compass in text:
        print("prologue: row 161 compass already present")
    else:
        after = "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 160) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 160 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 141) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 141 compass missing")
        new_line = lift_141_to_161(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-141"></span>'
    preview_dst = '| <span id="prologue-preview-row-161"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_141_to_161(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 161 closing stitch" not in text:
        stitch = (
            "**Row 161 closing stitch (Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** {#row-161-closing-stitch} "
            "When row 160 closed — Handshake 3 meta prelude capstone verified, row 159 or row 140 recited on the capstone path, and thermal pre-stress at \\(T_w\\) archived in `alpha_export.yaml` — but **row 61 Handshake 4a meta reunion still opens like standalone epilogue coursework after the Handshake 4a opening prelude chapter hinge on the capstone path** — "
            "read [preface row 161](../preface.md#skill-navigation-row-161), the "
            "[Row 68 → Row 141 reunion index](../appendix/sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161), and "
            "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) before row 62 Handshake 4b meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 160 closing stitch", stitch + "**Row 160 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 161 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161"
    if idx_key in text:
        print("sources: row 161 already present")
        return
    block = lift_141_to_161(
        extract_between(
            text,
            "## Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 141)",
            "## Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 122)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 161)",
        f"## Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 161) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 161 | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 3 meta prelude capstone ↔ row 61 meta) | "
        f"[Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 161](../preface.md#skill-navigation-row-161) · "
        "[prologue row 161 preview](../prologue/00-many-scales.md#prologue-preview-row-161) · "
        "[prologue row 161 closing stitch](../prologue/00-many-scales.md#row-161-closing-stitch) · "
        "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) · "
        "[memory sheet row 161 baby picture](memory-sheet.md#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 61 Handshake 4a meta reunion still feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path** — "
        "read row 68 + row 160 or row 141 gate + epilogue rate cross-links + row 61; "
        "[preface row 61](../preface.md#skill-navigation-row-61) |\n"
    )
    text = text.replace(
        "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        table_row + "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)",
        block + "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)",
    )
    path.write_text(text)
    print("sources: added row 161")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 161 already present")
        return
    baby = lift_141_to_161(
        extract_between(text, "### Row 141 baby picture", "### Row 122 baby picture")
    )
    text = text.replace("### Row 141 baby picture", baby + "### Row 141 baby picture", 1)
    mem_table = (
        "| 161 | Meta | Row 68 → Row 141 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion | "
        "[Row 68 → Row 141 Handshake 4a meta prelude capstone reunion index](sources.md#row68-row141-handshake4a-meta-prelude-capstone-reunion-index-row-161) · "
        "[preface row 161 skill checkpoint](../preface.md#skill-navigation-row-161) · "
        "[prologue row 161 preview](../prologue/00-many-scales.md#prologue-preview-row-161) · "
        "[prologue row 161 closing stitch](../prologue/00-many-scales.md#row-161-closing-stitch) · "
        "[epilogue row 161 closing loop](../epilogue/multiscale.md#row-161-closing-loop) | "
        "Row 68 closed but row 61 Handshake 4a meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path — "
        "read row 68 + row 160 or row 141 gate + epilogue rate cross-links + row 61; "
        "[row 161 baby picture](#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 160 | Meta | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion |",
        mem_table + "| 160 | Meta | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion |",
    )
    switch = (
        "When row 160 closed but Handshake 4a meta prelude capstone reunion still lags on the capstone path, switch to [row 161](#row-161-baby-picture-row68-row141-handshake4a-meta-prelude-capstone-reunion)."
    )
    if "When row 160 closed but Handshake 4a meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 159 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 160](#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion).",
            "When row 159 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 160](#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 161")


def fix_preface_row161() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m141 = re.search(
        r"(### Row 141 skill checkpoint.*?)(?=\n### Row 142 skill checkpoint)",
        text,
        re.S,
    )
    if not m141:
        raise SystemExit("row 141 preface checkpoint missing")
    block161 = lift_141_to_161(m141.group(1))
    start = text.find("### Row 161 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block161 + text[end:]
        path.write_text(text)
        print("preface: repaired row 161")


def fix_epilogue_row161() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-161-closing-loop" not in text:
        return
    block141 = extract_between(
        text, "### Row 141 closing loop", "### Row 142 closing loop"
    )
    block161 = lift_141_to_161(block141)
    start = text.find("### Row 161 closing loop")
    end = text.find("\n### Row 160 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block161 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 161 loop")


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(fix_row_160_tail(preface_path.read_text()))
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row161()
    insert_epilogue_loop()
    fix_epilogue_row161()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
