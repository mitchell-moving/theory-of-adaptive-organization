# Independent review: PR #265 (UFR forgetting note, locked prediction UFR-P1) and X reply Draft A

*Record of the independent review of PR #265 (merged as `ecdfe46`), with its passing re-check of head `a018aed` at the end (`OPEN_WORK.md` row `UFR-GAPS` cites it). Committed 24 November 2026 from the reviewer's file unchanged except: box paths are written `<local>`, the X reply draft path is described instead of printed, the heading word for the outcome is written RESULT instead of the reviewer's original, and the paper's word for inactive units is quoted. No finding was edited.*

Reviewer: independent executor, Tue 24 Nov 2026 (ET). Nothing merged, commented or posted.
Head reviewed: `64bb5995fc9cc0ebc22eb3f589790f43add575af` (fresh clone, `<local>/ufr-review/repo`, base main `19b6d0c`, merge-base confirmed `19b6d0c`).
Paper: arXiv:2611.11020v1 fetched fresh (`<local>/ufr-review/paper.pdf`, pdftotext), read independently. Thread posts re-read through the X read tool.

## RESULT: PASS WITH FIXES

Mechanics are clean (hash, files, checks, wording). The paper summary is mostly accurate. There are 5 blockers: two factual/citation errors, one design weakness that Draft A hides, and two lock-text defects. All have small fixes. Because the PR is unmerged and no data exist, the lock-text fixes (B4, B5) can be made now by editing the block and re-hashing. Update the hash in the PR text, `OPEN_WORK.md` (row `UFR-GAPS`) and the draft in the same commit.

## Blockers (numbered, with minimal fixes)

**B1. Gap 3 misattributes Fig 13 (factual error in the note).**
Note, Gap 3 "Observed": "The hand-built UFR networks change most in the first cycles and more slowly afterward (Fig 13 caption)". Fig 13 is a Picbreeder figure (constructed skull/nose targets, 120 cycles, evolved UFR networks; Fig 13 caption, App E). It is not the hand-built illustrative-domain networks. The 20-cycle illustrative result is the Fig 14 caption ("UFR (hand-designed) networks accrue almost no forgetting").
Fix: "The evolved Picbreeder UFR networks change most in the first cycles and more slowly afterward (Fig 13 caption, 120 cycles); the hand-designed illustrative UFR networks accrue almost no forgetting over 20 cycles while SGD networks forget progressively (Fig 14 caption)."

**B2. The capacity-control justification is mis-cited and mismatched to the domain (note §2 "What was known before locking"; Draft A last sentence).**
The note says R replaces parameter count "because the paper's own controls (Fig 11; App C) show that size alone does not track forgetting". Draft A repeats it: "your capacity controls already show size alone doesn't track forgetting".
- Fig 11 (caption) says the opposite within UFR: "Forgetting increases monotonically with free capacity added in every task". It is also Picbreeder, not Abs.
- The evidence that size alone is not the explanation is App H and App C. The distilled GELU students have 87,027 / 138,673 / 453,823 parameters against the 29,120-parameter SGD baseline, and they forget much less on 3 of 4 tasks. SGD with fewer parameters or the evolved topology forgets more (App C, §5.3). Those too are Picbreeder.
- For Abs, the paper says only that larger networks gave no significant benefit to SGD (§4.1).
Fix: cite App H and App C, not Fig 11. Say these are Picbreeder controls, and that size is excluded as a design choice, not as a shown fact for Abs. Suggested wording for the draft: "Parameter count is excluded as the measure: in your GELU-distillation control (App H) networks with 3–15× the parameters forget less."

