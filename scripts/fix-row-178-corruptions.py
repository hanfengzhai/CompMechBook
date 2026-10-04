#!/usr/bin/env python3
"""Polish row 178 sections after lift_158_to_178."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_178_mod", ROOT / "scripts" / "add-row-178.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_158_to_178 = _mod.lift_158_to_178
export_index_to_dft_workflows_178 = _mod.export_index_to_dft_workflows_178
extract_between = _mod.extract_between


def polish_row_178(s: str) -> str:
    s = s.replace("row 157 closed", "row 177 closed")
    s = s.replace("after row 157 alone on the capstone path", "after row 177 alone on the capstone path")
    s = s.replace(
        "verified Kohn–Sham meta prelude capstone closure (row 157)",
        "verified Kohn–Sham meta prelude capstone closure (row 177)",
    )
    s = s.replace("Row 68 → Row 58 meta (row 138)", "Row 68 → Row 58 meta (row 158)")
    s = s.replace(
        "Row 68 → Row 138 DFT workflows meta prelude capstone reunion index",
        "Row 68 → Row 151 DFT workflows meta prelude capstone reunion index",
    )
    s = s.replace("([row 158]", "([row 178]")
    s = s.replace("preface row 158 skill checkpoint", "preface row 178 skill checkpoint")
    s = s.replace("prologue row 158 preview", "prologue row 178 preview")
    s = s.replace("prologue row 158 closing stitch", "prologue row 178 closing stitch")
    s = s.replace("epilogue row 158 closing loop", "epilogue row 178 closing loop")
    s = s.replace("#prologue-preview-row-158", "#prologue-preview-row-178")
    s = s.replace("#row-158-closing-stitch", "#row-178-closing-stitch")
    s = s.replace("#row-158-closing-loop", "#row-178-closing-loop")
    s = s.replace("{#row-158-closing-loop}", "{#row-178-closing-loop}")
    s = s.replace(
        "row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion",
        "row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion",
    )
    s = s.replace(
        "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158",
        "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178",
    )
    s = re.sub(
        r"\[Preface row 178\]\(\.\./preface\.md#skill-navigation-row-158\)",
        "[Preface row 178](../preface.md#skill-navigation-row-178)",
        s,
    )
    s = re.sub(
        r"\[preface row 178\]\(\.\./preface\.md#skill-navigation-row-158\)",
        "[preface row 178](../preface.md#skill-navigation-row-178)",
        s,
    )
    epilogue_178_proceed = (
        "Do not conflate row 178 (row 68 ↔ row 58 reunion on the capstone path) with row 158 "
        "(opening-hinge prelude stitch alone) — row 158 names **Row 68 → Row 138 Row 68 → Row 58 "
        "DFT workflows meta prelude capstone reunion**; row 178 names **why that reunion must follow "
        "verified Kohn–Sham meta prelude capstone (row 177) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 159](#row-159-closing-loop) when row 68 closed but "
        "Handshake 3 meta prelude capstone still lags after row 178 on the capstone path, to "
        "[row 158](#row-158-closing-loop) when row 68 closed but DFT workflows meta prelude still "
        "lags on the opening-hinge path, to "
        "[row 138](#row-138-closing-loop) for the Row 68 ↔ Row 58 DFT workflows meta prelude audit on the "
        "opening-hinge path alone, to [row 177](#row-177-closing-loop) when Kohn–Sham meta prelude capstone still "
        "lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, to "
        "[row 58](#row-58-closing-loop) when only IX.2 → IX.3 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 178 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 158 \(row 68 ↔ row 58 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_178_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 178 is complete, proceed to [row 159](preface.md#skill-navigation-row-159) "
        "when row 68 closed but Handshake 3 meta prelude capstone still lags after verified "
        "DFT workflows meta prelude capstone on the capstone path, to [row 158](preface.md#skill-navigation-row-158) "
        "when Kohn–Sham meta prelude capstone is clean but DFT workflows meta prelude still lags on the "
        "opening-hinge path, to [row 138](preface.md#skill-navigation-row-138) for the Row 68 ↔ "
        "Row 58 DFT workflows meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 177](preface.md#skill-navigation-row-177) when Kohn–Sham meta prelude capstone still "
        "lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, to "
        "[row 58](preface.md#skill-navigation-row-58) for the IX.2 → IX.3 meta audit alone, to "
        "[row 39](preface.md#skill-navigation-row-39) when only the DFT workflows preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 178 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_178() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 178 skill checkpoint"
    end = "\n### Row 177 skill checkpoint"
    m = re.search(
        r"(### Row 158 skill checkpoint.*?)(?=\n### Row 159 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 158 template missing")
    block = polish_row_178(lift_158_to_178(m.group(1)))
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        raise SystemExit("preface row 178 checkpoint missing")
    path.write_text(text)
    print("preface: rebuilt row 178 checkpoint")


def rebuild_epilogue_row_178_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 178 closing loop"
    end = "### Row 177 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 178 loop missing")
    block = polish_row_178(
        lift_158_to_178(
            extract_between(
                text,
                "### Row 158 closing loop",
                "### Row 157 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 178 closing loop")


def fix_prologue_row_178() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 158) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion (row 178) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_178(lift_158_to_178(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-158"></span>Row 178 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-178"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-158"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_178(lift_158_to_178(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 178 compass/preview")


def rebuild_sources_row_178_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178"
    i178 = text.find(idx_key)
    if i178 < 0:
        print("sources: skip rebuild (row 178 marker missing)")
        return
    i178 = text.rfind("\n## ", 0, i178)
    start158 = "## Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 158)"
    i158 = text.find(start158)
    if i158 < 0:
        start158 = "row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158"
        i158 = text.find(start158)
        i158 = text.rfind("\n## ", 0, i158)
    if i158 < 0:
        raise SystemExit("sources row 158 template missing")
    j158_end = text.find("\n## Row 68 → Row 137", i158)
    if j158_end < 0:
        j158_end = text.find("\n## Row 68 → Row 119", i158)
    block = polish_row_178(
        export_index_to_dft_workflows_178(lift_158_to_178(text[i158:j158_end]))
    ).strip()
    block = block.replace(
        "(row 178) {#row68-row138-dft-workflows-meta-prelude-capstone-reunion-index-row-158}",
        f"(row 178) {{#{idx_key}}}",
        1,
    )
    j178_end = text.find("\n## Row 68 → Row 157", i178)
    if j178_end < 0:
        j178_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 57", i178)
    if j178_end < 0:
        j178_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 56", i178)
    text = text[:i178] + block + "\n\n\n" + text[j178_end:]
    path.write_text(text)
    print("sources: rebuilt row 178 index")


def rebuild_memory_row_178_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 178 baby picture"
    if anchor not in text:
        print("memory-sheet: row 178 baby missing — run add-row-178 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 158 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 157 baby picture", start + 1)
    baby158 = extract_between(
        text,
        "### Row 158 baby picture",
        "### Row 157 baby picture",
    )
    baby = polish_row_178(lift_158_to_178(baby158))
    baby = baby.replace(
        "### Row 178 baby picture (Row 68 → Row 138 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) "
        "{#row-158-baby-picture-row68-row138-dft-workflows-meta-prelude-capstone-reunion}",
        "### Row 178 baby picture (Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion) "
        "{#row-178-baby-picture-row68-row151-dft-workflows-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 178 baby picture")


def patch_row_177_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
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
    if "When row 177 is complete, proceed to [row 178]" in text:
        text = re.sub(
            r"When row 177 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 177 → row 178 proceed")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    marker = "### Row 178 baby picture"
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
    print("memory-sheet: deduped row 178 baby picture")


def global_polish_178_links() -> None:
    for rel in (
        "writings/preface/chapters/preface.md",
        "writings/prologue/chapters/00-many-scales.md",
        "writings/epilogue/chapters/multiscale.md",
        "writings/appendix/chapters/sources.md",
        "writings/appendix/chapters/memory-sheet.md",
    ):
        path = ROOT / rel
        text = path.read_text()
        text = text.replace(
            "Row 68 → Row 138 reunion index",
            "Row 68 → Row 151 reunion index",
        )
        text = text.replace(
            "[Preface: row 158 skill checkpoint](../preface.md#skill-navigation-row-178)",
            "[Preface: row 178 skill checkpoint](../preface.md#skill-navigation-row-178)",
        )
        path.write_text(text)
    print("writings: global row 178 link polish")


def main() -> None:
    remove_duplicate_corrupted_baby()
    global_polish_178_links()
    rebuild_preface_row_178()
    rebuild_epilogue_row_178_loop()
    fix_prologue_row_178()
    rebuild_sources_row_178_index()
    rebuild_memory_row_178_baby()
    patch_row_177_when_complete()


if __name__ == "__main__":
    main()
