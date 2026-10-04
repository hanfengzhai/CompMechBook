#!/usr/bin/env python3
"""Polish row 168 sections after lift_148_to_168 label substitutions."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_168_mod", ROOT / "scripts" / "add-row-168.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_148_to_168 = _mod.lift_148_to_168


def rebuild_sources_row_168_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker148 = (
        "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone "
        "reunion index (row 148) {#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148}"
    )
    marker167 = (
        "## Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone "
        "reunion index (row 167)"
    )
    i148 = text.find(marker148)
    i167 = text.find(marker167, i148 if i148 >= 0 else 0)
    if i148 < 0 or i167 < 0:
        print("sources: skip rebuild (row 148/167 markers missing)")
        return
    block168 = lift_148_to_168(text[i148:i167]).strip()
    block168 = block168.replace(
        "(row 148) {#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148}",
        "(row 168) {#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168}",
        1,
    )
    marker168 = (
        "## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone "
        "reunion index (row 168)"
    )
    i168 = text.find(marker168)
    j = text.find("\n## Row 68 → Row 147 Row 68 → Row 67", i168 if i168 >= 0 else 0)
    if i168 < 0 or j < 0:
        print("sources: skip rebuild (row 168 slot missing)")
        return
    text = text[:i168] + block168 + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 168 index from row 148 template")


def polish_row_168_text(s: str) -> str:
    epilogue_168_proceed = (
        "Do not conflate row 168 (row 68 ↔ row 48 reunion on the capstone path) with row 148 "
        "(opening-hinge prelude stitch alone) — row 148 names **Row 68 → Row 128 Row 68 → Row 48 "
        "midpoint meta prelude capstone reunion**; row 168 names **why that reunion must follow "
        "verified part-boundary meta prelude capstone (row 167) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy "
        "meta prelude capstone still lags after row 168 on the capstone path, to [row 148](#row-148-closing-loop) "
        "when row 68 closed but taxonomy meta prelude capstone still lags after verified midpoint meta "
        "prelude capstone on the opening-hinge path, to [row 128](#row-128-closing-loop) when row 68 "
        "closed but midpoint meta capstone still lags after row 167 on the opening-hinge path, to "
        "[row 128](preface.md#skill-navigation-row-128) for the Row 68 ↔ Row 48 meta audit on the "
        "opening-hinge prelude path alone, to [row 167](#row-167-closing-loop) when part-boundary meta "
        "prelude capstone still lags after verified Writings canonical meta prelude capstone, to "
        "[row 48](#row-48-closing-loop) when only the VI.4 → VII.0 meta stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 168 closing loop" in s and "row-168-closing-loop" in s:
        s = re.sub(
            r"Do not conflate row 148 \(row 68 ↔ row 48 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_168_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    fixes = [
        (
            "[preface row 148 skill checkpoint](../preface.md#skill-navigation-row-168)",
            "[preface row 168 skill checkpoint](../preface.md#skill-navigation-row-168)",
        ),
        (
            "[Preface row 148](../preface.md#skill-navigation-row-168)",
            "[Preface row 168](../preface.md#skill-navigation-row-168)",
        ),
        (
            "[prologue row 148 preview](../prologue/00-many-scales.md#prologue-preview-row-168)",
            "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-168)",
        ),
        (
            "[prologue row 148 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch)",
            "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch)",
        ),
        (
            "Prologue preview ([row 148](prologue/00-many-scales.md#prologue-preview-row-168))",
            "Prologue preview ([row 168](prologue/00-many-scales.md#prologue-preview-row-168))",
        ),
        (
            "Read the [prologue row 148 closing stitch](prologue/00-many-scales.md#row-168-closing-stitch)",
            "Read the [prologue row 168 closing stitch](prologue/00-many-scales.md#row-168-closing-stitch)",
        ),
        (
            "Then read the [prologue row 148 preview](prologue/00-many-scales.md#prologue-preview-row-168)",
            "Then read the [prologue row 168 preview](prologue/00-many-scales.md#prologue-preview-row-168)",
        ),
        (
            "read the [epilogue row 148 closing loop](epilogue/multiscale.md#row-168-closing-loop)",
            "read the [epilogue row 168 closing loop](epilogue/multiscale.md#row-168-closing-loop)",
        ),
        (
            "Row 148 closes the **midpoint meta prelude capstone",
            "Row 168 closes the **midpoint meta prelude capstone",
        ),
        (
            "Row 148 does not replace row 68, row 48, row 147, row 148, row 88, row 87, row 67, row 32, or row 20",
            "Row 168 does not replace row 68, row 48, row 167, row 148, row 88, row 87, row 67, row 32, or row 20",
        ),
        (
            "Row 68 → Row 108 midpoint meta prelude capstone reunion index (row 168)](appendix/sources.md#row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128)",
            "Row 68 → Row 148 midpoint meta prelude capstone reunion index (row 168)](appendix/sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168)",
        ),
        (
            "when twin-ladder reunion is clean after row 147 but",
            "when twin-ladder reunion is clean after row 167 but",
        ),
        (
            "when opening [row 169](preface.md#skill-navigation-row-149) before row 49 closes",
            "when opening [row 169](preface.md#skill-navigation-row-169) before row 49 closes",
        ),
        (
            "When row 148 is complete, proceed to [row 169](preface.md#skill-navigation-row-149)",
            "When row 168 is complete, proceed to [row 169](preface.md#skill-navigation-row-169)",
        ),
        (
            "[row 147](preface.md#skill-navigation-row-127) when Writings canonical",
            "[row 147](preface.md#skill-navigation-row-147) when Writings canonical",
        ),
        (
            "Recite [preface row 167](../preface.md#skill-navigation-row-147) to split part-boundary",
            "Recite [preface row 167](../preface.md#skill-navigation-row-167) to split part-boundary",
        ),
        (
            "**Row 168 baby picture:** when row 68 closed the midpoint prelude and row 147 or row 148 closed",
            "**Row 168 baby picture:** when row 68 closed the midpoint prelude and row 167 or row 148 closed",
        ),
        (
            "[preface row 147](../preface.md#skill-navigation-row-147) or [preface row 148](../preface.md#skill-navigation-row-148) part-boundary",
            "[preface row 167](../preface.md#skill-navigation-row-167) or [preface row 148](../preface.md#skill-navigation-row-148) part-boundary",
        ),
        (
            "[row 166](preface.md#skill-navigation-row-166)(preface.md#skill-navigation-row-166)",
            "[row 166](preface.md#skill-navigation-row-166)",
        ),
        (
            "read the [epilogue row 147 closing loop](epilogue/multiscale.md#row-167-closing-loop)",
            "read the [epilogue row 167 closing loop](epilogue/multiscale.md#row-167-closing-loop)",
        ),
        (
            "Row 147 does not replace row 68, row 67, row 166, row 147, row 87, row 66, row 47, or row 30",
            "Row 167 does not replace row 68, row 67, row 166, row 147, row 87, row 66, row 47, or row 30",
        ),
        ("on the capstone path on the capstone path", "on the capstone path"),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def main() -> None:
    rebuild_sources_row_168_index()
    paths = [
        ROOT / "writings/preface/chapters/preface.md",
        ROOT / "writings/prologue/chapters/00-many-scales.md",
        ROOT / "writings/epilogue/chapters/multiscale.md",
        ROOT / "writings/appendix/chapters/sources.md",
        ROOT / "writings/appendix/chapters/memory-sheet.md",
    ]
    for path in paths:
        text = polish_row_168_text(path.read_text())
        path.write_text(text)
        print(f"polished: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
