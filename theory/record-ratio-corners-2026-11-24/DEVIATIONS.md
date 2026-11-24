# Deviations

## 2026-11-24

The family table in `PREREG.md` lists 18 smooth targets, 1 pin, 3 caps, 9 equator cells, 9 pointer cells, 1 flat equator, 1 flat pointer, 1 flat interior, and 3 coarse actions. That is 46 cells. The sentence after the table says 45, and the equal-weight scheme says the sum is over 45 cells. The run scores every row of the table. No listed family was dropped to hit 45. The preregistration was not edited. The histograms are normalized, so the extra cell is a weight, not a new threshold.

No other deviation in the scored run.

## 2026-11-24, after the independent pass on PR #14

The pass found 0 blockers. Three prose lines in `MEMO.md` were wrong and are corrected in place. The lock, the thresholds, `corner_checks.py`, and `corner_checks.out` are unchanged. The named checks stay `FAILS 3`.

The memo said robustness survival dips to 1/3 at one probe when s = 2. Recomputed on the locked 129-point grid, over the 10 pairs \((\phi, s)\) in the cell list and the 21 probes: survival is 9/9 on 199 of 210 cells. The minimum is 2/9, at \(\phi=\pi/6\), \(s=2\), probe 0.5. One cell is 3/9, at \(\phi=0\), \(s=2\), probe 0.32. The stored histogram is unchanged. With survival identically 1, the same probes put mass 0.092857 in bin 24, already under the floor 0.10. The `P4c` miss is in the locked probe list.

The memo said the wide T79 sets are the equator cone. Of 171 `PAIR` rows in `bicausal_checks.out`, 102 are equator cones (\([0, 0.64]\) 72, \([0, 0.82]\) 24, \([0, 0.28]\) 6) and 67 are pointer cones (\([0.70, 2]\) 26, \([0, 2]\) 24 at stake 10, \([0.38, 2]\) 9, \([0.86, 2]\) 8). The other 2 are the pin \([0.30, 0.30]\).

The memo called \(9.623\times 10^{-5}\) the largest endpoint gap. In `corner_checks.out` that figure is the coarse equator scan against its own crossing. The largest residual among the smooth, pin, cap, fine equator, and pointer rows is \(5.170\times 10^{-7}\).

`G-dyn` was reported as agreement of the 17 starts. The landing is the equator end on all 782 starts. The cost \(I+sL\) falls with \(\theta\) on every locked pair, so a split is unavailable on this closed form.
