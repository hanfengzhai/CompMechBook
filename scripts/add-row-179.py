#!/usr/bin/env python3
"""Add row 179 (Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion)."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("add_row_178_mod", ROOT / "scripts" / "add-row-178.py")
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_158_to_178 = _mod.lift_158_to_178
export_index_to_dft_workflows_178 = _mod.export_index_to_dft_workflows_178
extract_between = _mod.extract_between
tx = _mod.tx


def _premap_159_to_158_shape(s: str) -> str:
    pairs = [
        ("Row 159 skill checkpoint", "Row 158 skill checkpoint"),
        ("skill-navigation-row-159", "skill-navigation-row-158"),
        ("Row 159 closing loop", "Row 158 closing loop"),
        ("row-159-closing-loop", "row-158-closing-loop"),
        ("Row 159 closing stitch", "Row 158 closing stitch"),
        ("row-159-closing-stitch", "row-158-closing-stitch"),
        ("prologue-preview-row-159", "prologue-preview-row-158"),
        ("Row 159 preview", "Row 158 preview"),
        ("Row 159 baby picture", "Row 158 baby picture"),
        ("Row 159 three-way audit", "Row 158 three-way audit"),
        ("memory sheet row 159", "memory sheet row 158"),
        ("Row 68 → Row 139", "Row 68 → Row 138"),
        ("row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159", "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158"),
        ("row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion", "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion"),
        ("Row 68 → Row 159 Handshake 3 meta prelude capstone reunion index (row 159)", "Row 68 → Row 138 DFT workflows meta prelude capstone reunion index (row 158)"),
        ("Row 68 → Row 159 reunion index", "Row 68 → Row 151 reunion index"),
        ("Handshake 3 meta prelude capstone reunion", "DFT workflows meta prelude capstone reunion"),
        ("Handshake 3 meta prelude capstone", "DFT workflows meta prelude capstone"),
        ("IX.3 Bridge to the epilogue", "IX.2 Bridge"),
        ("opening hinge to Handshake 3", "IX.3 opening hinge from IX.2"),
        ("IX.3 → Handshake 3", "IX.2 → IX.3"),
        ("foundation archive Lab act", "cutoff-sweep Lab act"),
        ("`foundation_export.yaml`", "`cutoff_convergence.yaml`"),
        ("epilogue homework", "DFT coursework"),
        ("epilogue coursework", "DFT coursework"),
        ("row 59", "row 58"),
        ("Row 59", "Row 58"),
        ("verified DFT workflows meta capstone", "verified Kohn–Sham meta capstone"),
        ("DFT workflows meta capstone", "Kohn–Sham meta capstone"),
        ("quasiharmonic \\alpha(T_w)", "calculation ladder"),
        ("foundation archive →", "cutoff certificate →"),
        ("load-cell", "cu.foundation/"),
        ("[row 139]", "[row 138]"),
        ("row 139", "row 138"),
        ("Row 139", "Row 138"),
    ]
    return tx(s, pairs)


def _postmap_178_to_179_handshake(s: str) -> str:
    pairs = [
        ("Row 178 skill checkpoint", "Row 179 skill checkpoint"),
        ("skill-navigation-row-178", "skill-navigation-row-179"),
        ("Row 178 closing loop", "Row 179 closing loop"),
        ("row-178-closing-loop", "row-179-closing-loop"),
        ("Row 178 closing stitch", "Row 179 closing stitch"),
        ("row-178-closing-stitch", "row-179-closing-stitch"),
        ("prologue-preview-row-178", "prologue-preview-row-179"),
        ("Row 178 preview", "Row 179 preview"),
        ("Row 178 baby picture", "Row 179 baby picture"),
        ("Row 178 three-way audit", "Row 179 three-way audit"),
        ("memory sheet row 178", "memory sheet row 179"),
        ("Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone", "Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone"),
        ("row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178", "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179"),
        ("row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion", "row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion"),
        ("Row 68 → Row 151 DFT workflows meta prelude capstone reunion index (row 178)", "Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index (row 179)"),
        ("DFT workflows meta prelude capstone reunion", "Handshake 3 meta prelude capstone reunion"),
        ("DFT workflows meta prelude capstone", "Handshake 3 meta prelude capstone"),
        ("Kohn–Sham meta prelude capstone", "DFT workflows meta prelude capstone"),
        ("IX.2 Bridge", "IX.3 Bridge to the epilogue"),
        ("IX.3 opening hinge from IX.2", "opening hinge to Handshake 3"),
        ("IX.2 → IX.3", "IX.3 → Handshake 3"),
        ("cutoff-sweep Lab act", "foundation archive Lab act"),
        ("`cutoff_convergence.yaml`", "`foundation_export.yaml`"),
        ("DFT coursework", "epilogue homework"),
        ("row 58", "row 59"),
        ("Row 58", "Row 59"),
        ("row 177", "row 178"),
        ("Row 177", "Row 178"),
        ("row 178", "row 179"),
        ("Row 178", "Row 179"),
        ("(row 178)", "(row 179)"),
        ("Row 178 closes the", "Row 179 closes the"),
        ("Row 178 does not conflate", "Row 179 does not conflate"),
        ("Row 178 does not replace", "Row 179 does not replace"),
        ("row 58 meta", "row 59 meta"),
        ("before row 59 Handshake 3 meta prelude opens", "before row 60 Handshake 3 meta prelude capstone opens"),
        ("When row 178 is complete, proceed to [row 159]", "When row 179 is complete, proceed to [row 160]"),
        ("when opening [row 159](preface.md#skill-navigation-row-159) before row 60 closes", "when opening [row 179](preface.md#skill-navigation-row-179) before row 60 closes"),
        ("when row 177 closed but row 58", "when row 178 closed but row 59"),
        ("after row 177.", "after row 178."),
        ("verified Kohn–Sham meta prelude capstone closure (row 177)", "verified DFT workflows meta prelude capstone closure (row 178)"),
        ("SCF fixed-point → calculation ladder", "foundation archive → quasiharmonic α(T_w)"),
        ("`cu.foundation/`", "`alpha_export.yaml`"),
        ("Row 68 → Row 58 meta (row 158)", "Row 68 → Row 59 meta (row 159)"),
        ("Row 68 → Row 138", "Row 68 → Row 151"),
    ]
    out = tx(s, pairs)
    out = out.replace(
        "[row 158](preface.md#skill-navigation-row-179)",
        "[row 158](preface.md#skill-navigation-row-158)",
    )
    out = out.replace(
        "[row 178](preface.md#skill-navigation-row-158)",
        "[row 178](preface.md#skill-navigation-row-178)",
    )
    return out


def lift_159_to_179(s: str) -> str:
    return _postmap_178_to_179_handshake(lift_158_to_178(_premap_159_to_158_shape(s)))


def export_index_to_handshake3_179(block: str) -> str:
    return _postmap_178_to_179_handshake(export_index_to_dft_workflows_178(lift_158_to_178(block)))


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 179 skill checkpoint" in text:
        print("preface: row 179 already present")
        return
    m = re.search(
        r"(### Row 159 skill checkpoint.*?)(?=\n### Row 160 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 159 checkpoint missing")
    block = lift_159_to_179(m.group(1))
    anchor = "\n### Row 178 skill checkpoint"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 179")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 179 closing loop" in text:
        print("epilogue: row 179 loop already present")
        return
    block = lift_159_to_179(
        extract_between(
            text,
            "### Row 159 closing loop",
            "### Row 158 closing loop",
        )
    )
    needle = "### Row 178 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 179 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 179) |"
    if compass in text:
        print("prologue: row 179 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 178) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 178 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 159 compass missing")
        new_line = lift_159_to_179(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-159"></span>'
    preview_dst = '| <span id="prologue-preview-row-179"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_159_to_179(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 179 closing stitch" not in text:
        stitch = (
            "**Row 179 closing stitch (Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-179-closing-stitch} "
            "When row 178 closed — DFT workflows meta prelude capstone verified, row 178 or row 158 recited on the capstone path, and IX.2 Bridge → IX.3 calculation ladder recited with "
            "[foundation archive Lab act](../part09-dft/03-dft-workflows.md#lab-act-archive-the-foundation-run-before-the-wire-scale-solve-act-vi--foundation) archived `foundation_export.yaml` — but **row 59 IX.3 → Handshake 3 opening hinge still opens like standalone epilogue homework after the workflow archive Scene on the capstone path** — "
            "the [preface row 179 When-to-pause opening sentence](../preface.md#skill-navigation-row-179) names the dual reunion before the Handshake 3 meta prelude capstone reunion; "
            "read [preface row 179](../preface.md#skill-navigation-row-179), then the "
            "[Row 68 → Row 151 Handshake 3 reunion index](../appendix/sources.md#row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179), then "
            "[epilogue row 179 closing loop](../epilogue/multiscale.md#row-179-closing-loop) before row 60 Handshake 3 meta prelude capstone opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 178 closing stitch", stitch + "**Row 178 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 179 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179"
    if idx_key in text:
        print("sources: row 179 already present")
        return
    start178 = "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178"
    i = text.find(start178)
    if i < 0:
        raise SystemExit("sources row 178 index missing")
    i = text.rfind("\n## ", 0, i)
    end177 = "## Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)"
    j177 = text.find(end177, i)
    if j177 < 0:
        j177 = text.find("\n## Row 68 → Row 151 Row 68 → Row 56", i)
    block = export_index_to_handshake3_179(lift_159_to_179(text[i:j177]))
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179)",
        f"## Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 179 | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone "
        "(midpoint prelude gate ↔ DFT workflows meta prelude capstone ↔ row 59 meta) | "
        f"[Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 179](../preface.md#skill-navigation-row-179) · "
        "[prologue row 179 preview](../prologue/00-many-scales.md#prologue-preview-row-179) · "
        "[prologue row 179 closing stitch](../prologue/00-many-scales.md#row-179-closing-stitch) · "
        "[epilogue row 179 closing loop](../epilogue/multiscale.md#row-179-closing-loop) · "
        "[memory sheet row 179 baby picture](memory-sheet.md#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 59 IX.3 → Handshake 3 opening hinge still feels disconnected from verified DFT workflows meta prelude capstone on the capstone path** — "
        "read row 68 + row 178 or row 159 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[preface row 59](../preface.md#skill-navigation-row-59) |\n"
    )
    text = text.replace(
        "| 178 | Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone",
        table_row + "| 178 | Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone",
    )
    text = text.replace(start178, block + start178, 1)
    extra = (
        f"[row 179](#{idx_key}) reunites **DFT workflows meta prelude capstone with the Handshake 3 meta prelude capstone boundary** "
        "when row 178 closed DFT workflows meta prelude capstone at verified IX.2 → IX.3 closure on the capstone path but IX.3 Bridge and row 59 still read like separate courses;"
    )
    needle = (
        "[row 178](#row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178) reunites **Kohn–Sham meta prelude capstone with the DFT workflows meta prelude capstone boundary** "
    )
    if extra not in text and needle in text:
        text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 179")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 179 already present")
        return
    baby = lift_159_to_179(
        extract_between(
            text,
            "### Row 159 baby picture",
            "### Row 158 baby picture",
        )
    )
    anchor = "### Row 159 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 179 | Meta | Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion | "
        "[Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179) · "
        "[preface row 179 skill checkpoint](../preface.md#skill-navigation-row-179) · "
        "[prologue row 179 preview](../prologue/00-many-scales.md#prologue-preview-row-179) · "
        "[prologue row 179 closing stitch](../prologue/00-many-scales.md#row-179-closing-stitch) · "
        "[epilogue row 179 closing loop](../epilogue/multiscale.md#row-179-closing-loop) | "
        "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified DFT workflows meta prelude capstone on the capstone path — "
        "read row 68 + row 178 or row 159 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
        "[row 179 baby picture](#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 178 | Meta | Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion |",
        mem_table + "| 178 | Meta | Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion |",
    )
    if "When row 178 closed but Handshake 3 meta reunion still lags" not in text:
        text = text.replace(
            "When row 177 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 178](#row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion).",
            "When row 177 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 178](#row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion). "
            "When row 178 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 179](#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 179")


def patch_row_178_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "proceed to [row 179](preface.md#skill-navigation-row-179)" not in text:
        text = text.replace(
            "when opening [row 178](preface.md#skill-navigation-row-178) before row 59 closes",
            "when opening [row 179](preface.md#skill-navigation-row-179) before row 60 closes",
        )
    path.write_text(text)
    print("preface: patched row 178 → row 179 proceed hints")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_178_proceed_links()


if __name__ == "__main__":
    main()
