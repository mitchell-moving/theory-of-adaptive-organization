# What next on the P1 line, chosen by the theory's own judgment rule

*Thursday 26 November 2026, about 22:55 EST. Chad t188u (22:50 EST): "Apply judgement yourself per the theory … don't be myopic and don't throw the baby out with the bath water." The hold is lifted for the P1 line only. Local note; nothing committed, pushed, emailed or posted. THEORY.md and CORE.md not edited.*

**Labels:** observed · hypothesis · proved-in-model (PIM) · known · elementary. **Every number in the scoring table below is my own prior (hypothesis).** The weights and the attention price are free prices in the sense of W2, so they are stated and their sensitivity is given.

## 1. The rule, as the repo writes it

- THEORY.md §3 (master equation): a system chooses its design to minimize J = κ·I_mem + h·K (holding memory) + w·E[ℓ] (being wrong or late) + A + L (acquiring and sharing information), subject to P(ruin) ≤ ε_r.
- Hold rule (`applications/GROK_BOT_MEMORY_2026-11-23.md` §4 rule 1, as used in `rnd/context/WORKING_CONTEXT.md` §0): hold an item only when stake × need beats upkeep. Re-check when drift is high; fade low-need items to pointers.
- Applied to choosing a route: the **stake** is the peak question; **need** is the chance the route returns something that can fail and is not already known; **upkeep** is the hours (attention) plus the usage it burns. Ruin cap here: the weekly usage ease-up line at 92% (now about 83%), so a route that would need more than about the 6 h budget is over the cap.

## 2. The stake: the peak question, split

Q = "Does judgment emerge from below and nest across scales?"
- **Qe (emergence), weight 0.6:** at the one boundary where physics has a real selection without heredity (the sieve), does a judge (a record, an action from it, anticipation) arise by selection alone, without being built in, and only under the conditions the theory names (heredity, drift that a record can follow, a first nat that pays)?
- **Qn (nesting), weight 0.4:** does the same pattern repeat level on level with a scale-free signature?

The 0.6/0.4 split is mine (hypothesis). Qe is weighted higher because Chad's correction (t183u) puts judgment, not nesting, at the core, and because nesting presupposes something that judges.

## 3. Scoring (all numbers are priors; EIV in bits on Q)

EIV = p · B_open + (1 − p) · B_known, where p = chance of a result that can fail and is not already known, B_open = bits moved on Q if so (weight × relevance × outcome entropy), B_known = bits if the outcome turns out fixed or known. Hold price λ = 0.02 bits/h (free price; see §5).

