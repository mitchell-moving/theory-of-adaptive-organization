#!/usr/bin/env python3
"""Tests for tools/check_fresh.py: no maintained page keeps a live fact by hand (25 November 2026).

Run:  python3 -m pytest -q tools/test_check_fresh.py
"""
from __future__ import annotations

import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_fresh as cf  # noqa: E402


def _copy(tmp_path):
    d = tmp_path / "r"
    for p in cf.live_pages(ROOT):
        dst = d / p
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(os.path.join(ROOT, p), dst)
    return d


def _plant(tmp_path, rel, text, append=True):
    d = _copy(tmp_path)
    p = d / rel
    p.write_text((p.read_text(encoding="utf-8") if append else "") + text, encoding="utf-8")
    return cf.check(str(d))


def test_real_tree_passes():
    assert cf.check(ROOT) == []


def test_planted_main_sha_fails(tmp_path):
    # Acceptance: a planted "main is abc1234" line fails.
    fails = _plant(tmp_path, "README.md", "\n\nThis page is current: `main` is `abc1234`.\n")
    assert len(fails) == 1 and "main SHA pointer" in fails[0] and "README.md" in fails[0]


def test_planted_open_pr_list_fails(tmp_path):
    fails = _plant(tmp_path, "process/PROCESS.md", "\n\nOpen upstream PRs not yet merged: #288 (Lean) and #290.\n")
    assert len(fails) == 1 and "open-PR list" in fails[0]


def test_planted_version_string_fails(tmp_path):
    # Acceptance: an edited version string outside its source fails.
    fails = _plant(tmp_path, "theory/SCALE_ENDS.md", "\n\nThe core is THEORY v2.9 draft.\n")
    assert len(fails) == 1 and "version string" in fails[0]
    fails = _plant(tmp_path, "applications/README.md", "\n\nClaim statuses: `measurement/CLAIM_MAP_v2.md` (v2.89).\n")
    assert len(fails) == 1 and "version string" in fails[0]


def test_planted_lean_total_fails(tmp_path):
    # Acceptance: an edited Lean total outside AUDIT.json fails.
    fails = _plant(tmp_path, "formal/lean/README.md", "\n\nLean now machine-checks **1370 declarations**.\n")
    assert len(fails) == 1 and "Lean total" in fails[0]


def test_core_canonical_statement_is_allow_listed():
    line = "`THEORY.md` is the canonical statement (v2.9 draft)."
    assert cf.hand_pointers(line, "CORE.md") == []
    assert cf.hand_pointers(line, "README.md") != []


def test_history_block_is_skipped():
    text = "a\n<!-- history:begin -->\nbatch 1: **757 declarations**\n<!-- history:end -->\nb\n"
    assert cf.hand_pointers(text, "formal/lean/README.md") == []


def test_prose_and_tables_are_not_pointers():
    assert cf.hand_pointers("The word main is feedback in prose.") == []
    assert cf.hand_pointers("domain is deadbeef; remain is deadbeef") == []
    assert cf.hand_pointers("| W14 | Prereg locked beside `main` `2c32ade`. | needs data | file |") == []
    assert len(cf.hand_pointers("current to main deadbeef")) == 1
    assert len(cf.hand_pointers("**As of:** Monday, on `main` `2c32ade` (PR #1).")) == 1


def test_cli_exit_codes(tmp_path, capsys):
    assert cf.main(["check_fresh.py", ROOT, "--offline"]) == 0
    assert "RESULT: PARTIAL" in capsys.readouterr().out
    d = _copy(tmp_path)
    (d / "README.md").write_text("`main` is `abc1234`\n", encoding="utf-8")
    assert cf.main(["check_fresh.py", str(d), "--offline"]) == 1
    assert "RESULT: FAIL" in capsys.readouterr().out


# ---------------------------------------------------------------- round 2 (Ace review of #291)
FAKE_MAIN = ["1eed183" + "0" * 33, "abc1234def" + "1" * 30, "591fb7b" + "2" * 33]
WORDINGS = ["Current main: abc1234def", "As of main abc1234", "HEAD is 1eed183", "Latest merge: 1eed183 (PR #288)"]


