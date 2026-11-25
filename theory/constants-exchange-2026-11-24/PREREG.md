# Preregistration: do \(k_B\) and \(\hbar\) enter as exchange rates?

*Tuesday 24 November 2026 (UTC). Locked before the dimension check in `MEMO.md`. Written against `main` `0f37918`. `THEORY.md` is not edited. No real-world series was opened. This file states the claim, the fail inputs, the prior art, and the pass/fail rule. It does not score them.*

The hypothesis sentence is the one at `CORE.md:7`. This note does not restate it.

## The claim

The cost alone is dimensionless (nats times stakes). On its own it cannot set a physical scale. The memory coordinate is a number of nats (`THEORY.md:30`; `CORE.md:33`; Theorem R1 at `CORE.md:52`). The stake \(w\) and the other prices are the currency (`THEORY.md:36`: only dimensionless ratios matter, and the optimal cost shares are currency-free). Nothing in that product is a joule or a second until a conversion is supplied.

Once the cost is coupled to physics, dimensional constants may enter as exchange rates. Whether they do, and in what combination, is an open question, not an established limit. Earlier notes say the cost contains neither \(G\), \(\hbar\), nor \(c\) (`theory/AREA_LAW_PROBE_2026-11-23.md:17`, `theory/PHYSICS_CHAIN_2026-11-23.md:73`). That wording is too absolute. This note does not adopt it.

**Claim C, the question this note locks.** When the memory term and the tracking term are given a physical energy and a physical time, do \(k_B\) and \(\hbar\) enter exactly as the exchange rates that conversion needs, and nowhere else?

It is a miss if, in a formula used below, the constants enter in a different combination, or the cost needs a different scale, or an extra dimensionful input. A miss is a puzzle about that bridge. It is not a limit on every later coupling, and it does not fix the value of \(k_B\), \(\hbar\), \(c\), or \(G\).

Only dimensionless constants are candidates for prediction. The fine-structure constant is the example. That question is handled by the nested-layer fixed point (a fixed point of the nested-layer map, conjectured and untested), on branch `ace-probe-memos-2026-11-23`, in `theory/probes-2026-11-23/MIRROR_MEMO.md` (the paragraph that begins "The only legitimate pattern found: a fixed point of a nested-layer map", and the claim-map row "Nested-layer fixed point gives a universal GTAO number"). This note does not touch it.

## What would count as the exchange rates

Two monomials are allowed. A pure numerical factor does not matter.

- **(A) Energy.** \(k_B \times T \times\) (a dimensionless information, or an information rate). The time in the rate is one the cost already takes: the world's spectrum or kernel (`THEORY.md:35`), or the clock's own rate and diffusion. The only dimensional constant in the monomial is \(k_B\). The bath temperature \(T\) is the intensive partner of that exchange rate, not a third constant.
- **(B) Time.** A pure number times \(\hbar / E\) or \(\hbar / \Delta E\), where that energy is already named by the coupling under test. The only dimensional constant in the monomial is \(\hbar\).

Anything else is a miss:

- **(F1) Different combination.** \(k_B\) and \(\hbar\) in one monomial, or either one together with \(c\) or \(G\). The quotient \(\hbar/(k_B T)\) is F1. It is not two separate exchange rates sitting in two slots.
- **(F2) Different scale.** A scale that is neither \(k_B T\) nor \(\hbar\) over a named energy.
- **(F3) Extra dimensionful input.** A length, \(c\), \(G\), or an energy the term does not already name.

## Predictions, and the input under which each misses

The memory term is \(\kappa I_{\mathrm{mem}}\) in the five-term display, replaced in the physical class by the bath heat (`CORE.md:39`: the stock rental is not the coordinate; the floor is \(kT\) times the learning rate). The tracking term is that learning rate, the worked-class floors, and the clock between looks.

