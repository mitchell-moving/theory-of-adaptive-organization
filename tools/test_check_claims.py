#!/usr/bin/env python3
"""Mutation tests for tools/check_claims.py.

The clean tree must pass. Each planted error must be reported.
"""
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_claims as cc  # noqa: E402


def copy_tree():
    import tempfile
    dest = tempfile.mkdtemp()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
        for name in filenames:
            if not name.endswith((".md", ".py", ".json")):
                continue
            src = os.path.join(dirpath, name)
            rel = os.path.relpath(src, ROOT)
            out = os.path.join(dest, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            shutil.copy(src, out)
    return dest


def fails_of(root):
    return "\n".join(cc.check(root))


def test_clean_tree_passes():
    assert cc.check(ROOT) == []


def test_proved_to_open_mismatch(tmp_path=None):
    root = copy_tree()
    try:
        path = os.path.join(root, "measurement/CLAIM_MAP_v2.md")
        text = open(path, encoding="utf-8").read()
        old = "| T61 | proved-in-model |"
        assert old in text
        open(path, "w", encoding="utf-8").write(text.replace(old, "| T61 | open |", 1))
        got = fails_of(root)
        assert "mismatch" in got, got
    finally:
        shutil.rmtree(root)


def test_unsupported_front_page_claim():
    root = copy_tree()
    try:
        path = os.path.join(root, "README.md")
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("\n\nT99 is PROVED in the model.\n")
        got = fails_of(root)
        assert "unmanaged" in got, got
    finally:
        shutil.rmtree(root)


def test_deleted_source_row():
    root = copy_tree()
    try:
        path = os.path.join(root, "measurement/CLAIM_MAP_v2.md")
        text = open(path, encoding="utf-8").read()
        old = "| THEORY.md:41 |"
        assert old in text
        open(path, "w", encoding="utf-8").write(text.replace(old, "| missing/NO_SUCH.md:1 |", 1))
        got = fails_of(root)
        assert "source missing" in got, got
    finally:
        shutil.rmtree(root)


def test_wrong_review_path():
    root = copy_tree()
    try:
        path = os.path.join(root, "measurement/CLAIM_MAP_v2.md")
        text = open(path, encoding="utf-8").read()
        old = "`reviews/coadaptation_2026-11-21/REVIEW.md`"
        assert old in text
        open(path, "w", encoding="utf-8").write(
            text.replace(old, "`reviews/no-such-review-2026.md`", 1)
        )
        got = fails_of(root)
        assert "review path missing" in got, got
    finally:
        shutil.rmtree(root)


def test_whole_physics_lean_claim():
    root = copy_tree()
    try:
        path = os.path.join(root, "README.md")
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("\n\nThe whole physical theorem is formalized in Lean.\n")
        got = fails_of(root)
        assert "lean overclaim" in got, got
    finally:
        shutil.rmtree(root)


def test_changed_hypothesis_sentence():
    root = copy_tree()
    try:
        path = os.path.join(root, "README.md")
        text = open(path, encoding="utf-8").read()
        assert cc.HYPOTHESIS in text
        changed = cc.HYPOTHESIS.replace("minimize", "maximizes")
        open(path, "w", encoding="utf-8").write(text.replace(cc.HYPOTHESIS, changed, 1))
        got = fails_of(root)
        assert "hypothesis sentence" in got, got
    finally:
        shutil.rmtree(root)


def test_invalid_edge():
    root = copy_tree()
    try:
        path = os.path.join(root, "measurement/CLAIM_MAP_v2.md")
        text = open(path, encoding="utf-8").read()
        old = "CX2:open"
        assert old in text
        open(path, "w", encoding="utf-8").write(text.replace(old, "NO_SUCH_EDGE:bogus", 1))
        got = fails_of(root)
        assert "edge" in got, got
    finally:
        shutil.rmtree(root)


if __name__ == "__main__":
    test_clean_tree_passes()
    test_proved_to_open_mismatch()
    test_unsupported_front_page_claim()
    test_deleted_source_row()
    test_wrong_review_path()
    test_whole_physics_lean_claim()
    test_changed_hypothesis_sentence()
    test_invalid_edge()
    print("RESULT: PASS")
