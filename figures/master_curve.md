# The master picture: one cost of judgment, in time and in space

`figures/master_curve.png` (16:9), drawn by `figures/master_curve.py` from `figures/master_curve_math.py` and `figures/master_curve_params.py`. Every plotted or printed number is recomputed by `figures/master_curve_checks.py` (run at `nice -n 19`; 40 checks, FAILS 0). Drawn 22 November 2026 from `main` at `5c36ee4`. `THEORY.md` is not edited. The hypothesis sentence is copied byte for byte and checked against README, CORE, and THEORY.

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

## What the picture says

The physics-grounded cost is heat plus a stake on the error, with a ruin cap beside it. In the worked class (equilibrium Ornstein–Uhlenbeck signals, mean-square error, a memory that does not move its signal), the minimum of that cost depends on one number, x = w·v/(kT·a): stake times signal variance over temperature times the signal's rate. In those units every time scale of every world in the class lands on one curve: below x = 1 no memory pays; above it a memory pays and its error falls as v/√x; nothing in the class sits below the curve. A ladder of time scales is a row of points on that curve, and the ones past x = 1 each get a store. Space adds two results: when a decision combines items, one shared (holographic) memory is on the curve while separate copies sit above it; on a Gaussian field the heat scales with the volume unless the decision names a cut, and then it scales with the cut. Where real strongly selected systems sit relative to this curve is the hypothesis, and no system has been placed.

## The collapse (worked class only)

From `theory/GENERAL_FORM_PHYSICS_2026-11-22.md` §5 (lines 84–87): blind when w ≤ kT a/v, cost wv; otherwise cost 2√(kT a v w) − kT a at error √(kT a v/w). Dividing by kT a, with x = wv/(kT a): J*/(kT a) = x for x ≤ 1 and 2√x − 1 for x > 1; the error is v/√x. The per-mode ladder count ⌊log(wv/(kT a))/log ρ⌋ + 1 (lines 91–98) depends only on x at the slowest mode and ρ. The scope is the class of §3 of that note, not general.

## Every claim on the figure

| Claim on the figure | Source (file:line on `5c36ee4`) | Status |
|---|---|---|
| Hypothesis sentence | README.md:5, CORE.md:7, THEORY.md:41 | hypothesis |
| J = heat + w·E[loss], P(ruin) ≤ ε | README.md:17; theory/GENERAL_FORM_PHYSICS_2026-11-22.md:26 | worked class (physics-grounded); w and cap assumed (GFP:155–158) |
| heat ≥ kT × learning rate, approached in a limit | GFP:21, GFP:29, GFP:56–64 (IP11) | worked class |
| R1: under A1–A7, ≥3 essential coordinates, a continuous representing cost is an additive price sum, and only that | README.md:31; theory/REPRESENTATION.md:19 | general |
| Five-term master equation is a stated decomposition; terms stay assumptions; IP5; T40 open | GFP:39, GFP:241, [OPEN_WORK.md:92](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md#L92) | stated, not derived |
| Curve: x ≤ 1 blind, 2√x − 1 above; error v/√x | GFP:84–87 | worked class (IP11) |
| Below the curve unreachable | GFP:62 (floor kT R(ε)); checks §4 | worked class |
| 240 random worlds on the curve | computed here (`brute_min`), not data | computed |
| Ladder: ρ = 10, 4 of 6 rungs past x = 1, stakes ×ρ adds one | GFP:95–98 (per-mode loss, equal variances; IP12 per HOLOGRAPHIC_2026-11-22.md:31) | worked class |
| Holographic: shared memory on the curve, pays from x = 1; K copies wait to x = K | GFP:106 (blind stake lower by K); HOLOGRAPHIC_MEMORY_2026-11-22.md:52–70; general_checks.py:383–398 | worked class (T42/T39) |
| Copies cost → √K = 2× at high stakes | HOLOGRAPHIC_MEMORY_2026-11-22.md:25 | worked class |
| Ties or loses when each item is read alone | HOLOGRAPHIC_MEMORY_2026-11-22.md:13, :118 | worked class |
| Aligned beats random: 4 vs 19.2 expected at equal heat (K = 20, heat 4) | HOLOGRAPHIC_MEMORY_2026-11-22.md:98, :120 | worked class (note's example) |
| Per-unit precision cap: a pool meets a ruin cap copies miss | BOUNDARY_SUFFICIENCY_2026-11-22.md:33, :145–147, :187 | worked class (T42, T44) |
| Field: heat ∝ volume at per-site error; 13 per site, 13·n² | HOLOGRAPHIC_2026-11-22.md:21, :130 | worked class (T41) |
| Named cut: ≈13.61 per cut site, bound 13 (217.693 vs 208 at n = 16) | HOLOGRAPHIC_2026-11-22.md:17, :130; recomputed with that note's checker functions | worked class (T41) |
| Boundary: blanket suffices for decisions outside a region; interior not | BOUNDARY_SUFFICIENCY_2026-11-22.md:13, :19, :39 | worked class (T44, Gaussian field) |
| General: heat ≥ kT × information flow (bipartite chains, additive-noise diffusions) | README.md:33; GENERALITY_2026-11-22.md:17 | general |
| General: stakes up → judgment not down (fixed menu, ruin slack) | README.md:33 | general |
| General: a factorizing cut screens | README.md:33 | general |
| Where real systems sit: not measured; none shown to qualify | README.md:7, :74 | hypothesis |

## Considered and not used

- **Real-system dots.** `figures/face_placements.md` places systems in stake ÷ upkeep (h) units. GFP §7 says hK is not a term of the floor, and no file on main gives w, v, a, kT for a real system. Converting would invent data, so the curve carries no system positions.
- **The telegraph.** Proved, but its frontier is a different formula, so it does not land on this curve.
- **The five-term equation as the headline.** IP5 is FALSE for the physical frontier; it stays a stated decomposition in the cost band.
- **Rebuild (T43) and acting (T45–T47).** In-model results under other assumptions, with no coordinate on this curve; left off to keep the picture readable. They stay in `figures/derivation_map.png`.
- **"Every system lands on one line."** True only for modes in the worked class; the panel is labeled worked class.
