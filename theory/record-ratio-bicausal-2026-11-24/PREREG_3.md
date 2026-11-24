# T79 preregistration 3: reversibility and the same equilibria

*Tuesday 24 November 2026 (UTC). Written and committed after `PREREG.md` and before `bicausal_checks.py`, before any scored grid, and before any number from that grid. `PREREG.md` is not edited. Its sha256 is `b78addd0edf765e9fa76c1f0d82cfdc88a30d9105b8bb0ddd5a4e6410a37e39e`. This file is locked by sha256 in `PREREG_3.sha256`, same commit. A later change is a deviation in `RUN_LOG.md`. This file is not edited after this commit.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every reading of an equilibrium is a model implication, in-model.

**Hypothesis from Chad and Ace, labeled as such.** The ratio measures how reversible the boundary is. The return is the backward half of the act. A fully time-symmetric boundary returns everything, \(q=1\). A fully one-way boundary with real destruction returns nothing, \(q=0\).

P5 is a secondary test on the equilibria of `PREREG.md`. It does not add a strategy, a price, a delay, or a cell to that model.

## Why this approach

The parent's return is already the backward edge of the child's act. Entropy production is the path-space divergence between that edge and its reverse. If the ratio is reversibility, it is a function of that divergence, and the delay enters only by changing the divergence.

## Can it fail

Can it fail: yes. The persistence reset is not the reverse of the keep rate, so the steady divergence need not hit 0, and the ratio need not fall as that divergence rises.

Cheapest way to fail: the smallest steady divergence on the headline Nash pairs stays away from 0, or two pairs with the same divergence carry different ratios.

## 1. The mirror run, read before this lock

The earlier mirror run built the conjugate in by the start. On `ace-probe-memos-2026-11-23` at `e3e0e701`:

- `theory/probes-2026-11-23/reviews/MIRROR_REVIEW.md:31`: the conjugate is put in by the real Hamiltonian. A real Hamiltonian commutes with complex conjugation, so the antilinear time reversal is a symmetry of the reference by assumption.
- The same review, `:36`: the premises are a real, time-symmetric reference, symmetric looks, and the turn \(\tau=it\).
- The same review, `:60`: the step works because the setup started real and time-symmetric, so the conjugate was already built in.
- `theory/probes-2026-11-23/MIRROR_MEMO.md:46`: the conjugate is not derived from the cost. It is relocated into those premises. `:168` says the same in the revised paragraph. The reviewer edit at `:13` records the circularity.

This lock does not start from a time-symmetric reference, does not set a reverse rate equal to a forward rate, and does not start the path measure at a reversible stationary distribution. The equilibria are the Nash pairs of `PREREG.md`. The starts below are asymmetric and fixed.

If a later match to \(q=1\) requires replacing those starts by the stationary distribution of a chain whose reverse rates were copied from the forward rates, the match is the mirror's circularity. It does not count.

If the equilibrium shares a cause with that mirror without the circularity, it reproduces \(q=1\) at vanishing steady entropy production from the asymmetric starts. That is the \(\sigma=0\) clause of P5. It is not a second target and it is not tuned.

## 2. Prior art, Crossref on 24 November 2026

Checked on the Crossref API this session, HTTP 200, before this commit. No number is taken from these papers.

- Jarzynski, C. Nonequilibrium equality for free energy differences. Physical Review Letters 78:2690–2693 (1997). doi `10.1103/PhysRevLett.78.2690`. The equality relates a forward protocol to its reverse. It is the reason a reverse path is the object. It does not set \(q\).
- Crooks, G. E. Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. Physical Review E 60:2721–2726 (1999). doi `10.1103/PhysRevE.60.2721`. The log ratio of forward and reverse path probabilities is the entropy production along the path. That is the definition used below.
- Seifert, U. Stochastic thermodynamics, fluctuation theorems and molecular machines. Reports on Progress in Physics 75:126001 (2012). doi `10.1088/0034-4885/75/12/126001`. For a stationary Markov jump process the mean entropy production per unit time is \(\sum_{i\neq j}\pi_i k_{ij}\ln(k_{ij}/k_{ji})\). The steady rate below is that sum. No table from the review is copied.

## 3. Pricing of the path

No new price. The rates are the equilibrium record, in the units of `PREREG.md` §2.3.

States \(U\) (no record), \(K\) (kept), \(D\) (destroyed). At a Nash pair \((\theta^\star,\alpha^\star)\) with the accounting's \(\rho\), and with \(\varepsilon_0=10^{-6}\),

| edge | rate |
|---|---|
| \(U\to K\) | \(I(\theta^\star)+\varepsilon_0\) |
| \(K\to U\) | \(1\) |
| \(K\to D\) | \(P_D(\theta^\star)+\varepsilon_0\) |
| \(D\to K\) | \(\alpha^\star\rho\,(P_D(\theta^\star)+\varepsilon_0)+\varepsilon_0\) |
| \(D\to U\) | \(1\) |
| \(U\to D\) | \(\varepsilon_0\) |

The reset rates \(K\to U\) and \(D\to U\) are the child's persistence clock, already the unit of \(\tau\). They are not set equal to the keep rate or the destroy rate. \(\varepsilon_0\) is a floor so every reverse edge has a finite logarithm. It is not a symmetry and it is not fitted. A specification that set \(D\to K\) equal to \(K\to D\) would be the mirror's circularity. This table does not do that.

