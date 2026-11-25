"""Reruns the CT34 nesting fixed-point scripts and checks the locked cell and the gate."""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "layer-fixed-point-2026-11-23")


def _run(script):
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, script)],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    with open(os.path.join(HERE, script.replace(".py", ".out")), encoding="utf-8") as fh:
        expected = fh.read()
    assert r.stdout == expected
    return r.stdout


def test_nest_map_cell_and_stdout():
    out = _run("nest_map.py")
    assert "cell MODE_DEPENDENT" in out
    assert "ALL LAYER-FP CHECKS DONE" in out
    with open(os.path.join(HERE, "nest_map.json"), encoding="utf-8") as fh:
        rec = json.load(fh)
    assert rec["cell"] == "MODE_DEPENDENT"
    assert rec["S1"] is True and rec["S2"] is True
    rhos = [rec["slack_primary_window"][k] for k in ("1", "2", "3")]
    assert max(rhos) - min(rhos) > rec["criteria_echo"]["stable_tol"]


def test_unit_choice_gate_yields_none():
    _run("nest_map.py")
    out = _run("unit_choice_gate.py")
    assert "gate FAIL_CHOICE" in out
    assert "yielded none" in out
    assert "unit_arm PASS" in out
    assert "raw_changes true" in out
    assert "ALL UNIT-CHOICE CHECKS DONE" in out
