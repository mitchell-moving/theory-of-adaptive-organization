# M4 desk check preregistration: is locality created by selecting links, or inherited from the world?

*Locked Friday 27 November 2026 (EST), before any run. Script m4_desk.py SHA-256 9bbaf48b9f783ec2b717a1b812aeda1cc18d1c88577d8f293a0e824cf51bbad0. Prior art (Crossref-verified, crossref_m4.out) is in DESIGN_PASS_M4_2026-11-27.md. Seeds 1–3 for the graph search; 101–103 for the hidden positions. One run.*

**Model.**
- 144 judges; cost J = L·(number of links) + w·Σ need_ij·hops_ij (link upkeep plus lateness), with L = 40 and w = 1.
- Greedy search: toggle a random link and keep the change if J does not rise, 6000 steps.
- Start: a ring plus random chords. No positions enter the cost except through need.
- Two worlds with the same total need: (a) **uniform** need; (b) need = exp(−distance/0.08) from **hidden 2D positions**.

**Estimator validity (pre-stated).** d_s comes from the lazy-walk return probability, fit over t ∈ [4, 40]. It is valid only if a 12×12 grid gives d_s ∈ [1.5, 2.5]; otherwise nothing is scored.

**Predictions** (the wall "locality stays an input", in-model). Each must hold in 3/3 seeds:
- **D1:** uniform need gives no low-dimensional locality: diameter ≤ 4 and d_s ≥ 4.
- **D2:** hidden-2D need gives a low-dimensional graph: d_s ∈ [1.5, 3.0].

If D1 fails (a finite low dimension arises from uniform need), that would be evidence that locality can come from the cost. That is the outcome GTAO would need for M4.

**Status.** This is a desk check of a recorded wall, not a new result. Known in kind: spatial network structure follows from distance-dependent costs (Barthélemy 2011).
