#!/usr/bin/env python3
"""Rewrite the main pointer in STATUS.md and OPEN_WORK.md to the current tip of main.

Run after a batch of merges (process/PROCESS.md §4), on a branch cut from
origin/main, then open a one-file-pair PR:

  git fetch origin main && git checkout -b status/pointer-refresh origin/main
  python3 tools/refresh_pointer.py
  python3 tools/check_pending.py --offline

It edits only the pointer. STATUS.md: "`main` is `OLD` (PR #N...)" becomes the
tip, and the merges since OLD (first-parent, newest first) are put at the front
of "following PRs". OPEN_WORK.md: "on `main` `OLD` (PR #N)" becomes the tip.
It never touches any other text. Open-PR lists and results stay hand-edited.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATUS_RE = re.compile(r"`main` is `([0-9a-f]{7,40})` \(PR #(\d+)([^)]*)\), following PRs ")
OPEN_RE = re.compile(r"on `main` `([0-9a-f]{7,40})` \(PR #(\d+)\)")
DUP_RE = re.compile(r"(#(\d+) \(`([0-9a-f]+)`\), )(?:#\2 \(`\3`\), )+")
MERGE_RE = re.compile(r"^Merge pull request #(\d+)\b")


def git(*a):
    r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("git %s: %s" % (" ".join(a), r.stderr.strip()))
    return r.stdout


def merges_since(old, tip):
    """[(pr, short sha)] newest first, from the tip back to and including old."""
    out = []
    lines = git("log", "--first-parent", "--format=%h %s", "%s..%s" % (old, tip)).splitlines()
    lines += git("log", "-1", "--format=%h %s", old).splitlines()
    for line in lines:
        sha, _, subj = line.partition(" ")
        m = MERGE_RE.match(subj)
        if m:
            out.append((int(m.group(1)), sha))
    return out


def main():
    tip = git("rev-parse", "--short", "refs/remotes/origin/main").strip()
    spath, opath = os.path.join(ROOT, "STATUS.md"), os.path.join(ROOT, "OPEN_WORK.md")
    s = open(spath, encoding="utf-8").read()
    m = STATUS_RE.search(s)
    if not m:
        raise SystemExit("STATUS.md: pointer sentence not found")
    old = m.group(1)
    if git("rev-parse", "--short", old).strip() == tip:
        print("already at", tip)
        return 0
    ms = merges_since(old, tip)
    if not ms:
        raise SystemExit("no merged PRs found between %s and %s" % (old, tip))
    new_pr = ms[0][0]
    listing = ", ".join("#%d (`%s`)" % (n, sha) for n, sha in ms) + ", "
    s = s[:m.start()] + "`main` is `%s` (PR #%d), following PRs %s" % (tip, new_pr, listing) + s[m.end():]
    s = DUP_RE.sub(r"\1", s)  # the old tip is listed by the sentence it replaces and again by merges_since
    open(spath, "w", encoding="utf-8").write(s)
    o = open(opath, encoding="utf-8").read()
    om = OPEN_RE.search(o)
    if om:
        o = o[:om.start()] + "on `main` `%s` (PR #%d)" % (tip, new_pr) + o[om.end():]
        open(opath, "w", encoding="utf-8").write(o)
    print("STATUS.md and OPEN_WORK.md now point at", tip, "(PR #%d)" % new_pr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
