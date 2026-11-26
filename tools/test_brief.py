#!/usr/bin/env python3
"""Tests for tools/brief.py (the live brief; no page keeps a hand pointer since 25 November 2026).

Run:  python3 -m pytest -q tools/test_brief.py
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import textwrap

import pytest


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import brief

REAL_STALE = brief.stale_reviewed_prs


def _git(repo, *args, env=None):
    e = os.environ.copy()
    e.update({
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.com",
        "GIT_AUTHOR_DATE": e.get("GIT_AUTHOR_DATE", "2026-11-21T12:00:00-05:00"),
        "GIT_COMMITTER_DATE": e.get("GIT_COMMITTER_DATE", "2026-11-21T12:00:00-05:00"),
    })
    if env:
        e.update(env)
    r = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, env=e)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _init_repo(dest, n_merges=4):
    """A small repo with main, THEORY/CLAIM_MAP/CORE/README, and n PR merges."""
    os.makedirs(dest)
    _git(dest, "init", "-b", "main")
    _git(dest, "config", "user.name", "Test")
    _git(dest, "config", "user.email", "test@example.com")
    os.makedirs(os.path.join(dest, "measurement"))
    os.makedirs(os.path.join(dest, "tools"))
    shutil.copy(os.path.join(ROOT, "tools", "brief.py"), os.path.join(dest, "tools"))

    def write(rel, body):
        path = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)

    write("THEORY.md", "# A Theory of Adaptive Organization v2.9 draft\n\nClaim statuses: `measurement/CLAIM_MAP_v2.md` (v2.69)\n")
    write(
        "measurement/CLAIM_MAP_v2.md",
        textwrap.dedent("""\
        **v2.68 note (old).**
        **v2.69 note (EVO1).**
        <!-- tally:begin -->
        | Status now (all sections) | Rows |
        |---|---|
        | OPEN | 2 |
        | PROVED (in-model) | 1 |
        | **Total** | **3** |
        <!-- tally:end -->
        """),
    )
    write(
        "CORE.md",
        textwrap.dedent("""\
        ## 3. The hypothesis

        **The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**
        """),
    )
    write(
        "README.md",
        textwrap.dedent("""\
        # Front page

        | ID | Item | State | Gate | Where |
        |---|---|---|---|---|
        | W1 | already shipped | **DONE.** Merged as `abc` | DONE | PR |
        | W2 | still open | in flight | needs reviewer | PR |
        | W3 | also open | notes | in progress | file |

        | ID | Item | Gate | Where |
        |---|---|---|---|
        | H1 | leftover | needs Chad (deletion only) | GitHub |
        | H2 | finished | **DONE** in this PR | file |
        """),
    )
    _git(dest, "add", ".")
    _git(dest, "commit", "-m", "seed")

    merges = []
    for i in range(1, n_merges + 1):
        branch = "feat-%d" % i
        _git(dest, "checkout", "-b", branch)
        write("f%d.txt" % i, "x%d\n" % i)
        _git(dest, "add", "f%d.txt" % i)
        env = {
            "GIT_AUTHOR_DATE": "2026-11-21T%02d:00:00-05:00" % (8 + i),
            "GIT_COMMITTER_DATE": "2026-11-21T%02d:00:00-05:00" % (8 + i),
        }
        _git(dest, "commit", "-m", "work %d" % i, env=env)
        _git(dest, "checkout", "main")
        # Offset merge times so brief.py can show distinct clocks.
        env = {
            "GIT_AUTHOR_DATE": "2026-11-21T%02d:15:00-05:00" % (8 + i),
            "GIT_COMMITTER_DATE": "2026-11-21T%02d:15:00-05:00" % (8 + i),
        }
        _git(
            dest,
            "merge",
            "--no-ff",
            "-m",
            "Merge pull request #%d from test/feat-%d\n\nFeature %d title" % (i, i, i),
            branch,
            env=env,
        )
        sha = _git(dest, "rev-parse", "HEAD")
        merges.append(sha)
    return dest, merges


@pytest.fixture(autouse=True)
def _no_live_gh(monkeypatch, request):
    if "live_gh" not in request.keywords:
        monkeypatch.setattr(brief, "stale_reviewed_prs", lambda root: ["Stale reviewed PRs: none"])


def test_brief_from_real_repo_runs():
    out = brief.render(ROOT)
    assert "GTAO live brief" in out
    assert "America/New_York" in out
    assert "THEORY.md v2.9" in out
    assert "CLAIM_MAP v2.89" in out
    assert "tally: total 392" in out
    assert "strongly selected systems minimize the cost of judgment" in out
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    # On a side branch the brief still reports main; on main it is HEAD.
    assert "main HEAD:" in out


def test_brief_lists_merges_hypothesis_and_open_work(tmp_path):
    repo, merges = _init_repo(tmp_path / "r", n_merges=4)
    out = brief.render(repo)
    assert "Feature 4 title" in out
    assert "Feature 1 title" in out
    assert "#4" in out
    assert "21 Nov 2026" in out
    assert "ET" in out
    assert "THEORY.md v2.9" in out
    assert "CLAIM_MAP v2.69" in out
    assert "tally: total 3" in out
    assert "OPEN 2" in out
    assert "strongly selected systems minimize the cost of judgment" in out
    assert "W2  needs reviewer" in out
    assert "W3  in progress" in out
    assert "H1  needs Chad" in out
    assert "W1  " not in out.split("Open work")[1]  # DONE row omitted
    assert "H2  " not in out.split("Open work")[1]
    assert "Stale reviewed PRs: none" in out


def test_stale_reviewed_pr_is_a_warning_in_the_brief(tmp_path, monkeypatch):
    # Acceptance: an unrelated stale PR only warns (brief.py), it never fails a check.
    import check_pending
    monkeypatch.setattr(check_pending, "collect", lambda api, **k: (["upstream#280 (Old work): reviewed 30h ago"], []))
    monkeypatch.setattr(check_pending, "read_parked", lambda root: ({}, []))
    out = REAL_STALE(str(tmp_path))
    assert out == ["WARN stale reviewed PR (merge, park in process/PROCESS.md §4, or close): upstream#280 (Old work): reviewed 30h ago"]
    monkeypatch.setattr(check_pending, "collect", lambda api, **k: (_ for _ in ()).throw(check_pending.Offline("no network")))
    assert REAL_STALE(str(tmp_path))[0].startswith("Stale reviewed PRs: not checked")


def test_brief_degrades_when_gh_missing(tmp_path, monkeypatch):
    repo, merges = _init_repo(tmp_path / "r", n_merges=1)
    monkeypatch.setattr(brief.shutil, "which", lambda name: None)
    out = brief.render(repo)
    assert "gh unavailable; skipped" in out


def test_pr_number_covers_merge_handwritten_and_squash_subjects():
    assert brief.pr_number("Merge pull request #183 from Chad-Mitchell/x") == 183
    assert brief.pr_number("Merge PR #206: front-page rewrite (reviewed #207)") == 206
    assert brief.pr_number("Update STATUS main pointer for PRs #210-#212 (#213)") == 213
    assert brief.pr_number("Point STATUS at the #209 pointer and record the #206 merge") is None
