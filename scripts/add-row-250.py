#!/usr/bin/env python3
"""Add row 250 meta-stitch (Row 68 → Row 230 ↔ Row 50 DDD meta prelude capstone reunion, full capstone path)."""
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


def t230_to_250(text: str) -> str:
    protected = (
        ("row-250-", "__P250__"),
        ("skill-navigation-row-250", "__S250__"),
        ("prologue-preview-row-250", "__prologue-preview-row-250__"),
        ("{#row-250-closing-stitch}", "__{#row-250-closing-stitch}__"),
        ("{#row-250-closing-loop}", "__{#row-250-closing-loop}__"),
        (
            "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
            "__row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250__",
        ),
        (
            "row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion",
            "__row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add230():
    spec = importlib.util.spec_from_file_location("add230", ROOT / "scripts/add-row-230.py")
    add230 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add230)
    return add230


def _compact_memory_baby() -> str:
    memory = (ROOT / "writings/appendix/chapters/memory-sheet.md").read_text()
    anchor = "{#row-230-baby-picture-row68-row210-ddd-meta-prelude-capstone-reunion}"
    start = memory.index(anchor)
    start = memory.rfind("\n### ", 0, start) + 1
    end = memory.find("\n\nWhen row 230 feels disconnected", start)
    if end == -1:
        end = memory.find("\n\n```", start) + 200
    chunk = memory[start:end].strip()
    chunk = t230_to_250(chunk)
    chunk = chunk.replace(
        "### Row 250 baby picture (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
        1,
    )
    chunk = chunk.replace(
        "### Row 250 baby picture (Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
        1,
    )
    return chunk + "\n\n"


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 230 skill checkpoint")
    end = preface.index("\n\n### Row 231 skill checkpoint", start)
    row250_preface = t230_to_250(preface[start:end]).strip() + "\n\n"

    b230 = _load_add230()._build_blocks()
    epilogue_loop = t230_to_250(b230["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-230-closing-loop}", "{#row-250-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 230 closing loop (Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        "### Row 250 closing loop (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion)",
        1,
    )
    for spill in ("\n\n\n\n### Row 249 closing loop", "\n\n\n\n### Row 250 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src230_header = (
        "## Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 230)"
    )
    next231_header = (
        "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211)"
    )
    i = sources.index(src230_header)
    j = sources.index(next231_header, i + len(src230_header))
    sources_index = t230_to_250(sources[i:j])
    sources_index = sources_index.replace(
        "(row 230) {#row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230}",
        "(row 250) {#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230",
        "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
    )

    return {
        "row250_preface": row250_preface,
        "prologue_compass": t230_to_250(b230["prologue_compass"]).replace("(row 230)", "(row 250)", 1),
        "prologue_stitch": t230_to_250(b230["prologue_stitch"].strip()) + "\n\n",
        "prologue_preview": t230_to_250(b230["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t230_to_250(b230["sources_table"]).replace("| 230 | Row 68 → Row 210", "| 250 | Row 68 → Row 230", 1),
        "sources_index": sources_index,
        "memory_table": (
            "| 250 | Meta | [Row 68 → Row 230 DDD meta prelude capstone reunion index]"
            "(sources.md#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250) · "
            "[preface row 250 skill checkpoint](../preface.md#skill-navigation-row-250) · "
            "[prologue row 250 preview](../prologue/00-many-scales.md#prologue-preview-row-250) · "
            "[prologue row 250 closing stitch](../prologue/00-many-scales.md#row-250-closing-stitch) · "
            "[epilogue row 250 closing loop](../epilogue/multiscale.md#row-250-closing-loop) | "
            "Row 68 closed but row 50 DDD meta reunion feels disconnected from verified "
            "taxonomy meta prelude capstone on the full capstone path — read row 68 + row 249 or "
            "row 230 gate + VII.1 Bridge → VII.2 + row 50; "
            "[row 250 baby picture](#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": _compact_memory_baby(),
    }


PROLOGUE_STITCH_ANCHOR = (
    "**Row 249 closing stitch (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-249-closing-stitch}"
)

ROW250_EPILOGUE_AFTER = (
    "### Row 249 closing loop (Row 68 → Row 229 Row 68 → Row 49 "
    "taxonomy meta prelude capstone reunion) {#row-249-closing-loop}"
)

ROW250_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

ROW249_STITCH_OLD = "before row 250 DDD meta prelude capstone reunion opens on the full capstone path."
ROW249_STITCH_NEW = "before row 251 homogenization meta prelude capstone reunion opens on the full capstone path."


def _epilogue_has_row250_after_249(text: str) -> bool:
    if ROW250_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW250_EPILOGUE_AFTER)
    window = text[idx : idx + 15000]
    return "{#row-250-closing-loop}" in window and "memory sheet row 250" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 250 skill checkpoint" in preface:
        print("preface: row 250 already present")
    else:
        if "### Row 249 skill checkpoint" not in preface:
            raise SystemExit("row 249 must exist before row 250")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row250_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 250")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "DDD meta prelude capstone reunion (row 250) |" not in prologue:
        needle = "| Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 249) |"
        if needle not in prologue:
            raise SystemExit("prologue compass row 249 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue and "**Row 250 closing stitch" not in prologue:
            prologue = prologue.replace(PROLOGUE_STITCH_ANCHOR, b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR, 1)
        preview_anchor = '| <span id="prologue-preview-row-249"></span>Row 249 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        if '<span id="prologue-preview-row-250">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW249_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW249_STITCH_OLD, ROW249_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 250")
    else:
        print("prologue: row 250 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if not _epilogue_has_row250_after_249(epilogue):
        if ROW250_EPILOGUE_AFTER not in epilogue or ROW250_EPILOGUE_BEFORE not in epilogue:
            raise SystemExit("epilogue row 249/247 insert anchors not found")
        head, tail = epilogue.split(ROW250_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW250_EPILOGUE_BEFORE, 1)
        if "{#row-250-closing-loop}" not in mid:
            mid = mid.rstrip() + "\n\n" + b["epilogue_loop"]
        epilogue_path.write_text(head + ROW250_EPILOGUE_AFTER + mid + ROW250_EPILOGUE_BEFORE + rest)
        print("epilogue: added row 250")
    else:
        print("epilogue: row 250 closing loop already present after row 249")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250" not in sources:
        sources = sources.replace(
            "| 249 | Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 249 | Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        if src230 := (
            "## Row 68 → Row 210 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 230)"
        ):
            if src230 in sources and b["sources_index"].strip()[:80] not in sources:
                sources = sources.replace(src230, b["sources_index"] + src230, 1)
        sources_path.write_text(sources)
        print("sources: added row 250")
    else:
        print("sources: row 250 index already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-250-baby-picture-row68-row230" not in memory:
        memory = memory.replace(
            "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]",
            b["memory_table"]
            + "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]",
            1,
        )
        baby_anchor = (
            "### Row 248 baby picture {#row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}"
        )
        if baby_anchor not in memory:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 250")
    else:
        print("memory-sheet: row 250 baby already present")


if __name__ == "__main__":
    main()
