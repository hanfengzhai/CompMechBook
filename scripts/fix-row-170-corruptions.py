#!/usr/bin/env python3
"""Polish row 170 sections after lift_150_to_170."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_170_mod", ROOT / "scripts" / "add-row-170.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_150_to_170 = _mod.lift_150_to_170
extract_between = _mod.extract_between


def polish_row_170(s: str) -> str:
    s = s.replace(
        "verified taxonomy meta prelude capstone closure (row 149)",
        "verified taxonomy meta prelude capstone closure (row 169)",
    )
    s = s.replace("When row 149 closed", "When row 169 closed")
    s = s.replace("after row 149 alone", "after row 169 alone")
    s = s.replace("Recite [preface row 149]", "Recite [preface row 169]")
    s = re.sub(
        r"\[row 149\]\(preface\.md#skill-navigation-row-169\)",
        "[row 169](preface.md#skill-navigation-row-169)",
        s,
    )
    s = s.replace(
        "[row 150](preface.md#skill-navigation-row-130)",
        "[row 150](preface.md#skill-navigation-row-150)",
    )
    s = s.replace(
        "Row 68 → Row 110 DDD meta prelude capstone reunion index (row 170)",
        "Row 68 → Row 150 DDD meta prelude capstone reunion index (row 170)",
    )
    s = s.replace(
        "row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130",
        "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170",
    )
    s = s.replace("#prologue-preview-row-150", "#prologue-preview-row-170")
    s = s.replace("#row-150-closing-stitch", "#row-170-closing-stitch")
    s = s.replace("#row-150-closing-loop", "#row-170-closing-loop")
    s = s.replace("{#row-150-closing-loop}", "{#row-170-closing-loop}")
    s = s.replace(
        "row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion",
        "row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion",
    )
    s = s.replace("preface row 150 skill checkpoint", "preface row 170 skill checkpoint")
    s = s.replace(
        "[Preface row 150]",
        "[Preface row 170]",
    )
    s = s.replace(
        "Row 170 does not replace row 68, row 50, row 149, row 150, row 110, row 90, or row 32",
        "Row 170 does not replace row 68, row 50, row 169, row 150, row 130, row 110, or row 32",
    )
    for n in (151, 150, 130, 149, 129):
        s = s.replace(f"skill-navigation-row-__N{n}", f"skill-navigation-row-{n}")
    s = re.sub(
        r"\[Preface row 170\]\(\.\./preface\.md#skill-navigation-row-150\)",
        "[Preface row 170](../preface.md#skill-navigation-row-170)",
        s,
    )
    s = re.sub(
        r"\[preface row 170\]\(\.\./preface\.md#skill-navigation-row-150\)",
        "[preface row 170](../preface.md#skill-navigation-row-170)",
        s,
    )
    epilogue_170_proceed = (
        "Do not conflate row 170 (row 68 ↔ row 50 reunion on the capstone path) with row 150 "
        "(opening-hinge prelude stitch alone) — row 150 names **Row 68 → Row 130 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion**; row 170 names **why that reunion must follow "
        "verified taxonomy meta prelude capstone (row 169) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 171](#row-171-closing-loop) when row 68 closed but "
        "homogenization meta prelude capstone still lags after row 170 on the capstone path, to "
        "[row 150](#row-150-closing-loop) when row 68 closed but DDD meta prelude capstone still "
        "lags after verified taxonomy meta prelude capstone on the opening-hinge path, to "
        "[row 130](#row-130-closing-loop) for the Row 68 ↔ Row 50 DDD meta prelude audit on the "
        "opening-hinge path alone, to [row 169](#row-169-closing-loop) when taxonomy meta prelude "
        "capstone still lags after verified midpoint meta prelude capstone on the capstone path, to "
        "[row 50](#row-50-closing-loop) when only VII.1 → VII.2 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 170 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 150 \(row 68 ↔ row 50 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_170_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 170 is complete, proceed to [row 171](preface.md#skill-navigation-row-151) "
        "when row 68 closed but homogenization meta prelude capstone still lags after verified "
        "DDD meta prelude capstone on the capstone path, to [row 150](preface.md#skill-navigation-row-150) "
        "when taxonomy meta prelude capstone is clean but DDD meta prelude still lags on the "
        "opening-hinge path, to [row 130](preface.md#skill-navigation-row-130) for the Row 68 ↔ "
        "Row 50 DDD meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 169](preface.md#skill-navigation-row-169) when taxonomy meta prelude capstone still "
        "lags after verified midpoint meta prelude capstone on the capstone path, to "
        "[row 149](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is "
        "clean but taxonomy meta prelude still lags on the opening-hinge path, to "
        "[row 50](preface.md#skill-navigation-row-50) for the VII.1 → VII.2 meta audit alone, to "
        "[row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 170 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_170() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 170 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("preface row 170 block missing")
    m = re.search(
        r"(### Row 150 skill checkpoint.*?)(?=\n### Row 151 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 150 template missing")
    block = polish_row_170(lift_150_to_170(m.group(1)))
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 170 checkpoint")


def rebuild_epilogue_row_170_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 170 closing loop"
    end = "### Row 167 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 170 loop missing")
    block = polish_row_170(
        lift_150_to_170(
            extract_between(
                text,
                "### Row 150 closing loop",
                "### Row 149 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 170 closing loop")


def fix_prologue_row_170() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion (row 150) |"
    bad = "| Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion (row 170) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_170(lift_150_to_170(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-150"></span>Row 170 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-170"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-150"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_170(lift_150_to_170(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 170 compass/preview")


def rebuild_sources_row_170_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker150 = (
        "## Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150) "
        "{#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150}"
    )
    marker151 = "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)"
    i150 = text.find(marker150)
    i151 = text.find(marker151, i150 if i150 >= 0 else 0)
    marker170 = "## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)"
    i170 = text.find(marker170)
    if i150 < 0 or i151 < 0 or i170 < 0:
        print("sources: skip rebuild (markers missing)")
        return
    block = polish_row_170(lift_150_to_170(text[i150:i151])).strip()
    block = block.replace(
        "(row 150) {#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150}",
        "(row 170) {#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170}",
        1,
    )
    block = re.sub(
        r"\s*\{#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150\}",
        "",
        block,
        count=1,
    )
    j = text.find("\n## Row 68 → Row 131", i170)
    if j < 0:
        j = text.find("\n## Row 68 → Row 129", i170)
    text = text[:i170] + block + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 170 index from row 150 template")


def rebuild_memory_row_170_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 170 baby picture"
    if anchor in text:
        print("memory-sheet: row 170 baby already present")
        return
    baby150 = extract_between(
        text,
        "### Row 150 baby picture (Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion) {#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion}",
        "### Row 151 baby picture",
    )
    baby = polish_row_170(lift_150_to_170(baby150))
    baby = baby.replace(
        "### Row 170 baby picture (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion) "
        "{#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion}",
        "### Row 170 baby picture (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion) "
        "{#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion}",
        1,
    )
    insert_at = "### Row 150 baby picture (Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion) {#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion}"
    text = text.replace(insert_at, baby + insert_at, 1)
    path.write_text(text)
    print("memory-sheet: rebuilt row 170 baby picture")


def main() -> None:
    rebuild_preface_row_170()
    rebuild_epilogue_row_170_loop()
    fix_prologue_row_170()
    rebuild_sources_row_170_index()
    rebuild_memory_row_170_baby()


if __name__ == "__main__":
    main()
