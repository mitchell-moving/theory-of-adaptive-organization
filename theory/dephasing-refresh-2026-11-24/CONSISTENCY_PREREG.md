# CONSISTENCY PREREG: the scored bars cannot miss

*Tuesday 24 November 2026 (UTC). Own file. `PREREG.md`, `ADDENDUM_PREREG.md`, `ADDENDUM_REVIEW_PREREG.md`, and `ONSET_PREREG.md` are not edited. Commit this file before any further computation. Branch `forge-dephasing-refresh`. `THEORY.md` and `CORE.md` are not edited. Open-work id **T84b**. Self-check, not an independent review. The independent review of head `067c485` is fork PR #26 comment `7145474164`, write-up `theory/reviews/DEPHASING_REFRESH_REVIEW_2026-11-24.md` on `forge-refresh-review` (fork PR #28).*

Can it fail: it cannot, while the closed forms in the three locks and in `ONSET_PREREG.md` stand. That is why the label below is a consistency check, not a test.

Cheapest way to fail it: there is none inside these formulas. A different loss, a different age law, or a measured device would be a different model. This file does not score one.

## Why this approach

The review's blocker is that no bar scored at `067c485` can miss while those closed forms stand. The later onset lock (`ONSET_PREREG.md`, commit `a27520c`) compares the same kind of closed forms: \(c^*=2\kappa kT\,b/a\) with \(a=1\), \(b=2\), and \(\Pi_c(\Theta)=2\Theta^2/[1-(1+\Theta)e^{-\Theta}]\). A stake derivative, an age integral, and a change of the short-time slope are fixed by those definitions. None of them can land outside the algebra. Process item 5 on upstream `652d936`: a sure-thing comparison has information about 0.

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. The qubit and the dephasing channel are inputs. The record price is a cost.

## 1. No missable bar

The named rival of the onset map remains a coincidence of the integer 4: \(2b/a=4\) from `theory/CLOCK_TERM_2026-11-23.md:126`, and 4 from the \((\gamma T)^2\) expansion of the Hamming time average. Both sides are fixed. There is no numeric band the arithmetic can leave.

Checked, and rejected, as candidates for a bar that could miss:

- Stake elasticity of \(A_c=w\gamma T^2/\Pi_c\). \(\Pi_c\) has no \(w\), so the elasticity is 1. It cannot be anything else.
- Exponential-age slope of the same Hamming loss. The integral is \(1/2\). The uniform-age slope is \(1/4\). Neither can move.
- Half-slope probe, \(\beta=1/8\). The refresh limit is \(1/\beta=8\), and \(c^*\) stays 4. That is arithmetic.

No other input inside these formulas is free. **No bar that can miss was built.** Label, up front: `CONSISTENCY_CHECK`. There is no scoring script.

## 2. Class of the model

The model is one reset, with loss linear in the gap, and no clock rate. That is the slow-drift square-root/EOQ class, KNOWN at `theory/INTERNAL_MODEL.md:45` and `:180`. The same exponent is the continuous-diffusive balance at `theory/CLOCK_TERM_2026-11-23.md:55` and the square-root minimum at `CORE.md:91`. It is not the deterministic-drift branch, whose lag grows as \(1/f^2\) and whose rate scales as \(w^{1/3}\) (`theory/CLOCK_TERM_2026-11-23.md:40-47`, `:55`).

The short-period identities \(\tau^*\sim 2\sqrt{A/(w\gamma)}\) and \(J^*\sim\sqrt{A w\gamma}\) are that class. Scoring them is `NOT A TEST`. Information about 0.
