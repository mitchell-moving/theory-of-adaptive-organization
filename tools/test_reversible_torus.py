"""Runs theory/torus_memory_checks/reversible_torus_checks.py (T82b)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "torus_memory_checks")


def test_reversible_torus_scoreboard_matches():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "reversible_torus_checks.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "SCOREBOARD COMPLETE" in r.stdout
    assert "I-rev PASS" in r.stdout
    assert "BEYOND PASS NOT_BEYOND" in r.stdout
    assert "SCORED_FAIL P2 P3 P4 P4-tongue P-kc" in r.stdout
    with open(os.path.join(HERE, "reversible_torus_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
