#!/usr/bin/env python3
"""Polish row 173 sections after lift_153_to_173."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_173_mod", ROOT / "scripts" / "add-row-173.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_153_to_173 = _mod.lift_153_to_173
extract_between = _mod.extract_between


def polish_row_173(s: str) -> str:
    s = s.replace("row 151 closed atomistic", "row 172 closed atomistic")
    s = s.replace("after row 151 alone on the capstone path", "after row 172 alone on the capstone path")
    s = s.replace(
        "verified atomistic meta prelude capstone closure (row 151)",
        "verified atomistic meta prelude capstone closure (row 172)",
    )
    s = s.replace(
        "Row 68 → Row 53 meta (row 113)",
        "Row 68 → Row 53 meta (row 153)",
    )
    s = s.replace(
        "[prologue row 153 preview]",
        "[prologue row 173 preview]",
    )
    s = s.replace(
        "prologue row 153 preview",
        "prologue row 173 preview",
    )
    s = s.replace(
        "Row 68 → Row 153 dynamics meta prelude capstone reunion index",
        "Row 68 → Row 151 dynamics meta prelude capstone reunion index",
    )
    s = s.replace(
        "[Row 68 → Row 153 reunion index]",
        "[Row 68 → Row 151 reunion index]",
    )
    s = s.replace(
        "([row 153]",
        "([row 173]",
    )
    s = s.replace("preface row 153 skill checkpoint", "preface row 173 skill checkpoint")
    s = s.replace("prologue row 153 closing stitch", "prologue row 173 closing stitch")
    s = s.replace("epilogue row 153 closing loop", "epilogue row 173 closing loop")
    s = s.replace(
        "Atomistic meta prelude capstone row 132",
        "Atomistic meta prelude capstone row 172",
    )
    s = s.replace(
        "When row 153 feels disconnected from row 132",
        "When row 173 feels disconnected from row 172",
    )
    s = s.replace(
        "row 132 when **VII.3 Bridge",
        "row 172 when **VII.3 Bridge",
    )
    s = s.replace(
        "row 153 when **VIII.1 Bridge",
        "row 173 when **VIII.1 Bridge",
    )
    s = s.replace(
        "When row 132 closed but dynamics meta reunion still lags",
        "When row 172 closed but dynamics meta reunion still lags",
    )
    s = s.replace(
        "Row 68 → Row 172 Row 68 → Row 53",
        "Row 68 → Row 151 Row 68 → Row 53",
    )
    s = s.replace(
        "Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion) {#row-173-closing-loop}",
        "Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion) {#row-173-closing-loop}",
    )
    s = s.replace(
        "verified atomistic meta prelude capstone closure (row 152)",
        "verified atomistic meta prelude capstone closure (row 172)",
    )
    s = s.replace("When row 152 closed", "When row 172 closed")
    s = s.replace("after row 152 alone", "after row 172 alone")
    s = s.replace("Recite [preface row 152]", "Recite [preface row 172]")
    s = re.sub(
        r"\[row 152\]\(preface\.md#skill-navigation-row-133\)",
        "[row 172](preface.md#skill-navigation-row-172)",
        s,
    )
    s = s.replace(
        "[row 153](preface.md#skill-navigation-row-133)",
        "[row 153](preface.md#skill-navigation-row-153)",
    )
    s = s.replace(
        "Row 68 → Row 113 dynamics meta prelude capstone reunion index (row 173)",
        "Row 68 → Row 151 dynamics meta prelude capstone reunion index (row 173)",
    )
    s = s.replace(
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        "row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173",
    )
    s = s.replace("#prologue-preview-row-153", "#prologue-preview-row-173")
    s = s.replace("#row-153-closing-stitch", "#row-173-closing-stitch")
    s = s.replace("#row-153-closing-loop", "#row-173-closing-loop")
    s = s.replace("{#row-153-closing-loop}", "{#row-173-closing-loop}")
    s = s.replace(
        "row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion",
        "row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion",
    )
    s = s.replace("preface row 153 skill checkpoint", "preface row 173 skill checkpoint")
    s = s.replace("[Preface row 153]", "[Preface row 173]")
    s = s.replace(
        "Row 173 does not replace row 68, row 53, row 152, row 153, row 133, row 93, or row 34",
        "Row 173 does not replace row 68, row 53, row 172, row 153, row 133, row 113, or row 34",
    )
    s = re.sub(
        r"\[Preface row 173\]\(\.\./preface\.md#skill-navigation-row-153\)",
        "[Preface row 173](../preface.md#skill-navigation-row-173)",
        s,
    )
    s = re.sub(
        r"\[preface row 173\]\(\.\./preface\.md#skill-navigation-row-153\)",
        "[preface row 173](../preface.md#skill-navigation-row-173)",
        s,
    )
    s = s.replace(
        "[preface row 172](../preface.md#skill-navigation-row-152)",
        "[preface row 172](../preface.md#skill-navigation-row-172)",
    )
    s = s.replace(
        "Row 68 → Row 153 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)",
        "Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)",
    )
    epilogue_173_proceed = (
        "Do not conflate row 173 (row 68 ↔ row 53 reunion on the capstone path) with row 153 "
        "(opening-hinge prelude stitch alone) — row 153 names **Row 68 → Row 133 Row 68 → Row 53 "
        "dynamics meta prelude capstone reunion**; row 173 names **why that reunion must follow "
        "verified atomistic meta prelude capstone (row 172) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 174](#row-174-closing-loop) when row 68 closed but "
        "export meta prelude capstone still lags after row 173 on the capstone path, to "
        "[row 153](#row-153-closing-loop) when row 68 closed but dynamics meta prelude still "
        "lags on the opening-hinge path, to "
        "[row 133](#row-133-closing-loop) for the Row 68 ↔ Row 53 dynamics meta prelude audit on the "
        "opening-hinge path alone, to [row 172](#row-172-closing-loop) when atomistic meta prelude capstone still "
        "lags after verified homogenization meta prelude capstone on the capstone path, to "
        "[row 53](#row-53-closing-loop) when only VIII.1 → VIII.2 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 173 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 153 \(row 68 ↔ row 53 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_173_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 173 is complete, proceed to [row 174](preface.md#skill-navigation-row-154) "
        "when row 68 closed but export meta prelude capstone still lags after verified "
        "dynamics meta prelude capstone on the capstone path, to [row 153](preface.md#skill-navigation-row-153) "
        "when atomistic meta prelude capstone is clean but dynamics meta prelude still lags on the "
        "opening-hinge path, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ "
        "Row 53 dynamics meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 172](preface.md#skill-navigation-row-172) when atomistic meta prelude capstone still "
        "lags after verified homogenization meta prelude capstone on the capstone path, to "
        "[row 53](preface.md#skill-navigation-row-53) for the VIII.1 → VIII.2 meta audit alone, to "
        "[row 34](preface.md#skill-navigation-row-34) when only the MD preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 173 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_173() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 173 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    m = re.search(
        r"(### Row 153 skill checkpoint.*?)(?=\n### Row 154 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 153 template missing")
    block = polish_row_173(lift_153_to_173(m.group(1)))
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        j = text.find(end)
        text = text[:j] + "\n" + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 173 checkpoint")


def rebuild_epilogue_row_173_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 173 closing loop"
    end = "### Row 172 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 173 loop missing")
    block = polish_row_173(
        lift_153_to_173(
            extract_between(
                text,
                "### Row 153 closing loop",
                "### Row 152 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 173 closing loop")


def fix_prologue_row_173() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 173) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_173(lift_153_to_173(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-153"></span>Row 173 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-173"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-153"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_173(lift_153_to_173(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 173 compass/preview")


def rebuild_sources_row_173_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker153 = (
        "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153) "
        "{#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153}"
    )
    marker173 = "## Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    if text.find(marker173) < 0:
        marker173 = "## Row 68 → Row 172 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    i153 = text.find(marker153)
    i173 = text.find(marker173)
    if i153 < 0 or i173 < 0:
        print("sources: skip rebuild (markers missing)")
        return
    end172 = "## Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    j172 = text.find(end172, i153)
    if j172 < 0:
        raise SystemExit("sources row 172 index missing for rebuild")
    block = polish_row_173(lift_153_to_173(text[i153:j172])).strip()
    block = block.replace(
        "(row 153) {#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153}",
        "(row 173) {#row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173}",
        1,
    )
    block = re.sub(
        r"\s*\{#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153\}",
        "",
        block,
        count=1,
    )
    j = text.find("\n## Row 68 → Row 133", i173)
    if j < 0:
        j = text.find("\n## Row 68 → Row 151 Row 68 → Row 52", i173)
    text = text[:i173] + block + "\n\n\n" + text[j:]
    path.write_text(text)
    print("sources: rebuilt row 173 index from row 153 template")


def rebuild_memory_row_173_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 173 baby picture"
    if anchor not in text:
        print("memory-sheet: row 173 baby missing — run add-row-173 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 153 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 154 baby picture", start + 1)
    baby153 = extract_between(
        text,
        "### Row 153 baby picture",
        "### Row 154 baby picture",
    )
    baby = polish_row_173(lift_153_to_173(baby153))
    baby = baby.replace(
        "### Row 173 baby picture (Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion) "
        "{#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion}",
        "### Row 173 baby picture (Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion) "
        "{#row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 173 baby picture")


def patch_row_172_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
        "When row 172 is complete, proceed to [row 173](preface.md#skill-navigation-row-173) "
        "when row 68 closed but dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the capstone path, "
        "to [row 152](preface.md#skill-navigation-row-152) when homogenization meta prelude capstone is clean but atomistic meta prelude still lags on the opening-hinge path, "
        "to [row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ Row 52 atomistic meta prelude audit on the opening-hinge prelude path alone, "
        "to [row 171](preface.md#skill-navigation-row-171) when homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path, "
        "to [row 52](preface.md#skill-navigation-row-52) for the VII.3 → VIII.1 meta audit alone, "
        "to [row 33](preface.md#skill-navigation-row-33) when only the MD preview stalls, or extend prose only under `writings/` then sync."
    )
    if "When row 172 is complete, proceed to [row 173](preface.md#skill-navigation-row-173)" not in text:
        text = re.sub(
            r"When row 172 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 172 → row 173 proceed")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    bad = (
        "### Row 173 baby picture (Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion) "
        "{#row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion}"
    )
    if bad in text:
        start = text.find(bad)
        end = text.find("### Row 134 baby picture", start)
        text = text[:start] + text[end:]
        path.write_text(text)
        print("memory-sheet: removed duplicate corrupted row 173 baby")


def main() -> None:
    remove_duplicate_corrupted_baby()
    rebuild_preface_row_173()
    rebuild_epilogue_row_173_loop()
    fix_prologue_row_173()
    rebuild_sources_row_173_index()
    rebuild_memory_row_173_baby()
    patch_row_172_when_complete()


if __name__ == "__main__":
    main()
