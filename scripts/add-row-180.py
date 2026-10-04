#!/usr/bin/env python3
"""Add row 180 (Handshake 3 meta prelude capstone reunion) from row 160 baseline."""
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


def lift_160_to_180(s: str) -> str:
    s = s.replace(
        "Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        "Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone",
    )
    s = s.replace("[row 161]", "__ROW161__")
    s = s.replace("[row 160](preface.md#skill-navigation-row-160)", "__ROW160HINGE__")
    s = s.replace(
        "[row 160](prologue/00-many-scales.md#prologue-preview-row-160)",
        "__ROW160PREVIEW__",
    )
    p = [
        ("Row 161 closing loop", "__ROW161_LOOP__"),
        ("skill-navigation-row-140", "skill-navigation-row-160"),
        ("skill-navigation-row-159", "skill-navigation-row-179"),
        ("skill-navigation-row-160", "skill-navigation-row-180"),
        ("Row 160 closing loop", "Row 180 closing loop"),
        ("row-160-closing-loop", "row-180-closing-loop"),
        ("Row 160 closing stitch", "Row 180 closing stitch"),
        ("row-160-closing-stitch", "row-180-closing-stitch"),
        ("prologue-preview-row-160", "prologue-preview-row-180"),
        ("Row 160 preview", "Row 180 preview"),
        ("Row 160 skill checkpoint", "Row 180 skill checkpoint"),
        ("memory sheet row 160", "memory sheet row 180"),
        ("Row 160 baby picture", "Row 180 baby picture"),
        ("Row 160 three-way audit", "Row 180 three-way audit"),
        ("Row 160 does not replace", "Row 180 does not replace"),
        (
            "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160",
            "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180",
        ),
        (
            "row-160-baby-picture-row68-row140-handshake3-meta-prelude-capstone-reunion",
            "row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion",
        ),
        ("[row 120]", "[row 140]"),
        ("row 120", "row 140"),
        ("Row 140", "Row 160"),
        ("[row 140]", "[row 160]"),
        ("row 140", "row 160"),
        ("Row 160", "Row 160"),
        ("[row 159]", "[row 179]"),
        ("row 159", "row 179"),
        ("Row 159", "Row 179"),
        ("(row 160)", "(row 180)"),
        ("__ROW161_LOOP__", "Row 161 closing loop"),
        (
            "verified Handshake 3 meta capstone closure (row 179)",
            "verified Handshake 3 meta prelude capstone closure (row 179)",
        ),
        (
            "Row 68 → Row 60 meta (row 160)",
            "Row 68 → Row 60 meta (row 180)",
        ),
        (
            "when opening [row 161](preface.md#skill-navigation-row-141) before row 61 closes on the capstone path",
            "when opening [row 181](preface.md#skill-navigation-row-161) before row 61 closes on the capstone path",
        ),
        (
            "When row 160 is complete, proceed to [row 161]",
            "When row 180 is complete, proceed to [row 161]",
        ),
        (
            "row 160 names **why that reunion must follow verified Handshake 3 meta capstone (row 179)",
            "row 180 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 179)",
        ),
        ("Row 68 → Row 160 reunion index", "Row 68 → Row 160 reunion index"),
        (
            "Proceed to [row 161](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 160 on the capstone path",
            "Proceed to [row 181](#row-180-closing-loop) when row 68 closed but Handshake 4a meta prelude capstone still lags after row 180 on the capstone path, "
            "to [row 161](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 160 on the opening-hinge path, "
            "to [row 160](#row-160-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 140 on the opening-hinge path",
        ),
        (
            "when `alpha_export.yaml` is correct on the capstone path after row 179 but the cross-links audit was skipped",
            "when `alpha_export.yaml` is correct on the capstone path after row 179 but the cross-links audit was skipped",
        ),
        (
            "when row 179 closed but row 60",
            "when row 179 closed but row 60",
        ),
        (
            "When row 179 closed — Handshake 3 meta capstone verified, row 158 or row 159 recited on the capstone path",
            "When row 179 closed — Handshake 3 meta prelude capstone verified, row 158 or row 159 recited on the capstone path",
        ),
        (
            "when row 179 and row 60 both verify individually",
            "when row 179 and row 60 both verify individually",
        ),
        (
            "when row 179 closed Handshake 3 meta capstone and row 68 closed the midpoint prelude but **row 60 Handshake 3 meta still opens",
            "when row 179 closed Handshake 3 meta prelude capstone and row 68 closed the midpoint prelude but **row 60 Handshake 3 meta still opens",
        ),
        (
            "rear-view mirror of row 179's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
            "rear-view mirror of row 179's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
        ),
        (
            "rear-view mirror of row 159's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
            "rear-view mirror of row 179's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → ascent chain turn",
        ),
        (
            "Do not conflate row 180 (row 68 ↔ row 60 reunion on the capstone path) with row 160 (opening-hinge prelude stitch alone)",
            "Do not conflate row 180 (row 68 ↔ row 60 reunion on the capstone path) with row 160 (opening-hinge prelude stitch alone)",
        ),
        (
            "Do not conflate row 160 (row 68 ↔ row 60 reunion on the capstone path) with row 160 (opening-hinge prelude stitch alone)",
            "Do not conflate row 180 (row 68 ↔ row 60 reunion on the capstone path) with row 160 (opening-hinge prelude stitch alone)",
        ),
        (
            "When row 160 is complete, proceed to [row 161](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 121](preface.md#skill-navigation-row-121) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 140](preface.md#skill-navigation-row-140) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 159](preface.md#skill-navigation-row-159) when Handshake 3 meta capstone still lags after verified DFT workflows meta capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-61) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync.",
            "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-161) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 161](preface.md#skill-navigation-row-141) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 160](preface.md#skill-navigation-row-160) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 179](preface.md#skill-navigation-row-179) when Handshake 3 meta capstone still lags after verified DFT workflows meta prelude capstone on the capstone path, to [row 60](preface.md#skill-navigation-row-60) when only Handshake 3 meta stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "before row 161 Handshake 4a meta prelude capstone or row 61 workflow reunion opens on the capstone path",
            "before row 181 Handshake 4a meta prelude capstone or row 61 workflow reunion opens on the capstone path",
        ),
        (
            "read row 68 gate + row 179 or row 160 Handshake 3 meta capstone / Handshake 3 meta prelude gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI",
            "read row 68 gate + row 179 or row 160 Handshake 3 meta prelude capstone / Handshake 3 meta prelude gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta prelude capstone but Handshake 3 still feels disconnected from Parts III–VI",
        ),
        (
            "Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)",
            "Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)",
        ),
        (
            "Row 68 → Row 160 Handshake 3 meta prelude reunion index (row 160)",
            "Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)",
        ),
        (
            "Row 68 → Row 160 Handshake 3 meta prelude reunion index (row 140)",
            "Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index (row 180)",
        ),
        (
            "When row 60 feels like epilogue homework after row 179 alone on the capstone path",
            "When row 60 feels like epilogue homework after row 179 alone on the capstone path",
        ),
        (
            "When row 60 feels like epilogue homework after row 159 alone on the capstone path",
            "When row 60 feels like epilogue homework after row 179 alone on the capstone path",
        ),
        (
            "row 160 names **Row 68 → Row 80 Row 68 → Row 60 Handshake 3 meta prelude reunion**; row 160 names",
            "row 160 names **Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude reunion**; row 180 names",
        ),
        (
            "Row 160 closes the **Handshake 3 meta prelude capstone",
            "Row 180 closes the **Handshake 3 meta prelude capstone",
        ),
        (
            "DFT workflows meta capstone both read correctly alone",
            "Handshake 3 meta prelude capstone both read correctly alone",
        ),
        (
            "verified DFT workflows meta capstone, or row 160's epilogue",
            "verified Handshake 3 meta prelude capstone, or row 160's epilogue",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW160HINGE__", "[row 160](preface.md#skill-navigation-row-160)")
    s = s.replace(
        "__ROW160PREVIEW__",
        "[row 160](prologue/00-many-scales.md#prologue-preview-row-160)",
    )
    s = s.replace("__ROW161__", "[row 161]")
    s = s.replace(
        "Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        "Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone",
    )
    s = s.replace(
        "Row 180 does not replace row 68, row 60, row 179, row 160, row 160,",
        "Row 180 does not replace row 68, row 60, row 179, row 160, row 140,",
    )
    s = s.replace(
        "When row 180 is complete, proceed to [row 161]",
        "When row 180 is complete, proceed to [row 181](preface.md#skill-navigation-row-161)",
    )
    s = s.replace("[row 180]", "[row 180]")
    s = s.replace(
        "([row 160](prologue/00-many-scales.md#prologue-preview-row-180))",
        "([row 180](prologue/00-many-scales.md#prologue-preview-row-180))",
    )
    s = s.replace("prologue row 160 preview", "prologue row 180 preview")
    s = s.replace("prologue row 160 closing stitch", "prologue row 180 closing stitch")
    s = s.replace("epilogue row 160 closing loop", "epilogue row 180 closing loop")
    s = s.replace("Preface row 160", "Preface row 180")
    s = s.replace(
        "per [row 160](../preface.md#skill-navigation-row-180)",
        "per [row 180](../preface.md#skill-navigation-row-180)",
    )
    return s


def fix_row_179_tail(preface: str) -> str:
    old = (
        "When row 179 is complete, proceed to [row 180](preface.md#skill-navigation-row-180) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 160](preface.md#skill-navigation-row-160) when Handshake 3 meta prelude capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 120](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 159](preface.md#skill-navigation-row-159) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 158](preface.md#skill-navigation-row-158) when DFT workflows meta prelude capstone still lags after verified Kohn–Sham meta prelude capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 179 is complete, proceed to [row 180](preface.md#skill-navigation-row-180) when load cell parses on the capstone path but Handshake 3 meta prelude capstone still lags, to [row 160](preface.md#skill-navigation-row-160) when Handshake 3 meta prelude capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 120](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 159](preface.md#skill-navigation-row-159) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 158](preface.md#skill-navigation-row-158) when DFT workflows meta prelude capstone still lags after verified Kohn–Sham meta prelude capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
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
    if "### Row 180 skill checkpoint" in text:
        print("preface: row 180 already present")
        return
    m = re.search(
        r"(### Row 160 skill checkpoint.*?)(?=\n## The copper wire through the book)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 160 checkpoint missing")
    block = lift_160_to_180(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 180")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-180-closing-loop" in text:
        print("epilogue: row 180 loop already present")
        return
    block = lift_160_to_180(
        extract_between(
            text,
            "### Row 160 closing loop",
            "### Row 159 closing loop",
        )
    )
    needle = "### Row 179 closing loop"
    if needle not in text:
        needle = "### Row 160 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 180 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    after = "#skill-navigation-row-179)"
    compass = "| Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 180) |"
    if compass in text:
        print("prologue: row 180 compass already present")
    else:
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 179 compass missing")
        line_start = text.rfind("\n", 0, idx) + 1
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 160) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 160 compass missing")
        new_line = lift_160_to_180(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-160"></span>'
    preview_dst = '| <span id="prologue-preview-row-180"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_160_to_180(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 180 closing stitch" not in text:
        stitch = (
            "**Row 180 closing stitch (Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-180-closing-stitch} "
            "When row 179 closed — Handshake 3 meta prelude capstone verified, row 158 or row 159 recited on the capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` at \\(T_w\\) — but **row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework after the load-cell chapter hinge on the capstone path** — "
            "read [preface row 180](../preface.md#skill-navigation-row-180), the "
            "[Row 68 → Row 160 reunion index](../appendix/sources.md#row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180), and "
            "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) before row 61 Handshake 4a meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 179 closing stitch", stitch + "**Row 179 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 180 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180"
    if idx_key in text:
        print("sources: row 180 already present")
        return
    start160 = "## Row 68 → Row 140 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 160)"
    i160 = text.find(start160)
    if i160 < 0:
        start160 = "row68-row140-handshake3-meta-prelude-capstone-reunion-index-row-160"
        i160 = text.find(start160)
        i160 = text.rfind("\n## ", 0, i160) if i160 >= 0 else -1
    if i160 < 0:
        start179 = "## Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179)"
        i179 = text.find(start179)
        if i179 < 0:
            print("sources: skip row 180 index (templates missing)")
            return
        j179 = text.find("\n## ", i179 + 10)
        block = lift_160_to_180(text[i179:j179])
    else:
        j160 = text.find("\n## Row 68 → Row 139", i160)
        if j160 < 0:
            j160 = text.find("\n## Row 68 → Row 101", i160)
        block = lift_160_to_180(text[i160:j160])
    block = block.replace(
        "## Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180)",
        f"## Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 180) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 180 | Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone "
        "(midpoint prelude gate ↔ Handshake 3 meta capstone ↔ row 60 meta) | "
        f"[Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 180](../preface.md#skill-navigation-row-180) · "
        "[prologue row 180 preview](../prologue/00-many-scales.md#prologue-preview-row-180) · "
        "[prologue row 180 closing stitch](../prologue/00-many-scales.md#row-180-closing-stitch) · "
        "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) · "
        "[memory sheet row 180 baby picture](memory-sheet.md#row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 60 Handshake 3 meta reunion still feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path** — "
        "read row 68 + row 179 or row 160 gate + epilogue α cross-links + row 60; "
        "[preface row 60](../preface.md#skill-navigation-row-60) |\n"
    )
    text = text.replace(
        "| 179 | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone",
        table_row + "| 179 | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone",
    )
    needle = "## Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179)"
    if needle in text:
        text = text.replace(needle, block + needle, 1)
    else:
        i179 = text.find("row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179")
        i179 = text.rfind("\n## ", 0, i179) if i179 >= 0 else -1
        if i179 < 0:
            raise SystemExit("sources row 179 anchor missing")
        text = text[:i179] + block + "\n\n\n" + text[i179:]
    path.write_text(text)
    print("sources: added row 180")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 180 already present")
        return
    baby = lift_160_to_180(
        extract_between(text, "### Row 160 baby picture", "### Row 174 baby picture")
    )
    text = text.replace("### Row 161 baby picture", baby + "### Row 161 baby picture", 1)
    mem_table = (
        "| 160 | Meta | Row 68 → Row 160 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion | "
        "[Row 68 → Row 160 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row160-handshake3-meta-prelude-capstone-reunion-index-row-180) · "
        "[preface row 180 skill checkpoint](../preface.md#skill-navigation-row-180) · "
        "[prologue row 180 preview](../prologue/00-many-scales.md#prologue-preview-row-180) · "
        "[prologue row 180 closing stitch](../prologue/00-many-scales.md#row-180-closing-stitch) · "
        "[epilogue row 180 closing loop](../epilogue/multiscale.md#row-180-closing-loop) | "
        "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path — "
        "read row 68 + row 179 or row 160 gate + epilogue α cross-links + row 60; "
        "[row 180 baby picture](#row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 159 | Meta | Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
        mem_table + "| 159 | Meta | Row 68 → Row 159 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion |",
    )
    switch = (
        "When row 179 closed but Handshake 3 meta prelude capstone reunion still lags on the capstone path, switch to [row 180](#row-180-baby-picture-row68-row160-handshake3-meta-prelude-capstone-reunion)."
    )
    if "When row 179 closed but Handshake 3 meta prelude capstone reunion still lags" not in text:
        text = text.replace(
            "When row 158 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion).",
            "When row 158 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 180")


def fix_preface_row180() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m160 = re.search(
        r"(### Row 160 skill checkpoint.*?)(?=\n## The copper wire through the book)",
        text,
        re.S,
    )
    if not m160:
        raise SystemExit("row 160 preface checkpoint missing")
    block180 = lift_160_to_180(m160.group(1))
    start = text.find("### Row 180 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block180 + text[end:]
        path.write_text(text)
        print("preface: repaired row 180")


def fix_epilogue_row180() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-180-closing-loop" not in text:
        return
    block160 = lift_160_to_180(
        extract_between(
            text,
            "### Row 160 closing loop",
            "### Row 159 closing loop",
        )
    )
    start = text.find("### Row 180 closing loop")
    end = text.find("\n### Row 179 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block160 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 180 loop")


def dedupe_preface_row_180() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    marker = "### Row 180 skill checkpoint"
    while text.count(marker) > 1:
        first = text.find(marker)
        second = text.find(marker, first + 1)
        end = text.find("\n### ", second)
        if end < 0:
            end = text.find("\n## The copper wire", second)
        text = text[:second] + text[end:]
    path.write_text(text)
    print("preface: deduped row 180 checkpoint")


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(fix_row_179_tail(preface_path.read_text()))
    dedupe_preface_row_180()
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row180()
    insert_epilogue_loop()
    fix_epilogue_row180()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
