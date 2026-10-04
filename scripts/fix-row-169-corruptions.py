#!/usr/bin/env python3
"""Polish row 169 sections after lift_149_to_169 label substitutions."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_169_mod", ROOT / "scripts" / "add-row-169.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_149_to_169 = _mod.lift_149_to_169
extract_between = _mod.extract_between


def rebuild_sources_row_169_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker149 = (
        "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone "
        "reunion index (row 149) {#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149}"
    )
    marker168 = (
        "## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone "
        "reunion index (row 168)"
    )
    i149 = text.find(marker149)
    i168 = text.find(marker168, i149 if i149 >= 0 else 0)
    if i149 < 0 or i168 < 0:
        print("sources: skip rebuild (row 149/168 markers missing)")
        return
    block169 = lift_149_to_169(text[i149:i168]).strip()
    block169 = block169.replace(
        "(row 149) {#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149}",
        "(row 169) {#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169}",
        1,
    )
    block169 = re.sub(
        r"\s*\{#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149\}",
        "",
        block169,
        count=1,
    )
    block169 = block169.replace("Row 129 names", "Row 169 names", 1)
    block169 = block169.replace("(row 129)", "(row 169)")
    marker169 = (
        "## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone "
        "reunion index (row 169)"
    )
    i169 = text.find(marker169)
    if i169 < 0:
        print("sources: skip rebuild (row 169 slot missing)")
        return
    j = text.find("\n## Row 68 → Row 148 Row 68 → Row 48", i169)
    if j < 0:
        print("sources: skip rebuild (row 168 boundary missing)")
        return
    text = text[:i169] + block169 + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 169 index from row 149 template")


def insert_epilogue_row_169_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 169 closing loop" in text:
        print("epilogue: row 169 loop already present")
        return
    block = lift_149_to_169(
        extract_between(
            text,
            "### Row 149 closing loop",
            "### Row 148 closing loop",
        )
    )
    needle = "### Row 168 closing loop"
    if needle not in text:
        raise SystemExit("epilogue row 168 closing loop missing")
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: inserted row 169 closing loop")


def insert_memory_row_169() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = (
        "### Row 149 baby picture (Row 68 → Row 129 Row 68 → Row 49 taxonomy meta "
        "prelude capstone reunion) {#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion}"
    )
    if "row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 169 baby already present")
        return
    baby149 = extract_between(text, anchor, "### Row 129 baby picture")
    baby169 = lift_149_to_169(baby149)
    baby169 = baby169.replace(
        "#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion",
        "#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion",
    )
    text = text.replace(anchor, baby169 + anchor, 1)
    mem_table = (
        "| 169 | Meta | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion | "
        "[Row 68 → Row 149 taxonomy meta prelude capstone reunion index](sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) · "
        "[preface row 169 skill checkpoint](../preface.md#skill-navigation-row-169) · "
        "[prologue row 169 preview](../prologue/00-many-scales.md#prologue-preview-row-169) · "
        "[prologue row 169 closing stitch](../prologue/00-many-scales.md#row-169-closing-stitch) · "
        "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) | "
        "Row 68 closed but row 49 VII.0 → VII.1 opening hinge feels disconnected from verified "
        "midpoint meta prelude capstone on the capstone path — read row 68 + row 168 or row 149 gate + "
        "VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
        "[row 169 baby picture](#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) |\n"
    )
    if "| 169 | Meta |" not in text:
        text = text.replace(
            "| 149 | Meta | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion |",
            mem_table + "| 149 | Meta | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion |",
        )
    switch = (
        "When row 168 closed but taxonomy meta reunion still lags on the capstone path, "
        "switch to [row 169](#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion)."
    )
    if switch not in text:
        text = text.replace(
            "When row 148 closed but taxonomy meta reunion still lags on the capstone path, switch to [row 149](#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion).",
            "When row 148 closed but taxonomy meta reunion still lags on the capstone path, switch to [row 149](#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 169 baby picture")


def add_sources_table_row_169() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    if "| 169 | Row 68 → Row 149" in text:
        print("sources: row 169 table row already present")
        return
    table_row = (
        "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone "
        "(midpoint prelude gate ↔ midpoint meta prelude capstone ↔ row 49 meta) | "
        "[Row 68 → Row 149 taxonomy meta prelude capstone reunion index](#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) · "
        "[preface row 169](../preface.md#skill-navigation-row-169) · "
        "[prologue row 169 preview](../prologue/00-many-scales.md#prologue-preview-row-169) · "
        "[prologue row 169 closing stitch](../prologue/00-many-scales.md#row-169-closing-stitch) · "
        "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) · "
        "[memory sheet row 169 baby picture](memory-sheet.md#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 49 VII.0 → VII.1 opening hinge still feels disconnected from "
        "verified midpoint meta prelude capstone on the capstone path** — read row 68 + row 168 or row 149 "
        "gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
        "[preface row 49](../preface.md#skill-navigation-row-49) |\n"
    )
    text = text.replace(
        "| 168 | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone",
        table_row + "| 168 | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone",
    )
    path.write_text(text)
    print("sources: added row 169 table row")


def polish_row_169_text(s: str) -> str:
    epilogue_169_proceed = (
        "Do not conflate row 169 (row 68 ↔ row 49 reunion on the capstone path) with row 149 "
        "(opening-hinge prelude stitch alone) — row 149 names **Row 68 → Row 129 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion**; row 169 names **why that reunion must follow "
        "verified midpoint meta prelude capstone (row 168) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 170](#row-170-closing-loop) when row 68 closed but DDD "
        "meta prelude capstone still lags after row 169 on the capstone path, to [row 149](#row-149-closing-loop) "
        "when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta "
        "prelude capstone on the opening-hinge path, to [row 129](#row-129-closing-loop) when row 68 "
        "closed but taxonomy meta prelude capstone still lags after row 168 on the opening-hinge path, to "
        "[row 129](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 taxonomy meta prelude audit "
        "on the opening-hinge prelude path alone, to [row 168](#row-168-closing-loop) when midpoint meta "
        "prelude capstone still lags after verified part-boundary meta prelude capstone, to "
        "[row 49](#row-49-closing-loop) when only the VII.0 → VII.1 meta stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 169 closing loop" in s and "row-169-closing-loop" in s:
        s = re.sub(
            r"Do not conflate row 149 \(row 68 ↔ row 49 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_169_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    fixes = [
        (
            "[preface row 149 skill checkpoint](../preface.md#skill-navigation-row-169)",
            "[preface row 169 skill checkpoint](../preface.md#skill-navigation-row-169)",
        ),
        (
            "[Preface row 149](../preface.md#skill-navigation-row-169)",
            "[Preface row 169](../preface.md#skill-navigation-row-169)",
        ),
        (
            "[memory sheet row 169 baby picture](memory-sheet.md#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion)",
            "[memory sheet row 169 baby picture](memory-sheet.md#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion)",
        ),
        (
            "[Row 68 → Row 129 reunion index](../appendix/sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149)",
            "[Row 68 → Row 149 reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169)",
        ),
        (
            "[Row 68 → Row 129 taxonomy meta prelude capstone reunion index](../appendix/sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149)",
            "[Row 68 → Row 149 taxonomy meta prelude capstone reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169)",
        ),
        (
            "the [preface row 168 When-to-pause opening sentence](../preface.md#skill-navigation-row-168) names the dual reunion before taxonomy meta prelude reunion",
            "the [preface row 169 When-to-pause opening sentence](../preface.md#skill-navigation-row-169) names the dual reunion before DDD meta prelude reunion",
        ),
        (
            "[Row 68 → Row 148 reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169)",
            "[Row 68 → Row 149 reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169)",
        ),
        (
            "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) before row 50",
            "[epilogue row 169 closing loop](../epilogue/multiscale.md#row-169-closing-loop) before row 50",
        ),
        (
            "when forest landing is clean on the capstone path but Burgers circuits feel disconnected from return-mapping after row 148",
            "when forest landing is clean on the capstone path but Burgers circuits feel disconnected from return-mapping after row 168",
        ),
        (
            "read row 68 gate + row 148 or row 129 midpoint meta prelude capstone / taxonomy meta prelude gate",
            "read row 68 gate + row 168 or row 149 midpoint meta prelude capstone / taxonomy meta prelude gate",
        ),
        (
            "When row 168 is complete, proceed to [row 169](preface.md#skill-navigation-row-149)",
            "When row 168 is complete, proceed to [row 169](preface.md#skill-navigation-row-169)",
        ),
        (
            "Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the capstone path, to [row 149](#row-149-closing-loop)",
            "Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the capstone path, to [row 149](#row-149-closing-loop)",
        ),
        ("on the capstone path on the capstone path", "on the capstone path"),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def main() -> None:
    insert_epilogue_row_169_loop()
    rebuild_sources_row_169_index()
    add_sources_table_row_169()
    insert_memory_row_169()
    paths = [
        ROOT / "writings/preface/chapters/preface.md",
        ROOT / "writings/prologue/chapters/00-many-scales.md",
        ROOT / "writings/epilogue/chapters/multiscale.md",
        ROOT / "writings/appendix/chapters/sources.md",
        ROOT / "writings/appendix/chapters/memory-sheet.md",
    ]
    for path in paths:
        text = polish_row_169_text(path.read_text())
        path.write_text(text)
        print(f"polished: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