**B3. The pooled hit criterion can be satisfied by arm differences alone, and Draft A does not say so (check 3).**
- The paper already reports F ordering by arm (Fig 6: SGD forgets most; symmetry-loss and distillation less). It has no R data, so the prediction is not already implied by the paper.
- But a pooled Spearman over three arms of 20 will clear +0.40 if R merely separates the arms in the same order as F, with zero within-arm information. The symmetry loss forces even activations, so it plausibly shifts R by construction.
- The note's S1 rule only makes write-ups say "arm-level association only" after a hit is already declared. Draft A says nothing about it.
- The authors' own camp already holds this idea: Lehman (post 2125322529602666625) describes UFOs as seeking "regular (compressible/low rank) activation patterns", and Sheppard et al. 2611.11862 regularize activations. A pooled hit would not surprise them.
Fix, best (block edit, re-hash): add a stratified criterion to the hit, e.g. a hit needs pooled rho ≥ +0.40 and p ≤ 0.01, and the mean of the three within-arm rhos ≥ +0.20 (or a within-arm-stratified permutation test). Fix, minimum: Draft A must say "pooled across the three arms" and "an arm-level association is reported separately and would be disclosed as such", and the draft should note that the prediction is not unique to GTAO (see N6).

**B4. The locked claim sentence reads backwards (note line 36, inside the locked block).**
"the more redundant the activations a network holds … the more it forgets. 'Redundant' is defined only by R". R is the entropy effective rank. High R means more independent directions used, not more redundancy. Low rank is the compressible/redundant case, as Lehman's post says. The predicted sign (+) is consistent with "excess dimensionality", but the word "redundant" invites the opposite reading from an expert.
Fix: replace with "the higher the effective rank R of the activations a network holds (the more distinct directions they span), the more it forgets. 'Higher rank' means only a larger R." Re-hash. Also change "redundancy" wherever it appears in the PR text, the README entry and the X draft.

**B5. Researcher degrees of freedom remain in the locked block (check 2; each is small, so one fix list).**
a. F's reference is not named. The block says "mean squared error on the held-out half … after the 20th cycle". Add "against the original target T1(x) = |x|, evaluated at the end of cycle 20 after the return-to-T1 step (App A: 'held-out portion of the original function')."
b. The inconclusive clause "or a code error is found" is an escape hatch that can be invoked after seeing a miss. Fix: "a code error counts only if it is established by a check or review fixed before the outcome is computed; any later change is reported alongside the original result, which stays the scored result."
c. The permutation is not bit-reproducible. Unspecified: the pooled order, whether F or its ranks are permuted, and the RNG call. Fix: "pool order = SGD, symmetry, distillation arms, seeds ascending; permute F with `rng.permutation(F)` called sequentially from `numpy.random.default_rng(20261124)`; Spearman via `scipy.stats.spearmanr` (average ranks)."
d. Seed provenance. The note says seeds 0–19 and 100–119 are "disjoint, as the paper does". The paper only says the distillation results use "disjoint RNG seeds" (App A) and gives no numbers. Say "disjoint as the paper does; the numbers are this block's choice." The clause "If the authors' release fixes other seeds" is vacuous because the paper links no code (grep found none). Say so. Also state the PRNG and initializer convention for a re-implementation (the paper says only "Flax library defaults (LeCun-normal)"), and the exact teacher weights/biases for the distillation arm (App A gives the construction only in words).
e. "Equal fit" is a pass/fail threshold, not matching. In my own quick pilot (see below) all SGD-arm nets pass 1e-4 with median MSE ≈ 6e-7, so residual fit differences span orders of magnitude and are not controlled. Fix: add S4, "Spearman between initial-training MSE and F, reported", or call the criterion "a common fit threshold".

## Checks, item by item

