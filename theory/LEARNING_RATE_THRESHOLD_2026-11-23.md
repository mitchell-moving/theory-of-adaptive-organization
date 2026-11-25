# T67: Does the judge's learning rate lose its area form at the mutual-information threshold? (threshold test)

*Monday 23 November 2026, America/New_York. Written against `main` `f4ec246`. Preregistered and hash-locked before any T67 number was computed: `learning_rate_threshold_checks/PREREG_T67.md`, sha256 `b91e2101ec93acf3c22cf8b93241014012938b0db2fccc7df62ea27748d54b98`, locked 17:37:25 EST and pushed as commit `b02a81b` (17:37:31 EST) before the run started. This note also folds in the independently reviewed result of the missing-piece hunt (the judge-inside-world reframe and the boundary-layer formula). Labels follow `CORE.md:168`: PROVED (in-model), KNOWN, ELEMENTARY, CONJECTURE, SPECULATION, OPEN, NUMERICAL. `THEORY.md` is unchanged. Independently reviewed (PR #247). The reviewer scoped the wording: the preregistered outcome is MIXED, and the "relabeled" reading below is an interpretation, not the locked rule's reading.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

## 0. Bottom line

**Plain answer.** By the locked rules the outcome is MIXED, not all-EQUAL. The thresholds came out equal in three of the four preregistered cells. In the fourth (2D, hot judge) \(\Delta\) went 0.012 past the tolerance, which is small against \(\sigma_\Delta=0.057\). It also went the "wrong" way for a new object: there the learning rate kept its area form to a slightly *lower* power than the stored information did. No cell came out DIFFERENT, so nothing here shows that the flow of judgment's cost has its own locality class. The most likely reading is that, on this route, the learning rate's area form tracks the known mutual-information area law. That reading is supported post hoc (§5); it is not the preregistered all-EQUAL outcome.

- **Setup.** Bipartite Gaussian (Ornstein-Uhlenbeck) lattices in 1D and 2D. Couplings fall off as \(r^{-p}\) (Kac-normalized) with a gap \(\alpha=0.5\). The judge is a region \(A\) of the world, and there are two drives that do not cancel: a judge hotter than the world (HOT, \(T_A=2,T_B=1\)) and a judge colder than the world (COLD, \(T_A=1,T_B=2\)).
- **Measure.** For each quantity, \(p_c\) is the power below which its density per unit boundary keeps growing with the judge's size. It is estimated from the zero of the approach exponent \(s(p)\) on doubling ladders (§3).
- **Preregistered result, by the locked rules: MIXED.**

| Cell | \(p_c(I)\) | \(p_c(\dot I_A)\) | \(\Delta\) | Outcome |
|---|---|---|---|---|
| 1D, HOT | 1.079 ± 0.026 | 1.007 ± 0.026 | −0.073 | EQUAL |
| 1D, COLD | 1.005 ± 0.053 | 0.964 ± 0.043 | −0.041 | EQUAL |
| 2D, HOT | 1.690 ± 0.040 | 1.529 ± 0.041 | −0.162 | P-b MISS (open) |
| 2D, COLD | 1.470 ± 0.094 | 1.446 ± 0.062 | −0.024 | EQUAL |

- **P-a met in both dimensions.** The equilibrium threshold of \(I\) is 1.048 ± 0.037 in 1D (window [0.85, 1.15]) and 1.604 ± 0.058 in 2D (window [1.35, 1.65]). This matches Kim–Kuwahara–Saito's \((d+1)/2\).
- **Two open misses, both in 2D HOT.**
  - P-a′: \(I_{\rm HOT}\) breaks at 1.690, outside [1.35, 1.65].
  - P-b: \(\Delta=-0.162<-0.15\).
- **P-c met everywhere.** Above \(d+1+0.2\), no learning rate grows faster than the boundary (maximum \(s\) is −2.36 in 1D and −1.005 in 2D).
- **Post-hoc diagnosis (not preregistered; it cannot change the outcome above).**
  - A corner-free strip judge with 8 to 16 times the preregistered boundary gives \(\Delta=-0.134\) (HOT) and \(-0.069\) (COLD), inside the EQUAL band.
  - The 2D mutual-information break sits about 0.1 above 1.5 at every size tried, including at equilibrium. So the miss looks like a slow approach to the threshold in the regime \(p<d\), where couplings are non-extensive. It does not look like a separate threshold for the learning rate (§5).
- **What it means (interpretation, not the locked rule).** The lock reserved the plain "relabeled" statement for EQUAL in all four cells, and that did not happen. Given 3/4 EQUAL, no DIFFERENT cell and the post-hoc diagnosis, the most likely reading is that on this route the area form of judgment's ongoing cost tracks the known area law of cross-cut correlation. If so, the angle adds bookkeeping (a reading of a known result in the theory's own cost), not a new locality class. One pattern stays open: \(\Delta<0\) in every cell, preregistered and post hoc (§9).
- **Secondary (descriptive).** The gross learning term on its own also breaks near \((d+1)/2\), not at the crossing-coupling bound's \(d+1\), so that bound is loose (§6). This is the flow's analogue of Kim–Kuwahara–Saito's own finding that the MI area law is more robust than the boundary-interaction argument suggests.
- **Scope.** Classical, linear, Gaussian, gapped, temperature-step drives. None of this bears on \(G\), quantum mechanics, or holography, and none of it is claimed.

