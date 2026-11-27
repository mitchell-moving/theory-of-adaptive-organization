# P4b gate specification (hashed before the gate ran)

*Thursday 26 November 2026 (EST). Model `p4b_model.py` SHA-256 7ae073318791b1622c5987f7ceffa9d0d71ea27ae1736ae0e7337a0eae905304; gate `gate.py` SHA-256 463fe7e32a53177dbdbd60de35cd293a789842df047d2a5005ce221669c62e42.*

**Model, and what each P4 review fix became**
- **Fix 2, exclusive cores.** Four lumped autocatalytic cores per compartment compete Lotka–Volterra style, with cross-inhibition β = 1.5 > 1. That makes them mutually exclusive: alternative stable states. Core switching can come only from small-number noise at division (Poisson split, 200 molecules per unit) or from a toxin crash that drops the incumbent toward the spontaneous floor. Nothing forces it.
- **Fix 3, same start.** Gate and test both start from random Dirichlet mixtures. No designed lineages.
- **Fix 4, clean null.** Heredity-off keeps the chemistry and the amounts but randomly permutes core identities in each daughter.
- **Fix 5, non-saturating measures.** Per-compartment core identity (one core ≥ 0.8 of core mass, otherwise "mixed"); Cohen's κ between the parent's identity at division and the daughter's identity at its own division; switching rate. A 50/50 mixture counts as mixed and cannot pass as a reader.
- **Fix 6, price per nat.**
  - The reader core pays c_nat × h(duty) nats per unit time as extra decay, where h is the binary entropy of the cue's duty cycle.
  - That is the per-sample mutual information of a perfect reader of a binary cue, an upper bound, charged whether or not the cue helps. It is not the cue's entropy rate.
  - The hedger reads nothing and pays nothing.
- **Roles.** Core 0 = hedger: always diverts θ·duty of its synthesis to detox D. Core 1 = reader: diverts θ to D while the cue is on. Cores 2 and 3 are plain.
- **Toxin and fitness.** A toxin pulse (length 5, jittered mean interval P) raises every core's decay by τ/(1 + D/D_k). Fitness = compartment volume growth only, which is proportional to core mass. No term rewards reading, anticipation or heredity (W12/W13).

**Disclosed smoke runs** (seed 999, T = 600, engineering only):
- Lognormal split: reader 0.34, hedger 0.02, κ 1.0, switch 0.
- Poisson split, M = 200: reader 0.12, hedger 0.29, κ 1.0, switch 0.
- Poisson split, M = 50: reader 0.43, hedger 0.23, κ 1.0, switch 0.
- M = 200 is now fixed. At τ = 1 a crash leaves the incumbent above the floor, so switching may stay at 0. τ = 2 is in the grid; τ was not tuned beyond that.

**Gate**
- **Grid:** τ ∈ {1, 2} × P ∈ {20, 40} × c_nat ∈ {0.01, 0.05}. Pilot seeds 101–105, T = 1500.
- **Pass:** reader frequency ≥ 0.5 and ≥ hedger frequency + 0.1 in ≥ 4/5 seeds.
- **Choice:** the largest c_nat, then the smallest τ, then the largest P (the least reader-friendly passing world).
- **Validity:** at the chosen cell, the random-cue world must pass in ≤ 2/5, or the gate is invalid. If no world passes or the gate is invalid, the test is not run.
- **Design choice that limits a pass:** the toxy world and the reader/hedger chemistry are hand-written, and the world is chosen from those where a reader can win. Prediction (ii-a) is therefore largely gate-implied.
