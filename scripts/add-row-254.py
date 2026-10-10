#!/usr/bin/env python3
"""Add row 254 meta-stitch (Row 68 → Row 234 ↔ Row 54 export meta prelude capstone reunion, full capstone path)."""
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


def fix_capstone_anchor_overbump(text: str) -> str:
    """Undo accidental +20 on capstone reunion anchors (253/254 → 273/274)."""
    return (
        text.replace("reunion-index-row-274", "reunion-index-row-254")
        .replace("reunion-index-row-273", "reunion-index-row-253")
        .replace("skill-navigation-row-273", "skill-navigation-row-253")
        .replace("prologue-preview-row-273", "prologue-preview-row-253")
        .replace("row-273-closing-stitch", "row-253-closing-stitch")
        .replace("row-273-closing-loop", "row-253-closing-loop")
        .replace("prologue-preview-row-274", "prologue-preview-row-254")
        .replace("row-274-closing-stitch", "row-254-closing-stitch")
        .replace("row-274-closing-loop", "row-254-closing-loop")
        .replace("skill-navigation-row-274", "skill-navigation-row-254")
    )


def t234_to_254(text: str) -> str:
    protected = (
        ("row-254-", "__P254__"),
        ("skill-navigation-row-254", "__S254__"),
        ("prologue-preview-row-254", "__prologue-preview-row-254__"),
        ("{#row-254-closing-stitch}", "__{#row-254-closing-stitch}__"),
        ("{#row-254-closing-loop}", "__{#row-254-closing-loop}__"),
        (
            "row68-row234-export-meta-prelude-capstone-reunion-index-row-254",
            "__row68-row234-export-meta-prelude-capstone-reunion-index-row-254__",
        ),
        (
            "row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion",
            "__row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return fix_capstone_anchor_overbump(out)


def _load_add234():
    spec = importlib.util.spec_from_file_location("add234", ROOT / "scripts/add-row-234.py")
    add234 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add234)
    return add234


def _compact_memory_baby() -> str:
    template = (
        "### Row 234 baby picture {#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion}\n\n"
        "**Row 234 baby picture:** when row 68 closed the midpoint prelude and row 233 or row 214 closed "
        "dynamics meta prelude capstone / export meta prelude but **row 54's VIII.2 → VIII.3 audit or the "
        "Bridge → pedigree chain still feel like separate checklists on the full capstone path**, "
        "open the [Row 68 → Row 234 export meta prelude capstone reunion index]"
        "(sources.md#row68-row214-export-meta-prelude-capstone-reunion-index-row-234) — read "
        "[preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 233]"
        "(../preface.md#skill-navigation-row-233) or [preface row 214]"
        "(../preface.md#skill-navigation-row-214) dynamics meta prelude capstone / export meta prelude gate → "
        "[VIII.2 Bridge](../part08-md/02-ensembles-integrators.md#bridge) through "
        "[VIII.3 opening hinge from VIII.2](../part08-md/03-ab-initio-and-coarse-graining.md#opening-hinge-viii2-to-viii3) "
        "aloud → [preface row 54](../preface.md#skill-navigation-row-54) five-step audit → confirm NPT Lab act "
        "steps 1–7 before pedigree checklist on the full capstone path.\n"
    )
    return t234_to_254(template) + "\n"


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 234 skill checkpoint")
    end = preface.index("\n\n### Row 235 skill checkpoint", start)
    row254_preface = t234_to_254(preface[start:end]).strip() + "\n\n"

    b234 = _load_add234()._build_blocks()
    epilogue_loop = t234_to_254(b234["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-234-closing-loop}", "{#row-254-closing-loop}", 1)
    for old_header in (
        "### Row 214 closing loop (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion)",
        "### Row 234 closing loop (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion)",
        "### Row 234 closing loop (Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion)",
    ):
        if old_header in epilogue_loop:
            epilogue_loop = epilogue_loop.replace(
                old_header,
                "### Row 254 closing loop (Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion)",
                1,
            )
            break
    for spill in ("\n\n\n\n### Row 253 closing loop", "\n\n\n\n### Row 254 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src234_header = (
        "## Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion index (row 234)"
    )
    next214_header = (
        "## Row 68 → Row 194 Row 68 → Row 54 export meta prelude capstone reunion index (row 214)"
    )
    i = sources.index(src234_header)
    j = sources.index(next214_header, i + len(src234_header))
    sources_index = t234_to_254(sources[i:j])
    sources_index = sources_index.replace(
        "(row 234) {#row68-row214-export-meta-prelude-capstone-reunion-index-row-234}",
        "(row 254) {#row68-row234-export-meta-prelude-capstone-reunion-index-row-254}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row214-export-meta-prelude-capstone-reunion-index-row-234",
        "row68-row234-export-meta-prelude-capstone-reunion-index-row-254",
    )
    sources_index = re.sub(
        r"\s*\{#row68-row234-export-meta-prelude-capstone-reunion-index-row-254\}\s*"
        r"\{#row68-row234-export-meta-prelude-capstone-reunion-index-row-254\}",
        " {#row68-row234-export-meta-prelude-capstone-reunion-index-row-254}",
        sources_index,
        count=1,
    )

    return {
        "row254_preface": row254_preface,
        "prologue_compass": t234_to_254(b234["prologue_compass"]).replace("(row 234)", "(row 254)", 1),
        "prologue_stitch": t234_to_254(b234["prologue_stitch"].strip()) + "\n\n",
        "prologue_preview": t234_to_254(b234["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t234_to_254(b234["sources_table"]).replace("| 234 | Row 68 → Row 214", "| 254 | Row 68 → Row 234", 1),
        "sources_index": sources_index,
        "memory_table": (
            "| 254 | Meta | [Row 68 → Row 234 export meta prelude capstone reunion index]"
            "(sources.md#row68-row234-export-meta-prelude-capstone-reunion-index-row-254) · "
            "[preface row 254 skill checkpoint](../preface.md#skill-navigation-row-254) · "
            "[prologue row 254 preview](../prologue/00-many-scales.md#prologue-preview-row-254) · "
            "[prologue row 254 closing stitch](../prologue/00-many-scales.md#row-254-closing-stitch) · "
            "[epilogue row 254 closing loop](../epilogue/multiscale.md#row-254-closing-loop) | "
            "Row 68 closed but row 54 export meta reunion feels disconnected from verified "
            "dynamics meta prelude capstone on the full capstone path — read row 68 + row 253 or "
            "row 234 gate + VIII.2 Bridge → VIII.3 + row 54; "
            "[row 254 baby picture](#row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": _compact_memory_baby(),
    }


ROW254_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

ROW254_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

PROLOGUE_STITCH_ANCHORS = (
    "**Row 253 closing stitch (Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-253-closing-stitch}",
    "**Row 233 closing stitch (Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-253-closing-stitch}",
    "**Row 214 closing stitch (Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-234-closing-stitch}",
)

ROW253_STITCH_OLD = "before row 254 export meta prelude capstone reunion opens on the full capstone path."
ROW253_STITCH_NEW = "before row 255 electronic audit meta prelude capstone reunion opens on the full capstone path."

ROW253_EPILOGUE_OLD = (
    "Proceed to [row 234](#row-234-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 233 on the full capstone path,"
)
ROW253_EPILOGUE_NEW = (
    "Proceed to [row 254](#row-254-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 253 on the full capstone path,"
)

BROKEN_SOURCES_HEADER = (
    "## Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion index (row 254) "
    "{#row68-row234-export-meta-prelude-capstone-reunion-index-row-274}"
)


def _epilogue_has_row254_in_capstone_chain(text: str) -> bool:
    if ROW254_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW254_EPILOGUE_AFTER)
    window = text[idx : idx + 25000]
    return (
        "{#row-254-closing-loop}" in window
        and "memory sheet row 254" in window
        and "### Row 254 closing loop" in window
    )


def _replace_epilogue_mid254(mid: str, loop254: str) -> str:
    if "{#row-253-closing-loop}" not in mid:
        raise SystemExit("row 253 closing loop must exist before row 254")
    idx = mid.index("{#row-253-closing-loop}")
    end = mid.find("\n\n", idx)
    if end == -1:
        end = len(mid)
    else:
        end += 2
    kept = mid[:end]
    return kept + loop254


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    before_copper = preface.split(copper, 1)[0]
    if "### Row 254 skill checkpoint" in before_copper:
        print("preface: row 254 capstone already present")
    else:
        if "### Row 253 skill checkpoint" not in before_copper:
            raise SystemExit("row 253 must exist before row 254")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row254_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 254")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "export meta prelude capstone reunion (row 254) |" not in prologue:
        needle = (
            "| Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 253) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 253 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 254 closing stitch" not in prologue:
            for anchor in PROLOGUE_STITCH_ANCHORS:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-253"></span>Row 233 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        if '<span id="prologue-preview-row-254">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW253_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW253_STITCH_OLD, ROW253_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 254")
    else:
        print("prologue: row 254 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW253_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW253_EPILOGUE_OLD, ROW253_EPILOGUE_NEW, 1)
        print("epilogue: updated row 253 proceed link")
    if not _epilogue_has_row254_in_capstone_chain(epilogue):
        if ROW254_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if ROW254_EPILOGUE_BEFORE not in epilogue.split(ROW254_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(ROW254_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW254_EPILOGUE_BEFORE, 1)
        mid = _replace_epilogue_mid254(mid, b["epilogue_loop"])
        epilogue_path.write_text(head + ROW254_EPILOGUE_AFTER + mid + ROW254_EPILOGUE_BEFORE + rest)
        print("epilogue: added row 254")
    else:
        print("epilogue: row 254 closing loop already present after row 253")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if BROKEN_SOURCES_HEADER in sources:
        start = sources.index(BROKEN_SOURCES_HEADER)
        end = sources.index(src234_header := (
            "## Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion index (row 234)"
        ), start)
        sources = sources[:start] + sources[end:]
        print("sources: removed broken row 254 stub")
    if "row68-row234-export-meta-prelude-capstone-reunion-index-row-254" not in sources:
        needle = "| 214 | Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone"
        if needle not in sources:
            needle = "| 234 | Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone"
        if needle not in sources:
            raise SystemExit("sources export table anchor not found")
        sources = sources.replace(needle, b["sources_table"] + needle, 1)
        src234_header = (
            "## Row 68 → Row 214 Row 68 → Row 54 export meta prelude capstone reunion index (row 234)"
        )
        if src234_header in sources and b["sources_index"].strip()[:80] not in sources:
            sources = sources.replace(src234_header, b["sources_index"] + src234_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 254")
    else:
        print("sources: row 254 index already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-254-baby-picture-row68-row234" not in memory:
        if "| 254 | Meta |" not in memory:
            mem253 = "| 253 | Meta | [Row 68 → Row 233 dynamics meta prelude capstone reunion index]"
            if mem253 in memory:
                memory = memory.replace(mem253, b["memory_table"] + mem253, 1)
        baby_anchors = (
            "### Row 253 baby picture {#row-253-baby-picture-row68-row233-dynamics-meta-prelude-capstone-reunion}",
            "### Row 234 baby picture {#row-234-baby-picture-row68-row214-export-meta-prelude-capstone-reunion}",
        )
        baby_anchor = next((a for a in baby_anchors if a in memory), None)
        if not baby_anchor:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 254")
    else:
        print("memory-sheet: row 254 baby already present")


if __name__ == "__main__":
    main()
