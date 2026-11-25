# T73: a stake on a dephased qubit, and the record basis

*Tuesday 24 November 2026. Self-check, not an independent review. Preregistered in `PREREG.md` (commit `6418237`, 2026-11-24 05:19:13 +0000) before this derivation. Run gate `RUN_LOG.md` (commit `bfd88ab`). Review: `theory/reviews/POINTER_BASIS_STAKES_REVIEW_2026-11-24.md` (commit `992920b`). `THEORY.md` is unchanged. The qubit and the dephasing channel are inputs. Nothing here derives general relativity, quantum mechanics, or holography.*

*The printed headline is fixed by the closed forms in `PREREG.md:72`. It is not a test result. The corrections are in the ERRATA below.*

## Why this approach

Theorem R1 names mutual information as the memory coordinate of a classical record (`CORE.md:52`). The record kept here is the outcome \(M\), so that coordinate is \(P_\chi\). A8, in that same sentence, only requires the coefficient to be nonnegative. \(P_D\) is the entropy produced by the pinch, a different term. On this antipodal ensemble the two prices are one curve (ERRATA). The predictability sieve picks states by entropy production, with no stake (Zurek, *Progress of Theoretical Physics* 89:281, 1993, doi `10.1143/ptp/89.2.281`). Quantum Darwinism says the redundant classical record is the pointer record, again with no stake in the sum (Zurek, *Nature Physics* 5:181, 2009, doi `10.1038/nphys1202`). The cheapest question is whether putting a stake into \(J=P+wL\) moves the record basis, and whether the answer depends on which nonnegative \(P\) is used. The duel priced the quantum record by Holevo \(\chi\) (`duel/PREREG.md:27` on `ace-probe-memos-2026-11-23` at `e3e0e70`). This note prices the pinch by its relative entropy, \(P_D\), and scores Holevo \(P_\chi=I(W;M)\) beside it (`PREREG.md:30`, `PREREG.md:38`). PRL 70:1187 is Zurek, Habib, and Paz, "Coherent states via decoherence" (doi `10.1103/PhysRevLett.70.1187`). Its criterion is least entropy increase, and the paper uses the name "predictability sieve" for that procedure. It attributes the name to Zurek's chapter in the 1993 Halliwell, Pérez-Mercader, and Zurek volume and to the then-forthcoming PTP paper. The PTP paper (doi `10.1143/ptp/89.2.281`) is a naming source. The PRL applies the name as well (review M3). `PREREG.md:172` has the narrower sentence; that file stays locked. This is not the record-count headwind at `WALLS_REVIEW.md:65` on that branch: dimension is fixed at one qubit.

The excluded comparison is not scored. At Bloch radius \(0.6\), the relative entropy of a right-angle Bloch rotation is \(0.415888308336\) and \(r^2=0.360000000000\) (`pointer_basis_stakes_checks.out:2`). The stated \(0.416\) is that relative entropy at three decimals.

## Results

Class PB, \(r=0.6\), grid as locked. Complete dephasing is \(\gamma=0\). Partial is \(\gamma=1/2\). \(\theta=0\) is the dephasing axis. \(\phi=0\) is \(\sigma_z\). \(\phi=\pi/2\) is \(\sigma_x\).

| Slice | Price | Minimizer | Reading |
|---|---|---|---|
| \(\gamma=0\), every \(\phi\), every \(w\) | \(P_D\) | \(\theta=0\), unique | **PROVED (in-model).** Relabel of the sieve on this slice |
| \(\gamma=0\), \(\phi=0\) or \(\pi/4\) | \(P_\chi\) | \(\pi/2\) for \(w\le 1\); \(0\) for \(w\ge 10\), on the locked grid | **PROVED (in-model).** Those cells are endpoints. \(\theta=0\) becomes unique later. ERRATA |
| \(\gamma=0\), \(\phi=\pi/2\) | \(P_\chi\) | \(\pi/2\) at every \(w\), through \(w=100\) | **PROVED (in-model).** `pointer_basis_stakes_checks.out:34`–`:39` |
| \(\gamma=1/2\), \(\phi=0\), every \(w\) | \(P_D\) | \(\theta=0\) | **NUMERICAL.** Commuting stake does not move it |
| \(\gamma=1/2\), \(\phi=\pi/4\) | \(P_D\) | \(0\) at \(w=0\); grid cell \(0.449422\) at \(w=100\); continuous minimum \(0.448575\); cost gap \(3.89538721\times 10^{-1}\) | **NUMERICAL.** Stake moves \(\theta\) at \(w=100\). The same bar fails at \(w=1\). ERRATA |
| \(\gamma=1/2\), \(\phi=\pi/2\) | \(P_D\) | \(0\) through \(w=1\); \(\pi/2\) at \(w=10\) and \(w=100\) | **NUMERICAL.** `pointer_basis_stakes_checks.out:68` |
| \(\gamma=1/2\), \(\phi=\pi/4\) | \(P_\chi\) | \(\pi/2\) at \(w=0\); \(0.479966\) at \(w=100\) | **NUMERICAL.** Also moves. `:81` |
| Printed headline | both | (A) flips across prices | **Fixed by the closed forms** in `PREREG.md:72`. Not a scored test. ERRATA |

