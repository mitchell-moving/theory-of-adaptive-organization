# Addendum to NOVELTY_ASSESSMENT_2026-11-27: after P4-DRIFT and P4-CLOSE

*Friday 27 November 2026, about 02:15 EST. New file; the earlier assessment (SHA-256 79f55a47…) is not edited. Labels: observed, PIM (proved-in-model, toy only), hypothesis, known. In-model toys. No physics claims. Sources: p4drift/RESULTS_AND_REVIEW_P4DRIFT_2026-11-27.md (SHA-256 e3fe7ea2…), p4close/RESULTS_AND_REVIEW_P4CLOSE_2026-11-27.md.*

## What the two runs added (observed, in-model)
| Run | Question | Result |
|---|---|---|
| P4-DRIFT (seeds 1601–1624; prereg 1c35c911…) | Does the band's peak move up with world drift? | **Primary D1 FAIL** (centroid +0.21 vs ≥ +0.25 registered; CI +0.05..+0.35); D1m FAIL. D2 PASS (low edge +0.69; CI +0.13..+1.10); D3 PASS (high edge −0.20); D4, C1, C2 PASS. The window is squeezed from below (width 3.19 → 2.30), the peak moves slightly down, and peak anticipation falls 0.023 → 0.016 → 0.010. |
| P4-CLOSE (seeds 1701–1716; prereg bbb9516d…) | Does the window close as drift rises further? | **Primary K1 FAIL** (width 2.37 at r 1/10; max mean A 0.0093 ≫ 0.005); K2 FAIL; K3 FAIL (−0.31; CI −0.83..+0.35); K4 PASS (2.69); C PASS (p 1.4e-6). The window does not close; the squeeze saturates. |

Open misses added: P4-DRIFT D1 and D1m, P4-CLOSE K1, K2 and K3 (all my directional predictions about *where* the band goes).

## Updated judgment, by the theory's own rule (stake × need vs upkeep; keep / check / fade)
**Novelty stays minor, with one refinement: it is a wide range condition whose floor depends on the world's drift. Outcome: check, not keep as a new clause, not fade.**

| Condition | Evidence now | Weight |
|---|---|---|
| Heredity | necessary at every μ ≤ 3e-2 (unchanged; controls at r 1/100 also ≈ 0) | major |
| Timed cue | necessary at every μ and every drift (RANDOM ≈ 0 at r 1/100 and 1/10) | major |
| Price | reading stops above c* ≈ 0.51 (unchanged) | moderate |
| World drift | cuts anticipation to about 40% at moderate drift, then plateaus; raises the novelty floor by about 0.7 decades; does not close the window | moderate |
| Novelty | needed above a floor that rises with drift; top roughly stable (it moved down about 0.6 decades beyond r 1/100); window 2.2–3.2 decades at every drift tested | **minor** |

Why not "keep": the drift prediction that would have made novelty a *binding* condition (the window closing, or the peak tracking drift) failed twice, so its stake × need stays low. The window's width never fell below 2.2 decades, so it binds only at the edges. Why not "fade": the floor shift (D2) is a real, controlled, in-model dependence of the novelty requirement on world drift, which is the content of SE7's "drift inside the hold band" read together with its novelty/Eigen clause. It earns one line, not a row.

## Link to the peak (hypothesis only; no physics claims)
- The window is an explore/retain tradeoff that the world's change rate shifts in one direction only (the floor rises). That is generic, and known in kind (Leigh 1970, doi 10.1086/282663; Kussell & Leibler 2005, doi 10.1126/science.1114383; Eigen 1971, doi 10.1007/BF00623322 for the top edge in shape). Both DOIs were verified on Crossref (p4band/crossref_band.out).
- Nothing here bears on forces or gravity. W11 and W13 still apply: the window's position was set by the hand-made world (L* ∈ {4, 11}).
- **What is new, narrowly:** a preregistered, controlled toy measurement of how the novelty floor moves with drift (+0.7 decades) and that the window does not close up to r 1/10. Not new: the qualitative tradeoff.

## Mechanism hypotheses raised (untested)
- At fast drift the population specialises on one regime's reader (lag 0–4 share 0.91, other regime 0.06 at r 1/10, μ 1e-3) and is right about half the time. This differs from a both-types hedge. A test: seed both reader types and see whether they persist, or make the two regimes unequal in cost.
- The window top falling at r ≥ 1/30 (high edge −1.15 → −1.8) is an unscored single-run observation.

## Proposal for CLAIM_MAP_v2 (for Ace; not applied; the file is not edited)
- **N28 (SE7) stays OPEN.** Replace the earlier proposed note's last sentence with: "In a drifting-lag version of the toy (P4-DRIFT, P4-CLOSE, preregistered), drift raised the lower novelty edge by about 0.7 decades and cut peak anticipation to about 40%, but did not close the window up to a regime-change rate of 1/10 per unit time. Registered misses: D1, D1m, K1, K2, K3. In-model, toy; not a field result."
- **No new row for novelty.** The optional "N-NOV: the window tracks world drift" is **not supported** as stated (the peak did not track drift); if a row is wanted, word it as "the floor rises with drift", OPEN, with a failure test of 'no floor shift at 2× the seeds'.

## Next cheapest tests (stopped here; not run)
1. Specialisation versus hedge at fast drift (seed both reader types, or unequal regime costs), about 10 min. Expected value under about 0.02 bits per hour: it explains a mechanism in one toy and moves no weight.
2. Powered low-side supply test (P4-BAND-T): not made decisive by drift. Both runs show drift moves the floor, which is a separate question.

**Stop.** By the keep/check/fade rule, further runs in this toy would tune a minor condition. The larger value now is Chad and Ace deciding whether the N28 note above is wanted.
