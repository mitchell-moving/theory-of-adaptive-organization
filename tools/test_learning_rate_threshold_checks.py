"""Runs theory/learning_rate_threshold_checks/learning_rate_threshold_checks.py (T67)."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "learning_rate_threshold_checks")


def test_learning_rate_threshold_checks_all_pass():
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "learning_rate_threshold_checks.py")],
        capture_output=True, text=True, timeout=600,
        env={**os.environ, "OMP_NUM_THREADS": "2", "OPENBLAS_NUM_THREADS": "2"},
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL T67 CHECKS PASS" in r.stdout
    assert "FAILS 0" in r.stdout
    with open(os.path.join(HERE, "learning_rate_threshold_checks.out"), encoding="utf-8") as f:
        expected = f.read()
    assert r.stdout == expected


def test_prereg_lock_unchanged():
    import hashlib
    h = hashlib.sha256(open(os.path.join(HERE, "PREREG_T67.md"), "rb").read()).hexdigest()
    assert h == "b91e2101ec93acf3c22cf8b93241014012938b0db2fccc7df62ea27748d54b98"
