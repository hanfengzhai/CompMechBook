#!/usr/bin/env python3
"""Add row 177 (Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone on capstone path)."""
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


LIFT_157_TO_177_PAIRS: list[tuple[str, str]] = [
    ("Row 158 closing loop", "__PH158_LOOP__"),
    ("Row 157 closing loop", "Row 177 closing loop"),
    ("row-158-closing-loop", "__PH158_LOOP_ANCHOR__"),
    ("row-157-closing-loop", "row-177-closing-loop"),
    ("Row 158 closing stitch", "__PH158_STITCH__"),
    ("Row 157 closing stitch", "Row 177 closing stitch"),
    ("row-158-closing-stitch", "__PH158_STITCH_ANCHOR__"),
    ("row-157-closing-stitch", "row-177-closing-stitch"),
    ("prologue-preview-row-158", "__PH158_PREVIEW__"),
    ("prologue-preview-row-157", "prologue-preview-row-177"),
    ("Row 158 preview", "__PH158_PREVIEW_TEXT__"),
    ("Row 157 preview", "Row 177 preview"),
    ("Row 158 skill checkpoint", "__PH158_SKILL__"),
    ("Row 157 skill checkpoint", "Row 177 skill checkpoint"),
    ("skill-navigation-row-158", "__PH158_SKILL_NAV__"),
    ("skill-navigation-row-157", "skill-navigation-row-177"),
    ("memory sheet row 158", "__PH158_MEM__"),
    ("memory sheet row 157", "memory sheet row 177"),
    ("Row 158 baby picture", "__PH158_BABY__"),
    ("Row 157 baby picture", "Row 177 baby picture"),
    ("Row 158 three-way audit", "__PH158_AUDIT__"),
    ("Row 157 three-way audit", "Row 177 three-way audit"),
    (
        "Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
    ),
    (
        "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
        "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
    ),
    (
        "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
        "row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion",
    ),
    ("[row 158]", "__ROW158_REF__"),
    ("[row 137]", "[row 157]"),
    ("row 137", "row 157"),
    ("Row 137", "Row 157"),
    ("__ROW158_REF__", "[row 158]"),
    ("[row 156]", "__ROW176_GATE__"),
    ("row 156", "__row176_gate__"),
    ("Row 156", "__ROW176_GATE_CAP__"),
    (
        "Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index (row 157)",
        "Row 68 → Row 151 Kohn–Sham meta prelude capstone reunion index (row 177)",
    ),
    (
        "row68-row117-kohn-sham-meta-capstone-reunion-index-row-137",
        "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
    ),
    (
        "verified Born–Oppenheimer meta prelude capstone closure (row 156)",
        "verified Born–Oppenheimer meta prelude capstone closure (row 176)",
    ),
    ("when row 156 closed but row 57", "when row 176 closed but row 57"),
    ("after row 156.", "after row 176."),
    ("when row 156 and row 57", "when row 176 and row 57"),
    (
        "rear-view mirror of row 156's BO/HK → SCF fixed-point turn",
        "rear-view mirror of row 176's BO/HK → SCF fixed-point turn",
    ),
    (
        "when opening [row 158](preface.md#skill-navigation-row-158) before row 58 closes on the capstone path",
        "when opening [row 177](preface.md#skill-navigation-row-177) before row 58 closes on the capstone path",
    ),
    (
        "When row 157 is complete, proceed to [row 158]",
        "When row 177 is complete, proceed to [row 158]",
    ),
    (
        "Proceed to [row 158](#row-157-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 157 on the capstone path",
        "Proceed to [row 177](#row-177-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 176 on the capstone path, "
        "to [row 157](#row-157-closing-loop) when row 68 closed but Kohn–Sham meta prelude still lags on the opening-hinge path",
    ),
    (
        "When row 57 feels like quantum chemistry homework after row 156 alone on the capstone path",
        "When row 57 feels like quantum chemistry homework after row 176 alone on the capstone path",
    ),
    (
        "row 157 (row 68 ↔ row 57 reunion on the capstone path) with row 137",
        "row 177 (row 68 ↔ row 57 reunion on the capstone path) with row 157",
    ),
    (
        "row 157 names **why that reunion must follow verified Born–Oppenheimer meta prelude capstone (row 156)",
        "row 177 names **why that reunion must follow verified Born–Oppenheimer meta prelude capstone (row 176)",
    ),
    ("Row 68 → Row 57 meta (row 137)", "Row 68 → Row 57 meta (row 157)"),
    (
        "Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index (row 157)",
        "Row 68 → Row 151 Kohn–Sham meta prelude capstone reunion index (row 177)",
    ),
    ("Row 68 → Row 137 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 157)", "(row 177)"),
    ("Row 157 closes the", "Row 177 closes the"),
    ("Row 157 does not conflate", "Row 177 does not conflate"),
    ("Row 157 does not replace", "Row 177 does not replace"),
    ("__PH158_LOOP__", "Row 158 closing loop"),
    ("__PH158_LOOP_ANCHOR__", "row-158-closing-loop"),
    ("__PH158_STITCH__", "Row 158 closing stitch"),
    ("__PH158_STITCH_ANCHOR__", "row-158-closing-stitch"),
    ("__PH158_PREVIEW__", "prologue-preview-row-158"),
    ("__PH158_PREVIEW_TEXT__", "Row 158 preview"),
    ("__PH158_SKILL__", "Row 158 skill checkpoint"),
    ("__PH158_SKILL_NAV__", "skill-navigation-row-158"),
    ("__PH158_MEM__", "memory sheet row 158"),
    ("__PH158_BABY__", "Row 158 baby picture"),
    ("__PH158_AUDIT__", "Row 158 three-way audit"),
    ("__ROW176_GATE__", "[row 176]"),
    ("__row176_gate__", "row 176"),
    ("__ROW176_GATE_CAP__", "Row 176"),
]


