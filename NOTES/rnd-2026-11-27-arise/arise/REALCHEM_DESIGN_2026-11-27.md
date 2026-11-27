# REALCHEM design pass: taking the P4 rule to a real reaction network

*2026-11-27 (EST), Chad t196u. Labels: observed / hypothesis / proved-in-model (PIM) / known. No physics claims. All DOIs were verified on Crossref (realchem/crossref_realchem.out).*

## 1. Candidates and choice

| System | Exclusive, heritable cores? | Measured rate constants? | Timed cue | Price | Fit for this use |
|---|---|---|---|---|---|
| E. coli RAF sets (Sousa, Hordijk & Steel 2015, 10.1186/s13322-015-0009-7) | known: overlapping irrRAFs | no compartment kinetics | n/a | n/a | structure only |
| Formose (Breslow 1959, 10.1016/S0040-4039(01)99487-0) | autocatalytic; exclusive cores not shown | partly | hard | hard | poor fit |
| RNA cooperative networks (Vaidya 2012, 10.1038/nature11549) | known: cooperative vs selfish | assembly rates in part | possible | possible | good, fewer constants |
| Peptide replicator networks (Ashkenasy 2004, 10.1073/pnas.0402674101) | network logic shown | some | possible | unclear | small networks |
| Cross-replicating ribozymes (Lincoln & Joyce 2009, 10.1126/science.1167856) | competing replicators | yes | weak | yes | runner-up |
| Micelles/vesicles (Bachmann/Luisi/Lang 1992, 10.1038/357057a0; Zhu & Szostak 2009, 10.1021/ja900919c) | division is real; no internal memory | partly | n/a | n/a | compartment layer only |
| Bistable organic network (Semenov 2016, 10.1038/nature19776) | known: bistable, oscillating | yes | possible (flow) | unclear | runner-up; no compartments |
| DNA strand displacement (Qian & Winfree 2011, 10.1126/science.1200520; Qian/Winfree/Bruck 2011, 10.1038/nature10262; Cherry & Qian 2018, 10.1038/s41586-018-0289-6; Pandi 2019, 10.1038/s41467-019-11889-0) | no autocatalysis (fuel-driven) | yes | yes | yes | strong reader layer; weak heredity |
| **PEN DNA toolbox** (Montagne 2011, 10.1038/msb.2010.120; Padirac 2012, 10.1073/pnas.1212069109; Rondelez 2012, 10.1103/PhysRevLett.108.018102; Genot 2012, 10.1103/PhysRevLett.109.208102; Genot 2016, 10.1038/nchem.2544) | **known: bistable switchable memories** (Padirac 2012) | **known: Table 1** (Montagne 2011) | input-strand pulse | **enzyme load / competition** (Rondelez 2012) | **chosen** |

**Why PEN.** It is the only candidate where all of the following are published together:
- exclusive autocatalytic cores that are bistable through cross-inhibition (heredity substrate);
- measured kinetics (Montagne Table 1);
- a natural, measurable price — enzymes are shared, so extra template slows the cores (Rondelez 2012);
- droplet-scale experiments for a compartment layer (Genot 2016).

Each P4 condition maps to something a wet lab can set: a cross-inhibited memory (heredity), a pulsed input strand (timed cue), and reader-template enzyme load (priced reading).

## 2. Mapping table (toy → PEN)

| Toy (P4b–P4h) | PEN quantity | Source / status |
|---|---|---|
| exclusive cores (LV pair) | two autocatalytic templates, cross-inhibited | Padirac 2012 (known) |
| core growth rate | k_pol 17, nick 3.0 min⁻¹; k_a 26×10⁶ M⁻¹min⁻¹; k_d 2.3 min⁻¹ | Montagne 2011 Table 1 (known) |
| inhibition strength | k_d^(Inh/T1) 0.0057 min⁻¹ (~400× tighter than trigger) | Montagne 2011 Table 1 (known) |
| decay | RecJf exo: 0.32 (trigger), 1.2 (inhibitor) min⁻¹ | Montagne 2011 Table 1 (known) |
| molecule count M | droplet volume V × concentration | Genot 2016 droplets (volume range to measure) |
| nucleation μ (novelty) | untemplated (leak) synthesis per droplet | **unpublished; must measure** |
| Poisson split | droplet split / passage | **stand-in;** PEN droplets do not divide |
| toxin pulse τ | timed input strand that degrades/blocks the cores | design (hypothesis) |
| cue/lag reader | reader template primed by the cue, giving an anti-toxin output | design; **no published kinetics** |
| price c per nat | core slowdown per unit of reader template (enzyme load) | concept known (Rondelez 2012); Michaelis constants in Montagne's supplement, **not retrieved** (PMC returned a challenge page, not the PDF) |

