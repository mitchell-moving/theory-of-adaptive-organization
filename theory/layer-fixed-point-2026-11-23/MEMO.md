# MEMO: CT34 nesting fixed point

*24 November 2026. The claim is a **CONJECTURE**. `THEORY.md` is not edited. Nothing here is compared to a measured physical constant.*

## Why this approach

The conjecture, `MIRROR_MEMO.md` §6 on `ace-probe-memos-2026-11-23` at `e3e0e701` (not merged; the review leaves the row **CONJECTURE, untested**), is that a fixed point of CT34 nesting would be a dimensionless number in the sense of Feigenbaum's δ. The clock-term onsets 4 and 6 are scale-symmetry onsets, a different mechanism, and are contrast only.

CT34 (`THEORY.md` line 497) is partial minimization: the parent's problem is \(F(x)\) plus the team's optimized cost. The dyadic reading, declared as the period-doubling analogue and not as a theorem, adds the same scalar cost at the parent's time and at that time divided by \(b\). The scalar cost is CT22 (`THEORY.md` line 442): \(J=c/\tau+\alpha\tau\) with \(\alpha=w\sigma^2/2\). Currency and time are removed by the argmin and by dividing by the minimum, which is the operator in `PREREG.md` §1. Lemma A of that file says every \(At+B/t\) is sent to \(t+1/t\) in one step, so a number has to live off that family. Three Rayleigh quotients are the smallest set that can tell one rate from a menu. The unit and choice gate then refuses a candidate that moves when the units are stretched or when \(b\), the mode, the window, or the cap is swapped.

## What was learned

The preregistered outcome is **BROKEN**. The locked argmin is a golden section on \(\ln t\in[-8,8]\) at tolerance \(10^{-14}\) (`PREREG.md` line 71, `criteria.json` lines 17–18). On that procedure, \(\max|Tf_*-f_*|=1.66872758278\times 10^{-7}\) on the coarse window, which misses \(10^{-12}\) (`PREREG.md` line 83). BROKEN wins, and \(\rho\) is not interpreted (`PREREG.md` lines 91–93). Lesson for the log: before locking a bar, check that the locked method can reach it.

The candidate mean of the three slack quotients at \(b=2\) is 1.20021282055. At \(b=3\) it is 2.87924521541. The mean moves by 1.67903239486. The figure 4.022 is the \(\varphi_2\) gap, \(|\rho(\varphi_2,b=3)-\rho(\varphi_2,b=2)|=4.02167955053\), not the movement of the mean (`unit_choice_gate.py` line 91). The three deformations at \(b=2\) spread by 3.352. The other fit window moves the mean by 0.0042, and the two caps by \(4\times 10^{-6}\). Stretching cost and time together by 4 moves the mean by \(1.9\times 10^{-13}\). That unit-arm pass is the normalization identity \(TH=Th\) (`PREREG.md` line 40). It cannot fail on this operator. A failure there would be a bug. The cap arm is an identity of the same kind. With \(\hat y=F_{f_*}(t_c)+(q/2)V(t_c)\) (`PREREG.md` lines 57–58), \(\Theta(t_c)=q\), the critical point stays feasible, and the binding operator equals \(T\) (`PREREG.md` line 61). The two caps agreeing to \(4\times 10^{-6}\) is not evidence that a binding cap was tested. The raw minimizer and the raw minimum do scale, from \(t_0=1.41421356237\) to 0.353553390593 and from \(F_0=4.24264068712\) to 16.9705627485 (`unit_choice_gate.out` line 16). The gate code does not score them (`unit_choice_gate.py` lines 95–98).

**Result.** This dyadic analogue yields no number. That does not settle the CT34 conjecture (`THEORY.md` line 497). The miss is open.

**Logged deviation and model implication, not the locked cell.** Newton polish (`nest_map.py` lines 94–127) brings the same residual to \(1.78\times 10^{-15}\), and the scorer then returns MODE_DEPENDENT (`nest_map.out`). The exact multipliers of modes 3 and 5 at \(s=0\), \(b=2\), are \(3/2\) and \(11/4\). The printed quotients match the finite-\(s\) trapezoid of that factor to the printed digits. They are not a yield, and they are not interpreted under BROKEN. **Model implication:** on this analogue the rate depends on the mode order and on \(b\). Ace's working conjecture, that the cost may fix structural facts but not constants, is the reading frame (`PREREG_ADDENDUM.md` line 36). One analogue does not establish it.