## 1. What is already in the repository (grep of `main` `f4ec246`)

- **Equilibrium cross-cut MI.**
  - The repository already has the equilibrium cross-cut MI area law, as "the field's own" quantity (Wolf et al. 2008, `theory/HOLOGRAPHIC_2026-11-22.md:116`).
  - It also has the interface learning-rate floor (Proposition H-iface, `theory/HOLOGRAPHIC_2026-11-22.md:40`, T41), and T44's blanket sufficiency for exterior decisions (`OPEN_WORK.md:95`).
- **Area cap and heat floor.** There is T62's class AL area cap on tracked flux, with a packing input (`theory/AREA_LAW_PROBE_2026-11-23.md:15`), and the heat floor \(\dot Q_M\ge kT\,\dot I_M\) (`CORE.md:70`).
- **Already cited.** Horowitz–Esposito 2014 and Hartich–Barato–Seifert 2014 are cited across `THEORY.md` and the theory notes. Jacobson 1995 is in `theory/AREA_LAW_PROBE_2026-11-23.md:51`.
- **Not in the repository before this note:** Jacobson 2016, Kim–Kuwahara–Saito 2025, Allahverdyan–Janzing–Mahler 2009, Demko–Moss–Smith 1984, and the words "judge inside" / "judge-inside" and "T67".

## 2. The hunt result, as independently reviewed (folded in)

**The reframe.** T63–T65 tried to cap how many *records* a region can hold. Judgment is something else: what the judge knows about the world outside it that is still true. When the judge is itself a region \(A\) of the world (world \(B\) = the rest, not exogenous), that knowledge is the correlation \(I(A;B)\) across its own boundary. The rate at which it is kept up is the Horowitz–Esposito information flow \(\dot I_A\), and its minimum heat is \(kT_A\,\dot I_A\) (`CORE.md:70`).

The reviewer graded this reframe as mostly a relabeling of known results. Horowitz–Esposito already price any bipartite split, and T41 and T44 already put the floor at the interface. *Credits:* Wolf, Verstraete, Hastings and Cirac 2008 (stock); Horowitz and Esposito 2014, and Hartich, Barato and Seifert 2014 (flow and its floor); Allahverdyan, Janzing and Mahler 2009 (information flows from hot to cold: the colder side learns).

**Boundary-layer formula (ELEMENTARY; re-derived independently by the reviewer, finite difference agreeing to about \(10^{-8}\)).**

