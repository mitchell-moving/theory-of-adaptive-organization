"""Runs theory/torus_memory_checks/t82e_checks.py (T82e)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "torus_memory_checks")


def test_t82e_scoreboard_matches():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "t82e_checks.py")],
        capture_output=True, text=True, timeout=180,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "SCOREBOARD COMPLETE" in r.stdout
    assert "SCORED_FAIL P-width P-scale P-record P-refine" in r.stdout
    with open(os.path.join(HERE, "t82e_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