**Lemma (hand, checked).** Linearize \(T\) at \(f_*=t+1/t\), where \(t_0=\sqrt{b}\) and \(F_0=2(b+1)/\sqrt{b}\). For \(\varphi_k(t)=t^k+t^{-k}\), \(F_\varphi(t_0 u)=2\cosh(k\ln b/2)\,\varphi_k(u)\). That value is even in \(\ln u\), so the argmin does not move at first order. Then \(DT(\varphi_k-f_*)=\lambda_k(\varphi_k-f_*)\), with

\[
\lambda_k=\frac{\cosh(k\ln b/2)}{\cosh(\ln b/2)}=b^{-(k-1)/2}\frac{b^k+1}{b+1},
\]

and \(DT f_*=0\) (Lemma A, `PREREG.md` line 43). At \(b=2\), \(\lambda_3=3/2\) and \(\lambda_5=11/4\). At \(b=3\), \(\lambda_3=7/3\) and \(\lambda_5=61/9\). For every real \(k>1\), \(\lambda_k>1\). It grows without a bound as \(k\) grows, and it depends on \(b\). This analogue has a continuum of expanding directions and no single relevant one. A \(\delta\)-type number needs exactly one. Checked by hand: the reduction of \(F_\varphi\), the closed form, and these four values. No new run. This is a model implication of the analogue, not the locked cell.

Prior odds, a judgment in `PREREG.md` §0 and not a result: about 1 in 10 of SUPPORT. SUPPORT is not reached. Under the locked order the cell is BROKEN, and for these deformations the closed form makes SUPPORT unreachable even after the residual is driven under \(10^{-12}\).

## Results

The table is the Newton-polish deviation stored in `nest_map.out` and `unit_choice_gate.out`. It is not the locked cell. The locked cell is BROKEN, above.

| Check | Value | Outcome |
|---|---|---|
| S1, \(\max\|Tf_*-f_*\|\) | \(1.78\times 10^{-15}\) | pass |
| S2, family residual | \(\le 2.7\times 10^{-15}\) | pass |
| Lemma B, \(F_0\) at \(b=2\) | 4.24264068712 \(= 3\sqrt{2}\) | pass |
| Cell | mode spread 3.35211337112 | MODE_DEPENDENT |
| \(\rho\), \(b=2\), \(\varphi_1,\varphi_2,\varphi_3\) | 1.45735693345, 2.74769744966, \(-0.604415921464\) | not one number |
| Same, \(s=10^{-5}\) | 1.45755367369, 2.74837748607, \(-0.604438662292\) | agrees inside 0.02 |
| Same, window \((3,96)\) | mean 1.20445021574 against 1.20021282055 | inside 0.02 |
| \(b=3\), same three | 2.26681080169, 6.76937700018, \(-0.398452155647\) | choice arm fails |
| Cap \(q=0.5\) and \(q=2\) | mean move \(4.4\times 10^{-6}\) | inside 0.02 |
| Unit stretch \((\mu,\gamma)=(4,4)\) | mean move \(1.9\times 10^{-13}\) | unit arm passes |
| Raw \(t_0\), \(F_0\) under that stretch | 0.353553390593, 16.9705627485 | gate fires |
| Gate | | FAIL_CHOICE, yielded none |

\(b=3\) is not part of the locked cell. It is part of the choice arm.

## Checkpoints

**1. Before any run** (`PREREG.md` §4, not rewritten). Still the right question: yes, an eigenvalue, not an EOQ share. Not built in: normalization is currency and time, \(b=3\) cannot flip the cell, a window-moving \(\rho\) is CUTOFF. Cheaper test: Lemma A is S2; three quotients are the minimum that separate one number from mode-dependent rates.

**2. After run 1, before the unit arm.** Still the right question: yes. The cell says the three rates disagree, and the open point is whether any one of them is forced by the cost rather than by a choice. Not built in: \(b=2\) was put in as the doubling analogue, so a rate that exists only at \(b=2\) is not a yield. Cheaper: the \(b\) and mode comparisons were already printed; the new work is the unit stretch.

**3. At the end.** Still the right question: the conjecture asked for one number, and on this operator the gate says there is none. Not built in: the gate was committed before the unit arm, and no quotient was picked after the fact. Cheaper: another operator, built so that \(b\) or the mode cancels, would be a search for a number the gate would reject unless the cancellation were forced. That search is not the next cheap step.

## Deviations

- Run 1 was executed before `PREREG_ADDENDUM.md` and before `PREREG_ADDENDUM_2.md`. The locked predictions were not edited. The choice arm reads the run 1 record. The unit arm ran after addendum 2 was committed (`8977f8f`).
- Comparing function values cannot place this minimum to the locked \(10^{-12}\): the curvature is below double precision. The stored scripts finish the argmin by Newton on a complex-step derivative (`nest_map.py` lines 94–127). That polish is not the locked procedure. Under the locked golden section the cell is BROKEN. The Newton cell MODE_DEPENDENT is this deviation.
- A golden section that crosses the feasible boundary can leave the feasible set. The binding polish is restricted to the feasible run the scan found. That is the argmin the operator names.
- `mean` had to take a list. The scorer returned early while S1 was failing, so the bug showed up only after the argmin was accurate enough for S1 to pass.

