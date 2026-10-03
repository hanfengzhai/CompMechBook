#!/usr/bin/env python3
"""Add row 139 (Row 68 → Row 119 ↔ Row 59 Handshake 3 meta capstone on capstone path)."""
from __future__ import annotations

import re
import sys
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


def lift_119_to_139(s: str) -> str:
    p = [
        ("Row 119 closing loop", "Row 139 closing loop"),
        ("row-119-closing-loop", "row-139-closing-loop"),
        ("Row 119 closing stitch", "Row 139 closing stitch"),
        ("row-119-closing-stitch", "row-139-closing-stitch"),
        ("prologue-preview-row-119", "prologue-preview-row-139"),
        ("Row 119 preview", "Row 139 preview"),
        ("Row 119 skill checkpoint", "Row 139 skill checkpoint"),
        ("skill-navigation-row-119", "skill-navigation-row-139"),
        ("memory sheet row 119", "memory sheet row 139"),
        ("Row 119 baby picture", "Row 139 baby picture"),
        ("Row 119 three-way audit", "Row 139 three-way audit"),
        (
            "Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone",
            "Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone",
        ),
        (
            "row68-row99-handshake3-meta-capstone-reunion-index-row-119",
            "row68-row119-handshake3-meta-capstone-reunion-index-row-139",
        ),
        (
            "row-119-baby-picture-row68-row99-handshake3-meta-capstone-reunion",
            "row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion",
        ),
        ("[row 118]", "[row 138]"),
        ("row 118", "row 138"),
        ("Row 118", "Row 138"),
        ("[row 99]", "[row 119]"),
        ("row 99", "row 119"),
        ("Row 99", "Row 119"),
        ("(row 119)", "(row 139)"),
        ("row 119", "row 139"),
        (
            "DFT workflows meta capstone / Handshake 3 opening prelude hinge",
            "DFT workflows meta capstone / Handshake 3 opening prelude hinge on the capstone path",
        ),
        (
            "after the foundation archive Lab act**",
            "after the foundation archive Lab act on the capstone path**",
        ),
        (
            "at the Handshake 3 meta capstone boundary inside the coupling gate",
            "at the Handshake 3 meta capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 59 reunion |", "Row 68 ↔ Row 59 reunion (capstone path) |"),
        (
            "[Row 68 → Row 79 Handshake 3 meta prelude reunion index (row 99)]",
            "[Row 68 → Row 99 Handshake 3 meta capstone reunion index (row 119)]",
        ),
        (
            "row68-row79-handshake3-meta-prelude-reunion-index-row-99",
            "row68-row99-handshake3-meta-capstone-reunion-index-row-119",
        ),
        (
            "before row 120 Handshake 3 meta prelude opens",
            "before row 60 Handshake 3 meta prelude opens on the capstone path",
        ),
        (
            "when `foundation_export.yaml` exists but `alpha_export.yaml` lists `target_temperature_K: 300` after row 118",
            "when `foundation_export.yaml` exists on the capstone path but `alpha_export.yaml` lists `target_temperature_K: 300` after row 138",
        ),
        ("when row 138 and row 59", "when row 138 and row 59"),
        (
            "before row 59 closes",
            "before row 60 closes on the capstone path",
        ),
        (
            "When row 119 is complete, proceed to [row 120]",
            "When row 139 is complete, proceed to [row 140](preface.md#skill-navigation-row-140) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 120](preface.md#skill-navigation-row-120) when Handshake 3 meta capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 119](preface.md#skill-navigation-row-119) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 138](preface.md#skill-navigation-row-138) when DFT workflows meta capstone still lags after verified Kohn–Sham meta capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_119",
        ),
        (
            "Handshake 3 meta capstone at the foundation archive → quasiharmonic \\(\\alpha(T_w)\\) chapter boundary in reading time",
            "Handshake 3 meta capstone at the foundation archive → quasiharmonic \\(\\alpha(T_w)\\) chapter boundary in reading time on the capstone path",
        ),
        (
            "verified DFT workflows meta capstone closure (row 138)",
            "verified DFT workflows meta capstone closure (row 138)",
        ),
        (
            "verified DFT workflows meta capstone closure (row 118)",
            "verified DFT workflows meta capstone closure (row 138)",
        ),
        (
            "Row 68 → Row 59 meta (row 119)",
            "Row 68 → Row 59 meta (row 139)",
        ),
        (
            "Row 68 → Row 59 meta (row 99)",
            "Row 68 → Row 59 meta (row 139)",
        ),
        (
            "before row 120 Handshake 3 meta prelude capstone opens in workflow time",
            "before row 60 Handshake 3 meta prelude opens on the capstone path in workflow time",
        ),
        (
            "When row 59 feels like epilogue homework after row 138 alone",
            "When row 59 feels like epilogue homework after row 138 alone on the capstone path",
        ),
        (
            "When row 59 feels like epilogue homework after row 118 alone",
            "When row 59 feels like epilogue homework after row 138 alone on the capstone path",
        ),
        ("Recite [preface row 138]", "Recite [preface row 138]"),
        (
            "Do not conflate row 139 (row 68 ↔ row 59 reunion",
            "Do not conflate row 139 (row 68 ↔ row 59 reunion on the capstone path",
        ),
        (
            "Do not conflate row 119 (row 68 ↔ row 59 reunion",
            "Do not conflate row 139 (row 68 ↔ row 59 reunion on the capstone path",
        ),
        (
            "row 119 names **Row 68 → Row 79",
            "row 139 names **why that reunion must follow verified DFT workflows meta capstone (row 138) and the outer midpoint prelude gate (row 68)**; row 119 names **Row 68 → Row 79",
        ),
        (
            "Proceed to [row 120](#row-120-closing-loop) when load cell parses at \\(T_w\\) after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI",
            "Proceed to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 139 on the capstone path, to [row 120](#row-120-closing-loop) when load cell parses at \\(T_w\\) after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI on the opening-hinge path",
        ),
        (
            "Proceed to [row 120](#row-120-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 119",
            "Proceed to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 139 on the capstone path, to [row 120](#row-120-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 119 on the opening-hinge path, to [row 119](#row-119-closing-loop) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 138](#row-138-closing-loop) when DFT workflows meta capstone still lags after row 137 on the capstone path, to [row 59](#row-59-closing-loop) when only IX.3 → Handshake 3 stalls",
        ),
        (
            "DFT workflows meta row 138",
            "DFT workflows meta row 138",
        ),
        (
            "row 138 when **foundation export manifest",
            "row 139 when **foundation export manifest",
        ),
        (
            "before row 120 Handshake 3 meta prelude capstone or row 100 prelude opens",
            "before row 140 Handshake 3 meta prelude capstone or row 60 workflow reunion opens on the capstone path",
        ),
        (
            "when foundation archive is clean but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta capstone |",
            "when foundation archive is clean on the capstone path but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta capstone |",
        ),
        (
            "read row 68 gate + row 138 or row 119 DFT workflows meta capstone / Handshake 3 opening gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59 meta aloud when foundation archive is clean but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta capstone",
            "read row 68 gate + row 138 or row 119 DFT workflows meta capstone / Handshake 3 opening gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59 meta aloud when foundation archive is clean on the capstone path but handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell after verified DFT workflows meta capstone",
        ),
        (
            "when opening [row 120](preface.md#skill-navigation-row-120) before row 59 closes",
            "when opening [row 140](preface.md#skill-navigation-row-140) before row 60 closes on the capstone path",
        ),
        (
            "**Kohn–Sham meta capstone and IX.3 → Handshake 3 opening hinge still feel like separate stories**",
            "**DFT workflows meta capstone and IX.3 → Handshake 3 opening hinge still feel like separate stories**",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_119" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_119.*", "", out, flags=re.S)
    return out


def fix_row_138_tail(preface: str) -> str:
    old = (
        "When row 138 is complete, proceed to [row 119](preface.md#skill-navigation-row-119) when `foundation_export.yaml` exists but row 59 IX.3 → Handshake 3 still feels disconnected from verified DFT workflows meta capstone, to [row 99](preface.md#skill-navigation-row-99) when handbook \\(\\alpha(300\\,\\text{K})\\) persists at the load cell, to [row 118](preface.md#skill-navigation-row-98) for the Row 68 ↔ Row 58 DFT workflows opening prelude audit alone, to [row 78](preface.md#skill-navigation-row-78) for the Row 68 ↔ Row 58 prelude audit alone, to [row 137](preface.md#skill-navigation-row-117) when Kohn–Sham meta capstone still lags after verified Born–Oppenheimer meta capstone, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 138 is complete, proceed to [row 139](preface.md#skill-navigation-row-139) when `foundation_export.yaml` exists on the capstone path but Handshake 3 still lags, to [row 119](preface.md#skill-navigation-row-119) when DFT workflows meta capstone is clean but Handshake 3 meta capstone still lags on the opening-hinge path, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 118](preface.md#skill-navigation-row-118) for the Row 68 ↔ Row 58 DFT workflows meta audit on the opening-hinge path alone, to [row 137](preface.md#skill-navigation-row-137) when Kohn–Sham meta capstone still lags after verified Born–Oppenheimer meta capstone on the capstone path, to [row 58](preface.md#skill-navigation-row-58) when only IX.2 → IX.3 stalls, or extend prose only under `writings/` then sync."
    )
    if old in preface:
        preface = preface.replace(old, new)
    return preface


def add_row_139() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = fix_row_138_tail(preface)
    if "skill-navigation-row-139" in preface and "### Row 139 skill checkpoint" in preface:
        print("preface: row 139 already present")
    else:
        m119 = re.search(
            r"(### Row 119 skill checkpoint.*?)(?=\n### Row 120 skill checkpoint)",
            preface,
            re.S,
        )
        if not m119:
            raise SystemExit("row 119 preface checkpoint missing")
        row139 = lift_119_to_139(m119.group(1))
        anchor = "\n## The copper wire through the book"
        preface = preface.replace(anchor, "\n" + row139 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 139")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-139-closing-loop" not in ep:
        block119 = extract_between(ep, "### Row 119 closing loop", "### Row 120 closing loop")
        block139 = lift_119_to_139(block119)
        ep = ep.replace("### Row 120 closing loop", block139 + "### Row 120 closing loop", 1)
        ep = ep.replace(
            "Proceed to [row 119](#row-119-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 138, to [row 99](#row-99-closing-loop) when `foundation_export.yaml` exists but handbook \\(\\alpha\\) persists at the load cell,",
            "Proceed to [row 139](#row-139-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 138 on the capstone path, to [row 119](#row-119-closing-loop) when row 68 closed but Handshake 3 meta capstone still lags after row 118 on the opening-hinge path, to [row 99](#row-99-closing-loop) when `foundation_export.yaml` exists but handbook \\(\\alpha\\) persists at the load cell,",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 139 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion (row 139) |"
    )
    if compass_line not in pro:
        line119 = "| Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion (row 119) |"
        idx119 = pro.find(line119)
        if idx119 < 0:
            raise SystemExit("prologue compass row 119 not found")
        line_end119 = pro.find("\n", idx119)
        compass139 = lift_119_to_139(pro[idx119:line_end119]) + "\n"
        line138 = "| Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone reunion (row 138) |"
        idx138 = pro.find(line138)
        if idx138 < 0:
            raise SystemExit("prologue compass row 138 not found")
        line_end138 = pro.find("\n", idx138)
        pro = pro[: line_end138 + 1] + compass139 + pro[line_end138 + 1 :]
        preview119 = extract_between(
            pro,
            '| <span id="prologue-preview-row-119"></span>',
            '\n| <span id="prologue-preview-row-120">',
        )
        preview139 = lift_119_to_139(preview119)
        pro = pro.replace(
            '| <span id="prologue-preview-row-119"></span>',
            preview139 + '| <span id="prologue-preview-row-119"></span>',
            1,
        )
        if "row-139-closing-stitch" not in pro:
            stitch = (
                "**Row 139 closing stitch (Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion).** {#row-139-closing-stitch} "
                "When row 138 closed — DFT workflows meta capstone verified, row 137 or row 118 recited on the capstone path, and IX.2 Bridge → IX.3 calculation ladder recited with "
                "[foundation archive Lab act](../part09-dft/03-dft-workflows.md#lab-act-archive-the-foundation-run-before-the-wire-scale-solve-act-vi--foundation) archived `foundation_export.yaml` — but **row 59 IX.3 → Handshake 3 opening hinge still opens like standalone epilogue homework after the workflow archive Scene on the capstone path** — "
                "the [preface row 139 When-to-pause opening sentence](../preface.md#skill-navigation-row-139) names the dual reunion before Handshake 3 meta prelude reunion; read [preface row 139](../preface.md#skill-navigation-row-139), then the "
                "[Row 68 → Row 119 reunion index](../appendix/sources.md#row68-row119-handshake3-meta-capstone-reunion-index-row-139), then "
                "[epilogue row 139 closing loop](../epilogue/multiscale.md#row-139-closing-loop) before row 60 Handshake 3 meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 120 closing stitch", stitch + "**Row 120 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 139 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row119-handshake3-meta-capstone-reunion-index-row-139" not in src:
        idx119 = src.find(
            "## Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion index (row 119)"
        )
        idx120 = src.find(
            "## Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 120)"
        )
        if idx119 < 0 or idx120 < 0:
            raise SystemExit("row 119/120 sources anchors missing")
        block = src[idx119:idx120]
        block139 = lift_119_to_139(block)
        table_row = (
            "| 139 | Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone (midpoint prelude gate ↔ DFT workflows meta capstone ↔ row 59 meta) | "
            "[Row 68 → Row 119 Handshake 3 meta capstone reunion index](#row68-row119-handshake3-meta-capstone-reunion-index-row-139) · "
            "[preface row 139](../preface.md#skill-navigation-row-139) · "
            "[prologue row 139 preview](../prologue/00-many-scales.md#prologue-preview-row-139) · "
            "[prologue row 139 closing stitch](../prologue/00-many-scales.md#row-139-closing-stitch) · "
            "[epilogue row 139 closing loop](../epilogue/multiscale.md#row-139-closing-loop) · "
            "[memory sheet row 139 baby picture](memory-sheet.md#row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion) | "
            "Row 68 closed but **row 59 IX.3 → Handshake 3 opening hinge still feels disconnected from verified DFT workflows meta capstone on the capstone path** — "
            "read row 68 + row 138 or row 119 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
            "[preface row 59](../preface.md#skill-navigation-row-59) |\n"
        )
        src = src.replace(
            "| 138 | Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone",
            table_row + "| 138 | Row 68 → Row 118 Row 68 → Row 58 DFT workflows meta capstone",
        )
        src = src.replace(
            "## Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion index (row 119)",
            block139 + "## Row 68 → Row 99 Row 68 → Row 59 Handshake 3 meta capstone reunion index (row 119)",
        )
        extra = (
            "[row 139](#row68-row119-handshake3-meta-capstone-reunion-index-row-139) reunites **DFT workflows meta capstone with the Handshake 3 meta capstone boundary** "
            "when row 138 closed DFT workflows meta capstone at verified foundation archive on the capstone path but `foundation_export.yaml` and IX.3 → Handshake 3 opening hinge still read like separate courses after verified Handshake 3 meta prelude meta;"
        )
        if extra not in src:
            src = src.replace(
                "when row 137 closed Kohn–Sham meta capstone at verified Murnaghan scan on the capstone path but `cutoff_convergence.yaml` and IX.2 → IX.3 opening hinge still read like separate courses after verified DFT workflows meta prelude meta;",
                "when row 137 closed Kohn–Sham meta capstone at verified Murnaghan scan on the capstone path but `cutoff_convergence.yaml` and IX.2 → IX.3 opening hinge still read like separate courses after verified DFT workflows meta prelude meta; "
                + extra,
            )
        src_path.write_text(src)
        print("sources: added row 139 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-139-baby-picture" not in mem:
        baby119 = extract_between(mem, "### Row 119 baby picture", "### Row 120 baby picture")
        baby139 = lift_119_to_139(baby119)
        mem = mem.replace("### Act VI baby picture", baby139 + "### Act VI baby picture", 1)
        mem_table = (
            "| 139 | Meta | Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion | "
            "[Row 68 → Row 119 Handshake 3 meta capstone reunion index](sources.md#row68-row119-handshake3-meta-capstone-reunion-index-row-139) · "
            "[preface row 139 skill checkpoint](../preface.md#skill-navigation-row-139) · "
            "[prologue row 139 preview](../prologue/00-many-scales.md#prologue-preview-row-139) · "
            "[prologue row 139 closing stitch](../prologue/00-many-scales.md#row-139-closing-stitch) · "
            "[epilogue row 139 closing loop](../epilogue/multiscale.md#row-139-closing-loop) | "
            "Row 68 closed but row 59 IX.3 → Handshake 3 opening hinge feels disconnected from verified DFT workflows meta capstone on the capstone path — "
            "read row 68 + row 138 or row 119 gate + IX.3 Bridge → opening hinge to Handshake 3 + row 59; "
            "[row 139 baby picture](#row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion) |\n| 93 | Meta |",
            "[row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 138 closed but Handshake 3 meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 137 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 138](#row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion).",
                "When row 137 closed but DFT workflows meta reunion still lags on the capstone path, switch to [row 138](#row-138-baby-picture-row68-row118-dft-workflows-meta-capstone-reunion). When row 138 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 139](#row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 139")
    else:
        mem_path.write_text(mem)
        print("memory-sheet: row 139 baby already present")


def main() -> None:
    add_row_139()


if __name__ == "__main__":
    main()
