# SIM-1 / T28: simulation is already inside \(J\)

*21 November 2026 (America/New_York). Package `core/sim1_2026-11-21/`. This package does not change `CORE.md` or the hypothesis sentence in [`OPEN_WORK.md`](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/OPEN_WORK.md) (SIM-1). In-model. Field-untested.*

## Already in the repository (not new)

- The master equation already prices model memory and compute: \(J(\mathcal D)=\kappa I_{\mathrm{mem}}+hK+w\mathbb E[\ell_{\mathcal D}]+A(\mathcal D)+L(\mathcal D)\) subject to \(P(\mathrm{ruin})\le\varepsilon\) (`CORE.md` §1).
- CT4 (the first bit must pay): a model is carried iff memory is cheaper than the first increment of predictive value; Gaussian form \(I^\star=\tfrac12\log_2(2\ln 2\cdot a^2\cdot\mathrm{Var}/\kappa)\).
- CT10 is the in-repo ancestor of the official P1 and P3 statements: with \(J(f;w)=c\cdot f+w\cdot A(\lambda/f)\), the minimizing check frequency is nondecreasing in stakes \(w\), by the same decreasing-differences / Topkis argument (THEORY CT10 / G4). CT12's read-rate rule and the single-instrument clause of CT20(ii) are the same shape at a fixed instrument. CT33 (with CT20) is the in-repo ancestor of the spend-and-error diagnostic: with the ruin cap slack, total judgment spend is nondecreasing and expected error is nonincreasing in stakes \(w\). A single instrument (layer count, read rate, or rollout count) is monotone only when the other instruments are held fixed; substitutes can move against the stake (the referee's reads-for-layers counterexample, B.9).
- CT22: when the Lundberg cap binds, the feasible set can shrink with \(w\) and those monotone statements can fail.
- T27 / `core/bridge_2026-11-21/`: under \(m=-\alpha J\), weak-mutation Moran has stationary law \(\pi\propto e^{-\beta J}\), \(\beta=\alpha(N-1)\). Official T27 result: P1 and P2 passed, P3 failed; the lesson for later preregs is to compute every gate's exact/analytic value on published pilots *before* locking, and to hash-lock the runner and the library at lock time.

What is new here is a *minimal mechanism* for rehearsal, already booked in those existing terms, and a preregistered in-model test of the comparative statics of the rollout count \(m^\star\). The qualitative idea that a system should simulate more when stakes or ruin risk are high and an internal model is cheap, and simulate zero when stakes are near the model's cost, is not a discovery of this package.

## Prior art (not a novelty claim)

The same qualitative arbitration — a costly model-based (goal-directed) controller competing with a cheap model-free (habitual) one, with more use of the costly model when uncertainty or the value of information is high — is already in the reinforcement-learning literature. Verified on the Crossref API, 21 November 2026:

- Daw, Niv & Dayan 2005, “Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control,” *Nature Neuroscience* **8**, 1704–1711, doi `10.1038/nn1560` (issued 6 November 2005).
- Keramati, Dezfouli & Piray 2011, “Speed/Accuracy Trade-Off between the Habitual and the Goal-Directed Processes,” *PLoS Computational Biology* **7**, e1002055, doi `10.1371/journal.pcbi.1002055` (issued 26 May 2011).

This package does not claim that qualitative prediction as original. Its in-repo ancestors are CT10 (and CT12 / CT20(ii)) for the official monotone statements on \(m^\star\) at fixed \(K\), and CT33 for the total-spend and error diagnostic. What is tested is a booking of rehearsal inside the existing terms of \(J\), and the comparative statics of that booking, in-model only.

## Booking (no new term)

A design chooses a layer count \(K\in\{0,\ldots,K_{\max}\}\) and a number of simulation rollouts per decision \(m\in\{0,\ldots,m_{\max}\}\).

$$
J(K,m)=\kappa I(m)+hK+cm+(w+\lambda\chi)\,E(K,m).
$$

- \(I(m)=I_0\) if \(m\ge 1\), else \(0\): the internal model is held only if the system actually rehearses. This is the existing \(\kappa I_{\mathrm{mem}}\) term.
- \(hK\): existing layer upkeep.
- \(cm\): compute per rollout, booked in \(A(\mathcal D)\) (the cost of a read — here, a read of the model).
- \(w E(K,m)\): existing stake times expected *real-trial* loss.
- \(\lambda\chi E(K,m)\): ruin *exposure*, booked in \(L\), proportional to residual error. This is **not** the Lundberg cap. The cap is kept slack. When it binds, CT33 can fail, and this package does not claim the monotone statements in that regime.