1. **P1, erasure.** Landauer's cost of erasing the memory, as the repository already states it (`theory/SCALE_ENDS.md:23`: at least \(kT \ln 2\) per bit). Misses if that cost is not monomial (A).
2. **P2, ongoing heat.** The floor \(\dot Q_M \ge kT\,\dot I_M\) (`CORE.md:70`) and the tracking floors that use it: the random-walk floor \(kT\cdot\sigma^2/(2D)\) (`THEORY.md:295`, CT7), the OU and telegraph floors (`CORE.md:90`, `CORE.md:94`). Misses if any of those formulas is not monomial (A). The world's rates are the input at `THEORY.md:35`, not a new constant.
3. **P3, clock.** The TUR price of an internal clock, \(\kappa kT\,\omega'^2/D\) (`theory/CLOCK_TERM_2026-11-23.md:11`, `:35`). Misses if that price is not monomial (A).
4. **P4, Margolus–Levitin.** The 1998 bound depends only on the mean energy above the ground state (abstract, below). The repository records \(\mathrm{ops/s}\le 2E/(\pi\hbar)\) (`theory/SCALE_ENDS.md:169`). Misses if that time is not monomial (B) with energy \(E-E_0\), or if the only energy the cost can put there is \(k_B T\) times a nat count (that substitution is F1), or if \(E-E_0\) is an energy the cost does not name (F3).
5. **P5, Mandelstam–Tamm.** An energy–time limit whose time is \(\hbar\) over an energy width (the speed-limit reading in Deffner and Campbell 2017; the 1945 text was not opened). Misses if \(\Delta E\) is an energy width the cost does not name (F3), or if the published relation is not of the form (B).
6. **P6, Bekenstein-type stock.** The 1981 bound as the repository states it, \(E/S \ge \hbar c/(2\pi R)\) (`theory/SCALE_ENDS.md:163`), and Lloyd's 2000 limits, which the abstract says are set by \(c\), \(\hbar\), and \(G\). Misses if the dimensionless count is not (A) or (B): a length, \(c\), or \(G\) is F1 and F3.

P1 is the quasistatic cost the repository uses. Proesmans, Ehrich, and Bechhoefer 2020 is the finite-time erasure paper. Its text was not opened, so no finite-time formula is an input. A later opening that found a scale other than (A) would be a new preregistration, not a patch of P1.

## Modeling choice Q (quantum record)

**Choice.** This note does not replace \(I_{\mathrm{mem}}\) by a von Neumann entropy or a Holevo quantity. Margolus–Levitin, Mandelstam–Tamm, and the Bekenstein-type bounds are scored only as external ceilings on a carrier that one has chosen to treat as quantum.

**Reason.** Theorem R1 fixes Shannon mutual information for classical records: Shannon information on a finite alphabet, and, when the mutual information is finite, the Gelfand–Yaglom–Dobrushin supremum (`CORE.md:52`; `theory/REPRESENTATION.md` A6; `theory/CONTINUOUS_A6_2026-11-23.md:13-26`). It does not fix a quantum information coordinate. A price quoted for a quantum record is therefore a modeling choice, not a consequence of R1.

## Pass/fail rule for the memo

The memo may check dimensions of the formulas named above. It may not change Claim C, the two monomials, or the fail inputs. A formula that is (A) or (B), and no other dimensional constant, is a pass for that bridge. A formula that hits F1, F2, or F3 is a miss, reported as a puzzle about that bridge. The mapping from a GTAO term to a bridge is an interpretation unless a dimension identity is all the memo claims, in which case that identity is elementary. The memo does not predict a dimensionless constant, and it does not state values of \(\hbar\), \(c\), or \(G\).

## Prior art

Resolved on the Crossref API (`https://api.crossref.org/works/<doi>`) on 24 November 2026. Title, authors, and year below are the record's. The log is `crossref.out`. Abstracts quoted from arXiv were fetched the same day from `export.arxiv.org`. Texts not opened are marked.

- **Landauer 1961.** R. Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development*, doi `10.1147/rd.53.0183`, year 1961. No abstract in the record. Text not opened. The repository's statement is \(kT\ln 2\) per bit (`theory/SCALE_ENDS.md:23`).
- **Sagawa and Ueda 2009.** Takahiro Sagawa; Masahito Ueda, "Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure," *Physical Review Letters*, doi `10.1103/PhysRevLett.102.250602`, year 2009. Erratum: doi `10.1103/PhysRevLett.106.189901`, year 2011, same authors. The repository's use is a floor on the sum of measurement and erasure (`theory/SHANNON_2026-11-21.md:29`).
- **Horowitz and Esposito 2014.** Jordan M. Horowitz; Massimiliano Esposito, "Thermodynamics with Continuous Information Flow," *Physical Review X*, doi `10.1103/PhysRevX.4.031015`, year 2014. This is the source of the floor at `CORE.md:70`.
- **Margolus and Levitin 1998.** Norman Margolus; Lev B. Levitin, "The maximum speed of dynamical evolution," *Physica D*, doi `10.1016/S0167-2789(98)00054-2`, year 1998. arXiv `quant-ph/9710043` abstract: previous bounds use the standard deviation of the energy; their bound depends only on \(E-E_0\), the average energy minus the ground-state energy; one joule raises the processing rate by at most about \(3\times 10^{33}\) operations per second. The repository's prefactor \(2E/(\pi\hbar)\) is its own record (`theory/SCALE_ENDS.md:169`), not a re-derivation here. Both are an energy in the denominator of a time. This preregistration does not add a third prefactor.
- **Mandelstam and Tamm.** A Crossref query for the 1945 paper returned no 1945 works record. The reprint that did resolve: L. Mandelstam; Ig. Tamm, "The Uncertainty Relation Between Energy and Time in Non-relativistic Quantum Mechanics," *Selected Papers*, pages 115–123, doi `10.1007/978-3-642-74626-0_8`, year 1991. No abstract. Text not opened. **Deffner and Campbell 2017.** Sebastian Deffner; Steve Campbell, "Quantum speed limits: from Heisenberg's uncertainty principle to optimal quantum control," *Journal of Physics A*, doi `10.1088/1751-8121/aa86c6`, year 2017. arXiv `1705.08023` abstract: the Mandelstam–Tamm and Margolus–Levitin bounds are milestones of the quantum speed limit. **Bhattacharyya 1983.** K Bhattacharyya, "Quantum decay and the Mandelstam-Tamm-energy inequality," *Journal of Physics A*, doi `10.1088/0305-4470/16/13/021`, year 1983, pages 2993–2996. No abstract. Text not opened. P5 uses only the speed-limit reading those titles support: a time set by \(\hbar\) and an energy width. The numerical factor in the orthogonalization corollary is not an input, because the 1945 text was not opened.
- **Bekenstein 1981.** Jacob D. Bekenstein, "Universal upper bound on the entropy-to-energy ratio for bounded systems," *Physical Review D*, doi `10.1103/PhysRevD.23.287`, year 1981. Repository statement: \(E/S \ge \hbar c/(2\pi R)\) (`theory/SCALE_ENDS.md:163`). **Bekenstein 1973.** Jacob D. Bekenstein, "Black Holes and Entropy," *Physical Review D*, doi `10.1103/PhysRevD.7.2333`, year 1973. **Bousso 2002.** Raphael Bousso, "The holographic principle," *Reviews of Modern Physics*, doi `10.1103/RevModPhys.74.825`, year 2002. **Casini 2008.** H Casini, "Relative entropy and the Bekenstein bound," *Classical and Quantum Gravity*, doi `10.1088/0264-9381/25/20/205021`, year 2008.
- **Lloyd 2000.** Seth Lloyd, "Ultimate physical limits to computation," *Nature*, doi `10.1038/35023282`, year 2000. arXiv `quant-ph/9908043` abstract: the limits it explores are set by \(c\), \(\hbar\), and \(G\).
- **Barato and Seifert 2015.** Andre C. Barato; Udo Seifert, "Thermodynamic Uncertainty Relation for Biomolecular Processes," *Physical Review Letters*, doi `10.1103/PhysRevLett.114.158101`, year 2015. Source of the clock price in `theory/CLOCK_TERM_2026-11-23.md`.
- **Proesmans, Ehrich, and Bechhoefer 2020.** Karel Proesmans; Jannik Ehrich; John Bechhoefer, "Finite-Time Landauer Principle," *Physical Review Letters*, doi `10.1103/PhysRevLett.125.100602`, year 2020. No abstract in the record. Text not opened. Not an input to P1–P6.

Grep before this lock, on `main` `0f37918`: "Margolus" is in `theory/SCALE_ENDS.md` and the gravity-barrier note; "Mandelstam" does not appear; "Landauer" and "Bekenstein" appear as above. No file `theory/constants-exchange-2026-11-24/` existed.
