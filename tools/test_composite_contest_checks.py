"""Byte-for-byte rerun of the composite-contest scoring (OPEN_WORK T72)."""
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "theory", "composite_contest_checks")
LOCKED = ("lemmas.out", "envelope.txt", "decisions.out", "control.out", "crossref.out")


def _sums(path):
    out = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            digest, name = line.split(None, 1)
            out[name] = digest
    return out


def test_composite_contest_matches_locked_outputs():
    locked = _sums(os.path.join(HERE, "SHA256SUMS"))
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"
    env["OMP_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "run_all.py")],
        cwd=HERE,
        capture_output=True,
        text=True,
        timeout=180,
        env=env,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ALL LEMMAS PASS" in r.stdout
    assert "H1 PASS" in r.stdout
    # Stored bytes. The errata corrects this orthogonal-menu P1 to LOSE
    # (theory/COMPOSITE_CONTEST_2026-11-24.md:15). This assertion is not changed.
    assert "P1 PASS" in r.stdout
    for name in LOCKED:
        digest = hashlib.sha256(open(os.path.join(HERE, name), "rb").read()).hexdigest()
        assert digest == locked[name], name
