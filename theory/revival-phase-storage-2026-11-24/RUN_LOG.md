# T83 run log

Append only. A line in this file is not rewritten.

- Preregistration locked in this commit, before any scored script and before any stored output. The sha256 of `PREREG.md` is the first line of `PREREG.sha256`. No script has been run.
- Preregistration commit `f97d11fa2154a846c56bc5a002ff553e90f933a3`. `PREREG.md` was not edited after that commit. sha256 `0397c70ea558bdbd58e6a4657213c12aee7582d6deea3a555c862f5e4cdc0144`.
- Scored script `theory/revival_phase_checks/revival_phase_checks.py`. Stdout is `theory/revival_phase_checks/revival_phase_checks.out`. The script imports no random module. Two consecutive runs matched byte for byte. `FAILS 6`, all six `B-shape` rows with denominator 7. The bars were not edited. The diagnosis is `DEVIATIONS.md`.
- After that output was stored, `python3 tools/check_consistency.py` and `python3 tools/check_open_work.py` passed. `python3 -m pytest -q --ignore=reviews/night2/CAUSAL_NULL_INVARIANCE` was 291 passed and 1 skipped. numba is not installed, so that path was ignored. The skip is the Lean test.
- Review on the draft. The preregistration and the stored output were not edited. Appended `DEVIATIONS.md` items 3–5: even separations of the printed off-diagonal are 0 and the integral is not; four bars are identities and are not evidence; three glosses in the lock name the wrong theorem, add a destruction clause the Crossref record does not carry, and say irrational times where the same bullet already says almost every time. The six fails stay fails.
