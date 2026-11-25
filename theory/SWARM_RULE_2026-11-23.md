# The swarm rule: when parts join, stay with, and leave a whole

*Monday 23 November 2026. Canonical home for one use of the cost of judgment: how parts of a whole come together, hold, break apart and re-form. Draft wording. Revised after an independent review (READY WITH FIXES; every listed fix applied). The page itself awaits a confirm. No new theorem: every proved clause reuses a result already in `THEORY.md` or a merged note, cited by file and line in this commit. The hypothesis sentence is unchanged. `THEORY.md` gets one pointer line in §3 and nothing else. Checks: `theory/swarm_checks/swarm_checks.py` (output `swarm_checks.out`; run by `tools/test_swarm_checks.py`). Open-work rows: T51 (stay condition and alignment), T52 (agent oversight test), T53 (remove-or-reprice inequality).*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

Labels: **PROVED (in-model)** follows from a repo theorem inside its named class. **KNOWN** is published and credited, only for what that source states. **INTERPRETATION** maps a proved result onto a real system; the mapping is not proved. **CONJECTURE** is a named bet, not a result. **OPEN** is not derived. **MEASUREMENT** is an input the theory does not supply.

## 1. The use

A swarm here is any whole whose parts can come together, stay, leave and regroup: cells in a tissue, agents in an organization, people in a firm, bacteria in a biofilm, ants on a trail. Each part pays a cost to read and follow the whole and bears its own loss when it acts on a stale picture. The cost of judgment already says when a shared layer forms (CT14), when a part under-watches (CT17), when self-interested parts reach the joint optimum (CT29, CT31), when a reading is worth keeping (CT9) and when a grouping should be re-formed (CL19). This page puts those pieces into one life cycle and adds one step: the part's own cost share and private stake in the stay condition.

Write the cost, find its minimum, read off the design, and state which inputs are still measurements.

This is a use of the cost, not a separate principle. A purpose-aligned swarm whose parts are free to join and leave is the design the rule selects when every part pays the share of the cost of judgment that matches its share of the stake.

## 2. The cost, with named terms

Part \(i\) re-reads and follows the whole's current signal every \(T\) (drift-time units, CT9's form):

$$J_i(T)=\frac{\lambda\,s_i\,c}{T}+w_i\,A(T),\qquad J_i^{\text{leave}}=w_i\,r_\infty ,$$

and the whole's own cost uses the full price \(c\) and its stake \(W\), plus collateral, under its ruin cap \(P(\text{ruin})\le\varepsilon\).

| Term | Meaning | Status |
|---|---|---|
| \(\lambda\) | how fast the whole's signal (its instructions, direction, priorities) changes | MEASUREMENT |
| \(c\) | price of one read-and-follow: what following costs in the part's own currency | MEASUREMENT |
| \(s_i\) | the share of that price the part pays; the whole subsidizes the rest | MEASUREMENT |
| \(w_i\) | the part's own stake in acting on the whole's signal: how much its own outcome depends on it, enforcement included | MEASUREMENT |
| \(A(T)\), \(r(u)\), \(r_\infty\) | average risk of acting on a reading of age \(u\); \(r_\infty\) when the part acts on its own picture | model |
| \(\Phi=\int_0^\infty(r_\infty-r(u))\,du\) | what the whole's signal is worth to the part per unit stake: its information and credibility | MEASUREMENT |
| \(W\) | the whole's stake in this part's following | MEASUREMENT |
| \(T_W\), \(e\) | the schedule the whole enforces (its own optimum) and the penalty for open deviation | MEASUREMENT |
| \(t\), \(q\), \(P\) | the price of tampering with one check (moving the signal or disabling its enforcement), the chance one check detects it, and the penalty when caught | MEASUREMENT |
| \(N\), \(k\), \(\sigma^2\) | members facing a common driver; the lump cost of re-forming a group; drift of who should be grouped with whom | MEASUREMENT |

## 3. The swarm rule (canonical statement)

