# T80 memo: the ratio as a normal cone at a corner

*Tuesday 24 November 2026. Self-check, not an independent review. The lock is `PREREG.md` (sha256 `367adf39a76ef6adebe3881702a8a8f7997099280e10313b66d8f105dba3f69f`, commit `4786746`), before `corner_checks.py`. That file was not edited after the commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every number below is in-model.

## Why this approach

H-corner is Forge's hypothesis. The ratio \(q=\kappa_D/\kappa\) is the shadow price of the record constraint. On a smooth fine menu the observed angle should name a point. An interval should appear only at a binding cap, the flat equator, or a coarse menu. The T79 set would then be that cone. Chad's reading, secondary, weights the same cells three ways. Neither reading is an axiom. Both stay open to course-correction. There is no parent return and no time-symmetric rate table.

## Can it fail

Can it fail: yes. A smooth interior cell can keep a wide rationalizing set on the finest grid, or a corner's set can miss the normal cone.

Cheapest way: one interior angle on the 513-point grid whose rationalizing width stays above \(5\times 10^{-3}\).

## PROVED (in-model)

`G-form` passes. The closed form and `functionals` differ by at most \(5.551\times 10^{-17}\).

`G-cone` passes. At \(\phi=0\), \(s=1\), \(q_{\mathrm{eq}}=0.640000000000\) and \(q_{\mathrm{ptr}}=0.688377871168\).

`G-dyn` passes. All 17 quadratic starts land on the same action in every cell, and that action is the equator end: 782 landings, each recorded at \(q_{\mathrm{eq}}\). On this closed form the cost falls with \(\theta\), so the landings do not split. The starts are not mirrored.

## NUMERICAL

`corner_checks.out`, `FAILS 3`. P1, P2, and P3 pass. The three misses are the secondary weighting.

**P1, matches.** 22 smooth cells. The widest 513-grid set has width \(2.941\times 10^{-4}\), under the floor \(5\times 10^{-3}\). Widths fall from the 9-point grid to the 513-point grid by more than the locked factor 8. The T79 pin angle, \(\phi=0\), \(s=2\), \(\theta=1.075559\), has widths \(1.632\times 10^{-2}\), \(3.682\times 10^{-3}\), \(9.217\times 10^{-4}\), \(2.315\times 10^{-4}\). The midpoint is \(0.299858\). The review's continuous width \(1.65\times 10^{-4}\) on a 721-point grid is the same closing, on a finer menu.

**P2, matches.** No smooth cell is wide. All 23 corner cells have width at least \(0.01\). The flat interior tie is the point \(\{1\}\), width \(0\). The equator at \(\phi=0\), \(s=1\) is \([0,\ 0.640000]\), the equator-end formula \(1-r^2\), and it does not close under refinement. The coarse middle action stays an interval of width \(0.024149\).

**P3, matches.** The scored maximum is \(9.623\times 10^{-5}\), the coarse equator scan against its own crossing, under \(10^{-3}\). Smooth, pin, cap, fine equator, and pointer residuals are at most \(5.170\times 10^{-7}\). On smooth cells the midpoint sits on \(\lambda(u)\) at the installed angle. On corners the set fills the cone: \([0,\ q_{\mathrm{eq}}]\) at the equator, \([q_{\mathrm{ptr}},\ 2]\) at the pointer, \([0,\ 1]\) on the flat equator, \([1,\ 2]\) on the flat pointer.

**Model implication.** On this menu the rationalizing set is the multiplier where the action is an interior critical point, and it is the normal cone where the action is an endpoint, a flat equator, or a coarse menu. That is the one-dimensional envelope relation on a menu whose disturbance falls strictly with \(u\). A ratio inside a cone stays unidentified. Of 171 T79 pair rows, 102 are equator cones and 67 are pointer cones, 24 of those the full window \([0,\ 2]\) at stake 10. The other 2 are the pin. Its 513-grid midpoint is \(0.299858\), \(\lambda\) at that angle. The parent's root \(0.6\) is not this multiplier and was not an input.

## PUZZLE, P4

Three schemes. Equal weight has peaks in bins 8 and 10, masses \(0.148430\) and \(0.146252\), diffuse. The dynamics rule, which never reads \(R\), has peaks in bins 3, 8, and 10, masses \(0.108696\), \(0.217391\), and \(0.260870\), concentrated. Those bins sit on corner values: bin 3 on \(q_{\mathrm{eq}}(0,2)=0.28\), bin 8 on \(0.64\), bin 10 on the cluster near \(0.82\).

Robustness has no peak. Its heaviest bin is \(0.094724\), under the locked floor \(0.10\). The scheme histograms the probe coordinate times survival, and it does not read \(R\). Survival is \(9/9\) on 199 of 210 pair-probe cells. The minimum is \(2/9\), at \(\phi=\pi/6\), \(s=2\), probe \(0.5\). One cell is \(3/9\), at \(\phi=0\), \(s=2\), probe \(0.32\). With survival identically 1 the locked probes already put mass \(0.092857\) in the heaviest bin, under \(0.10\). The miss is in the probe list. The stored histogram is the scored one.

Equal weight is the scheme that weighs \(R\). Dynamics records \(q_{\mathrm{eq}}\). Robustness records the probes. `P4-agree` and `P4-corner` fail because those three histograms share no peak. The optional clause has no shared mode to sit on a corner. The thresholds were not moved after the histogram. A miss here is a puzzle about the weighting. H-corner and the distributional reading both stay open to course-correction.

## Errata

The family table enumerates 46 cells. The sentence that says 45 was not used to drop a row. See `DEVIATIONS.md`. The lock was not edited.

After the independent pass on PR #14 (0 blockers), three prose lines were corrected in place. The old survival floor was \(1/3\); the recomputed floor is \(2/9\). The old T79 sentence named only the equator cone; 67 of 171 pair rows are pointer cones. The old name for \(9.623\times 10^{-5}\) was an endpoint gap; that figure is the coarse equator scan. Scores, thresholds, and the lock are unchanged.
