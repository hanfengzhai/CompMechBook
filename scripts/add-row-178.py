#!/usr/bin/env python3
"""Add row 178 (Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone on capstone path) meta prelude capstone on capstone path)."""
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


LIFT_158_TO_178_PAIRS: list[tuple[str, str]] = [
    ("Row 159 closing loop", "__PH159_LOOP__"),
    ("Row 158 closing loop", "Row 178 closing loop"),
    ("row-159-closing-loop", "__PH159_LOOP_ANCHOR__"),
    ("row-158-closing-loop", "row-178-closing-loop"),
    ("Row 159 closing stitch", "__PH159_STITCH__"),
    ("Row 158 closing stitch", "Row 178 closing stitch"),
    ("row-159-closing-stitch", "__PH159_STITCH_ANCHOR__"),
    ("row-158-closing-stitch", "row-178-closing-stitch"),
    ("prologue-preview-row-159", "__PH159_PREVIEW__"),
    ("prologue-preview-row-158", "prologue-preview-row-178"),
    ("Row 159 preview", "__PH159_PREVIEW_TEXT__"),
    ("Row 158 preview", "Row 178 preview"),
    ("Row 159 skill checkpoint", "__PH159_SKILL__"),
    ("Row 158 skill checkpoint", "Row 178 skill checkpoint"),
    ("skill-navigation-row-159", "__PH159_SKILL_NAV__"),
    ("skill-navigation-row-158", "skill-navigation-row-178"),
    ("memory sheet row 159", "__PH159_MEM__"),
    ("memory sheet row 158", "memory sheet row 178"),
    ("Row 159 baby picture", "__PH159_BABY__"),
    ("Row 158 baby picture", "Row 178 baby picture"),
    ("Row 159 three-way audit", "__PH159_AUDIT__"),
    ("Row 158 three-way audit", "Row 178 three-way audit"),
    (
        "Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone",
    ),
    (
        "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
        "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
    ),
    (
        "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion",
        "row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion",
    ),
    ("[row 159]", "__ROW159_REF__"),
    ("[row 138]", "[row 158]"),
    ("row 138", "row 158"),
    ("Row 138", "Row 158"),
    ("__ROW159_REF__", "[row 159]"),
    ("[row 157]", "__ROW177_GATE__"),
    ("row 157", "__row177_gate__"),
    ("Row 157", "__ROW177_GATE_CAP__"),
    (
        "Row 68 → Row 138 DFT workflows meta prelude capstone reunion index (row 158)",
        "Row 68 → Row 151 DFT workflows meta prelude capstone reunion index (row 178)",
    ),
    (
        "row68-row118-dft-workflows-meta-capstone-reunion-index-row-138",
        "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
    ),
    (
        "verified Kohn–Sham meta prelude capstone closure (row 157)",
        "verified Kohn–Sham meta prelude capstone closure (row 178)",
    ),
    ("when row 157 closed but row 58", "when row 177 closed but row 58"),
    ("after row 157.", "after row 177."),
    ("when row 157 and row 58", "when row 177 and row 58"),
    (
        "rear-view mirror of row 157's SCF fixed-point → calculation ladder turn",
        "rear-view mirror of row 177's SCF fixed-point → calculation ladder turn",
    ),
    (
        "when opening [row 159](preface.md#skill-navigation-row-159) before row 59 closes on the capstone path",
        "when opening [row 178](preface.md#skill-navigation-row-178) before row 59 closes on the capstone path",
    ),
    (
        "When row 158 is complete, proceed to [row 159]",
        "When row 178 is complete, proceed to [row 159]",
    ),
    (
        "Proceed to [row 159](#row-158-closing-loop) when row 68 closed but Handshake 3 meta prelude capstone still lags after row 158 on the capstone path",
        "Proceed to [row 178](#row-178-closing-loop) when row 68 closed but DFT workflows meta prelude capstone still lags after row 177 on the capstone path, "
        "to [row 158](#row-158-closing-loop) when row 68 closed but DFT workflows meta prelude still lags on the opening-hinge path",
    ),
    (
        "When row 58 feels like DFT coursework after row 157 alone on the capstone path",
        "When row 58 feels like DFT coursework after row 177 alone on the capstone path",
    ),
    (
        "row 158 (row 68 ↔ row 58 reunion on the capstone path) with row 138",
        "row 178 (row 68 ↔ row 58 reunion on the capstone path) with row 158",
    ),
    (
        "row 158 names **why that reunion must follow verified Kohn–Sham meta prelude capstone (row 157)",
        "row 178 names **why that reunion must follow verified Kohn–Sham meta prelude capstone (row 178)",
    ),
    ("Row 68 → Row 58 meta (row 138)", "Row 68 → Row 58 meta (row 158)"),
    (
        "Row 68 → Row 138 DFT workflows meta prelude capstone reunion index (row 158)",
        "Row 68 → Row 151 DFT workflows meta prelude capstone reunion index (row 178)",
    ),
    ("Row 68 → Row 138 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 158)", "(row 178)"),
    ("Row 158 closes the", "Row 178 closes the"),
    ("Row 158 does not conflate", "Row 178 does not conflate"),
    ("Row 158 does not replace", "Row 178 does not replace"),
    ("__PH159_LOOP__", "Row 159 closing loop"),
    ("__PH159_LOOP_ANCHOR__", "row-159-closing-loop"),
    ("__PH159_STITCH__", "Row 159 closing stitch"),
    ("__PH159_STITCH_ANCHOR__", "row-159-closing-stitch"),
    ("__PH159_PREVIEW__", "prologue-preview-row-159"),
    ("__PH159_PREVIEW_TEXT__", "Row 159 preview"),
    ("__PH159_SKILL__", "Row 159 skill checkpoint"),
    ("__PH159_SKILL_NAV__", "skill-navigation-row-159"),
    ("__PH159_MEM__", "memory sheet row 159"),
    ("__PH159_BABY__", "Row 159 baby picture"),
    ("__PH159_AUDIT__", "Row 159 three-way audit"),
    ("__ROW177_GATE__", "[row 177]"),
    ("__row177_gate__", "row 177"),
    ("__ROW177_GATE_CAP__", "Row 177"),
]

