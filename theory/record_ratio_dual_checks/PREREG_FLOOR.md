# T77 preregistration: a gravitational disturbance floor

*Tuesday 24 November 2026 (UTC). Written and committed before `floor_checks.py` and before any floor grid. Branch `forge-record-ratio-dual`. `THEORY.md` is not edited. Its blob at this lock is `6caadae569116a94a74563398be94cebf6e99e9b`. The shadow-price lock `PREREG.md` is not edited. Locked by sha256 in `PREREG_FLOOR.sha256`. A later change to the criteria below is a deviation, logged in `DEVIATIONS.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, or holography. A miss is a puzzle. The record price is a cost. Ratio \(0\) means \(\kappa_D=0\).

## 0. Question

**Model implication, not a derivation of gravity.** A record that has mass might broadcast part of its state through a channel that cannot be screened. That would put a floor \(P_D\ge\varepsilon(m)>0\) under every physical record, and it might be a reason \(\kappa_D\) cannot be \(0\).

The candidate source is Groszek, Woffinden, Harvey, White, and Davis, "Unblockable communication with gravity," *Science Advances* 12 (2026), doi `10.1126/sciadv.aee0802`. Crossref, 24 November 2026: type `journal-article`, those five authors, title as given, container *Science Advances*, volume 12, issue 47, issued 20 November 2026. The abstract reports a binary message encoded by moving a mass and read by a gravimeter through a brick wall, about \(0.7\) m, at about \(1\) bit per minute.

## 1. Where a floor is allowed to come from

The same four sources as `PREREG.md` §1, and no others: the ledger stock, Reeb–Wolf / Landauer, the ruin cap, and \(w_\ast\). A number chosen so that a multiplier comes out near \(1\) is not a floor. The experimental bit rate is not \(P_D\). T64's barrier-to-mass step is an assumed input in another note. It is not a map from a mass to a nat of this \(P_D\), and it is not used as \(\varepsilon(m)\).

## 2. Prior exposure

- On ANT, \(\gamma=0\), \(r=0.6\), \(P_D\) rises from \(0\) at \(\theta=0\) to \(P_\chi(0)\) at \(\theta=\pi/2\). The shadow price of an upper cap \(P_D\le D\) was scored in `PREREG.md`. At the ledger that price is \(0\).
- A lower constraint \(P_D\ge\varepsilon\) has a multiplier \(\mu\ge 0\) on \(\varepsilon-P_D\). Stationarity of \(I+w L+\mu(\varepsilon-P_D)\) identifies the coefficient of \(P_D\) in \(J\) with \(q=-\mu\le 0\).
- Hand reading, not this lock's grid: at \(w=10>w_\star\) the minimizer of \(I+w L\) is the pointer, where \(P_D=0\). A positive floor excludes it. The probe below is how the sign of \(q\) is read. It is not \(\varepsilon(m)\).

## 3. Model

\(\kappa=1\). ANT, \(\gamma=0\), \(\phi=0\), \(r=0.6\). `SEED = 20261124` is set and not drawn from. \(P_\chi(0)=\tfrac12\big[\ln 2-h((1+r)/2)\big]\).

The probe is \(\varepsilon=P_\chi(0)/2\) at stake \(w=10\). Let \(\theta_\varepsilon\) be the angle in \((0,\pi/2)\) with \(P_D(\theta_\varepsilon)=\varepsilon\), found by bisection to absolute error \(10^{-10}\). The probe coefficient is the central difference, step \(10^{-4}\),

\[
q_{\mathrm{probe}}=-\frac{\Delta(I+w L)}{\Delta P_D}
\]

at \(\theta_\varepsilon\).

## 4. Predictions

**H-eps.** None of the four sources is a function of a mass, and the bit rate in §0 is not a disturbance. The line is the token `NO-EPS` and contains no decimal numeral.

*Fails if* the line contains a decimal numeral. A printed floor would be a free parameter, or a conversion of the bit rate into \(P_D\). The absence is the result this line is allowed to record.

**H-sign.** \(q_{\mathrm{probe}}<0\) and \(|q_{\mathrm{probe}}-1|>0.5\).

*Fails if* \(q_{\mathrm{probe}}\ge 0\) or \(|q_{\mathrm{probe}}-1|\le 0.5\). Then a binding floor on this menu prices a nonnegative ratio, and the hope that the floor sets \(\kappa_D\) has a number at the probe. Report \(q_{\mathrm{probe}}\) and \(\theta_\varepsilon\). Do not replace the probe by a fitted \(\varepsilon(m)\).

**H-move.** The upper-budget shadow price at \(D=P_\chi(0)\), \(w=10\), remains \(0\) within \(10^{-6}\). The probe coefficient is not that price.

*Fails if* the upper-budget price satisfies \(|\lambda^\star|\ge 10^{-6}\), or \(|q_{\mathrm{probe}}-\lambda^\star|\le 0.05\). Then the floor has moved the ledger cap's multiplier. Report both numbers.

What counts as the finding, stated before the run: `NO-EPS`, together with a probe coefficient that is not \(1\), means the floor's size is not fixed by the four sources and the floor does not move \(\lambda^\star\) to \(1\). That outcome is a puzzle for the hope that an unscreenable channel forces \(\kappa_D>0\). It is not a reason to introduce a coupling by hand. A hand-chosen \(\varepsilon(m)\) would count as that same finding.

## 5. What this run will not say

It will not edit `THEORY.md` or `PREREG.md`. It will not say the ratio has been solved. It will not say the experiment derives a record price, and it will not say this note derives gravity. The \(1\) bit per minute is left as a bit rate.

## 6. Output

One line per check, `PASS` or `FAIL`, then `FAILS` and a count. Stdout is stored and byte-compared by the test.