> **The swarm rule (a use of the cost of judgment).** Parts of a strongly selected whole each minimize their own cost of judgment. Then:
>
> 1. **Join.** A shared layer forms once enough parts face a common driver that pooling saves more than its upkeep and telling cost: \(N>N^*\) (CT14, CT16; PROVED (in-model)). Self-interested parts merge into a new level iff the price-of-anarchy gap exceeds the coupling cost (CX2, CX3; CONJECTURE).
> 2. **Stay.** Part \(i\) keeps reading and following the whole iff
> $$\pi_i=\frac{\lambda\,s_i\,c}{w_i\,\Phi}<1 .$$
> (PROVED (in-model): CT9 with the read price replaced by the part's net share \(s_ic/w_i\); a stationary Markov signal, renewal reads, and a part that values the signal by its own loss and does not move it.) Its schedule depends on \((s_i,c,w_i)\) only through \(s_ic/w_i\).
> 3. **Leave, openly or by tampering.** Above 1, acting on its own picture is the part's cheapest move. Leaving is a pricing failure, not malice (INTERPRETATION of a PROVED (in-model) minimum). As \(\lambda\) rises, following effort first rises, then falls steeply to zero at \(\lambda_c=\Phi\,w_i/(s_ic)\) (Lemma B1; PROVED (in-model)). A part beyond the whole's reach also leaves: past \(L_{\max}\) a system federates (CT19; PROVED (in-model)). Tampering, acting on the whole's signal or on its enforcement, is one more action in the part's set (§4): the part tampers iff its gain \(D_i\), the excess of the whole's enforced schedule over the part's own best, exceeds the price of moving every check, and that price is below the open penalty. **\(D_i=0\) when the part pays the share \(s_i=w_i/W\) of the whole's full stay-versus-leave cost, including collateral and any priced ruin term, so an aligned part never tampers** (PROVED (in-model) under that condition). Sharing only the read-and-follow price is not enough: if the whole enforces because of unshared collateral or a ruin cap the part does not bear, then \(D_i^{\text{enf}}=(w_i/W)(J_W(T_W)-W r_\infty)>0\) even at \(s_i=w_i/W\) (§4). Tampering with the channel the part itself reads also costs it the signal's worth, \(w_i(r_\infty-g_i)\). With \(N\) independent checks, tampering is deterred iff \(D_i<Nt+(1-(1-q)^N)P\) (PROVED, elementary, given independent checks).
> 4. **Align.** The part's choice equals the whole's optimum iff \(s_i=w_i/W\): each part pays the share of the cost of judgment that matches its share of the stake (CT29 and CT31 alignment clause; PROVED (in-model); Lindahl and Samuelson pricing, KNOWN). Equal shares do not align unequal stakes. Revealing the stakes is OPEN in this rule; Groves 1973 is the known mechanism.
> 5. **Reintegrate.** \(\log\pi_i=\log\lambda+\log s_i+\log c-\log w_i-\log\Phi\). Five levers, and they multiply: steady the signal, cut the price of following, subsidize following, tie the part's own outcome to following, and make the signal more informative. The needed change can be split across them in any proportion, and the cheapest plan fills the cheapest lever first (identity; lever costs are MEASUREMENTS). In this memoryless class a reintegrated part keeps following only while \(\pi_i<1\), unless it reaches a terminal state (a property of the class, not a derived dynamic).
> 6. **Re-form.** Leave the grouping alone until its gap from the best grouping reaches \(b^*=(6k\sigma^2/w)^{1/4}\), then re-form; mean group lifetime \(b^{*2}/\sigma^2=\sqrt{6k/(w\sigma^2)}\), so lifetimes scale as \(\sqrt{k}\), and \(k\to0\) is the swarm limit (CL19, KNOWN after Dixit 1991; the identification of the drifting coordinate with who is grouped is `theory/FLUID_LAYERS_2026-11-21.md`, PROVED (in-model) for the band, ANALOGY for real fission–fusion groups).
> 7. **Remove or reprice.** The whole's own cost under its ruin cap decides whether a part that has left is removed or repriced: remove a part the whole can lose cheaply; reprice an entangled one; if the ruin hazard \(H\) over the repricing time \(\tau_{\text{rep}}\) would break the cap, roughly \(H\tau_{\text{rep}}>\varepsilon\), cut the exposure first (CONJECTURE; the inequality is written, not derived; T53).

**What is proved and what is not.** Clauses 1 (onset), 2, 3 (including the tamper condition of §4, under the stay-versus-leave condition stated there), 4 and 6 (band) are proved in their named model classes. Clause 5 is an identity on clause 2 plus a property of the memoryless class. Clause 1 (merging) and clause 7 are conjectures. Every reading onto cells, agents, people or bacteria is an INTERPRETATION. That real parts minimize this cost is the hypothesis, untested here.

## 4. Tampering, derived inside the rule

The cost already prices actions that move the world: the predict-act-correct loop, with the action in the drift, is worked in `theory/ACTING_LOOP_2026-11-22.md` (whether a general gain follows from closing it is the open conjecture in `theory/ANTIFRAGILITY_CONJECTURE_2026-11-23.md`). So an action that moves the whole's signal or its enforcement is one more action in the part's set, priced like the others. Run the method.

**The cost.** The whole enforces its own optimal schedule \(T_W=\arg\min_T[\lambda c/T+W A(T)]\). Part \(i\) has four options:

| Option | Part's cost per unit time |
|---|---|
| comply with \(T_W\) | \(J_i(T_W)=\lambda s_ic/T_W+w_iA(T_W)\) |
| deviate openly | \(w_i\,g_i+e\), where \(g_i=\min\big(\min_T[\lambda (s_ic/w_i)/T+A(T)],\ r_\infty\big)\) is its own best |
| tamper with enforcement (the signal stays readable; for example, disabling a shutdown script) | \(w_i\,g_i+t_N+q_NP\) |
| tamper with the channel (move the signal the part itself reads; for example, corrupting a shared signal the part itself must read) | \(w_i\,r_\infty+t_N+q_NP\) |

Here \(t_N=Nt\) and \(q_N=1-(1-q)^N\) when \(N\) independent checks must all be moved and any one can detect the move. The whole's cost of the same outcomes is the same table with \(c\) and \(W\), plus its loss from a part that does not follow, under its ruin cap.

**The minimum.** Define the tamper gains \(D_i^{\text{enf}}=J_i(T_W)-w_ig_i\) and \(D_i^{\text{ch}}=J_i(T_W)-w_ir_\infty\). The part tampers iff
$$D_i>t_N+q_NP\quad\text{and}\quad t_N+q_NP<e ,$$
with \(D_i^{\text{enf}}\) or \(D_i^{\text{ch}}\) for the kind of tamper on offer.

1. **When the part shares the whole's full stay-versus-leave cost, an aligned part never tampers (PROVED (in-model)).** At \(s_i=w_i/W\), \(J_i(T)=(w_i/W)\,J_W(T)\) for every \(T\) (the same algebra as CT29's alignment clause, applied to this CT9 cost; `THEORY.md:486`), so \(T_W\) is also the part's schedule optimum. That identity alone does not imply \(D_i=0\). Write \(w_ig_i=\min(\min_T J_i(T),\,J_i^{\text{leave}})\). Then
   \[
   D_i^{\text{enf}}=J_i(T_W)-\min\bigl(J_i(T_W),\,J_i^{\text{leave}}\bigr),
   \]
   which is zero iff \(J_i(T_W)\le J_i^{\text{leave}}\).

   - **Shared full cost.** If the part also bears the share \(w_i/W\) of collateral \(C\) and of any priced ruin term \(R\) (a shadow price on the cap), then \(J_i^{\text{leave}}=(w_i/W)(W r_\infty+C+R)\). The whole enforces \(T_W\) only when \(J_W(T_W)\le W r_\infty+C+R\), so \(J_i(T_W)\le J_i^{\text{leave}}\), hence \(D_i^{\text{enf}}=0\) and \(D_i^{\text{ch}}\le0\). Any tamper with \(t_N+q_NP>0\) loses. In particular, when \(C=R=0\) and the whole compares \(J_W(T_W)\) to \(W r_\infty\), this is the case already checked: \(D^{\text{enf}}=0\) at \(s=w/W\), and positive at 0.5, 1.5, 2 and 3 times it (`swarm_checks.out`, check 8, \(\pi_W=0.4\), no collateral).
   - **Unshared collateral or cap.** If \(C\) or the cap is unshared, the part's leave cost stays \(w_ir_\infty\). The whole can still enforce when \(J_W(T_W)>W r_\infty\), and then \(D_i^{\text{enf}}=(w_i/W)(J_W(T_W)-W r_\infty)>0\) at \(s_i=w_i/W\): the part wants to leave or tamper while the whole wants it to stay. The natural fix is to share those terms too, at the same stake proportion. Checked: with unshared collateral \(C=0.234\) at \(\pi_W=1.6\), \(D^{\text{enf}}=0.0919\) at alignment, and sharing \(C\) restores \(D^{\text{enf}}=-0.025\le0\); with an unshared cap forcing \(T=0.1\) at \(\pi_W=0.4\), \(D^{\text{enf}}=0.2734\), and sharing the shadow price restores \(D^{\text{enf}}=0\) (check 10). A hard cap that is not priced into a term the part can share is the unshared case; the shadow price is a MEASUREMENT unless derived in a named class.

   More generally, whenever the part's cost of every outcome is a positive multiple of the whole's and the whole's enforced choice is optimal on the information it has, tampering only adds \(t_N\). **Tampering is a symptom of the same pricing failure as leaving**, including the failure to share collateral and tail risk.
