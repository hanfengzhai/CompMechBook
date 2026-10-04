#!/usr/bin/env python3
"""Polish row 176 sections after lift_156_to_176."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_176_mod", ROOT / "scripts" / "add-row-176.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_156_to_176 = _mod.lift_156_to_176
export_index_to_born_oppenheimer_176 = _mod.export_index_to_born_oppenheimer_176
extract_between = _mod.extract_between


def polish_row_176(s: str) -> str:
    s = s.replace("row 155 closed electronic", "row 175 closed electronic")
    s = s.replace(
        "after row 155 alone on the capstone path",
        "after row 175 alone on the capstone path",
    )
    s = s.replace(
        "verified electronic audit meta prelude capstone closure (row 155)",
        "verified electronic audit meta prelude capstone closure (row 175)",
    )
    s = s.replace("Row 68 → Row 56 meta (row 136)", "Row 68 → Row 56 meta (row 156)")
    s = s.replace("[prologue row 156 preview]", "[prologue row 176 preview]")
    s = s.replace("prologue row 156 preview", "prologue row 176 preview")
    s = s.replace(
        "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index",
        "Row 68 → Row 151 Born–Oppenheimer meta prelude capstone reunion index",
    )
    s = s.replace("([row 156]", "([row 176]")
    s = s.replace("preface row 156 skill checkpoint", "preface row 176 skill checkpoint")
    s = s.replace("prologue row 156 closing stitch", "prologue row 176 closing stitch")
    s = s.replace("epilogue row 156 closing loop", "epilogue row 176 closing loop")
    s = s.replace(
        "Electronic audit meta prelude capstone row 155",
        "Electronic audit meta prelude capstone row 175",
    )
    s = s.replace(
        "When row 176 feels disconnected from row 155",
        "When row 176 feels disconnected from row 175",
    )
    s = s.replace("row 155 when **VIII.3 Bridge", "row 175 when **VIII.3 Bridge")
    s = s.replace("row 156 when **IX.0 Bridge", "row 176 when **IX.0 Bridge")
    s = s.replace(
        "When row 175 closed but Born–Oppenheimer meta reunion still lags",
        "When row 175 closed but Born–Oppenheimer meta reunion still lags",
    )
    s = s.replace(
        "Row 68 → Row 176 Row 68 → Row 56",
        "Row 68 → Row 151 Row 68 → Row 56",
    )
    s = s.replace("#prologue-preview-row-156", "#prologue-preview-row-176")
    s = s.replace("#row-156-closing-stitch", "#row-176-closing-stitch")
    s = s.replace("#row-156-closing-loop", "#row-176-closing-loop")
    s = s.replace("{#row-156-closing-loop}", "{#row-176-closing-loop}")
    s = s.replace(
        "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
        "row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion",
    )
    s = s.replace("[Preface row 156]", "[Preface row 176]")
    s = re.sub(
        r"\[Preface row 176\]\(\.\./preface\.md#skill-navigation-row-156\)",
        "[Preface row 176](../preface.md#skill-navigation-row-176)",
        s,
    )
    s = re.sub(
        r"\[preface row 176\]\(\.\./preface\.md#skill-navigation-row-156\)",
        "[preface row 176](../preface.md#skill-navigation-row-176)",
        s,
    )
    s = s.replace(
        "[preface row 175](../preface.md#skill-navigation-row-155)",
        "[preface row 175](../preface.md#skill-navigation-row-175)",
    )
    s = s.replace(
        "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        "row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
    )
    epilogue_176_proceed = (
        "Do not conflate row 176 (row 68 ↔ row 56 reunion on the capstone path) with row 156 "
        "(opening-hinge prelude stitch alone) — row 156 names **Row 68 → Row 136 Row 68 → Row 56 "
        "Born–Oppenheimer meta prelude capstone reunion**; row 176 names **why that reunion must follow "
        "verified electronic audit meta prelude capstone (row 175) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 177](#row-177-closing-loop) when row 68 closed but "
        "Kohn–Sham meta prelude capstone still lags after row 176 on the capstone path, to "
        "[row 156](#row-156-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude still "
        "lags on the opening-hinge path, to "
        "[row 136](#row-136-closing-loop) for the Row 68 ↔ Row 56 Born–Oppenheimer meta prelude audit on the "
        "opening-hinge path alone, to [row 175](#row-175-closing-loop) when electronic audit meta prelude capstone still "
        "lags after verified export meta prelude capstone on the capstone path, to "
        "[row 56](#row-56-closing-loop) when only IX.0 → IX.1 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 176 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 156 \(row 68 ↔ row 56 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_176_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 176 is complete, proceed to [row 177](preface.md#skill-navigation-row-177) "
        "when row 68 closed but Kohn–Sham meta prelude capstone still lags after verified "
        "Born–Oppenheimer meta prelude capstone on the capstone path, to [row 156](preface.md#skill-navigation-row-156) "
        "when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta prelude still lags on the "
        "opening-hinge path, to [row 136](preface.md#skill-navigation-row-136) for the Row 68 ↔ "
        "Row 56 Born–Oppenheimer meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 175](preface.md#skill-navigation-row-175) when electronic audit meta prelude capstone still "
        "lags after verified export meta prelude capstone on the capstone path, to "
        "[row 56](preface.md#skill-navigation-row-56) for the IX.0 → IX.1 meta audit alone, to "
        "[row 37](preface.md#skill-navigation-row-37) when only the Born–Oppenheimer preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 176 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_176() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 176 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    m = re.search(
        r"(### Row 156 skill checkpoint.*?)(?=\n### Row 157 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 156 template missing")
    block = polish_row_176(lift_156_to_176(m.group(1)))
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        j = text.find(end)
        text = text[:j] + "\n" + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 176 checkpoint")


def rebuild_epilogue_row_176_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 176 closing loop"
    end = "### Row 175 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 176 loop missing")
    block = polish_row_176(
        lift_156_to_176(
            extract_between(
                text,
                "### Row 156 closing loop",
                "### Row 155 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 176 closing loop")


def fix_prologue_row_176() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 176) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_176(lift_156_to_176(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-156"></span>Row 176 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-176"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-156"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_176(lift_156_to_176(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 176 compass/preview")


def rebuild_sources_row_176_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker176 = "## Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 176)"
    i176 = text.find(marker176)
    if i176 < 0:
        print("sources: skip rebuild (row 176 marker missing)")
        return
    start175 = "## Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)"
    i175 = text.find(start175)
    if i175 < 0:
        raise SystemExit("sources row 175 template missing")
    j175_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 54", i176)
    if j175_end < 0:
        j175_end = text.find("\n## Row 68 → Row 132", i176)
    block = polish_row_176(
        export_index_to_born_oppenheimer_176(
            lift_156_to_176(text[i175 : text.find("\n## Row 68 → Row 151 Row 68 → Row 54", i175)])
        )
    ).strip()
    block = block.replace(
        "(row 176) {#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176}",
        "(row 176) {#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176}",
        1,
    )
    text = text[:i176] + block + "\n\n\n" + text[j175_end:]
    path.write_text(text)
    print("sources: rebuilt row 176 index")


def rebuild_memory_row_176_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 176 baby picture"
    if anchor not in text:
        print("memory-sheet: row 176 baby missing — run add-row-176 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 156 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 157 baby picture", start + 1)
    baby156 = extract_between(
        text,
        "### Row 156 baby picture",
        "### Row 137 baby picture",
    )
    baby = polish_row_176(lift_156_to_176(baby156))
    baby = baby.replace(
        "### Row 176 baby picture (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) "
        "{#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion}",
        "### Row 176 baby picture (Row 68 → Row 151 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion) "
        "{#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 176 baby picture")


def patch_row_175_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
        "When row 175 is complete, proceed to [row 176](preface.md#skill-navigation-row-176) "
        "when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after verified electronic audit meta prelude capstone on the capstone path, "
        "to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone is clean but electronic audit meta prelude still lags on the opening-hinge path, "
        "to [row 135](preface.md#skill-navigation-row-135) for the Row 68 ↔ Row 55 electronic audit meta prelude audit on the opening-hinge prelude path alone, "
        "to [row 174](preface.md#skill-navigation-row-174) when export meta prelude capstone still lags after verified dynamics meta prelude capstone on the capstone path, "
        "to [row 55](preface.md#skill-navigation-row-55) for the VIII.3 → IX.0 meta audit alone, "
        "to [row 36](preface.md#skill-navigation-row-36) when only the DFT preview stalls, or extend prose only under `writings/` then sync."
    )
    if "When row 175 is complete, proceed to [row 176](preface.md#skill-navigation-row-176)" not in text:
        text = re.sub(
            r"When row 175 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 175 → row 176 proceed")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    marker = "### Row 176 baby picture"
    while text.count(marker) > 1:
        first = text.find(marker)
        second = text.find(marker, first + 1)
        end = text.find("\n### ", second)
        if end < 0:
            end = len(text)
        else:
            end += 1
        text = text[:second] + text[end:]
    if text.count(marker) == 1:
        start = text.find(marker)
        end = text.find("\n### ", start + 1)
        block = text[start:end if end >= 0 else len(text)]
        fixed = polish_row_176(block)
        fixed = re.sub(
            r"\{#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion\}",
            "{#row-176-baby-picture-row68-row151-born-oppenheimer-meta-prelude-capstone-reunion}",
            fixed,
        )
        fixed = fixed.replace(
            "Row 68 → Row 136 Row 68 → Row 56",
            "Row 68 → Row 151 Row 68 → Row 56",
        )
        fixed = fixed.replace(
            "sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
            "sources.md#row68-row151-born-oppenheimer-meta-prelude-capstone-reunion-index-row-176",
        )
        fixed = fixed.replace(
            "[preface row 156](../preface.md#skill-navigation-row-176)",
            "[preface row 156](../preface.md#skill-navigation-row-156)",
        )
        text = text[:start] + fixed + text[end if end >= 0 else len(text) :]
    path.write_text(text)
    print("memory-sheet: deduped row 176 baby picture")


def global_polish_176_links() -> None:
    for rel in (
        "writings/preface/chapters/preface.md",
        "writings/prologue/chapters/00-many-scales.md",
        "writings/epilogue/chapters/multiscale.md",
        "writings/appendix/chapters/sources.md",
    ):
        path = ROOT / rel
        text = path.read_text()
        text = text.replace(
            "Row 68 → Row 136 reunion index",
            "Row 68 → Row 151 reunion index",
        )
        text = text.replace(
            "[Preface: row 156 skill checkpoint](../preface.md#skill-navigation-row-176)",
            "[Preface: row 176 skill checkpoint](../preface.md#skill-navigation-row-176)",
        )
        text = text.replace(
            "**why verified electronic audit meta prelude capstone demands IX.0 Bridge before any BO/HK proof on row 56**",
            "**why verified electronic audit meta prelude capstone demands IX.0 Bridge before any BO/HK proof on row 56**",
        )
        text = text.replace(
            "one continuous foundation SCF → export arc",
            "one continuous foundation SCF → BO/HK arc",
        )
        path.write_text(text)
    print("writings: global row 176 link polish")


def main() -> None:
    remove_duplicate_corrupted_baby()
    global_polish_176_links()
    rebuild_preface_row_176()
    rebuild_epilogue_row_176_loop()
    fix_prologue_row_176()
    rebuild_sources_row_176_index()
    rebuild_memory_row_176_baby()
    patch_row_175_when_complete()


if __name__ == "__main__":
    main()
