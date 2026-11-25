# Memory, tracking, and the exchange rates

*Tuesday 24 November 2026 (UTC). Against `main` `0f37918`, after the lock in `PREREG.md` (`0846e2e`). Open-work id T70. `THEORY.md` is not edited. No real-world series was opened.*

Why this approach. The cost alone is dimensionless (nats times stakes), so on its own it cannot set a physical scale. The memory coordinate is a number of nats (`THEORY.md:30`, `CORE.md:33`, Theorem R1 at `CORE.md:52`). The stake is the currency, and only dimensionless ratios of those products matter (`THEORY.md:36`). Nothing in that product is a joule or a second until a conversion is supplied. Once the cost is coupled to physics, dimensional constants may enter as exchange rates, and whether they do is an open question, not an established limit. `THEORY.md:36` says physics sets price floors, "not exchange rates between systems": that is prices across systems, while an exchange rate here is a unit conversion inside one coupled system. The absolute sentence is `theory/PHYSICS_CHAIN_2026-11-23.md:73`: the cost contains neither \(G\), \(\hbar\), nor \(c\). That wording is too absolute. This note does not adopt it. `PREREG.md:11` also cites `theory/AREA_LAW_PROBE_2026-11-23.md:17` for that sentence. Line 17 does not state it. The correction is in the errata. A miss below is an open question about that bridge, not a limit on a later coupling.

**Label.** The mapping from a term to a bridge is **INTERPRETATION**. The dimension identities in `dimension_check.py` are **ELEMENTARY** checks of formulas the repository or the cited papers already state. They are not a derivation of the values of \(k_B\), \(\hbar\), \(c\), or \(G\), and they are not a proof that a physical system uses this coupling. This note does not derive general relativity, quantum mechanics, or holography.

## Which term is which

The question is the memory term and the tracking term. In the five-term display the memory term is \(\kappa I_{\mathrm{mem}}\). In the physical class that term is the bath heat, with floor \(kT\) times the learning rate (`CORE.md:39`). The tracking term is that learning rate: the general floor (`CORE.md:70`), the random-walk floor (`CORE.md:76`, `THEORY.md:295`), the OU and telegraph floors (`CORE.md:90`, `CORE.md:94`), and the clock between looks (`theory/CLOCK_TERM_2026-11-23.md:11`, `:19`, `:35`). The world's rates are measured inputs (`THEORY.md:35`). Upkeep \(hK\), the separate read price \(A\), the link price \(L\), the stake \(w\), and the ruin cap stay assumed (`CORE.md:40-44`); temperature does not set \(w\) (`CORE.md:29`). They are not scored.

A quantum-record price is the modeling choice in `PREREG.md`: \(I_{\mathrm{mem}}\) is not replaced by a von Neumann entropy or a Holevo quantity, because R1 fixes Shannon mutual information for classical records only (`CORE.md:52`). Margolus–Levitin, Mandelstam–Tamm, and the Bekenstein-type bounds are read as external ceilings on a carrier one has chosen to treat as quantum.

## What each bridge puts in the monomial

Bath temperature \(T\) is the intensive partner of the \(k_B\) exchange. It is not a third constant. A pure numerical factor is not part of the score (`PREREG.md`).

**Erasure.** The repository states Landauer's cost as at least \(kT\ln 2\) per bit (`theory/SCALE_ENDS.md:23`). That is \(k_B T\) times a dimensionless count. The 1961 text was not opened. The finite-time paper (Proesmans, Ehrich, and Bechhoefer 2020) was not opened, so no finite-time formula is scored. The quasistatic cost is the one in the table.

**Ongoing heat and the tracking floors.** \(\dot Q_M\ge kT\,\dot I_M\) (`CORE.md:70`). The same \(k_B T\) multiplies a rate the cost already takes: \(\sigma^2/(2D)\) (`THEORY.md:295`), \(a(v-\varepsilon)/\varepsilon\) (`CORE.md:90`), and the telegraph flow (`CORE.md:94`). Each rate is \(1/\mathrm{time}\) once the error is in the world's own units. \(\hbar\) does not appear.

