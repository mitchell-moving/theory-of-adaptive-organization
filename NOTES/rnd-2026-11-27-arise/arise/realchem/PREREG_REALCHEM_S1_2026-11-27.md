# REALCHEM-S1 preregistration: heredity vs novelty with published PEN kinetics

*Locked Friday 27 November 2026 (EST), before the main run. Script pen_s1.py SHA-256 e158e149ed0171d3c76d119583b5a5c6eee445c4a7c27e90f33bb7f46c92326b. One run; seeds 1–3 per cell. Chad t196u.*

**System.** A cross-inhibited pair of PEN-toolbox autocatalytic templates, a bistable "switchable memory" of the kind built by Padirac et al. 2012 (doi 10.1073/pnas.1212069109).
- All kinetic constants come from Montagne et al. 2011, Table 1 (doi 10.1038/msb.2010.120), read from the PMC full text tonight, with the row labels checked against the table images:
  - k_a = 26×10⁶ M⁻¹min⁻¹; k_d^α = 2.3 min⁻¹; k_d^(Inh/T1) = 0.0057 min⁻¹;
  - polymerase 17 and strand-displacing polymerase 6.9 min⁻¹; nickase 3.0 min⁻¹;
  - exonuclease: 0.32 min⁻¹ for triggers, 1.2 min⁻¹ for inhibitors.
- The erratum (doi 10.1038/msb.2011.12) does not touch Table 1.
- Template 60 nM, as in Montagne's T1.
- **Model reductions (disclosed):** quasi-steady template occupancy; first-order enzymes, so there is no enzyme saturation or competition (the Michaelis constants are in the supplement, which was not read); one k_a for all pairs.

**Disclosed engineering checks before the lock.**
1. The first bistability test was flawed: it seeded the other trigger at 0, so plain independence counted as bistability. I fixed it by seeding the other trigger at 1 nM.
2. With the fix: the inhibitor template at T_i = 0 is **not** bistable; T_i = 1, 3, 10 and 30 nM are all bistable. The pre-stated rule takes the smallest, T_i = 1 nM.
3. A timing run (V 10 fL, 2 passages, seed 999) took 0.2 s; no outcomes were looked at.

**Run.**
- 200 droplets, 40 passages of 60 min each.
- At each passage, molecules are split binomially into halves and refilled with fresh mix; daughters of random droplets fill the slots. This is neutral passaging, with no selection.
- Intrinsic noise by tau-leaping at droplet volume V ∈ {0.1, 0.3, 1, 3, 10} fL.
- Leak (untemplated trigger synthesis; **not published**) ∈ {0, 1e-3, 1e-2} nM/min.
- Identity: a state is A (or B) if its trigger is > 50 nM and > 10× the other trigger; otherwise "mixed/none".
- κ: parent's identity at the split vs the daughter's at the end of the next passage, scored over the last 20 passages.
- Switching rate: share of A↔B changes among those pairs.
- Each cell is scored on its median over seeds 1–3.

**Predictions** (these map the toy's heredity–novelty axis onto droplet size).
- **R2:** κ ≥ 0.9 at every V ≥ 1 fL, for every leak.
- **R3:** the novelty band is non-empty: some (V, leak) has κ ≥ 0.5 and switching ≥ 0.002 per passage.
- **R4:** at leak 1e-3, switching is non-increasing in V.
- **Miss:** R3 empty. That would mean that, in real PEN kinetics, droplet size gives either faithful heredity or none, with no window for novelty, so the toy's band would have no physical counterpart here.

**Status.** In-silico with published constants for the core switch only. The reader, toxin and price parts of the P4 rule are not in this run: no published kinetics exist for a cue-gated reader template, and the enzyme-load price needs the unread saturation constants. No physics claims.
