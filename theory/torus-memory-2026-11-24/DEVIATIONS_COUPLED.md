# Deviations, coupled loop

`PREREG_COUPLED.md` was not edited. The classifier, the grid, and the predictions were not changed.

2026-11-24, after the locking commit `0352de5`. The return \(Q_s(\rho)\) is defined on \([1,9]\). The step has no clamp, and gain \(\alpha=1.5\) can send \(\rho\) outside that interval during the transient. Those calls, 950 of them (272 below 1, 678 above 9), use the endpoint value \(Q_s(1)\) or \(Q_s(9)\). The tail of every orbit is inside the interval. The twelve gains and initial conditions on each cell and start rule share one terminal (`coupled_loop_checks.out:31`), including the gains \(\alpha\le 1\) that never leave \([1,9]\). The endpoint hold does not choose the locked number.