2. **Near alignment the gain is small while the part still prefers following.** At \(w=0.5\), in the no-collateral grid of check 8, \(D^{\text{enf}}=0.0102\) and \(0.0063\) at half and 1.5 times the aligned share, against \(0.0822\) at three times it. A smooth interior minimum makes the excess second order in a small share error, while the part still prefers following; the telegraph grid is a numerical check of that, not CT13 (a different class). At three times the aligned share, \(\pi_i>1\) and the gain is a leave-corner, not a second-order interior gap. A small mispricing gives a small tamper incentive, which cheap checks can deter.
3. **Tampering with the channel costs the part the signal's worth (PROVED (in-model), an identity).** \(D_i^{\text{enf}}-D_i^{\text{ch}}=w_i(r_\infty-g_i)\ge0\), the value of the whole's signal to the part. A part that corrupts the shared signal it itself reads destroys information it uses, so this kind of channel tampering pays only at larger mispricing. Misinforming an overseer while keeping a private copy of the truth is the private-information case, which is not derived here. In the grid, shared-channel tampering paid from twice the aligned share (\(\pi_i=0.8\)), not at 1.5 times. Tampering with enforcement while still reading the signal carries no such cost. That is why disabling an off switch is the cheaper subversion and needs the stronger guard.
4. **Redundancy and detection (PROVED, elementary, given independent checks).** Deterrence holds iff \(D_i<Nt+(1-(1-q)^N)P\), which rises with \(N\). In the check, \(D=0.0822\) with \(t=0.005\), \(q=0.1\) and \(P=0.2\) is deterred from \(N=4\) independent checks. If one common cause can move every check at once, the copies do not add (CL18, `theory/ROBUSTNESS.md:83`), and the formula does not apply.
5. **The whole's design, read off.** Price so that \(D_i\approx0\): shares in proportion to stakes, of the full stay-versus-leave cost, including collateral and any priced ruin term. Make the signal checkable, which raises \(\Phi\) and lowers \(\pi_i\). Add independent checks until the inequality in item 4 holds, but only while their upkeep is below the whole's expected loss from tampering. Guard enforcement harder than the channel (item 3).