Closed form against the grid at \(\gamma=0\): max absolute error \(5.551\times 10^{-17}\) (`pointer_basis_stakes_checks.out:3`). Checks C0–C7 pass, `FAILS 0` (`:76`–`:85`).

### Complete dephasing, from the closed form

`PREREG.md:64` and `pointer_basis_stakes_checks.py:70`. For \(r\in(0,1)\), \(h((1+u)/2)\) is strictly decreasing in \(u\in[0,1]\), so \(P_D\) is strictly increasing on \([0,\pi/2]\) and zero only at \(\theta=0\). The loss satisfies \(L(\theta)-L(0)=(r^4\cos^2\phi/4)\sin^2\theta\ge 0\). Hence
\[
J_D(\theta)-J_D(0)=P_D(\theta)+w\big(L(\theta)-L(0)\big)>0
\]
for every \(\theta\in(0,\pi/2]\), every \(w\ge 0\), and every \(\phi\). The unique minimizer is the sieve basis. A stake scales the loss and does not move \(\theta\).

\(P_\chi\) is the same binary entropy with the opposite sign, so it is largest at \(\theta=0\) and zero at \(\theta=\pi/2\). The endpoint gap is
\[
J_\chi(0)-J_\chi(\pi/2)=P_\chi(0)-w\,r^4\cos^2\phi/4,
\]
with \(P_\chi(0)=0.096372378511\). Those two stakes, \(w>2.974456126879\) at \(\phi=0\) and \(w>5.948912253758\) at \(\phi=\pi/4\), are the endpoint crossings \(J_\chi(0)=J_\chi(\pi/2)\). They are not the stakes at which \(\theta=0\) becomes the minimizer. Just above each crossing the minimizer is interior, at \(\theta=0.763460\), and cheaper than either endpoint by \(1.731735\times 10^{-3}\). The unique \(\theta=0\) minimizer starts at
\[
w_\star(\phi)=\frac{1}{\cos^2\phi}\cdot\frac{\ln\frac{1+r}{1-r}}{2r^3},
\]
which is \(3.209014724815\) at \(\phi=0\) and \(6.418029449629\) at \(\phi=\pi/4\) (**PROVED, in-model**, from the closed form: one interior stationary point while \(2r<\alpha<\ln\frac{1+r}{1-r}\), with \(\alpha=2wr^3\cos^2\phi\), and none after). The locked grid jumps from \(w=1\) to \(w=10\) and never samples that window. At \(\phi=\pi/2\) the gap equals \(P_\chi(0)>0\) at every \(w\), so \(\theta=\pi/2\) is strictly cheaper (at \(w=100\), \(J=18\) against \(J(0)=18.09637238\), `:39`). The grid sits on the predicted side of both endpoint crossings (`:10`–`:15`). Predicate (A), "\(\theta=0\) for every stake at complete dephasing," is true for \(P_D\) and false for \(P_\chi\), and `PREREG.md:72` already says so.

### Partial dephasing

