"""Runs theory/pointer_basis_stakes_checks/pointer_basis_stakes_checks.py (T73)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "pointer_basis_stakes_checks")


def test_pointer_basis_stakes_checks_all_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "pointer_basis_stakes_checks.py")],
        capture_output=True, text=True, timeout=120,
        env={**os.environ, "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2"},
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T73 CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    assert "HEADLINE PRICING_ARTIFACT" in r.stdout
    with open(os.path.join(HERE, "pointer_basis_stakes_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected
