#!/usr/bin/env python3
"""Polish row 167 sections after lift_147_to_167 label substitutions."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_167_mod", ROOT / "scripts" / "add-row-167.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_147_to_167 = _mod.lift_147_to_167


def rebuild_sources_row_167_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    text = text.replace(
        "{#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167} "
        "{#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167}",
        "{#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167}",
    )
    marker147 = (
        "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone "
        "reunion index (row 147) {#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147}"
    )
    marker166 = (
        "## Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone "
        "reunion index (row 166)"
    )
    i147 = text.find(marker147)
    i166 = text.find(marker166, i147 if i147 >= 0 else 0)
    if i147 < 0 or i166 < 0:
        print("sources: skip rebuild (row 147/166 markers missing)")
        return
    block167 = lift_147_to_167(text[i147:i166]).strip()
    block167 = block167.replace(
        "(row 147) {#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147}",
        "(row 167) {#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167}",
        1,
    )
    marker167 = (
        "## Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone "
        "reunion index (row 167)"
    )
    i167 = text.find(marker167)
    j = text.find("\n## Row 68 → Row 166 Row 68 → Row 66 Writings", i167 if i167 >= 0 else 0)
    if i167 < 0 or j < 0:
        print("sources: skip rebuild (row 167 slot missing)")
        return
    text = text[:i167] + block167 + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 167 index from row 147 template")


def polish_row_167_text(s: str) -> str:
    epilogue_167_proceed = (
        "Do not conflate row 167 (row 68 ↔ row 67 reunion on the capstone path) with row 147 "
        "(opening-hinge prelude stitch alone) — row 147 names **Row 68 → Row 127 Row 68 → Row 67 "
        "part-boundary meta prelude capstone reunion**; row 167 names **why that reunion must follow "
        "verified Writings canonical meta prelude capstone (row 166) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 168](#row-168-closing-loop) when row 68 closed but midpoint "
        "meta prelude capstone still lags after row 167 on the capstone path, to [row 147](#row-147-closing-loop) "
        "when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary "
        "meta prelude capstone on the opening-hinge path, to [row 148](#row-128-closing-loop) when row 68 "
        "closed but midpoint meta capstone still lags after row 147 on the opening-hinge path, to "
        "[row 127](#row-107-closing-loop) for the Row 68 ↔ Row 67 meta audit on the opening-hinge "
        "prelude path alone, to [row 166](#row-166-closing-loop) when Writings canonical meta prelude "
        "capstone still lags after verified second-pass meta prelude capstone, to [row 67](#row-67-closing-loop) "
        "when only part-boundary prelude meta stalls, or extend prose only under `writings/` then sync."
    )
    if "### Row 167 closing loop" in s and "row-167-closing-loop" in s:
        import re

        s = re.sub(
            r"Do not conflate row 147 \(row 68 ↔ row 67 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_167_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    fixes = [
        (
            "[preface row 147 skill checkpoint](../preface.md#skill-navigation-row-167)",
            "[preface row 167 skill checkpoint](../preface.md#skill-navigation-row-167)",
        ),
        (
            "[Preface: row 147 skill checkpoint](../preface.md#skill-navigation-row-167)",
            "[Preface: row 167 skill checkpoint](../preface.md#skill-navigation-row-167)",
        ),
        (
            "[prologue row 147 preview row](#prologue-preview-row-167)",
            "[prologue row 167 preview row](#prologue-preview-row-167)",
        ),
        (
            "[prologue row 147 closing stitch](#row-167-closing-stitch)",
            "[prologue row 167 closing stitch](#row-167-closing-stitch)",
        ),
        (
            "[epilogue row 147 closing loop](../epilogue/multiscale.md#row-167-closing-loop)",
            "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop)",
        ),
        (
            "Prologue preview ([row 147](prologue/00-many-scales.md#prologue-preview-row-167))",
            "Prologue preview ([row 167](prologue/00-many-scales.md#prologue-preview-row-167))",
        ),
        (
            "[Preface row 147](../preface.md#skill-navigation-row-167)",
            "[Preface row 167](../preface.md#skill-navigation-row-167)",
        ),
        (
            "Read the [prologue row 147 closing stitch]",
            "Read the [prologue row 167 closing stitch]",
        ),
        (
            "Then read the [prologue row 147 preview](prologue/00-many-scales.md#prologue-preview-row-167)",
            "Then read the [prologue row 167 preview](prologue/00-many-scales.md#prologue-preview-row-167)",
        ),
        (
            "[Preface row 127](../preface.md#skill-navigation-row-167)",
            "[Preface row 167](../preface.md#skill-navigation-row-167)",
        ),
        (
            "Row 147 closes the **part-boundary meta prelude capstone",
            "Row 167 closes the **part-boundary meta prelude capstone",
        ),
        (
            "Row 68 → Row 67 meta (row 147) must read",
            "Row 68 → Row 67 meta (row 167) must read",
        ),
        (
            "return there when row 126 closed Writings",
            "return there when row 166 closed Writings",
        ),
        (
            "When row 67 feels like elasticity homework after row 146 alone",
            "When row 67 feels like elasticity homework after row 166 alone",
        ),
        (
            "Recite [preface row 146](../preface.md#skill-navigation-row-146) to split Writings",
            "Recite [preface row 166](../preface.md#skill-navigation-row-166) to split Writings",
        ),
        (
            "The [prologue row 147 preview](../prologue/00-many-scales.md#prologue-preview-row-167) and [prologue row 147 closing stitch]",
            "The [prologue row 167 preview](../prologue/00-many-scales.md#prologue-preview-row-167) and [prologue row 167 closing stitch]",
        ),
        (
            "**Row 167 baby picture:** when row 68 closed the midpoint prelude and row 126 or row 147 closed",
            "**Row 167 baby picture:** when row 68 closed the midpoint prelude and row 166 or row 147 closed",
        ),
        (
            "[preface row 126](../preface.md#skill-navigation-row-146) or [preface row 147](../preface.md#skill-navigation-row-107)",
            "[preface row 166](../preface.md#skill-navigation-row-166) or [preface row 147](../preface.md#skill-navigation-row-147)",
        ),
        (
            "WM[Writings meta prelude capstone row 126]",
            "WM[Writings meta prelude capstone row 166]",
        ),
        (
            "When row 147 feels disconnected from row 126, read them as **Writings meta prelude capstone vs part-boundary meta prelude capstones**: row 126 when",
            "When row 167 feels disconnected from row 166, read them as **Writings meta prelude capstone vs part-boundary meta prelude capstones**: row 166 when",
        ),
        (
            "row 147 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 128 midpoint meta prelude capstone opens**",
            "row 167 when **V.4 → VI.0 twin-ladder reunion and Row 66 → Row 47 meta must read on the same wire before row 168 midpoint meta prelude capstone opens**",
        ),
        (
            "switch to [row 147](#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion)",
            "switch to [row 167](#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion)",
        ),
        (
            "Row 146 closes the **Writings canonical meta prelude capstone at the source-time boundary",
            "Row 166 closes the **Writings canonical meta prelude capstone at the source-time boundary",
        ),
        (
            "Do not conflate row 147 (row 68 ↔ row 67 reunion on the capstone path) with row 127",
            "Do not conflate row 167 (row 68 ↔ row 67 reunion on the capstone path) with row 147",
        ),
        (
            "row 147 names **why that reunion must follow verified Writings canonical meta prelude capstone (row 146)",
            "row 167 names **why that reunion must follow verified Writings canonical meta prelude capstone (row 166)",
        ),
        (
            "Proceed to [row 128](#row-128-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path",
            "Proceed to [row 168](#row-168-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 167 on the capstone path",
        ),
        ("on the capstone path on the capstone path", "on the capstone path"),
    ]
    for a, b in fixes:
        s = s.replace(a, b)
    return s


def main() -> None:
    rebuild_sources_row_167_index()
    paths = [
        ROOT / "writings/preface/chapters/preface.md",
        ROOT / "writings/prologue/chapters/00-many-scales.md",
        ROOT / "writings/epilogue/chapters/multiscale.md",
        ROOT / "writings/appendix/chapters/sources.md",
        ROOT / "writings/appendix/chapters/memory-sheet.md",
    ]
    for path in paths:
        text = polish_row_167_text(path.read_text())
        path.write_text(text)
        print(f"polished: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
