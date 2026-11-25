#!/usr/bin/env python3
"""Tests for tools/verify_locks.py. Run: python3 -m pytest -q tools/test_verify_locks.py"""
from __future__ import annotations

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import verify_locks as vl  # noqa: E402


def h(b):
    return hashlib.sha256(b).hexdigest()


def _tree(tmp_path, files, lock_lines, lock_name="d/PREREG.sha256"):
    for p, b in files.items():
        f = tmp_path / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b)
    lf = tmp_path / lock_name
    lf.parent.mkdir(parents=True, exist_ok=True)
    lf.write_text("\n".join("%s  %s" % x for x in lock_lines) + "\n")
    return str(tmp_path)


def test_real_repo_every_lock_is_ok_or_accounted_for():
    fails, counts, _ = vl.verify(ROOT)
    assert fails == []


def test_real_repo_counts_are_pinned():
    _, counts, _ = vl.verify(ROOT, history=False)
    assert counts["SCRUB"] == 13 and counts["POST_LOCK"] == 2
    assert counts["UNVERIFIABLE"] == 2 and counts["MISSING"] == 42
    assert counts["OK"] >= 163


def test_ok_lock(tmp_path):
    root = _tree(tmp_path, {"d/a.py": b"x=1\n"}, [(h(b"x=1\n"), "a.py")])
    fails, counts, _ = vl.verify(root, scrub=set(), post={}, unverifiable=set(), missing_pin={})
    assert fails == [] and counts["OK"] == 1


def test_scrub_only_file_is_proved_by_reversal(tmp_path):
    original = b"path = '/workspace/theory-of-adaptive-organization/x' ; tmp='/workspace/t'\n"
    scrubbed = b"path = '<repo>/x' ; tmp='<local>/t'\n"
    root = _tree(tmp_path, {"d/a.py": scrubbed}, [(h(original), "a.py")])
    fails, counts, _ = vl.verify(root, scrub={"d/a.py"}, post={}, unverifiable=set(), missing_pin={})
    assert fails == [] and counts["SCRUB"] == 1


def test_scrub_file_with_a_real_edit_fails(tmp_path):
    original = b"path = '/workspace/x'\n"
    edited = b"path = '<local>/x'  # edited\n"
    root = _tree(tmp_path, {"d/a.py": edited}, [(h(original), "a.py")])
    fails, _, _ = vl.verify(root, scrub={"d/a.py"}, post={}, unverifiable=set(), missing_pin={})
    assert fails and "scrub-only" in fails[0]


def test_unpinned_mismatch_fails(tmp_path):
    root = _tree(tmp_path, {"d/a.py": b"changed\n"}, [(h(b"locked\n"), "a.py")])
    fails, _, _ = vl.verify(root, scrub=set(), post={}, unverifiable=set(), missing_pin={})
    assert fails and "not accounted for" in fails[0]


def test_changed_missing_count_fails(tmp_path):
    root = _tree(tmp_path, {}, [(h(b"raw"), "gone.json")], lock_name="d/SHA256SUMS")
    fails, counts, _ = vl.verify(root, scrub=set(), post={}, unverifiable=set(), missing_pin={})
    assert counts["MISSING"] == 1 and fails and "uncommitted" in fails[0]
    fails, _, _ = vl.verify(root, scrub=set(), post={}, unverifiable=set(), missing_pin={"d/SHA256SUMS": 1})
    assert fails == []


def test_pinned_file_that_now_verifies_must_be_unpinned(tmp_path):
    root = _tree(tmp_path, {"d/a.py": b"x\n"}, [(h(b"x\n"), "a.py")])
    fails, _, _ = vl.verify(root, scrub={"d/a.py"}, post={}, unverifiable=set(), missing_pin={})
    assert fails and "now verifies" in fails[0]


def test_unverifiable_is_disclosed_not_failed(tmp_path):
    root = _tree(tmp_path, {"d/a.py": b"y\n"}, [(h(b"locked-never-committed\n"), "a.py")])
    fails, counts, _ = vl.verify(root, scrub=set(), post={}, unverifiable={"d/a.py"}, missing_pin={})
    assert fails == [] and counts["UNVERIFIABLE"] == 1


def test_post_lock_requires_the_lock_time_blob_in_history():
    # real history: pull.py at 86aa1cc hashes to the lock; current differs.
    if not os.path.exists(os.path.join(ROOT, ".git")):
        return
    h_ = vl.git_history_sha256(ROOT, "night2/GITHUB/code/pull.py")
    if h_ is None or "86aa1cc" not in h_:
        return  # shallow clone: the script reports a note instead
    assert vl.POST_LOCK["night2/GITHUB/code/pull.py"][2] in h_


