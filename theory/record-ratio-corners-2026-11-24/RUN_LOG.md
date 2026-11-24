# T80 run log

The scored script is `corner_checks.py`. Stdout is `corner_checks.out`. Seed `20261124` is set and not drawn from. The script imports no random module. Grids, cones, tolerances, the 17 starts, and the 21 probes are the locked values.

`PREREG.md` was not edited after commit `4786746`. Its sha256 is `367adf39a76ef6adebe3881702a8a8f7997099280e10313b66d8f105dba3f69f`.

One deviation, also in `DEVIATIONS.md`: the family table enumerates 46 cells and the following sentence says 45. The run scores the table.

`HIST` lines and `NOTE reclass_count` are in the stdout so the three histograms and the reclass count sit next to the named checks. Reclass count is 0. They are not extra cells and not a changed threshold.

No parent return, no delay, and no binary-entropy channel is in the script. The number 0.6 is not a target. The starts are the locked quadratic list.

## Errata

The cell-count slip above.

After the independent pass on PR #14, `MEMO.md` was corrected in place. Survival bottoms at 2/9, not at 1/3. The wide T79 rows are 102 equator cones and 67 pointer cones. The scored gap \(9.623\times 10^{-5}\) is the coarse equator scan. Details are in `DEVIATIONS.md`. The script, the stored stdout, the thresholds, and the lock were not edited. The checks remain `FAILS 3`.
