#!/usr/bin/env python3
"""Tests for tools/banned_words.py. Run: python3 -m pytest -q tools/test_banned_words.py"""
from __future__ import annotations

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import banned_words as bw  # noqa: E402


def test_each_word_is_caught():
    for w in ("puzzle", "puzzles", "bill", "billed", "kill", "killed", "dead", "verdict", "VERDICT"):
        assert bw.hits("This is a %s here." % w), w


def test_plain_words_are_not_caught():
    assert bw.hits("The miss is open; the cost is small; the outcome is a result.") == []
    assert bw.hits("Dedicated deadline, skilled billet.") == []


def test_quoted_and_backticked_are_exempt():
    assert bw.hits("Never say `puzzle` or \"kill\" or “dead” or ‘verdict’.") == []
    assert bw.hits("It is a \"quoted\" line, but the verdict is not.") == ["verdict"]


def test_escape_marker_needs_a_reason():
    assert bw.hits("kill rule <!-- banned-ok: locked-test term from the prereg -->") == []
    assert bw.hits("kill rule <!-- banned-ok: -->") == ["kill"]


def test_rule_files_exempt_tables_lists_and_ban_statements_only():
    assert bw.hits("| a | puzzle | b |", "process/PROCESS.md") == []
    assert bw.hits("| a | puzzle | b |", "STATUS.md") == ["puzzle"]
    assert bw.hits("Use no kill, verdict or puzzle wording.", "process/FAILURES.md") == []
    assert bw.hits("These words are banned: dead.", "process/VOCABULARY.md") == []
    assert bw.hits("It was a verdict.", "process/PROCESS.md") == ["verdict"]


def test_puzzle_check_ignores_rule_statements():
    assert bw.puzzle_hits("An open puzzle.", "STATUS.md") == ["puzzle"]
    assert bw.puzzle_hits("'puzzle' is banned.", "process/PROCESS.md") == []


def _git(cwd, *a):
    subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True,
                   env={**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def _repo(tmp_path):
    d = str(tmp_path)
    _git(d, "init", "-q", "-b", "main")
    open(os.path.join(d, "a.md"), "w").write("old kill rule stays\nplain\n")
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "base")
    _git(d, "update-ref", "refs/remotes/origin/main", "HEAD")
    return d


def test_only_added_lines_fail(tmp_path):
    d = _repo(tmp_path)
    assert bw.check_added(d) == ([], None)          # old "kill" line is not rescanned
    with open(os.path.join(d, "a.md"), "a") as f:
        f.write("a new verdict line\nclean line\n")
    fails, note = bw.check_added(d)
    assert note is None and len(fails) == 1 and "a.md:3" in fails[0]


def test_changed_old_line_counts_as_added(tmp_path):
    d = _repo(tmp_path)
    open(os.path.join(d, "a.md"), "w").write("old kill rule stays, edited\nplain\n")
    fails, _ = bw.check_added(d)
    assert len(fails) == 1 and "a.md:1" in fails[0]


def test_committed_added_lines_fail_too(tmp_path):
    d = _repo(tmp_path)
    open(os.path.join(d, "b.md"), "w").write("the dead end\n")
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "b")
    fails, _ = bw.check_added(d)
    assert len(fails) == 1 and "b.md:1" in fails[0]


def test_no_origin_main_is_reported_not_passed(tmp_path):
    d = str(tmp_path)
    _git(d, "init", "-q", "-b", "main")
    open(os.path.join(d, "a.md"), "w").write("x\n")
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "base")
    fails, note = bw.check_added(d)
    assert fails == [] and note and "skipped" in note


def test_non_markdown_files_are_ignored(tmp_path):
    d = _repo(tmp_path)
    open(os.path.join(d, "x.py"), "w").write("# verdict\n")
    assert bw.check_added(d) == ([], None)


def test_maintained_docs_have_no_puzzle():
    from check_consistency import MAINTAINED_DOCS
    files = [f for f in MAINTAINED_DOCS if os.path.exists(os.path.join(ROOT, f))]
    assert files and bw.check_puzzle(ROOT, files) == []


# ---- locked files are exempt only while their bytes are unchanged ----
import hashlib  # noqa: E402


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _blob(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def _locked_repo(tmp_path):
    d = _repo(tmp_path)
    return d


def test_hash_locked_file_is_exempt_while_unchanged(tmp_path):
    d = _repo(tmp_path)
    prereg = b"This is a puzzle and a verdict, locked.\n"
    os.makedirs(os.path.join(d, "t"))
    open(os.path.join(d, "t", "PREREG.md"), "wb").write(prereg)
    open(os.path.join(d, "t", "PREREG.sha256"), "w").write("%s  PREREG.md\n" % _sha(prereg))
    open(os.path.join(d, "t", "notes.md"), "w").write("another puzzle here\n")
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "add")
    fails, _ = bw.check_added(d)
    assert len(fails) == 1 and "t/notes.md" in fails[0]       # only the unlocked file