- **The formula.** Take bipartite linear Gaussian dynamics \(dx=-Kx\,dt+\sqrt{2D}\,dW\) with steady covariance \(\Sigma\) and \(P=\Sigma^{-1}\). Then
\[
\dot I_A=\underbrace{-\operatorname{tr}\!\big(\Sigma_{AA}^{-1}K_{AB}\Sigma_{BA}\big)}_{t_1\ \text{(gross learning)}}\ \underbrace{-\operatorname{tr}\!\big(D_{AA}\,P_{AB}P_{BB}^{-1}P_{BA}\big)}_{t_2\ \text{(gross forgetting)}\ \le0}.
\]
It follows from \(\Sigma_{AA}^{-1}=P_{AA}-P_{AB}P_{BB}^{-1}P_{BA}\).
- **Exact conditions.** \(D\) need not be diagonal, but \(D_{AB}=0\) (bipartite noise) is required. With \(\kappa=\lambda_{\max}(\Sigma)/\lambda_{\min}(\Sigma)\):
  - \(|t_1|\le\kappa\sum_{a\in A,b\in B}|K_{ab}|\), for any \(\Sigma\).
  - \(|t_2|\le D_{\max}\lambda_{\max}(\Sigma)\,\|P_{AB}\|_F^2\).
- **When the area form holds.** \(|\dot I_A|=O(|\partial A|)\) whenever four things hold: \(K\) has finite range, \(D_{AB}=0\), \(\kappa\) is bounded (a gap), and \(\|P_{AB}\|_F^2=O(|\partial A|)\).
  - The last holds for exponentially decaying \(P\). Demko, Moss and Smith 1984 cover inverses of banded matrices; here \(\Sigma\) is only exponentially localized, so what is used is the standard extension of that result to well-conditioned, exponentially localized matrices.
  - For tails \(|P_{ab}|\sim r^{-p}\), it holds iff \(2p>d+1\).
  - That is the threshold \((d+1)/2\) Kim, Kuwahara and Saito 2025 found for the thermal MI area law (in quantum lattice systems, assuming power-law clustering of bipartite correlations; in this classical Gaussian model the Frobenius count above gives the same number directly), and it is why T67 asks whether the flow's threshold is the same.
- **No packing input.** The packing input of T62 can be dropped for the flow: locality, a gap and bipartite noise bound it by the cut. This is a modest, possibly new corollary of known decay results; a moderate search found it nowhere, and it is not claimed as a theorem of physics.

**An equilibrium area-law stock costs zero.**

- At equilibrium \(\dot I_A=0\). The gross terms are each about ± the perimeter and cancel; the reviewer found ±17.8894 at \(L=16\), and here the check at \(n=256\) gives \(t_1=-t_2\) to \(10^{-10}\).
- So a passive region's area-law "knowledge" carries **zero ongoing cost of judgment**. The area-law stock is correlation, not cost, and in this sense any rock "judges".
- Relatedly, a circulation that preserves the Gibbs measure, \(\Omega=\gamma(S-S^T)/2\) commuting with \(Q\), gives \(\dot I_A=0\) for every region (ELEMENTARY, reviewer).
- Only a drive (here a temperature step) makes the flow, and so its cost, nonzero.

**Chad's hunch, "Perhaps there is no gravity in its derivative" (treated as data).**

- *Right, in a narrow sense.* The area *form* of judgment's stock and flow needs locality, a gap and bipartite noise, not gravity (in-model; KNOWN for the stock).
- *Not right about the coefficient.* \(\eta\), and so \(G=c^3/(4\hbar\eta)\), still needs a short-distance cutoff plus Jacobson's identification (Jacobson 2016, entanglement equilibrium).
- *The objects differ.* Jacobson's input is vacuum entanglement entropy. A classical thermal MI or a learning rate is a different object, and equating them is SPECULATION.