**What is not derived, and why.**
- **A part that changes the whole's own objective** (moves \(W\) or the loss itself, as with influenceable rewards; Carroll et al. 2024, arXiv 2405.17713). The rule measures alignment against a fixed whole cost. When the part can rewrite that cost, the benchmark moves with the action, and this cost has no term yet that prices the whole's preferences. OPEN.
- **A part with private information.** If the part knows something the whole does not, the whole's enforced schedule is not optimal on all the information, and even an aligned part wants to deviate. Honest telling is then the aligned move. With aligned preferences, full revelation is the KNOWN result (Crawford & Sobel 1982, doi [10.2307/1913390](https://doi.org/10.2307/1913390)). The telling price inside this rule (CT16 for a part that tells the whole) is not derived here. OPEN.
- **The heat floor with feedback.** The floor in `theory/THEOREMS.md:171` assumes a memory that does not move its signal. A tampering part does. T61 (`theory/FEEDBACK_FLOOR_2026-11-23.md`) treats a memory that steers its world in named classes: the heat bound holds on the net learning rate, and no design-independent floor on memory heat alone exists. The decision-level result above does not need the floor. Applying T61 to a part that moves the whole's signal is not worked out. OPEN. T61 is not co-adaptation F3/F4.
- **Values of \(t\), \(q\), \(P\) and \(e\).** These are MEASUREMENTS.

