#!/usr/bin/env python3
"""Tests for tools/check_fresh.py.

Run:  python3 -m pytest -q tools/test_check_fresh.py
"""
from __future__ import annotations

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_fresh as fresh


def _git(repo, *args):
    e = os.environ.copy()
    e.update({
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.com",
        "GIT_AUTHOR_DATE": "2026-11-21T12:00:00-05:00",
        "GIT_COMMITTER_DATE": "2026-11-21T12:00:00-05:00",
    })
    r = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, env=e)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _repo_with_commits(dest, n_first_parent):
    """Exactly n_first_parent first-parent commits on main (linear history)."""
    os.makedirs(dest)
    _git(dest, "init", "-b", "main")
    _git(dest, "config", "user.name", "Test")
    _git(dest, "config", "user.email", "test@example.com")
    shas = []
    for i in range(n_first_parent):
        path = os.path.join(dest, "f%d.txt" % i)
        open(path, "w", encoding="utf-8").write("c%d\n" % i)
        _git(dest, "add", "f%d.txt" % i)
        _git(dest, "commit", "-m", "c%d" % i)
        shas.append(_git(dest, "rev-parse", "HEAD"))
    return dest, shas


def _write_status(repo, sha):
    open(os.path.join(repo, "STATUS.md"), "w", encoding="utf-8").write(
        "# STATUS\n\n**As of:** today. `main` is `%s` (PR #1).\n" % sha
    )


def test_real_repo_status_is_in_window_after_fix():
    # After the STATUS.md fix this must pass on the working tree.
    fails = fresh.check(ROOT)
    assert fails == []


def test_head_pointer_passes(tmp_path):
    repo, shas = _repo_with_commits(tmp_path / "r", 6)
    _write_status(repo, shas[-1][:7])
    assert fresh.check(repo) == []


def test_pointer_within_last_three_first_parent_passes(tmp_path):
    repo, shas = _repo_with_commits(tmp_path / "r", 6)
    # shas[-3] is the 3rd first-parent commit counting HEAD as 1; still in window.
    _write_status(repo, shas[-3][:7])
    window = fresh.first_parent_window(repo, "HEAD", fresh.WINDOW)
    assert fresh.WINDOW == 3
    assert shas[-3] in window
    assert fresh.check(repo) == []


def test_pointer_sixth_first_parent_fails(tmp_path):
    repo, shas = _repo_with_commits(tmp_path / "r", 6)
    _write_status(repo, shas[-6][:7])
    window = fresh.first_parent_window(repo, "HEAD", 5)
    assert shas[-6] not in window
    fails = fresh.check(repo)
    assert fails and "freshness:" in fails[0]
    assert shas[-6][:7] in fails[0] or shas[-6][:7] in " ".join(fails)


def test_unknown_sha_fails(tmp_path):
    repo, shas = _repo_with_commits(tmp_path / "r", 3)
    _write_status(repo, "deadbee")
    fails = fresh.check(repo)
    assert fails and "not a commit" in fails[0]


def test_missing_pointer_fails(tmp_path):
    repo, shas = _repo_with_commits(tmp_path / "r", 2)
    open(os.path.join(repo, "STATUS.md"), "w", encoding="utf-8").write("# STATUS\nNo pointer.\n")
    fails = fresh.check(repo)
    assert fails and "no 'main is SHA' pointer" in fails[0]


def test_missing_git_is_skipped(tmp_path):
    dest = tmp_path / "nogit"
    dest.mkdir()
    _write_status(dest, "a65b64e")
    # check() returns no failures when git is absent, so consistency
    # mutation copies without .git still pass.
    assert fresh.is_git_repo(str(dest)) is False
    assert fresh.check(str(dest)) == []


def test_branch_six_commits_ahead_of_main_passes(tmp_path):
    # A correct main-SHA pointer must still pass when HEAD is six
    # commits ahead of main. Judging the window from HEAD would fail.
    repo, shas = _repo_with_commits(tmp_path / "r", 3)
    main_sha = shas[-1]
    _write_status(repo, main_sha[:7])
    _git(repo, "checkout", "-b", "feat")
    for i in range(6):
        path = os.path.join(repo, "b%d.txt" % i)
        open(path, "w", encoding="utf-8").write("b%d\n" % i)
        _git(repo, "add", "b%d.txt" % i)
        _git(repo, "commit", "-m", "b%d" % i)
    head = _git(repo, "rev-parse", "HEAD")
    assert head != main_sha
    assert fresh.check(repo) == []


def test_nested_copy_without_git_is_skipped(tmp_path):
    repo, shas = _repo_with_commits(tmp_path / "r", 3)
    _write_status(repo, shas[-1][:7])
    nested = os.path.join(repo, "copy")
    os.makedirs(nested)
    # A SHA that would fail if this copy were graded against the parent.
    _write_status(nested, "deadbee")
    assert not os.path.exists(os.path.join(nested, ".git"))
    assert fresh.is_git_repo(nested) is False
    assert fresh.check(nested) == []


def test_unquoted_main_is_feedback_is_not_a_sha():
    assert fresh.stated_main_sha("main is feedback") is None
    assert fresh.stated_main_sha("main is deadbeef") == "deadbeef"
    assert fresh.stated_main_sha("`main` is `2c32ade`") == "2c32ade"
    assert fresh.stated_main_sha("domain is deadbeef") is None
    assert fresh.stated_main_sha("remain is deadbeef") is None
    assert fresh.stated_main_sha("domain is deadbeef. `main` is `2c32ade`.") == "2c32ade"



def test_pointer_fourth_first_parent_fails(tmp_path):
    # Window is 3 since 24 November 2026 (process/FAILURES.md).
    repo, shas = _repo_with_commits(tmp_path / "r", 6)
    _write_status(repo, shas[-4][:7])
    fails = fresh.check(repo)
    assert fails and "freshness:" in fails[0]
