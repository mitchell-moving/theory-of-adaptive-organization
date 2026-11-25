#!/usr/bin/env python3
"""Headline-claim check for the GTAO repository (stdlib only).

The canonical statuses live in the headline ledger of
measurement/CLAIM_MAP_v2.md (between the ledger markers). Front pages carry
a derived view of that ledger. This script fails when the view is stale,
when a cited source or review path is missing, when an edge is invalid,
when a front page states a headline status the ledger does not, when the
hypothesis sentence changes, or when a page claims Lean coverage the ledger
does not give.

Run from the repo root:  python3 tools/check_claims.py
Exit 0 = no FAIL. A local pass is not a server-side publication gate.
"""
from __future__ import annotations

import os
import re
import sys

HYPOTHESIS = (
    "The law of adaptive organization (hypothesis): "
    "strongly selected systems minimize the cost of judgment."
)
HYP_FILES = [
    "README.md",
    "CORE.md",
    "THEORY.md",
    "STATUS.md",
    "ONE_PAGER.md",
    "theory/COADAPTATION.md",
    "theory/GROWTH_BRIDGE.md",
    "theory/FEEDBACK_FLOOR_2026-11-23.md",
    "theory/SWARM_RULE_2026-11-23.md",
    "theory/AREA_LAW_PROBE_2026-11-23.md",
]
FRONT = ["README.md", "CORE.md", "STATUS.md", "ONE_PAGER.md", "THEORY.md"]
STATUSES = {
    "proved-in-model",
    "known",
    "open",
    "conjecture",
    "hypothesis",
    "false",
    "synthesis",
    "interpretation",
}
EDGE_KINDS = {"proved", "known", "interpretation", "open", "conjecture"}
LEDGER_BEGIN = "<!-- headline-ledger:begin -->"
LEDGER_END = "<!-- headline-ledger:end -->"
RULES_BEGIN = "<!-- claim-rules:begin -->"
RULES_END = "<!-- claim-rules:end -->"
VIEW_BEGIN = "<!-- claims-view:begin -->"
VIEW_END = "<!-- claims-view:end -->"
LEAN_OVERCLAIM = re.compile(
    r"whole physical theorem is formalized|all of the physics is formalized|"
    r"every heat floor is formalized|the physical argument as a whole is formalized",
    re.I,
)
UNMANAGED = re.compile(
    r"\b(T\d{2,}|CX\d+|CT\d{2}|CA\d+|F\d+|CL\d{2}|BICAUSAL|IP5)\b"
    r"[^.\n]{0,100}\b(PROVED|OPEN|CONJECTURE)\b"
)
ROW_ID = re.compile(r"^\| ([A-Za-z][A-Za-z0-9-]*) \|")
CLAIM_ROW = re.compile(r"^\| ((?:[A-Z]{1,2}\d+[′']?[a-z]?)) \|")
GAP_ID = re.compile(r"^\| ([A-Z][A-Z0-9-]*) \|")


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(root, path):
    with open(os.path.join(root, path), encoding="utf-8") as fh:
        return fh.read()


def split_cells(line):
    parts = re.split(r"(?<!\\)\|", line.strip())
    if line.strip().startswith("|"):
        parts = parts[1:]
    if line.strip().endswith("|") and not line.strip().endswith("\\|"):
        parts = parts[:-1]
    return [p.strip() for p in parts]


def parse_ledger(text):
    """Return (rows, rules, errors) from a CLAIM_MAP document."""
    errors = []
    if LEDGER_BEGIN not in text or LEDGER_END not in text:
        return [], [], ["claims: headline ledger markers missing"]
    block = text.split(LEDGER_BEGIN, 1)[1].split(LEDGER_END, 1)[0]
    rows = []
    header = None
    for line in block.splitlines():
        if not line.startswith("|"):
            continue
        cells = split_cells(line)
        if header is None:
            header = cells
            continue
        if set(cells) <= {"---", ":---", "---:"} or all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        if len(cells) != len(header):
            errors.append("claims: ledger row has %d cells, header %d (%s)" % (len(cells), len(header), cells[0] if cells else "?"))
            continue
        row = dict(zip(header, cells))
        rows.append(row)
    if not rows:
        errors.append("claims: headline ledger has no rows")
    seen = set()
    for row in rows:
        ident = row.get("id", "")
        if not ident or ident in seen:
            errors.append("claims: duplicate or blank ledger id %r" % ident)
        seen.add(ident)
        if row.get("status") not in STATUSES:
            errors.append("claims: %s has status %r" % (ident, row.get("status")))
        if not row.get("source") or not row.get("anchor") or not row.get("plain"):
            errors.append("claims: %s missing plain, source, or anchor" % ident)
    rules = []
    if RULES_BEGIN not in text or RULES_END not in text:
        errors.append("claims: claim-rules markers missing")
    else:
        rblock = text.split(RULES_BEGIN, 1)[1].split(RULES_END, 1)[0]
        for line in rblock.splitlines():
            line = line.strip()
            if not line or line.startswith("<!--"):
                continue
            parts = line.split(" ", 2)
            if len(parts) < 3 or parts[0] not in {"must", "forbid", "must-near", "forbid-near"}:
                errors.append("claims: bad rule %r" % line[:80])
                continue
            if parts[0].endswith("-near"):
                bits = parts[2].split(" ", 1)
                if len(bits) != 2:
                    errors.append("claims: bad near-rule %r" % line[:80])
                    continue
                rules.append((parts[0], parts[1], bits[0], bits[1]))
            else:
                rules.append((parts[0], parts[1], None, parts[2]))
    return rows, rules, errors


