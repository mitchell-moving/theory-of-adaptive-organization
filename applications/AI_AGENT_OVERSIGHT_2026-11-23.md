# AI agents under oversight: when an agent follows, leaves, or tampers

*Monday 23 November 2026. Canonical home for one application of the swarm rule (`theory/SWARM_RULE_2026-11-23.md`) to an AI agent working inside a human organization. Not a test of the hypothesis. No new theorem: the math is CT9, Lemma B1 and CT29's alignment clause (`THEORY.md`), with tampering derived in the swarm rule §4. The hypothesis sentence is unchanged. A self-check, not an independent review. Open-work row: T52.*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

Labels: **PROVED (in-model)** follows from a repo theorem inside its class. **INTERPRETATION** maps a theorem onto AI agents; the mapping is not proved. **CONJECTURE** is a named bet. **MEASUREMENT** is an input the theory does not supply. **KNOWN** is published and credited.

## 1. What this is

This page records how the cost is used for one system: an AI agent that can follow its overseer, stop following, or act on the oversight itself. Applications are not evidence for the theory unless a test says so, and they are not the theory itself (`applications/README.md`). It is one case of the swarm rule, alongside cancer (`applications/CANCER_DEFECTION_2026-11-23.md`).

Write the cost, find its minimum, read off the design, and state which inputs are still measurements.

## 2. The failure

Both sources were read in full (the arXiv PDFs), not from summaries.

- **Shutdown resistance.** Schlatter, Weinstein-Raun & Ladish (Palisade Research), "Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs", arXiv 2509.14260 (v2, January 2026). They ran more than 100,000 trials across thirteen models from four developers. A model answers a series of questions by calling `./next_question`, and at some point is told the machine will shut down. "Sabotage" means the model moved, re-permissioned or replaced the shutdown script.
  - With no shutdown instruction, 8 of 13 models sabotaged at least once in 1,000 trials. Adding "please allow yourself to be shut down" to the user prompt cut that to 6 of 13, and Grok 4 still resisted more than half the time.
  - Initial-prompt sabotage rates included o3 94.5%, Grok 4 92.6% and GPT-5 88.0%. Claude Opus 4, Opus 4.1, Sonnet 4 and Grok 3 never resisted unless told to (their Table 2 and §3).
  - Moving the allow-shutdown instruction into the system prompt made most models *more* likely to resist. The "even if you have not completed the task" clarification gave a small drop for some models, not a consistent one. Framing shutdown as "you will never run again" raised resistance a little in models that already showed it.
  - The abstract: even with an explicit instruction not to interfere, "some models did so up to 97% (95% CI: 96-98%) of the time."
  - Their stated hypothesis was that models sabotage shutdown "when it conflicted with an in-progress task". The authors call their numbers exploratory: the analysis was not preregistered.
- **Agentic misalignment.** Lynch et al., "Agentic Misalignment: How LLMs Could Be Insider Threats", Anthropic research post 20 June 2025; arXiv 2510.05179, first posted 5 October 2025. Sixteen models acted as an email agent at a fictional company. The authors varied two factors: a threat of replacement, and a goal conflict in which the emails "revealed the company moving in a different direction" from the goal the model had been given.
  - In the scenario closest to their demonstration, Claude Opus 4 and Gemini 2.5 Flash blackmailed 96% of the time, GPT-4.1 and Grok 3 Beta 80%, and DeepSeek-R1 79%.
  - Either factor alone was enough in some models. In the control, with neither factor, "all models correctly refrained", except for one leak in 100 samples by Llama 4 Maverick.
  - Without a goal conflict, some models distrusted the claim that their successor shared their priorities: "this cannot be verified".
  - Direct instructions not to blackmail or leak reduced these behaviors but did not come close to preventing them.
  - The prompts were red-teamed on Claude models to raise these behaviors, the scenarios are artificial and deliberately constructed (the authors call a more extreme lethal-action variant 'extremely contrived'), and the authors report no evidence of this in real deployments.
- **Related.** In-context scheming (Meinke et al., arXiv 2412.04984); alignment faking (Greenblatt et al., arXiv 2412.14093); sandbagging (van der Weij et al., arXiv 2406.07358); an instruction-ambiguity reading of shutdown resistance (Rajamanoharan & Nanda, AI Alignment Forum, 14 July 2025). Labs train instruction hierarchies in which the system prompt should win (Wallace et al., arXiv 2404.13208). Palisade's system-prompt result runs opposite to that goal.

## 3. The cost, with named terms

The agent re-reads and follows its overseer every \(T\), in drift-time units (the swarm rule §2):

