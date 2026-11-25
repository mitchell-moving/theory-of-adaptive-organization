#!/usr/bin/env python3
"""Tests for tools/refresh_pointer.py (a throwaway git repo with merge commits)."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_fresh as fresh  # noqa: E402


def _git(repo, *a):
    e = dict(os.environ, GIT_AUTHOR_NAME="T", GIT_AUTHOR_EMAIL="t@e", GIT_COMMITTER_NAME="T", GIT_COMMITTER_EMAIL="t@e")
    r = subprocess.run(["git", *a], cwd=repo, capture_output=True, text=True, env=e)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def test_pointer_refresh_after_four_merges(tmp_path):
    repo = str(tmp_path / "r")
    os.makedirs(os.path.join(repo, "tools"))
    shutil.copy(os.path.join(ROOT, "tools", "refresh_pointer.py"), os.path.join(repo, "tools"))
    shutil.copy(os.path.join(ROOT, "tools", "check_fresh.py"), os.path.join(repo, "tools"))
    _git(repo, "init", "-b", "main")
    open(os.path.join(repo, "x"), "w").write("0")
    _git(repo, "add", "."); _git(repo, "commit", "-m", "base")
    old = _git(repo, "rev-parse", "--short", "HEAD")
    open(os.path.join(repo, "STATUS.md"), "w").write(
        "**As of:** x. `main` is `%s` (PR #1, thing), following PRs #0 (`aaaaaaa`), and more.\n" % old)
    open(os.path.join(repo, "OPEN_WORK.md"), "w").write("# OW\n\n**As of:** x, on `main` `%s` (PR #1). rest\n" % old)
    _git(repo, "add", "."); _git(repo, "commit", "-m", "pointer")
    # four merged PRs: feature branch + --no-ff merge each
    for n in (2, 3, 4, 5):
        _git(repo, "checkout", "-q", "-b", "f%d" % n)
        open(os.path.join(repo, "f%d" % n), "w").write("x")
        _git(repo, "add", "."); _git(repo, "commit", "-m", "work %d" % n)
        _git(repo, "checkout", "-q", "main")
        _git(repo, "merge", "--no-ff", "-m", "Merge pull request #%d from a/b" % n, "f%d" % n)
    _git(repo, "update-ref", "refs/remotes/origin/main", "main")
    assert fresh.check(repo)  # stale: the pointer is far behind
    out = subprocess.run([sys.executable, "tools/refresh_pointer.py"], cwd=repo, capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    _git(repo, "commit", "-qam", "refresh")
    _git(repo, "update-ref", "refs/remotes/origin/main", "main")
    s = open(os.path.join(repo, "STATUS.md")).read()
    assert "(PR #5), following PRs #5 (" in s and "#2 (" in s and "#0 (`aaaaaaa`)" in s
    # the pointer now names the merge before the refresh commit; the refresh commit is first-parent HEAD
    assert fresh.check(repo) == []


def test_duplicate_tip_entries_are_collapsed():
    import refresh_pointer as rp
    line = "following PRs #275 (`4ff299e`), #275 (`4ff299e`), #271 (`62da4fb`), #270 (`12cb996`), and more"
    assert rp.DUP_RE.sub(r"\1", line) == "following PRs #275 (`4ff299e`), #271 (`62da4fb`), #270 (`12cb996`), and more"
    assert rp.DUP_RE.sub(r"\1", "#1 (`aaaaaaa`), #2 (`bbbbbbb`), ") == "#1 (`aaaaaaa`), #2 (`bbbbbbb`), "
