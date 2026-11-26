#!/usr/bin/env python3
"""Live current-state brief for the GTAO repository.

Computed from git and the canonical files, so it cannot go stale the way a
hand-kept pointer can (no page keeps one since 25 November 2026). Stdlib plus git; gh is used for open
PRs when available and is skipped when it is not.

Run from the repo root:  python3 tools/brief.py
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(root, *args, check=True):
    r = subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if check and r.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), r.stderr.strip()))
    return r


def resolve_main(root):
    """Return (ref, full SHA) for main.

    origin/main wins when it exists: a local main left behind after a
    fetch is stale.
    """
    for ref in ("refs/remotes/origin/main", "refs/heads/main", "HEAD"):
        r = git(root, "rev-parse", "--verify", ref, check=False)
        if r.returncode == 0:
            return ref, r.stdout.strip()
    raise RuntimeError("could not resolve main or HEAD")


def expand_sha(root, short):
    r = git(root, "rev-parse", "--verify", short + "^{commit}", check=False)
    if r.returncode == 0:
        return r.stdout.strip()
    return None


def format_et(dt):
    local = dt.astimezone(ET)
    hour = local.strftime("%I").lstrip("0") or "0"
    return "%s %d %s %s, %s:%s %s ET" % (
        local.strftime("%a"),
        local.day,
        local.strftime("%b"),
        local.year,
        hour,
        local.strftime("%M"),
        local.strftime("%p"),
    )


def parse_git_date(text):
    text = text.strip()
    # git %cI may end with Z or an offset; fromisoformat handles both in 3.11+.
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    return datetime.fromisoformat(text)


def commit_date(root, sha):
    r = git(root, "log", "-1", "--format=%cI", sha)
    return parse_git_date(r.stdout)


def last_merges(root, ref, n):
    """First-parent merge commits of ref, newest first, each a dict."""
    r = git(
        root,
        "log",
        "--merges",
        "--first-parent",
        "-n",
        str(n),
        "--format=%H%x00%cI%x00%s%x00%b%x1e",
        ref,
    )
    out = []
    for rec in r.stdout.split("\x1e"):
        rec = rec.strip()
        if not rec:
            continue
        parts = rec.split("\x00", 3)
        if len(parts) < 3:
            continue
        sha, iso, subject = parts[0], parts[1], parts[2]
        body = parts[3] if len(parts) > 3 else ""
        title = next((ln.strip() for ln in body.splitlines() if ln.strip()), subject)
        m = re.search(r"Merge pull request #(\d+)\b", subject)
        out.append({
            "sha": sha,
            "date": parse_git_date(iso),
            "subject": subject,
            "title": title,
            "number": int(m.group(1)) if m else None,
        })
    return out


PR_SUBJECT_RES = (
    re.compile(r"^Merge pull request #(\d+)\b"),
    re.compile(r"^Merge PR #(\d+)\b"),
    re.compile(r"\(#(\d+)\)\s*$"),
)


def pr_number(subject):
    """PR number from a merge or squash-merge subject, or None."""
    for rx in PR_SUBJECT_RES:
        m = rx.search(subject)
        if m:
            return int(m.group(1))
    return None


def last_merged_prs(root, ref, n=10):
    """Last n first-parent commits that land a GitHub PR, newest first.

    Covers GitHub merge commits ("Merge pull request #N"), hand-written
    merges ("Merge PR #N: ..."), and squash merges ("... (#N)").
    """
    r = git(
        root,
        "log",
        "--first-parent",
        "-n",
        str(max(n * 5, n)),
        "--format=%H%x00%cI%x00%s%x00%b%x1e",
        ref,
    )
    found = []
    for rec in r.stdout.split("\x1e"):
        rec = rec.strip()
        if not rec:
            continue
        parts = rec.split("\x00", 3)
        if len(parts) < 3:
            continue
        sha, iso, subject = parts[0], parts[1], parts[2]
        body = parts[3] if len(parts) > 3 else ""
        num = pr_number(subject)
        if num is None:
            continue
        if subject.startswith("Merge pull request #"):
            title = next((ln.strip() for ln in body.splitlines() if ln.strip()), subject)
        else:
            title = subject
        found.append({
            "sha": sha,
            "date": parse_git_date(iso),
            "subject": subject,
            "title": title,
            "number": num,
        })
        if len(found) >= n:
            break
    return found


def open_prs(root):
    """Return a list of open PR dicts, or None if gh is unavailable."""
    if shutil.which("gh") is None:
        return None
    r = subprocess.run(
        [
            "gh", "pr", "list", "--state", "open",
            "--json", "number,title,isDraft,headRefName,updatedAt",
            "--limit", "30",
        ],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None
    import json
    try:
        rows = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    out = []
    for p in rows:
        updated = p.get("updatedAt") or ""
        try:
            dt = parse_git_date(updated) if updated else None
        except ValueError:
            dt = None
        out.append({
            "number": p.get("number"),
            "title": p.get("title") or "",
            "draft": bool(p.get("isDraft")),
            "head": p.get("headRefName") or "",
            "updated": dt,
        })
    return out


def theory_version(text):
    m = re.search(r"^# .*? v(\d+\.\d+(?:\.\d+)?[a-z]?) draft", text, re.M)
    return m.group(1) if m else None


def claim_map_version(text):
    notes = [tuple(int(x) for x in v.split(".")) for v in re.findall(r"^\*\*v(2\.\d+) note", text, re.M)]
    return "%d.%d" % max(notes) if notes else None


def split_cells(ln):
    t = ln.strip()
    parts = re.split(r"(?<!\\)\|", t)
    if t.startswith("|"):
        parts = parts[1:]
    if t.endswith("|") and not t.endswith("\\|"):
        parts = parts[:-1]
    return [p.strip() for p in parts]


def claim_map_tally(text):
    """Return (total, [(status, count), ...]) from the current tally block."""
    m = re.search(r"<!-- tally:begin -->(.*?)<!-- tally:end -->", text, re.S)
    if not m:
        return None, []
    rows, total = [], None
    for ln in m.group(1).split("\n"):
        if not ln.startswith("|"):
            continue
        c = [x.replace("*", "").strip() for x in split_cells(ln)]
        if len(c) != 2 or not c[1].isdigit():
            continue
        if c[0] == "Total":
            total = int(c[1])
        elif c[0] not in ("Status now (all sections) Rows", "Status now (all sections)"):
            rows.append((c[0], int(c[1])))
    return total, rows


def is_done_gate(gate):
    s = re.sub(r"[*_`]", "", gate or "").strip()
    return bool(re.match(r"^DONE(?!-)(\b|$)", s))


def open_work_undone(text):
    """Rows whose Gate (or State, if there is no Gate column) is not DONE."""
    lines = text.splitlines()
    i, rows = 0, []
    while i < len(lines):
        cells = split_cells(lines[i]) if lines[i].startswith("|") else []
        if cells and cells[0] == "ID" and ("Item" in cells or "gap" in cells):
            headers = cells
            i += 1
            if i < len(lines) and re.match(r"^\|[\s:|-]+$", lines[i]):
                i += 1
            if "Gate" in headers:
                gate_idx = headers.index("Gate")
            elif "State" in headers:
                gate_idx = headers.index("State")
            elif "rank" in headers:
                gate_idx = headers.index("rank")
            else:
                gate_idx = 2
            while i < len(lines) and lines[i].startswith("|"):
                row = split_cells(lines[i])
                i += 1
                if not row or not row[0] or set(row[0]) <= set("- "):
                    continue
                ident = row[0]
                gate = row[gate_idx] if len(row) > gate_idx else ""
                if not is_done_gate(gate):
                    rows.append((ident, gate))
            continue
        i += 1
    return rows


def hypothesis(text):
    m = re.search(
        r"^\*\*(The law of adaptive organization \(hypothesis\):.*?)\*\*\s*$",
        text,
        re.M,
    )
    if m:
        return m.group(1)
    m = re.search(r"The law of adaptive organization \(hypothesis\):[^\n*]+", text)
    return m.group(0).strip() if m else None


def stale_reviewed_prs(root):
    """WARN lines for open PRs reviewed with no blockers but unmerged > 24h (check_pending's rule).

    Warning only: a stale PR elsewhere never fails another PR's merge (25 November 2026)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import check_pending as cp
        parked, _problems = cp.read_parked(root)
        pending, _open = cp.collect(cp.gh_api, parked=parked, is_merged=lambda sha: cp.in_main(root, sha))
    except Exception as e:  # offline, no gh: say so, never fail
        return ["Stale reviewed PRs: not checked (%s)" % (str(e).split("\n")[0][:80] or type(e).__name__)]
    if not pending:
        return ["Stale reviewed PRs: none"]
    return ["WARN stale reviewed PR (merge, park in process/PROCESS.md §4, or close): %s" % x for x in pending]


def render(root=None):
    root = root or repo_root()
    ref, main_sha = resolve_main(root)
    # Prefer to label the SHA we actually resolved.
    try:
        main_date = commit_date(root, main_sha)
        date_s = format_et(main_date)
    except Exception:
        date_s = "(date unavailable)"

    lines = []
    lines.append("GTAO live brief (computed from git; times in America/New_York)")
    lines.append("=" * 72)
    lines.append("main HEAD: %s" % main_sha)
    lines.append("date: %s" % date_s)
    if ref not in ("refs/heads/main", "HEAD"):
        lines.append("resolved from: %s" % ref)

    lines.append("")
    lines.append("Last 10 merged PRs")
    prs = last_merged_prs(root, main_sha, 10)
    if not prs:
        lines.append("  (none found)")
    for p in prs:
        num = "#%d" % p["number"] if p["number"] else "    "
        lines.append(
            "  %s  %s  %s  %s"
            % (num, p["sha"][:7], format_et(p["date"]), p["title"])
        )

    lines.append("")
    op = open_prs(root)
    if op is None:
        lines.append("Open PRs")
        lines.append("  (gh unavailable; skipped)")
    elif not op:
        lines.append("Open PRs")
        lines.append("  (none)")
    else:
        lines.append("Open PRs (%d)" % len(op))
        for p in op:
            flag = "DRAFT " if p["draft"] else ""
            when = format_et(p["updated"]) if p["updated"] else ""
            lines.append(
                "  #%s  %s%s  %s"
                % (p["number"], flag, p["title"], when)
            )

    theory = _read(root, "THEORY.md")
    cmap = _read(root, "measurement/CLAIM_MAP_v2.md")
    tv, cv = theory_version(theory or ""), claim_map_version(cmap or "")
    total, tally_rows = claim_map_tally(cmap or "")
    lines.append("")
    lines.append("Versions")
    lines.append("  THEORY.md v%s" % (tv or "(unparsed)"))
    lines.append("  CLAIM_MAP v%s" % (cv or "(unparsed)"))
    if total is not None:
        compact = ", ".join("%s %d" % (n, c) for n, c in tally_rows)
        lines.append("  tally: total %d (%s)" % (total, compact))
    else:
        lines.append("  tally: (unparsed)")

    hypo = hypothesis(_read(root, "CORE.md") or "")
    lines.append("")
    lines.append("Hypothesis")
    lines.append("  %s" % (hypo or "(unparsed)"))

    ow = _read(root, "README.md") or ""
    undone = open_work_undone(ow)
    lines.append("")
    lines.append("Open work (gate not DONE): %d" % len(undone))
    for ident, gate in undone:
        gate_one = re.sub(r"\s+", " ", gate).strip()
        if len(gate_one) > 100:
            gate_one = gate_one[:97] + "..."
        lines.append("  %s  %s" % (ident, gate_one))

    lines.append("")
    lines.extend(stale_reviewed_prs(root))
    return "\n".join(lines) + "\n"


def _read(root, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return None
    return open(path, encoding="utf-8").read()


def main(argv=None):
    argv = sys.argv if argv is None else argv
    root = argv[1] if len(argv) > 1 else repo_root()
    try:
        sys.stdout.write(render(root))
        return 0
    except Exception as e:
        sys.stderr.write("brief failed: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