**Steady entropy production.** Let \(\pi\) be the unique stationary distribution of this chain (the chain is irreducible because \(\varepsilon_0>0\)). 

\[
\sigma=\sum_{i\neq j}\pi_i k_{ij}\ln\frac{k_{ij}}{k_{ji}}.
\]

This is the long-run path-space KL per unit time. It is the headline \(\sigma\).

**Path KL from asymmetric starts.** Discrete skeleton, step \(dt=0.05\), \(n=20\) steps, one persistence time. \(P_{ij}=dt\,k_{ij}\) for \(i\neq j\), and \(P_{ii}=1-dt\sum_{j\neq i}k_{ij}\). Outflow times \(dt\) stays below \(1\) on this menu because each rate is at most \(1+P_D+I+2\varepsilon_0<1.3\) and two edges leave a state. The expected path KL from a start \(p_0\), including the boundary term \(\mathbb{E}[\ln p_0(x_0)-\ln p_0(x_n)]\), is

\[
\sigma_{\mathrm{path}}(p_0)=\sum_{t=0}^{n-1}\sum_{i\neq j}p_t(i)\,P_{ij}\ln\frac{P_{ij}}{P_{ji}}+\big(H(p_n)-H(p_0)\big),
\]

where \(p_{t+1}=p_t P\) and \(H\) is the Shannon entropy in nats. The boundary term uses the start \(p_0\) as the reference density on both ends, which is the Seifert boundary for a protocol scored against a fixed reference. It is not the stationary distribution.

Locked starts, none of them uniform, seed `20261124` set and not drawn from:

| start | \((U,K,D)\) |
|---|---|
| S1 | \((0.80,\ 0.15,\ 0.05)\) |
| S2 | \((0.05,\ 0.20,\ 0.75)\) |
| S3 | \((0.50,\ 0.40,\ 0.10)\) |

## 4. What is scored

Every exhaustive Nash pair of the headline family in `PREREG.md` §2.5, both accountings, both tie rules, every locked \(\tau\), every \(w\in\{1,2,10\}\). The ratio coordinate is that pair's \(q_{\mathrm{hat}}\) from `PREREG.md` §2.6. A cell with an empty Nash set is omitted from the cloud and listed. Pairs that are not pinned are still points in the cloud: a wide set is represented by its midpoint, and the miss of uniqueness is already P1.

**Code gate G-rev.** Six equal off-diagonal rates, value \(1\), have \(|\sigma|<10^{-12}\). This checks the sum, not the equilibria.

## 5. Prediction P5

Across the headline Nash cloud of one accounting, \(q_{\mathrm{hat}}\) is a monotone function of \(\sigma\): it equals \(1\) at \(\sigma=0\), and it goes to \(0\) as \(\sigma\) grows. \(\tau\) enters only through \(\sigma\).

Tolerances, fixed: two divergences are the same when they differ by at most \(10^{-3}\). Two ratios differ when they differ by more than \(0.02\). A divergence at most \(0.05\) is the reached reversible point. The cloud is read separately for each accounting. A pass requires both.

*Fails if* any of the following holds. Report the pairs, both \(\sigma\), both \(q_{\mathrm{hat}}\), both \(\tau\), both \(w\), the tie rule, and the accounting.

1. **Same \(\sigma\), different \(q\).** Two pairs in one accounting with \(|\sigma_1-\sigma_2|\le 10^{-3}\) and \(|q_1-q_2|>0.02\).
2. **Not monotone.** In one accounting, sort the pairs by \(\sigma\). Some adjacent pair has \(\sigma_{i+1}>\sigma_i+10^{-3}\) and \(q_{i+1}>q_i+0.02\).
3. **Not \(1\) at \(0\).** The pair with the smallest \(\sigma\) in that accounting has \(\sigma>0.05\), or \(|q_{\mathrm{hat}}-1|>0.02\).
4. **Does not go to \(0\).** The pair with the largest \(\sigma\) in that accounting has \(q_{\mathrm{hat}}>0.02\).
5. **Delay left over.** Two pairs in one accounting with different \(\tau\), \(|\sigma_1-\sigma_2|\le 10^{-3}\), and \(|q_1-q_2|>0.02\). This is clause 1 restricted to a delay change. It is reported even when clause 1 already fails, so the memo can see the delay.
6. **Start left over.** For a start S1, S2, or S3, the path KL orders the same pairs so that clause 2 fails, or the pair with the smallest path KL is a different \((\tau,w,\text{tie})\) cell from the pair with the smallest steady \(\sigma\).

An empty cloud fails clauses 3 and 4.

## 6. What a miss points to

A miss of clause 3 with a large smallest \(\sigma\) means every equilibrium of this cost is irreversible. The reversible boundary is not selected. The clue is the reset rate, which has no matching reverse in the keep rate.

A miss of clause 2 or 1 means the ratio is not the divergence. Some other coordinate of the same pair still moves \(q\).

A miss of clause 5 means the delay still shows once the divergence is held fixed.

A miss of clause 6 means the answer depended on which asymmetric start was used. That is the dependence this file exists to detect.

## 7. What this file will not say

It will not edit `PREREG.md`. It will not add a rate to make \(\sigma\) hit 0. It will not call a monotone plot a derivation of quantum mechanics. It will not treat the mirror's conjugate as a result of this cost.