## 3. The preregistered test (summary of the lock; the lock file governs)

- **Lattices and couplings.**
  - The lattice is a ring (1D, \(n\in\{1024,2048\}\)) or a torus (2D, \(n\in\{48,64\}\)), with minimum-image distance.
  - \(J_{xy}=r^{-p}/Z(n,p)\), with row sum 1, and \(K=(\alpha+1)I-J\), \(\alpha=0.5\).
  - \(D\) is diagonal, so \(D_{AB}=0\).
- **Judge and grids.**
  - The judge is an interval of length \(L\) (1D, \(L\le n/8\)) or an \(L\times L\) square (2D, \(L\le n/4\)).
  - The \(p\) grid is 0.6–3.0 (1D) and 1.1–4.0 (2D), in steps of 0.1.
- **Estimator.**
  - On a doubling ladder \((L,2L,4L)\), with \(y=Y/|\partial A|\), \(s=\log_2[(y_3-y_2)/(y_2-y_1)]\). This is the exponent of \(y=c+bL^{s}\). \(s<0\) means a finite boundary density (area form); \(s\ge0\) means it grows.
  - \(p_c\) is the largest zero crossing of \(s(p)\) by linear interpolation.
  - The primary ladder is the largest at the largest \(n\). The error bar is half the range over the primary ladder and three variant ladders.
- **Predictions.**
  - P-a: \(p_c(I_{\rm EQ})=(d+1)/2\pm0.15\). P-a′: the same window for the NESS \(I\).
  - P-b: \(p_c(I)-0.15\le p_c(\dot I)\le d+1+0.15\).
  - P-c: \(s_{\dot I}<0.05\) for every \(p\ge d+1+0.2\).
- **Decision rule.** EQUAL if \(|\Delta|\le0.15\). DIFFERENT if \(\Delta>\max(0.15,2\sigma_\Delta)\). UNRESOLVED in between. P-b MISS if \(\Delta<-0.15\).
- **Prior exposure (disclosed in the lock).**
  - The reviewer's exploratory 1D run: \(n=600\), hot judge, \(p\in\{0.8,1.2,1.6,2,3\}\), with \(I\) and \(|\dot I_A|\) slopes of 0.533/0.443, 0.155/0.098, 0.02/0.009, 0.002/0.001, and 0/0.
  - The writer's stated lean toward EQUAL, from the equilibrium cancellation of the gross terms.
  - The 2D arm, the COLD drive, the sizes and the estimator were unexposed.

## 4. Results (NUMERICAL; `learning_rate_threshold_checks/t67_run.out`)

**Validation gates (all PASS).**

| Gate | Check | Result |
|---|---|---|
| G1 | Fourier Lyapunov solver vs scipy | \(4\times10^{-15}\) |
| G2 | Identity vs finite difference | \(3\times10^{-9}\) relative |
| G3 | Equilibrium \(|\dot I_A|\) | \(\le2.7\times10^{-14}\) at every \((n,p,L)\) |
| G4 | Lyapunov residual | \(\le2.1\times10^{-14}\) |
| G5 | Every Cholesky factorization | succeeded |

The sign is as expected everywhere: the hot judge forgets (\(\dot I_A<0\)) and the cold judge learns (\(\dot I_A>0\)).

**Thresholds (primary ± half-range over 4 ladders).**

| Quantity | 1D \(p_c\) | 2D \(p_c\) | Window \((d+1)/2\pm0.15\) |
|---|---|---|---|
| \(I_{\rm EQ}\) | 1.048 ± 0.037 | 1.604 ± 0.058 | met, met |
| \(I_{\rm HOT}\) | 1.079 ± 0.026 | **1.690 ± 0.040** | met, **missed** |
| \(I_{\rm COLD}\) | 1.005 ± 0.053 | 1.470 ± 0.094 | met, met |
| \(\lvert\dot I_A\rvert\) HOT | 1.007 ± 0.026 | 1.529 ± 0.041 | (P-b) met, **missed via \(\Delta\)** |
| \(\lvert\dot I_A\rvert\) COLD | 0.964 ± 0.043 | 1.446 ± 0.062 | met, met |