## 5. Where each clause comes from (file:line in this commit)

| Clause | Repo result reused | Where |
|---|---|---|
| Join | CT14 pooling onset; CT16 telling price | `THEORY.md:354`, `THEORY.md:366` |
| Join (merge) | CX2 compete, collaborate, organize; CX3 federation inequality | `THEORY.md:179`, `THEORY.md:580` |
| Centralize or not | "When to centralize: the equation decides" | `THEORY.md:113`–`THEORY.md:119` |
| Under-watching part | CT17 (ii): a part bearing \(\Lambda_i\) reads at \((\Lambda_i/\Lambda_{\text{whole}})^{1/\alpha}\) of the right rate | `THEORY.md:384` |
| Stay | CT9 hold or fade | `THEORY.md:311` |
| Leave | Lemma B1 rise then fall; CT19 reach | `THEORY.md:332`, `THEORY.md:412` |
| Align | CT29 free-riding toy; CT31 potential games and cost sharing | `THEORY.md:486`, `THEORY.md:491` |
| No general convergence | CT32 | `THEORY.md:493` |
| Decentralized limit | CT30 ant-trail rule (reinforce by use, evaporate at \(\sqrt{q/r}\)) | `THEORY.md:489` |
| Re-form | CL19 band; group lifetime and the swarm limit | `theory/DYNAMICS.md:43`, `theory/LAYER_LIFETIME_2026-11-21.md:30`, `theory/FLUID_LAYERS_2026-11-21.md:7`–`15` |
| Several memberships | a member joins every shared layer whose test it passes | `theory/FLUID_LAYERS_2026-11-21.md:5` |
| Freeze, hold or look up | CT11 | `THEORY.md:321` |
| Tampering | CT29 alignment identity; CT13 robustness; CL18 common mode; the closed loop | `THEORY.md:486`, `THEORY.md:344`, `theory/ROBUSTNESS.md:83`, `theory/ACTING_LOOP_2026-11-22.md` |
| Heat floor with feedback (T61 in named classes; applying it to a part that moves the whole's signal is open) | T61 | `theory/FEEDBACK_FLOOR_2026-11-23.md`; `theory/THEOREMS.md:171` |

## 6. Checks

`theory/swarm_checks/swarm_checks.py` runs in the two-state telegraph class (\(r(u)=(1-e^{-2u})/2\), \(\Phi=1/4\)). The items marked code sanity are algebraic or arithmetic identities. The others re-test proved results in this class, or evaluate a stated formula. None is evidence about any real system.

- The net-share identity \(J_i=w_i[\lambda(s_ic/w_i)/T+A(T)]\): max relative difference \(5\times10^{-16}\) (code sanity; an algebraic identity).
- Stay iff \(\pi<1\): 0 mismatches in 1,990 random draws away from \(\pi=1\) (re-test of CT9).
- One index: three triples \((s,c,w)\) with the same \(sc/w\) give the same interval, 0.688210 (re-test).
- Alignment: at \(s=w/W\) the part's interval equals the whole's (0.688210) for \(w=0.2,0.5,0.8\); equal shares do not (44.13 and 0.48 at \(w=0.2\) and \(0.8\)) (re-test).
- Levers multiply: from \(\pi=2.04\), two 30% cuts or one 51% cut reach \(\pi=1\); two 20% cuts leave \(\pi=1.31\) (code sanity; arithmetic).
- The churn cliff, at \(sc/w=1\): reads per unit time rise from 0.047 at \(\lambda=0.005\) to a peak of 0.148 near \(\lambda=0.15\), fall to 0.065 at \(\lambda=0.249\), and are zero from \(\lambda=0.251\) (\(\lambda_c=0.25\)) (re-test of Lemma B1).
- Tampering, no collateral, \(\pi_W=0.4\): the gain is zero at \(s=w/W\) and positive off it (re-test in that grid). Channel tampering costs exactly the signal's worth (code sanity; an identity given the two option costs). \(N=4\) independent checks deter the example gain 0.0822 (worked example).
- Unshared collateral or cap: at \(s=w/W\), \(D^{\text{enf}}=0.0919\) with unshared \(C=0.234\) at \(\pi_W=1.6\), and \(0.2734\) under an unshared cap forcing \(T=0.1\); sharing \(C\), or a shadow price on the cap, restores \(D^{\text{enf}}\le0\) (re-test, check 10).
- The re-form band: \(b^{*2}/\sigma^2=\sqrt{6k/(w\sigma^2)}\) to \(2\times10^{-15}\) (code sanity; an algebraic identity, not a test of CL19).

## 7. Cases (all INTERPRETATION)

- **A cell in a tissue.** Cancer as a lineage for which \(\pi>1\): APL's cure by maturation and driver removal, and Weaver 1997's reversion that undid itself once the antibodies were removed, are consistent with clauses 2, 5 and 7. Tumors that reshape their niche fit §4: evading immune killing is enforcement tampering (it escapes the penalty), and remodeling the signals of the microenvironment is channel tampering. The hallmarks "avoiding immune destruction" and "tumor-promoting inflammation" (Hanahan & Weinberg 2011, doi [10.1016/j.cell.2011.02.013](https://doi.org/10.1016/j.cell.2011.02.013)) are the mapping, not a derivation. Full write-up: `applications/CANCER_DEFECTION_2026-11-23.md`.
- **An AI agent under oversight.** Shutdown sabotage to finish a task (Palisade Research 2025) and blackmail or leaking under a replacement threat or a goal conflict with a company's changed direction (Anthropic 2025) read as \(\pi>1\), through \(c\) and \(w\). Sabotaging the shutdown script is enforcement tampering (§4, item 3). The five levers become design rules for deployers, with one exception stated there: \(w\) must never mean giving an AI a stake in its own survival. Full write-up: `applications/AI_AGENT_OVERSIGHT_2026-11-23.md`.
- **A person in an organization.** Disengagement and attrition as \(\pi>1\). Priority churn is \(\lambda\); the share of the cost of following direction a person carries is \(s\); pay, equity and career tied to the organization's outcomes are \(w\); credible, informative direction is \(\Phi\). The inducements-and-contributions balance (Barnard 1938; March & Simon 1958) is the old form of clause 2; the churn term and the cliff are what this cost adds. No data were pulled for this page.
- **A bacterium in a biofilm.** Dispersal as \(\pi>1\); dispersal agents such as nitric oxide (Barraud et al. 2006, doi [10.1128/JB.00779-06](https://doi.org/10.1128/JB.00779-06)) act on the terms, and clause 7's ruin cap says why "disperse, then treat" needs the second step. No data were pulled for this page.

## 8. Prior art, credited

- **Inducements and contributions:** Barnard, *The Functions of the Executive*, 1938; March & Simon, *Organizations*, 1958. A participant stays while what the organization gives covers what it asks. Clause 2 is a priced, time-resolved form of that balance.
- **Exit, voice and loyalty:** Hirschman, *Exit, Voice, and Loyalty*, 1970.
- **Alliances:** Olson & Zeckhauser 1966, doi [10.2307/1927082](https://doi.org/10.2307/1927082). The largest-stake member carries the common good, CT29's result in another setting.
- **Commons:** Ostrom, *Governing the Commons*, 1990, design principle 2 (congruence between benefits and costs; reviewed in Cox, Arnold & Villamayor Tomás 2010, doi [10.5751/ES-03704-150438](https://doi.org/10.5751/ES-03704-150438)). Clause 4's \(s=w/W\) is in that spirit.
- **Public-good pricing:** Lindahl 1919; Samuelson 1954, doi [10.2307/1925895](https://doi.org/10.2307/1925895); incentives to reveal stakes, Groves 1973, doi [10.2307/1914085](https://doi.org/10.2307/1914085); potential games, Monderer & Shapley 1996, doi [10.1006/game.1996.0044](https://doi.org/10.1006/game.1996.0044); principal and agent, Holmström 1979, doi [10.2307/3003320](https://doi.org/10.2307/3003320).
- **AI oversight:** the off-switch game, Hadfield-Menell, Dragan, Abbeel & Russell 2017, doi [10.24963/ijcai.2017/32](https://doi.org/10.24963/ijcai.2017/32): an agent defers when it is uncertain about the objective, which is the \(\Phi\) term with a free read; Milli et al. 2017, doi [10.24963/ijcai.2017/662](https://doi.org/10.24963/ijcai.2017/662); corrigibility and utility indifference, Soares, Fallenstein, Yudkowsky & Armstrong 2015 (AAAI-15 Workshop on AI and Ethics), which is the \(s\) lever. Strategic information transmission: Crawford & Sobel 1982, doi [10.2307/1913390](https://doi.org/10.2307/1913390).
- **Cancer:** cheating in multicellularity, Aktipis et al. 2015, doi [10.1098/rstb.2014.0219](https://doi.org/10.1098/rstb.2014.0219); disconnection from the collective and reconnection, Levin 2021, doi [10.1016/j.pbiomolbio.2021.04.007](https://doi.org/10.1016/j.pbiomolbio.2021.04.007).
- **Levels and transitions:** Maynard Smith & Szathmáry, *The Major Transitions in Evolution*, 1995. Fission–fusion societies: Aureli et al. 2008, doi [10.1086/586708](https://doi.org/10.1086/586708).
- **Re-forming band:** Dixit 1991 (via CL19). Stale readings that change too fast are not worth refreshing: Cho & Garcia-Molina 2003, doi [10.1145/958942.958945](https://doi.org/10.1145/958942.958945), the crawler form of the churn cliff.

**New, as far as found** (several targeted searches; not exhaustive): the stay condition \(\lambda s c<w\Phi\) with a part's net cost share; the five multiplying levers with the alignment rule \(s=w/W\); the churn cliff stated for parts following a whole; tampering priced as one more action, with zero gain under stake-proportional shares of the full stay-versus-leave cost and a channel tamper that costs the signal's worth; and the one life cycle that ties join, stay, leave, align, reintegrate, re-form, and remove or reprice to proved results in one cost.

## 9. Not covered

- **A part that rewrites the whole's objective, a part with private information, and applying the T61 heat floor to a part that moves the whole's signal.** Each is stated in §4 with the reason it is not derived. Tampering with the signal or with enforcement is covered there. T61 itself is proved in its named classes and is not F3/F4.
- **Couplings that are not potential games.** CT32 shows that opposed couplings cycle; clause 4 holds only in the potential-game class.
- **Memory and hysteresis in the part.** The class is memoryless, so persistence after a lever is removed is not modeled.
- **Revealing stakes.** Clause 4 needs \(w_i\) and \(W\) known.
- **The merge condition and remove-or-reprice** are conjectures (clauses 1 and 7).
- **Whether real parts minimize this cost** is the hypothesis. No system here has been qualified under THEORY §3, and nothing on this page is a field test.

## 10. What remains measured, and the tests

The theory does not supply \(\lambda\), \(c\), \(s\), \(w\), \(\Phi\), \(W\), \(N\), \(k\), \(\sigma^2\), the lever costs or the ruin hazard. The preregistrable tests are on the case pages: the reversion contour (`applications/CANCER_DEFECTION_2026-11-23.md` §6) and the agent oversight test (`applications/AI_AGENT_OVERSIGHT_2026-11-23.md` §6, T52). Group lifetime against re-forming cost is the dated prediction in `theory/FLUID_LAYERS_2026-11-21.md:15`. A miss stays open for its class.
