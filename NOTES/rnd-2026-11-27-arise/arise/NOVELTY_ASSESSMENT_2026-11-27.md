# Novelty assessment: how much does novelty matter in the P4 runs?

*Friday 27 November 2026, about 01:10–01:20 EST. Written after P4-BAND and P4-BAND-T were scored, as asked by Chad (via the parent agent): judge novelty by the theory's own rule (stake × need vs upkeep; keep / check / fade), weighed against heredity, the timed cue and the price, and give it the weight the evidence earns. Labels: observed (a script printed it), PIM (proved-in-model, this toy only), hypothesis, known (prior art). In-model toys only. No physics claims. Append-only note.*

## Judgment, stated plainly
**Novelty is a minor condition in this evidence: a wide range condition, not a fine-tuned or central one.** Heredity and a timed cue are each necessary at every novelty rate tested; removing either takes anticipation to about zero. Novelty matters only at the edges of a window about 2.5 decades wide. The upper edge is already in the theory's switch-on claim (SE7/N28, "heredity below Eigen's threshold"), and the lower edge is the familiar point that a variant has to exist before it can be selected. By the hold rule: **check, not keep as a new clause.** It is worth one line under N28, not a row of its own. It may matter more where the window is narrow, which is untested.

## 1. What novelty did in each run
| Run | Model | Novelty's role (mechanism) | Numbers | Side of band | Label |
|---|---|---|---|---|---|
| P4c | fixed-menu lumped cores | Switching arises only through deep crashes plus one-molecule nucleation; more switching means less faithful inheritance | κ ≈ 1 − 1.3 × switch (switch 0.002 → κ 0.996; 0.11–0.14 → κ 0.82–0.86); at switch ≈ 0.12 even a ready-made reader did not pay (0/5, cores ≈ 0.25 each) | high | observed |
| P4d | fixed menu, reader absent at start | Nucleation brings the menu reader in; more novelty erodes its spread | S = ON − drift falls monotonically: +0.50 (μ 1e-3) → +0.01 (μ 0.1); reader appeared 10/10 at every μ; interior optimum FAILED (range too high) | high only | PIM (toy), with open miss |
| P4e | open-ended cores, zero-read start | Novelty is the only source of readers | μ 1e-5: 3/10 seeds no reader, MI 0.010; μ 1e-4–1e-2: MI ≈ 0.09–0.10 (ceiling); (d) tie artifact | low only | observed; (d) not informative |
| P4f | open-ended, A measure | Same | A 0.0024 (1e-5), 0.012 (1e-4), 0.020 (1e-3), 0.023 (1e-2); F4 interior FAILED | low only | PIM (toy), with open miss |
| P4g | same | High novelty washes out timing | median A 0.0196 (1e-2), 0.0179 (3e-2), 0.0052 (1e-1); p 9.1e-5 | high | PIM (toy) |
| **P4-BAND** | same, one locked 12-point transect | Both edges in one run | median A 0 (1e-6) → 0.0154 (1e-4) → **0.0250 (1e-2, peak)** → 0.0053 (1e-1) → 0.0034 (3e-1); peak CI μ 1e-3–1e-2; all 7 clauses PASS | both | **PIM (toy)** |
| P4-BAND-T | same, T 2× | Low edge did not move as a supply limit predicts (underpowered); high edge stable | low shift +0.16 (CI −0.50..+0.83) FAIL; high shift −0.10 (CI −0.22..+0.04) PASS | both | observed; S1 open miss |

**Mechanisms (observed, descriptive, from P4-BAND):**
- *Low side:* readers arrive rarely and seeds split into "a reader arrived and spread" or "none did" (A > 0.005 in 0/20, 1/20, 6/20, 8/20, 16/20 seeds from 1e-6 to 1e-4). A pure arrival-supply story (μ·N·T) was **not** supported by the 2× run-length test (P4-BAND-T S1 FAIL, underpowered).
- *High side:* identity turnover outruns selection on timing. The informative-lag share falls (0.90 → 0.27) while reader cores stay common (0.75), and heredity stops mattering (OFF ≈ ON at μ ≥ 0.1). **Growth does not fall** (0.0679 at both 1e-2 and 3e-1, post hoc). At high novelty, a re-supplied spread of untimed protectors does about as well for growth as a timed reader. So the high edge removes *anticipation*, not fitness.

## 2. Novelty weighed against the other conditions (same toy)
| Condition | Effect of removing or breaking it | Range over which it binds | Weight |
|---|---|---|---|
| Heredity | A → ≈ 0 at every μ ≤ 3e-2 (P4f F1; P4-BAND C1: 0.0007 vs 0.0250 at the peak) | everywhere except μ ≥ 0.1, where nothing is left to lose | **major** (necessary) |
| Timed cue | A → ≈ 0 at every μ (RANDOM ≤ 0.0002; P4e, P4f, P4-BAND C3) | everywhere | **major** (necessary) |
| Price | reading stops above c*_evolved ≈ 0.51 (CI 0.44–0.56; P4g); moderate price c 0.3 doubles A (P4h H1, mechanism unknown) | above a threshold; shapes A below it | **moderate** (a range condition, plus a shaping effect) |
| Novelty | A → 0 below about 3e-5 and falls about 5× above 3e-2 | outside a window of about 2.5 decades | **minor** (a wide range condition) |

Hold-rule reading: stake × need for a separate novelty clause is low because (a) its upper bound is already SE7's Eigen clause, (b) its lower bound is implicit in "a *selected* model" (something to select from), and (c) inside a 2.5-decade window it barely changes A (within about 40%). Upkeep of a new clause (wording, a failure test, review) exceeds that. **Check:** keep it as a note under N28 and re-check it if a model shows a narrow window.

