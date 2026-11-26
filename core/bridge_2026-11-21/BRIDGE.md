# Physics, selection, and the cost of judgment

*21 November 2026 (America/New_York). Short face note for `core/bridge_2026-11-21/`. Does not change `CORE.md` or the hypothesis sentence. Official in-model test: T27, preregistered in `PREREG.md` before any official run.*

The **law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.** This note is about how that hypothesis sits next to the second law and next to population genetics. It is not a claim that the hypothesis is now a physical law, and it is not a theory of everything.

## The chain, in one paragraph

The second law sets *floors* on the prices in \(J\) (Landauer; Still, Sivak, Bell & Crooks 2012). Selection is a thermal search over designs at an inverse temperature \(\beta\) fixed by selection strength (Sella & Hirsh 2005, applied to \(J\)). The hypothesis is the low-temperature limit of that search: strongly selected systems sit near \(\arg\min J\), with a typical excess of order \(d/(2\beta)\) when the minimum is quadratic. Physics explains why a cost exists; evolution explains how a lineage gets near the minimum; the hypothesis says what the end of that search looks like. Costs *above* the floor are set by the niche, not by \(kT\).

## Already in the repository

None of the following is rediscovered here. Pointers:

- Floors on the prices in \(J\): THEORY, “one currency” paragraph; CORE.md, definition section; SCALE_ENDS E3 / SE3 / SE7; FRAMEWORK §3.11 (\(\beta_{\mathrm{phys}}\)).
- Predictive information-bottleneck curve and “first bit must pay”: CT4 (THEORY Result 1 / GENERAL_THEOREM); Still 2020 derivation of the bottleneck from a dissipation bound, already credited there; Bialek, Nemenman & Tishby 2001 and the causal-state conjecture, THEORY §9.
- Atoms and the switch-on: `theory/SCALE_ENDS.md` (E1, E2, S1–S4); Kelly-type existence condition \(E_{\mathrm{gen}}>\beta_{\mathrm{phys}}kT\).
- Operational “strongly selected,” \(\sigma\) (the cost-to-fitness map of THEORY §3 / FRAMEWORK §9; **not** the shock scale in the line below), \(N_e\), drift barrier \(s N_e\approx 1\), band \(\varepsilon=10/(\sigma N_e)\): THEORY §3; FRAMEWORK §9 (around the qualification protocol).
- Ruin-constraint “temperature” \(z=B/(\sigma\tau^H)\): THEORY (iv), CT18, CT25. Here \(\sigma\) is the **CT18 shock scale**, a different symbol from the cost-to-fitness map above. Field tests C3, F1 and DECISIVE were PROXY-FAIL and are not part of the structural core. Drăgulescu & Yakovenko (2000) is credited as an analogy only ([`history/2026-11-12_X_POST.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/history/2026-11-12_X_POST.md); THEORY (iv)).

Details of the floor, and one explicit corollary, are in `FLOOR.md`. Details of the selection mapping are in `SELECTION.md`.

## What this package adds

1. **An explicit stakes-to-thermal ratio** \(\rho=(w\Delta\ell_1)/(\nu kT)\), a corollary of CT4 plus the Landauer floor, not a new theorem: \(\rho\le 1\Rightarrow K^\star=0\). This packages SCALE_ENDS S4 / SE7 as a scale-end statement. For atoms the load-bearing argument remains E1+E2 (benefit zero), not this ratio alone. When \(\beta_{\mathrm{phys}}\gg 1\) the floor does not decide designs. See `FLOOR.md`.
2. **A stationary distribution** \(\pi\propto\exp(-\beta J)\) under weak-mutation selection and a linear map \(m=-\alpha J\), with \(\beta=\alpha(N-1)\) for haploid Moran (standard pop-gen, applied to \(J\)).
3. **An equipartition prediction** \(\mathbb{E}[J]-J^\star=d/(2\beta)\) near a quadratic minimum, which turns “systems lag” into a predicted spread of order \(1/\)selection strength, and which is consistent with the existing band: typical fractional excess \(\approx d/(2\sigma N_e)\), versus \(\varepsilon=10/(\sigma N_e)\), so the ratio is \(d/20\). The locked factor of 10 is not changed. See `SELECTION.md`.
4. **T27**, a preregistered in-model Moran test of (2)–(3) in Model S. Official result in `RESULTS.md`.

## Two temperatures, and they are not the same

The repository already uses the word “temperature” for the ruin-constraint group

$$z=\frac{B}{\sigma\tau^H}$$

(THEORY (iv), CT18, CT25): shock times a power of the time to fix, divided by the buffer. The \(\sigma\) in this formula is the **CT18 shock scale**, not the cost-to-fitness map \(\sigma\) of THEORY §3 / FRAMEWORK §9 used in the qualification band and in the \(d/(2\sigma N_e)\) consistency note below. The two meanings share a letter and are not the same quantity. Per-window ruin at most \(\varepsilon_r\) means \(z\ge z_\varepsilon\). That quantity is the *world’s stress on a design*. It belongs inside the constraint \(P(\mathrm{ruin})\le\varepsilon\). It decides which designs are feasible, and how much buffer a given design needs. The only shared mathematics with Drăgulescu & Yakovenko’s money-gas “temperature” is that independent shocks spread as a power of time. It is an analogy only. It is not measured in kelvin, and no physical law sets its unit. Tests C3, F1 and DECISIVE, which tried related real-world readings, were PROXY-FAIL and were moved out of the structural core.

This package uses a second inverse temperature, \(\beta\), the selection strength in \(\pi\propto e^{-\beta J}\). Its reciprocal \(1/\beta\) is the *noise of the selection search*. It decides how far realized designs sit from \(\arg\min J\) among the designs that are feasible. It is also not a kelvin temperature. The only kelvin in this package is the Landauer floor on the *prices* in \(J\).

**One picture, no forced identification.** A complete sketch is: the ruin constraint (the \(z\) side) cuts the design set to those with \(P(\mathrm{ruin})\le\varepsilon\); selection then searches that feasible set with \(\pi\propto e^{-\beta J}\) (the \(\beta\) side), or with \(\pi=0\) off the feasible set. Buffer, shock and fix-time shape *which* designs can persist; \(N_e\) and the cost-to-fitness map \(\sigma\) (THEORY §3 / FRAMEWORK §9; a different \(\sigma\) from the shock scale that appears in \(z\)) shape *how tightly* a lineage sits at the cheapest feasible one.

A formal relation is not derived. A large-deviation rate function for lifetime ruin could, in some models, look like \(\varepsilon\sim e^{-I(B,\ldots)}\) and might be compared with \(\beta\), but that would be a new calculation, not an identity, and this package does not force one. The two quantities can vary independently: a system can be tightly selected (large \(\beta\)) in a calm world (large \(z\)), or loosely selected in a harsh one.

## What is theorem, what is assumption, what is loose

- **Theorems (known, used here):** Landauer’s bound; Still et al.’s dissipation identity in their stated class; CT4; Moran/Wright–Fisher detailed balance \(\Rightarrow\pi\propto e^{-\beta J}\) given the linear map and weak mutation; equipartition for a quadratic energy under a Boltzmann measure.
- **Assumptions:** erasure-type updates when writing \(\kappa_{\mathrm{floor}}=kT\cdot\nu\); \(m=-\alpha J\); weak mutation and a connected design graph; a locally quadratic minimum for the \(d/(2\beta)\) formula.
- **Loose:** the thermodynamic floor as a *design* constraint in real systems (\(\beta_{\mathrm{phys}}\) usually \(\gg 1\)); Still et al. outside their stated class; the factor of 10 in the qualification band (a conservative choice, now comparable to \(d/2\) rather than replaced).

## What is new versus what is known

| Piece | Status |
|---|---|
| Landauer, Still et al. 2012, information bottleneck, CT4, SCALE_ENDS switch-on | Known; already in this repository |
| Sella–Hirsh / Iwasa free fitness; Shahshahani gradient view; Lynch drift barrier | Known prior art; qualification already used the last |
| \(\rho\le 1\Rightarrow K^\star=0\) as an explicit ratio | Corollary of existing results, written out |
| \(\pi\propto e^{-\beta J}\) for designs, and \(\mathbb{E}[J]-J^\star=d/(2\beta)\) as a predicted lag | New claim of this package (in-model; T27 tests it) |
| Using that spread to read the FRAMEWORK §9 band | New consistency note; the band itself is unchanged |

## What this does not show

It does not make the theory “all physics.” The floor is a floor. Prices above it — salaries, attention, ATP per useful nat in a cell that is not at Landauer — are set by the niche. The hypothesis is still a hypothesis about selected systems, not a restatement of the second law. It does not explain consciousness, and it does not identify \(1/\beta\) or \(z\) with a kelvin temperature. It does not lift PROXY-FAIL field tests, and it does not change the law sentence.

## Math that is still missing

- A large-deviation rate function for the lifetime-ruin constraint \(\varepsilon\), and any *derived* (not forced) relation between that rate and \(\beta\).
- Information geometry of the design search beyond crediting the Shahshahani metric: a Fisher–Rao or information-bottleneck account of the Hessian that enters equipartition.
- The same stationary law under strong mutation, standing polymorphism, or a nonlinear \(m(J)\).
- A persistence-only (non-replicating) version of the switch-on inequality, already flagged in SCALE_ENDS §6b.

T27 does not close these. It only tests the weak-mutation, linear-map, in-model consequences in Model S.

## Official in-model test (T27)

Preregistered in `PREREG.md` and `predictions.json`, locked in `LOCK.txt` at 12:05:31 AM EST on 21 November 2026, before any official world was evaluated. Official result, scored the same night: **FAIL** (in-model, numerical). P1 (high-\(\beta\) mode equals the argmin) passed 3/3; P2 (equipartition, \(\beta\)-excess within 20% of \(d/2\)) passed 3/3; P3 (low-\(\beta\) two-\(K\) mass floor) failed 0/3. The mean at low \(\beta\) did stay above \(J^\star\); the locked spread clause did not, because mass piled on the larger \(K=3\) slice. No rescue. Details in `RESULTS.md`.
