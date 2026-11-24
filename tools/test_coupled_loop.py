"""Runs theory/torus_memory_checks/coupled_loop_checks.py (T82 coupled loop)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "torus_memory_checks")


def test_coupled_loop_scoreboard_matches():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "coupled_loop_checks.py")],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "SCOREBOARD COMPLETE" in r.stdout
    assert "H-settle PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    with open(os.path.join(HERE, "coupled_loop_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