**Clock.** The TUR price is \(kT\,\omega'^2/D\) (`theory/CLOCK_TERM_2026-11-23.md:35`). Phase is dimensionless in that note, so \(\omega'\) and \(D\) are both rates and \(\omega'^2/D\) is a rate. The only dimensionless group of the small-angle model is \(c/(\kappa kT)\) (`theory/CLOCK_TERM_2026-11-23.md:60`). Again \(k_B\) alone.

**Margolus–Levitin.** The 1998 abstract says the bound depends only on \(E-E_0\). The repository records \(\mathrm{ops/s}\le 2E/(\pi\hbar)\) (`theory/SCALE_ENDS.md:169`). Both are a time \(\hbar\) over an energy. This note does not add a prefactor. An imported \(E-E_0\) is monomial (B), labeled INPUT; as the tracking term's own time the row is F3, because the tracking term does not name \(E-E_0\). Setting that energy to \(k_B T\) times a nat count gives \(\hbar/(k_B T)\), F1. The reserve \(B\) is a buffer in the system's one currency (`THEORY.md:34`, `:209`, `:36`), and the only scale the cost gives it is the buffer it needs, \(B\ge z_\varepsilon\cdot\sigma\sqrt{\tau}\) (`THEORY.md:82`, CT25), built from the world's shock scale \(\sigma\), a measured input (`THEORY.md:35`): where \(\sigma\) is \(kT\) times a pure number, \(\hbar/B=\hbar/(kT\cdot n)\) is F1 (`PREREG.md:28`), the same combination as the Margolus–Levitin plus Landauer row, and where \(\sigma\) is an outside energy, \(\hbar/B\) is monomial (B) labeled INPUT, or F3 as the tracking term's own time (`PREREG.md:24`, `:30`); the locked rule fixes both, and neither is the cost supplying \(\hbar\), so a run would teach nothing, while \(B\) is energy held to be spent and \(E-E_0\) is the evolving carrier's energy above its ground state, so treating them as the same thing is an extra bridge assumption, a labeled CONJECTURE that needs its own preregistration, and only once a model makes the reserve literally the carrier's energy.

**OPEN.** Whether a carrier with a stated \(E-E_0\) can run the cost-optimal rate, fixed by the tracking floors from world rates and \(kT\) (`CORE.md:90-94`), at \(\mathrm{rate}^*\le 2(E-E_0)/(\pi\hbar)\) (`theory/SCALE_ENDS.md:169`): a feasibility check that uses \(\hbar\) as an exchange rate, not a derivation of \(\hbar\), and not run here.

**Mandelstam–Tamm.** Deffner and Campbell 2017 treat this as a quantum speed limit. The 1945 text was not opened, so the orthogonalization prefactor is not re-derived. The conversion that was checked is \(\hbar/\Delta E\). \(\Delta E\) is not a width the tracking term names (F3).

**Bekenstein-type stock.** The repository states \(E/S\ge\hbar c/(2\pi R)\) (`theory/SCALE_ENDS.md:163`). The dimensionless count is \(ER/(\hbar c)\): \(\hbar\), \(c\), and a length (F1 and F3). The printed entropy \(S=kA/(4\ell_p^2)=4\pi k GM^2/(\hbar c)\) (`theory/SCALE_ENDS.md:161`) carries a factor \(k\) and is also given as a nat count. Dividing out \(k\) leaves \(4\pi GM^2/(\hbar c)\). The script checks \(GM^2/(\hbar c)\); the \(4\pi\) is a pure number and is not part of the score. The combination contains \(\hbar\), \(c\), and \(G\). Lloyd's 2000 abstract says the limits it explores are set by \(c\), \(\hbar\), and \(G\). No formula from that paper was dimension-checked. Naming those three constants across the paper is not one monomial. The speed limit inside that paper is the Margolus–Levitin bound, already its own row. The stored log still scores the row fail F1+F3 (`dimension_check.out`). That score is not adopted. Logged deviation: the row is NOT SCORED / abstract only.

## Results

Scores are the locked rule applied by `dimension_check.py`. The stored run is `dimension_check.out`.

| Term | Bridge | Constant | Combination | Score |
|---|---|---|---|---|
| Memory erasure | Landauer (`SCALE_ENDS.md:23`) | \(k_B\) | \(k_B T\times\) nats | pass (A) |
| Ongoing memory heat | Horowitz–Esposito (`CORE.md:70`) | \(k_B\) | \(k_B T\times\) (nats/time) | pass (A) |
| Tracking floors | CT7, OU, telegraph (`THEORY.md:295`, `CORE.md:90`, `CORE.md:94`) | \(k_B\) | \(k_B T\times\) (world rate) | pass (A) |
| Clock | TUR, Barato–Seifert (`CLOCK_TERM_2026-11-23.md:35`) | \(k_B\) | \(k_B T\times(\omega'^2/D)\) | pass (A) |
| Speed, mean energy | Margolus–Levitin (`SCALE_ENDS.md:169`) | \(\hbar\) | \(\hbar/(E-E_0)\) | (B) given an imported \(E-E_0\), labeled INPUT; as the tracking term's own time, F3 |
| Same speed, energy set to the erasure cost | Margolus–Levitin composed with Landauer | \(k_B\) and \(\hbar\) | \(\hbar/(k_B T)\) | fail (F1) |
| Speed, energy spread | Mandelstam–Tamm (prefactor not re-derived) | \(\hbar\) | \(\hbar/\Delta E\) | fail (F3) |
| Stock bound | Bekenstein 1981 (`SCALE_ENDS.md:163`) | \(\hbar\) and \(c\) | \(ER/(\hbar c)\) | fail (F1+F3) |
| Printed entropy count | `SCALE_ENDS.md:161`, \(k\) divided out | \(\hbar\), \(c\), and \(G\) | \(GM^2/(\hbar c)\) | fail (F1+F3) |
| Ultimate laptop | Lloyd 2000, abstract only | \(c\), \(\hbar\), and \(G\) | not checked as a formula | NOT SCORED / abstract only |

The four \(k_B\) rows cannot miss. \(k_B T\) as an energy is the definition of \(k_B\), and \(k_B T\) times a rate is that energy per time. Given the formulas `PREREG.md` already cites, those passes are a consistency check, not a test. The speed row is (B) given an imported \(E-E_0\), labeled INPUT, and F3 as the tracking term's own time. The reserve sentence is with the Margolus–Levitin paragraph. Four dimension-checked rows pass and five fail. The stored log counts Lloyd as a sixth fail (`dimension_check.out`). This table does not. That departure is the logged deviation above: the row is NOT SCORED / abstract only, and its speed limit is the Margolus–Levitin row. Every identity in the script holds (`DIMENSIONS OK`). The stored output is unchanged.

## What was learned

The classical memory and tracking heat already in the repository is \(k_B T\) per nat, or per nat per time. \(\hbar\) does not enter those formulas. That \(k_B\) pass cannot miss: \(k_B T\) as an energy is the definition of \(k_B\), so the four rows are a consistency check, not a test. A quantum speed limit prices time as \(\hbar\) over an energy. The tracking term does not name that energy. An imported \(E-E_0\) is labeled INPUT. Inserting \(k_B T\) into the tracking term's time mixes the two constants. The reserve is scored by the locked rule in the Margolus–Levitin paragraph, with no new run. A Bekenstein-type stock bound mixes \(\hbar\) with \(c\) and a length, and the printed entropy count mixes in \(G\) as well. On the scored bridges, \(k_B\) and \(\hbar\) sit in separate slots. The fused thermal time and the stock bound are open questions about those bridges. They are not an established limit on every coupling. Lloyd's abstract was not scored. The question stays open.

Only dimensionless constants are candidates for prediction. The fine-structure constant is the example. That question is the nested-layer fixed point, a conjecture and untested, on branch `ace-probe-memos-2026-11-23` in `theory/probes-2026-11-23/MIRROR_MEMO.md` (the paragraph that begins "The only legitimate pattern found: a fixed point of a nested-layer map", and the claim-map row "Nested-layer fixed point gives a universal GTAO number"). This note does not take it up. That work's open-work id is T69.

## ERRATA

Checked against `theory/reviews/CONSTANTS_EXCHANGE_REVIEW_2026-11-24.md` (`dc28752`), which reviewed `587c99f`. `PREREG.md`, `dimension_check.py`, and `dimension_check.out` are unchanged. Accept means the review's claim holds.

**1. Preregistration order. Accept.** `0846e2e` (2026-11-24 04:53:04 UTC) is the parent of `587c99f` (2026-11-24 05:03:45 UTC). The first commit is the lock. The second is the memo and the dimension log. No change.

**2. `THEORY.md`. Accept.** This branch does not change `THEORY.md`. Upstream `main` is `0f37918`. No change.

**3. Crossref. Accept.** The review re-fetched the 15 DOIs and the three arXiv abstracts. Titles, authors, and years stand. No 1945 journal record was required. The 1945 text stays unopened. No change.

**4. Dimension identities. Accept.** The stored log still reports `DIMENSIONS OK`, four passes, and six fails, and it says the sixth fail is not an identity (`dimension_check.out`). The identities are unchanged. The sixth fail is the Lloyd deviation in item 10.

**5. Classical \(k_B\) reading. Accept.** Erasure, the ongoing floor, the tracking floors, and the clock, at the lines the review cites, are \(kT\) times a count or a rate. None of those expressions contains \(\hbar\), \(c\), or \(G\). The mapping stays an interpretation.

**6. The \(k_B\) pass cannot miss. Accept.** \(k_B T\) as an energy is the definition of \(k_B\). \(k_B T\) times a rate is that energy per time. The script is handed `constants=("k_B",)` for those four rows (`dimension_check.py:67-111`). P1–P3 already name monomial A (`PREREG.md:36-38`). Given those lines, the pass was fixed before the script ran. It is a consistency check, not a test. The stored log still prints `pass A`. The results section now says so. The log is not edited.

**7. Margolus–Levitin and Mandelstam–Tamm. Accept.** The tracking-term fail stays F3. The composed row stays F1. A thermal width \(\Delta E\sim k_B T\) would be that same F1 for Mandelstam–Tamm. It is not a separate row. The unsubstituted F3 stands. The review reads the 1998 orthogonalization time as a pure number times \(\hbar\) over an energy, and the abstract's rate as another pure number times the same ratio. This note still does not choose a prefactor. The 1945 text stays unopened.

**8. "The cost does not name the energy." Accept.** At `587c99f`, `MEMO.md:25` said the cost does not name \(E-E_0\), and `MEMO.md:52` said the energy is not fixed by the cost. Both now say the tracking term. The \(\Delta E\) sentence is narrowed the same way. At `dc28752` the ruin reserve was not scored. Ace's later note scores it by the locked rule in the Margolus–Levitin paragraph, with no new run. The F3 score for the tracking term is unchanged.

**9. Bekenstein and the printed entropy. Accept.** The 1981 row stays \(\hbar\), \(c\), and a length. Dividing \(k\) out of `theory/SCALE_ENDS.md:161` leaves \(4\pi GM^2/(\hbar c)\). The script checks \(GM^2/(\hbar c)\) (`dimension_check.py:161-171`). The \(4\pi\) is a pure number. This note does not recompute the solar-mass count. No change.

**10. Lloyd 2000. Accept.** The stored line is `reading lloyd-2000: ... score fail F1+F3`, and `n_fail += 1` is unconditional (`dimension_check.py:216-219`). No formula was checked. P6's miss input is a dimensionless count (`PREREG.md:41`). None was computed for Lloyd. The speed limit inside that paper is the Margolus–Levitin row. Logged deviation: the memo table says NOT SCORED / abstract only. `dimension_check.out` is not edited, and it still counts the line as the sixth fail.

**11. Scope wording. Accept.** The cost alone is dimensionless (nats times stakes) and on its own cannot set a physical scale. Once coupled to physics, dimensional constants may enter as exchange rates, and whether they do is an open question, not an established limit. This note does not claim that \(\hbar\), \(c\), or \(G\) cannot arise. Misses stay open questions about the bridge. No change.

**12. Wording rules. Accept.** The new files and the open-work row keep those rules. No change required by this item.

**13. The loose citation. Accept.** `PREREG.md:11` is not edited. It cites `theory/AREA_LAW_PROBE_2026-11-23.md:17` for the sentence that the cost contains neither \(G\), \(\hbar\), nor \(c\). Line 17 says the extra input uses no \(\hbar\) or \(G\), and that a gravitational ingredient is one the cost does not supply. It does not name \(c\). Line 135 says the packing input does not use Newton's constant. The absolute sentence is `theory/PHYSICS_CHAIN_2026-11-23.md:73`. The opening of this memo now cites that line.

**14. The T69 collision. Accept.** At `587c99f` this note's open-work row was T69, the same id as the nested-layer row on `forge-layer-fixed-point` (`2be9290` at review time). This note's row is now T70. The parallel ids are layer T69, constants T70, information causality T71, composite T72, pointer T73. The review file still says T69, which is the id it reviewed. The test docstring now says T70.