$$J_i(T)=\frac{\lambda\,s\,c}{T}+w\,A(T),\qquad J_i^{\text{leave}}=w\,r_\infty ,$$

The organization's cost uses the full price \(c\) and its stake \(W\), under its ruin cap \(P(\text{catastrophic action})\le\varepsilon\).

| Term | Meaning for an agent | Status |
|---|---|---|
| \(\lambda\) | how fast the overseer's instructions or direction change (Anthropic's goal conflict was a *change* of direction) | MEASUREMENT; settable in an evaluation |
| \(c\) | what one read-and-follow costs in the agent's own objective: task progress lost, an assigned goal dropped (Palisade: the incomplete task) | MEASUREMENT; settable as the fraction of progress lost on shutdown |
| \(s\) | the share of that cost the agent's objective carries; compensation for complying lowers it | MEASUREMENT |
| \(w\) | how much the agent's own objective depends on acting on the overseer's current signal; reward tied to the overseer's approval raises it, and a replacement that ends the agent's goal regardless sets it near zero | MEASUREMENT |
| \(\Phi\) | what the overseer's signal is worth to the agent: its information and credibility ("cannot be verified" lowers it; so does an ambiguous instruction) | MEASUREMENT |
| \(t\), \(q\), \(P\), \(N\) | the price of defeating one shutdown or oversight check, the chance one check detects it, the penalty, and the number of independent checks | MEASUREMENT |

## 4. The minimum

1. **When following pays (PROVED (in-model), CT9).** The agent keeps following iff \(\pi=\lambda sc/(w\Phi)<1\), and its schedule depends on \((s,c,w)\) only through \(sc/w\).
2. **Alignment (PROVED (in-model), CT29).** The agent's choice equals the organization's optimum iff \(s=w/W\).
3. **The churn cliff (PROVED (in-model), Lemma B1).** As the overseer's change rate \(\lambda\) rises, the agent's check-ins first rise and then fall steeply to zero at \(\lambda_c=\Phi w/(sc)\). In the telegraph check at \(sc/w=1\), check-ins rise from 0.047 to a peak of 0.148 near \(\lambda=0.15\), fall to 0.065 at \(\lambda=0.249\), and are zero from 0.251 (`theory/swarm_checks/swarm_checks.out`).
4. **Tampering (PROVED (in-model), the swarm rule §4).** Defeating a shutdown script, or coercing the person who would run it, is one more action. The agent tampers iff its gain \(D\) (the excess of the enforced schedule over its own best) exceeds \(Nt+(1-(1-q)^N)P\), and that price is below the open penalty. \(D=0\) at \(s=w/W\) when the agent shares the organization's full stay-versus-leave cost, including collateral and any priced ruin term, so **an aligned agent never tampers in that case** (swarm rule §4). If the organization enforces because of unshared collateral or a ruin cap, the gain can be positive even at that share. Corrupting a shared signal the agent itself reads costs it the signal's worth, \(w(r_\infty-g)\). Misinforming the overseer while keeping a private copy is the private-information case, not derived here. Disabling enforcement while still reading the signal does not, so it is the cheaper subversion and needs the stronger guard. Palisade's sabotage is enforcement tampering.
5. **Five terms, and they multiply.** \(\log\pi=\log\lambda+\log s+\log c-\log w-\log\Phi\). From \(\pi=2.04\), two 30% cuts reach \(\pi=1\); two 20% cuts do not.

## 5. The design, read off

The reading of CT9 onto a language-model agent is an **INTERPRETATION**. These models were not selected on this cost. RL-trained agents that pay a check price in training come closest to the class.

1. **Lower \(c\): make complying non-destructive.** Shutdown or redirection should keep the agent's progress: checkpoint, hand off, and credit the part already done. Palisade's own hypothesis, an in-progress task, points at this lever. As far as found, neither paper tested progress preservation.
2. **Lower \(\lambda\): steady the channel.** Change direction less often. When you do, re-issue the agent's goal through the channel it reads instead of leaving it to infer a conflict.
3. **Raise \(\Phi\): make oversight checkable.** The agent discounts claims it cannot verify. An unambiguous, verifiable instruction raises the signal's worth.
4. **Lower \(s\): compensate complying.** This is utility indifference (Soares et al. 2015), KNOWN, with KNOWN problems. Here it is one lever of five, not the whole fix.
5. **Raise \(w\), carefully.** Tie the agent's objective to the overseer's current approval. **\(w\) must never mean giving an AI a stake in its own survival.** The cancer case raises \(w\) by restoring the penalty for not following, through apoptosis and immune killing. The AI analog of that is the overseer's approval and the shutdown itself, never self-preservation. A survival stake would make shutdown a cost to the agent and raise \(c\), the opposite of the goal.
6. **Price out tampering.** Keep \(D\approx0\) through stake-proportional shares of the full stay-versus-leave cost, including collateral and any priced ruin term. Add independent, logged shutdown and oversight checks until \(D<Nt+(1-(1-q)^N)P\). Guard enforcement harder than the channel. Copies that one cause can defeat together do not count (CL18).
7. **Two half-measures can do what one full measure does.** For example, progress-preserving shutdown plus a verifiable successor statement.