At \(\gamma=0\) the formulas already forbid a move under \(P_D\), so a grid is informative only for \(\gamma>0\), where \(P_D\) and \(L\) need not share a minimizer. That grid is the scored run. Under \(P_D\), a commuting stake stays at \(0\) (`:78`). A stake at \(\pi/4\) moves from \(0\) to the grid cell \(0.449422\) between \(w=0\) and \(w=100\), past the \(0.2\) rad bar, with cost gap \(0.389538721\) (`:77`). The continuous minimizer at that cell is \(0.448575\), half a locked step (\(\pi/1440\approx 0.002182\)) below the printed cell. The same bar at \(w=1\) fails: the stored minimizer is \(0.085085\) (`pointer_basis_stakes_checks.out:55`) and the continuous minimizer is \(0.085795\), both under \(0.2\). The first visible step, \(0.008727\) at \(w=0.1\) (`:54`), is below that bar. Holevo on the same slice also moves, from \(\pi/2\) to the grid cell \(0.479966\) (`:81`); the continuous Holevo minimizer at \(w=100\) is \(0.479348\). Dropping the \(\pm x\) states and keeping \(\pm z\), at \(\gamma=1/2\), \(\phi=\pi/4\), \(w=100\), leaves the \(P_D\) minimizer at \(\theta=0\). The partial-dephasing move needs those states. The tilt boolean does not flip. The always-sieve boolean does. On this ensemble that last sentence is a sign, because \(P_D+P_\chi\) does not depend on \(\theta\) (ERRATA).

## Conclusions

**Result.** The printed headline `PRICING_ARTIFACT` (`pointer_basis_stakes_checks.out:83`) is fixed by the closed forms already written in `PREREG.md:72`. At \(w=0\) the cost is the price, \(P_D\) is minimized only at \(\theta=0\), and \(P_\chi\) is minimized at \(\theta=\pi/2\). P4 restates that pair, and the headline rule returns the label as soon as P4 holds (`pointer_basis_stakes_checks.py:217`). C7 compares the rule to itself (`pointer_basis_stakes_checks.py:226`–`:227`). This is an open miss in the test, not a scored finding. The underlying slice stands: **PROVED (in-model)**, at complete dephasing the relative-entropy minimizer is \(\theta=0\) for every stake, and the Holevo minimizer is not.

**Model implication.** Conditional on \(P_D\): once dephasing is complete, the cost-minimizing record basis is the dephasing axis for every stake, a relabel of the sieve (**PROVED, in-model**). A stake moves \(\theta\) at partial dephasing on this grid when the observable does not commute with the axis (**NUMERICAL**), and that move needs the \(\pm x\) states. Theorem R1 (`CORE.md:52`) names mutual information as the memory coordinate of a classical record. The record kept here is \(M\), so that coordinate is \(P_\chi\). \(P_D\) is the entropy produced by writing, a different term. A8 requires each coefficient to be nonnegative. The ratio of the two coefficients is the open number below.

**Open miss.** On this antipodal ensemble
\[
P_D(\theta)+P_\chi(\theta)=\ln 2-\mathbb{E}[S(\rho)],
\]
and the right-hand side does not depend on \(\theta\). The two prices are one curve. R1 already names the classical coordinate, and A8 does not have two candidates for it on this ensemble.

**Exchange rate.** With the terms named, the cost is
\[
J=\kappa\,I(W;M)+\kappa_D\,P_D+w\,L,
\]
with \(\kappa,\kappa_D\ge 0\) (A8, `CORE.md:52`). \(I(W;M)\) is \(P_\chi\). The open number is the ratio \(\kappa_D/\kappa\), the exchange rate between the entropy of writing and the information held. The two prices scored above are the endpoints of that ratio, \(0\) and \(\infty\). On this antipodal ensemble the sum \(P_D+P_\chi\) does not depend on \(\theta\), so at \(\kappa_D=\kappa\) the record terms are flat in \(\theta\) and the stake alone sets \(\theta\). Until the ratio is derived, every claim in this note is conditional on it. A record kept as an unmeasured state is a separate question and is not taken up here.

The grid does not answer whether a non-commuting stake moves \(\theta\) under one price and not the other once the sum depends on \(\theta\). That question is a test of whether the ratio matters off this ensemble. It is locked, unscored, in `PREREG_2.md` (commit `8ea241d`). The four-angle check of the sum named in `PREREG_2.md:21` was not saved.

**Conjecture, not a result.** The entropy-production half is the proved slice above: on this ensemble, complete pure dephasing keeps the sieve basis for every stake when the price is \(P_D\). The Holevo half is the other sign of the same curve here, so this grid does not separate the two prices. Quantum Darwinism's redundancy plateau was not computed, and this grid does not extend it.

## Deviations

The preregistration reserved open-work id T70 (`PREREG.md:5`) because each open fork branch then printed a T69 row and none printed a higher id. Those four questions are assigned T69 through T72: layer fixed point, constants as exchange rates, information causality, composite records. This row is **T73**. The model, the grid, the prices, the predictions, and the headline rule are unchanged. `PREREG.md:107` named the pass line `ALL T70 CHECKS PASS`. The script prints `ALL T73 CHECKS PASS` (`pointer_basis_stakes_checks.out:85`). Same checks, corrected id.