### (1) Paper claims (note §1 and §3 "Observed" bullets) vs the paper
Matches the paper:
- Abs setup: |x| ↔ 0.25|x|, even functions on [−1,1], a pure slope change (App A "Target setup details", §4, Fig 3a).
- Architecture: 4 hidden layers × 20 ReLU, scalar in/out, Adam 0.005, full-batch (App A).
- Initial training: 500 iterations, all 101 points, no warmup, no early stopping (App A).
- SGD, symmetry-loss weight 0.25 on all hidden layers, applied only in initial training; distillation weight 0.1, k = 8, ℓ2, teacher = hand-built UFR, all hidden layers (App A).
- Cyclic protocol: 20 cycles, 5 gradations each way plus endpoint = 240 target changes; train x ≥ 0 (51 points), held out x < 0 (50 points); 101-point per-seed draw (50 uniforms in (0,1), their negations, and 0); 20 seeds (App A).
- Metric: "final validation loss after 20 rounds", MSE over the held-out complement (Fig 6 caption, App A). The paper's own words are "final validation loss". Draft A's "final held-out loss" is a fair paraphrase.
- Hand-built UFR: only 2 live units per layer, 18 "dead" (the paper's word, App A).
- Picbreeder and controls:
  - Symmetry loss gave a 47% reduction on Butterfly (fly), §6.2.
  - Distillation helped in 3 of 4 UFR-compatible Picbreeder tasks, §6.2 and Fig 8.
  - SGD baseline chosen by a search over depth, width, optimizer and activation, §5.1 / App C.
  - Evolved topology or fewer parameters forget more, App C.
  - App H GELU copy keeps most of the resistance (but UFR still forgets less on 3 of 4 tasks).
  - Fig 11 added capacity raises forgetting. This is correct as a summary; see B2 for how it is used.
  - Sawtooth (Fig 6) and Skull X (Fig 8) as non-compatible controls.
  - App J: 6/20 fit, 6.1× the reference, p = 0.01; SGD-elaborated 20/20 and 10× more forgetting. The "cost of arriving at 3-Level Abs by elaboration rather than by construction" quote is verbatim.
  - The 1e-4 fit threshold is from App J ("final training loss on 3-Level Abs is below 10⁻⁴").
- "No general way to construct UFR" is §3.4. Paper version and date are right (arXiv:2611.11020v1, 7 Nov 2026).
- Thread quotes verified through the X read tool:
  - Post 2125314236582948960: "We don't have a mathematical definition…".
  - Post 2125322529602666625: "regular (compressible/low rank) activation patterns". Note this is about UFOs, which the note labels "a related method". The label is accurate.
  - Post 2125280932055888237 (identical outputs, different organization).
  - The announcement post is 2125280929967190380, 24 Nov 2026 17:30 UTC (12:30 ET), from Joel Lehman "w/ @kenneth0stanley at @LilaSciences". The note's "Announced by Lila Sciences" is loose; "posted by Lehman (with Stanley, Lila Sciences)" is exact.
Problems: B1 (Fig 13), B2 (Fig 11/App C use). Minor: "(Discussion) the paper does not present a method ready to scale" is a paraphrase. The Discussion says scalable methods are an open direction, and Joel's post calls the Sheppard paper "a step towards scaling UFR". Not wrong, but quote or soften.
Minor omission: Sheppard et al. 2611.11862 (UFOs, Lehman and Stanley co-authors) is the closest prior art to "low-rank activations as the UFR property". The note does not cite it. Add it as related work with one sentence.

### (2) UFR-P1 executable by a third party, hash
- Hash recomputes: the printed command returns `5360c2ba48ca9837cfcdd2bdc8e0f88f954f1753b5abf77746f9c53ad1b4d98f`, equal to the printed hash, to the `OPEN_WORK.md` stub (`5360c2ba…`) and to Draft A's header. The marker pair is unique (3 matches: the prose mention and the two markers).
- Fully specified: grid (201 points, k/100), layers (all 4, post-ReLU), centering (column mean over 201), SVD, effective-rank formula with the zero/threshold rule, the mean over layers, float64, equal-fit threshold, arms and seeds, pooled Spearman with average ranks, permutations (10,000, p = (1+count)/10,001), hit / miss / sign-reversed miss / inconclusive thresholds, S1–S3.
- Degrees of freedom found: B5 a–e. The pooled-vs-arm issue is B3. The wording sign issue is B4.
- Executability pilot (my own numpy re-implementation, App A settings, SGD arm, seeds 0–19, initial training only): 20/20 nets pass MSE < 1e-4 (median 6e-7), and R computes with the printed formula (range ≈ 2.31–2.65). I did not run fine-tuning and did not compute F or any R–F correlation, so this does not test the prediction. It shows the inconclusive thresholds (30 total, 8 per arm) are not binding for the SGD arm. This is a reviewer sanity run, not evidence about UFR-P1.

### (3) Not trivially implied by the paper; arm-level caveat
- Not already in the paper: the paper reports no activation-rank statistic and no per-network F.
- It is partly implied at arm level (B3). The S1 rule is a reporting caveat, not a decision rule, and it attaches only after the hit label. Not adequate as it stands; fix in B3.
- The sample-size remark is correct: SE ≈ 1/√(n−1) ≈ 0.13 at n = 60, so 0.40 is about 3 SE. Within one arm (n = 20) SE ≈ 0.23, so an S1 test has little power; the stratified rule in B3 should use the mean of within-arm rhos, not a per-arm significance test.
- The "hypothesis, not derived" status is stated correctly in the note (§2 "Why this is a hypothesis", §4). The block also correctly bars the hand-built UFR from the scored set.

### (4) Three gaps: labels, cites, overclaiming
- Labels: all three are labeled open, with candidate forms labeled hypothesis. No derivation is claimed. §4 repeats this. The candidate σ²_eff,i = σ²_i + Σ γ_ij u_j and its consequence (T* shortens, hold rule tightens) are correct algebra from `GROK_BOT_MEMORY:54-55`.
- Cites verified on head:
  - `CORE.md:7`, `THEORY.md:30` (κ per nat), `:36` (floor), `:35, 37` (exogenous world, open lever, CX2/CL11), `:41`, `:45-51`, `:166` (N54), `:182` (lump-sum band; CX9 open), `:497` (CT34): correct.
  - `GROK_BOT_MEMORY:42, 54-55, 71, 72`: correct (0.63 → 137% at `:72`).
  - `OPEN_WORK.md:112` (T61), `theory/DYNAMICS.md:43` (CL19), `process/VOCABULARY.md:72`, `litmap/LITMAP.md:204`, `PROCESS.md` §1 item 4, `measurement/FRAMEWORK.md` anti-rescue clause: correct.
  - `theory/LAYER_LIFETIME_2026-11-21.md:51` is the §3b heading; the 0.63/137% numbers are at `:53`. Cosmetic: cite `:51-53`.
  - `MEMORY_MISS_COST_BOUNDS:142` is Proposition 5 (branching-process total progeny). It supports "one wrong item contaminating dependents" only loosely. Say "Proposition 5, `:142`".
- Overclaiming: none found about derivation. The only substantive error is B1. Gap 2's reading of App J (elaboration cost) as evidence about GTAO's redesign cost k is an analogy and is labeled hypothesis; acceptable.

### (5) Wording rules
- No "solved", "theory of everything", "bill", "kill", "dead", "verdict", "puzzle" in the three changed files' added text. "law" appears only inside the hypothesis sentence. That sentence is present byte-identical (exact-string grep count 1, line 5, inside bold).
- Misses are called misses, hits logged, "breach" used for lock edits. Meets `process/PROCESS.md` §2.
- Draft A and B: no banned words; "law" absent.
- Note: `process/PROCESS.md` §2 allows "inconclusive" only as a formal gate status; the block uses it as a logged outcome neither hit nor miss. Acceptable and consistent with `measurement/FRAMEWORK.md`.

### (6) Scope and checks
- `git diff --name-only origin/main...HEAD`: exactly `OPEN_WORK.md`, `applications/README.md`, `applications/UFR_FORGETTING_2026-11-24.md`. `THEORY.md` and `CORE.md` untouched (127 insertions only).
- `tools/check_consistency.py`: PASS (FAIL 0; 3 advisory length warnings, existing). `tools/check_fresh.py`: PASS. `tools/check_open_work.py`: PASS (union missing 0).
- `OPEN_WORK.md` row `UFR-GAPS` is accurate (open, self-check only, needs reviewer). It should be updated after this review: status becomes "independently reviewed, fixes applied" only after the fixes land and a re-check.
- The note's header says "no independent review yet". Update after review, and list this review in the PR.

## Draft A (the X reply draft (not in this repository)) vs the note and paper

Supported: the hash (matches the block); measure/grid/centering/entropy effective rank/mean of four layers; MSE < 1e-4; the three arms with 20 seeds each; Spearman ≥ +0.40; one-sided permutation p ≤ 0.01; signed miss; "protocol unchanged"; "hypothesis, not derived"; "grades a memory by what it costs to hold plus what a wrong answer costs at the moment of use" (`THEORY.md:29-31`); the paper link and note link. Draft A and B both have the right status words.

Flag these lines in Draft A:
1. "Parameter count is excluded, because your capacity controls already show size alone doesn't track forgetting." Unsupported as worded: see B2 (Fig 11 shows the reverse within UFR; the support is App H/C, in Picbreeder). Use the B2 wording.
2. "Prediction: Spearman(R, your final held-out loss) >= +0.40 …" with no statement that the correlation is pooled over three arms, whose F differences the paper already reports (B3). Add "pooled over the three arms; we will also report within-arm correlations".
3. "Anything less is a logged miss, with its signed size." Incomplete: the note also has an inconclusive outcome (fewer than 30 nets, or an arm under 8). Say "a logged miss (or inconclusive if too few nets reach the fit threshold)".
4. "three gaps your paper exposes in our own math". "Exposes" is stronger than the note, which says they are open questions with candidate forms and one of them (Gap 3) cites the wrong figure (B1). Use "points to three open gaps in our own math".
5. "This is a real result, and it exposes a framing problem in the field." The first clause is a judgment I cannot verify from the paper (it is hand-built networks plus evolved Picbreeder networks; the authors themselves call it "evidence for" a hypothesis). Suggest "This is a clean result" or "This is an interesting result". The second clause is an opinion, not claimed by the note; either soften ("suggests") or drop.
6. Link: `…/blob/main/…` points at a moving branch and 404s until merge. A locked prediction should link to an immutable permalink, ideally the merge-commit SHA. After merge, post `…/blob/<merge-sha>/applications/UFR_FORGETTING_2026-11-24.md`. The draft header already says do not post before merge; keep that.
7. Novelty framing: Draft A reads as if the low-rank-activation idea comes from GTAO. Lehman's own thread post and Sheppard et al. 2611.11862 already use low-rank/compressible activations as the target. Add half a sentence: "…close to the low-rank-activation idea in your UFO paper; the contribution here is a locked, checkable test on Abs." That is also honest about prior art.
8. Length: Draft A is about 1,290 characters (about 1,190 with link shortening), so it needs X long-post ability. Confirm the account has it, or use Draft B.
Draft B: reject its second sentence ("Same outputs, very different cost to keep old behavior: that is what you get when a memory is graded only by its fit at training time."). The note does not claim that, and the paper does not say it; it is a causal claim about the field that GTAO has not derived. Draft B also omits the pooled caveat, the fit/size exclusion and the "not derived" wording, and shortens "a hypothesis" to a clause. Prefer Draft A with the fixes above.

## Non-blocking suggestions
- N1. Cite Roy and Vetterli 2007 (EUSIPCO) for the entropy effective rank. The note says no citation was resolved; this is the standard one.
- N2. Add Sheppard et al. 2611.11862 and Brown et al. 2022 (intrinsic dimension of activations; cited by that paper) as related work for the measure.
- N3. Tighten the cite `LAYER_LIFETIME…:51` to `:51-53`.
- N4. "Announced by Lila Sciences": say "posted by J. Lehman (with K. Stanley, Lila Sciences)".
- N5. `MV10` (feasibility gate) applies to causal/optimality-form preregs, not this one; a one-line power note (n ≈ 60 gives SE ≈ 0.13) is already there. Fine.

## What was not independently checked
- I did not watch the paper's explainer video. I did not read the figure images beyond captions (the Fig 6 axis values are not extractable from text).
- I did not run the authors' code (none is linked in the paper). My pilot is a re-implementation and initial training only.
- I did not check `THEORY.md` claims beyond the cited lines.

## Re-check (Tue 24 Nov 2026, after author fixes)

Re-check of head `a018aed8beff5c438a783292cfbab75cd3067d9e` (fresh clone `<local>/ufr-review/repo2`, base and merge-base still main `19b6d0c`). New printed hash `b15887c2288cb32d61d41ca29f7ef252b21c41153d7bf7e98e6d7a8bfeb56dff`. Revised Draft A read from the X reply draft (not in this repository). Nothing merged, commented or posted; the PR was not edited by this reviewer.

### RESULT: PASS

All five blockers are resolved, and every previously flagged line in Draft A is now supported by the note. Residuals below are nits, not blockers.

### Hash, scope, checks, wording
- The printed command on the new head returns `b15887c2288cb32d61d41ca29f7ef252b21c41153d7bf7e98e6d7a8bfeb56dff`. That value is in the note (line 82), in `OPEN_WORK.md` row `UFR-GAPS` (full 64 hex, not the old stub), and in Draft A's header. The old hash `5360c2ba…` is gone from those files.
- `git diff --name-only origin/main...HEAD`: still exactly `OPEN_WORK.md`, `applications/README.md`, `applications/UFR_FORGETTING_2026-11-24.md` (139 insertions). `git diff origin/main -- THEORY.md CORE.md` is empty.
- `tools/check_consistency.py`, `check_fresh.py`, `check_open_work.py`: all PASS (consistency has the same advisory length warnings as before; open-work union missing 0).
- Hypothesis sentence remains byte-identical (one occurrence, line 5). No "solved", "theory of everything", "bill", "kill", "dead", "verdict" or "puzzle" in the three files. "law" appears only inside that sentence. "redundant" / "redundancy" are gone.

### Blockers 1–5
**B1 (Fig 13 / 14). Resolved.** Gap 3 now says the evolved Picbreeder UFR networks change most in the first cycles and more slowly afterward (Fig 13 caption, 120 cycles), and that the hand-designed illustrative UFR networks accrue almost no forgetting over 20 cycles while SGD networks forget progressively (Fig 14 caption). Rechecked against the paper: Fig 13 is the constructed Picbreeder targets, 120 cycles, "UFR changes most in the first cycles and more slowly afterwards"; Fig 14 is the illustrative domain, "UFR (hand-designed) networks accrue almost no forgetting over the 20 cycles, whereas the from-scratch SGD networks forget progressively."

**B2 (capacity-control cite). Resolved.** The locked "What was known" paragraph now treats size as a design choice, not a shown fact for Abs; cites App H and App C (Picbreeder); and correctly says Fig 11 is a Picbreeder result whose caption has forgetting increasing with added UFR capacity. Section 1 now lists the App H counts: 87,027 / 138,673 / 453,823 against a 29,120-parameter SGD baseline, less forgetting on 3 of 4 tasks. Rechecked in App H: "The student has 87,027 (skull), 138,673 (butterfly) and 453,823 (apple) trainable parameters, notably more than the 29,120 of the SGD baseline"; "The student forgets much less than SGD on three of the four tasks" (Apple not significant). Draft A uses the same App H wording. The "3–15×" shorthand is a slight rounding (exact ratios 2.99×, 4.76×, 15.58×); see residual R1.

**B3 (arm-level hit). Resolved.** The hit rule now requires all three of: pooled rho ≥ +0.40, permutation p ≤ 0.01, and mean within-arm rho ≥ +0.20. The block states why: the paper already reports that F is ordered by arm (Fig 6), and clause (iii) stops a between-arm-only association from counting as a hit. S1 now prints all three within-arm rhos, which also enter the hit rule. Draft A states the pooled correlation, the 0.20 mean, and "so arm separation alone cannot count as a hit." The choice of a mean rather than a 2-of-3 sign count, and the 0.20 threshold as about one within-arm SE, are disclosed judgments. No new freedom in the rule as written; one edge case is noted as residual R2.

**B4 (backwards "redundant"). Resolved.** The locked claim now reads: "the higher the effective rank R of the activations a network holds … (the more distinct directions they span), the more it forgets. 'Higher rank' means only a larger R." Predicted sign is unchanged and consistent with that wording.

**B5 (researcher freedoms). Resolved.**
- (a) F is now "MSE against the original target T1(x) = |x| … at the end of cycle 20 after the return-to-T1 step," with the App A phrase.
- (b) A code error is inconclusive only if a check or review fixed it before any F is computed; later changes are reported alongside the original scored result.
- (c) Pool order is fixed (SGD, then symmetry, then distillation, seeds ascending, failed-fit nets omitted). F, not R, is permuted. Generator is `numpy.random.Generator(numpy.random.PCG64(20261124))`, with no other draw from that rng, 10,000 loops, `rng.permutation(F)`, `scipy.stats.spearmanr(..., nan_policy="raise").statistic`, p = (1+count)/10001. Midrank ties are SciPy's default. I confirmed this permutation stream is bit-stable across two fresh Generators.
- (d) Seeds 0–19 and 100–119, and the input-draw PRNG (`PCG64(s).uniform(0, 1, 50)`), are labeled this block's choice. The paper's "disjoint RNG seeds" wording is quoted, and the block says there is no authors'-release seed list and that the paper links no code. Flax `lecun_normal` / `PRNGKey(s)` is specified; other libraries must log the seed-to-stream mapping before any outcome. The teacher is specified from App A in words, must have MSE 0 on T1 on both the 101-point set and the 201-point grid, and any leftover factorization (signs, scales, live indices) must be logged before any outcome. That last clause is a disclosed residual, not a new freedom (R3).
- (e) The criterion is now called a common fit threshold, not a matching of residuals. S4 reports Spearman(initial-training MSE, F).

### Draft A items
1. Size exclusion now cites App H, "networks with 3–15× the parameters forget less." Supported (rounding at R1).
2. Pooled over the three arms, plus the mean-within-arm ≥ +0.20 condition, is in the draft and in the hit rule.
3. Inconclusive if too few nets reach the fit threshold is in the draft.
4. "three open gaps this paper points to in our own math" matches the note; "exposes" is gone.
5. Opening is now "This is a clean result, and it suggests a framing problem." Supported as a softened judgment, not as a derived claim.
6. The URL is `…/blob/{MERGE_SHA}/applications/UFR_FORGETTING_2026-11-24.md`. The header says not to post until a re-review and merge, then replace the placeholder with the merge-commit SHA.
7. Prior framing: "close to the low-rank-activation idea already in your UFO paper (Sheppard et al., arXiv:2611.11862) and in Lehman's remark on compressible, low-rank activations; the contribution here is a locked, checkable test on Abs." Rechecked: arXiv:2611.11862v1, submitted 9 Nov 2026, Sheppard, Albalak, Lehman and Stanley, *Are UFOs Real? Introducing Unified Factored Organizers*. The abstract (re-fetched) says UFOs "model regularities in the representations of other neural networks" and are used as a regularizer; it does not itself use the words "low rank." The "compressible/low rank activation patterns" wording is Lehman's, post 2125322529602666625, describing UFOs. The pairing in the draft is fair, given that post and the note's own "authors' camp" sentence. The note cites the abstract as fetched, not read in full, which is accurate.
8. Draft A is now about 1,775 characters, so it still needs X long-post ability (R4). Draft B is withdrawn, as recommended.

All testable claims in Draft A (measure, grid, centering, effective rank, mean of four layers, common fit threshold 1e-4, three arms with 20 seeds, T1 = |x| after cycle 20, pooled Spearman ≥ +0.40, p ≤ 0.01, mean within-arm ≥ +0.20, signed miss, inconclusive, App H size exclusion, hypothesis / not derived, GTAO cost-to-hold-plus-loss-at-use, hash, permalink) are supported by the locked note.

Non-blocking suggestions N1, N3 and N4 from the first review are now in the note (Roy and Vetterli 2007, no DOI; `LAYER_LIFETIME…:51-53`; "Posted by J. Lehman (with K. Stanley, Lila Sciences)"). N2 is partly done (Sheppard et al. is in; Brown et al. 2022 is still absent, and is still optional).

### Residuals (not blockers)
- **R1.** "3–15×" is a rounding of 2.99×, 4.76× and 15.58×. Exact counts are already in the note. No change required.
- **R2.** `scipy.stats.spearmanr(..., nan_policy="raise")` does not raise when an input is constant; it returns NaN and a `ConstantInputWarning` (checked on SciPy 1.18.1). If one arm has constant R or constant F, `rho_within` is NaN and `rho_within >= +0.20` is False, so the literal path is a miss. A third party could instead call that inconclusive. If this is ever amended, say in the block: a NaN `rho_arm` makes the result inconclusive. Not required for a pass, and not a free choice under the literal Python.
- **R3.** The teacher's signs, scales and live-unit indices remain a logged, pre-outcome choice, because App A gives no numerical table. Disclosed; a later run should paste that log.
- **R4.** Draft A is long. Confirm the posting account can send a long post, and replace `{MERGE_SHA}` only after merge.

No remaining blockers.
