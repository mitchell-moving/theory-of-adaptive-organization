"""Runs theory/dephasing_crossover_checks/dephasing_crossover_checks.py (OPEN_WORK T84)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "dephasing_crossover_checks")


def test_dephasing_crossover_checks_all_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "dephasing_crossover_checks.py")],
        capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T84 CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    assert "HEADLINE CLUE_SPLIT" in r.stdout
    with open(os.path.join(HERE, "dephasing_crossover_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