**The shape of \(s(p)\).**

- In 1D, \(s(p)\) tracks \(d+1-2p=2-2p\) closely above the threshold for every quantity. For example, \(s(2.0)=-2.02\) for \(I_{\rm EQ}\) and \(-2.05\) for \(\dot I_{\rm HOT}\). Below the threshold it is flatter (\(s(0.6)=0.52\) for \(I_{\rm EQ}\), against 0.8 asymptotically).
- In 2D, \(s(p)\) is much flatter than \(3-2p\) near the threshold: about \(-0.9\) per unit \(p\), against \(-2\) asymptotically. That is a sign of strong finite-size rounding (§5). Above about \(p=2.6\) it flattens at \(-1\), where the square's corners (a \(1/L\) term in the per-boundary density) dominate the approach.
- The learning rate's \(s\) is at or below the MI's \(s\) at the grid points that bracket each crossing. That is why \(\Delta\le0\) in every cell. Well below the threshold the order can flip (for example COLD at \(p\le0.7\) in 1D and \(p\le1.3\) in 2D).

**Above the learning-term bound threshold \(d+1\) (P-c).** The maximum \(s_{\dot I}\) for \(p\ge d+1+0.2\) is −2.46/−2.36 (1D HOT/COLD) and −1.005/−1.006 (2D). The density is finite with room to spare, and nothing grows faster than the boundary.

**The naive estimator (descriptive only).** The log-log slope of \(y\) crossing 0.05 gives \(p_c\) values 0.2–1.0 higher in every case, the usual rounding of a slow approach. This is why the preregistered estimator uses the approach exponent instead.

## 5. The open misses, diagnosed (POST HOC, not preregistered)

**The open misses.** In 2D HOT, \(I_{\rm HOT}\) breaks at 1.690, outside its window, and so \(\Delta=-0.162\) falls just past −0.15. The predictions are not patched. Three diagnostics follow.

1. **Corner-free strip judge at larger sizes** (`posthoc_strip.py`, exact transverse-Fourier decomposition, validated against the dense code to \(3\times10^{-15}\)). The judge is a band \(\{x<L\}\) on an \(n\times n\) torus, with boundary \(2n\), and the same estimator is used.

| Strip | \(I_{\rm EQ}\) | \(I_{\rm HOT}\) | \(\dot I_{\rm HOT}\) | \(I_{\rm COLD}\) | \(\dot I_{\rm COLD}\) | \(\Delta_{\rm HOT}\) | \(\Delta_{\rm COLD}\) |
|---|---|---|---|---|---|---|---|
| \(n=256\), \(L=8,16,32\) | 1.600 | 1.647 | 1.509 | 1.522 | 1.453 | −0.138 | −0.069 |
| \(n=512\), \(L=16,32,64\) | 1.595 | 1.640 | 1.506 | 1.520 | 1.451 | −0.134 | −0.069 |

   (Full grid p = 1.1–4.0 at both sizes; `posthoc_strip.out`.) Above threshold the strip shows no faster-than-boundary flow either: at \(n=512\), \(s_{\dot I}\) is \(-3.10/-2.89\) (HOT/COLD) at \(p=3.0\) and \(-5.19/-4.89\) at \(p=4.0\), close to \(3-2p\) once corners are gone. Without corners and with 8 to 16 times the preregistered boundary, both drives fall in the EQUAL band. The hot-drive MI still sits at 1.64.

