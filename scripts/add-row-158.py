#!/usr/bin/env python3
"""Add row 158 (DFT workflows meta prelude capstone reunion) from row 138 baseline."""
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


def lift_138_to_158(s: str) -> str:
    s = s.replace("Row 68 → Row 98", "__ROW68ROW98__")
    s = s.replace(
        "Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone",
        "__ROW158TITLE__",
    )
    p = [
        ("skill-navigation-row-137", "skill-navigation-row-157"),
        ("skill-navigation-row-118", "skill-navigation-row-138"),
        ("skill-navigation-row-138", "skill-navigation-row-158"),
        ("### Row 138 skill checkpoint", "### Row 158 skill checkpoint"),
        ("Row 138 does not replace", "Row 158 does not replace"),
        ("Row 138 three-way audit", "Row 158 three-way audit"),
        ("Row 138 closing loop", "Row 158 closing loop"),
        ("row-138-closing-loop", "row-158-closing-loop"),
        ("Row 138 closing stitch", "Row 158 closing stitch"),
        ("row-138-closing-stitch", "row-158-closing-stitch"),
        ("prologue-preview-row-138", "prologue-preview-row-158"),
        ("Row 138 preview", "Row 158 preview"),
        ("Row 138 skill checkpoint", "Row 158 skill checkpoint"),
        ("memory sheet row 138", "memory sheet row 158"),
        ("Row 138 baby picture", "Row 158 baby picture"),
        (
            "row68-row118-dft-workflows-meta-capstone-reunion-index-row-138",
            "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
        ),
        (
            "row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion",
            "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion",
        ),
        ("[row 139]", "__ROW139__"),
        ("[row 138]", "[row 158]"),
        ("row 138", "row 158"),
        ("Row 138", "Row 158"),
        ("__ROW139__", "[row 139]"),
        ("[row 137]", "[row 157]"),
        ("row 137", "row 157"),
        ("Row 137", "Row 157"),
        ("[row 118]", "[row 138]"),
        ("row 118", "row 138"),
        ("Row 118", "Row 138"),
        (
            "Row 68 → Row 118 DFT workflows meta capstone reunion index (row 138)",
            "Row 68 → Row 138 DFT workflows meta prelude capstone reunion index (row 158)",
        ),
        (
            "verified Kohn–Sham meta capstone closure (row 137)",
            "verified Kohn–Sham meta prelude capstone closure (row 157)",
        ),
        ("when row 137 closed but row 58", "when row 157 closed but row 58"),
        ("when row 137 and row 58", "when row 157 and row 58"),
        (
            "rear-view mirror of row 137's SCF fixed-point → calculation ladder turn",
            "rear-view mirror of row 157's SCF fixed-point → calculation ladder turn",
        ),
        (
            "when opening [row 139](preface.md#skill-navigation-row-139) before row 59 closes on the capstone path",
            "when opening [row 159](preface.md#skill-navigation-row-159) before row 59 closes on the capstone path",
        ),
        (
            "When row 138 is complete, proceed to [row 139]",
            "When row 158 is complete, proceed to [row 139]",
        ),
        (
            "When row 58 feels like DFT coursework after row 137 alone on the capstone path",
            "When row 58 feels like DFT coursework after row 157 alone on the capstone path",
        ),
        (
            "row 138 names **why that reunion must follow verified Kohn–Sham meta capstone (row 137)",
            "row 158 names **why that reunion must follow verified Kohn–Sham meta prelude capstone (row 157)",
        ),
        ("Row 68 → Row 58 meta (row 138)", "Row 68 → Row 58 meta (row 158)"),
        ("Row 68 → Row 118 reunion index", "Row 68 → Row 138 reunion index"),
        (
            "Proceed to [row 139](#row-138-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 138 on the capstone path",
            "Proceed to [row 159](#row-158-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the capstone path, "
            "to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 138 on the opening-hinge path, "
            "to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 137 on the opening-hinge path",
        ),
        (
            "it names the dual reunion before the foundation archive Lab act",
            "it names the dual reunion before the Handshake 3 meta prelude capstone reunion",
        ),
        ("Recite [preface row 137]", "Recite [preface row 157]"),
        ("DFT workflows meta capstone reunion", "DFT workflows meta prelude capstone reunion"),
        ("DFT workflows meta capstone at the", "DFT workflows meta prelude capstone at the"),
        ("before DFT workflows meta capstone", "before DFT workflows meta prelude capstone"),
        ("DFT workflows meta capstone for index-card", "DFT workflows meta prelude capstone for index-card"),
        (
            "when `cutoff_convergence.yaml` exists but `cu.foundation/` is empty after row 137",
            "when `cutoff_convergence.yaml` exists on the capstone path but `cu.foundation/` is empty after row 157",
        ),
        (
            "when row 137 closed but row 58 IX.2 → IX.3 reunion still feels like DFT coursework disconnected from verified Kohn–Sham meta capstone",
            "when row 157 closed but row 58 IX.2 → IX.3 reunion still feels like DFT coursework disconnected from verified Kohn–Sham meta prelude capstone on the capstone path",
        ),
        (
            "Row 68 → Row 58 meta (row 158) must read as one cutoff certificate",
            "Row 68 → Row 58 meta (row 158) must read as one cutoff certificate",
        ),
        (
            "Do not conflate row 138 (row 68 ↔ row 58 reunion on the capstone path) with row 118",
            "Do not conflate row 158 (row 68 ↔ row 58 reunion on the capstone path) with row 138",
        ),
        (
            "row 118 names **Row 68 → Row 78 Row 68 → Row 58 DFT workflows meta prelude reunion**; row 138 names",
            "row 138 names **Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone reunion**; row 158 names",
        ),
        ("Kohn–Sham meta capstone / DFT workflows opening gate", "Kohn–Sham meta prelude capstone / DFT workflows opening gate"),
        (
            "Kohn–Sham meta capstone / DFT workflows opening prelude hinge",
            "Kohn–Sham meta prelude capstone / DFT workflows opening prelude hinge",
        ),
        ("Kohn–Sham meta capstone and IX.2 → IX.3", "Kohn–Sham meta prelude capstone and IX.2 → IX.3"),
        ("verified Kohn–Sham meta capstone closure", "verified Kohn–Sham meta prelude capstone closure"),
        ("Name Kohn–Sham meta capstone before IX.2 Bridge", "Name Kohn–Sham meta prelude capstone before IX.2 Bridge"),
        (
            "Midpoint Bridge chain recited before DFT workflows meta capstone",
            "Midpoint Bridge chain recited before DFT workflows meta prelude capstone",
        ),
        (
            "Name row 68 closed before DFT workflows meta capstone",
            "Name row 68 closed before DFT workflows meta prelude capstone",
        ),
        (
            "return there when row 157 closed Kohn–Sham meta capstone and row 68 closed the midpoint prelude",
            "return there when row 157 closed Kohn–Sham meta prelude capstone and row 68 closed the midpoint prelude",
        ),
        (
            "before row 99 Handshake 3 meta prelude opens in workflow time",
            "before row 59 Handshake 3 meta prelude opens on the capstone path in workflow time",
        ),
        (
            "When row 138 is complete, proceed to [row 139](preface.md#skill-navigation-row-139) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 119](preface.md#skill-navigation-row-139) when DFT workflows meta capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 118](preface.md#skill-navigation-row-118) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 137](preface.md#skill-navigation-row-137) when Kohn–Sham meta capstone still lags after verified Born–Oppenheimer meta capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync.",
            "When row 158 is complete, proceed to [row 159](preface.md#skill-navigation-row-159) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 139](preface.md#skill-navigation-row-139) when DFT workflows meta capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 157](preface.md#skill-navigation-row-157) when Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync.",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW68ROW98__", "Row 68 → Row 98")
    s = s.replace(
        "__ROW158TITLE__",
        "Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
    )
    return s


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
    if "### Row 158 skill checkpoint" in text:
        print("preface: row 158 already present")
        return
    m = re.search(
        r"(### Row 138 skill checkpoint.*?)(?=\n### Row 139 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 138 checkpoint missing")
    block = lift_138_to_158(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 158")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-158-closing-loop" in text:
        print("epilogue: row 158 loop already present")
        return
    block = lift_138_to_158(
        extract_between(
            text,
            "### Row 138 closing loop",
            "### Row 119 closing loop",
        )
    )
    needle = "### Row 157 closing loop"
    if needle not in text:
        needle = "### Row 138 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 158 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    after = "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |"
    if "| Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 158) |" in text:
        print("prologue: row 158 compass already present")
    else:
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 157 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone reunion (row 138) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 138 compass missing")
        new_line = lift_138_to_158(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-138"></span>'
    preview_dst = '| <span id="prologue-preview-row-158"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_138_to_158(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 158 closing stitch" not in text:
        stitch = (
            "**Row 158 closing stitch (Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-158-closing-stitch} "
            "When row 157 closed — Kohn–Sham meta prelude capstone verified, row 156 or row 137 recited on the capstone path, and IX.1 Bridge → IX.2 SCF recited with "
            "[cutoff-sweep Lab act](../part09-dft/02-kohn-sham.md#lab-act-cutoff-sweep-on-fcc-cu-act-vi--convergence-certificate) archived `cutoff_convergence.yaml` — but **row 58 IX.2 → IX.3 opening hinge still opens like standalone DFT coursework after the SCF implementation Scene on the capstone path** — "
            "read [preface row 158](../preface.md#skill-navigation-row-158), the "
            "[Row 68 → Row 138 reunion index](../appendix/sources.md#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158), and "
            "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) before row 59 Handshake 3 meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 157 closing stitch", stitch + "**Row 157 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 158 compass/preview/stitch")


def lift_118_section_to_158(s: str) -> str:
    p = [
        ("row 118", "row 158"),
        ("Row 118", "Row 158"),
        (
            "row68-row98-dft-workflows-meta-capstone-reunion-index-row-118",
            "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
        ),
        (
            "Row 68 → Row 98 Row 68 → Row 58 DFT workflows meta capstone",
            "Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
        ),
        (
            "DFT workflows meta capstone reunion index (row 118)",
            "DFT workflows meta prelude capstone reunion index (row 158)",
        ),
        ("DFT workflows meta capstone reunion**", "DFT workflows meta prelude capstone reunion**"),
        ("DFT workflows meta capstone boundary", "DFT workflows meta prelude capstone boundary"),
        ("Kohn–Sham meta capstone", "Kohn–Sham meta prelude capstone"),
        ("row 117", "row 157"),
        ("Row 117", "Row 157"),
        ("row 137", "row 157"),
        ("Row 137", "Row 157"),
        ("row 98", "row 138"),
        ("Row 98", "Row 138"),
        ("skill-navigation-row-158", "skill-navigation-row-158"),
        (
            "row-118-baby-picture",
            "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion",
        ),
        (
            "row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion",
            "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion",
        ),
        (
            "before row 59 Handshake 3 meta capstone opens",
            "before row 59 Handshake 3 meta prelude opens on the capstone path",
        ),
        ("Preface row 118", "Preface row 158"),
        ("memory sheet row 118 baby picture", "memory sheet row 158 baby picture"),
    ]
    return tx(s, p)


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158"
    if idx_key in text:
        print("sources: row 158 already present")
        return
    block = lift_138_to_158(
        extract_between(
            text,
            "## Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone reunion index (row 138)",
            "## Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion index (row 139)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)",
        f"## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 158 | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone "
        "(midpoint prelude gate ↔ Kohn–Sham meta prelude capstone ↔ row 58 meta) | "
        f"[Row 68 → Row 138 DFT workflows meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 158](../preface.md#skill-navigation-row-158) · "
        "[prologue row 158 preview](../prologue/00-many-scales.md#prologue-preview-row-158) · "
        "[prologue row 158 closing stitch](../prologue/00-many-scales.md#row-158-closing-stitch) · "
        "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) · "
        "[memory sheet row 158 baby picture](memory-sheet.md#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 58 IX.2 → IX.3 opening hinge still feels disconnected from verified Kohn–Sham meta prelude capstone on the capstone path** — "
        "read row 68 + row 157 or row 138 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
        "[preface row 58](../preface.md#skill-navigation-row-58) |\n"
    )
    text = text.replace(
        "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        table_row + "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157)",
        block + "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157)",
    )
    path.write_text(text)
    print("sources: added row 158")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-158-baby-picture" in text:
        print("memory-sheet: row 158 already present")
        return
    baby = lift_138_to_158(
        extract_between(text, "### Row 138 baby picture", "### Row 139 baby picture")
    )
    text = text.replace("### Row 139 baby picture", baby + "### Row 139 baby picture", 1)
    mem_table = (
        "| 158 | Meta | Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion | "
        "[Row 68 → Row 138 DFT workflows meta prelude capstone reunion index](sources.md#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158) · "
        "[preface row 158 skill checkpoint](../preface.md#skill-navigation-row-158) · "
        "[prologue row 158 preview](../prologue/00-many-scales.md#prologue-preview-row-158) · "
        "[prologue row 158 closing stitch](../prologue/00-many-scales.md#row-158-closing-stitch) · "
        "[epilogue row 158 closing loop](../epilogue/multiscale.md#row-158-closing-loop) | "
        "Row 68 closed but row 58 IX.2 → IX.3 opening hinge feels disconnected from verified Kohn–Sham meta prelude capstone on the capstone path — "
        "read row 68 + row 157 or row 138 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
        "[row 158 baby picture](#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 157 | Meta | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion |",
        mem_table + "| 157 | Meta | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion |",
    )
    switch = (
        "When row 157 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 158](#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion)."
    )
    if "When row 157 closed but DFT workflows meta reunion still lags" not in text:
        text = text.replace(
            "When row 156 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 157](#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion).",
            "When row 156 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 157](#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 158")


def fix_preface_row158() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m138 = re.search(
        r"(### Row 138 skill checkpoint.*?)(?=\n### Row 139 skill checkpoint)",
        text,
        re.S,
    )
    if not m138:
        raise SystemExit("row 138 preface checkpoint missing")
    block158 = lift_138_to_158(m138.group(1))
    start = text.find("### Row 158 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block158 + text[end:]
        path.write_text(text)
        print("preface: repaired row 158")


def fix_epilogue_row158() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-158-closing-loop" not in text:
        return
    block138 = extract_between(
        text, "### Row 138 closing loop", "### Row 119 closing loop"
    )
    block158 = lift_138_to_158(block138)
    start = text.find("### Row 158 closing loop")
    end = text.find("\n### Row 157 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block158 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 158 loop")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row158()
    insert_epilogue_loop()
    fix_epilogue_row158()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