## 3. Possible link to the peak (hypothesis only)
- *Hypothesis:* if, as Chad's 26 Nov aim puts it, tracking comes first, any tracker that has to be found by selection needs a supply of new states bounded by retention: an explore/retain window. P4-BAND is one toy instance of such a window.
- Caveats: this is the generic exploration–exploitation and mutation–selection tradeoff, known in biology and learning. Nothing here bears on forces, gravity or any physics; no physics is derived or claimed. W11 (closure picks nothing asymmetric) and W13 (self-reference moves the input) still apply: the window's position was set by the hand-made world (toxin period, lag space).
- A testable sharpening (hypothesis): the window sits where novelty roughly matches the world's drift rate, which would tie it to SE7's "drift inside the hold band" rather than make it a separate condition. Untested (see §5).

## 4. Prior art and what, if anything, is new
DOIs verified on Crossref tonight (p4band/crossref_band.out):
- Eigen 1971, *Naturwissenschaften*, doi 10.1007/BF00623322: the error threshold. The high side matches it **in shape only**; the toy has no sequence space.
- Leigh 1970, *Am. Nat.*, doi 10.1086/282663, and Sniegowski, Gerrish & Lenski 1997, *Nature*, doi 10.1038/42701: mutation-rate evolution; an intermediate rate tied to environmental change is known in kind.
- Kussell & Leibler 2005, *Science*, doi 10.1126/science.1114383, and Kussell, Kishony, Balaban & Leibler 2005, *Genetics*, doi 10.1534/genetics.104.035352: sensing vs stochastic switching in fluctuating environments. The high-side result (a re-supplied untimed spread matches the timed reader's growth) is **known in kind** from that work; it overlaps repo row CL20 (bet-hedging, PRIOR ART).
- Philippi & Seger 1989, *TREE*, doi 10.1016/0169-5347(89)90138-9: bet-hedging.
- Pigliucci 2008, *Nat. Rev. Genet.*, doi 10.1038/nrg2278: evolvability.
- (One DOI I first tried for Kussell et al. 2005 pointed to an unrelated paper; it is flagged in crossref_band.out and not used.)

**New, narrowly:** a single preregistered, controlled toy run in which a timed reader that is not written in arises and is kept only inside a two-sided novelty window, with the tie rule, heredity-off and untimed-cue controls at every rate, and a CI on the peak. **Not new:** the existence of an intermediate novelty optimum, the error threshold, and the sensing-vs-hedging tradeoff. I see no new principle here.

## 5. Open misses and the next cheapest tests
**Open misses (sizes and places; not rescored):**
- P4d P1 interior optimum: monotone, best at the lowest μ (range too high). `p4d/RESULTS_AND_REVIEW_P4d_2026-11-26.md`.
- P4e (d): tie artifact at the MI ceiling. `p4e/RESULTS_AND_REVIEW_P4e_2026-11-26.md`.
- P4f F4: A rose monotonically through 1e-2. `p4f/RESULTS_AND_REVIEW_P4f_2026-11-27.md`.
- P4-BAND-T S1: the low edge did not shift with 2× run length (+0.16; CI −0.50..+0.83). The low-side mechanism is unexplained. `p4band/RESULTS_AND_REVIEW_P4BAND_T_2026-11-27.md`.
- High side affects A but not growth (post hoc): "too much novelty erases judgment" holds for timing only.

**Next cheapest tests (by expected information per hour):**
1. *Window vs world drift (about 15 min compute):* make the cue–toxin lag L* drift at rates r ∈ {0, slow, fast} and rerun a coarse μ transect. Prediction (hypothesis): the window's upper edge stays while its centre moves up with r. This is the one that could tie novelty to SE7's drift band, or show it is separate. Highest value.
2. *Powered low-side test (about 10 min):* 40 seeds at μ 1e-5, 3e-5, 1e-4 with T 6000 vs 12000 vs N_c 400, with an absolute success rule (A > 0.005), to settle whether the low side is a supply limit.
3. *Reader present at start (about 5 min):* rerun the low side with a timed reader seeded in. If the low side disappears, it is arrival only; if it remains, low novelty costs something else (for example, no way to re-find the lag after loss).

## Proposal for CLAIM_MAP_v2 (for Ace; not applied; CLAIM_MAP_v2.md is not edited)
- **N28 (SE7), status stays OPEN.** Proposed note: "In-model evidence (toy, GTAO notes 27 Nov, branch forge-rnd-arise-2026-11-27): in a lumped-core toy with open-ended variants and no reader written in, a timed reader arises and is kept only with heredity, a timed cue and a price below c* ≈ 0.5, and only inside a two-sided novelty window about 2.5 decades wide (P4-BAND, preregistered, 7/7 clauses; peak μ 1e-3–1e-2). The window's upper edge is consistent in shape with the Eigen clause; its lower edge says a variant must arise. Registered misses: P4d P1, P4e (d), P4f F4, P4-BAND-T S1. In-model, toy; not a field result."
- **No new row** for novelty (judgment above). If Ace prefers a row: "N-NOV (hypothesis): the switch-on novelty window tracks world drift," OPEN, with test 1 above as its failure test.
- **CL20 (PRIOR ART):** a possible cross-reference: "toy instance (P4-BAND, post hoc): at high novelty a re-supplied untimed spread matches a timed reader's growth (Kussell & Leibler 2005)."
