#!/usr/bin/env python3
"""Polish row 177 sections after lift_157_to_177."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_177_mod", ROOT / "scripts" / "add-row-177.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_157_to_177 = _mod.lift_157_to_177
export_index_to_kohn_sham_177 = _mod.export_index_to_kohn_sham_177
extract_between = _mod.extract_between


def polish_row_177(s: str) -> str:
    s = s.replace("row 156 closed Born", "row 176 closed Born")
    s = s.replace(
        "after row 156 alone on the capstone path",
        "after row 176 alone on the capstone path",
    )
    s = s.replace(
        "verified Born–Oppenheimer meta prelude capstone closure (row 156)",
        "verified Born–Oppenheimer meta prelude capstone closure (row 176)",
    )
    s = s.replace("Row 68 → Row 57 meta (row 137)", "Row 68 → Row 57 meta (row 157)")
    s = s.replace("[prologue row 157 preview]", "[prologue row 177 preview]")
    s = s.replace("prologue row 157 preview", "prologue row 177 preview")
    s = s.replace(
        "Row 68 → Row 137 Kohn–Sham meta prelude capstone reunion index",
        "Row 68 → Row 151 Kohn–Sham meta prelude capstone reunion index",
    )
    s = s.replace("([row 157]", "([row 177]")
    s = s.replace("preface row 157 skill checkpoint", "preface row 177 skill checkpoint")
    s = s.replace("prologue row 157 closing stitch", "prologue row 177 closing stitch")
    s = s.replace("epilogue row 157 closing loop", "epilogue row 177 closing loop")
    s = s.replace(
        "Born–Oppenheimer meta prelude capstone row 156",
        "Born–Oppenheimer meta prelude capstone row 176",
    )
    s = s.replace(
        "When row 177 feels disconnected from row 156",
        "When row 177 feels disconnected from row 176",
    )
    s = s.replace("#prologue-preview-row-157", "#prologue-preview-row-177")
    s = s.replace("#row-157-closing-stitch", "#row-177-closing-stitch")
    s = s.replace("#row-157-closing-loop", "#row-177-closing-loop")
    s = s.replace("{#row-157-closing-loop}", "{#row-177-closing-loop}")
    s = s.replace(
        "row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion",
        "row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion",
    )
    s = s.replace("[Preface row 157]", "[Preface row 177]")
    s = re.sub(
        r"\[Preface row 177\]\(\.\./preface\.md#skill-navigation-row-157\)",
        "[Preface row 177](../preface.md#skill-navigation-row-177)",
        s,
    )
    s = re.sub(
        r"\[preface row 177\]\(\.\./preface\.md#skill-navigation-row-157\)",
        "[preface row 177](../preface.md#skill-navigation-row-177)",
        s,
    )
    s = s.replace(
        "row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157",
        "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177",
    )
    epilogue_177_proceed = (
        "Do not conflate row 177 (row 68 ↔ row 57 reunion on the capstone path) with row 157 "
        "(opening-hinge prelude stitch alone) — row 157 names **Row 68 → Row 137 Row 68 → Row 57 "
        "Kohn–Sham meta prelude capstone reunion**; row 177 names **why that reunion must follow "
        "verified Born–Oppenheimer meta prelude capstone (row 176) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 178](#row-178-closing-loop) when row 68 closed but "
        "DFT workflows meta prelude capstone still lags after row 177 on the capstone path, to "
        "[row 157](#row-157-closing-loop) when row 68 closed but Kohn–Sham meta prelude still "
        "lags on the opening-hinge path, to "
        "[row 137](#row-137-closing-loop) for the Row 68 ↔ Row 57 Kohn–Sham meta prelude audit on the "
        "opening-hinge path alone, to [row 176](#row-176-closing-loop) when Born–Oppenheimer meta prelude capstone still "
        "lags after verified electronic audit meta prelude capstone on the capstone path, to "
        "[row 57](#row-57-closing-loop) when only IX.1 → IX.2 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 177 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 157 \(row 68 ↔ row 57 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_177_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 177 is complete, proceed to [row 178](preface.md#skill-navigation-row-178) "
        "when row 68 closed but DFT workflows meta prelude capstone still lags after verified "
        "Kohn–Sham meta prelude capstone on the capstone path, to [row 157](preface.md#skill-navigation-row-157) "
        "when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude still lags on the "
        "opening-hinge path, to [row 137](preface.md#skill-navigation-row-137) for the Row 68 ↔ "
        "Row 57 Kohn–Sham meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 176](preface.md#skill-navigation-row-176) when Born–Oppenheimer meta prelude capstone still "
        "lags after verified electronic audit meta prelude capstone on the capstone path, to "
        "[row 57](preface.md#skill-navigation-row-57) for the IX.1 → IX.2 meta audit alone, to "
        "[row 38](preface.md#skill-navigation-row-38) when only the Kohn–Sham preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 177 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_177() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 177 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    m = re.search(
        r"(### Row 157 skill checkpoint.*?)(?=\n### Row 158 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 157 template missing")
    block = polish_row_177(lift_157_to_177(m.group(1)))
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        j = text.find(end)
        text = text[:j] + "\n" + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 177 checkpoint")


def rebuild_epilogue_row_177_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 177 closing loop"
    end = "### Row 176 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 177 loop missing")
    block = polish_row_177(
        lift_157_to_177(
            extract_between(
                text,
                "### Row 157 closing loop",
                "### Row 156 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 177 closing loop")


def fix_prologue_row_177() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 177) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_177(lift_157_to_177(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-157"></span>Row 177 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-177"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-157"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_177(lift_157_to_177(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 177 compass/preview")


def rebuild_sources_row_177_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker177 = "## Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 177)"
    i177 = text.find(marker177)
    if i177 < 0:
        print("sources: skip rebuild (row 177 marker missing)")
        return
    start157 = "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion index (row 157)"
    i157 = text.find(start157)
    if i157 < 0:
        # fallback: lift from row 137 section
        start157 = "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 137)"
        i157 = text.find(start157)
    if i157 < 0:
        raise SystemExit("sources row 157 template missing")
    j157_end = text.find("\n## Row 68 → Row 97", i157)
    if j157_end < 0:
        j157_end = text.find("\n## Row 68 → Row 136", i157)
    block = polish_row_177(
        export_index_to_kohn_sham_177(
            lift_157_to_177(text[i157:j157_end])
        )
    ).strip()
    idx_key = "row68-row151-kohn-sham-meta-prelude-capstone-reunion-index-row-177"
    block = block.replace(
        "(row 177) {#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157}",
        f"(row 177) {{#{idx_key}}}",
        1,
    )
    block = block.replace(
        "(row 177) {#row68-row117-kohn-sham-meta-capstone-reunion-index-row-137}",
        f"(row 177) {{#{idx_key}}}",
        1,
    )
    j177_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 56", i177)
    if j177_end < 0:
        j177_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 55", i177)
    text = text[:i177] + block + "\n\n\n" + text[j177_end:]
    path.write_text(text)
    print("sources: rebuilt row 177 index")


def rebuild_memory_row_177_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 177 baby picture"
    if anchor not in text:
        print("memory-sheet: row 177 baby missing — run add-row-177 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 157 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 137 baby picture", start + 1)
    baby157 = extract_between(
        text,
        "### Row 157 baby picture",
        "### Row 137 baby picture",
    )
    baby = polish_row_177(lift_157_to_177(baby157))
    baby = baby.replace(
        "### Row 177 baby picture (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) "
        "{#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion}",
        "### Row 177 baby picture (Row 68 → Row 151 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) "
        "{#row-177-baby-picture-row68-row151-kohn-sham-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 177 baby picture")


def patch_row_176_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
        "When row 176 is complete, proceed to [row 177](preface.md#skill-navigation-row-177) "
        "when row 68 closed but Kohn–Sham meta prelude capstone still lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, "
        "to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta prelude still lags on the opening-hinge path, "
        "to [row 136](preface.md#skill-navigation-row-136) for the Row 68 ↔ Row 56 Born–Oppenheimer meta prelude audit on the opening-hinge prelude path alone, "
        "to [row 175](preface.md#skill-navigation-row-175) when electronic audit meta prelude capstone still lags after verified export meta prelude capstone on the capstone path, "
        "to [row 56](preface.md#skill-navigation-row-56) for the IX.0 → IX.1 meta audit alone, "
        "to [row 37](preface.md#skill-navigation-row-37) when only the Born–Oppenheimer preview stalls, or extend prose only under `writings/` then sync."
    )
    if "When row 176 is complete, proceed to [row 177](preface.md#skill-navigation-row-177)" in text:
        text = re.sub(
            r"When row 176 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 176 → row 177 proceed")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    marker = "### Row 177 baby picture"
    while text.count(marker) > 1:
        first = text.find(marker)
        second = text.find(marker, first + 1)
        end = text.find("\n### ", second)
        if end < 0:
            end = len(text)
        else:
            end += 1
        text = text[:second] + text[end:]
    path.write_text(text)
    print("memory-sheet: deduped row 177 baby picture")


def global_polish_177_links() -> None:
    for rel in (
        "writings/preface/chapters/preface.md",
        "writings/prologue/chapters/00-many-scales.md",
        "writings/epilogue/chapters/multiscale.md",
        "writings/appendix/chapters/sources.md",
    ):
        path = ROOT / rel
        text = path.read_text()
        text = text.replace(
            "Row 68 → Row 137 reunion index",
            "Row 68 → Row 151 reunion index",
        )
        text = text.replace(
            "[Preface: row 157 skill checkpoint](../preface.md#skill-navigation-row-177)",
            "[Preface: row 177 skill checkpoint](../preface.md#skill-navigation-row-177)",
        )
        path.write_text(text)
    print("writings: global row 177 link polish")


def main() -> None:
    remove_duplicate_corrupted_baby()
    global_polish_177_links()
    rebuild_preface_row_177()
    rebuild_epilogue_row_177_loop()
    fix_prologue_row_177()
    rebuild_sources_row_177_index()
    rebuild_memory_row_177_baby()
    patch_row_176_when_complete()


if __name__ == "__main__":
    main()
