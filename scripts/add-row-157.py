#!/usr/bin/env python3
"""Add row 157 (Kohn–Sham meta prelude capstone reunion) from row 137 baseline."""
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


def lift_137_to_157(s: str) -> str:
    s = s.replace("Row 68 → Row 117", "__ROW68ROW137__")
    s = s.replace(
        "Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta capstone",
        "__ROW157TITLE__",
    )
    p = [
        ("skill-navigation-row-136", "skill-navigation-row-156"),
        ("skill-navigation-row-117", "skill-navigation-row-137"),
        ("skill-navigation-row-137", "skill-navigation-row-157"),
        ("### Row 137 skill checkpoint", "### Row 157 skill checkpoint"),
        ("Row 137 does not replace", "Row 157 does not replace"),
        ("Row 137 three-way audit", "Row 157 three-way audit"),
        ("Row 137 closing loop", "Row 157 closing loop"),
        ("row-137-closing-loop", "row-157-closing-loop"),
        ("Row 137 closing stitch", "Row 157 closing stitch"),
        ("row-137-closing-stitch", "row-157-closing-stitch"),
        ("prologue-preview-row-137", "prologue-preview-row-157"),
        ("Row 137 preview", "Row 157 preview"),
        ("Row 137 skill checkpoint", "Row 157 skill checkpoint"),
        ("memory sheet row 137", "memory sheet row 157"),
        ("Row 137 baby picture", "Row 157 baby picture"),
        (
            "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137",
            "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
        ),
        (
            "row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion",
            "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
        ),
        ("[row 138]", "__ROW138__"),
        ("[row 137]", "[row 157]"),
        ("row 137", "row 157"),
        ("Row 137", "Row 157"),
        ("__ROW138__", "[row 138]"),
        ("[row 136]", "[row 156]"),
        ("row 136", "row 156"),
        ("Row 136", "Row 156"),
        ("[row 117]", "[row 137]"),
        ("row 117", "row 137"),
        ("Row 117", "Row 137"),
        (
            "Row 68 → Row 117 Kohn–Sham meta capstone reunion index (row 137)",
            "Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index (row 157)",
        ),
        (
            "verified Born–Oppenheimer meta capstone closure (row 136)",
            "verified Born–Oppenheimer meta prelude capstone closure (row 156)",
        ),
        ("when row 136 closed but row 57", "when row 156 closed but row 57"),
        ("when row 136 and row 57", "when row 156 and row 57"),
        (
            "rear-view mirror of row 136's BO/HK → SCF fixed-point turn",
            "rear-view mirror of row 156's BO/HK → SCF fixed-point turn",
        ),
        (
            "when opening [row 118](preface.md#skill-navigation-row-118) before row 58 closes on the capstone path",
            "when opening [row 158](preface.md#skill-navigation-row-158) before row 58 closes on the capstone path",
        ),
        (
            "When row 137 is complete, proceed to [row 138]",
            "When row 157 is complete, proceed to [row 138]",
        ),
        (
            "When row 57 feels like quantum chemistry homework after row 136 alone on the capstone path",
            "When row 57 feels like quantum chemistry homework after row 156 alone on the capstone path",
        ),
        (
            "row 157 (row 68 ↔ row 57 reunion on the capstone path) with row 137",
            "row 157 (row 68 ↔ row 57 reunion on the capstone path) with row 137",
        ),
        (
            "row 137 names **why that reunion must follow verified Born–Oppenheimer meta capstone (row 136)",
            "row 157 names **why that reunion must follow verified Born–Oppenheimer meta prelude capstone (row 156)",
        ),
        ("Row 68 → Row 57 meta (row 137)", "Row 68 → Row 57 meta (row 157)"),
        ("Row 68 → Row 117 reunion index", "Row 68 → Row 137 reunion index"),
        (
            "Proceed to [row 138](#row-137-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 137 on the capstone path",
            "Proceed to [row 158](#row-157-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 157 on the capstone path, "
            "to [row 138](#row-138-closing-loop) when row 68 closed but DFT workflows meta capstone still lags after row 137 on the opening-hinge path, "
            "to [row 137](#row-137-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136 on the opening-hinge path",
        ),
        ("before the DFT workflows meta reunion", "before the DFT workflows meta prelude capstone reunion"),
        ("Recite [preface row 136]", "Recite [preface row 156]"),
        ("Kohn–Sham meta capstone reunion", "Kohn–Sham meta prelude capstone reunion"),
        ("Kohn–Sham meta capstone at the", "Kohn–Sham meta prelude capstone at the"),
        ("before Kohn–Sham meta capstone", "before Kohn–Sham meta prelude capstone"),
        ("Kohn–Sham meta capstone for index-card", "Kohn–Sham meta prelude capstone for index-card"),
        (
            "it names the dual reunion before the cutoff-sweep Lab act",
            "it names the dual reunion before the DFT workflows meta prelude capstone reunion",
        ),
        (
            "when `murnaghan_eos.yaml` exists on the capstone path but the inner SCF loop at each volume point is unnamed after row 136",
            "when `murnaghan_eos.yaml` exists on the capstone path but the inner SCF loop at each volume point is unnamed after row 156",
        ),
        (
            "when row 136 closed but row 57 IX.1 → IX.2 reunion still feels like quantum chemistry homework disconnected from verified Born–Oppenheimer meta capstone on the capstone path",
            "when row 156 closed but row 57 IX.1 → IX.2 reunion still feels like quantum chemistry homework disconnected from verified Born–Oppenheimer meta prelude capstone on the capstone path",
        ),
        (
            "Row 68 → Row 57 meta (row 157) must read as one Murnaghan scan",
            "Row 68 → Row 57 meta (row 157) must read as one Murnaghan scan",
        ),
        (
            "Do not conflate row 137 (row 68 ↔ row 57 reunion on the capstone path) with row 117",
            "Do not conflate row 157 (row 68 ↔ row 57 reunion on the capstone path) with row 137",
        ),
        (
            "row 117 names **Row 68 → Row 77 Row 68 → Row 57 Kohn–Sham meta prelude reunion**; row 137 names",
            "row 137 names **Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion**; row 157 names",
        ),
        ("Born–Oppenheimer meta capstone / Kohn–Sham opening gate", "Born–Oppenheimer meta prelude capstone / Kohn–Sham opening gate"),
        ("Born–Oppenheimer meta capstone / Kohn–Sham opening prelude hinge", "Born–Oppenheimer meta prelude capstone / Kohn–Sham opening prelude hinge"),
        ("Born–Oppenheimer meta capstone and IX.1 → IX.2", "Born–Oppenheimer meta prelude capstone and IX.1 → IX.2"),
        ("verified Born–Oppenheimer meta capstone closure", "verified Born–Oppenheimer meta prelude capstone closure"),
        ("Born–Oppenheimer meta capstone boundary", "Born–Oppenheimer meta prelude capstone boundary"),
        ("Name Born–Oppenheimer meta capstone before IX.1 Bridge", "Name Born–Oppenheimer meta prelude capstone before IX.1 Bridge"),
        ("Midpoint Bridge chain recited before Kohn–Sham meta capstone", "Midpoint Bridge chain recited before Kohn–Sham meta prelude capstone"),
        ("Name row 68 closed before Kohn–Sham meta capstone", "Name row 68 closed before Kohn–Sham meta prelude capstone"),
        (
            "When row 157 is complete, proceed to [row 138](preface.md#skill-navigation-row-138) when cutoff certificates exist on the capstone path but IX.3 still lags, to [row 118](preface.md#skill-navigation-row-118) when Kohn–Sham meta capstone is clean but DFT workflows meta capstone still lags on the opening-hinge path, to [row 98](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge path alone, to [row 136](preface.md#skill-navigation-row-136) when Born–Oppenheimer meta capstone still lags after verified electronic audit meta prelude capstone on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
            "When row 157 is complete, proceed to [row 158](preface.md#skill-navigation-row-158) when cutoff certificates exist on the capstone path but IX.3 still lags, to [row 138](preface.md#skill-navigation-row-138) when Kohn–Sham meta capstone is clean but DFT workflows meta capstone still lags on the opening-hinge path, to [row 98](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 137](preface.md#skill-navigation-row-137) for the Row 68 ↔ Row 57 Kohn–Sham meta audit on the opening-hinge path alone, to [row 156](preface.md#skill-navigation-row-156) when Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW68ROW137__", "Row 68 → Row 137")
    s = s.replace(
        "__ROW157TITLE__",
        "Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
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
    if "### Row 157 skill checkpoint" in text:
        print("preface: row 157 already present")
        return
    m = re.search(
        r"(### Row 137 skill checkpoint.*?)(?=\n### Row 138 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 137 checkpoint missing")
    block = lift_137_to_157(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    text = text.replace(
        "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags after verified Murnaghan archive on the capstone path, to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-97) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags after verified Murnaghan archive on the capstone path, to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-97) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        1,
    )
    path.write_text(text)
    print("preface: added row 157")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-157-closing-loop" in text:
        print("epilogue: row 157 loop already present")
        return
    block = lift_137_to_157(
        extract_between(
            text,
            "### Row 137 closing loop",
            "### Row 136 closing loop",
        )
    )
    needle = "### Row 156 closing loop"
    if needle not in text:
        needle = "### Row 136 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 157 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    after = "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |"
    if "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |" in text:
        print("prologue: row 157 compass already present")
    else:
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 156 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion (row 137) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 137 compass missing")
        new_line = lift_137_to_157(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-137"></span>'
    preview_dst = '| <span id="prologue-preview-row-157"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_137_to_157(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 157 closing stitch" not in text:
        stitch = (
            "**Row 157 closing stitch (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-157-closing-stitch} "
            "When row 156 closed — Born–Oppenheimer meta prelude capstone verified, row 155 or row 136 recited on the capstone path, and IX.0 Bridge → IX.1 BO/HK recited with "
            "[Murnaghan Lab act](../part09-dft/01-born-oppenheimer.md#lab-act-murnaghan-fit-on-fcc-cu-act-vi--foundation) archived `murnaghan_eos.yaml` — but **row 57 IX.1 → IX.2 opening hinge still opens like standalone quantum chemistry homework after the BO/HK Scene on the capstone path** — "
            "read [preface row 157](../preface.md#skill-navigation-row-157), the "
            "[Row 68 → Row 137 reunion index](../appendix/sources.md#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157), and "
            "[epilogue row 157 closing loop](../epilogue/multiscale.md#row-157-closing-loop) before row 58 DFT workflows meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 156 closing stitch", stitch + "**Row 156 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 157 compass/preview/stitch")


def lift_117_section_to_157(s: str) -> str:
    p = [
        ("row 117", "row 157"),
        ("Row 117", "Row 157"),
        (
            "row68-row97-kohn-sham-meta-capstone-reunion-index-row-117",
            "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
        ),
        (
            "Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone",
            "Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        ),
        (
            "Kohn–Sham meta capstone reunion index (row 117)",
            "Kohn–Sham meta prelude capstone reunion index (row 157)",
        ),
        ("Kohn–Sham meta capstone reunion**", "Kohn–Sham meta prelude capstone reunion**"),
        ("Kohn–Sham meta capstone boundary", "Kohn–Sham meta prelude capstone boundary"),
        ("Born–Oppenheimer meta capstone", "Born–Oppenheimer meta prelude capstone"),
        ("row 116", "row 156"),
        ("Row 116", "Row 156"),
        ("row 136", "row 156"),
        ("Row 136", "Row 156"),
        ("skill-navigation-row-157", "skill-navigation-row-157"),
        (
            "row-117-baby-picture",
            "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
        ),
        (
            "row-137-baby-picture-row68-row117-kohn-sham-meta-capstone-reunion",
            "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
        ),
        ("before row 58 DFT workflows meta capstone opens", "before row 58 DFT workflows meta prelude opens on the capstone path"),
        ("Preface row 117", "Preface row 157"),
        ("memory sheet row 117 baby picture", "memory sheet row 157 baby picture"),
    ]
    return tx(s, p)


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157"
    if idx_key in text:
        print("sources: row 157 already present")
        return
    block = lift_137_to_157(
        extract_between(
            text,
            "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 137)",
            "## Row 68 → Row 97 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 117)",
        )
    )
    block = block.replace(
        "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157)",
        f"## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 157 | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone "
        "(midpoint prelude gate ↔ Born–Oppenheimer meta prelude capstone ↔ row 57 meta) | "
        f"[Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 157](../preface.md#skill-navigation-row-157) · "
        "[prologue row 157 preview](../prologue/00-many-scales.md#prologue-preview-row-157) · "
        "[prologue row 157 closing stitch](../prologue/00-many-scales.md#row-157-closing-stitch) · "
        "[epilogue row 157 closing loop](../epilogue/multiscale.md#row-157-closing-loop) · "
        "[memory sheet row 157 baby picture](memory-sheet.md#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 57 IX.1 → IX.2 opening hinge still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the capstone path** — "
        "read row 68 + row 156 or row 137 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[preface row 57](../preface.md#skill-navigation-row-57) |\n"
    )
    text = text.replace(
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        table_row + "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        block + "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
    )
    path.write_text(text)
    print("sources: added row 157")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-157-baby-picture" in text:
        print("memory-sheet: row 157 already present")
        return
    baby = lift_137_to_157(
        extract_between(text, "### Row 137 baby picture", "### Row 136 baby picture")
    )
    text = text.replace("### Row 136 baby picture", baby + "### Row 136 baby picture", 1)
    mem_table = (
        "| 157 | Meta | Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion | "
        "[Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index](sources.md#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157) · "
        "[preface row 157 skill checkpoint](../preface.md#skill-navigation-row-157) · "
        "[prologue row 157 preview](../prologue/00-many-scales.md#prologue-preview-row-157) · "
        "[prologue row 157 closing stitch](../prologue/00-many-scales.md#row-157-closing-stitch) · "
        "[epilogue row 157 closing loop](../epilogue/multiscale.md#row-157-closing-loop) | "
        "Row 68 closed but row 57 IX.1 → IX.2 opening hinge feels disconnected from verified Born–Oppenheimer meta prelude capstone on the capstone path — "
        "read row 68 + row 156 or row 137 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[row 157 baby picture](#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion |",
        mem_table + "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion |",
    )
    switch = (
        "When row 156 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 157](#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion)."
    )
    if "When row 156 closed but Kohn–Sham meta reunion still lags" not in text:
        text = text.replace(
            "When row 155 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion).",
            "When row 155 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 157")


def fix_preface_row157() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m137 = re.search(
        r"(### Row 137 skill checkpoint.*?)(?=\n### Row 138 skill checkpoint)",
        text,
        re.S,
    )
    if not m137:
        raise SystemExit("row 137 preface checkpoint missing")
    block157 = lift_137_to_157(m137.group(1))
    start = text.find("### Row 157 skill checkpoint")
    end = text.find("\n## The copper wire through the book", start)
    if start >= 0 and end > start:
        text = text[:start] + block157 + text[end:]
        path.write_text(text)
        print("preface: repaired row 157")


def fix_epilogue_row157() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-157-closing-loop" not in text:
        return
    block137 = extract_between(
        text, "### Row 137 closing loop", "### Row 136 closing loop"
    )
    block157 = lift_137_to_157(block137)
    start = text.find("### Row 157 closing loop")
    end = text.find("\n### Row 156 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block157 + text[end:]
        path.write_text(text)
        print("epilogue: repaired row 157 loop")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    fix_preface_row157()
    insert_epilogue_loop()
    fix_epilogue_row157()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