def lift_158_to_178(s: str) -> str:
    out = tx(s, LIFT_158_TO_178_PAIRS)
    out = out.replace(
        "[row 177](preface.md#skill-navigation-row-157)",
        "[row 177](preface.md#skill-navigation-row-177)",
    )
    out = out.replace(
        "[row 158](preface.md#skill-navigation-row-138)",
        "[row 158](preface.md#skill-navigation-row-158)",
    )
    out = re.sub(
        r"(### Row 178 skill checkpoint[^\n]*)\{#skill-navigation-row-158\}",
        r"\1{#skill-navigation-row-178}",
        out,
        count=1,
    )
    return out


def export_index_to_dft_workflows_178(block: str) -> str:
    """Turn a lifted Kohn–Sham capstone index (177-shaped) into DFT workflows capstone 178."""
    pairs = [
        (
            "Kohn–Sham meta prelude capstone reunion index (row 177)",
            "DFT workflows meta prelude capstone reunion index (row 178)",
        ),
        (
            "Kohn–Sham meta prelude capstone reunion index (row 178)",
            "DFT workflows meta prelude capstone reunion index (row 178)",
        ),
        ("Row 68 → Row 57", "Row 68 → Row 58"),
        ("row 57", "row 58"),
        ("Born–Oppenheimer meta prelude capstone", "Kohn–Sham meta prelude capstone"),
        ("row 176", "row 177"),
        (
            "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
            "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
        ),
        ("IX.1 Bridge", "IX.2 Bridge"),
        (
            "IX.2 opening hinge from IX.1",
            "IX.3 opening hinge from IX.2",
        ),
        ("IX.2 Kohn–Sham SCF vocabulary audit", "IX.3 calculation ladder vocabulary audit"),
        (
            "ix1-ix2-opening-hinge-reunion-index-row-57",
            "ix2-ix3-opening-hinge-reunion-index-row-58",
        ),
        ("Murnaghan Lab act steps 1–5", "cutoff-sweep Lab act steps 1–5"),
        ("`murnaghan_eos.yaml`", "`cutoff_convergence.yaml`"),
        (
            "Kohn–Sham meta prelude capstone reunion",
            "DFT workflows meta prelude capstone reunion",
        ),
        ("skill-navigation-row-177", "skill-navigation-row-178"),
        ("row-177-baby-picture", "row-178-baby-picture"),
        ("Row 177", "Row 178"),
        ("row 177", "row 178"),
        ("row 57 Kohn–Sham meta prelude", "row 58 DFT workflows meta prelude"),
        ("row 58 DFT workflows meta prelude", "row 59 Handshake 3 meta prelude"),
        ("Kohn–Sham meta prelude capstone", "DFT workflows meta prelude capstone"),
        ("IX.1 → IX.2", "IX.2 → IX.3"),
        (
            "Born–Oppenheimer meta prelude capstone boundary",
            "Kohn–Sham meta prelude capstone boundary",
        ),
        ("BO/HK → Kohn–Sham SCF", "SCF fixed-point → calculation ladder"),
        (r"\(\rho^\star = \mathcal{G}(\rho^\star)\)", "`cu.foundation/`"),
        ("quantum chemistry homework", "DFT coursework"),
    ]
    return tx(block, pairs)