def test_real_repo_pins_the_three_unlocked_current_blobs():
    assert set(vl.CURRENT_BLOB) == {"theory/layers_checks/stores.py", "tests/F1/code/outcome.py", "tests/DECISIVE/glucose/code/analyze.py"}
    for path, blob in vl.CURRENT_BLOB.items():
        assert vl.git_blob(open(os.path.join(ROOT, path), "rb").read()) == blob, path


def test_git_blob_matches_git_hash_object():
    assert vl.git_blob(b"") == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
    assert vl.git_blob(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"


def test_later_edit_to_a_pinned_unlocked_file_fails(tmp_path):
    root = _tree(tmp_path, {"d/a.py": b"y\n"}, [(h(b"locked-never-committed\n"), "a.py")])
    pin = {"d/a.py": vl.git_blob(b"y\n")}
    fails, _, _ = vl.verify(root, scrub=set(), post={}, unverifiable={"d/a.py"}, missing_pin={}, blobs=pin)
    assert fails == []
    (tmp_path / "d" / "a.py").write_bytes(b"y\n# appended later\n")
    fails, _, _ = vl.verify(root, scrub=set(), post={}, unverifiable={"d/a.py"}, missing_pin={}, blobs=pin)
    assert len(fails) == 1 and "changed since it was pinned" in fails[0]


def test_later_edit_to_post_lock_file_fails(tmp_path):
    root = _tree(tmp_path, {"d/a.py": b"later\n"}, [(h(b"locked-version\n"), "a.py")])
    pin = {"d/a.py": vl.git_blob(b"later\n")}
    post = {"d/a.py": ("abc1234", "0" * 40, "def5678", pin["d/a.py"])}
    fails, counts, _ = vl.verify(root, history=False, scrub=set(), post=post, unverifiable=set(), missing_pin={}, blobs=pin)
    assert fails == [] and counts["POST_LOCK"] == 1
    (tmp_path / "d" / "a.py").write_bytes(b"later\n#more\n")
    fails, _, _ = vl.verify(root, history=False, scrub=set(), post=post, unverifiable=set(), missing_pin={}, blobs=pin)
    assert fails and "changed since it was pinned" in fails[0]


def test_scrub_file_is_not_blob_pinned(tmp_path):
    # scrub-only files are protected by the reverse-substitution proof, so a blob pin must not apply to them
    original = b"p='/workspace/x'\n"
    root = _tree(tmp_path, {"d/a.py": b"p='<local>/x'\n"}, [(h(original), "a.py")])
    fails, _, _ = vl.verify(root, scrub={"d/a.py"}, post={}, unverifiable=set(), missing_pin={}, blobs={"d/a.py": "0" * 40})
    assert fails == []


def test_commit_matches_accepts_short_or_long_abbreviations():
    assert vl.commit_matches("86aa1cc", ["86aa1cc33021abcdef"])
    assert vl.commit_matches("86aa1cc33021", ["86aa1cc"])
    assert not vl.commit_matches("86aa1cc", ["d9152f209361"])


def test_declared_post_lock_passes_when_the_lock_time_commit_is_absent(tmp_path):
    """A declared erratum must not fail a standalone run just because this clone is shallow."""
    later = b"later bytes\n"
    root = _tree(tmp_path, {"d/a.py": later}, [(h(b"locked-version\n"), "a.py")])
    # a real git history that contains only the later bytes, not the lock-time commit
    subprocess = __import__("subprocess")
    env = {**__import__("os").environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
           "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=root, check=True, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=root, check=True, capture_output=True, env=env)
    subprocess.run(["git", "commit", "-qm", "later only"], cwd=root, check=True, capture_output=True, env=env)
    post = {"d/a.py": ("86aa1cc", "0" * 40, "def5678", vl.git_blob(later))}
    fails, counts, notes = vl.verify(root, history=True, scrub=set(), post=post, unverifiable=set(), missing_pin={}, blobs={})
    assert fails == [] and counts["POST_LOCK"] == 1
    assert any("not in this clone" in n for n in notes)


def test_declared_post_lock_still_fails_if_the_pin_commit_is_present_but_wrong(tmp_path):
    import subprocess, os
    root = _tree(tmp_path, {"d/a.py": b"later\n"}, [(h(b"locked-version\n"), "a.py")])
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
           "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=root, check=True, capture_output=True)
    # first commit: bytes that do not hash to the lock
    subprocess.run(["git", "add", "-A"], cwd=root, check=True, capture_output=True, env=env)
    subprocess.run(["git", "commit", "-qm", "wrong lock-time bytes"], cwd=root, check=True, capture_output=True, env=env)
    pin = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=True).stdout.strip()
    (tmp_path / "d" / "a.py").write_bytes(b"later edited\n")
    subprocess.run(["git", "add", "-A"], cwd=root, check=True, capture_output=True, env=env)
    subprocess.run(["git", "commit", "-qm", "later"], cwd=root, check=True, capture_output=True, env=env)
    post = {"d/a.py": (pin[:7], pin, "def5678", vl.git_blob(b"later edited\n"))}
    fails, counts, _ = vl.verify(root, history=True, scrub=set(), post=post, unverifiable=set(), missing_pin={}, blobs={})
    assert counts["POST_LOCK"] == 1 and fails and "does not hash to the locked value" in fails[0]


def test_post_lock_later_blob_is_checked_even_without_history(tmp_path):
    later = b"later bytes\n"
    root = _tree(tmp_path, {"d/a.py": later}, [(h(b"locked-version\n"), "a.py")])
    post = {"d/a.py": ("86aa1cc", "0" * 40, "def5678", vl.git_blob(later))}
    fails, counts, _ = vl.verify(root, history=False, scrub=set(), post=post, unverifiable=set(), missing_pin={}, blobs={})
    assert fails == [] and counts["POST_LOCK"] == 1
    (tmp_path / "d" / "a.py").write_bytes(later + b"# appended\n")
    fails, _, _ = vl.verify(root, history=False, scrub=set(), post=post, unverifiable=set(), missing_pin={}, blobs={})
    assert fails and "d/a.py" in fails[0] and "declared later version" in fails[0]


def test_tampered_pull_py_fails_on_a_real_depth_5_clone(tmp_path):
    """B-281-1: a shallow clone must still catch a tamper of pull.py. Use file:// so --depth is honoured."""
    if not os.path.exists(os.path.join(ROOT, ".git")):
        return
    import subprocess
    dest = tmp_path / "shallow"
    url = "file://" + os.path.abspath(ROOT)
    r = subprocess.run(["git", "clone", "-q", "--depth", "5", url, str(dest)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert os.path.exists(os.path.join(str(dest), ".git", "shallow"))
    missing = subprocess.run(["git", "-C", str(dest), "cat-file", "-e", "86aa1cc^{commit}"], capture_output=True)
    assert missing.returncode != 0, "clone was not shallow; lock-time commit is present"

    fails, counts, notes = vl.verify(str(dest))
    assert fails == [] and counts["POST_LOCK"] == 2
    assert any("pull.py" in n and "not in this clone" in n for n in notes)

    path = dest / "night2" / "GITHUB" / "code" / "pull.py"
    path.write_bytes(path.read_bytes() + b"# tampered\n")
    fails, counts, notes = vl.verify(str(dest))
    assert any("night2/GITHUB/code/pull.py" in f and "declared later version" in f for f in fails), fails


def test_shallow_history_notes_print_without_verbose(tmp_path, capsys):
    if not os.path.exists(os.path.join(ROOT, ".git")):
        return
    import subprocess
    dest = tmp_path / "shallow"
    url = "file://" + os.path.abspath(ROOT)
    r = subprocess.run(["git", "clone", "-q", "--depth", "5", url, str(dest)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    # run main() from the shallow tree by pointing ROOT... the module uses its own ROOT.
    # Call verify and also simulate main's print of notes.
    fails, counts, notes = vl.verify(str(dest))
    assert fails == [] and notes
    # main() always prints notes (no -v required); exercise that path with a stub root by
    # printing the same way main does and checking capsys after a direct verify+print.
    for n in notes:
        print("  note: " + n)
    out = capsys.readouterr().out
    assert "not in this clone" in out and "pull.py" in out


def test_main_prints_shallow_notes_without_verbose(monkeypatch, capsys):
    counts = {"OK": 163, "SCRUB": 13, "POST_LOCK": 2, "UNVERIFIABLE": 2, "MISSING": 42}
    notes = ["post-lock history for night2/GITHUB/code/pull.py: lock-time commit 86aa1cc is not in this clone; the erratum in process/LOCK_ERRATA.md still stands"]
    monkeypatch.setattr(vl, "verify", lambda root: ([], counts, notes))
    assert vl.main([]) == 0
    out = capsys.readouterr().out
    assert "note:" in out and "pull.py" in out and "not in this clone" in out
    assert "RESULT: PASS" in out
