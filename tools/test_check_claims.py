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


# ---------------------------------------------------------------- claims link (views retired), 25 November 2026
def _edit(root, rel, old, new):
    path = os.path.join(root, rel)
    text = open(path, encoding="utf-8").read()
    assert old in text, (rel, old)
    open(path, "w", encoding="utf-8").write(text.replace(old, new, 1))


LINK = "Claim statuses: [`measurement/CLAIM_MAP_v2.md`](measurement/CLAIM_MAP_v2.md) (headline ledger)."
VIEW = cc.VIEW_BEGIN + "\nT61 | proved-in-model | reviewed\n" + cc.VIEW_END


def test_front_pages_carry_the_link_not_a_view():
    for rel in cc.LINK_FILES:
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        assert cc.LINK_RX.search(text) and cc.VIEW_BEGIN not in text, rel


def test_missing_link_fails():
    for rel in ("CORE.md", "THEORY.md"):
        root = copy_tree()
        try:
            _edit(root, rel, LINK, "")
            assert "%s lacks the one-line link" % rel in fails_of(root)
        finally:
            shutil.rmtree(root)


def test_view_planted_anywhere_fails():
    for rel in ("README.md", "CORE.md", "theory/PHYSICS_CHAIN_2026-11-23.md"):
        root = copy_tree()
        try:
            with open(os.path.join(root, rel), "a", encoding="utf-8") as fh:
                fh.write("\n" + VIEW + "\n")
            assert "%s carries a claims view" % rel in fails_of(root)
        finally:
            shutil.rmtree(root)


def test_write_is_retired():
    assert cc.main(["check_claims.py", "--write"]) == 2


# ---------------------------------------------------------------- direction (README.md, Ranked gaps)
def test_data_one_given_a_rank_fails():
    # Acceptance: DATA-ONE given a rank fails.
    root = copy_tree()
    try:
        text = open(os.path.join(root, "README.md"), encoding="utf-8").read()
        row = next(l for l in text.splitlines() if l.startswith("| DATA-ONE | parked |"))
        _edit(root, "README.md", row, row.replace("| DATA-ONE | parked |", "| DATA-ONE | 7 |", 1))
        assert "DATA-ONE is parked work" in fails_of(root)
    finally:
        shutil.rmtree(root)


def test_in_parallel_real_system_line_fails():
    # Acceptance: an "In parallel" real-system line, or a rank for RS-SCREEN outside README Ranked gaps, fails.
    for rel, line in [("theory/PHYSICS_CHAIN_2026-11-23.md", "3. **In parallel (Level 2):** qualify one real system.\n"),
                      ("README.md", "Next after BICAUSAL: RS-SCREEN.\n"),
                      ("process/PROCESS.md", "Real-system work runs in parallel with the physics chain.\n")]:
        root = copy_tree()
        try:
            with open(os.path.join(root, rel), "a", encoding="utf-8") as fh:
                fh.write("\n" + line)
            got = fails_of(root)
            assert "orders real-system work outside README.md Ranked gaps" in got and rel in got, (rel, got)
        finally:
            shutil.rmtree(root)


def test_parked_mention_outside_ranked_table_passes():
    root = copy_tree()
    try:
        with open(os.path.join(root, "README.md"), "a", encoding="utf-8") as fh:
            fh.write("\nDATA-ONE is parked; the next step is not chosen here.\n")
        assert cc.check(root) == []
    finally:
        shutil.rmtree(root)


def test_parked_row_without_restart_or_decider_fails():
    root = copy_tree()
    try:
        text = open(os.path.join(root, "README.md"), encoding="utf-8").read()
        row = next(l for l in text.splitlines() if l.startswith("| RS-SCREEN | parked |"))
        _edit(root, "README.md", row, row.replace("Restart:", "Later:"))
        assert "parked row RS-SCREEN needs" in fails_of(root)
    finally:
        shutil.rmtree(root)


def _direction_line():
    text = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    return next(l for l in text.splitlines() if l.startswith("**Direction ("))


def test_direction_line_has_one_copy():
    copies = [l for l in open(os.path.join(ROOT, "README.md"), encoding="utf-8").read().splitlines()
              if l.startswith("**Direction (")]
    assert len(copies) == 1


def test_second_copy_of_direction_line_fails():
    # Acceptance: a second copy of the direction line fails, wherever it lands.
    for rel in ("process/PROCESS.md", "theory/PHYSICS_CHAIN_2026-11-23.md", "README.md"):
        root = copy_tree()
        try:
            with open(os.path.join(root, rel), "a", encoding="utf-8") as fh:
                fh.write("\n" + _direction_line() + "\n")
            got = fails_of(root)
            assert "the direction line has 2 copies" in got and rel in got, (rel, got)
        finally:
            shutil.rmtree(root)