def render_view(rows):
    lines = [
        VIEW_BEGIN,
        "Derived from the headline ledger in measurement/CLAIM_MAP_v2.md. Refresh this block from that ledger. A disagreement is a miss of a public claim.",
    ]
    for row in rows:
        lines.append("%s | %s | %s" % (row["id"], row["status"], row["review"]))
    lines.append(VIEW_END)
    return "\n".join(lines)


def strip_view(text):
    return re.sub(
        re.escape(VIEW_BEGIN) + r".*?" + re.escape(VIEW_END),
        "",
        text,
        flags=re.S,
    )


def claim_ids(text):
    ids = set()
    # Count only the lettered claim sections, not the headline ledger.
    if LEDGER_BEGIN in text:
        text = text.split(LEDGER_BEGIN, 1)[0]
    for line in text.splitlines():
        m = CLAIM_ROW.match(line)
        if m:
            ids.add(m.group(1))
    return ids


def paragraphs_with(text, ident):
    """Lines that name ident. These pages put one claim on one long line."""
    body = strip_view(text)
    rx = re.compile(r"(?<![A-Za-z0-9-])" + re.escape(ident) + r"(?![A-Za-z0-9-])")
    return [ln for ln in body.splitlines() if rx.search(ln)]


def check_sources(rows, root):
    errors = []
    lean_tree = os.path.isdir(os.path.join(root, "formal", "lean", "GTAO"))
    for row in rows:
        ident = row["id"]
        src = row["source"]
        m = re.match(r"^([^:]+):(\d+)(?:-(\d+))?$", src)
        if not m:
            errors.append("claims: %s source %r is not path:line" % (ident, src))
            continue
        path, start, end = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            errors.append("claims: source missing %s (%s)" % (path, ident))
            continue
        lines = read(root, path).splitlines()
        if start < 1 or end > len(lines) or end < start:
            errors.append("claims: %s source range %s outside %s (%d lines)" % (ident, src, path, len(lines)))
            continue
        chunk = "\n".join(lines[start - 1:end])
        if row["anchor"] not in chunk:
            errors.append("claims: %s anchor not in %s" % (ident, src))
        lean = row.get("lean", "")
        if re.search(r"\b(1185|whole|entire physics|all heat floors)\b", lean, re.I):
            errors.append("claims: %s lean cell treats an aggregate or a whole-physics claim as coverage" % ident)
        for lp in re.findall(r"formal/lean/\S+?\.lean", lean):
            if lean_tree and not os.path.isfile(os.path.join(root, lp)):
                errors.append("claims: %s lean path missing %s" % (ident, lp))
        for rp in re.findall(r"`([^`]+)`", row.get("review", "")):
            if "/" not in rp:
                continue
            if not os.path.isfile(os.path.join(root, rp)):
                errors.append("claims: review path missing %s (%s)" % (rp, ident))
    return errors


def check_edges(rows, known):
    errors = []
    ids = {r["id"] for r in rows}
    for row in rows:
        raw = row.get("connects", "").strip()
        if raw in {"", "-"}:
            errors.append("claims: %s has no connects edge" % row["id"])
            continue
        for edge in raw.split(";"):
            edge = edge.strip()
            if ":" not in edge:
                errors.append("claims: edge %r on %s" % (edge, row["id"]))
                continue
            target, kind = edge.split(":", 1)
            if kind not in EDGE_KINDS:
                errors.append("claims: edge %s has kind %r" % (row["id"], kind))
            if target not in ids and target not in known:
                errors.append("claims: edge %s -> %s is not a ledger or claim-map id" % (row["id"], target))
    return errors


def check_views(rows, root):
    errors = []
    want = render_view(rows)
    for path in FRONT:
        if not os.path.isfile(os.path.join(root, path)):
            errors.append("claims: front page missing %s" % path)
            continue
        text = read(root, path)
        n = text.count(VIEW_BEGIN)
        if n != 1 or text.count(VIEW_END) != 1:
            errors.append("claims: view stale %s (markers %d)" % (path, n))
            continue
        got = text.split(VIEW_BEGIN, 1)[1]
        got = VIEW_BEGIN + got.split(VIEW_END, 1)[0] + VIEW_END
        if got != want:
            errors.append("claims: view stale %s" % path)
    return errors


