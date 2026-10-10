#!/usr/bin/env python3
"""Add row 251 meta-stitch (Row 68 → Row 231 ↔ Row 51 homogenization meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 108,
}


def bump_meta_plus20(text: str) -> str:
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


def t231_to_251(text: str) -> str:
    protected = (
        ("row-251-", "__P251__"),
        ("skill-navigation-row-251", "__S251__"),
        ("prologue-preview-row-251", "__prologue-preview-row-251__"),
        ("{#row-251-closing-stitch}", "__{#row-251-closing-stitch}__"),
        ("{#row-251-closing-loop}", "__{#row-251-closing-loop}__"),
        (
            "row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251",
            "__row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251__",
        ),
        (
            "row-251-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion",
            "__row-251-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add231():
    spec = importlib.util.spec_from_file_location("add231", ROOT / "scripts/add-row-231.py")
    add231 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add231)
    return add231


def _compact_memory_baby() -> str:
    template = (
        "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}\n\n"
        "**Row 231 baby picture:** when row 68 closed the midpoint prelude and row 230 or row 231 closed "
        "DDD meta prelude capstone / homogenization meta prelude but **row 51's VII.2 → VII.3 audit or the "
        "Bridge → polycrystal handoff chain still feel like separate checklists on the full capstone path**, "
        "open the [Row 68 → Row 231 homogenization meta prelude capstone reunion index]"
        "(sources.md#row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251) — read "
        "[preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 250]"
        "(../preface.md#skill-navigation-row-250) or [preface row 231]"
        "(../preface.md#skill-navigation-row-231) DDD meta prelude capstone / homogenization meta prelude gate → "
        "[VII.2 Bridge to VII.3](../part07-defects/02-dislocation-dynamics.md#bridge-to-vii3) through "
        "[VII.3 opening hinge from VII.2](../part07-defects/03-polycrystal-and-fem-handoff.md#opening-hinge-vii2-to-vii3) "
        "aloud → [preface row 51](../preface.md#skill-navigation-row-51) five-step audit → confirm forest-density "
        "Lab act before DAMASK decks on the full capstone path.\n"
    )
    return t231_to_251(template) + "\n"


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 231 skill checkpoint")
    end = preface.index("\n\n### Row 232 skill checkpoint", start)
    row251_preface = t231_to_251(preface[start:end]).strip() + "\n\n"

    b231 = _load_add231()._build_blocks()
    epilogue_loop = t231_to_251(b231["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-231-closing-loop}", "{#row-251-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 231 closing loop (Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        "### Row 251 closing loop (Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion)",
        1,
    )
    for spill in ("\n\n\n\n### Row 250 closing loop", "\n\n\n\n### Row 251 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    return {
        "row251_preface": row251_preface,
        "prologue_compass": t231_to_251(b231["prologue_compass"]).replace("(row 231)", "(row 251)", 1),
        "prologue_stitch": t231_to_251(b231["prologue_stitch"].strip()) + "\n\n",
        "prologue_preview": t231_to_251(b231["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t231_to_251(b231["sources_table"]).replace("| 231 | Row 68 → Row 211", "| 251 | Row 68 → Row 231", 1),
        "sources_index": t231_to_251(b231["sources_index"]),
        "memory_table": (
            "| 251 | Meta | [Row 68 → Row 231 homogenization meta prelude capstone reunion index]"
            "(sources.md#row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251) · "
            "[preface row 251 skill checkpoint](../preface.md#skill-navigation-row-251) · "
            "[prologue row 251 preview](../prologue/00-many-scales.md#prologue-preview-row-251) · "
            "[prologue row 251 closing stitch](../prologue/00-many-scales.md#row-251-closing-stitch) · "
            "[epilogue row 251 closing loop](../epilogue/multiscale.md#row-251-closing-loop) | "
            "Row 68 closed but row 51 homogenization meta reunion feels disconnected from verified "
            "DDD meta prelude capstone on the full capstone path — read row 68 + row 250 or "
            "row 231 gate + VII.2 Bridge → VII.3 + row 51; "
            "[row 251 baby picture](#row-251-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": _compact_memory_baby(),
    }


ROW251_EPILOGUE_AFTER = (
    "### Row 250 closing loop (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion) "
    "{#row-250-closing-loop}"
)

ROW251_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

PROLOGUE_STITCH_ANCHOR = (
    "**Row 250 closing stitch (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion).** {#row-250-closing-stitch}"
)

ROW250_STITCH_OLD = "before row 251 homogenization meta prelude capstone reunion opens on the full capstone path."
ROW250_STITCH_NEW = "before row 252 atomistic meta prelude capstone reunion opens on the full capstone path."


def _epilogue_has_row251_after_250(text: str) -> bool:
    if ROW251_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW251_EPILOGUE_AFTER)
    window = text[idx : idx + 15000]
    return "{#row-251-closing-loop}" in window and "memory sheet row 251" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 251 skill checkpoint" in preface:
        print("preface: row 251 already present")
    else:
        if "### Row 250 skill checkpoint" not in preface:
            raise SystemExit("row 250 must exist before row 251")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row251_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 251")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "homogenization meta prelude capstone reunion (row 251) |" not in prologue:
        needle = (
            "| Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion (row 250) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 250 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if PROLOGUE_STITCH_ANCHOR in prologue and "**Row 251 closing stitch" not in prologue:
            prologue = prologue.replace(PROLOGUE_STITCH_ANCHOR, b["prologue_stitch"] + PROLOGUE_STITCH_ANCHOR, 1)
        preview_anchor = '| <span id="prologue-preview-row-250"></span>Row 249 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        if '<span id="prologue-preview-row-251">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW250_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW250_STITCH_OLD, ROW250_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 251")
    else:
        print("prologue: row 251 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if not _epilogue_has_row251_after_250(epilogue):
        if ROW251_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 250 anchor not found")
        if ROW251_EPILOGUE_BEFORE not in epilogue.split(ROW251_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 250")
        head, tail = epilogue.split(ROW251_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW251_EPILOGUE_BEFORE, 1)
        if "{#row-251-closing-loop}" not in mid:
            mid = mid.rstrip() + "\n\n" + b["epilogue_loop"]
        epilogue_path.write_text(head + ROW251_EPILOGUE_AFTER + mid + ROW251_EPILOGUE_BEFORE + rest)
        print("epilogue: added row 251")
    else:
        print("epilogue: row 251 closing loop already present after row 250")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row231-homogenization-meta-prelude-capstone-reunion-index-row-251" not in sources:
        sources = sources.replace(
            "| 250 | Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone",
            b["sources_table"] + "| 250 | Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone",
            1,
        )
        src211_header = (
            "## Row 68 → Row 191 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 211)"
        )
        if src211_header in sources and b["sources_index"].strip()[:80] not in sources:
            sources = sources.replace(src211_header, b["sources_index"] + src211_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 251")
    else:
        print("sources: row 251 index already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-251-baby-picture-row68-row231" not in memory:
        mem_needle = "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]"
        if mem_needle in memory and "| 250 | Meta |" not in memory.split(mem_needle, 1)[0][-500:]:
            memory = memory.replace(
                mem_needle,
                mem_needle,
                1,
            )
        if "| 250 | Meta |" not in memory:
            memory = memory.replace(
                mem_needle + "(sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249)",
                mem_needle + "(sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249)",
                1,
            )
            # insert 250 table row after 249 if add-row-250 skipped memory table
            row250_table = (
                "| 250 | Meta | [Row 68 → Row 230 DDD meta prelude capstone reunion index]"
                "(sources.md#row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250) · "
                "[preface row 250 skill checkpoint](../preface.md#skill-navigation-row-250) · "
                "[prologue row 250 preview](../prologue/00-many-scales.md#prologue-preview-row-250) · "
                "[prologue row 250 closing stitch](../prologue/00-many-scales.md#row-250-closing-stitch) · "
                "[epilogue row 250 closing loop](../epilogue/multiscale.md#row-250-closing-loop) | "
                "Row 68 closed but row 50 DDD meta reunion feels disconnected from verified taxonomy meta "
                "prelude capstone on the full capstone path — read row 68 + row 249 or row 230 gate + "
                "VII.1 Bridge → VII.2 + row 50; "
                "[row 250 baby picture](#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion) |\n"
            )
            full249 = (
                "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]"
                "(sources.md#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249) · "
            )
            if full249 in memory:
                memory = memory.replace(full249, full249, 1)  # no-op anchor locate
                line_start = memory.index(full249)
                line_end = memory.find("\n", line_start)
                memory = memory[: line_end + 1] + row250_table + memory[line_end + 1 :]
        if "| 251 | Meta |" not in memory:
            mem250 = "| 250 | Meta | [Row 68 → Row 230 DDD meta prelude capstone reunion index]"
            if mem250 in memory:
                memory = memory.replace(
                    mem250,
                    b["memory_table"] + mem250,
                    1,
                )
        baby_anchors = (
            "### Row 250 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
            "### Row 230 baby picture {#row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion}",
        )
        baby_anchor = next((a for a in baby_anchors if a in memory), None)
        if not baby_anchor:
            raise SystemExit("memory row 250 baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 251")
    else:
        print("memory-sheet: row 251 baby already present")


if __name__ == "__main__":
    main()
