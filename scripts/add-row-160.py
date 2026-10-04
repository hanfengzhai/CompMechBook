#!/usr/bin/env python3
"""Add row 160 (Handshake 3 meta prelude capstone reunion) from row 140 baseline."""
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


def lift_140_to_160(s: str) -> str:
    s = s.replace(
        "Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        "__ROW160TITLE__",
    )
    s = s.replace("[row 141]", "__ROW141__")
    s = s.replace("[row 140](preface.md#skill-navigation-row-140)", "__ROW140HINGE__")
    s = s.replace(
        "[row 140](prologue/00-many-scales.md#prologue-preview-row-140)",
        "__ROW140PREVIEW__",
    )
    p = [
        ("Row 141 closing loop", "__ROW141_LOOP__"),
        ("skill-navigation-row-120", "skill-navigation-row-140"),
        ("skill-navigation-row-139", "skill-navigation-row-159"),
        ("skill-navigation-row-140", "skill-navigation-row-160"),
        ("Row 140 closing loop", "Row 160 closing loop"),
        ("row-140-closing-loop", "row-160-closing-loop"),
        ("Row 140 closing stitch", "Row 160 closing stitch"),
        ("row-140-closing-stitch", "row-160-closing-stitch"),
        ("prologue-preview-row-140", "prologue-preview-row-160"),
        ("Row 140 preview", "Row 160 preview"),
        ("Row 140 skill checkpoint", "Row 160 skill checkpoint"),
        ("memory sheet row 140", "memory sheet row 160"),
        ("Row 140 baby picture", "Row 160 baby picture"),
        ("Row 140 three-way audit", "Row 160 three-way audit"),
        ("Row 140 does not replace", "Row 160 does not replace"),
        (
            "row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140",
            "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
        ),
        (
            "row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion",
            "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion",
        ),
        ("[row 100]", "[row 120]"),
        ("row 100", "row 120"),
        ("Row 100", "Row 120"),
        ("[row 120]", "[row 140]"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("[row 139]", "[row 159]"),
        ("row 139", "row 159"),
        ("Row 139", "Row 159"),
        ("(row 140)", "(row 160)"),
        ("__ROW141_LOOP__", "Row 141 closing loop"),
        (
            "verified Handshake 3 meta capstone closure (row 159)",
            "verified Handshake 3 meta prelude capstone closure (row 159)",
        ),
        (
            "Row 68 → Row 60 meta (row 140)",
            "Row 68 → Row 60 meta (row 160)",
        ),
        (
            "when opening [row 141](preface.md#skill-navigation-row-141) before row 61 closes on the capstone path",
            "when opening [row 161](preface.md#skill-navigation-row-161) before row 61 closes on the capstone path",
        ),
        (
            "When row 140 is complete, proceed to [row 141]",
            "When row 160 is complete, proceed to [row 141]",
        ),
        (
            "row 140 names **why that reunion must follow verified Handshake 3 meta capstone (row 159)",
            "row 160 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 159)",
        ),
        ("Row 68 → Row 140 reunion index", "Row 68 → Row 140 reunion index"),
        (
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 140 on the capstone path",
            "Proceed to [row 161](#row-160-closing-loop) when row 68 closed but Handshake 4a meta prelude capstone still lags after row 160 on the capstone path, "
            "to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 140 on the opening-hinge path, "
            "to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 120 on the opening-hinge path",
        ),
        (
            "when `alpha_export.yaml` is correct on the capstone path after row 159 but the cross-links audit was skipped",
            "when `alpha_export.yaml` is correct on the capstone path after row 159 but the cross-links audit was skipped",
        ),
        (
            "when row 159 closed but row 60",
            "when row 159 closed but row 60",
        ),
        (
            "When row 159 closed — Handshake 3 meta capstone verified, row 158 or row 139 recited on the capstone path",
            "When row 159 closed — Handshake 3 meta prelude capstone verified, row 158 or row 139 recited on the capstone path",
        ),
        (
            "when row 159 and row 60 both verify individually",
            "when row 159 and row 60 both verify individually",
        ),
        (
            "when row 159 closed Handshake 3 meta capstone and row 68 closed the midpoint prelude but **row 60 Handshake 3 meta still opens",
            "when row 159 closed Handshake 3 meta prelude capstone and row 68 closed the midpoint prelude but **row 60 Handshake 3 meta still opens",
        ),
        (
            "rear-view mirror of row 159's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
            "rear-view mirror of row 159's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
        ),
        (
            "rear-view mirror of row 139's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
            "rear-view mirror of row 159's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
        ),
        (
            "Do not conflate row 160 (row 68 ↔ row 60 reunion on the capstone path) with row 140 (opening-hinge prelude stitch alone)",
            "Do not conflate row 160 (row 68 ↔ row 60 reunion on the capstone path) with row 140 (opening-hinge prelude stitch alone)",
        ),
        (
            "Do not conflate row 140 (row 68 ↔ row 60 reunion on the capstone path) with row 140 (opening-hinge prelude stitch alone)",
            "Do not conflate row 160 (row 68 ↔ row 60 reunion on the capstone path) with row 140 (opening-hinge prelude stitch alone)",
        ),
        (
            "When row 140 is complete, proceed to [row 141](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 121](preface.md#skill-navigation-row-121) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 139](preface.md#skill-navigation-row-139) when Handshake 3 meta capstone still lags after verified DFT workflows meta capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-61) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync.",
            "When row 160 is complete, proceed to [row 161](preface.md#skill-navigation-row-161) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 141](preface.md#skill-navigation-row-141) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 159](preface.md#skill-navigation-row-159) when Handshake 3 meta capstone still lags after verified DFT workflows meta prelude capstone on the capstone path, to [row 60](preface.md#skill-navigation-row-60) when only Handshake 3 meta stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "before row 141 Handshake 4a meta prelude capstone or row 61 workflow reunion opens on the capstone path",
            "before row 161 Handshake 4a meta prelude capstone or row 61 workflow reunion opens on the capstone path",
        ),
        (
            "read row 68 gate + row 159 or row 140 Handshake 3 meta capstone / Handshake 3 meta prelude gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI",
            "read row 68 gate + row 159 or row 140 Handshake 3 meta prelude capstone / Handshake 3 meta prelude gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI",
        ),
        (
            "Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index (row 160)",
            "Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index (row 160)",
        ),
        (
            "Row 68 → Row 140 Handshake 3 meta prelude reunion index (row 140)",
            "Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index (row 160)",
        ),
        (
            "Row 68 → Row 140 Handshake 3 meta prelude reunion index (row 120)",
            "Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index (row 160)",
        ),
        (
            "When row 60 feels like epilogue homework after row 159 alone on the capstone path",
            "When row 60 feels like epilogue homework after row 159 alone on the capstone path",
        ),
        (
            "When row 60 feels like epilogue homework after row 139 alone on the capstone path",
            "When row 60 feels like epilogue homework after row 159 alone on the capstone path",
        ),
        (
            "row 140 names **Row 68 → Row 80 Row 68 → Row 60 Handshake 3 meta prelude reunion**; row 140 names",
            "row 140 names **Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude reunion**; row 160 names",
        ),
        (
            "Row 140 closes the **Handshake 3 meta prelude capstone",
            "Row 160 closes the **Handshake 3 meta prelude capstone",
        ),
        (
            "DFT workflows meta capstone both read correctly alone",
            "Handshake 3 meta prelude capstone both read correctly alone",
        ),
        (
            "verified DFT workflows meta capstone, or row 140's epilogue",
            "verified Handshake 3 meta prelude capstone, or row 140's epilogue",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW140HINGE__", "[row 140](preface.md#skill-navigation-row-140)")
    s = s.replace(
        "__ROW140PREVIEW__",
        "[row 140](prologue/00-many-scales.md#prologue-preview-row-140)",
    )
    s = s.replace("__ROW141__", "[row 141]")
    s = s.replace(
        "__ROW160TITLE__",
        "Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
    )
    s = s.replace(
        "Row 160 does not replace row 68, row 60, row 159, row 140, row 140,",
        "Row 160 does not replace row 68, row 60, row 159, row 140, row 120,",
    )
    s = s.replace(
        "When row 160 is complete, proceed to [row 141]",
        "When row 160 is complete, proceed to [row 161](preface.md#skill-navigation-row-161)",
    )
    s = s.replace("[row 160]", "[row 160]")
    s = s.replace(
        "([row 140](prologue/00-many-scales.md#prologue-preview-row-160))",
        "([row 160](prologue/00-many-scales.md#prologue-preview-row-160))",
    )
    s = s.replace("prologue row 140 preview", "prologue row 160 preview")
    s = s.replace("prologue row 140 closing stitch", "prologue row 160 closing stitch")
    s = s.replace("epilogue row 140 closing loop", "epilogue row 160 closing loop")
    s = s.replace("Preface row 140", "Preface row 160")
    s = s.replace(
        "per [row 140](../preface.md#skill-navigation-row-160)",
        "per [row 160](../preface.md#skill-navigation-row-160)",
    )
    return s


def fix_row_159_tail(preface: str) -> str:
    old = (
        "When row 159 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 158](preface.md#skill-navigation-row-158) when DFT workflows meta prelude capstone still lags after verified Kohn–Sham meta prelude capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 159 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) when load cell parses on the capstone path but Handshake 3 meta prelude capstone still lags, to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 158](preface.md#skill-navigation-row-158) when DFT workflows meta prelude capstone still lags after verified Kohn–Sham meta prelude capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
    )
    return preface.replace(old, new) if old in preface else preface


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
    if "### Row 160 skill checkpoint" in text:
        print("preface: row 160 already present")
        return
    m = re.search(
        r"(### Row 140 skill checkpoint.*?)(?=\n### Row 141 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 140 checkpoint missing")
    block = lift_140_to_160(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 160")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-160-closing-loop" in text:
        print("epilogue: row 160 loop already present")
        return
    block = lift_140_to_160(
        extract_between(
            text,
            "### Row 140 closing loop",
            "### Row 141 closing loop",
        )
    )
    needle = "### Row 159 closing loop"
    if needle not in text:
        needle = "### Row 140 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 160 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    after = "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
    compass = "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 160) |"
    if compass in text:
        print("prologue: row 160 compass already present")
    else:
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 159 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 140) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 140 compass missing")
        new_line = lift_140_to_160(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-140"></span>'
    preview_dst = '| <span id="prologue-preview-row-160"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_140_to_160(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 160 closing stitch" not in text:
        stitch = (
            "**Row 160 closing stitch (Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-160-closing-stitch} "
            "When row 159 closed — Handshake 3 meta prelude capstone verified, row 158 or row 139 recited on the capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` at \\(T_w\\) — but **row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework after the load-cell chapter hinge on the capstone path** — "
            "read [preface row 160](../preface.md#skill-navigation-row-160), the "
            "[Row 68 → Row 140 reunion index](../appendix/sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160), and "
            "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) before row 61 Handshake 4a meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 159 closing stitch", stitch + "**Row 159 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 160 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160"
    if idx_key in text:
        print("sources: row 160 already present")
        return
    block = lift_140_to_160(
        extract_between(
            text,
            "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)",
            "## Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 121)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)",
        f"## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 160 | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 3 meta capstone ↔ row 60 meta) | "
        f"[Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 160](../preface.md#skill-navigation-row-160) · "
        "[prologue row 160 preview](../prologue/00-many-scales.md#prologue-preview-row-160) · "
        "[prologue row 160 closing stitch](../prologue/00-many-scales.md#row-160-closing-stitch) · "
        "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) · "
        "[memory sheet row 160 baby picture](memory-sheet.md#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 60 Handshake 3 meta reunion still feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path** — "
        "read row 68 + row 159 or row 140 gate + epilogue α cross-links + row 60; "
        "[preface row 60](../preface.md#skill-navigation-row-60) |\n"
    )
    text = text.replace(
        "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
        table_row + "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159)",
        block + "## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159)",
    )
    path.write_text(text)
    print("sources: added row 160")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 160 already present")
        return
    baby = lift_140_to_160(
        extract_between(text, "### Row 140 baby picture", "### Row 154 baby picture")
    )
    text = text.replace("### Row 141 baby picture", baby + "### Row 141 baby picture", 1)
    mem_table = (
        "| 160 | Meta | Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion | "
        "[Row 68 → Row 140 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160) · "
        "[preface row 160 skill checkpoint](../preface.md#skill-navigation-row-160) · "
        "[prologue row 160 preview](../prologue/00-many-scales.md#prologue-preview-row-160) · "
        "[prologue row 160 closing stitch](../prologue/00-many-scales.md#row-160-closing-stitch) · "
        "[epilogue row 160 closing loop](../epilogue/multiscale.md#row-160-closing-loop) | "
        "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path — "
        "read row 68 + row 159 or row 140 gate + epilogue α cross-links + row 60; "
        "[row 160 baby picture](#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 159 | Meta | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
        mem_table + "| 159 | Meta | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
    )
    switch = (
        "When row 159 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 160](#row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion)."
    )
    if "When row 159 closed but Handshake 3 meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 158 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 159](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion).",
            "When row 158 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 159](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 160")


def fix_preface_row160() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m140 = re.search(
        r"(### Row 140 skill checkpoint.*?)(?=\n### Row 141 skill checkpoint)",
        text,
        re.S,
    )
    if not m140:
        raise SystemExit("row 140 preface checkpoint missing")
    block160 = lift_140_to_160(m140.group(1))
    start = text.find("### Row 160 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block160 + text[end:]
        path.write_text(text)
        print("preface: repaired row 160")


def fix_epilogue_row160() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-160-closing-loop" not in text:
        return
    block140 = extract_between(
        text, "### Row 140 closing loop", "### Row 141 closing loop"
    )
    block160 = lift_140_to_160(block140)
    start = text.find("### Row 160 closing loop")
    end = text.find("\n### Row 159 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block160 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 160 loop")


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(fix_row_159_tail(preface_path.read_text()))
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row160()
    insert_epilogue_loop()
    fix_epilogue_row160()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