2. **The MI threshold itself sits about 0.1 high in 2D, even at equilibrium** (`posthoc_eq_ratio.py`, exact, cheap because \(P=K\) at equilibrium). Over \(n=512\)–\(4096\) and two ladders, \(p_c(I_{\rm EQ})\) stays at 1.59–1.64 with no monotone drift. The local exponent at \(p=1.5\) is +0.12 to +0.22 where the asymptotic value is 0, and the slope of \(s(p)\) is about \(-0.9\) rather than \(-2\).

   **Diagnosis (CONJECTURE).** In 2D the threshold \(3/2\) lies in the non-extensive regime \(p<d\). There the Kac normalization \(Z\sim n^{2-p}\) makes the covariance itself carry \(r/n\)-dependent tails: \(J*J\) has a \(|r|^{2-2p}/Z^2\) part, comparable to \(J\) at \(r\sim n\). So the approach to \((d+1)/2\) is slow and size-structured. KKS themselves call their numerics "qualitatively accurate" in this regime. In 1D the threshold \(1=d\) is the marginal case, and the offset is only +0.05.

3. **The hot drive raises the MI break more than the learning rate's.** The HOT temperature step lifts \(p_c(I)\) by +0.05 to +0.09 over equilibrium, while \(p_c(\dot I_{\rm HOT})\) stays at 1.51–1.53, near 1.5. The miss in \(\Delta\) is the stock's threshold moving up, not the flow's threshold moving away. Why a hot judge's NESS correlation keeps growing to a higher \(p\) than its equilibrium correlation is OPEN.

**Reading.** The single P-b miss is 0.012 past the tolerance, small against \(\sigma_\Delta=0.057\), and in the direction opposite to "the flow is its own object". Under the post-hoc diagnostics it shrinks into the EQUAL band. This is evidence, not a preregistered result, and a fresh lock would be needed to make it one.

## 6. Secondary (descriptive, preregistered as descriptive)

**The gross terms share the MI threshold.**

- In 1D, the gross learning term \(|t_1|\) breaks at 0.917 (HOT) and 0.779 (COLD), and the gross forgetting term \(|t_2|\) at 0.950 and 0.678.
- In 2D HOT, \(|t_1|\) breaks at 1.342 and \(|t_2|\) at 1.398.
- The crossing-coupling bound \(|t_1|\le\kappa\sum|K_{ab}|\) has threshold \(d+1\) (2 in 1D, 3 in 2D), which is far from these values. That bound is valid but loose: the learning term inherits the \(\|P_{AB}\|^2\)-type tail, \((d+1)/2\), as the equilibrium cancellation \(t_1=-t_2\) suggested.

**The 2D COLD gross terms are ill-conditioned for this estimator.** \(|t_1|\) has a crossing at 2.808, and \(|t_2|\) is censored, with one undefined point at 2.5. Above about \(p=2.5\) their per-boundary densities are almost exactly constant (for example \(t_1/4L=0.017472, 0.017456, 0.017439\) at \(L=4,8,16\), \(p=2.8\)). The increments are tiny and change sign, so \(s\) is noise there. The net \(\dot I_{\rm COLD}\) is well conditioned. This affects no decision.

## 7. The GTAO method, run explicitly