| route | p | B_open | B_known | EIV (bits) | hours | EIV/h | walls risked | prior art that lowers p |
|---|---|---|---|---|---|---|---|---|
| **P1-S** selection of heritable linear controllers in a dephasing oscillator with a drifting force; heredity-off and reading-off nulls | **0.40** | 0.48 | 0.05 | **0.22** | 4 | **0.056** | W12 (selection ranks; the cost's terms are inputs, accepted, not tested); W13 (the capacity to judge is given as a generic linear memory; heredity imposed in the main arm, so tested by a null); W10 (drift is a premise, used to make a prediction, not escaped); W3 (Hilbert space, bath) | Kussell & Leibler 2005 (sensing vs bet-hedging; when information pays); Tagkopoulos et al. 2008 and Mitchell et al. 2009 (observed anticipation in microbes); quantum LQG (Doherty–Jacobs 1999; Wiseman–Doherty 2005) |
| P4 prebiotic anticipation (RAF chemistry) | 0.30 | 0.48 | 0.08 | 0.20 | 12+ | 0.017 | W12, W14; over the usage cap | Kauffman; Hordijk–Steel; Vasas et al. 2012; England |
| SE4(iii) wording fix (draft only; no PR under the hold) | 0.00 | — | 0.02 | 0.02 | 0.25 | 0.08 (tiny absolute) | none | — |
| P3 nesting as a renormalization map vs Lera–Sornette's 3–4 | 0.10 | 0.32 | 0.03 | 0.06 | 4 | 0.015 | W2; and a **recorded open miss**: `theory/layer-fixed-point-2026-11-23/MEMO.md` (24 Nov) ran the CT34 fixed point and scored BROKEN; its rate depends on mode order and b | Lera & Sornette 2019 (PLOS ONE, doi 10.1371/journal.pone.0214911); Wilson–Kogut |
| P1-T task-set optimum separating from the medium's symmetric point | 0.10 | 0.12 | 0.02 | 0.03 | 2 | 0.015 | W2; H1/F1 again in a quantum class | Dalvit–Dziarmaga–Zurek 2005 (short horizons favor x-squeezed states) |
| Stop | — | — | — | 0 | 0 | 0 | — | — |

Notes on the numbers:
- **P1-S p = 0.40, not higher**, because selection finding a good linear controller is close to known (a genetic search), and when information pays is known in kind (Kussell–Leibler). What is not known, as far as this search found: whether, with fitness = survival under priced reading and a ruin edge only (no loss term, no reward for prediction), the memory comes to hold information about the **future** force beyond what the body already carries; whether that needs heredity; and whether **record heredity** (passing the memory to offspring), left free to evolve, rises only when the world's drift outlasts a generation. The last two can come out either way.
- **P3 p = 0.10** because the repo already ran its nearest version and the miss is open (a W-list gap: that miss is not in WALLS.md; flagged here, not added).
- **P4** is the closest to Chad's "molecules come to anticipate", but it costs more than the budget, and P1-S's result is a prerequisite for designing P4's nulls honestly.

## 4. Decision

**Run P1-S** (EIV 0.22 bits, 0.056 bits/h; the only route above λ with real information on Qe). Fold the SE4(iii) wording draft into the result note (15 minutes; it scores high per hour but moves almost nothing). Defer P3 (recorded open miss) and P4 (over the cap; P1-S designs its nulls). P1-T is dropped.

## 5. Sensitivity (the price is free, so show it)

P1-S stays first for any λ ≤ 0.05 bits/h, for Qe weight from 0.3 to 0.9, and for its own p down to 0.15 (EIV/h at p = 0.15: (0.15·0.48 + 0.85·0.05)/4 = 0.029). It loses first place to "stop" only if λ > 0.056. It loses to P4 only if P4 could be done in ≤ 3.6 h, which it cannot.

## 6. What carries forward from P1 (the baby, not the bath water)

| P1 finding | how it enters P1-S |
|---|---|
| The sieve and the judge are different (no record, no choice, no heredity vs record + action) | Operational split: a **sieve** population cannot read (k = 0) or cannot inherit; a **judge** population reads, acts on its memory, and inherits. Same prices, same world |
| Symmetry: over whole periods every quadratic loss picks the coherent state, from the oscillator's rotation, not from the cost | Births start in the coherent state (the sieve's state is given, not claimed as selected). No credit is taken for "recovering ZHP" |
| Kalman / W10: records and anticipation pay only under drift a record can follow, with a correlation time longer than the record's lifetime | Turned into a prediction: two worlds, persistent drift (τ_f = 30) vs fast drift (τ_f = 0.2). Record heredity should rise only in the first |
| Zero-action limit: the cost's high-price limit is the sieve | A high-price arm: reading should evolve to zero, leaving the sieve state |
| The judge must not be true by assumption (W12/W13) | Fitness has no loss term and no reward for prediction or for heredity. The controller is a generic 3-variable linear memory, not a Kalman filter. Heredity has an off-switch null; record heredity is an evolvable gene, not imposed |

## 7. SE4(iii) wording draft (proposal only; for Ace; not a PR)

SCALE_ENDS SE4 test (iii) now reads "a non-hereditary, non-learning structure whose design sits measurably nearer a GTAO optimum than unselected controls". The P1 desk check (`desk_check_symmetry.out`) shows a decohered oscillator meets this for free, because the oscillator's own symmetry makes the coherent state the optimum of every period-averaged quadratic loss. Proposed wording: "… nearer a **task-set** GTAO optimum **that differs from the optimum fixed by the medium's own symmetry** than unselected controls". Status: proposal; N28 stays OPEN; CLAIM_MAP untouched.

## 8. Sources (Crossref-checked: `crossref.out`, `crossref2.out`)
Kussell & Leibler 2005, Science 309, doi 10.1126/science.1114383 · Tagkopoulos, Liu & Tavazoie 2008, Science 320, doi 10.1126/science.1154456 · Mitchell et al. 2009, Nature 460, doi 10.1038/nature08112 · Wiseman & Doherty 2005, PRL 94:070405, doi 10.1103/PhysRevLett.94.070405 · Lera & Sornette 2019, PLOS ONE 14, doi 10.1371/journal.pone.0214911 · plus the P1 table in `P1_PRIOR_ART_AND_STOP_2026-11-26.md` §1.