## Files

`PREREG.md`, `PREREG_ADDENDUM.md`, `PREREG_ADDENDUM_2.md`, `criteria.json`, `crossref.out`, `nest_map.py`, `nest_map.out`, `unit_choice_gate.py`, `unit_choice_gate.out`, `RUN_LOG.md`. The review is `theory/reviews/LAYER_FIXED_POINT_REVIEW_2026-11-24.md` (`8631e48`).

## ERRATA

Checked against `theory/reviews/LAYER_FIXED_POINT_REVIEW_2026-11-24.md`. `PREREG.md`, both addenda, `criteria.json`, and the stored outputs are unchanged. Each item was recomputed or reread. Accept means the review's claim holds.

**1. Accept.** The locked procedure is a golden section on \(\ln t\in[-8,8]\) at tolerance \(10^{-14}\) (`PREREG.md` line 71, `criteria.json` lines 17–18). S1 requires \(\max|Tf_*-f_*|<10^{-12}\) (`PREREG.md` line 83). BROKEN wins if S1 fails, and \(\rho\) is not interpreted (`PREREG.md` lines 91–93). Calling that golden section, and nothing else, on \(f_*\) at \(b=2\) gives \(\max|Tf_*-f_*|=1.66872758278\times 10^{-7}\). Scan plus golden section, still without Newton, gives \(5.03183716916\times 10^{-9}\). Both miss \(10^{-12}\). The preregistered outcome is **BROKEN**.

The stored cell MODE_DEPENDENT uses `newton_polish` (`nest_map.py` lines 94–127), which is not in the preregistration. It is a logged deviation and a model implication. With that polish the residual is \(1.776\times 10^{-15}\) and the scorer returns MODE_DEPENDENT (`nest_map.py` lines 254–269, `nest_map.out`). The scripts and both outputs first enter git together at `2be9290`.

The exact multipliers are real. For \(\varphi(t)=t^k+t^{-k}\) at \(s=0\) and \(b=2\), the factor is \(\cosh(k\ln 2/2)/\cosh(\ln 2/2)\), which is \(3/2\) for mode 3 and \(11/4\) for mode 5. At \(s=10^{-4}\) the trapezoid formula \([\cosh(k L/2)/D]\,(1-\langle t+1/t,\varphi\rangle/\langle\varphi,\varphi\rangle)\), with \(L=\ln b\) and \(D=\cosh(L/2)+s\cosh(k L/2)\), reproduces the printed Newton quotients to every printed digit: 1.45735693345 and 2.74769744966 at \(b=2\), and 2.26681080169 and 6.76937700018 at \(b=3\). Those quotients are not interpreted under BROKEN.

**2. Accept.** `da9c817` (2026-11-24 04:33:58 +0000) locks `PREREG.md` and `criteria.json` before any result script. Run 1 had already been executed when `43ad8c6` added `PREREG_ADDENDUM.md` (line 5 of that file). The choice arm was locked in `8977f8f` (`PREREG_ADDENDUM_2.md` line 5) as a read of that record. `nest_map.out` lines 12–31 already show the \(b=2\)/\(b=3\) quotients and the three deformations, and those already differ by more than `stable_tol` 0.02. The choice half was not prospective. The unit-arm sentence is in the same commit. Git does not order the unit computation separately: both scripts and both outputs first appear in `2be9290`. The review could not check that the unit arm was unrun at `8977f8f`. This note does not claim that separate order.

**3. Accept.** 4.022 is not the movement of the candidate mean. The means are 1.20021282055 and 2.87924521541 (`PREREG_ADDENDUM_2.md` line 11). The difference is 1.67903239486. The figure 4.02167955053, rounded to 4.022 in the earlier memo and in the earlier OPEN_WORK row, is \(|\rho(\varphi_2,b=3)-\rho(\varphi_2,b=2)|\). `unit_choice_gate.py` line 91 sets `b_move` to the max of the mean move and the per-mode moves. The choice arm still fails on the mean alone, since \(1.679>0.02\). The printed gate remains `FAIL_CHOICE` (`unit_choice_gate.py` lines 99–107, `unit_choice_gate.out` lines 17–18).

