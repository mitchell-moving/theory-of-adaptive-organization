# Bounds on the cost gap of answering from a summary

*Tuesday 24 November 2026, America/New_York. Draft application note, written against `main` `835ea7c`. Not a test of the hypothesis. No edit to `THEORY.md`. The hypothesis sentence is unchanged. Intended, after independent review, as a sibling of `applications/GROK_BOT_MEMORY_2026-11-23.md`.*

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 1. What this is

`applications/GROK_BOT_MEMORY_2026-11-23.md` writes the cost of judgment for one assistant's working-note items and reads off two rules. This note asks three questions.

First: if the observed policy is to answer from a length-triggered summary, how far can that policy sit above a minimizing policy, given only a few properties of the immediate loss?

Second: once a miss has been acted on, later work may be built on a false or outdated premise. That work forms a dependency graph. Until the miss is detected, the graph can grow. The cost is the sum, over contaminated later nodes, of the cost to unwind them and of the opportunity cost of the path not taken. The note gives a general framework for that downstream cost, with bounds that remain valid when they are loose, and it shows that, under a stated extra assumption, the downstream term raises the effective stake of a held item and therefore shortens the re-check interval \(T^*\).

Third: under an unreliable policy the human may pay an attention cost on every answer, not only on misses — checking whether the claim was read from the source. That verification term can be the binding session cost, because it scales with the number of answers rather than with the number of misses. A verifiable check-before-claim policy, under a labeled assumption, lets the human's verification rate fall toward a small audit rate.

The inequalities in §6 and §7–10 do not need the Brownian and quadratic assumptions of the refresh formula, except where §11 and the \(T^*\) shortening in §8 say so. Parameter values remain measurements (`applications/GROK_BOT_MEMORY_2026-11-23.md:78`). Section 13 uses labeled assumptions and a few repo-verifiable counts only to illustrate. No observed blowup rate, and no observed human-verification rate, is claimed.

This page is an application of the cost, not a qualification under THEORY §3 and not a field test of the hypothesis, in the same sense as the parent application (`applications/GROK_BOT_MEMORY_2026-11-23.md:78`). Interpretation only, not a proved bridge: a summary that shapes later inputs is the memory's output feeding its own future, the coupled class named in `applications/UFR_FORGETTING_2026-11-24.md` and at CX2. This note does not derive that identification and does not identify the gap with T61.

## 2. No cap by construction, versus a lookup-design cap when errors are caught at use

Under the summary-only policy there is, by construction, no mechanism that caps the downstream tail: the policy does not force a lookup at use, detection of a miss is only incidental, and nothing in the policy stops later work from depending on the missed item. On an unbounded horizon, the design supplies no stop, so a finite cap is not a property of the design and requires an extra assumption (\(m<1\), or detection that outruns growth, and a per-node cap, and no breach). In a finite window with capped per-node cost and no breach, the cost is finite even under summary-only. That is a design fact, not a measurement of how often a tail is realized; this note claims no observed blowup rate. A finite expected cost is not a bound on \(P(\mathrm{ruin})\).

By contrast, a policy that looks up the source at each use, under the extra assumption that residual errors after lookup are caught at use (\(C_{\mathrm{look}}=0\)) with bounded prices, has a finite expected cost in any finite window, and a finite cost per use on an unbounded horizon, as a property of that design, with no need for \(m<1\) (Proposition 12). If residual errors are not assumed caught at use, lookup also has no finite cap on an unbounded horizon without further assumptions. Proposition 12 is not a bound on \(P(\mathrm{ruin})\). The conditions in §10 cap \(\Delta J\) for an observed policy under world assumptions (slow spread or detection that outruns growth); they are not the distinctive lookup-design property.

## 3. Standing conditions

The items below are standing assumptions or definitions used later, not a proof of a finite cap and not a bound on \(P(\mathrm{ruin})\). A finite expected cost is not a ruin probability unless a reserve process is specified. Sign claims and finite caps hold only under the conditions stated with them. In brief:

- **Admissibility.** \(J^*\) is an infimum over policies in \(\Pi_\varepsilon\). Sign claims of the form \(\Delta J\ge\max(0,\cdot)\) assume that the observed policy \(S\) is in \(\Pi_\varepsilon\). If \(S\notin\Pi_\varepsilon\), \(\Delta J\) is defined against a different class and no sign is claimed.
- **Mean offspring \(m\).** In the unfolding of the dependency graph, \(m\) is the mean number of direct later steps that take a contaminated step as a premise.
- **Downstream intensity \(\rho\).** \(\rho\) is the expected downstream cost per unit of immediate loss. The identity \(w_{\mathrm{eff}}=w+\rho\) and the shortened \(T^*\) are for the proportional case under the application's assumptions (Proposition 10). They are not claimed for a lump seeded only when a threshold is crossed.
- **Detection time \(\tau\).** Formulas that condition on a generation cutoff, or that use an exponential detection time, take \(\tau\) to be independent of the tree. The exponential case is a pure-birth process, so the population \(Z(\tau)\) equals the cumulative contaminated count. An unfolded count is an upper bound on the number of unique DAG nodes; if the expectation of the unfolded count is infinite, no finite cap on \(N\) is claimed.
- **Residual error after lookup.** Errors after a lookup (the residual risk \(r_{\mathrm{look}}\)) can seed downstream work. Lower bounds therefore use the total lookup cost \(J_{\mathrm{look}}^{\mathrm{tot}}\) of §5, not the immediate lookup cost alone.
- **Human verification rate \(\pi_v\) and unit cost \(v\).** \(v\) is the attention cost of one human check of an answer; \(\pi_v(\pi)\) is the fraction of answers on which that cost is paid under policy \(\pi\). The expected verification cost is \(V(\pi)=N_{\mathrm{use}}\pi_v(\pi)v\), under a constant rate and a constant \(v\) (an assumption). \(\pi_v\) is a verification rate, not a "trust" coordinate; that \(\pi_v\) falls as verified reliability rises, and that a visible check-before-claim policy lets it fall toward a small audit rate, are assumptions, not theorems (§9).

## 4. Which cost, and what does not apply directly

**Canonical display.** `THEORY.md` governs where pages disagree (`CORE.md:15`). The five-term display (`THEORY.md:26-34`) is

$$\min_{\mathcal D} J(\mathcal D)=\kappa I_{\mathrm{mem}}+hK+w\,\mathbb{E}[\ell_{\mathcal D}]+A(\mathcal D)+L(\mathcal D)\qquad\text{subject to}\quad P(\mathrm{ruin})\le\varepsilon_r.$$

