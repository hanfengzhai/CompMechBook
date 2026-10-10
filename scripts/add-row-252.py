#!/usr/bin/env python3
"""Add row 252 meta-stitch (Row 68 → Row 232 ↔ Row 52 atomistic meta prelude capstone reunion, full capstone path)."""
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


def t232_to_252(text: str) -> str:
    protected = (
        ("row-252-", "__P252__"),
        ("skill-navigation-row-252", "__S252__"),
        ("prologue-preview-row-252", "__prologue-preview-row-252__"),
        ("{#row-252-closing-stitch}", "__{#row-252-closing-stitch}__"),
        ("{#row-252-closing-loop}", "__{#row-252-closing-loop}__"),
        (
            "row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252",
            "__row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252__",
        ),
        (
            "row-252-baby-picture-row68-row232-atomistic-meta-prelude-capstone-reunion",
            "__row-252-baby-picture-row68-row232-atomistic-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add232():
    spec = importlib.util.spec_from_file_location("add232", ROOT / "scripts/add-row-232.py")
    add232 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add232)
    return add232


def _compact_memory_baby() -> str:
    template = (
        "### Row 232 baby picture {#row-232-baby-picture-row68-row212-atomistic-meta-prelude-capstone-reunion}\n\n"
        "**Row 232 baby picture:** when row 68 closed the midpoint prelude and row 251 or row 232 closed "
        "homogenization meta prelude capstone / atomistic meta prelude but **row 52's VII.3 → VIII.1 audit or the "
        "Bridge → phase-space chain still feel like separate checklists on the full capstone path**, "
        "open the [Row 68 → Row 232 atomistic meta prelude capstone reunion index]"
        "(sources.md#row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252) — read "
        "[preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 251]"
        "(../preface.md#skill-navigation-row-251) or [preface row 232]"
        "(../preface.md#skill-navigation-row-232) homogenization meta prelude capstone / atomistic meta prelude gate → "
        "[VII.3 Bridge to Part VIII](../part07-defects/03-polycrystal-and-fem-handoff.md#bridge-to-part-viii) through "
        "[VIII.1 opening hinge from VII.3](../part08-md/01-potentials-phase-space.md#opening-hinge-vii3-to-viii1) "
        "aloud → [preface row 52](../preface.md#skill-navigation-row-52) five-step audit → confirm handoff Lab act "
        "step 5 before LAMMPS decks on the full capstone path.\n"
    )
    return t232_to_252(template) + "\n"


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 232 skill checkpoint")
    end = preface.index("\n\n### Row 233 skill checkpoint", start)
    row252_preface = t232_to_252(preface[start:end]).strip() + "\n\n"

    b232 = _load_add232()._build_blocks()
    epilogue_loop = t232_to_252(b232["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-232-closing-loop}", "{#row-252-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 232 closing loop (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion)",
        "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion)",
        1,
    )
    for spill in ("\n\n\n\n### Row 251 closing loop", "\n\n\n\n### Row 252 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src232_header = (
        "## Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 232)"
    )
    next192_header = (
        "## Row 68 → Row 192 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 212)"
    )
    i = sources.index(src232_header)
    j = sources.index(next192_header, i + len(src232_header))
    sources_index = t232_to_252(sources[i:j])
    sources_index = sources_index.replace(
        "(row 232) {#row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232}",
        "(row 252) {#row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row212-atomistic-meta-prelude-capstone-reunion-index-row-232",
        "row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252",
    )

    return {
        "row252_preface": row252_preface,
        "prologue_compass": t232_to_252(b232["prologue_compass"]).replace("(row 232)", "(row 252)", 1),
        "prologue_stitch": t232_to_252(b232["prologue_stitch"].strip()) + "\n\n",
        "prologue_preview": t232_to_252(b232["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t232_to_252(b232["sources_table"]).replace("| 232 | Row 68 → Row 212", "| 252 | Row 68 → Row 232", 1),
        "sources_index": sources_index,
        "memory_table": (
            "| 252 | Meta | [Row 68 → Row 232 atomistic meta prelude capstone reunion index]"
            "(sources.md#row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252) · "
            "[preface row 252 skill checkpoint](../preface.md#skill-navigation-row-252) · "
            "[prologue row 252 preview](../prologue/00-many-scales.md#prologue-preview-row-252) · "
            "[prologue row 252 closing stitch](../prologue/00-many-scales.md#row-252-closing-stitch) · "
            "[epilogue row 252 closing loop](../epilogue/multiscale.md#row-252-closing-loop) | "
            "Row 68 closed but row 52 atomistic meta reunion feels disconnected from verified "
            "homogenization meta prelude capstone on the full capstone path — read row 68 + row 251 or "
            "row 232 gate + VII.3 Bridge → VIII.1 + row 52; "
            "[row 252 baby picture](#row-252-baby-picture-row68-row232-atomistic-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": _compact_memory_baby(),
    }


ROW252_EPILOGUE_AFTER = (
    "### Row 231 closing loop (Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion) "
    "{#row-251-closing-loop}"
)

ROW252_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

PROLOGUE_STITCH_ANCHORS = (
    "**Row 251 closing stitch (Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-251-closing-stitch}",
    "**Row 231 closing stitch (Row 68 → Row 211 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-231-closing-stitch}",
    "**Row 250 closing stitch (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion).** {#row-250-closing-stitch}",
)

ROW251_STITCH_OLD = "before row 252 atomistic meta prelude capstone reunion opens on the full capstone path."
ROW251_STITCH_NEW = "before row 253 dynamics meta prelude capstone reunion opens on the full capstone path."


def _epilogue_has_row252_after_251(text: str) -> bool:
    if ROW252_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW252_EPILOGUE_AFTER)
    window = text[idx : idx + 15000]
    return "{#row-252-closing-loop}" in window and "memory sheet row 252" in window


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 252 skill checkpoint" in preface.split(copper, 1)[0]:
        print("preface: row 252 capstone already present")
    else:
        if "### Row 251 skill checkpoint" not in preface:
            raise SystemExit("row 251 must exist before row 252")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row252_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 252")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "atomistic meta prelude capstone reunion (row 252) |" not in prologue:
        needle = (
            "| Row 68 → Row 231 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 251) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 251 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 252 closing stitch" not in prologue:
            for anchor in PROLOGUE_STITCH_ANCHORS:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-251"></span>Row 231 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        if '<span id="prologue-preview-row-252">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW251_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW251_STITCH_OLD, ROW251_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 252")
    else:
        print("prologue: row 252 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if not _epilogue_has_row252_after_251(epilogue):
        if ROW252_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 251 anchor not found")
        if ROW252_EPILOGUE_BEFORE not in epilogue.split(ROW252_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 251")
        head, tail = epilogue.split(ROW252_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW252_EPILOGUE_BEFORE, 1)
        if "{#row-252-closing-loop}" not in mid:
            mid = mid.rstrip() + "\n\n" + b["epilogue_loop"]
        epilogue_path.write_text(head + ROW252_EPILOGUE_AFTER + mid + ROW252_EPILOGUE_BEFORE + rest)
        print("epilogue: added row 252")
    else:
        print("epilogue: row 252 closing loop already present after row 251")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row232-atomistic-meta-prelude-capstone-reunion-index-row-252" not in sources:
        needle = "| 192 | Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone"
        if needle not in sources:
            raise SystemExit("sources atomistic table anchor not found")
        sources = sources.replace(
            needle,
            b["sources_table"] + needle,
            1,
        )
        src232_header = (
            "## Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 232)"
        )
        if src232_header in sources and b["sources_index"].strip()[:80] not in sources:
            sources = sources.replace(src232_header, b["sources_index"] + src232_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 252")
    else:
        print("sources: row 252 index already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-252-baby-picture-row68-row232" not in memory:
        if "| 252 | Meta |" not in memory:
            mem251 = "| 251 | Meta | [Row 68 → Row 231 homogenization meta prelude capstone reunion index]"
            if mem251 in memory:
                memory = memory.replace(
                    mem251,
                    b["memory_table"] + mem251,
                    1,
                )
        baby_anchors = (
            "### Row 251 baby picture {#row-251-baby-picture-row68-row231-homogenization-meta-prelude-capstone-reunion}",
            "### Row 231 baby picture {#row-231-baby-picture-row68-row211-homogenization-meta-prelude-capstone-reunion}",
        )
        baby_anchor = next((a for a in baby_anchors if a in memory), None)
        if not baby_anchor:
            raise SystemExit("memory row 251 baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 252")
    else:
        print("memory-sheet: row 252 baby already present")


if __name__ == "__main__":
    main()