No other change to the criteria. `PREREG.md`, `RUN_LOG.md`, and `pointer_basis_stakes_checks.out` are untouched. The scratch named in `PREREG.md` §5.3 was not kept and is not a number above. The reading corrections are the ERRATA.

## ERRATA

*After `theory/reviews/POINTER_BASIS_STAKES_REVIEW_2026-11-24.md` (commit `992920b`). The stored output is not regenerated. `PREREG.md` and `RUN_LOG.md` are not edited.*

**E1. Headline.** High finding of the review. `PREREG.md:72` already fixes \(Q(P_D)\) true and \(Q(P_\chi)\) false at \(w=0\), because \(P_D\) increases with \(|\theta|\) and \(P_\chi\) is largest at \(\theta=0\). The headline table returns `PRICING_ARTIFACT` on that flip alone (`PREREG.md:96`, `pointer_basis_stakes_checks.py:217`). P2, P3, P5, and P6 do not enter. C7 (`pointer_basis_stakes_checks.py:226`–`:227`) compares the rule to itself. Under the rule that an identity is not a test, the printed headline is **fixed by the locked closed forms**. It is not a test result. The label in `pointer_basis_stakes_checks.out:83` stays, because the stored output stays. **Open miss:** the scored run could not have come out another way, so it did not decide whether a stake chooses the classical basis. The proved \(P_D\) relabel at complete dephasing, and the numerical partial-dephasing grid, are separate from that label.

**E2. One curve.** On this ensemble the four states are two antipodal pairs, so \(P(M=+1)=1/2\) at every \(\theta\) and every \(\gamma\). Then \(P_D+P_\chi=\ln 2-\mathbb{E}[S(\rho)]\), constant in \(\theta\). At \(\gamma=0\), \(P_\chi=P_\chi(0)-P_D\). Minimizing one price is maximizing the other. A density-matrix reading in the review, and the closed form, agree. Theorem R1 (`CORE.md:52`) already names mutual information as the classical record's coordinate, and the record kept is \(M\), so that coordinate is \(P_\chi\). \(P_D\) prices the disturbance of the pinch. The two are not two choices of one coordinate on this ensemble. The previous draft's open miss, that R1 and A8 leave the quantum price unfixed, is narrowed to that.

**E3. Holevo window.** \(2.974456126879\) and \(5.948912253758\) are endpoint crossings. The unique \(\theta=0\) minimizer starts at \(3.209014724815\) and \(6.418029449629\). Between them the minimizer is interior, \(\theta=0.763460\), cheaper than either endpoint by \(1.731735\times 10^{-3}\). The grid's stakes jump from \(1\) to \(10\) and skip the window. At \(\phi=\pi/2\) there is no window.

**E4. Partial dephasing, scope.** P2's bar fails at \(w=1\): \(\theta=0.085085\) on the stored grid (`pointer_basis_stakes_checks.out:55`). The locked P2 compares \(w=100\) and passes. The continuous \(P_D\) minimizer at \(\gamma=1/2\), \(\phi=\pi/4\), \(w=100\) is \(0.448575\). The stored \(0.449422\) is the cell. The move needs the \(\pm x\) states: without them the \(P_D\) minimizer at that cell stays at \(0\).

**E5. Citation.** PRL 70:1187 uses the name "predictability sieve" and applies the least-entropy procedure. The PTP paper remains a naming source. The earlier sentence that the PRL does not name the sieve is withdrawn.

**E6. Follow-up.** The two-line gate on a non-antipodal ensemble passes. (a) The split can fail, and a split or a miss would each change the belief E2 leaves: whether a stake moves \(\theta\) under one price and not the other once the prices are not one curve. (b) Two states, one angle, one stake pair, no bath and no Monte Carlo, is the cheapest such test. It is locked in `PREREG_2.md` (commit `8ea241d`), predicted label `NOT_SPLIT`, failing input `SPLIT`. No scoring script has been run. The four-angle check of the sum named in `PREREG_2.md:21` was not saved.

**E7. Exchange rate.** The cost with both record terms named is \(J=\kappa\,I(W;M)+\kappa_D\,P_D+w\,L\), \(\kappa,\kappa_D\ge 0\). The open number is \(\kappa_D/\kappa\). At \(\kappa_D=\kappa\) the antipodal record terms are flat in \(\theta\) and the stake alone sets \(\theta\). Until that ratio is derived, every claim above is conditional on it.