def lift_157_to_177(s: str) -> str:
    out = tx(s, LIFT_157_TO_177_PAIRS)
    out = out.replace(
        "[row 176](preface.md#skill-navigation-row-156)",
        "[row 176](preface.md#skill-navigation-row-176)",
    )
    out = out.replace(
        "[row 157](preface.md#skill-navigation-row-137)",
        "[row 157](preface.md#skill-navigation-row-157)",
    )
    out = re.sub(
        r"(### Row 177 skill checkpoint[^\n]*)\{#skill-navigation-row-157\}",
        r"\1{#skill-navigation-row-177}",
        out,
        count=1,
    )
    return out


def export_index_to_kohn_sham_177(block: str) -> str:
    """Turn a lifted Born–Oppenheimer capstone index (176-shaped) into Kohn–Sham capstone 177."""
    pairs = [
        (
            "Born–Oppenheimer meta prelude capstone reunion index (row 176)",
            "Kohn–Sham meta prelude capstone reunion index (row 177)",
        ),
        (
            "Born–Oppenheimer meta prelude capstone reunion index (row 177)",
            "Kohn–Sham meta prelude capstone reunion index (row 177)",
        ),
        ("Row 68 → Row 56", "Row 68 → Row 57"),
        ("row 56", "row 57"),
        ("electronic audit meta prelude capstone", "Born–Oppenheimer meta prelude capstone"),
        ("row 175", "row 176"),
        (
            "row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
            "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
        ),
        ("IX.0 Bridge", "IX.1 Bridge"),
        (
            "IX.1 opening hinge from IX.0",
            "IX.2 opening hinge from IX.1",
        ),
        ("IX.1 BO/HK vocabulary audit", "IX.2 Kohn–Sham SCF vocabulary audit"),
        (
            "ix0-ix1-opening-hinge-reunion-index-row-56",
            "ix1-ix2-opening-hinge-reunion-index-row-57",
        ),
        ("foundation SCF audit Lab act steps 1–6", "Murnaghan Lab act steps 1–5"),
        ("`cu.relax.out`", "`murnaghan_eos.yaml`"),
        (
            "Born–Oppenheimer meta prelude capstone reunion",
            "Kohn–Sham meta prelude capstone reunion",
        ),
        ("skill-navigation-row-176", "skill-navigation-row-177"),
        ("row-176-baby-picture", "row-177-baby-picture"),
        ("Row 176", "Row 177"),
        ("row 176", "row 177"),
        ("row 56 Born–Oppenheimer meta prelude", "row 57 Kohn–Sham meta prelude"),
        ("row 57 Kohn–Sham meta prelude", "row 58 DFT workflows meta prelude"),
        ("Born–Oppenheimer meta prelude capstone", "Kohn–Sham meta prelude capstone"),
        ("IX.0 → IX.1", "IX.1 → IX.2"),
        (
            "electronic audit meta prelude capstone boundary",
            "Born–Oppenheimer meta prelude capstone boundary",
        ),
        ("foundation SCF → BO/HK", "BO/HK → Kohn–Sham SCF"),
        (r"\(V_{\text{BO}}\)", r"\(\rho^\star = \mathcal{G}(\rho^\star)\)"),
    ]
    return tx(block, pairs)


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 177 skill checkpoint" in text:
        print("preface: row 177 already present")
        return
    m = re.search(
        r"(### Row 157 skill checkpoint.*?)(?=\n### Row 158 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 157 checkpoint missing")
    block = lift_157_to_177(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 177")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 177 closing loop" in text:
        print("epilogue: row 177 loop already present")
        return
    block = lift_157_to_177(
        extract_between(
            text,
            "### Row 157 closing loop",
            "### Row 156 closing loop",
        )
    )
    needle = "### Row 176 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 177 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 177) |"
    if compass in text:
        print("prologue: row 177 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 176) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 176 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 157 compass missing")
        new_line = lift_157_to_177(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-157"></span>'
    preview_dst = '| <span id="prologue-preview-row-177"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_157_to_177(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 177 closing stitch" not in text:
        stitch = (
            "**Row 177 closing stitch (Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion).** {#row-177-closing-stitch} "
            "When row 176 closed — Born–Oppenheimer meta prelude capstone verified, row 176 or row 156 recited on the capstone path, and IX.0 Bridge → IX.1 BO/HK recited with "
            "[Murnaghan Lab act](../part09-dft/01-born-oppenheimer.md#lab-act-murnaghan-fit-on-fcc-cu-act-vi--foundation) archived `murnaghan_eos.yaml` — but **row 57 IX.1 → IX.2 opening hinge still opens like standalone quantum chemistry homework after the BO/HK Scene on the capstone path** — "
            "the [preface row 177 When-to-pause opening sentence](../preface.md#skill-navigation-row-177) names the dual reunion before the DFT workflows meta prelude capstone reunion; "
            "read [preface row 177](../preface.md#skill-navigation-row-177), then the "
            "[Row 68 → Row 151 Kohn–Sham reunion index](../appendix/sources.md#row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177), then "
            "[epilogue row 177 closing loop](../epilogue/multiscale.md#row-177-closing-loop) before row 58 DFT workflows meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 176 closing stitch", stitch + "**Row 176 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 177 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177"
    if idx_key in text:
        print("sources: row 177 already present")
        return
    start176 = "## Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)"
    i = text.find(start176)
    if i < 0:
        raise SystemExit("sources row 176 index missing")
    end175 = "## Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)"
    j175 = text.find(end175, i)
    if j175 < 0:
        j175 = text.find("\n## Row 68 → Row 151 Row 68 → Row 54", i)
    block = export_index_to_kohn_sham_177(lift_157_to_177(text[i:j175]))
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)",
        f"## Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 177 | Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone (midpoint prelude gate ↔ Born–Oppenheimer meta prelude capstone ↔ row 57 meta) | "
        f"[Row 68 → Row 151 Kohn–Sham meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 177](../preface.md#skill-navigation-row-177) · "
        "[prologue row 177 preview](../prologue/00-many-scales.md#prologue-preview-row-177) · "
        "[prologue row 177 closing stitch](../prologue/00-many-scales.md#row-177-closing-stitch) · "
        "[epilogue row 177 closing loop](../epilogue/multiscale.md#row-177-closing-loop) · "
        "[memory sheet row 177 baby picture](memory-sheet.md#row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 57 IX.1 → IX.2 opening hinge still feels disconnected from verified Born–Oppenheimer meta prelude capstone on the capstone path** — "
        "read row 68 + row 176 or row 157 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[preface row 57](../preface.md#skill-navigation-row-57) |\n"
    )
    text = text.replace(
        "| 176 | Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        table_row + "| 176 | Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
    )
    text = text.replace(start176, block + start176, 1)
    extra = (
        f"[row 177](#{idx_key}) reunites **Born–Oppenheimer meta prelude capstone with the Kohn–Sham meta prelude capstone boundary** "
        "when row 176 closed Born–Oppenheimer meta prelude capstone at verified IX.0 → IX.1 closure on the capstone path but IX.1 Bridge and row 57 still read like separate courses;"
    )
    needle = (
        "[row 176](#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176) reunites **electronic audit meta prelude capstone with the Born–Oppenheimer meta prelude capstone boundary** "
    )
    if extra not in text and needle in text:
        text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 177")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 177 already present")
        return
    baby = lift_157_to_177(
        extract_between(
            text,
            "### Row 157 baby picture",
            "### Row 137 baby picture",
        )
    )
    anchor = "### Row 157 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 177 | Meta | Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion | "
        "[Row 68 → Row 151 Kohn–Sham meta prelude capstone reunion index](sources.md#row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177) · "
        "[preface row 177 skill checkpoint](../preface.md#skill-navigation-row-177) · "
        "[prologue row 177 preview](../prologue/00-many-scales.md#prologue-preview-row-177) · "
        "[prologue row 177 closing stitch](../prologue/00-many-scales.md#row-177-closing-stitch) · "
        "[epilogue row 177 closing loop](../epilogue/multiscale.md#row-177-closing-loop) | "
        "Row 68 closed but row 57 IX.1 → IX.2 opening hinge feels disconnected from verified Born–Oppenheimer meta prelude capstone on the capstone path — "
        "read row 68 + row 176 or row 157 gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57; "
        "[row 177 baby picture](#row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 176 | Meta | Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion |",
        mem_table + "| 176 | Meta | Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion |",
    )
    if "When row 176 closed but Kohn–Sham meta reunion still lags" not in text:
        text = text.replace(
            "When row 175 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 176](#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion).",
            "When row 175 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 176](#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion). "
            "When row 176 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 177](#row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 177")


def patch_row_176_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 177](preface.md#skill-navigation-row-157)",
        "proceed to [row 177](preface.md#skill-navigation-row-177)",
    )
    text = text.replace(
        "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes",
        "when opening [row 177](preface.md#skill-navigation-row-177) before row 58 closes",
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 177](preface.md#skill-navigation-row-157)",
        "proceed to [row 177](preface.md#skill-navigation-row-177)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 176 → row 177 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_176_proceed_links()


if __name__ == "__main__":
    main()
