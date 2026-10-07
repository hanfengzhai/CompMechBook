#!/usr/bin/env python3
"""Add row 229 meta-stitch (Row 68 → Row 209 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]


def shift_meta_bump(text: str, delta: int = 20) -> str:
    """Shift capstone-path row references (100–230) by delta for meta-stitch copy."""
    protected: dict[str, str] = {}

    def protect(pat: str, flags: int = 0) -> None:
        for i, m in enumerate(re.finditer(pat, text if not protected else "", flags)):
            pass

    out = text
    for tag in ("__R189__", "__R190__", "__R209__", "__R210__", "__R229__", "__R230__"):
        out = out.replace(tag, tag)

    def in_band(n: int) -> bool:
        return 100 <= n <= 230

    def repl_row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"row {n + delta}" if in_band(n) else m.group(0)

    def repl_Row(m: re.Match[str]) -> str:
        n = int(m.group(1))
        return f"Row {n + delta}" if in_band(n) else m.group(0)

    out = re.sub(r"row68-row(\d{3})", lambda m: f"row68-row{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0), out)
    out = re.sub(
        r"index-row-(\d{3})",
        lambda m: f"index-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"skill-navigation-row-(\d{3})",
        lambda m: f"skill-navigation-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"prologue-preview-row-(\d{3})",
        lambda m: f"prologue-preview-row-{int(m.group(1)) + delta}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(
        r"row-(\d{3})-(closing-stitch|closing-loop|baby-picture)",
        lambda m: f"row-{int(m.group(1)) + delta}-{m.group(2)}" if in_band(int(m.group(1))) else m.group(0),
        out,
    )
    out = re.sub(r"\brow (\d{3})\b", repl_row, out)
    out = re.sub(r"\bRow (\d{3})\b", repl_Row, out)
    return out


def bump209_to_229(text: str) -> str:
    return shift_meta_bump(text, 20)


def _load_add209():
    spec = importlib.util.spec_from_file_location("add209", ROOT / "scripts/add-row-209.py")
    add209 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add209)
    return add209


def _build_blocks() -> dict[str, str]:
    add209 = _load_add209()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 209 skill checkpoint")
    end = preface.index("\n\n### Row 210 skill checkpoint", start)
    row229_preface = bump209_to_229(preface[start:end]) + "\n\n"

    b209 = add209._build_blocks()
    prologue_stitch = bump209_to_229(
        b209["prologue_stitch"]
        .replace("{#row-209-closing-stitch}", "{#row-229-closing-stitch}")
        .replace(
            "**Row 209 closing stitch (Row 68 → Row 189",
            "**Row 229 closing stitch (Row 68 → Row 209",
        )
    )
    prologue_compass = bump209_to_229(b209["prologue_compass"])
    prologue_preview = bump209_to_229(b209["prologue_preview"])

    epilogue = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    row209_loop_anchor = (
        "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
        "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
    )
    row210_loop_end = (
        "### Row 210 closing loop (Row 68 → Row 190 Row 68 → Row 50 "
        "DDD meta prelude capstone reunion) {#row-210-closing-loop}"
    )
    if row209_loop_anchor in epilogue and row210_loop_end in epilogue.split(row209_loop_anchor, 1)[1]:
        ep_slice = row209_loop_anchor + epilogue.split(row209_loop_anchor, 1)[1].split(row210_loop_end, 1)[0]
    else:
        ep_slice = b209["epilogue_loop"]
    epilogue_loop = bump209_to_229(ep_slice)
    epilogue_loop = epilogue_loop.replace("{#row-209-closing-loop}", "{#row-229-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 229 closing loop (Row 68 → Row 189",
        "### Row 229 closing loop (Row 68 → Row 209",
        1,
    )
    epilogue_loop = epilogue_loop.rstrip() + "\n\n"

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src209_header = (
        "## Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 209) "
        "{#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209}"
    )
    next210_header = (
        "## Row 68 → Row 190 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 210)"
    )
    sources_index = bump209_to_229(sources.split(src209_header, 1)[1].split(next210_header, 1)[0])
    sources_index = (
        "## Row 68 → Row 209 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 229) "
        "{#row68-row209-taxonomy-meta-prelude-capstone-reunion-index-row-229}\n"
        + sources_index.lstrip("\n")
    )

    sources_table = bump209_to_229(b209["sources_table"])
    sources_table = sources_table.replace("| 209 | Row 68 → Row 189", "| 229 | Row 68 → Row 209", 1)

    memory_table = bump209_to_229(b209["memory_table"])
    memory_table = memory_table.replace("| 209 | Meta |", "| 229 | Meta |", 1)
    memory_baby = bump209_to_229(b209["memory_baby"]).rstrip() + "\n\n"

    preface209 = preface[start:end]
    tail_old = preface209.split("When row 209 is complete", 1)[1]
    row228_tail_new = "When row 228 is complete" + bump209_to_229("When row 209 is complete" + tail_old).split("When row 229 is complete", 1)[1]

    return {
        "row229_preface": row229_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
        "row228_tail_new": row228_tail_new,
    }


ROW228_EPILOGUE_OLD = (
    "Proceed to [row 189](#row-189-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 228 on the full capstone path,"
)
ROW228_EPILOGUE_NEW = (
    "Proceed to [row 229](#row-229-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 228 on the full capstone path,"
)

ROW228_BABY_OLD = (
    "when opening [row 229](preface.md#skill-navigation-row-229) before row 49 closes on the full capstone path"
)
ROW228_BABY_NEW = (
    "when opening [row 229](preface.md#skill-navigation-row-229) before row 49 closes on the full capstone path"
)

ROW228_STITCH_OLD = (
    "before row 229 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW228_STITCH_NEW = (
    "before row 230 DDD meta prelude capstone reunion opens on the full capstone path."
)


def _strip_premature_row229_epilogue(epilogue: str) -> str:
    """Remove placeholder Row 229 loop lacking {#row-229-closing-loop}."""
    if "{#row-229-closing-loop}" in epilogue:
        return epilogue
    return re.sub(
        r"\n### Row 229 closing loop[\s\S]*?(?=\n### Row 210 closing loop)",
        "\n",
        epilogue,
        count=1,
    )


def main() -> None:
    b = _build_blocks()

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    copper = "\n## The copper wire through the book"
    if "### Row 229 skill checkpoint" in preface:
        print("preface: row 229 already present")
    else:
        if "### Row 228 skill checkpoint" not in preface:
            raise SystemExit("row 228 must exist before row 229")
        if "When row 208 is complete" in preface:
            idx = preface.index("When row 208 is complete")
            end = preface.find("\n\n\n\n", idx)
            if end == -1:
                end = preface.find(copper, idx)
            old_tail = preface[idx:end]
            preface = preface.replace(old_tail, b["row228_tail_new"], 1)
        preface = preface.replace(copper, "\n" + b["row229_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 229")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "**Row 229 closing stitch" not in prologue:
        needle = "| Row 68 → Row 208 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 208) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 228 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 229 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 228 closing stitch",
                b["prologue_stitch"] + "**Row 228 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-228"></span>Row 228 preview'
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW228_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW228_STITCH_OLD, ROW228_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 229")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    epilogue = _strip_premature_row229_epilogue(epilogue)
    if "{#row-229-closing-loop}" not in epilogue:
        if ROW228_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW228_EPILOGUE_OLD, ROW228_EPILOGUE_NEW, 1)
        marker = (
            "### Row 209 closing loop (Row 68 → Row 189 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-209-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 209 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 229")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row209-taxonomy-meta-prelude-capstone-reunion-index-row-229" not in sources:
        sources = sources.replace(
            "| 209 | Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 209 | Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        sources = sources.replace(
            src209_header := (
                "## Row 68 → Row 189 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 209) "
                "{#row68-row189-taxonomy-meta-prelude-capstone-reunion-index-row-209}"
            ),
            b["sources_index"] + src209_header,
            1,
        )
        sources_path.write_text(sources)
        print("sources: added row 229")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-229-baby-picture-row68-row209" not in memory:
        memory = memory.replace(
            "| 209 | Meta | [Row 68 → Row 189 taxonomy meta prelude capstone reunion index]",
            b["memory_table"] + "| 209 | Meta | [Row 68 → Row 189 taxonomy meta prelude capstone reunion index]",
            1,
        )
        memory = memory.replace(
            baby_anchor := (
                "### Row 209 baby picture {#row-209-baby-picture-row68-row189-taxonomy-meta-prelude-capstone-reunion}"
            ),
            b["memory_baby"] + baby_anchor,
            1,
        )
        if ROW228_BABY_OLD in memory:
            memory = memory.replace(ROW228_BABY_OLD, ROW228_BABY_NEW)
        memory_path.write_text(memory)
        print("memory-sheet: added row 229")


if __name__ == "__main__":
    main()
