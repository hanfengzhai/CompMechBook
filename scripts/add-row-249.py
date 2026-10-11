#!/usr/bin/env python3
"""Add row 249 meta-stitch (Row 68 → Row 229 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 108,
}


def bump_meta_plus20(text: str) -> str:
    """Shift capstone-path meta row numbers by +20; preserve plot-spine row ids."""

    def repl(m: re.Match[str]) -> str:
        n = int(m.group(1))
        if n in PRESERVE_ROW_NUMS:
            return m.group(0)
        return m.group(0).replace(str(n), str(n + 20))

    for pat in (
        r"(?<![0-9])row (\d+)",
        r"(?<![0-9])Row (\d+)",
        r"skill-navigation-row-(\d+)",
        r"prologue-preview-row-(\d+)",
        r"row-(\d+)-closing",
        r"row-(\d+)-baby-picture",
        r"row68-row(\d+)",
        r"reunion-index-row-(\d+)",
        r"index-row-(\d+)",
    ):
        text = re.sub(pat, repl, text)
    return text


def t229_to_249(text: str) -> str:
    protected = (
        ("row-249-", "__P249__"),
        ("skill-navigation-row-249", "__S249__"),
        ("prologue-preview-row-249", "__prologue-preview-row-249__"),
        ("{#row-249-closing-stitch}", "__{#row-249-closing-stitch}__"),
        ("{#row-249-closing-loop}", "__{#row-249-closing-loop}__"),
        (
            "row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249",
            "__row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249__",
        ),
        (
            "row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion",
            "__row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add229():
    spec = importlib.util.spec_from_file_location("add229", ROOT / "scripts/add-row-229.py")
    add229 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add229)
    return add229


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 229 skill checkpoint")
    end = preface.index("\n\n### Row 230 skill checkpoint", start)
    row249_preface = t229_to_249(preface[start:end]).strip() + "\n\n"

    b229 = _load_add229()._build_blocks()
    epilogue_loop = t229_to_249(b229["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace(
        "### Row 249 closing loop (Row 68 → Row 229",
        "### Row 229 closing loop (Row 68 → Row 229",
        1,
    )
    for spill in ("\n\n\n\n### Row 248 closing loop", "\n\n\n\n### Row 249 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    return {
        "row249_preface": row249_preface,
        "prologue_compass": t229_to_249(b229["prologue_compass"]),
        "prologue_stitch": t229_to_249(b229["prologue_stitch"]),
        "prologue_preview": t229_to_249(b229["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t229_to_249(b229["sources_table"]).replace(
            "| 229 | Row 68 → Row 209", "| 249 | Row 68 → Row 229", 1
        ),
        "memory_table": (
            "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]"
            "(sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249) · "
            "[preface row 249 skill checkpoint](../preface.md#skill-navigation-row-249) · "
            "[prologue row 249 preview](../prologue/00-many-scales.md#prologue-preview-row-249) · "
            "[prologue row 249 closing stitch](../prologue/00-many-scales.md#row-249-closing-stitch) · "
            "[epilogue row 249 closing loop](../epilogue/multiscale.md#row-249-closing-loop) | "
            "Row 68 closed but row 49 taxonomy meta reunion feels disconnected from verified "
            "midpoint meta prelude capstone on the full capstone path — read row 68 + row 248 or "
            "row 229 gate + VII.0 Bridge → VII.1 + row 49; confirm `hardening.yaml` beside Act IV; "
            "[row 249 baby picture](#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion) |\n"
        ),
        "sources_index": t229_to_249(b229["sources_index"]),
        "memory_baby": t229_to_249(b229["memory_baby"]).replace(
            "### Row 249 baby picture",
            "### Row 249 baby picture {#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion}",
            1,
        ),
    }


PROLOGUE_STITCH_ANCHOR = (
    "**Row 248 closing stitch (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-248-closing-stitch}"
)

ROW249_INSERT_MARKER = (
    "### Row 228 closing loop (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-248-closing-loop}"
)

ROW248_STITCH_OLD = "before row 249 taxonomy meta prelude capstone reunion opens on the full capstone path."
ROW248_STITCH_NEW = "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."


def _epilogue_has_row249_at_capstone(text: str) -> bool:
    if ROW249_INSERT_MARKER not in text:
        return False
    idx = text.index(ROW249_INSERT_MARKER)
    window = text[max(0, idx - 12000) : idx]
    return "{#row-249-closing-loop}" in window and "memory sheet row 249" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 249 skill checkpoint" in preface:
        print("preface: row 249 already present")
    else:
        if "### Row 248 skill checkpoint" not in preface:
            raise SystemExit("row 248 must exist before row 249")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row249_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 249")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "taxonomy meta prelude capstone reunion (row 249) |" not in prologue:
        needle = (
            "| Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 248) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 248 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue:
            prologue = prologue.replace(
                PROLOGUE_STITCH_ANCHOR,
                b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR,
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-248"></span>Row 248 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW248_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW248_STITCH_OLD, ROW248_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 249")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if not _epilogue_has_row249_at_capstone(epilogue):
        marker = ROW249_INSERT_MARKER
        if marker not in epilogue:
            raise SystemExit("epilogue row 248 insert anchor not found")
        epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 249")
    else:
        print("epilogue: row 249 closing loop already present at capstone anchor")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249" not in sources:
        sources = sources.replace(
            "| 248 | Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone",
            b["sources_table"] + "| 248 | Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone",
            1,
        )
        src_header = (
            "## Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 248) "
            "{#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248}"
        )
        if src_header in sources and b["sources_index"].strip()[:80] not in sources:
            sources = sources.replace(src_header, b["sources_index"] + src_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 249")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-249-baby-picture-row68-row229" not in memory:
        memory = memory.replace(
            "| 248 | Meta | [Row 68 → Row 228 midpoint meta prelude capstone reunion index](sources.md#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248)",
            b["memory_table"]
            + "| 248 | Meta | [Row 68 → Row 228 midpoint meta prelude capstone reunion index](sources.md#row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248)",
            1,
        )
        baby_anchor = (
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 249")
    else:
        print("memory-sheet: row 249 baby already present")


if __name__ == "__main__":
    main()
