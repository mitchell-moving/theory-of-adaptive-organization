# PREREG ADDENDUM 2: unit and choice gate

*24 November 2026. `PREREG.md` and `PREREG_ADDENDUM.md` are committed and are not edited. This addendum locks the check Ace required before the unit arm is run.*

**Deviation.** Run 1 was executed before this gate existed. Its printed quotients already compare \(b=2\) with \(b=3\), the three deformations, the two windows, and the two caps. The choice arm below only reads that record. The unit arm, \((\mu,\gamma)=(4,4)\) against \((1,1)\), has not been run. No results-producing run starts until this file is committed.

## The rule

Any number a fixed point of this operator yields has to be dimensionless, and it must not be put in by hand. It is not a yield if its value depends on a chosen scale, unit, or tuned parameter.

The candidate \(N\) is the mean of the three slack Rayleigh quotients at \(b=2\), coarse window, \(s=10^{-4}\): the single number a SUPPORT cell would have quoted. Tolerance is `stable_tol` in `criteria.json`. The same tolerance is applied to each deformation separately.

## The check

**Unit arm.** Let \(h\) be \(f_*+s\varphi\). In a coordinate whose time unit is stretched by \(\gamma\) and whose cost unit is stretched by \(\mu\),

\[
H(\tilde t)=\mu\, h(\gamma\tilde t).
\]

Locked pair: \((\mu,\gamma)=(1,1)\) against \((4,4)\). Recompute the candidate from \(H\) with the same operator. The arm **fails** if the candidate moves by more than `stable_tol`.

**Choice arm.** The arm **fails** if the candidate moves by more than `stable_tol` when any one of these arbitrary choices is swapped, the others held fixed:

- nesting ratio \(b=2\) swapped for \(b=3\)
- the deformation set, measured by the spread of the three locked quotients
- fit window \((Z,N)=(2,64)\) swapped for \((3,96)\)
- cap strength \(q=0.5\) swapped for \(q=2\)

\(b\), the mode order, the window, and \(q\) are choices. They are not fixed by the cost.

**Gate.** A number is yielded only if both arms pass. Otherwise the yield is none.

## An input on which the check fails

The raw minimizer \(t_0\) and the raw minimum \(F_0\) are not dimensionless. Under \((\mu,\gamma)=(4,4)\) they scale as \(1/\gamma\) and as \(\mu\). If either were quoted as the fixed-point number, the unit arm would fail. That is the input that shows the gate can fire. A quotient that has been stripped of currency and time can pass the unit arm and still fail the choice arm.

## What is not claimed

Passing the unit arm does not make a mode-dependent or \(b\)-dependent quotient into a constant. Ace's working conjecture, in `PREREG_ADDENDUM.md` §4, still stands as the reading frame: structural dependence is not a constant. No quantum-record price is used (`PREREG_ADDENDUM.md` §3).