## 3. What must be measured
1. Leak (untemplated synthesis) rate per template at working enzyme concentrations.
2. Polymerase and nickase saturation constants (Montagne supplement, or re-measured).
3. Reader-template kinetics: cue-primed output rate and enzyme load.
4. Droplet volumes, and a lineage method (split/fuse droplets, or a serial-transfer surrogate).
5. Core growth slowdown vs reader concentration — this is the price c.

## 4. Predictions (hypotheses until run)
- **P-threshold (from P4g, PIM in the toy).** Under selection with a timed toxin and a read-only-when-used reader, the reader persists only if price < c*. The c* reached by evolution should fall within a factor of 2 of the c* from a head-to-head designed contest (the toy gave 0.511 vs 0.617). Above c*, reader load drops to background.
- **P-band (from P4g P-high and S1).** The benefit of reading falls as novelty rises. In PEN, novelty is set by leak × droplet volume against inhibitor strength (S1 observation). There should be a leak × V window with κ ≥ 0.5 and nonzero switching, cores locked on one side, mixed states on the other.
- **P-timing (from P4f/P4h).** Reader enrichment under a timed cue should exceed enrichment under an untimed cue at equal total cue dose.

## 5. Nulls
- **Heredity-off:** pool and redistribute droplet contents each passage (break lineage). The toy predicts detox advantage A → 0 (P4f F-tests).
- **Untimed cue:** same total input strand, spread flat. P-timing predicts no reader enrichment over cost.
- **No price:** reader free to express. The hold rule predicts the reader is retained regardless of cue, so timing carries no information.

## 6. What counts as a miss
- **P-threshold miss:** evolved c* off designed c* by more than a factor of 2, or readers persist above c*.
- **P-band miss (tested in S1, see §9):** no leak × V window gives both κ ≥ 0.5 and nonzero switching within reachable droplet sizes — real PEN noise gives either full heredity or none.
- **P-timing miss:** timed and untimed cues enrich the reader equally.

## 7. What is already known (state honestly)
- Experimental in-vitro learning in DNA circuits exists (Cherry & Qian 2025, 10.1038/s41586-025-09479-w) — but that is supervised, not Darwinian selection.
- Classical conditioning in DNA is a design only, not demonstrated (Nakakuki 2024, 10.1021/acssynbio.3c00459).
- PEN bistable memories, enzyme competition, and droplet kinetics are published (Padirac 2012; Rondelez 2012; Genot 2016). What is new here is testing the P4 *threshold-price* and *novelty-band* rules on these constants.
- The anticipation result (McGregor 2012) is in silico, not wet-lab.

## 8. Judgment-rule score
- Open: can the P4 threshold-price and novelty-band predictions fail on real measured constants? Yes.
- EIV: p ≈ 0.35 that at least one prediction is cleanly failable in silico with published constants; B_open high (connects M1/M5 to a measurable system); B_known moderate. Discounted ×0.6.
- Cost: the core-switch S1 is ~0.5 h; the full reader/price run is blocked on unpublished constants (needs wet-lab or supplement). 
- Call: run S1 now (feasible, cheap, failable); defer reader/price to a measurement pass. This matches the hold rule — stake × need > upkeep only for S1.

## 9. Feasibility and the S1 result
- **Feasible now with published constants:** the heredity substrate only (the cross-inhibited bistable switch). This is REALCHEM-S1 (prereg b6ef5292…, run pen_s1.out).
- **Not feasible with published constants:** the reader/price part — no reader-template kinetics are published, and enzyme-saturation constants were not retrieved. This is *why the full design pass is not a single late-night run*: two of the three conditions have no measured kinetics yet.
- **S1 result (details in realchem/RESULTS_REALCHEM_S1_2026-11-27.md):**
  - R1 PASS: bistability only for T_i ≥ 1 nM (none at 0).
  - R2 FAIL: κ dips to 0.49–0.67 at high leak.
  - R3 PASS but narrow: one of 15 cells (3 fL, leak 1e-2) is in the κ≥0.5/switch≥0.002 band.
  - R4 PASS but trivial (no switching at low leak).
  - **Observed:** intrinsic molecular noise alone never flips a state (inhibitor binding ~400× tighter than trigger); in this model novelty comes from **leak**, not small molecule counts. So the toy's heredity–novelty axis maps onto *leak × volume vs inhibitor strength*, not droplet volume alone.
  - **Hostile review:** leak is unpublished and decides the band; the band is 1/15 cells; the model drops enzyme saturation/competition; passaging is a stand-in. S1 supports the band's existence only weakly and needs the leak rate measured.
