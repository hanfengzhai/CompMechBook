#!/usr/bin/env python3
"""Polish row 172 sections after lift_152_to_172."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_172_mod", ROOT / "scripts" / "add-row-172.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_152_to_172 = _mod.lift_152_to_172
extract_between = _mod.extract_between


def polish_row_172(s: str) -> str:
    s = s.replace(
        "Row 68 → Row 171 Row 68 → Row 52",
        "Row 68 → Row 151 Row 68 → Row 52",
    )
    s = s.replace(
        "Row 68 → Row 152 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-172-closing-loop}",
        "Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion) {#row-172-closing-loop}",
    )
    s = s.replace(
        "verified homogenization meta prelude capstone closure (row 151)",
        "verified homogenization meta prelude capstone closure (row 171)",
    )
    s = s.replace("When row 151 closed", "When row 171 closed")
    s = s.replace("after row 151 alone", "after row 171 alone")
    s = s.replace("Recite [preface row 151]", "Recite [preface row 171]")
    s = re.sub(
        r"\[row 151\]\(preface\.md#skill-navigation-row-132\)",
        "[row 171](preface.md#skill-navigation-row-171)",
        s,
    )
    s = s.replace(
        "[row 152](preface.md#skill-navigation-row-132)",
        "[row 152](preface.md#skill-navigation-row-152)",
    )
    s = s.replace(
        "Row 68 → Row 112 atomistic meta prelude capstone reunion index (row 172)",
        "Row 68 → Row 151 atomistic meta prelude capstone reunion index (row 172)",
    )
    s = s.replace(
        "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        "row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172",
    )
    s = s.replace("#prologue-preview-row-152", "#prologue-preview-row-172")
    s = s.replace("#row-152-closing-stitch", "#row-172-closing-stitch")
    s = s.replace("#row-152-closing-loop", "#row-172-closing-loop")
    s = s.replace("{#row-152-closing-loop}", "{#row-172-closing-loop}")
    s = s.replace(
        "row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion",
        "row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion",
    )
    s = s.replace("preface row 152 skill checkpoint", "preface row 172 skill checkpoint")
    s = s.replace("[Preface row 152]", "[Preface row 172]")
    s = s.replace(
        "Row 172 does not replace row 68, row 52, row 151, row 152, row 132, row 92, or row 33",
        "Row 172 does not replace row 68, row 52, row 171, row 152, row 132, row 112, or row 33",
    )
    s = re.sub(
        r"\[Preface row 172\]\(\.\./preface\.md#skill-navigation-row-152\)",
        "[Preface row 172](../preface.md#skill-navigation-row-172)",
        s,
    )
    s = re.sub(
        r"\[preface row 172\]\(\.\./preface\.md#skill-navigation-row-152\)",
        "[preface row 172](../preface.md#skill-navigation-row-172)",
        s,
    )
    s = s.replace(
        "[preface row 171](../preface.md#skill-navigation-row-151)",
        "[preface row 171](../preface.md#skill-navigation-row-171)",
    )
    s = s.replace(
        "Row 68 → Row 171 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)",
        "Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)",
    )
    epilogue_172_proceed = (
        "Do not conflate row 172 (row 68 ↔ row 52 reunion on the capstone path) with row 152 "
        "(opening-hinge prelude stitch alone) — row 152 names **Row 68 → Row 132 Row 68 → Row 52 "
        "atomistic meta prelude capstone reunion**; row 172 names **why that reunion must follow "
        "verified homogenization meta prelude capstone (row 171) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 173](#row-173-closing-loop) when row 68 closed but "
        "dynamics meta prelude capstone still lags after row 172 on the capstone path, to "
        "[row 152](#row-152-closing-loop) when row 68 closed but atomistic meta prelude capstone still "
        "lags after verified homogenization meta prelude capstone on the opening-hinge path, to "
        "[row 132](#row-132-closing-loop) for the Row 68 ↔ Row 52 atomistic meta prelude audit on the "
        "opening-hinge path alone, to [row 171](#row-171-closing-loop) when homogenization meta prelude capstone still "
        "lags after verified DDD meta prelude capstone on the capstone path, to "
        "[row 52](#row-52-closing-loop) when only VII.3 → VIII.1 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 172 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 152 \(row 68 ↔ row 52 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_172_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 172 is complete, proceed to [row 173](preface.md#skill-navigation-row-153) "
        "when row 68 closed but dynamics meta prelude capstone still lags after verified "
        "atomistic meta prelude capstone on the capstone path, to [row 152](preface.md#skill-navigation-row-152) "
        "when homogenization meta prelude capstone is clean but atomistic meta prelude still lags on the "
        "opening-hinge path, to [row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ "
        "Row 52 atomistic meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still "
        "lags after verified DDD meta prelude capstone on the capstone path, to "
        "[row 52](preface.md#skill-navigation-row-52) for the VII.3 → VIII.1 meta audit alone, to "
        "[row 33](preface.md#skill-navigation-row-33) when only the MD preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 172 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def remove_duplicate_preface_row_171() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    dup = "### Row 171 skill checkpoint — Row 68 → Row 131"
    first = text.find("### Row 171 skill checkpoint")
    second = text.find(dup)
    if second > 0 and second != first:
        end = text.find("\n## The copper wire through the book", second)
        text = text[:second] + text[end:]
        path.write_text(text)
        print("preface: removed duplicate corrupted row 171 block")


def rebuild_preface_row_172() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 172 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    m = re.search(
        r"(### Row 152 skill checkpoint.*?)(?=\n### Row 153 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 152 template missing")
    block = polish_row_172(lift_152_to_172(m.group(1)))
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        j = text.find(end)
        text = text[:j] + "\n" + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 172 checkpoint")


def rebuild_epilogue_row_172_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 172 closing loop"
    end = "### Row 171 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 172 loop missing")
    block = polish_row_172(
        lift_152_to_172(
            extract_between(
                text,
                "### Row 152 closing loop",
                "### Row 151 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 172 closing loop")


def fix_prologue_row_172() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 152) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 172) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_172(lift_152_to_172(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-152"></span>Row 172 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-172"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-152"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_172(lift_152_to_172(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 172 compass/preview")


def rebuild_sources_row_172_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker152 = (
        "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152) "
        "{#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152}"
    )
    marker172 = "## Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    if text.find(marker172) < 0:
        marker172 = "## Row 68 → Row 171 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    i152 = text.find(marker152)
    i172 = text.find(marker172)
    if i152 < 0 or i172 < 0:
        print("sources: skip rebuild (markers missing)")
        return
    end171 = "## Row 68 → Row 151 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 171)"
    j171 = text.find(end171, i152)
    if j171 < 0:
        raise SystemExit("sources row 171 index missing for rebuild")
    block = polish_row_172(lift_152_to_172(text[i152:j171])).strip()
    block = block.replace(
        "(row 152) {#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152}",
        "(row 172) {#row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172}",
        1,
    )
    block = re.sub(
        r"\s*\{#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152\}",
        "",
        block,
        count=1,
    )
    j = text.find("\n## Row 68 → Row 132", i172)
    if j < 0:
        j = text.find("\n## Row 68 → Row 171", i172)
    text = text[:i172] + block + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 172 index from row 152 template")


def rebuild_memory_row_172_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 172 baby picture"
    if anchor not in text:
        print("memory-sheet: row 172 baby missing — run add-row-172 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 152 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 153 baby picture", start + 1)
    baby152 = extract_between(
        text,
        "### Row 152 baby picture",
        "### Row 153 baby picture",
    )
    baby = polish_row_172(lift_152_to_172(baby152))
    baby = baby.replace(
        "### Row 172 baby picture (Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
        "{#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion}",
        "### Row 172 baby picture (Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
        "{#row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    # Remove corrupted row 171 baby duplicate if anchor wrong
    text = re.sub(
        r"### Row 171 baby picture \(Row 68 → Row 131.*?\{#row-172-baby-picture-row68-row151-homogenization.*?\n\n",
        "",
        text,
        count=1,
        flags=re.S,
    )
    path.write_text(text)
    print("memory-sheet: rebuilt row 172 baby picture")


def patch_row_171_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    old = "When row 151 is complete, proceed to [row 132]"
    new = (
        "When row 171 is complete, proceed to [row 172](preface.md#skill-navigation-row-172) "
        "when row 68 closed but atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the capstone path, "
        "to [row 152](preface.md#skill-navigation-row-152) when homogenization meta prelude capstone is clean but atomistic meta prelude still lags on the opening-hinge path, "
        "to [row 151](preface.md#skill-navigation-row-151) for the Row 68 ↔ Row 51 homogenization meta prelude audit on the opening-hinge path alone, "
        "to [row 170](preface.md#skill-navigation-row-170) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, "
        "to [row 51](preface.md#skill-navigation-row-51) for the VII.2 → VII.3 meta audit alone, "
        "to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
    )
    if old in text and "When row 171 is complete, proceed to [row 172]" not in text:
        text = re.sub(
            r"When row 151 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 171 → row 172 proceed")


def main() -> None:
    remove_duplicate_preface_row_171()
    rebuild_preface_row_172()
    rebuild_epilogue_row_172_loop()
    fix_prologue_row_172()
    rebuild_sources_row_172_index()
    rebuild_memory_row_172_baby()
    patch_row_171_when_complete()


if __name__ == "__main__":
    main()