def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 178 skill checkpoint" in text:
        print("preface: row 178 already present")
        return
    m = re.search(
        r"(### Row 158 skill checkpoint.*?)(?=\n### Row 159 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 158 checkpoint missing")
    block = lift_158_to_178(m.group(1))
    anchor = "\n### Row 177 skill checkpoint"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 178")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 178 closing loop" in text:
        print("epilogue: row 178 loop already present")
        return
    block = lift_158_to_178(
        extract_between(
            text,
            "### Row 158 closing loop",
            "### Row 157 closing loop",
        )
    )
    needle = "### Row 177 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 178 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 178) |"
    if compass in text:
        print("prologue: row 178 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 177) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 177 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 158) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 158 compass missing")
        new_line = lift_158_to_178(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-158"></span>'
    preview_dst = '| <span id="prologue-preview-row-178"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_158_to_178(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 178 closing stitch" not in text:
        stitch = (
            "**Row 178 closing stitch (Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion).** {#row-178-closing-stitch} "
            "When row 177 closed — Kohn–Sham meta prelude capstone verified, row 177 or row 157 recited on the capstone path, and IX.1 Bridge → IX.2 SCF recited with "
            "[cutoff-sweep Lab act](../part09-dft/02-kohn-sham.md#lab-act-cutoff-sweep-on-fcc-cu-act-vi--convergence-certificate) archived `cutoff_convergence.yaml` — but **row 58 IX.2 → IX.3 opening hinge still opens like standalone DFT coursework after the SCF implementation Scene on the capstone path** — "
            "the [preface row 178 When-to-pause opening sentence](../preface.md#skill-navigation-row-178) names the dual reunion before the Handshake 3 meta prelude capstone reunion; "
            "read [preface row 178](../preface.md#skill-navigation-row-178), then the "
            "[Row 68 → Row 151 DFT workflows reunion index](../appendix/sources.md#row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178), then "
            "[epilogue row 178 closing loop](../epilogue/multiscale.md#row-178-closing-loop) before row 59 Handshake 3 meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 177 closing stitch", stitch + "**Row 177 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 178 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178"
    if idx_key in text:
        print("sources: row 178 already present")
        return
    start177 = "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177"
    i = text.find(start177)
    if i < 0:
        raise SystemExit("sources row 177 index missing")
    i = text.rfind("\n## ", 0, i)
    end176 = "## Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)"
    j176 = text.find(end176, i)
    if j176 < 0:
        j176 = text.find("\n## Row 68 → Row 151 Row 68 → Row 55", i)
    block = export_index_to_dft_workflows_178(lift_158_to_178(text[i:j176]))
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)",
        f"## Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 178 | Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone "
        "(midpoint prelude gate ↔ Kohn–Sham meta prelude capstone ↔ row 58 meta) | "
        f"[Row 68 → Row 151 DFT workflows meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 178](../preface.md#skill-navigation-row-178) · "
        "[prologue row 178 preview](../prologue/00-many-scales.md#prologue-preview-row-178) · "
        "[prologue row 178 closing stitch](../prologue/00-many-scales.md#row-178-closing-stitch) · "
        "[epilogue row 178 closing loop](../epilogue/multiscale.md#row-178-closing-loop) · "
        "[memory sheet row 178 baby picture](memory-sheet.md#row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 58 IX.2 → IX.3 opening hinge still feels disconnected from verified Kohn–Sham meta prelude capstone on the capstone path** — "
        "read row 68 + row 177 or row 158 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
        "[preface row 58](../preface.md#skill-navigation-row-58) |\n"
    )
    text = text.replace(
        "| 177 | Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
        table_row + "| 177 | Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone",
    )
    text = text.replace(start177, block + start177, 1)
    extra = (
        f"[row 178](#{idx_key}) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta prelude capstone boundary** "
        "when row 177 closed Kohn–Sham meta prelude capstone at verified IX.1 → IX.2 closure on the capstone path but IX.2 Bridge and row 58 still read like separate courses;"
    )
    needle = (
        "[row 176](#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176) reunites **electronic audit meta prelude capstone with the Born–Oppenheimer meta prelude capstone boundary** "
    )
    if extra not in text and needle in text:
        text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 178")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 178 already present")
        return
    baby = lift_158_to_178(
        extract_between(
            text,
            "### Row 158 baby picture",
            "### Row 157 baby picture",
        )
    )
    anchor = "### Row 158 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 178 | Meta | Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion | "
        "[Row 68 → Row 151 DFT workflows meta prelude capstone reunion index](sources.md#row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178) · "
        "[preface row 178 skill checkpoint](../preface.md#skill-navigation-row-178) · "
        "[prologue row 178 preview](../prologue/00-many-scales.md#prologue-preview-row-178) · "
        "[prologue row 178 closing stitch](../prologue/00-many-scales.md#row-178-closing-stitch) · "
        "[epilogue row 178 closing loop](../epilogue/multiscale.md#row-178-closing-loop) | "
        "Row 68 closed but row 58 IX.2 → IX.3 opening hinge feels disconnected from verified Kohn–Sham meta prelude capstone on the capstone path — "
        "read row 68 + row 177 or row 158 gate + IX.2 Bridge → opening hinge → IX.3 calculation ladder + row 58; "
        "[row 178 baby picture](#row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 177 | Meta | Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion |",
        mem_table + "| 177 | Meta | Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion |",
    )
    if "When row 177 closed but DFT workflows meta reunion still lags" not in text:
        text = text.replace(
            "When row 176 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 177](#row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion).",
            "When row 176 closed but Kohn–Sham meta reunion still lags on the capstone path, switch to [row 177](#row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion). "
            "When row 177 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 178](#row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 178")


def patch_row_177_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "proceed to [row 178](preface.md#skill-navigation-row-178)" not in text:
        text = text.replace(
            "when opening [row 177](preface.md#skill-navigation-row-177) before row 58 closes",
            "when opening [row 178](preface.md#skill-navigation-row-178) before row 59 closes",
        )
    path.write_text(text)
    print("preface: patched row 177 → row 178 proceed hints")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_177_proceed_links()


if __name__ == "__main__":
    main()