def test_edited_locked_file_is_scanned_again(tmp_path):
    d = _repo(tmp_path)
    prereg = b"A locked puzzle line.\n"
    os.makedirs(os.path.join(d, "t"))
    open(os.path.join(d, "t", "PREREG.md"), "wb").write(prereg)
    open(os.path.join(d, "t", "SHA256SUMS"), "w").write("%s  PREREG.md\n" % _sha(prereg))
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "add")
    assert bw.check_added(d) == ([], None)
    open(os.path.join(d, "t", "PREREG.md"), "wb").write(prereg + b"and a new kill line\n")
    fails, _ = bw.check_added(d)
    assert fails and "t/PREREG.md" in fails[0]


def test_scrubbed_hash_locked_file_is_exempt(tmp_path):
    d = _repo(tmp_path)
    original = b"path /workspace/x has a puzzle\n"
    os.makedirs(os.path.join(d, "t"))
    open(os.path.join(d, "t", "PREREG.md"), "wb").write(b"path <local>/x has a puzzle\n")
    open(os.path.join(d, "t", "LOCK.txt"), "w").write("%s  PREREG.md\n" % _sha(original))
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "add")
    assert bw.check_added(d) == ([], None)


def test_blob_listed_file_is_exempt_only_for_that_blob(tmp_path):
    d = _repo(tmp_path)
    locked = b"locked by commit order: a verdict\n"
    os.makedirs(os.path.join(d, "process"))
    open(os.path.join(d, "x.md"), "wb").write(locked)
    open(os.path.join(d, "process", "LOCKED_BLOBS.txt"), "w").write(
        "# comment\nx.md %s committed before the run\n" % _blob(locked))
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "add")
    _git(d, "update-ref", "refs/remotes/origin/main", "HEAD")  # exemption is on main
    assert bw.check_added(d) == ([], None)
    open(os.path.join(d, "x.md"), "wb").write(b"a verdict, now edited\n")
    fails, _ = bw.check_added(d)
    assert fails and "x.md" in fails[0]


def test_same_pr_new_exemption_plus_banned_word_is_flagged(tmp_path):
    """B-278-2: a PR cannot add a LOCKED_BLOBS line and a banned word in the same change."""
    d = _repo(tmp_path)  # origin/main has no LOCKED_BLOBS.txt
    locked = b"a verdict in a file this PR also exempts\n"
    os.makedirs(os.path.join(d, "process"))
    open(os.path.join(d, "x.md"), "wb").write(locked)
    open(os.path.join(d, "process", "LOCKED_BLOBS.txt"), "w").write(
        "x.md %s added in the same PR\n" % _blob(locked))
    _git(d, "add", "-A"); _git(d, "commit", "-qm", "exemption and word together")
    fails, note = bw.check_added(d)
    assert note is None and fails and "x.md" in fails[0] and "verdict" in fails[0]


def test_blob_list_ignores_malformed_lines():
    assert bw.parse_blob_list("x.md notablob why\njust-one-field\n# c\n") == {}


def test_blob_list_is_read_from_origin_main_not_the_working_tree():
    working = os.path.join(ROOT, "process", "LOCKED_BLOBS.txt")
    assert os.path.isfile(working), "this PR keeps process/LOCKED_BLOBS.txt"
    text = open(working, encoding="utf-8").read()
    assert "theory/composite-contest-2026-11-24/PREREG_4.md" in text
    assert "6f97e49b0f0d4674726c5558e967903636d24905" in text
    assert "theory/menu3_checks/RUN_LOG.md" in text
    assert "3a5efc2adf5a498d5f1f9f9403157136c6d880c9" in text
    listed = bw.blob_list(ROOT)
    shown = bw.git(ROOT, "show", "origin/main:process/LOCKED_BLOBS.txt")
    if shown.returncode != 0:
        assert listed == {}
    else:
        assert listed == bw.parse_blob_list(shown.stdout)


def test_standalone_entry_point(capsys):
    # Ace nit: banned_words.py has a real entry point.
    rc = bw.main(["banned_words.py", ROOT])
    out = capsys.readouterr().out
    assert rc in (0, 2) and "RESULT:" in out
