# T79 run log

No deviation from `PREREG.md` or `PREREG_3.md`.

The scored script is `bicausal_checks.py`. Stdout is `bicausal_checks.out`. Seed `20261124` is set and not drawn from. Grids, tie rules, tolerances, the three iteration starts, the three path starts, \(\varepsilon_0=10^{-6}\), \(dt=0.05\), and \(n=20\) are the locked values.

Cycles are printed on `CYCLE` lines. Each Nash pair's rationalizing set is printed on a `PAIR` line. On a `CELL` line, when more than one Nash \(\alpha\) exists, `qhat` is the midpoint for the smallest \(\alpha\). The `PAIR` lines are the record for the other angles.

`PREREG.md` and `PREREG_3.md` were not edited after their commits. There is no `PREREG_2.md`: the timescale ratio was locked inside `PREREG.md` before that file was committed, and the reversibility reading is the separate third lock.

Crossref, 24 November 2026, HTTP 200, before the third lock: `10.1103/PhysRevLett.78.2690`, `10.1103/PhysRevE.60.2721`, `10.1088/0034-4885/75/12/126001`. No number was taken from those records.

## After the independent review

No change to either lock, to the script, or to `bicausal_checks.out`.

The path KL in the stdout is the displayed equation in `PREREG_3.md`, \(H(p_n)-H(p_0)\). The sentence above that equation puts the start density on both ends. Both readings were in the lock at `9c004d7`. The memo's errata names which one was scored.

The printed `P4` count `119` includes twelve repeated \((1,1,1)\) scale rows. The unique unpinned count is 107 of 108. The miss is the same.

The script does not add a separate comparison of \(q_{\mathrm{hat}}\) across the two tie rules. On this grid the only pin's other rule is unpinned, so the fail count does not depend on that comparison.

## Errata

See `MEMO.md`. The locks stay as committed.
