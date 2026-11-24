# ADDENDUM PREREG: is T84's holding floor the T68 clock term?

*Tuesday 24 November 2026 (UTC). Own file. The parent `PREREG.md` is not edited. Commit this file before any script that scores the prediction below. Branch `forge-dephasing-refresh`. `THEORY.md` and `CORE.md` are not edited. A later change to a prediction or a bar is a deviation, appended in `DEVIATIONS.md`. Open-work id **T84b**. Self-check, not an independent review. Results of this addendum are labeled observed in-model until an independent review clears them.*

Can it fail: the noiseless holding cost can sit within 3 nats of \(4\kappa/\lambda\), the clock heat at zero rate can equal that holding cost, or the frozen ongoing heat can clear the same gap bar, in which case the comparison cannot tell the forms apart and the label is a consistency check.

Cheapest way to fail it: evaluate the locked T84 cost at zero dephasing, the clock term at zero rate, the onset \(4\kappa/\lambda\), and the frozen ongoing heat. No bath Hilbert space and no Monte Carlo.

## Why this approach

`theory/CLOCK_TERM_2026-11-23.md:125` is an onset for class CK: a clock first pays when a look carries more than \(4\kappa/\lambda\) nats. T84's noiseless holding cost is a different expression, \(\kappa\ln 2\), named as the cost of the noiseless box (`theory/dephasing-crossover-2026-11-24/PREREG.md:134`). Comparing the two forms on shared inputs answers whether that floor is the clock term again. An alternative form that fails the same numeric bar is scored beside it, so a pass is not only two different formulas agreeing with themselves.

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. The record price is a cost.

## A. The prediction

**Stock floor.** T84 design H at zero dephasing (`theory/dephasing-crossover-2026-11-24/PREREG.md:131-134`, `:148`):

\[
F_{\mathrm{hold}}(\kappa)=J_H(\gamma\tau=0,w)=\kappa\ln 2.
\]

It does not depend on \(w\), \(\gamma\), \(\tau\), a clock rate \(\omega'\), a diffusion \(D\), or \(\lambda\).

**Clock term.** Class CK (`theory/CLOCK_TERM_2026-11-23.md:19-21`):

\[
C(\kappa,kT,\omega',D)=\kappa kT\,\frac{\omega'^2}{D}\quad(D>0),\qquad C=0\text{ at }\omega'=0.
\]

**Onset, line 125.** \(I_*=4\kappa/\lambda\) nats (`theory/CLOCK_TERM_2026-11-23.md:125`). At \(\kappa=\lambda=1\) this is 4.

**Predicted relation.** \(F_{\mathrm{hold}}\) is not \(C\) and it is not \(\kappa I_*\). Locked bars at \(\kappa=\lambda=kT=1\), for each \(w\in\{0,1,2\}\), with \(F=J_H(0,w)/\kappa\) computed from \(\chi(1)=\ln 2-h(1)\):

- B1. \(|F-\ln 2|\le 10^{-12}\).
- B2. \(|F-4|\ge 3\).
- B3. \(|F-C(\omega'=0)|\ge 0.5\).

\(C\) at \((\omega',D)=(1,1)\) equals 1 and at \((1,2)\) equals \(1/2\). \(F\) has no \(D\) argument, so those two clock values cannot both equal \(F\).

## B. Circularity guard

**Alt-onset.** Read the floor as the line-125 onset, \(F_{\mathrm{on}}=4\kappa/\lambda\). Bar B2 applied to \(F_{\mathrm{on}}/\kappa\) fails, because the gap is 0.

**Alt-frozen.** Read the floor as the ongoing heat after a one-time write, which is 0 (`CORE.md:78`; T84's frozen reading at `theory/dephasing-crossover-2026-11-24/PREREG.md:136`). Bar B3 applied to that 0 fails, because \(C(\omega'=0)=0\).

The script must show both alternatives failing the bar that the stock floor passes. Headline `OBSERVED_NOT_CLOCK` only if B1–B3 hold for the stock floor and both alternatives fail. If either alternative clears the bar it was meant to fail, the headline is `CONSISTENCY_CHECK`: the bar did not separate the forms. Any other miss is `PUZZLE`. The script computes the label from those booleans and does not print `OBSERVED_NOT_CLOCK` after a miss. The label is observed in-model either way.

## C. Standing locks, not refit

These were locked in `PREREG.md` at commit `612b82e`, before `dephasing_refresh_checks.py` existed. This addendum does not move them and does not replace their bars with script output.

**Stake exponent.** Short-period elasticity tends to \(1/2\), not to T68's \(1/3\) (`theory/CLOCK_TERM_2026-11-23.md:53-55`). The parent bars stand: \(e(0.01)<0.505\), \(e(0.5)<0.55\), \(e(1)>0.55\) (`PREREG.md` R4). The candidate band \(0.50\pm 0.05\) is the short-period side. It is not a uniform exponent.

**Threshold scaling.** With \(\Theta=\gamma T_{\mathrm{hold}}\) and \(A=\lambda kT\,I_0\),

\[
\frac{w_c}{\gamma A}=\frac{2}{1-(1+\Theta)e^{-\Theta}}.
\]

As \(\Theta\to 0\), \(w_c\sim 4A/(\gamma T_{\mathrm{hold}}^2)\): inverse in \(\gamma\), inverse square in \(T_{\mathrm{hold}}\). The parent series is \(\Pi_c=4+(8/3)\Theta+(7/9)\Theta^2+O(\Theta^3)\) (`PREREG.md` R2). \(\Pi_c\to 4\), not 16.
