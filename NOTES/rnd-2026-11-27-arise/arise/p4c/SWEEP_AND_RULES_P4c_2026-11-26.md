# P4c sweep spec and selection rules (hashed before the sweep ran)

*Thursday 26 November 2026 (EST). Model p4c_model.py SHA-256 4c278c9d6550ea9d523df5d3742a33824288ef5407fa7ac1ebb60a985d13b41e; sweep.py SHA-256 e9ad182cea210e37e81783a4e439ed0998eedcba4646cc94ff03c2f096a73671. Prior art for (iii): Eigen 1971, Naturwissenschaften 58, doi 10.1007/BF00623322 (Crossref-verified, crossref_p4c.out). Error threshold: heredity fails above a critical copying-error rate.*

**Model change from P4b.**
- Spontaneous ε is set to 0. The only source of new core material is stochastic nucleation: at rate μ per compartment-time, one molecule (1/M) of a uniformly random core appears, from food-set side reactions.
- The reader core is absent at start (its column is zeroed in the random mixtures).
- Everything else is as in P4b: Lotka–Volterra cross-inhibition β, Poisson split with M molecules, toxin crash τ, hedger present, price per nat, and fitness = growth only.

**Disclosed smoke run** (seed 999, T 600, β 1.5, M 200, τ 2, μ 0.01): κ 0.998, switch 0.001, reader first seen at t 53, reader frequency 0.118, hedger 0.50.

**Sweep.**
- Grid: β ∈ {1.1, 1.5, 3} × M ∈ {20, 200} × τ ∈ {1, 2, 3} × μ ∈ {0.001, 0.01, 0.1}.
- Pilot seeds 101–103, T 1500, cued world P 40, c_nat 0.01.
- It writes only the median κ and switch rate per division. Reader outcomes are not recorded, so choosing the regime cannot peek at them. The κ-vs-switch scatter (sweep.csv) is reported as a finding.

**Pre-stated rules.**
1. **Band:** median κ ≥ 0.5 and median switch ≥ 0.002 per division (lineage-generation).
2. **Operating regime:** the band cell with the largest switch rate, ties broken by larger κ.
3. **Gate at that regime:**
   - Pilot seeds 101–105; the same random-mixture start as the test, but with the reader *present* (it shows the reader pays once it exists); hedger present.
   - Pass: reader ≥ 0.3 and ≥ hedger + 0.1 in ≥ 4/5. Validity: the random cue passes ≤ 2/5.
   - If the gate fails or is invalid, try the next band cell in order, at most 3 cells. If none passes: report that no regime with both heredity and novelty lets a reader pay, and run no test.
4. **(iii) transect:** at the chosen (β, M, τ), μ ∈ μ* × {0.01, 0.1, 1, 10, 100}.
5. **If the band is empty:** report the tradeoff and stop.
