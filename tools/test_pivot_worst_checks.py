"""Byte-for-byte rerun of the worst-question pivot (OPEN_WORK T72)."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "pivot_worst_checks")


def test_pivot_matches_locked_output():
    sums = {}
    with open(os.path.join(HERE, "SHA256SUMS"), encoding="utf-8") as fh:
        for line in fh:
            digest, name = line.split()
            sums[name] = digest
    env = dict(os.environ)
    env["OMP_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "run_pivot.py")],
        cwd=HERE, capture_output=True, text=True, timeout=120, env=env,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Q1 PASS" in r.stdout
    assert "headline MIXED" in r.stdout
    path = os.path.join(HERE, "decisions.out")
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    assert digest == sums["decisions.out"]