def test_direction_line_missing_from_readme_fails():
    root = copy_tree()
    try:
        _edit(root, "README.md", _direction_line(), "Physics comes first.")
        assert "README.md has no dated '**Direction" in fails_of(root)
    finally:
        shutil.rmtree(root)


# ---------------------------------------------------------------- work rows have one home (Ace 2d)
def test_work_ids_come_from_readme():
    ids = cc.work_ids(ROOT)
    assert {"BICAUSAL", "DATA-ONE", "T40", "T72", "LOCK-V1.5"} <= ids


def test_work_row_copied_to_another_page_fails():
    plants = [("process/PROCESS.md", "| T40 | Adopt the physical cost display | open |\n"),
              ("theory/PHYSICS_CHAIN_2026-11-23.md", "1. **BICAUSAL** first.\n"),
              ("CORE.md", "| STOP-COPY | 2 | math |\n"),
              ("measurement/FRAMEWORK.md", "2. MV9-DECISION: needs Chad.\n")]
    for rel, line in plants:
        root = copy_tree()
        try:
            with open(os.path.join(root, rel), "a", encoding="utf-8") as fh:
                fh.write("\n\n| a | b |\n|---|---|\n" + line if line.startswith("|") else "\n\n" + line)
            got = fails_of(root)
            assert "work rows: %s" % rel in got, (rel, got)
        finally:
            shutil.rmtree(root)


def test_open_row_and_bicausal_period_fail():
    # Open, not ranked IDs are work rows, and "1. **BICAUSAL.**" is an ordered label.
    ids = cc.work_ids(ROOT)
    assert "T13" in ids and "T21-T24" in ids and "T49-LOSSES" in ids
    plants = [("process/PROCESS.md", "| T13 | Other open conjectures | Open |\n"),
              ("CORE.md", "1. **BICAUSAL.**\n")]
    for rel, line in plants:
        root = copy_tree()
        try:
            with open(os.path.join(root, rel), "a", encoding="utf-8") as fh:
                fh.write("\n\n" + line)
            got = fails_of(root)
            assert "work rows: %s" % rel in got, (rel, got)
        finally:
            shutil.rmtree(root)


def test_altered_hypothesis_line_fails():
    root = copy_tree()
    try:
        with open(os.path.join(root, "process/PROCESS.md"), "a", encoding="utf-8") as fh:
            fh.write("\nThe law of adaptive organization (hypothesis): strongly selected systems maximize the cost of judgment.\n")
        got = fails_of(root)
        assert "hypothesis sentence altered or incomplete in process/PROCESS.md" in got, got
    finally:
        shutil.rmtree(root)


def test_hypothesis_label_without_colon_passes():
    root = copy_tree()
    try:
        before = set(cc.check(root))
        with open(os.path.join(root, "process/PROCESS.md"), "a", encoding="utf-8") as fh:
            fh.write('\nThe label is "The law of adaptive organization (hypothesis)" and nothing more.\n')
        added = [e for e in cc.check(root) if e not in before]
        assert added == [], added
    finally:
        shutil.rmtree(root)


def test_work_id_in_prose_or_history_passes():
    root = copy_tree()
    try:
        with open(os.path.join(root, "process/PROCESS.md"), "a", encoding="utf-8") as fh:
            fh.write("\n\nT40 waits on Chad (see README.md).\n\n<!-- history:begin -->\n| T40 | old row |\n<!-- history:end -->\n")
        assert "work rows" not in fails_of(root)
    finally:
        shutil.rmtree(root)


# ---------------------------------------------------------------- summaries
def test_whole_theory_summary_fails():
    # Acceptance: a whole-theory summary with no row cite fails.
    for s in ["Overall the theory is looking promising after this week.",
              "This result shows the theory works.",
              "GTAO is confirmed by the swarm data."]:
        assert cc.summary_fails(s, ROOT), s


def test_exact_status_cite_passes_and_wrong_status_fails():
    # Acceptance: an exact-status cite passes.
    assert cc.summary_fails("T61 is proved-in-model in its named classes, so the heat bound holds there.", ROOT) == []
    assert cc.summary_fails("T61 (PROVED (in-model)) holds for a passive plant.", ROOT) == []
    got = cc.summary_fails("T61 holds in general.", ROOT)
    assert got and "T61 is proved-in-model" in got[0]
    assert cc.summary_fails("The theory's reach grows with this result.", ROOT)
    assert cc.summary_fails("The theory's reach: T61 is proved-in-model in its classes.", ROOT) == []


def test_row_by_row_table_quotes_and_plain_mentions_pass():
    table = "| Row | Result | Rival |\n|---|---|---|\n| T61 | holds in class | Landauer-only |\n"
    assert cc.summary_fails(table, ROOT) == []
    assert cc.summary_fails("> the theory works\n", ROOT) == []
    assert cc.summary_fails("A reviewer wrote \"the theory works\" and we did not adopt it.", ROOT) == []
    assert cc.summary_fails("See T61 and T63 for the classes.", ROOT) == []
