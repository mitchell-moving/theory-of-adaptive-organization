# PREREG ADDENDUM

*24 November 2026. `PREREG.md` is already committed (`da9c817`, 2026-11-24 04:33:58 +0000) and is not edited. This addendum adds Ace's three requirements. It does not change the locked cells, the thresholds, or the odds.*

**Deviation.** Run 1 (`nest_map.py`, `nest_map.out`, `nest_map.json`, `RUN_LOG.md`) was executed before this addendum existed. Those files are uncommitted at this commit. The requirement arrived after `PREREG.md` was locked and after that run. This commit contains no result output. No further results-producing run starts until this file is committed.

## 1. An input on which each locked prediction fails

These inputs were not part of the locked cell. They stop the checks being identities. They are not a rescoring of run 1.

| Prediction | Fails on this input |
|---|---|
| S1. \(\max \|T f_*-f_*\|<10^{-12}\) with the prefactor 2 | The same \(f_*\) and the same \(b=2\), but the prefactor in \(T\) replaced by 1. Then \((Tf_*)(u)=f_*(u)/2\), and the residual is order 1. |
| S2 / Lemma A. Every \(At+B/t\) is sent to \(u+1/u\) | \(f(t)=(t+1/t)+(t^3+t^{-3})\). The proof uses one power pair. This sum is outside the family, and one application does not return \(f_*\). |
| Lemma B. \(F_0=3\sqrt{2}\) for \(b=2\), and two same-\(J_1\) copies are not an income fixed point | The equality fails at \(b=3\). The strict gap fails at \(b=1\), where \((1+b)/\sqrt{b}=2\) and the rescaled minimum equals the one-copy minimum. |
| SUPPORT. One \(\rho\), the same to 0.02 on \(\varphi_1,\varphi_2,\varphi_3\) | Mode order 5 in place of mode order 3, at the locked \(b\), \(s\), and window. The three locked deformations are exactly this comparison. Run 1 had already been executed when this row was written; that timing is the deviation above, not a new prediction of the cell. |

## 2. Prior art, logged before any further run

Repo grep on this branch, 24 November 2026, after `PREREG.md` and before any run beyond run 1. "Feigenbaum", "Coullet", "Lanford", and "period-doubling" appear only in `PREREG.md`. The conjecture under test is not in this tree. It is `MIRROR_MEMO.md` §6 on `ace-probe-memos-2026-11-23` at `e3e0e701`, left **CONJECTURE, untested**, by `MIRROR_REVIEW.md`. That branch is cited and not merged.

Already in this tree, and not the object under test:

- `theory/MATH_COMPLETENESS_AUDIT.md` §(iii). An RG fixed point of layered design would be a beta function for price ratios. The audit says a universal layered fixed point is likely false, and that the dimensionless groups in `THEORY.md` B.9 do not produce layers.
- `theory/MATH_ATTACK.md` §3.1 and §3.6. Shock distributions have probabilistic-RG fixed points. The same note says the renormalization picture here is a Gaussian fixed point with no anomalous exponents, and that claiming a deep RG would be inflation.
- `reviews/night1/CORE_AUDIT.md` §2.5(e). \(\Pi^\star\) and a vigilance ratio are exponent arithmetic at \(H=1/2\), not an eigenvalue of a nesting map.

Literature check for the operator analogy is the one already locked in `PREREG.md` §5, with DOIs in `crossref.out` (Crossref, 24 November 2026). No further citation is added. Nothing in that list states the operator in `PREREG.md` §1.

## 3. Quantum-record price

No price of a quantum record is used. **Modeling choice, stated:** the cost is the classical scalar tracking cost, \(J=c/\tau+\alpha\tau\), ruin cap outside the sum (`PREREG.md` §1). **Reason:** Theorem R1 (`CORE.md` line 52) fixes the memory coordinate as Shannon mutual information for classical records (finite alphabets; the Gelfand–Yaglom–Dobrushin supremum when the mutual information is finite). It does not set a price for a quantum record. This test does not add one. The memory coordinate is not an input of the operator.

## 4. Working conjecture these outcomes are read against

Ace's working conjecture, not a result: **the cost may fix dimensionless or structural facts, but not constants.**

A SUPPORT cell (one \(\rho\), independent of deformation, window, step, and the locked caps) would be a constant read off this cost and would count against that conjecture. A rate that depends on the mode order or on the nesting ratio \(b\) is a structural dependence. It is not a constant, and one operator does not establish the conjecture.
