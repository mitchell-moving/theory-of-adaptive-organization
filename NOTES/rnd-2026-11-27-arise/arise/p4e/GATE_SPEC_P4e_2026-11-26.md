# P4e gate specification (hashed before the gate ran)

*Thursday 26 November 2026 (EST). Model p4e_model.py SHA-256 94342d4d9e3dea2eae3c3a247b28366da85143706386b670c3bf0e9802ba2e1b; gate.py SHA-256 6dab10f80f696cde0aeaee576f7131566b79eb6d25520e38deec37eba1b7d7e2.*

**Model (open-ended).**
- Each compartment has 4 slots, competing Lotka–Volterra (β 1.5).
- Nucleation (rate μ) writes one molecule of a **new** core with random inherited (lag ∈ {none, 0..15}, read strength θ ∈ U[0, 0.6]) into the emptiest slot. No reader is written in. The start is all zero-read cores.
- Signals: a cue pulse comes 6 time units before each toxin onset (toxin interval P 40, length 5, crash τ 3, M 20). A core with lag l diverts θ of its synthesis to detox during [l, l+4) after the last cue.
- **Price per nat:** c_nat · (θ/0.6) · h(duty). This is a *linear proxy* that ties information bought to read strength. It is not a measured mutual information, which is disclosed.
- Fitness = growth only.

**Disclosed smoke run** (seed 999, T 600, μ 1e-3): MI 0.008, read effort 0.048, growth 0.053.

**Gate.**
- Contest: 100 compartments with a lag-l core (θ 0.3) vs 100 with zero-read cores; μ 0, heredity on, cued world, T 1500, pilot seeds 101–105, l ∈ {0, 2, 4, 6, 8, 12}.
- A lag passes if its frequency is ≥ 0.75 in ≥ 4/5 seeds. **L_inf** = the passing lags, which is the pre-stated "informative set" for the test.
- Validity: at the best passing lag, the random cue must pass ≤ 2/5.
- If no lag passes, or the gate is invalid: report that the first nat does not pay in this open-ended world, and run no test.