def check_rules(rules, rows, root):
    errors = []
    ids = {r["id"] for r in rows}
    by_id = {r["id"]: r for r in rows}
    for kind, path, ident, phrase in rules:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            errors.append("claims: rule file missing %s" % path)
            continue
        text = strip_view(read(root, path))
        if ident:
            if ident not in ids:
                errors.append("claims: rule names unknown id %s" % ident)
                continue
            windows = paragraphs_with(read(root, path), ident)
            hit = any(phrase in w for w in windows)
            if kind == "must-near" and not hit:
                errors.append("claims: mismatch %s prose lacks %r near %s" % (path, phrase, ident))
            if kind == "forbid-near" and hit:
                errors.append("claims: mismatch %s prose has %r near %s" % (path, phrase, ident))
            # Status word in the same paragraph must not fight the ledger.
            status = by_id[ident]["status"]
            for w in windows:
                if status == "open" and re.search(r"\bPROVED\b", w) and not re.search(r"\bnot\b[^.]{0,40}\bPROVED\b|no\b[^.]{0,40}\bPROVED\b", w):
                    errors.append("claims: mismatch %s says PROVED near open %s" % (path, ident))
                if status == "proved-in-model" and re.search(r"not worked out|remains open", w) and not re.search(
                    r"beyond|outside those|applying|joined|general case|still open|not worked out\. OPEN", w
                ):
                    errors.append("claims: mismatch %s undersells proved %s" % (path, ident))
        else:
            hit = phrase in text
            if kind == "must" and not hit:
                errors.append("claims: mismatch %s lacks %r" % (path, phrase))
            if kind == "forbid" and hit:
                errors.append("claims: mismatch %s has %r" % (path, phrase))
    return errors


def check_hypothesis(root):
    errors = []
    for path in HYP_FILES:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            continue
        if HYPOTHESIS not in read(root, path):
            errors.append("claims: hypothesis sentence changed or missing in %s" % path)
    for path in FRONT:
        full = os.path.join(root, path)
        if os.path.isfile(full) and HYPOTHESIS not in read(root, path):
            errors.append("claims: hypothesis sentence changed or missing in %s" % path)
    return errors


def check_unmanaged(rows, root, known):
    errors = []
    ids = {r["id"] for r in rows} | set(known)
    for path in FRONT:
        full = os.path.join(root, path)
        if not os.path.isfile(full):
            continue
        body = strip_view(read(root, path))
        if path == "THEORY.md" and "## Appendix C" in body:
            body = body.split("## Appendix C", 1)[0]
        if LEAN_OVERCLAIM.search(body):
            errors.append("claims: lean overclaim in %s" % path)
        for m in UNMANAGED.finditer(body):
            ident = m.group(1)
            if ident not in ids:
                errors.append("claims: unmanaged headline %s in %s" % (ident, path))
    return errors


def check_gap(root):
    errors = []
    ow = os.path.join(root, "OPEN_WORK.md")
    gp = os.path.join(root, "theory/GAP_PLAN.md")
    if not os.path.isfile(ow) or not os.path.isfile(gp):
        return ["claims: GAP_PLAN or OPEN_WORK missing"]
    text = read(root, "OPEN_WORK.md")
    m = re.search(r"^## 9\. Ranked gaps.*", text, re.M | re.S)
    if not m:
        return ["claims: OPEN_WORK has no section 9 ranked gaps"]
    sec = m.group(0).split("\n## ", 1)[0]
    ids = []
    for line in sec.splitlines():
        mm = GAP_ID.match(line)
        if mm and mm.group(1) not in {"ID"}:
            ids.append(mm.group(1))
    if not ids:
        errors.append("claims: section 9 has no gap rows")
    gtext = read(root, "theory/GAP_PLAN.md")
    for ident in ids:
        if ident not in gtext:
            errors.append("claims: GAP_PLAN.md missing %s" % ident)
    if "not a second queue" not in gtext and "not a second list" not in gtext:
        errors.append("claims: GAP_PLAN.md does not say it is derived")
    return errors


def check(root=None):
    """Return a list of failure strings (empty means pass)."""
    root = root or repo_root()
    cm_path = os.path.join(root, "measurement/CLAIM_MAP_v2.md")
    if not os.path.isfile(cm_path):
        return ["claims: measurement/CLAIM_MAP_v2.md missing"]
    text = read(root, "measurement/CLAIM_MAP_v2.md")
    rows, rules, errors = parse_ledger(text)
    if not rows:
        return errors
    errors.extend(check_sources(rows, root))
    errors.extend(check_edges(rows, claim_ids(text)))
    errors.extend(check_views(rows, root))
    errors.extend(check_rules(rules, rows, root))
    errors.extend(check_hypothesis(root))
    errors.extend(check_unmanaged(rows, root, claim_ids(text)))
    errors.extend(check_gap(root))
    # de-duplicate, keep order
    out, seen = [], set()
    for e in errors:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


def main(argv=None):
    argv = sys.argv if argv is None else argv
    root = argv[1] if len(argv) > 1 else repo_root()
    fails = check(root)
    if fails:
        for f in fails:
            print("  FAIL " + f)
        print("RESULT: FAIL")
        return 1
    print("claims: ledger, views, sources, edges, hypothesis: OK")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
