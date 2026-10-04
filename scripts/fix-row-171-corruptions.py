#!/usr/bin/env python3
"""Polish row 171 sections after lift_151_to_171."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_171_mod", ROOT / "scripts" / "add-row-171.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_151_to_171 = _mod.lift_151_to_171
extract_between = _mod.extract_between


def polish_row_171(s: str) -> str:
    s = s.replace(
        "verified DDD meta prelude capstone closure (row 150)",
        "verified DDD meta prelude capstone closure (row 170)",
    )
    s = s.replace("When row 150 closed", "When row 170 closed")
    s = s.replace("after row 150 alone", "after row 170 alone")
    s = s.replace("Recite [preface row 150]", "Recite [preface row 170]")
    s = re.sub(
        r"\[row 150\]\(preface\.md#skill-navigation-row-151\)",
        "[row 170](preface.md#skill-navigation-row-170)",
        s,
    )
    s = s.replace(
        "[row 151](preface.md#skill-navigation-row-111)",
        "[row 151](preface.md#skill-navigation-row-151)",
    )
    s = s.replace(
        "Row 68 → Row 130 homogenization meta prelude capstone reunion index (row 171)",
        "Row 68 → Row 151 homogenization meta prelude capstone reunion index (row 171)",
    )
    s = s.replace(
        "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        "row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171",
    )
    s = s.replace("#prologue-preview-row-151", "#prologue-preview-row-171")
    s = s.replace("#row-151-closing-stitch", "#row-171-closing-stitch")
    s = s.replace("#row-151-closing-loop", "#row-171-closing-loop")
    s = s.replace("{#row-151-closing-loop}", "{#row-171-closing-loop}")
    s = s.replace(
        "row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion",
        "row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion",
    )
    s = s.replace("preface row 151 skill checkpoint", "preface row 171 skill checkpoint")
    s = s.replace("[Preface row 151]", "[Preface row 171]")
    s = s.replace(
        "Row 171 does not replace row 68, row 51, row 150, row 151, row 131, row 91, or row 32",
        "Row 171 does not replace row 68, row 51, row 170, row 151, row 131, row 111, or row 32",
    )
    for n in (152, 151, 131, 170, 150):
        s = s.replace(f"skill-navigation-row-__N{n}", f"skill-navigation-row-{n}")
    s = re.sub(
        r"\[Preface row 171\]\(\.\./preface\.md#skill-navigation-row-151\)",
        "[Preface row 171](../preface.md#skill-navigation-row-171)",
        s,
    )
    s = re.sub(
        r"\[preface row 171\]\(\.\./preface\.md#skill-navigation-row-151\)",
        "[preface row 171](../preface.md#skill-navigation-row-171)",
        s,
    )
    epilogue_171_proceed = (
        "Do not conflate row 171 (row 68 ↔ row 51 reunion on the capstone path) with row 151 "
        "(opening-hinge prelude stitch alone) — row 151 names **Row 68 → Row 131 Row 68 → Row 51 "
        "homogenization meta prelude capstone reunion**; row 171 names **why that reunion must follow "
        "verified DDD meta prelude capstone (row 170) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 172](#row-172-closing-loop) when row 68 closed but "
        "atomistic meta prelude capstone still lags after row 171 on the capstone path, to "
        "[row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still "
        "lags after verified DDD meta prelude capstone on the opening-hinge path, to "
        "[row 131](#row-131-closing-loop) for the Row 68 ↔ Row 51 homogenization meta prelude audit on the "
        "opening-hinge path alone, to [row 170](#row-170-closing-loop) when DDD meta prelude capstone still "
        "lags after verified taxonomy meta prelude capstone on the capstone path, to "
        "[row 51](#row-51-closing-loop) when only VII.2 → VII.3 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 171 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 151 \(row 68 ↔ row 51 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_171_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 171 is complete, proceed to [row 172](preface.md#skill-navigation-row-152) "
        "when row 68 closed but atomistic meta prelude capstone still lags after verified "
        "homogenization meta prelude capstone on the capstone path, to [row 151](preface.md#skill-navigation-row-151) "
        "when DDD meta prelude capstone is clean but homogenization meta prelude still lags on the "
        "opening-hinge path, to [row 131](preface.md#skill-navigation-row-131) for the Row 68 ↔ "
        "Row 51 homogenization meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still "
        "lags after verified taxonomy meta prelude capstone on the capstone path, to "
        "[row 150](preface.md#skill-navigation-row-150) when taxonomy meta prelude capstone is "
        "clean but DDD meta prelude still lags on the opening-hinge path, to "
        "[row 51](preface.md#skill-navigation-row-51) for the VII.2 → VII.3 meta audit alone, to "
        "[row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 171 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_171() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 171 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("preface row 171 block missing")
    m = re.search(
        r"(### Row 151 skill checkpoint.*?)(?=\n### Row 152 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 151 template missing")
    block = polish_row_171(lift_151_to_171(m.group(1)))
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 171 checkpoint")


def rebuild_epilogue_row_171_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 171 closing loop"
    end = "### Row 170 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 171 loop missing")
    block = polish_row_171(
        lift_151_to_171(
            extract_between(
                text,
                "### Row 151 closing loop",
                "### Row 132 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 171 closing loop")


def fix_prologue_row_171() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 151) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 171) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_171(lift_151_to_171(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-151"></span>Row 171 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-171"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-151"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_171(lift_151_to_171(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 171 compass/preview")


def rebuild_sources_row_171_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker151 = (
        "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151) "
        "{#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151}"
    )
    marker170 = "## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)"
    i151 = text.find(marker151)
    i170 = text.find(marker170)
    marker171 = "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)"
    i171 = text.find(marker171)
    if i151 < 0 or i170 < 0 or i171 < 0:
        print("sources: skip rebuild (markers missing)")
        return
    i112 = text.find("## Row 68 → Row 112", i151)
    block = polish_row_171(lift_151_to_171(text[i151:i112])).strip()
    block = block.replace(
        "(row 151) {#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151}",
        "(row 171) {#row68-row151-homogenization-meta-prelude-capstone-reunion-index-row-171}",
        1,
    )
    block = re.sub(
        r"\s*\{#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151\}",
        "",
        block,
        count=1,
    )
    j = text.find("\n## Row 68 → Row 150", i171)
    if j < 0:
        j = text.find("\n## Row 68 → Row 131", i171)
    text = text[:i171] + block + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 171 index from row 151 template")


def rebuild_memory_row_171_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 171 baby picture"
    if anchor not in text:
        print("memory-sheet: row 171 baby missing — run add-row-171 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 151 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 152 baby picture", start + 1)
    baby151 = extract_between(
        text,
        "### Row 151 baby picture",
        "### Row 152 baby picture",
    )
    baby = polish_row_171(lift_151_to_171(baby151))
    baby = baby.replace(
        "### Row 171 baby picture (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion) "
        "{#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion}",
        "### Row 171 baby picture (Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion) "
        "{#row-171-baby-picture-row68-row151-homogenization-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 171 baby picture")


def main() -> None:
    rebuild_preface_row_171()
    rebuild_epilogue_row_171_loop()
    fix_prologue_row_171()
    rebuild_sources_row_171_index()
    rebuild_memory_row_171_baby()


if __name__ == "__main__":
    main()
