#!/usr/bin/env python3
"""Add row 159 (Handshake 3 meta prelude capstone reunion) from row 139 baseline."""
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


def lift_139_to_159(s: str) -> str:
    s = s.replace("Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone", "__ROW159TITLE__")
    s = s.replace("[row 140]", "__ROW140__")
    s = s.replace("[row 119]", "__ROW139OPEN__")
    s = s.replace("row 119", "__ROW139OPENNUM__")
    p = [
        ("skill-navigation-row-138", "skill-navigation-row-158"),
        ("skill-navigation-row-98", "skill-navigation-row-158"),
        ("skill-navigation-row-117", "skill-navigation-row-157"),
        ("skill-navigation-row-119", "skill-navigation-row-139"),
        ("skill-navigation-row-139", "skill-navigation-row-159"),
        (
            "row68-row79-handshake3-meta-prelude-reunion-index-row-99",
            "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        ),
        (
            "Row 68 → Row 79 Handshake 3 meta prelude reunion index (row 99)",
            "Row 68 → Row 139 Handshake 3 meta prelude reunion index (row 139)",
        ),
        ("### Row 139 skill checkpoint", "### Row 159 skill checkpoint"),
        ("Row 139 does not replace", "Row 159 does not replace"),
        ("Row 139 three-way audit", "Row 159 three-way audit"),
        ("Row 139 closing loop", "Row 159 closing loop"),
        ("row-139-closing-loop", "row-159-closing-loop"),
        ("Row 139 closing stitch", "Row 159 closing stitch"),
        ("row-139-closing-stitch", "row-159-closing-stitch"),
        ("prologue-preview-row-139", "prologue-preview-row-159"),
        ("Row 139 preview", "Row 159 preview"),
        ("Row 139 skill checkpoint", "Row 159 skill checkpoint"),
        ("memory sheet row 139", "memory sheet row 159"),
        ("Row 139 baby picture", "Row 159 baby picture"),
        (
            "row68-row119-handshake3-meta-capstone-reunion-index-row-139",
            "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        ),
        (
            "row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion",
            "row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion",
        ),
        ("[row 138]", "[row 158]"),
        ("row 138", "row 158"),
        ("Row 138", "Row 158"),
        ("Row 119", "Row 139"),
        ("[row 139]", "[row 159]"),
        ("row 139", "row 159"),
        ("Row 139", "Row 159"),
        (
            "Row 68 → Row 119 Handshake 3 meta capstone reunion index (row 139)",
            "Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index (row 159)",
        ),
        (
            "verified DFT workflows meta capstone closure (row 138)",
            "verified DFT workflows meta prelude capstone closure (row 158)",
        ),
        ("when row 138 closed but row 59", "when row 158 closed but row 59"),
        ("when row 138 and row 59", "when row 158 and row 59"),
        (
            "rear-view mirror of row 138's cutoff certificate → foundation archive → quasiharmonic",
            "rear-view mirror of row 158's foundation archive → quasiharmonic \\(\\alpha(T_w)\\) → load-cell turn",
        ),
        (
            "when opening [row 140](preface.md#skill-navigation-row-140) before row 60 closes on the capstone path",
            "when opening [row 160](preface.md#skill-navigation-row-160) before row 60 closes on the capstone path",
        ),
        (
            "When row 139 is complete, proceed to [row 140]",
            "When row 159 is complete, proceed to [row 140]",
        ),
        (
            "row 139 names **why that reunion must follow verified DFT workflows meta capstone (row 138)",
            "row 159 names **why that reunion must follow verified DFT workflows meta prelude capstone (row 158)",
        ),
        ("Row 68 → Row 59 meta (row 139)", "Row 68 → Row 59 meta (row 159)"),
        ("Row 68 → Row 119 reunion index", "Row 68 → Row 139 reunion index"),
        (
            "Proceed to [row 140](#row-139-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 139 on the capstone path",
            "Proceed to [row 160](#row-159-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 159 on the capstone path, "
            "to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 139 on the opening-hinge path, "
            "to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 119 on the opening-hinge path",
        ),
        (
            "it names the dual reunion before the quasiharmonic \\(\\alpha\\) Lab act",
            "it names the dual reunion before the Handshake 3 meta prelude capstone reunion",
        ),
        ("Recite [preface row 138]", "Recite [preface row 158]"),
        ("Handshake 3 meta capstone reunion", "Handshake 3 meta prelude capstone reunion"),
        ("Handshake 3 meta capstone at the", "Handshake 3 meta prelude capstone at the"),
        ("before Handshake 3 meta capstone", "before Handshake 3 meta prelude capstone"),
        ("Handshake 3 meta capstone boundary", "Handshake 3 meta prelude capstone boundary"),
        ("Midpoint Bridge chain recited before Handshake 3 meta capstone", "Midpoint Bridge chain recited before Handshake 3 meta prelude capstone"),
        ("Name row 68 closed before Handshake 3 meta capstone", "Name row 68 closed before Handshake 3 meta prelude capstone"),
        ("Name DFT workflows meta capstone before IX.3 Bridge", "Name DFT workflows meta prelude capstone before IX.3 Bridge"),
        ("DFT workflows meta capstone / Handshake 3 opening gate", "DFT workflows meta prelude capstone / Handshake 3 opening gate"),
        ("DFT workflows meta capstone and IX.3 → Handshake 3", "DFT workflows meta prelude capstone and IX.3 → Handshake 3"),
        (
            "when `foundation_export.yaml` exists on the capstone path but `alpha_export.yaml` lists `target_temperature_K: 300` after row 138",
            "when `foundation_export.yaml` exists on the capstone path but `alpha_export.yaml` lists `target_temperature_K: 300` after row 158",
        ),
        (
            "when row 138 closed but row 59 IX.3 → Handshake 3 reunion still feels like epilogue homework disconnected from verified DFT workflows meta capstone",
            "when row 158 closed but row 59 IX.3 → Handshake 3 reunion still feels like epilogue homework disconnected from verified DFT workflows meta prelude capstone on the capstone path",
        ),
        (
            "Do not conflate row 139 (row 68 ↔ row 59 reunion on the capstone path) with row 119",
            "Do not conflate row 159 (row 68 ↔ row 59 reunion on the capstone path) with row 139",
        ),
        (
            "before row 60 Handshake 3 meta prelude opens on the capstone path in workflow time",
            "before row 60 Handshake 3 meta prelude capstone opens on the capstone path in workflow time",
        ),
        (
            "When row 139 is complete, proceed to [row 140](preface.md#skill-navigation-row-140) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 120](preface.md#skill-navigation-row-120) when Handshake 3 meta capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 119](preface.md#skill-navigation-row-119) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 138](preface.md#skill-navigation-row-138) when DFT workflows meta capstone still lags after verified Kohn–Sham meta capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync.",
            "When row 159 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 158](preface.md#skill-navigation-row-158) when DFT workflows meta prelude capstone still lags after verified Kohn–Sham meta prelude capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "When row 158 is complete, proceed to [row 139](preface.md#skill-navigation-row-139) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 119](preface.md#skill-navigation-row-139) when DFT workflows meta capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 138](preface.md#skill-navigation-row-158) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 157](preface.md#skill-navigation-row-157) when Kohn–Sham meta capstone still lags after verified Born–Oppenheimer meta capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync.",
            "When row 158 is complete, proceed to [row 159](preface.md#skill-navigation-row-159) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 139](preface.md#skill-navigation-row-139) when DFT workflows meta prelude capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 157](preface.md#skill-navigation-row-157) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync.",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW140__", "[row 140]")
    s = s.replace("__ROW139OPEN__", "[row 139]")
    s = s.replace("__ROW139OPENNUM__", "row 139")
    s = s.replace(
        "__ROW159TITLE__",
        "Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone",
    )
    s = s.replace(
        "and [row 158](preface.md#skill-navigation-row-158) or [row 159](preface.md#skill-navigation-row-159) closed the DFT",
        "and [row 158](preface.md#skill-navigation-row-158) or [row 139](preface.md#skill-navigation-row-139) closed the DFT",
    )
    s = s.replace("Row 159 does not replace row 68, row 59, row 158, row 159,", "Row 159 does not replace row 68, row 59, row 158, row 139,")
    s = s.replace(
        "When row 159 is complete, proceed to [row 140]",
        "When row 159 is complete, proceed to [row 160](preface.md#skill-navigation-row-160)",
    )
    return s


def fix_row_158_tail(preface: str) -> str:
    old = (
        "When row 158 is complete, proceed to [row 139](preface.md#skill-navigation-row-139) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 119](preface.md#skill-navigation-row-139) when DFT workflows meta capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 138](preface.md#skill-navigation-row-158) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 157](preface.md#skill-navigation-row-157) when Kohn–Sham meta capstone still lags after verified Born–Oppenheimer meta capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 158 is complete, proceed to [row 159](preface.md#skill-navigation-row-159) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 139](preface.md#skill-navigation-row-139) when DFT workflows meta prelude capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 157](preface.md#skill-navigation-row-157) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
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
    if "### Row 159 skill checkpoint" in text:
        print("preface: row 159 already present")
        return
    m = re.search(
        r"(### Row 139 skill checkpoint.*?)(?=\n### Row 140 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 139 checkpoint missing")
    block = lift_139_to_159(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 159")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-159-closing-loop" in text:
        print("epilogue: row 159 loop already present")
        return
    block = lift_139_to_159(
        extract_between(
            text,
            "### Row 139 closing loop",
            "### Row 120 closing loop",
        )
    )
    needle = "### Row 158 closing loop"
    if needle not in text:
        needle = "### Row 139 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 159 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    after = "| Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 158) |"
    compass = "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
    if compass in text:
        print("prologue: row 159 compass already present")
    else:
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 158 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion (row 139) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 139 compass missing")
        new_line = lift_139_to_159(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-139"></span>'
    preview_dst = '| <span id="prologue-preview-row-159"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_139_to_159(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 159 closing stitch" not in text:
        stitch = (
            "**Row 159 closing stitch (Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-159-closing-stitch} "
            "When row 158 closed — DFT workflows meta prelude capstone verified, row 157 or row 138 recited on the capstone path, and IX.2 Bridge → IX.3 calculation ladder recited with "
            "[foundation archive Lab act](../part09-dft/03-dft-workflows.md#lab-act-archive-the-foundation-run-before-the-wire-scale-solve-act-vi--foundation) archived `foundation_export.yaml` — but **row 59 IX.3 → Handshake 3 opening hinge still opens like standalone epilogue homework after the workflow archive Scene on the capstone path** — "
            "read [preface row 159](../preface.md#skill-navigation-row-159), the "
            "[Row 68 → Row 139 reunion index](../appendix/sources.md#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159), and "
            "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) before row 60 Handshake 3 meta prelude capstone opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 158 closing stitch", stitch + "**Row 158 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 159 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159"
    if idx_key in text:
        print("sources: row 159 already present")
        return
    block = lift_139_to_159(
        extract_between(
            text,
            "## Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion index (row 139)",
            "## Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 140)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159)",
        f"## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 159 | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone "
        "(midpoint prelude gate ↔ DFT workflows meta prelude capstone ↔ row 59 meta) | "
        f"[Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 159](../preface.md#skill-navigation-row-159) · "
        "[prologue row 159 preview](../prologue/00-many-scales.md#prologue-preview-row-159) · "
        "[prologue row 159 closing stitch](../prologue/00-many-scales.md#row-159-closing-stitch) · "
        "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) · "
        "[memory sheet row 159 baby picture](memory-sheet.md#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 59 IX.3 → Handshake 3 opening hinge still feels disconnected from verified DFT workflows meta prelude capstone on the capstone path** — "
        "read row 68 + row 158 or row 139 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[preface row 59](../preface.md#skill-navigation-row-59) |\n"
    )
    text = text.replace(
        "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
        table_row + "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)",
        block + "## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)",
    )
    path.write_text(text)
    print("sources: added row 159")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 159 already present")
        return
    baby = lift_139_to_159(
        extract_between(text, "### Row 139 baby picture", "### Row 140 baby picture")
    )
    text = text.replace("### Row 140 baby picture", baby + "### Row 140 baby picture", 1)
    mem_table = (
        "| 159 | Meta | Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion | "
        "[Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159) · "
        "[preface row 159 skill checkpoint](../preface.md#skill-navigation-row-159) · "
        "[prologue row 159 preview](../prologue/00-many-scales.md#prologue-preview-row-159) · "
        "[prologue row 159 closing stitch](../prologue/00-many-scales.md#row-159-closing-stitch) · "
        "[epilogue row 159 closing loop](../epilogue/multiscale.md#row-159-closing-loop) | "
        "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified DFT workflows meta prelude capstone on the capstone path — "
        "read row 68 + row 158 or row 139 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[row 159 baby picture](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 158 | Meta | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion |",
        mem_table + "| 158 | Meta | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion |",
    )
    switch = (
        "When row 158 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 159](#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion)."
    )
    if "When row 158 closed but Handshake 3 meta reunion still lags" not in text:
        text = text.replace(
            "When row 157 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 158](#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion).",
            "When row 157 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 158](#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 159")


def fix_preface_row159() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m139 = re.search(
        r"(### Row 139 skill checkpoint.*?)(?=\n### Row 140 skill checkpoint)",
        text,
        re.S,
    )
    if not m139:
        raise SystemExit("row 139 preface checkpoint missing")
    block159 = lift_139_to_159(m139.group(1))
    start = text.find("### Row 159 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block159 + text[end:]
        path.write_text(text)
        print("preface: repaired row 159")


def fix_epilogue_row159() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-159-closing-loop" not in text:
        return
    block139 = extract_between(
        text, "### Row 139 closing loop", "### Row 120 closing loop"
    )
    block159 = lift_139_to_159(block139)
    start = text.find("### Row 159 closing loop")
    end = text.find("\n### Row 158 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block159 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 159 loop")


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface_path.write_text(fix_row_158_tail(preface_path.read_text()))
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row159()
    insert_epilogue_loop()
    fix_epilogue_row159()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