1. **The cost, with named terms.** The ongoing cost of judgment for a judge that is a region of its world is the heat term \(kT_A\,\dot I_A\) (the floor, `CORE.md:70`), plus the stake and the ruin cap. Those two are not used here; this test touches only the heat term, as in T63–T66. The stock \(I(A;B)\) has no ongoing cost at equilibrium (§2); only its upkeep under a drive does.
2. **Its minimum.** At fixed locality, gap and bipartite noise, the minimum upkeep is a boundary sum, \(t_1+t_2\) over the cut layer (§2). T67 asks whether the locality class of that minimum differs from the stock's. Within this model class no difference was found: equal thresholds in 3/4 cells, no DIFFERENT cell, and the fourth diagnosed post hoc (CONJECTURE) as the stock's slow approach.
3. **Read-off design (the model's implication, stated plainly).** A judge's ongoing cost scales with its boundary exactly when the world's correlations across that boundary are area-form. A judge facing a world with long-range coupling, \(p<(d+1)/2\), pays an upkeep that grows faster than its skin. There, the cheaper design is to *move the cut* (a model implication, untested here): choose the judge's boundary so that fewer long-range bonds cross it, or coarse-grain them. Making the boundary larger does not help. A colder judge learns and a hotter one forgets (Allahverdyan 2009), so it is the sign of the temperature step at the cut that sets which side pays.
4. **Scope.** *Covered:* classical, linear, Gaussian lattices with a gap, Kac-normalized power-law couplings, bipartite noise, temperature-step drives, rings and tori, and the sizes listed. *Excluded:* non-bipartite (conserving) noise (the Chétrite–Rosinberg–Sagawa–Tarjus 2019 flow), nonlinear or critical media, quantum states, unnormalized couplings, bulk non-cancelling drives with power-law couplings, and anything about \(G\), quantum mechanics or holography.

## 8. What is new, and what is not

- **KNOWN.** The equilibrium MI area law and its kT-per-nat boundary-energy price (Wolf 2008). The \((d+1)/2\) threshold for thermal MI (Kim–Kuwahara–Saito 2025). Information flow and its heat floor for bipartite splits, zero at equilibrium (Horowitz–Esposito 2014; Hartich–Barato–Seifert 2014; Horowitz–Sandberg 2014). Hot-to-cold information flow (Allahverdyan–Janzing–Mahler 2009). Gaussian/OU flow formulas (Loos–Klapp 2020). Gravity from entanglement equilibrium (Jacobson 2016).
- **In the repository already.** The interface floor (T41), blanket sufficiency (T44), and the area cap on tracked flux with a packing input (T62).
- **Possibly new, modest (not found in a moderate search).** Locality, a gap and bipartite noise alone bound the learning rate by the cut, with the exact conditions in §2. The NUMERICAL finding that, in this class, the learning rate's area-form threshold equals the MI threshold (3/4 cells preregistered; the fourth inside the band only post hoc, on a different geometry), and that the crossing-coupling bound's \(d+1\) is not the operative threshold (the flow's analogue of Kim–Kuwahara–Saito's observation for the MI, so only modestly new).
- **Not new.** The "judge = region" reading is a relabeling.

## 9. Open

- Why the hot drive raises the 2D NESS MI threshold above equilibrium's (§5.3). Whether 2D \(p_c\) approaches 1.5 at much larger \(L\), or with unnormalized couplings.
- Why \(\Delta<0\) in every cell (4/4 preregistered, 4/4 strip post hoc): the flow's threshold sits at or slightly below the stock's, and nearer \((d+1)/2\). Whether that is finite-size structure or a small real offset is OPEN.
- A fresh preregistered lock on the corner-free strip geometry, if this angle is reopened. The lock's stop instruction belonged to the all-EQUAL branch; with a MIXED outcome, reopening is a judgment call. The case for a low priority is that no cell came out DIFFERENT.
- The non-bipartite (conserving) case with the Chétrite et al. 2019 flow. Bulk drives with power-law couplings.
- A proof that the learning term's tail is \(\|P_{AB}\|_F^2\)-type, threshold \((d+1)/2\), out of equilibrium (CONJECTURE, supported numerically here).

## 10. Claim map for this note

| Claim | Label |
|---|---|
| Boundary-layer formula for \(\dot I_A\), with exact conditions | ELEMENTARY (reviewed) |
| Equilibrium area-law stock carries zero ongoing cost; Gibbs-preserving circulation gives zero flow | ELEMENTARY (reviewed) |
| P-a: \(p_c(I_{\rm EQ})=(d+1)/2\pm0.15\) in 1D and 2D | NUMERICAL, preregistered, met |
| \(p_c(\dot I)=p_c(I)\) within 0.15 in 1D HOT, 1D COLD, 2D COLD | NUMERICAL, preregistered, EQUAL |
| 2D HOT: \(p_c(I_{\rm HOT})=1.690\) outside window; \(\Delta=-0.162\) | NUMERICAL, preregistered, open miss |
| No faster-than-boundary learning rate above \(d+1+0.2\) | NUMERICAL, preregistered, met |
| Strip geometry puts 2D HOT/COLD in the EQUAL band | NUMERICAL, post hoc |
| 2D offset is a slow approach in the non-extensive regime | CONJECTURE |
| \(p_c(\dot I)\le p_c(I)\) in every cell (sign of \(\Delta\)) | NUMERICAL (descriptive); cause OPEN |
| Gross learning term threshold is \((d+1)/2\), not \(d+1\) | NUMERICAL (descriptive); proof OPEN |
| Any route from this to \(G\), quantum mechanics or holography | SPECULATION, not claimed |

## 11. Files, and what the checks verify

- `learning_rate_threshold_checks/PREREG_T67.md`, `PREREG_T67.sha256`: the lock.
- `t67lib.py`: model, Fourier Lyapunov solver, identity, estimator.
- `gates_small.py`: gates G1 and G2.
- `run_t67.py`: the main run. Its raw output is in `raw_d1_n1024.json`, `raw_d1_n2048.json`, `raw_d2_n48.json` and `raw_d2_n64.json`.
- `analyze_t67.py`: the analysis. Its output is in `t67_run.out` and `t67_results.json`.
- Post hoc: `posthoc_strip.py`, `strip_n256.json`, `strip_n512.json`, `analyze_strip.py` → `posthoc_strip.out`; `posthoc_eq_ratio.py` → `posthoc_eq_ratio.out`.
- `crossref.out`: 13 DOIs, all resolving on Crossref on 23 Nov 2026.
- `learning_rate_threshold_checks.py` → `learning_rate_threshold_checks.out`, run by `tools/test_learning_rate_threshold_checks.py`. It re-checks the following:
  - The prereg hash.
  - Gates G1 and G2, and gates G3 and G4 as recorded.
  - The equilibrium cancellation.
  - Stored raw values, recomputed at sample points.
  - The strip decomposition, against the dense code.
  - That the analysis reproduces `t67_run.out` byte for byte.

  The full main run takes about 25 minutes at nice 19, so it is not in the test suite.

**DOIs (Crossref-verified, `crossref.out`).**

| Work | DOI |
|---|---|
| Wolf et al. 2008 | 10.1103/PhysRevLett.100.070502 |
| Kim–Kuwahara–Saito 2025 | 10.1103/PhysRevLett.134.020402 |
| Horowitz–Esposito 2014 | 10.1103/PhysRevX.4.031015 |
| Hartich–Barato–Seifert 2014 | 10.1088/1742-5468/2014/02/P02016 |
| Barato–Hartich–Seifert 2014 | 10.1088/1367-2630/16/10/103024 |
| Allahverdyan–Janzing–Mahler 2009 | 10.1088/1742-5468/2009/09/P09011 |
| Jacobson 2016 | 10.1103/PhysRevLett.116.201101 |
| Horowitz–Sandberg 2014 | 10.1088/1367-2630/16/12/125007 |
| Demko–Moss–Smith 1984 | 10.1090/S0025-5718-1984-0758197-9 |
| Loos–Klapp 2020 | 10.1088/1367-2630/abcc1e |
| Chétrite–Rosinberg–Sagawa–Tarjus 2019 | 10.1088/1742-5468/ab47fe |
| Gullans–Huse 2019 | 10.1103/PhysRevX.9.021007 |
| Eisler–Zimborás 2014 | 10.1103/PhysRevA.89.032321 |

**What this note does not do.** It does not touch `THEORY.md`. It makes no claim about real systems, \(G\), quantum mechanics or holography, and it does not treat the post-hoc strip result as preregistered.
