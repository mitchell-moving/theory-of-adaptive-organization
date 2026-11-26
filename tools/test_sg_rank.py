#!/usr/bin/env python3
"""Tests for tests/SG_RANK/sg_rank.py (run: python3 -m pytest -q tools/test_sg_rank.py)."""
import importlib.util, json, os, sys, textwrap

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SG_PATH = os.path.join(ROOT, "tests", "SG_RANK", "sg_rank.py")


def load_sg():
    spec = importlib.util.spec_from_file_location("sg_rank", SG_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_ledger(path, rows):
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row) + "\n")


def ranked(item="A", index=1.0, unaided=1, uniform_pos=0, p=0.5, n=2):
    # first-seen tuple uses: index, n+1-unaided_rank, n-uniform_perm.index, P!=0.5
    order = ["A", "B"]
    return {
        "entry": 7,
        "kind": "rule_rank",
        "protocol": 2,
        "order": order,
        "index": {"A": 1.0, "B": 0.4},
        "unaided_rank": {"A": 1, "B": 2},
        "uniform_perm": ["A", "B"],
        "P": {"A": 0.5, "B": 0.5},
    }


def test_score_accepts_claim_map_status_changed_alias(tmp_path, capsys, monkeypatch):
    sg = load_sg()
    led = tmp_path / "LEDGER.jsonl"
    write_ledger(led, [
        {"entry": 6, "kind": "protocol"},
        ranked(),
        {"entry": 8, "kind": "outcome", "item": "A", "claim_map_status_changed": True},
        {"entry": 9, "kind": "outcome", "item": "B", "status_changed": False},
    ])
    monkeypatch.setattr(sg, "LEDGER", str(led))
    # fewer than 15 outcomes: no verdict, but must not crash
    sg.cmd_score()
    out = capsys.readouterr().out
    assert "claim_map_status_changed (accepted): 8" in out
    assert "with outcomes: 2" in out
    assert "fewer than 15 outcomes: no verdict" in out


def test_score_skips_outcome_missing_both_fields(tmp_path, capsys, monkeypatch):
    sg = load_sg()
    led = tmp_path / "LEDGER.jsonl"
    write_ledger(led, [
        {"entry": 6, "kind": "protocol"},
        ranked(),
        {"entry": 8, "kind": "outcome", "item": "A"},
        {"entry": 9, "kind": "outcome", "item": "B", "status_changed": True},
    ])
    monkeypatch.setattr(sg, "LEDGER", str(led))
    sg.cmd_score()
    out = capsys.readouterr().out
    assert "missing status_changed and claim_map_status_changed (skipped): 8" in out
    assert "with outcomes: 1" in out


def test_real_ledger_no_longer_crashes_on_entry_156(capsys):
    """The 20 Nov crash: entry 156 has claim_map_status_changed, not status_changed.

    This is a read-only smoke test of the crash, not the official Q0 / SG-SCORE
    score. It does not assert an AUC, write the ledger, or add a rule_change.
    """
    sg = load_sg()
    # Use the repository ledger (read-only).
    sg.cmd_score()
    out = capsys.readouterr().out
    assert "KeyError" not in out
    assert "with outcomes:" in out
    # The known alias entry is accepted, not skipped.
    assert "claim_map_status_changed (accepted): 156" in out
    assert "fewer than 15 outcomes: no verdict" not in out
