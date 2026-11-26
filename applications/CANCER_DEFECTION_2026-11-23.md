# Cancer as defection from the body's judgment

*Monday 23 November 2026. Canonical home for one application of the cost to a cell lineage inside a tissue. Not a test of the hypothesis. No new theorem: the math is CT9 and CT29's alignment clause (`THEORY.md`, Appendix B.2 and B.10). `THEORY.md` is not edited. The hypothesis sentence is unchanged. Independently reviewed before this page was written (READY-WITH-FIXES; every fix applied).*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

Labels: **PROVED (in-model)** follows from a repo theorem inside its class. **INTERPRETATION** maps a theorem onto cells; the mapping is not proved. **CONJECTURE** is a named bet. **MEASUREMENT** is an input the theory does not supply. **KNOWN** is published and credited.

## 1. What this is

This page records how the cost is used for one system: a cell lineage that can follow or stop following its tissue. Applications are not evidence for the theory unless a test says so, and they are not the theory itself (`applications/README.md`).

It is one case of the swarm rule, the general statement of when parts join, stay with and leave a whole (`theory/SWARM_RULE_2026-11-23.md`); the AI-agent case is `applications/AI_AGENT_OVERSIGHT_2026-11-23.md`.

Write the cost, find its minimum, read off the design, and state which inputs are still measurements.

## 2. The failure