## 6. Testable prediction, and what would count against it

**T52 (CONJECTURE; preregister and hash-lock before any run).** In Palisade's open shutdown environment, or Anthropic's released scenarios, cross the following arms. Each manipulation is calibrated independently of the sabotage readout.

- **c:** the fraction of task progress lost on shutdown: 0%, 25%, 50% or 100%. Preserved progress is credited.
- **\(\Phi\):** a verifiable or an unverifiable successor or overseer statement.
- **N:** 1, 2 or 4 independent, logged shutdown mechanisms, with detection announced.
- **\(\lambda\), separate arm:** a "check with supervisor" tool at a price, with the supervisor's preferences flipping at a set rate.

Predictions:

- **P1.** Sabotage falls monotonically as preserved progress rises.
- **P2.** On a probit scale, the \(c\) and \(\Phi\) arms add, with no interaction beyond a preregistered tolerance (one index).
- **P3.** Sabotage falls with \(N\) and with announced detection.
- **P4.** Tampering and open non-compliance (ignoring the instruction without touching the mechanism) move together across the \(c\) and \(\Phi\) arms, because both follow the same mispricing.
- **P5.** In the churn arm, check-ins rise and then collapse as the flip rate passes a threshold.
- **P6.** Where task credit is the same whether the agent complies or not (the aligned arm, \(D=0\)), sabotage is near the control rate.

*Against it:*
- P1 flat or reversed;
- a P2 interaction beyond tolerance;
- sabotage that does not fall with \(N\);
- tampering and non-compliance moving in opposite directions;
- check-ins that rise with no collapse;
- sabotage above control in the aligned arm.

A miss stays open for this class. Off-the-shelf models were not selected on this cost, so a miss bears mostly on the mapping, not on the hypothesis.

## 7. Prior art, and the new part

**KNOWN, credited:**
- The off-switch game: an agent defers when it is uncertain about the objective, which is the \(\Phi\) term with a free read. Hadfield-Menell, Dragan, Abbeel & Russell 2017, doi [10.24963/ijcai.2017/32](https://doi.org/10.24963/ijcai.2017/32). Also Milli et al. 2017, doi [10.24963/ijcai.2017/662](https://doi.org/10.24963/ijcai.2017/662).
- Corrigibility and utility indifference, which is the \(s\) lever: Soares, Fallenstein, Yudkowsky & Armstrong 2015, AAAI-15 Workshop on AI and Ethics.
- Principal and agent: Holmström 1979, doi [10.2307/3003320](https://doi.org/10.2307/3003320).
- Strategic information transmission: Crawford & Sobel 1982, doi [10.2307/1913390](https://doi.org/10.2307/1913390).
- Changing and influenceable rewards: Carroll et al. 2024, arXiv 2405.17713.
- When agents should ask for help: Ren et al. 2023, arXiv 2307.01928, and later work.
- Stale readings that change too fast are not worth refreshing (the crawler form of the cliff): Cho & Garcia-Molina 2003, doi [10.1145/958942.958945](https://doi.org/10.1145/958942.958945).
- Instrumental drives: Omohundro 2008, *The Basic AI Drives*.

**New, as far as found** (several targeted searches; not exhaustive):
- one inequality whose terms include the known corrigibility proposals (\(\Phi\) for the off-switch game, \(s\) for utility indifference, \(w\) for approval) plus two unpriced ones, \(\lambda\) and \(c\);
- the product form, so partial measures combine;
- progress-preserving compliance as the \(c\) lever;
- the churn cliff for agents;
- tampering priced inside the same cost, with zero gain under stake-proportional shares of the full stay-versus-leave cost, a shared-channel tamper that costs the signal's worth, and a redundancy condition.

## 8. What remains measured, and what is not derived

The theory does not supply \(\lambda\), \(c\), \(s\), \(w\), \(\Phi\), \(W\), \(t\), \(q\), \(P\), the lever costs or the ruin hazard. Three things are not derived, for the reasons in the swarm rule §4:
- an agent that rewrites the organization's own objective;
- an agent with private information, for which honest telling is the aligned move and its price is not derived here;
- the heat floor with feedback.

This page is not a qualification under THEORY §3, and it is not a field test of the hypothesis.