def test_four_sha_wordings_fail_by_rule_without_git():
    # Acceptance: each of the four wordings fails even with no git history to compare against.
    for w in WORDINGS:
        got = cf.hand_pointers(w, "README.md", recent=())
        assert got and got[0][1] == "main SHA pointer", (w, got)


def test_four_sha_wordings_fail_when_planted(tmp_path):
    # Acceptance: each of the four wordings, planted on a live page, fails.
    for i, w in enumerate(WORDINGS):
        d = _copy(tmp_path / str(i))
        p = d / "README.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n\n" + w + "\n", encoding="utf-8")
        fails = cf.check(str(d), recent=FAKE_MAIN)
        assert len(fails) == 1 and "README.md" in fails[0], (w, fails)


def test_any_recent_main_sha_fails_in_any_wording():
    got = cf.hand_pointers("See 591fb7b for the details.", "process/PROCESS.md", recent=FAKE_MAIN)
    assert got and got[0][1] == "recent main SHA"
    assert cf.hand_pointers("See 591fb7b for the details.", "process/PROCESS.md", recent=()) == []
    assert cf.hand_pointers("An old commit `deadbee` is not on the recent list.", "README.md", recent=FAKE_MAIN) == []


def test_merged_as_and_history_block_are_exempt():
    assert cf.hand_pointers("PR #288 merged as `1eed183`.", "README.md", recent=FAKE_MAIN) == []
    text = "a\n<!-- history:begin -->\nHEAD is 1eed183, latest merge 591fb7b\n<!-- history:end -->\nb\n"
    assert cf.hand_pointers(text, "README.md", recent=FAKE_MAIN) == []


def test_permalinks_are_not_pointers():
    url = "[`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md)"
    assert cf.hand_pointers(url, "README.md", recent=FAKE_MAIN) == []


def test_hand_typed_pr_head_fails(tmp_path):
    # Acceptance: a hand-typed PR head fails on any live page.
    for w in ["The review covers head `abc1234`.", "Waiting on PR #291 (head a0508fd)."]:
        got = cf.hand_pointers(w, "process/PROCESS.md", recent=())
        assert got and got[0][1] == "PR head", (w, got)
    fails = _plant(tmp_path, "measurement/FRAMEWORK.md", "\n\nPR #12 (head `abc1234`) is reviewed.\n")
    assert len(fails) == 1 and "PR head" in fails[0]


def test_root_status_page_fails(tmp_path):
    # Acceptance: a root STATUS.md fails.
    d = _copy(tmp_path)
    (d / "STATUS.md").write_text("# Status\n\nAll good.\n", encoding="utf-8")
    fails = cf.check(str(d), recent=[])
    assert fails and any("root page STATUS.md" in f for f in fails) and all("STATUS.md" in f for f in fails)


def test_every_maintained_doc_is_scanned():
    import check_consistency
    pages = set(cf.live_pages(ROOT))
    for p in check_consistency.MAINTAINED_DOCS:
        if os.path.isfile(os.path.join(ROOT, p)) and p not in cf.SKIP:
            assert p in pages, p
    for p in os.listdir(ROOT):
        if p.endswith(".md"):
            assert p in pages and p in cf.ROOT_ALLOW, p


# ---------------------------------------------------------------- round 3 (Ace review of 7a5f33d)
HEADS = {"df114b6" + "3" * 33: "fork#7"}


def test_claim_map_failures_and_physics_chain_are_scanned():
    # Ace 2a/2b: CLAIM_MAP_v2, FAILURES and PHYSICS_CHAIN are maintained pages now.
    pages = cf.live_pages(ROOT)
    for p in ("measurement/CLAIM_MAP_v2.md", "process/FAILURES.md", "theory/PHYSICS_CHAIN_2026-11-23.md"):
        assert p in pages, p


