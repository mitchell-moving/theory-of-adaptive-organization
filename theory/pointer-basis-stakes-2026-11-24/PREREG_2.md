# PREREG_2: do the two prices split once they are not the same curve?

*Tuesday 24 November 2026. Committed alone, before any scoring script for this question. The parent note is `MEMO.md`. Its preregistration `PREREG.md` and its run log `RUN_LOG.md` stay as locked. `THEORY.md` is not edited. This file does not rescore class PB.*

## Run gate

(a) It can fail, and either outcome would change the belief left by the review. The claim is that a non-commuting stake moves the record angle under the relative-entropy price and does not move it under Holevo \(\chi\). The two-state stationarity condition is transcendental, so the locked cell does not fix that split or its negation. A split would mean the price choice still decides the basis once the prices are not one curve. A miss would mean the one-sided tilt does not survive the smallest break of the antipodal pairing. The four-point "both move" reading was a sign flip of one curve (`MEMO.md` ERRATA), so it did not decide this.

(b) Yes. This is the cheapest test of that claim: one qubit, two states, one projective measurement, one observable angle, one stake pair, and a one-dimensional angle grid. No bath Hilbert space and no Monte Carlo.

## 0. Question

On a non-antipodal ensemble, where \(P_D+P_\chi\) depends on the record angle, does a stake on an observable that does not commute with the dephasing axis move the minimizing \(\theta\) under \(P_D\) and leave it unmoved under \(P_\chi\)?

Class PB is not rerun. Its headline was fixed by the closed forms in `PREREG.md:72` before any grid was scored. This file asks the question that closed form does not answer.

## 1. What is already fixed, and what is not

Theorem R1 (`CORE.md:52`) names mutual information as the memory coordinate of a classical record. The record kept is the outcome \(M\), so that coordinate is \(P_\chi=I(W;M)\). A8 requires the coefficient to be nonnegative. \(P_D\) is the entropy produced by the pinch, a different term.

On the four-point antipodal ensemble the sum \(P_D+P_\chi\) does not depend on \(\theta\). Minimizing one price maximizes the other. This ensemble is chosen so that the sum depends on \(\theta\). A four-angle check of the sum, and no evaluation of \(J\), was run before this lock to confirm that dependence. The sum at \(\theta=0\) and at \(\theta=\pi/2\) differs by more than \(0.03\) nat at \(\gamma=1/2\). That difference is not a scored quantity, and no minimizer angle from any scratch is a criterion.

## 2. Model (class PB2)

Same qubit, same pure dephasing, same radius \(r=0.6\), same projective record \(n(\theta)\cdot\sigma\), same stake \(A(\phi)\), same conditional-mean action, same squared loss, same prices \(P_D\) and \(P_\chi\), same cost \(J_P=P+wL\), \(\kappa=1\). Definitions are the ones in `PREREG.md` §1–§2.

**What changes.** \(W\) is uniform on two labels \(\{+z,+x\}\). Pre-dephasing Bloch vectors \(+r\hat z\) and \(+r\hat x\). They are not an antipodal pair, so the outcome bias is not cancelled. \(\gamma=1/2\) only: a transverse component survives. \(\gamma=0\) is out of scope, because complete dephasing erases the component this question is about. \(\phi=\pi/4\) only.

**Why \(w=1\) against \(w=0\).** On class PB the price and the stake term are the same order at \(w=1\), and at \(w=100\) the price is a small shift of the loss minimum (review M1). The comparison that can still go either way is \(w=0\) against \(w=1\). \(w=100\) is not scored.

**Grid.** \(721\) points, \(\theta_j=j\cdot(\pi/2)/720\). Tie \(10^{-9}\). `SEED = 20261124`, not drawn from. No random numbers.

**Separation.** For each price, \(\Delta\) is the absolute gap between the minimizing angles at \(w=0\) and at \(w=1\). If several grid points lie within the tie, the minimizer used for \(\Delta\) is the smallest \(\theta\) among them. If two tied minimizers differ by at least \(0.2\) rad, the cell is `UNRESOLVED`.

## 3. Headline, and the input that fails it

| Predicates on the one cell | Label |
|---|---|
| \(\Delta_D\ge 0.2\) and \(\Delta_\chi<0.2\) | `SPLIT` |
| both separations \(\ge 0.2\) | `BOTH` |
| both separations \(<0.2\) | `NEITHER` |
| \(\Delta_D<0.2\) and \(\Delta_\chi\ge 0.2\) | `CHI_ONLY` |
| a tie spans \(0.2\) rad, or the sum \(P_D+P_\chi\) varies by less than \(10^{-3}\) on the grid | `UNRESOLVED` |

`SPLIT` is the claim under test: the stake moves \(\theta\) under \(P_D\) and does not move it under \(P_\chi\). The other three resolved labels are `NOT_SPLIT`.

**Predicted label, written before any scoring script: `NOT_SPLIT`.** Reason, an argument and not a computation: both costs add the same loss, and the prices differ by the marginal entropy \(H(M)\). Nothing in that sum places the loss minimum on the \(w=0\) minimizer of exactly one price. The argument does not derive the label. \(H(M)\) could still pin one minimizer and not the other.

*Fails if* the cell returns `SPLIT`. `BOTH`, `NEITHER`, and `CHI_ONLY` all confirm the prediction and are reported separately, because they are different misses of the one-sided claim. `UNRESOLVED` is a puzzle. It does not confirm the prediction.

**Effect size.** A move smaller than \(0.2\) rad does not count. The same cut as class PB, so a pass here is the same angular bar that class PB cleared only at \(w=100\).

## 4. Code, when a script is written

A later commit may add `theory/pointer_basis_stakes_checks/pointer_basis_stakes_2_checks.py`, standard library only. It is not part of this commit. It would print the two separations, the sum's range, the label, `FAILS`, and a pass line only when the predicted label holds. A stored stdout would be byte-compared. This lock does not contain those bytes.

## 5. What this note will not say

It will not edit `THEORY.md`. It will not say that quantum mechanics, general relativity, or holography has been derived. Dephasing and the qubit are inputs. It will not call the hypothesis a law, and it will not say the question is solved. A miss is a puzzle. The record price is a cost.