Real-trial error, with model fidelity \(\varphi\in(0,1]\):

$$
E(K,m)=e_0(K)\Bigl(1-\varphi+\frac{\varphi}{1+\varphi m}\Bigr),\qquad e_0(K)=\frac{e_{\mathrm{base}}}{1+\gamma K}.
$$

Simulation drives error from \(e_0(K)\) toward the fidelity floor \(e_0(K)(1-\varphi)\), with diminishing returns \(1/(1+\varphi m)\). Layers shrink the pre-simulation residual; they do not change \(\varphi\). So \(K\) and \(m\) are substitutes: the continuous interior \(m^\star\) falls as \(e_0(K)\) falls. Official monotone gates for \(m^\star\) are therefore stated **at fixed \(K\)**, in the same spirit as CT20 (ii). Joint \((K^\star,m^\star)\) can, in principle, drop in \(m\) when a new layer is added; that is reported as a diagnostic, not a gate. CT33 still applies to total spend and error when the cap is slack.

## Analytic \(m^\star\) (continuous, \(m>0\), model already paid)

Write \(W=w+\lambda\chi\). Differentiating gives \(\partial E/\partial m=-e_0\varphi^2/(1+\varphi m)^2\), so the first-order condition \(c+W\,\partial E/\partial m=0\) is

$$
m_{\mathrm{cont}}(K)=\Bigl[\sqrt{\frac{W e_0(K)}{c}}-\frac{1}{\varphi}\Bigr]_+.
$$

The fixed cost \(\kappa I_0\) is paid for every \(m\ge 1\) and does not shift this interior FOC. It does shift the *extensive* margin: \(m^\star=0\) whenever \(J(0)\le\min_{m\ge 1}J(m)\). The first-order threshold, ignoring that fixed cost, is \(W=c/(e_0\varphi^2)\); the true discrete threshold \(W_{\mathrm{th}}(K)=\inf\{w:m_K^\star(w)\ge 1\}\) is weakly larger and is computed by bisection on the discrete grid (exact for the official gates, up to the bisection tolerance).

Comparative statics, **at fixed \(K\)**, ruin cap slack (exposure additive):

- \(m^\star\) is nondecreasing in \(w\) and in \(\lambda\) (Topkis: \(-J\) has increasing differences in \((m,w)\) and in \((m,\lambda)\), because \(E\) is nonincreasing in \(m\)).
- \(m^\star=0\) below a stakes threshold (the first model and the first rollout must pay; CT4-style).
- \(m^\star\) is nonincreasing in \(c\) (Topkis in \((m,-c)\)).

These three are **theorems** on the discrete grid, with the least argmin used as the official selection (the least and greatest selections are both monotone). They are not theorems about joint \(m^\star(w)\) once \(K\) is also chosen, and they are not theorems when the Lundberg cap binds.

## Evolution (numerical)

Under the same fitness map as T27, \(m=-\alpha J\), haploid Moran, weak mutation, equal edge clocks, the stationary law is \(\pi\propto e^{-\beta J}\) with \(\beta=\alpha(N-1)\). The mutation graph is local in \(K\) and in \(m\), plus adopt/drop edges \((K,0)\leftrightarrow(K,m)\) for every \(m\ge 1\): \(\kappa I_0\) is a fixed cost, so \(J(1)\) can exceed \(J(0)\) even when a larger \(m\) beats \(J(0)\), and a \(\pm 1\) walk in \(m\) would have to cross that valley. Adopt/drop is one mutation (start rehearsing at a useful length). The official P4 run *simulates* that process; it does not sample \(\pi\) directly. Exact Boltzmann weights are a validity screen and a diagnostic, never the official pass bar (T27 lesson).

P4 is a finite-sample numerical test that high-\(\beta\) occupation finds \(m^\star\) within a locked tolerance, not a new theorem.

## Official test

Preregistered as T28 in `PREREG.md`, locked (including this library and `run_sim1.py`) in `LOCK.txt` before any official world was evaluated. Official numbers are in `RESULTS.md`.