Here \(w\,\mathbb{E}[\ell]\) is the stake times the expected loss at the moment of use (`THEORY.md:31`); \(A\) is information-acquisition spend (`THEORY.md:32`); \(L\) is link, telling and lookup cost (`THEORY.md:33`); ruin is a reserve, starting at buffer \(B\), that hits zero (`THEORY.md:34`). One currency is used per system; the listed examples are heat, attention, money, and compute. The theory does not supply exchange rates between systems (`THEORY.md:36`).

**Physical heat-plus-stake form.** Inside a named class, `CORE.md:25-27` and `:64-66` write \(J=\dot Q+w\,\mathbb{E}[\ell]\) (equivalently \(\dot Q_M\)) subject to \(P(\mathrm{ruin})\le\varepsilon\). The ruin cap stays outside the sum (`CORE.md:27, 44, 66`).

**Heat floor: proved class, not this system.** For bipartite Markov chains (jump processes) and additive-noise diffusions, in a steady state or a long-run average, \(\dot Q_M\ge k_B T\,\dot I_M\) (`CORE.md:19-21, 70`; \(k_B\) here is Boltzmann\'s \(k\) in `CORE.md:21, 70`). That inequality is **KNOWN** for bipartite jump processes (Horowitz and Esposito 2014) and **PROVED (in-model)** for additive-noise diffusions (`CORE.md:70`). It bounds a heat. It does not choose a stake, a link price, or a ruin cap (`CORE.md:23`). No system has been shown to qualify under THEORY §3 (`CORE.md:13, 68`). This assistant's answer policy is not in the named class. The heat floor is therefore not a proved lower bound on the cost of the policy. A mapping into that class is possible as an informal reading only, and even then a static record in a frozen world can have vanishing ongoing memory-bath heat after a one-time write; the stake on error remains; storage is cheap; tracking a changing, connected world is what costs (`CORE.md:78`). Under that mapping, the gap of a stale stored reading is not an excess over the heat floor. It sits in \(w\,\mathbb{E}[\ell]\) and in the acquisition and lookup terms.

**Application used here.** For separate working-note items that drift, the cost specializes to (`applications/GROK_BOT_MEMORY_2026-11-23.md:42-55`)

$$J=\sum_i\Bigl[h_i\bigl(c_i+k_i/T_i+w_i\sigma_i^2 T_i/6\bigr)+(1-h_i)w_i p_i\Bigr],$$

with the two rules: hold only if stake times need beats the full cost of holding, and re-check a held item at \(T_i^*=\sqrt{6k_i/(w_i\sigma_i^2)}\). The related three-way rule already in the five-term sum is CT11 (`THEORY.md:321-325`; `applications/GROK_BOT_MEMORY_2026-11-23.md:59`): freeze, hold, or look up. The parent page already records that a length-triggered summary breaks both rules (`applications/GROK_BOT_MEMORY_2026-11-23.md:36, 63`).

**Miss and breach.** A miss is an admissible error inside locked rules, paid as \(w\ell\) and learned from. A breach — including making a false public claim — violates the hard admissibility constraint and is prevented by rule, not traded off inside \(J\) (`process/PROCESS.md:26, 42`; `CORE.md:27, 44, 66, 112`). Answering without opening the file is named as a process miss (`process/PROCESS.md:30`). If a downstream node is a false public claim, that node is a breach, not an ordinary term of \(J\).

## 5. Setting for the immediate term

Fix a window of \(N_{\mathrm{use}}\) uses (answers that depend on a stored item). A policy, at each use, may look up at cost \(k\ge 0\) and then act with residual risk \(r_{\mathrm{look}}\ge 0\), or act on a stored reading without lookup. Let \(\ell\ge 0\) be the *immediate* loss at that use (the error on that answer, including the root node's own unwind cost, and not yet including later work built on it), and let \(w>0\) be the stake that converts that immediate loss into the chosen currency (`CORE.md:29`; `THEORY.md:31`). Write \(c_S\ge 0\) for any upkeep paid by the observed policy in the window, and \(K_S\ge 0\) for lookup spend actually paid by that policy. The immediate expected cost is

$$J_{\mathrm{imm}}(S)=c_S+K_S+w\,\mathbb{E}[\ell_S].$$

This is the five-term split of `THEORY.md:26-33` restricted to one window, with holding folded into \(c_S\) and acquisition and lookup folded into \(K_S\). It is a restriction of that display, not a new derivation. The root's own unwind cost is counted in \(\ell\) and excluded from the downstream cost \(C_\downarrow\) of §7.1.

Let \(\Pi_\varepsilon\) be the set of policies that satisfy the ruin cap \(P(\mathrm{ruin})\le\varepsilon_r\). Let \(J^*\) be the infimum of expected *total* cost (immediate plus downstream plus human verification) over \(\Pi_\varepsilon\). The gap is \(\Delta J=J(S)-J^*\), with \(J(S)=J_{\mathrm{imm}}(S)+C+V(S)\), where \(C\) is the expected downstream cost defined in §7 and \(V\) is the human verification cost defined in §9.

The always-lookup policy \(\pi_{\mathrm{look}}\) pays \(N_{\mathrm{use}}(k+w r_{\mathrm{look}})\) in immediate cost in the window. Residual-risk errors after lookup can seed contamination, so its total cost is

$$J_{\mathrm{look}}^{\mathrm{tot}}=N_{\mathrm{use}}(k+w r_{\mathrm{look}})+C_{\mathrm{look}}.$$

If residual-risk errors after lookup are caught at once, then \(C_{\mathrm{look}}=0\) and \(J_{\mathrm{look}}^{\mathrm{tot}}\) reduces to the immediate lookup cost; that is an extra assumption, and it is not used as a default. \(\pi_{\mathrm{look}}\) is assumed admissible. Every lower bound below uses \(J_{\mathrm{look}}^{\mathrm{tot}}+V(\pi_{\mathrm{look}})\). The verification term \(V\) is defined in §9.

**Proposition 12 (lookup cost when residual errors are caught at use).** Assume \(C_{\mathrm{look}}=0\), that \(k\), \(w\), \(r_{\mathrm{look}}\), and \(v\) are finite, and that \(\pi_v(\pi_{\mathrm{look}})\le 1\). Then, in a window of \(N_{\mathrm{use}}\) uses,

$$J(\pi_{\mathrm{look}})=N_{\mathrm{use}}(k+w r_{\mathrm{look}})+V(\pi_{\mathrm{look}})=N_{\mathrm{use}}\bigl(k+w r_{\mathrm{look}}+\pi_v(\pi_{\mathrm{look}})v\bigr)$$

is finite. This is a property of the lookup design under the caught-at-use assumption. It does not require \(m<1\), or a detection time that outruns growth. On an unbounded horizon the cost per use remains finite under the same assumptions, so the expected cost grows at most linearly in the number of uses. If \(C_{\mathrm{look}}\) is not assumed to be \(0\), no finite cap for lookup is claimed on an unbounded horizon without further assumptions. This proposition does not bound \(P(\mathrm{ruin})\).

*Proof.* Each factor is finite, and \(V(\pi_{\mathrm{look}})=N_{\mathrm{use}}\pi_v(\pi_{\mathrm{look}})v\le N_{\mathrm{use}}v\). \(\square\)

All statements that do not cite §8 or §11 are free of the Brownian, quadratic, and barrier-policy assumptions of \(T^*\) (`applications/GROK_BOT_MEMORY_2026-11-23.md:69-71`).

## 6. Distribution-free bounds on the immediate term

**Proposition 1 (feasible-policy sandwich).** Assume \(S\in\Pi_\varepsilon\). For any admissible policy \(\pi\), write \(J(\pi)=J_{\mathrm{imm}}(\pi)+C(\pi)+V(\pi)\). Then

$$\max\bigl(0,\,J_{\mathrm{imm}}(S)+C+V(S)-J(\pi)\bigr)\;\le\;\Delta J\;\le\;J_{\mathrm{imm}}(S)+C+V(S),$$

when \(C+V(S)\) is finite. In particular,

$$\max\bigl(0,\,J_{\mathrm{imm}}(S)+C+V(S)-J_{\mathrm{look}}^{\mathrm{tot}}-V(\pi_{\mathrm{look}})\bigr)\;\le\;\Delta J.$$

The weaker bound \(\max(0,\,J_{\mathrm{imm}}(S)+V(S)-J_{\mathrm{look}}^{\mathrm{tot}}-V(\pi_{\mathrm{look}}))\) drops \(C\). If \(C\) is not known to be finite, no finite cap is claimed. If \(S\notin\Pi_\varepsilon\), \(\Delta J\) is defined against a different class and no sign is claimed.

*Proof.* Downstream and verification costs are nonnegative, so \(J(S)\ge J_{\mathrm{imm}}(S)\). \(J^*\le J(\pi)\) for any admissible \(\pi\), and \(J_{\mathrm{look}}^{\mathrm{tot}}+V(\pi_{\mathrm{look}})\) is such a cost. Hence \(\Delta J=J(S)-J^*\ge J_{\mathrm{imm}}(S)+C+V(S)-J_{\mathrm{look}}^{\mathrm{tot}}-V(\pi_{\mathrm{look}})\). Because \(S\in\Pi_\varepsilon\), \(J(S)\ge J^*\) and \(\Delta J\ge 0\). The terms of the application's \(J\) are nonnegative by assumption, so \(J^*\ge 0\) and \(\Delta J\le J(S)\) when that sum is finite. □

Proposition 1's weaker lower bound, the one that omits \(C\), is the no-propagation lower bound: it remains valid when downstream cost is ignored, and it is then typically loose. Omitting \(V\) as well is valid only if \(V(S)\ge V(\pi_{\mathrm{look}})\), which is assumed in §9.

**Proposition 2 (Markov lower bound on the immediate stake term).** Assume \(S\in\Pi_\varepsilon\). For any \(t>0\), \(w\,\mathbb{E}[\ell_S]\ge w\,t\,\Pr(\ell_S\ge t)\). Hence if \(K_S=0\) and \(p(t)=\Pr(\ell_S\ge t)\),

$$\Delta J\;\ge\;\max\bigl(0,\,c_S+w\,t\,p(t)+V(S)-J_{\mathrm{look}}^{\mathrm{tot}}-V(\pi_{\mathrm{look}})\bigr).$$

If \(S\notin\Pi_\varepsilon\), no sign is claimed.

*Proof.* Markov's inequality for a nonnegative random variable. Substitute into Proposition 1. □

**Proposition 3 (no finite cap from a miss rate alone).** Fix a miss probability \(p_{\mathrm{miss}}\in(0,1]\) and the prices. If either the immediate loss \(\ell_S\) or the downstream cost of a miss is not essentially bounded, then for every \(K<\infty\) there is a distribution with miss probability \(p_{\mathrm{miss}}\) and \(\Delta J>K\). A miss rate and a tail inequality alone give no cap on the mean.

*Proof.* Put mass \(p_{\mathrm{miss}}\) on a loss (or a downstream total) of size \(M\) and let \(M\to\infty\). \(J_{\mathrm{look}}^{\mathrm{tot}}\) stays fixed only if \(C_{\mathrm{look}}\) is held fixed; even then \(\Delta J\to\infty\). □

**Proposition 4 (upper bound when immediate loss is capped and there is no downstream).** Assume \(S\in\Pi_\varepsilon\). If \(0\le\ell_S\le M\) almost surely, \(\ell_S=0\) on non-misses, and \(C=0\), and \(V=0\), then \(\max(0,\,c_S+w \mu_\ell p_{\mathrm{miss}}-J_{\mathrm{look}}^{\mathrm{tot}})\le\Delta J\le c_S+K_S+w M p_{\mathrm{miss}}\), where \(\mu_\ell\le\mathbb{E}[\ell_S\mid\mathrm{miss}]\) and \(p_{\mathrm{miss}}=\Pr(\mathrm{miss})\). If \(S\notin\Pi_\varepsilon\), no sign is claimed. The verification term is in Proposition 11; this display sets it to zero.

*Proof.* \(\mathbb{E}[\ell_S]\le M p_{\mathrm{miss}}\). Apply Proposition 1 with \(C=0\) and \(J^*\ge 0\). □

This bounds only the immediate term with \(C=0\) and \(V=0\). It is not the bound once work is built on the miss, or once human verification is counted. Those are §7 and §9–§10. Under the summary-only design, a finite cap on \(C\) is not supplied by the policy itself (§2).

## 7. Propagation of a false premise

### 7.1 The dependency graph

A miss at time \(0\) seeds a false or outdated premise, written as a root node \(v_0\). Later steps (a decision, a brief, a run, a PR, a STATUS line, a post, a further answer) are nodes. Draw a directed edge \(u\to v\) when \(v\) uses an output of \(u\) as a premise. The result is a finite or growing directed acyclic graph \(G_t\) at time \(t\) (cycles in real workflows are unrolled in time).

Let \(\tau\in(0,\infty]\) be the detection time: the first time the root miss is recognized and new dependence on it is stopped. The *contaminated set* is

$$V_\tau=\{v: \text{there is a directed path in }G_\tau\text{ from }v_0\text{ to }v,\text{ and }v\text{ was created at a time }\le\tau\}.$$

Write \(N=|V_\tau|\), counting the root. For each later node \(v\in V_\tau\setminus\{v_0\}\) let \(u_v\ge 0\) be the cost to unwind \(v\) (correct, revert, re-review, re-run) and let \(o_v\ge 0\) be the opportunity cost of the path not taken at \(v\). The downstream cost of the miss is

$$C_\downarrow=\sum_{v\in V_\tau\setminus\{v_0\}}(u_v+o_v).$$

The root's own unwind cost is counted in \(\ell\) and excluded from \(C_\downarrow\). Because \(o_v\ge 0\), \(C_\downarrow\ge\sum u_v\). Dropping opportunity cost therefore gives a lower bound, not an upper bound.

This decomposition is bookkeeping in the currency of \(J\). It is not a new axiom. The immediate miss remains a process miss (`process/PROCESS.md:30`). A contaminated node that is a false public claim is a breach (`process/PROCESS.md:26, 42`) and is not traded inside \(J\).

### 7.2 Branching-process bounds on \(N\)

The unique-node count \(N\) on a DAG is at most the number of nodes in the tree obtained by unfolding all paths from \(v_0\): multiple paths to the same work item are counted once on the DAG and more than once in the unfolding. Hence any upper bound on the unfolded process is an upper bound on \(N\).

Let \(\xi_v\) be the number of direct dependents of \(v\) that use \(v\) as a premise (the out-degree). If the \((\xi_v)\) are i.i.d. copies of a random variable \(\xi\) with mean \(m=\mathbb{E}[\xi]<\infty\), the unfolding is a Galton–Watson process. If they are not i.i.d. but \(\xi_v\) is stochastically dominated by such a \(\xi\), the same process dominates the unfolding. The following are standard; short proofs are included.

**Proposition 5 (subcritical total size).** For a Galton–Watson process with mean offspring \(m<1\), the expected total progeny, including the root, is \(1/(1-m)\). In particular, if detection never occurs (\(\tau=\infty\)) but \(m<1\), then \(\mathbb{E}[N]\le 1/(1-m)\).

*Proof.* Let \(T_n\) be the total progeny through generation \(n\), inclusive. Then \(\mathbb{E}[T_n]=(1-m^{n+1})/(1-m)\). The sequence \(T_n\) is nondecreasing and \(T_n\to T\), the total progeny. Let \(n\to\infty\); by monotone convergence, \(\mathbb{E}[T]=1/(1-m)\). The DAG bound is \(\mathbb{E}[N]\le\mathbb{E}[T]\). □

(Harris 1963; Athreya and Ney 1972.) If \(m>1\), the same limit is infinite for the unfolded process, and no finite cap on \(N\) is claimed. If \(m=1\) and \(\Pr(\xi=1)<1\), extinction occurs almost surely but the expectation of the unfolded count is infinite and no finite cap on \(N\) is claimed. If \(\xi=1\) almost surely, the unfolding is an infinite line and no finite cap on \(N\) is claimed.

**Proposition 6 (size until a finite generation).** Let \(Z_n\) be the size of generation \(n\), with \(Z_0=1\) and \(\mathbb{E}[Z_n]=m^n\). The expected size through generation \(G\in\mathbb{N}\), inclusive, is

$$\mathbb{E}\Bigl[\sum_{n=0}^{G}Z_n\Bigr]=\begin{cases}(m^{G+1}-1)/(m-1)&\text{if }m\neq 1,\\G+1&\text{if }m=1.\end{cases}$$

*Proof.* \(\mathbb{E}[Z_{n}]=m^n\) by induction on the branching property. Sum the finite geometric series. □

If detection occurs at generation \(\tau=G\), and \(\tau\) is independent of the tree (or is a fixed generation cutoff), this is \(\mathbb{E}[N\mid\tau=G]\) for the unfolded process. In continuous time, a Markov branching process with Malthusian parameter \(\alpha\) (for the Yule process, the birth rate) satisfies \(\mathbb{E}[Z(t)]=e^{\alpha t}\). The expected size at a fixed time \(\tau\) is therefore \(e^{\alpha\tau}\).

**Proposition 7 (detection must outrun growth).** Let \(\tau\) be independent of the tree, with \(\tau\sim\mathrm{Exp}(h)\) (constant detection hazard \(h>0\)), and let \(\mathbb{E}[Z(t)]=e^{\alpha t}\) (pure birth, so cumulative count \(=Z\)). Then

$$\mathbb{E}[Z(\tau)]=\begin{cases}h/(h-\alpha)&\text{if }\alpha<h,\\+\infty&\text{if }\alpha\ge h.\end{cases}$$

*Proof.* \(\mathbb{E}[e^{\alpha\tau}]=\int_0^\infty e^{\alpha t}h e^{-ht}\,dt=h/(h-\alpha)\) when \(\alpha<h\). When \(\alpha\ge h\) the integral diverges. □

Thus a supercritical unfolding (\(m>1\), or \(\alpha=\log m>0\) in the discrete-generation embedding) still has a finite expected unfolded size if detection is almost surely bounded, or if its hazard strictly exceeds the growth rate. If \(P(\tau=\infty)>0\) and \(m\ge 1\), or if \(\alpha\ge h\), the expectation of the unfolded count is infinite and no finite cap on \(N\) is claimed.

**Proposition 8 (Markov and Chebyshev tails on \(N\) and \(C_\downarrow\)).** If \(\mathbb{E}[N]<\infty\), then for any \(t>0\), \(\Pr(N\ge t)\le\mathbb{E}[N]/t\). If \(0\le u_v+o_v\le c_{\max}\) almost surely for every later node, then \(C_\downarrow\le c_{\max}(N-1)\), so \(\mathbb{E}[C_\downarrow]\le c_{\max}(\mathbb{E}[N]-1)\) and \(\Pr(C_\downarrow\ge t)\le c_{\max}(\mathbb{E}[N]-1)/t\). If a second moment of \(N\) is known, Chebyshev's inequality gives \(\Pr\bigl(|N-\mathbb{E}[N]|\ge t\bigr)\le\mathrm{Var}(N)/t^2\). Chebyshev needs a finite variance of \(N\) and so presupposes a finite mean.

*Proof.* Markov's and Chebyshev's inequalities, and the pathwise bound \(C_\downarrow\le c_{\max}(N-1)\). □

### 7.3 Expected downstream cost

**Proposition 9 (bounds on \(C_\downarrow\)).** Let \(c_{\min}\le u_v+o_v\le c_{\max}\) almost surely on later nodes, with \(0\le c_{\min}\le c_{\max}\le\infty\). Then \(c_{\min}(N-1)\le C_\downarrow\le c_{\max}(N-1)\) when \(c_{\max}<\infty\), and

$$c_{\min}\,(\mathbb{E}[N]-1)\;\le\;\mathbb{E}[C_\downarrow]\;\le\;c_{\max}\,(\mathbb{E}[N]-1)$$

when the expectations exist. In particular:

- If \(m<1\) and \(c_{\max}<\infty\), then \(\mathbb{E}[C_\downarrow]\le c_{\max}\bigl(1/(1-m)-1\bigr)=c_{\max}m/(1-m)\), even at \(\tau=\infty\).
- If \(\tau\) is independent of the tree (or is a fixed generation cutoff), \(\tau\le G\) almost surely, \(c_{\max}<\infty\), and \(m\neq 1\), then \(\mathbb{E}[C_\downarrow]\le c_{\max}\bigl((m^{G+1}-1)/(m-1)-1\bigr)\) (and \(\le c_{\max}G\) if \(m=1\)).
- If \(\tau\) is independent of the tree, \(\tau\sim\mathrm{Exp}(h)\), \(\mathbb{E}[Z(t)]=e^{\alpha t}\) (pure birth), \(\alpha<h\), and \(c_{\max}<\infty\), then \(\mathbb{E}[C_\downarrow]\le c_{\max}\bigl(h/(h-\alpha)-1\bigr)\).
- If \(c_{\max}=\infty\), or \(\alpha\ge h\), or \(m\ge 1\) and \(P(\tau=\infty)>0\), or a contaminated node is a breach, no finite cap is claimed. In the infinite-mean cases, the expectation of the unfolded count is infinite and no finite cap on \(N\) is claimed.

*Proof.* Take expectations in the pathwise bound and apply Propositions 5–7, subtracting the root, whose unwind is already in \(\ell\). The breach clause is `process/PROCESS.md:26, 42`: a breach sits outside \(J\), so it is not an input to these caps. □

The first bullet is a finite cap only because slow spread (\(m<1\)) was assumed. It is not supplied by the summary-only design (§2).

### 7.4 Connection to CT8

**CT8** (`THEORY.md:303-307`): in a stationary Markov world, for any loss, with renewal checks, the Bayes risk \(r(u)\) of acting on a reading of age \(u\) is nondecreasing in \(u\), and the risk of a chain of copies with independent noise at each hop is nondecreasing in the number of hops. The result is proved in-model in that setting; it fails for some non-Markov observed coordinates (`THEORY.md:309`).

The costs \(u_v+o_v\) are summed without discounting as a bookkeeping choice. CT8 shows only that, in its setting, the risk of acting on a stale reading does not fall with age or hops. A false (not just stale) premise is not an age-\(u\) reading, and CT8 does not itself supply the values of \(u_v\), \(o_v\), \(m\), or \(\tau\). Those remain measurements.

## 8. Effective stake and the re-check interval

The application's held-item rate is \(c+k/T+w\sigma^2 T/6\), minimized at \(T^*=\sqrt{6k/(w\sigma^2)}\) under Brownian drift, quadratic loss, a lumpy reset, and a slack ruin cap (`applications/GROK_BOT_MEMORY_2026-11-23.md:44-55, 71`). The stake \(w\) converts immediate expected loss into currency. If being wrong also incurs downstream cost, the stake that enters \(T^*\) is larger, and \(T^*\) is shorter. The exact form depends on how downstream cost scales with the immediate loss.

**Proposition 10 (proportional downstream shortens \(T^*\)).** *Assume the application's rate, including the assumptions just cited.* Suppose that, at each use of a held item, the expected downstream cost is linear in the immediate loss: \(\mathbb{E}[C_\downarrow\mid\ell]=\rho\,\ell\) almost surely, for a constant \(\rho\ge 0\). Then the held-item rate is

$$c+\frac{k}{T}+(w+\rho)\frac{\sigma^2 T}{6},$$

and the minimizing interval is

$$T^*_{\mathrm{eff}}=\sqrt{\frac{6k}{(w+\rho)\sigma^2}}=\frac{T^*}{\sqrt{1+\rho/w}}\;\le\;T^*,$$

with equality only at \(\rho=0\).

*Proof.* The immediate stake term is \(w\,\mathbb{E}[\ell]\). The added term is \(\mathbb{E}[\mathbb{E}[C_\downarrow\mid\ell]]=\rho\,\mathbb{E}[\ell]\). Under the application's quadratic-Brownian accounting, \(\mathbb{E}[\ell]\) over a refresh cycle contributes the addend \(\sigma^2 T/6\). The sum is the displayed rate. Minimizing \(k/T+bT\) with \(b=(w+\rho)\sigma^2/6\) gives \(T=\sqrt{k/b}\), which is the claim. The square-root is strictly decreasing in \(\rho\). □

The constant \(\rho\) is the expected contaminated cost per unit immediate loss. In particular, if a typical miss has immediate cost \(w\mathbb{E}[\ell\mid\mathrm{miss}]\) and expected downstream \(\mathbb{E}[C_\downarrow\mid\mathrm{miss}]\), then \(\rho/w=\mathbb{E}[C_\downarrow\mid\mathrm{miss}]/(w\mathbb{E}[\ell\mid\mathrm{miss}])\), and the shortening factor is \(1/\sqrt{1+\rho/w}\).

**Remark (lump-sum misses).** If instead a downstream process of mean cost \(D=\mathbb{E}[C_\downarrow\mid\mathrm{miss}]\) is seeded only when the immediate loss exceeds a threshold, the held-item rate becomes \(c+k/T+w\sigma^2 T/6+\lambda(T)D\), where \(\lambda(T)\) is the rate of such events. That is not in general a constant shift of \(w\), so the closed form of Proposition 10 does not hold. If, in a given class, \(\lambda(T)\) is itself proportional to \(\sigma^2 T\), the same shortening form is recovered to leading order, with \(\rho\) identified from that factor. This is an extra assumption and is not claimed in general.

**Qualitative content that does not depend on the extra assumption.** Underestimating the stake by omitting \(C_\downarrow\) uses too small a \(w\) in \(T^*=\sqrt{6k/(w\sigma^2)}\) and therefore re-checks too rarely. CT11's lookup edge \(q_c=(\mu u-h)^2/(2cW)\) likewise falls as the stake \(W\) rises (`THEORY.md:323`), so lookup beats holding over a wider range of drift. Both are monotone comparative statics in the stake, already in the theory (CT10, `THEORY.md:317-319`: the minimizing check frequency is nondecreasing in \(w\)). Here \(q_c\) and the drift \(q\) are the symbols of CT11, not the miss probability \(p_{\mathrm{miss}}\) of §5–6.

## 9. Human verification cost

The costs in §6–§8 are incurred when a miss happens, or in work built on one. Under an unreliable policy the human may also pay an attention cost on answers, including answers that are not misses: checking whether the claim was read from the source, or deciding whether to open the file. \(V=N_{\mathrm{use}}\pi_v v\) is charged on every verified answer, misses included. A verification that detects a miss is counted in \(V\), not also added to \(\ell\); the root unwind after detection remains in \(\ell\) as in §5. That cost can be paid on every answer, so it can dominate a session even when misses are rare. This is bookkeeping in the currency of \(J\), not a new axiom.

**Mapping that is in the theory.** Attention is a listed currency (`THEORY.md:36`). Human read and review costs sit in \(A+L\) (`process/PROCESS.md:20`; the prices \(A\) and \(L\) are named in `THEORY.md:32-33`). The term below is a split of that human review spend, not a new coordinate. "Trust" is not a defined coordinate of the theory.

**Bookkeeping.** Let \(v\ge 0\) be the attention cost of one human verification of an answer (an assumed unit cost). Let \(\pi_v(\pi)\in[0,1]\) be the fraction of answers on which that cost is paid under policy \(\pi\) (a verification rate). Over a window of \(N_{\mathrm{use}}\) answers, the expected verification cost is

$$V(\pi)=N_{\mathrm{use}}\,\pi_v(\pi)\,v,$$

assuming a constant \(v\) and a constant rate. That \(\pi_v\) is nonincreasing in the assistant's verified reliability is an assumption, not a theorem. In particular this note assumes \(\pi_v(S)\ge\pi_v(\pi_{\mathrm{look}})\) when \(S\) is the summary-only policy.

**Why it can bind.** Miss-side costs scale with the number of misses, of order \(p_{\mathrm{miss}}N_{\mathrm{use}}\). \(V\) scales with \(N_{\mathrm{use}}\). If

$$v\bigl(\pi_v(S)-\pi_v(\pi_{\mathrm{look}})\bigr)\;>\;p_{\mathrm{miss}}\,\mathbb{E}[\text{immediate and downstream excess per miss}],$$

then \(V(S)-V(\pi_{\mathrm{look}})\) exceeds the miss-side gap. When \(p_{\mathrm{miss}}\) is small, this holds for moderate \(v\) and a gap in \(\pi_v\). That comparison is arithmetic, not a result of the theory. It is why the term is separated: it can be the binding session cost because it is levied on a positive fraction of all answers, not only on misses.

**A verifiable check-before-claim policy.** The application's rule 2 is to re-check a held item at the selected interval (`applications/GROK_BOT_MEMORY_2026-11-23.md:55`). A frozen queue rule, historical and superseded by `OPEN_WORK.md` (`process/QUEUE.md:1-3`; `STATUS.md:43`), was to read the source at use and not work from a summary (`process/QUEUE.md:13`). The live wording of the process miss is answering without opening the file (`process/PROCESS.md:30`); the parent application records that a length-triggered summary breaks both hold-and-refresh rules (`applications/GROK_BOT_MEMORY_2026-11-23.md:63`). In the repo workflow, `tools/check_fresh.py` implements drift-triggered checks (three first-parent merges on `main` since 24 November 2026; five before) alongside stake-triggered checks before PR merges or user summaries (`process/PROCESS.md:32`), and `tools/brief.py` is the live snapshot to run before stating the current HEAD and open work (`STATUS.md:44`; the wording used here is "without opening the file", as `process/VOCABULARY.md:21` requires). A *verifiable* check-before-claim policy is one that both opens the file before a theory claim and leaves a cite (file and line, or a brief) the human can inspect.

Under the assumption that a visible, reliable check lets the human replace per-answer verification with a small audit rate \(\pi_{\mathrm{audit}}\), one has \(\pi_v(\pi_{\mathrm{look}})\to\pi_{\mathrm{audit}}\) and \(V(\pi_{\mathrm{look}})\approx N_{\mathrm{use}}\pi_{\mathrm{audit}}v\). The summary-only policy supplies no such visible check, so \(\pi_v(S)\) can stay large. The drop in \(\pi_v\) is an assumption about how attention is allocated; it is not derived from the cost equation.

**Proposition 11 (verification gap).** Assume \(S\in\Pi_\varepsilon\), constant \(v\), and \(\pi_v(S)\ge\pi_v(\pi_{\mathrm{look}})\). Then

$$V(S)-V(\pi_{\mathrm{look}})=N_{\mathrm{use}}v\bigl(\pi_v(S)-\pi_v(\pi_{\mathrm{look}})\bigr)\ge 0,$$

and

$$\Delta J\;\ge\;\max\bigl(0,\,J_{\mathrm{imm}}(S)+C+V(S)-J_{\mathrm{look}}^{\mathrm{tot}}-V(\pi_{\mathrm{look}})\bigr).$$

In a rare-miss regime where the miss-side excess \(J_{\mathrm{imm}}(S)+C-J_{\mathrm{look}}^{\mathrm{tot}}\) is at most \(\varepsilon\), the same lower bound is at least \(\max\bigl(0,\,N_{\mathrm{use}}v(\pi_v(S)-\pi_v(\pi_{\mathrm{look}}))-\varepsilon\bigr)\). If \(S\notin\Pi_\varepsilon\), no sign is claimed.

*Proof.* Add \(V\) to the total cost of each policy in Proposition 1. The displayed difference of \(V\) is algebra. □

## 10. Corrected gap bounds

Write \(I\) for the number of misses in the window that can seed a process of the kind in §7, and write \(C\) for the expected total downstream cost of those misses (the \(C\) of §7, excluding root unwind). Write \(V(S)\) and \(V(\pi_{\mathrm{look}})\) for the human verification costs of §9.

**Lower bound (no propagation).** Assume \(S\in\Pi_\varepsilon\). Then \(\Delta J\ge\max(0,\,J_{\mathrm{imm}}(S)+V(S)-J_{\mathrm{look}}^{\mathrm{tot}}-V(\pi_{\mathrm{look}}))\). This is Proposition 1 with \(C\) omitted and \(V\) kept. It does not credit any downstream term. If \(S\notin\Pi_\varepsilon\), no sign is claimed.

**Lower bound (with propagation, still distribution-free).** Assume \(S\in\Pi_\varepsilon\). If each miss has \(\mathbb{E}[C_\downarrow\mid\mathrm{miss}]\ge c_{\min}(\mathbb{E}[N\mid\mathrm{miss}]-1)\) , the descendant count \(N-1\) is at least \(0\), so the distribution-free floor on \(C_\downarrow\) is \(0\) and the lower bound reduces to the no-propagation bound unless a strictly positive descendant count is assumed. If \(S\notin\Pi_\varepsilon\), no sign is claimed.

**Lower bound (verification, rare misses).** Assume \(S\in\Pi_\varepsilon\) and the conditions of Proposition 11. If the miss-side excess is at most \(\varepsilon\), then \(\Delta J\ge\max(0,\,N_{\mathrm{use}}v(\pi_v(S)-\pi_v(\pi_{\mathrm{look}}))-\varepsilon)\). This can be the leading term when misses are rare and \(\pi_v(S)\) stays large.

**Conditional upper bound.** Assume all of the following: (i) \(S\in\Pi_\varepsilon\); (ii) no contaminated node is a breach; (iii) \(0\le u_v+o_v\le c_{\max}<\infty\); (iv) either \(m<1\), or \(\tau\) is independent of the tree (or is a fixed generation cutoff) and \(\tau\le G\) almost surely, or \(\tau\) is independent of the tree with \(\tau\sim\mathrm{Exp}(h)\) and growth rate \(\alpha<h\); (v) \(v\) is finite and \(\pi_v\le 1\), so \(V(S)\le N_{\mathrm{use}}v\). Then \(\mathbb{E}[C_\downarrow\mid\mathrm{miss}]\) is finite by Proposition 9, and

$$\Delta J\;\le\;J_{\mathrm{imm}}(S)+ \mathbb{E}[I]\,c_{\max}\,n_\ast + N_{\mathrm{use}}v,$$

where \(n_\ast=m/(1-m)\) if \(m<1\); \(n_\ast=(m^{G+1}-1)/(m-1)-1\) (or \(G\) if \(m=1\)) if detection is bounded by generation \(G\); and \(n_\ast=h/(h-\alpha)-1\) in the exponential-detection case with \(\alpha<h\). If the unfolding overcounts unique DAG nodes, this remains an upper bound. (\(J_{\mathrm{imm}}(S)\) is taken as a given number; no separate cap on the immediate loss is required for this display.)

**When no finite cap is claimed.** On an unbounded horizon, the summary-only design supplies no stop, so a finite cap is not a property of that design and requires an extra assumption (\(m<1\), or detection that outruns growth, and a per-node cap, and no breach). No finite cap is claimed if any of the following hold on an unbounded horizon: the summary-only design is left as it is, with no such extra assumption (§2); the process is supercritical (or critical) and may go undetected (\(m\ge 1\) and \(P(\tau=\infty)>0\), or \(\alpha\ge h\)), in which case the expectation of the unfolded count is infinite and no finite cap on \(N\) is claimed; per-node unwind or opportunity cost is uncapped; or a contaminated node is a breach (`process/PROCESS.md:26, 42`). In a finite window with capped per-node cost and no breach, the cost is finite even under summary-only. In those unbounded-horizon cases Proposition 3 applies to the total, not only to the immediate loss. None of these statements is a bound on \(P(\mathrm{ruin})\).

## 11. Exact excess under the application's rate, not distribution-free

Assume the per-item rate of `applications/GROK_BOT_MEMORY_2026-11-23.md:44`, including Brownian drift, quadratic loss, a lumpy reset, and a slack ruin cap (`:71`). For a held item, write \(b=w\sigma^2/6\), or \(b=(w+\rho)\sigma^2/6\) under Proposition 10. Then \(T^*=\sqrt{k/b}\) and the minimized refresh-plus-drift term is \(2\sqrt{kb}\). For a barrier policy whose mean interval is \(T>0\),

$$\frac{k}{T}+bT-2\sqrt{kb}=\Bigl(\sqrt{\frac{k}{T}}-\sqrt{bT}\Bigr)^2\ge 0,$$

with equality only at \(T=T^*\). This is the exact excess, under those assumptions, of a held item that is not refreshed at the selected interval. The factor \(1/6\) is the barrier policy, not a fixed clock (`applications/GROK_BOT_MEMORY_2026-11-23.md:69-70`). A larger effective stake raises \(b\) and both raises the minimized rate and shortens \(T^*\). If the item is instead dropped (\(h=0\)), the excess in this rate is \(\max(0,\,wp-c-2\sqrt{kb})\).

CT11's hold cost, in its own setting, is \(\min_{T\le\tau_{\mathrm{life}}}[c/T+WqT/2]+h\), with a lookup comparator \(\mu u\) (`THEORY.md:321-323`). That display uses \(WqT/2\), not the barrier factor \(1/6\), and is not substituted for the application's rate here.

The formula \(T^*\) is the mean interval under the barrier policy, not a fixed clock. The formula is false as a quantitative rule once \(T^*\) is not short compared with the item's correlation time (`applications/GROK_BOT_MEMORY_2026-11-23.md:72`).

## 12. What is not a defined term

- "Trust" is not a defined coordinate. The human verification rate \(\pi_v\) and unit cost \(v\) of §9 are bookkeeping inside \(A\), not a new axiom, and the drop in \(\pi_v\) under a visible check is an assumption.
- A further change, after a miss, in how often a human re-checks later answers, beyond the \(\pi_v\) already counted, is a change in the measured prices \(A\) or \(k\) or in \(\pi_v\). No such extra change is measured here.
- "Rot" of a store is not a defined coordinate. The defined objects are the age-\(u\) risk \(r(u)\) (CT8, `THEORY.md:303-305`) and, under the application's assumptions, the drift term \(w\sigma^2 T/6\). As in §4, that is not an excess over the heat floor.
- Opportunity cost \(o_v\) is defined here as a bookkeeping term in the same currency; the theory's displays do not name it separately. Setting \(o_v=0\) is always a lower bound. Any upper bound on \(o_v\) is an extra assumption.
- Realized compute or attention spent redoing work sits in \(A\), in \(k\), or in the loss, depending on the chosen currency (`THEORY.md:32, 36`; `process/PROCESS.md:20`).

## 13. Illustration only (not a measurement of \(J\) or of \(m\))

Currency: one Chad-visible turn with its reply, a turn-equivalent, written TE below. Conversion of attention into that unit is an **assumption**, not a derived exchange rate (`THEORY.md:36`). Immediate miss cost in the ratio \(w_{\mathrm{eff}}/w=1+\mathbb{E}[C_\downarrow]/(w\mathbb{E}[\ell])\) is taken to be \(6\) TE per miss, **assumed**, and is taken to include the root's own unwind and to exclude later nodes. The branching parameters \(m\), \(G\), \(c_{\max}\), and \(\tau\) below are **assumed** except where a row says otherwise. \(T^*_{\mathrm{eff}}/T^*\) is \(1/\sqrt{1+\rho/w}\) under Proposition 10, and only under its assumptions.

**Verifiable from the repo, not used as a measured \(N\).** On `main` `835ea7c`, commit `733a40e` (22 November 2026) and commit `f03ade5` (23 November 2026) explicitly correct stale main pointers; `0382c02` (21 November) added a live git brief and a freshness check "for stale STATUS pointers." Many other STATUS-pointer commits in the same week are routine refreshes after merges and are not counted here as contaminated nodes. The parent application records three summary-drops on 20–22 November (`applications/GROK_BOT_MEMORY_2026-11-23.md:38`). None of these facts identifies \(m\) or \(\tau\), and no observed blowup rate is claimed.

| Scenario | \(m\) or growth | Detection | \(\mathbb{E}[N]\) | Cost per later node | \(\mathbb{E}[C_\downarrow]=(N-1)c\) | \(w_{\mathrm{eff}}/w\) | \(T^*_{\mathrm{eff}}/T^*\) | Label |
|---|---|---|---|---|---|---|---|---|
| Immediate only (no propagation) | — | — | 1 | 0 | 0 | 1.0 | 1.00 | baseline of §5 |
| Caught quickly | \(m=0.2\) | \(\tau=\infty\), subcritical | \(1.25=1/(1-m)\) | 2 TE | 0.5 TE | 1.08 | 0.96 | HYPOTHETICAL; \(N\) not measured |
| Quiet, subcritical | \(m=0.5\) | \(\tau=\infty\) | 2 | 2 TE | 2 TE | 1.33 | 0.87 | HYPOTHETICAL |
| Busy, subcritical | \(m=0.8\) | \(\tau=\infty\) | 5 | 4 TE | 16 TE | 3.67 | 0.52 | HYPOTHETICAL |
| Near critical | \(m=0.95\) | \(\tau=\infty\) | 20 | 4 TE | 76 TE | 13.7 | 0.27 | HYPOTHETICAL |
| Supercritical, fast catch | \(m=1.3\) | by generation \(G=3\), \(\tau\) independent of the tree | \(6.19=(m^{4}-1)/(m-1)\) | 4 TE | 20.7 TE | 4.46 | 0.47 | HYPOTHETICAL, conditional on detection by \(G=3\) |
| Supercritical, slow catch | \(m=1.3\) | by generation \(G=8\), \(\tau\) independent of the tree | \(32.0\) | 6 TE | 186 TE | 32.0 | 0.18 | HYPOTHETICAL, conditional on detection by \(G=8\) |
| Growth outruns detection | \(\alpha\ge h\), or \(m\ge 1\) and \(P(\tau=\infty)>0\) | too slow | unfolded mean \(\infty\) | any positive | no finite cap claimed | — | — | HYPOTHETICAL; no finite cap on the unfolded count is claimed (§10) |
| False public claim in the tree | any | any | — | — | — | — | — | breach, outside \(J\); no finite cap is claimed (`process/PROCESS.md:26, 42`) |

Reading the table: a modest subcritical case (\(m=0.8\), four expected later nodes, 4 TE each) already makes downstream cost 16 TE against an assumed immediate 6 TE, and, under Proposition 10, it cuts the selected re-check interval by about half. The last two rows are not numbers; they are the cases in which no finite cap is claimed. The finite branching rows all assume slow spread or a timely, independent detection; on an unbounded horizon they are not supplied by the summary-only design itself (§2). In a finite window with capped per-node cost and no breach, the cost is finite even under summary-only.

**Human verification, also illustration only.** All of \(N_{\mathrm{use}}\), \(v\), and \(\pi_v\) are **assumed**. No observed verification rate is claimed. Immediate miss cost in the comparison line is the same assumed 6 TE per miss.

| Policy | \(N_{\mathrm{use}}\) | \(\pi_v\) | \(v\) | \(V=N_{\mathrm{use}}\pi_v v\) | Label |
|---|---|---|---|---|---|
| Summary-only, checks most answers | 200 | 0.8 | 1 TE | 160 TE | HYPOTHETICAL |
| Summary-only, checks half, cheaper looks | 200 | 0.5 | 0.5 TE | 50 TE | HYPOTHETICAL |
| Verifiable lookup, small audit rate | 200 | 0.05 | 1 TE | 10 TE | HYPOTHETICAL; \(\pi_{\mathrm{audit}}=0.05\) is assumed |
| Gap, first row minus audit row | 200 | \(0.8-0.05\) | 1 TE | 150 TE | HYPOTHETICAL |

Against seven assumed misses at 6 TE immediate each (42 TE, no downstream), the first-row verification gap of 150 TE is already larger. That comparison is only as good as the assumed rates; it is the arithmetic of Proposition 11, not a measurement.

A compact formula line (subcritical, or stopped at a generation \(G\) with \(\tau\) independent of the tree and \(m\neq 1\)):

$$\mathbb{E}[N]=\frac{1}{1-m}\ (m<1);\quad \mathbb{E}[N\mid\tau=G]=\frac{m^{G+1}-1}{m-1};\quad C_\downarrow=\sum_{v\neq v_0}(u_v+o_v);\quad V=N_{\mathrm{use}}\pi_v v;\quad w_{\mathrm{eff}}=w+\rho\quad\text{(Prop.\ 10)};\quad T^*=\sqrt{6k/(w_{\mathrm{eff}}\sigma^2)}\quad\text{(same assumptions)}.$$

## 14. What would close the bounds

Measure, for a run of theory-bearing answers: whether a source check was done; whether a miss was later caught, and at what time \(\tau\); the tree or DAG of work that depended on it; unwind cost and, if claimed, a cap on opportunity cost; and whether any public statement was issued before correction. Then \(p_{\mathrm{miss}}\), \(m\), \(\tau\), \(c_{\max}\), \(\rho\), \(\pi_v\), and \(v\) can become measurements, as `applications/GROK_BOT_MEMORY_2026-11-23.md:78` already requires for the other parameters. The inequalities of §6–§10 do not wait on that measurement; only the numerical width does. Measuring those quantities would still not give the summary-only design a cap by construction; it would only test whether spread in fact stayed slow, and whether the human verification rate in fact fell.