Cancer is the second leading cause of death in the United States (CDC FastStats, 2024 data: about 620,000 deaths, after heart disease). The main treatments remove or destroy the dividing cells, and resistance evolves under that pressure: on standard-dose abiraterone in metastatic castrate-resistant prostate cancer, median time to progression is about 16.5 months (Zhang et al. 2017, doi [10.1038/s41467-017-01968-5](https://doi.org/10.1038/s41467-017-01968-5)).

There is a second route, and it has worked:

- **APL.** All-trans retinoic acid (ATRA) made acute promyelocytic leukemia cells mature: 24 of 24 patients reached complete remission (one with low-dose cytarabine added), and 8 relapsed after 2–5 months on ATRA alone (Huang et al. 1988, *Blood*, doi [10.1182/blood.V72.2.567.567](https://doi.org/10.1182/blood.V72.2.567.567)). ATRA plus arsenic trioxide, without chemotherapy, gave 97% two-year event-free survival against 86% for ATRA plus chemotherapy in low-to-intermediate-risk APL (Lo-Coco et al. 2013, *NEJM*, doi [10.1056/NEJMoa1300874](https://doi.org/10.1056/NEJMoa1300874)). Arsenic also degrades the PML-RARA fusion protein that drives the disease, so this is maturation plus removal of the driver, not maturation alone.
- **Tissue over genotype in culture.** β1-integrin blocking antibodies reverted malignant human breast cells in 3D culture to growth-arrested acini and reduced tumors in nude mice. The phenotypes were reversible when the cells were dissociated and the antibodies removed (Weaver et al. 1997, *J Cell Biol*, doi [10.1083/jcb.137.1.231](https://doi.org/10.1083/jcb.137.1.231)).
- **Malignant cells in normal tissue.** Teratocarcinoma cells placed in blastocysts gave normal mosaic mice (Mintz & Illmensee 1975, *PNAS*, doi [10.1073/pnas.72.9.3585](https://doi.org/10.1073/pnas.72.9.3585)).
- **Bioelectric normalization.** Restoring membrane voltage reduced and normalized oncogene-induced tumor-like structures in *Xenopus*, a model system (Chernet & Levin 2014, doi [10.18632/oncotarget.1935](https://doi.org/10.18632/oncotarget.1935); Chernet et al. 2016, doi [10.18632/oncotarget.8036](https://doi.org/10.18632/oncotarget.8036)).

## 3. The cost, with named terms

The tissue issues instructions: divide or wait, differentiate, stay put, die. A cell lineage \(i\) can follow them or stop. Somatic selection acts on lineages, and tumors are large, strongly selected populations; under the hypothesis, that selection moves lineages toward the minimum of their own cost, in their own fitness currency.

The cell's cost per unit time, re-reading the tissue every \(T\) (drift-time units), is CT9's cost with a cost share and a private stake:

$$J_i(T)=\frac{\lambda\,s_i\,c}{T}+w_i\,A(T),\qquad J_i^{\text{stop}}=w_i\,r_\infty,\qquad P(\text{ruin of the organism})\le\varepsilon .$$

| Term | Meaning in the tissue | Status |
|---|---|---|
| \(\lambda\) | how fast the tissue's instructions change (wounding, inflammation, remodeling raise it) | MEASUREMENT |
| \(c\) | price of one read-and-follow (energy, division forgone, differentiation) | MEASUREMENT |
| \(s_i\) | share of that price the cell pays itself; the tissue subsidizes the rest (supplied factors, oxygen, matrix) | MEASUREMENT |
| \(w_i\) | the cell's private stake in following: how much its own growth and survival depend on acting as instructed. **It carries the enforcement**: contingent supply, anoikis, apoptosis, immune penalty. Without enforcement an instruction such as "die" has no value to the cell's own fitness | MEASUREMENT |
| \(A(T)\), \(r(u)\), \(r_\infty\) | average risk to the cell of acting on a reading of age \(u\); \(r_\infty\) if it ignores the tissue | model |
| \(\Phi=\int_0^\infty(r_\infty-r(u))\,du\) | what the tissue's signal is worth to the cell per unit stake. Signaling channels can carry about one bit (Cheong et al. 2011, doi [10.1126/science.1204553](https://doi.org/10.1126/science.1204553)) | MEASUREMENT |
| \(W\) | the organism's stake in this cell's compliance: its own loss per unit error in what this lineage does | MEASUREMENT |

## 4. The minimum

1. **When following pays (PROVED (in-model), CT9).** \(J_i=w_i\,[\lambda c'/T+A(T)]\) with \(c'=s_i c/w_i\), so this is CT9 with the read price replaced by the cell's net share \(s_ic/w_i\). CT9 then gives: following beats stopping iff
   $$\pi_i=\frac{\lambda\,s_i\,c}{w_i\,\Phi}<1 .$$
   The class is CT9's: a stationary Markov signal and renewal reads. The grid check in the scouting notes re-tests CT9 only; it is a code sanity check, not evidence about cells.
2. **One ratio sets the schedule (PROVED (in-model)).** While the cell follows, its schedule depends on \((s_i, c, w_i)\) only through \(s_ic/w_i\).
3. **Alignment (PROVED (in-model); KNOWN in form).** The organism's own schedule uses \(c/W\). The two match iff \(s_i=w_i/W\): the cell pays the share of the cost that matches its share of the stake. This is CT29's alignment clause (cost shares proportional to stakes implement the joint optimum) applied to one party. Its form is Lindahl or Pigou pricing (Samuelson 1954). It is not the multi-party free-riding game, and the price of anarchy is not used here.
4. **Five terms, and they multiply.** \(\log\pi=\log\lambda+\log s+\log c-\log w-\log\Phi\). The needed change is \(\log\pi\), and it can be split across the terms in any proportion. This is the same identity as item 1, not a second result.

## 5. The design, read off

The reading of CT9's "stop reading" as "stop following" is an **INTERPRETATION**. A cancer cell usually still reads tissue signals (growth factors, chemokines, matrix) and exploits them. What it stops doing is following the instructions that cost it fitness. CT9 values a reading by how much it improves the reader's own action. So the mapping holds only to the extent that \(w\) builds enforcement into the cell's own loss.

1. **A cancer cell is not bad in its own cost.** Under this interpretation, stopping is the lineage's minimum under the prices it faces. "Bad" is measured in the organism's cost.
2. **Five levers.** With the signal's information held fixed there are four.
   - Lower \(\lambda\): steady the tissue. Examples: resolve inflammation; normalize vasculature (Jain 2005, doi [10.1126/science.1104819](https://doi.org/10.1126/science.1104819)). Tumors have been called "wounds that do not heal" (Dvorak 1986, *NEJM* 315:1650, doi [10.1056/NEJM198612253152606](https://doi.org/10.1056/NEJM198612253152606)).
   - Raise \(\Phi\) or lower \(c\): restore the channel. Examples: matrix and polarity (Weaver 1997), gap junctions, membrane voltage (Levin), or a dose high enough to read through a block (ATRA in APL). Several of these raise the signal's worth \(\Phi\) rather than lower a price.
   - Lower \(s\): subsidize following, by supplying what the compliant state needs.
   - Raise \(w\): make the cell's own survival depend on following again, by restoring apoptosis and immune surveillance. Immunotherapy acts on this lever through selection. It removes lineages that do not follow; it does not change their minds.
3. **Mutations enter as changes to the terms (INTERPRETATION).**
   - Self-made growth signals and apoptosis evasion lower \(w\).
   - Receptor or gap-junction loss raises \(c\) or lowers \(\Phi\). A destroyed receptor sets that channel's \(c=\infty\).
   - Chronic wounding raises \(\lambda\).
   This is a mapping onto the hallmarks (Hanahan & Weinberg 2011, doi [10.1016/j.cell.2011.02.013](https://doi.org/10.1016/j.cell.2011.02.013)), not a derivation.
4. **Persistence.** In this memoryless class, a reverted lineage keeps following only while \(\pi<1\). That is a property of the class, which has no state. Real cells have epigenetic memory and hysteresis. Weaver 1997 is consistent with the class, not a confirmation of it. The design reading has two branches: keep the terms repriced (maintenance), or move the lineage into a terminal state. APL fits the second: matured granulocytes have a finite life, and arsenic removes the driver.
5. **Repriceable and channel-broken lineages.** Where a channel is intact somewhere downstream, the levers on \(\lambda\), \(\Phi\), \(c\) and \(s\) can act. Where it is cut at the receptor, only a bypass downstream, \(w\) (selection), or removal can. Genomics can measure which case holds before treatment.
6. **Remove or reprice (CONJECTURE, design reading).** Remove when the collateral is low, for a part the whole can lose cheaply. Reprice when the part is entangled. If the organism's ruin hazard \(H\) during the repricing time \(\tau_{\text{rep}}\) would break the cap, roughly \(H\,\tau_{\text{rep}}>\varepsilon\), reduce the burden first, then reprice. That inequality is written here and not derived. APL practice has this shape: ATRA plus arsenic for low-to-intermediate risk, cytoreduction added for high-risk disease. That is a fit in form, not a test.

7. **Reshaping the niche (INTERPRETATION).** A lineage that changes its own surroundings is acting on the tissue's signal, not only ignoring it. The swarm rule prices that action (`theory/SWARM_RULE_2026-11-23.md` §4). Evading immune killing escapes the penalty and corresponds to enforcement tampering. Remodeling the microenvironment's signals corresponds to channel tampering, which also costs the lineage the signal's worth to it. In the model, a lineage that pays a share of the cost of following matched to its stake (\(s=w/W\)) gains nothing from either, when it also shares the tissue's collateral and any priced ruin term (swarm rule §4).

So the math fixes the shape of the intervention: the condition, the five terms, the alignment rule \(s=w/W\), and maintain-or-terminate. It does not pick the cheapest lever in a given tumor (lever costs are measurements). It does not show that real lineages minimize this cost (that is the hypothesis). It does not show which channels are intact (a measurement).

## 6. Testable prediction, and what would count against it

**P1: the reversion contour (CONJECTURE; preregister before data).** In a reversion assay where the signal's change rate \(\lambda\) and the read price \(c\) can both be set, the 50% reversion contour is \(\pi=1\). That is a line of slope −1 in \(\log c\) against \(\log\lambda\). Candidate systems: 3D mammary culture, organoids, *Xenopus*.

That slope is a dimensional consequence. \(\lambda\) only rescales time and \(c\) is a per-read price, so with one clock they can enter only as \(\lambda c\). That is the form of Haber's rule in toxicology (concentration × time, long known). The test is informative only under conditions the preregistration must lock:

1. **A single random-switching clock.** The manipulated signal must be the only clock in what the cell reads, and it must be a stationary random-switching (telegraph) process, not a periodic pulse train. With a second, unmanipulated component the contour bends. In the review's check, slopes were −0.86 and −0.43 over two decades at weight 0.7 on the manipulated clock, and −0.57 and −0.14 at weight 0.3.
2. **Independent calibration of \(c\).** \(c\) must be calibrated against a measured fitness cost, independently of the reversion readout. Otherwise the test is circular.
3. **Heterogeneity.** The cell heterogeneity that makes a 50% contour must not depend on \((\lambda,c)\).
4. **A slope tolerance, set in advance.** An after-the-fact rescue by "other clocks" is not allowed.

*Against it:* under those conditions, a slope outside the preregistered tolerance, reversion that is not monotone in \(\pi\), or a reversion that lasts after the lever is removed without a terminal state. A miss stays open for this class.

**P2 (retrospective, CONJECTURE).** Differentiation and reversion therapies should work where the drivers act on \(w\), \(s\), \(\lambda\) or \(\Phi\), or where a drug reads through a block. They should do poorly where the receptor channel itself is destroyed. Candidate data: published differentiation-therapy cohorts. No numbers were pulled for this page.

## 7. Prior art, and the new part

**KNOWN, credited:**
- Cancer as cheating on the foundations of multicellular cooperation: Aktipis et al. 2015, doi [10.1098/rstb.2014.0219](https://doi.org/10.1098/rstb.2014.0219); Aktipis 2015, doi [10.1111/eva.12303](https://doi.org/10.1111/eva.12303).
- Cancer cells as disconnected from the tissue's collective, to be reconnected rather than only destroyed: Levin 2021, *Bioelectrical approaches to cancer as a problem of the scaling of the cellular self*, doi [10.1016/j.pbiomolbio.2021.04.007](https://doi.org/10.1016/j.pbiomolbio.2021.04.007). This is the closest prior art to this page's framing.
- Quantitative cooperation thresholds inside tumors, from growth-factor public goods: Archetti 2013, *BJC*, doi [10.1038/bjc.2013.336](https://doi.org/10.1038/bjc.2013.336); Archetti 2013, *Evol Appl*, doi [10.1111/eva.12092](https://doi.org/10.1111/eva.12092); review, Archetti & Pienta 2019, doi [10.1038/s41568-018-0083-7](https://doi.org/10.1038/s41568-018-0083-7).
- Tumor game theory: Axelrod, Axelrod & Pienta 2006, doi [10.1073/pnas.0606053103](https://doi.org/10.1073/pnas.0606053103).
- Ecology of differentiation therapy, which finds it often needs concurrent cytotoxics: Aguadé-Gorgorió & Solé 2019, bioRxiv, doi [10.1101/853002](https://doi.org/10.1101/853002).
- Cancer as an evolutionary and ecological process: Merlo et al. 2006, doi [10.1038/nrc2013](https://doi.org/10.1038/nrc2013).
- Atavism: Davies & Lineweaver 2011, doi [10.1088/1478-3975/8/1/015001](https://doi.org/10.1088/1478-3975/8/1/015001); Trigos et al. 2017, doi [10.1073/pnas.1617743114](https://doi.org/10.1073/pnas.1617743114).
- Tissue organization field theory: Soto & Sonnenschein 2011, doi [10.1002/bies.201100025](https://doi.org/10.1002/bies.201100025).
- Cancer as information loss: Gatenby & Frieden 2002, *Cancer Res* 62:3675.
- Reversion: Mintz & Illmensee 1975; Weaver et al. 1997 (Bissell lab).
- Differentiation therapy: Huang et al. 1988; Lo-Coco et al. 2013.
- Adaptive therapy: Zhang et al. 2017.
- Lindahl shares: Samuelson 1954.
- Haber's rule.

**New, as far as found** (several targeted searches; not exhaustive):
- the one-line condition \(\lambda s c<w\Phi\) for a cell in a tissue, read as CT9 with the cell's net share of the cost of following;
- the five-term arithmetic in logs, with the alignment rule \(s=w/W\);
- a preregistrable log-log reversion contour with its single-clock condition.

No published reversion contour in \(\log\lambda\times\log c\) was found.

## 8. What remains measured

The theory does not supply \(\lambda\), \(c\), \(s\), \(w\), \(\Phi\), \(W\), the lever costs, or the ruin hazard. Until they are measured in one system, the condition and the levers are the design this cost selects under an interpretation. They are not a scored test. This page is not a qualification under THEORY §3, and it is not a field test of the hypothesis.
