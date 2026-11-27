# P4c results: heredity vs novelty, and a gate that did not pass

*Thursday 26 November 2026 (EST). Rules: SWEEP_AND_RULES_P4c_2026-11-26.md (SHA-256 f784fcc384bd7ad04a49aa311508d58b307b3042e181d30c3512decf30f4a961, hashed before the sweep). Outputs: sweep.out, sweep.csv, gate.out. In-model only, for a toy with lumped cores. No test was run and no prereg was locked, because the pre-stated gate rule stopped it.*

## Finding 1: the κ-vs-switching tradeoff (observed in-model, pilot seeds 101–103)
- **New heritable states do arise.** Once the incumbent core can be crashed below one molecule, stochastic nucleation from food-set side reactions (rate μ) re-seeds a random core. Switching then happens. It requires deep crashes (τ ≥ 2; at τ = 1 switching is ≈ 0 for every β, M and μ) and is helped by small molecule counts (M 20 > M 200 at τ 2).
- **The tradeoff is smooth and monotone.** Median κ falls as switching rises: switch 0.002 → κ 0.996; 0.02 → 0.97; 0.05–0.07 → 0.90–0.93; 0.11–0.14 → 0.82–0.86. Roughly κ ≈ 1 − 1.3 × switch over this range.
- Cross-inhibition β (1.1 to 3) barely mattered. Crash depth τ and nucleation rate μ set the rate.
- 26 of 54 cells fell in the band (κ ≥ 0.5 and switch ≥ 0.002). The sweep never reached κ < 0.8, so the low-heredity side of an error threshold was not sampled at μ ≤ 0.1.

## Finding 2: the gate did not pass
The pre-stated rule took band cells in descending switch order. The top three were (β, M, τ, μ) = (3, 20, 3, 0.1), (1.5, 20, 3, 0.1) and (3, 200, 3, 0.1), with switching 0.11–0.14 and κ 0.82–0.84.
- In all three, even a reader **present at start** did not pay: reader 0.23–0.28 and hedger 0.19–0.25 in every seed, 0/5 each.
- All four cores sit near 0.25. That is mutation–selection balance at about uniform: identities turn over faster than the reader's edge can accumulate.
- Per the rule, **no regime passed, so the test was not run.** Predictions (i)–(iii) remain unscored. Nothing is claimed for them.

## Hostile review
1. **My selection rule was the flaw.** Picking the *highest*-switch band cell aimed the gate straight at the high-error edge. P4b's world (τ 2, switching about 0) let the reader pay. The result is consistent with an error-threshold shape: the reader pays at low switching and not at about 0.12. But that is two points from different setups, **not** a test of (iii).
2. **The gate used T = 1500,** the same as the sweep. A longer run might reveal a weak edge. The rule fixed T in advance, so it is not changed after the fact.
3. **Why the reader fails at τ 3 is a hypothesis:** each crash may reset most compartments regardless of detox, so the reader's protection is overwhelmed. That was not measured.
4. **Lumped toy cores and one model structure;** the switching mechanism (one-molecule nucleation) is a design choice.

## Plain-words meaning (M1)
- **In-model:** heritable states and new ones trade off along a single smooth curve. More novelty means less faithful inheritance (κ ≈ 1 − 1.3 × switch).
- **At the novelty-rich end of what was swept (about 1 identity change per 8 divisions),** even a ready-made timed reader cannot spread over an untimed hedger.
- **At the faithful end (P4b),** it can spread, but nothing new arises.
- **Whether there is a middle band where a reader both arises and spreads** is still open. It is the obvious next test. Consistent with Eigen 1971 (doi 10.1007/BF00623322) in shape only: too much novelty erases what selection builds.

## Suggested P4d (not run)
- **Main test:** make the transect itself the test. Use the reader-absent start, fixed τ 3, M 20, β 1.5, and μ ∈ {0.001, 0.003, 0.01, 0.03, 0.1} (switching about 0.004–0.13). Run 10 fresh seeds per level, T 3000.
- **Controls at every level:** a no-cue drift baseline, heredity-off, random cue, and high price.
- **Predictions:** an interior μ maximizes reader spread above the drift baseline; at that μ the reader appears in ≥ 8/10 seeds and beats hedger, heredity-off, random-cue and high-price runs (Mann–Whitney p < 0.05).
- **Estimated cost:** about 250 runs, a few minutes of compute.