def test_plant_in_claim_map_and_failures_fails_outside_history_only(tmp_path):
    # Ace 2a: a live pointer planted in CLAIM_MAP_v2 or FAILURES fails; the same text in a history block passes.
    for i, rel in enumerate(("measurement/CLAIM_MAP_v2.md", "process/FAILURES.md", "theory/PHYSICS_CHAIN_2026-11-23.md")):
        fails = _plant(tmp_path / ("a%d" % i), rel, "\n\nHEAD is 1eed183.\n")
        assert len(fails) == 1 and rel in fails[0], (rel, fails)
        fails = _plant(tmp_path / ("b%d" % i), rel, "\n\n<!-- history:begin -->\nHEAD is 1eed183.\n<!-- history:end -->\n")
        assert fails == [], (rel, fails)


def test_open_pr_head_wordings_fail(tmp_path):
    # Ace 2c: the three plants fail by rule (no network), and any wording of a live open-PR head fails.
    for w in ["The branch is at df114b6.", "tip: df114b6", "main moved to 1eed183"]:
        got = cf.hand_pointers(w, "README.md", recent=(), heads=None)
        assert got, w
    got = cf.hand_pointers("Compare with df114b6 for the delta.", "README.md", recent=(), heads=HEADS)
    assert got and "open PR head (fork#7)" in got[0][1]
    assert cf.hand_pointers("Compare with df114b6 for the delta.", "README.md", recent=(), heads={}) == []
    for i, w in enumerate(["The branch is at df114b6.", "tip: df114b6", "main moved to 1eed183", "See df114b6."]):
        d = _copy(tmp_path / ("h%d" % i))
        p = d / "process" / "PROCESS.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n\n" + w + "\n", encoding="utf-8")
        fails = cf.check(str(d), recent=[], heads=HEADS)
        assert len(fails) == 1 and "process/PROCESS.md" in fails[0], (w, fails)


def test_open_pr_head_in_history_block_passes():
    text = "<!-- history:begin -->\nReviewed at df114b6.\n<!-- history:end -->\n"
    assert cf.hand_pointers(text, "README.md", recent=(), heads=HEADS) == []


def test_status_or_open_work_in_any_folder_fails(tmp_path):
    # Ace 2e
    for i, rel in enumerate(("theory/STATUS.md", "process/OPEN_WORK.md", "tests/deep/dir/STATUS.md", "OPEN_WORK.md")):
        d = _copy(tmp_path / str(i))
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        (d / rel).write_text("# x\n", encoding="utf-8")
        fails = cf.check(str(d), recent=[])
        assert any(rel in f and "retired page name" in f for f in fails), (rel, fails)


def test_history_begin_at_line_start_fails_on_four_pages(tmp_path):
    # A line that starts with the marker fails on the four front pages, including a block that hides a stale SHA.
    block = "\n<!-- history:begin -->\nHEAD is 1eed183.\n<!-- history:end -->\n"
    for i, rel in enumerate(sorted(cf.NO_HIST_BLOCK)):
        fails = _plant(tmp_path / ("h%d" % i), rel, block)
        assert any(f.startswith("history block at %s:" % rel) for f in fails), (rel, fails)


def test_history_marker_quoted_mid_line_passes(tmp_path):
    # process/PROCESS.md quotes the marker inside backticks mid-line. That line, and a planted copy, pass.
    line = open(os.path.join(ROOT, "process/PROCESS.md"), encoding="utf-8").read().splitlines()[58]
    assert "<!-- history:begin" in line and not line.startswith("<!-- history:begin")
    fails = _plant(tmp_path, "process/PROCESS.md",
                   "\nDated entries sit inside `<!-- history:begin -->` and are skipped.\n")
    assert fails == [], fails


def test_plain_lean_total_fails(tmp_path):
    # Ace 2f
    for w in ["Lean checks 1370 declarations.", "1,370 Lean declarations, OK", "**1370 declarations**"]:
        got = cf.hand_pointers(w, "formal/lean/README.md")
        assert got and got[0][1] == "Lean total", w
    fails = _plant(tmp_path, "formal/lean/README.md", "\n\nThe audit now covers 1370 declarations.\n")
    assert len(fails) == 1 and "Lean total" in fails[0]