The unit-arm pass is a normalization identity. For \(H(\tilde t)=\mu\, h(\gamma\tilde t)\), \(F_H=\mu F_h(\gamma\,\cdot)\), so \(t_0\) scales by \(1/\gamma\), \(F_0\) by \(\mu\), and \(TH=Th\) (`PREREG.md` line 40). Any Rayleigh quotient of \(TH\) equals that of \(Th\), up to rounding. The pass cannot fail on this operator, and it adds no evidence beyond that normalization. A failure would have been a bug. The raw pair does scale (`unit_choice_gate.out` line 16). The cap arm is an identity of the same kind: \(\Theta(t_c)=q\) by `PREREG.md` lines 57–58, so the binding operator equals \(T\) (`PREREG.md` line 61). The \(4\times 10^{-6}\) cap move is not evidence.

**4. Accept.** The tested map is the dyadic analogue, declared not a theorem of CT34 (`PREREG.md` lines 31–41). CT34 is partial minimization, \(\min_{x,y}[F(x)+G(y;\theta(x))]=\min_x[F(x)+J^*_T(\theta(x))]\) (`THEORY.md` line 497). The scalar cost is the next paragraph of the CT22 proof (`THEORY.md` line 442). CORE does not set a nesting integer. The \(b\) at `CORE.md` line 58 is a control coefficient. Ruin outside the sum is `CORE.md` lines 27 and 66. Theorem R1 is `CORE.md` line 52.

The conclusion is narrowed. This dyadic analogue yields no number. That does not settle the CT34 conjecture. Lemma A (`PREREG.md` line 43) gives the multiplier 0 on \(At+B/t\) for every \(b>0\). SUPPORT requires \(|\rho|\ge 1.05\) (`PREREG.md` line 85, `criteria.json` line 13), so that 0 is outside SUPPORT on purpose. The miss is open.

**5. Accept.** `nest_map.py` lines 254–281 can return SUPPORT and the six failure cells. That rule faces both ways. For these deformations it does not: modes 3 and 5 already differ by 1.29034051621, so the spread exceeds 0.02 without \(\varphi_3\), and under the locked golden section S1 fails first. SUPPORT cannot be reached for these deformations. That is a property of the deformations, not a scorer that was edited. The cells and `criteria.json` were not edited after `da9c817`.

`unit_choice_gate.py` lines 99–106 name PASS, FAIL_UNITS, FAIL_CHOICE, and FAIL_UNITS_AND_CHOICE. On this operator the unit arm cannot fail, by the identity in item 3, and the choice arm cannot pass, by the closed form. `raw_moves` is printed and is not an input to `unit_fail` (`unit_choice_gate.py` lines 95–98). `PREREG_ADDENDUM_2.md` lines 34–36 say that quoting \(t_0\) or \(F_0\) is the input on which the gate fires. The code does not score that input.

**6. Accept.** The SUPPORT falsifier was written after run 1. That timing is disclosed (`PREREG_ADDENDUM.md` lines 5 and 16). The S1 prefactor-1 input, the Lemma A input \((t+1/t)+(t^3+t^{-3})\), and Lemma B at \(b=3\) and \(b=1\) (`PREREG_ADDENDUM.md` lines 13–15) follow from the locked lemmas and do not use the printed quotients. The SUPPORT row names mode order 5 in place of mode order 3, which is the locked comparison itself, written after the result. SUPPORT cannot be reached for these deformations, as item 5 says.

**7. Accept.** `PREREG_ADDENDUM.md` line 20 says that Feigenbaum, Coullet, Lanford, and period-doubling appear only in `PREREG.md`. At `43ad8c6` those strings also appear in that sentence and in `criteria.json` line 20 ("Feigenbaum-sized"). Nothing in that grep sits outside `theory/layer-fixed-point-2026-11-23/`.

The three section pointers are real, and they are not those grep hits. `theory/MATH_COMPLETENESS_AUDIT.md` lines 313–317, §(iii), say a universal layered fixed point is likely false, and that the dimensionless groups in `THEORY.md` B.9 do not produce layers. `theory/MATH_ATTACK.md` line 237, §3.1, is the probabilistic renormalization group for shocks, and line 302, §3.6, says there is no deep RG and no anomalous exponents. `reviews/night1/CORE_AUDIT.md` line 165, §2.5(e), is \(\Pi^\star=\gamma^{-1/(1-\gamma)}\) (4 at \(\gamma=1/2\)). The exponent there is \(\gamma\), not \(H\), and the line does not say "eigenvalue of a nesting map."

The mirror row, upstream `e3e0e701`, `MIRROR_MEMO.md` lines 113 and 147, is "Nested-layer fixed point gives a universal GTAO number | CONJECTURE, untested" and "no route to \(\alpha\) was found." `MIRROR_REVIEW.md` passes the no-route claim. Ace's working conjecture is stated and labeled not a result (`PREREG_ADDENDUM.md` line 36).
