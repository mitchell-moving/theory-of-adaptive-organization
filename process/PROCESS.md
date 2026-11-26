# PROCESS: research-process vocabulary and rules from the cost of judgment

*Tuesday 24 November 2026 (America/New_York). Live maintained process rulebook (`tools/check_consistency.py`). It replaces an older wording rule that described misses with a word that §2 now bans. Dated records such as `reviews/lock_2026-11-18/PROCESS.md` are not edited.*

> **The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.** (`CORE.md:7`)

## 1. Derivation from the cost of judgment

Apply the theory's own cost to our research process (`CORE.md:5, 25-27, 64-66`):

$$J = \dot Q_M + w\,\mathbb{E}[\ell] \qquad\text{subject to}\qquad P(\mathrm{ruin})\le\varepsilon,$$

where $\dot Q_M \ge kT\,\dot I_M$ (`CORE.md:19-21, 70`; Horowitz and Esposito 2014) bounds the bath heat of **net** learning $\dot I_M$, $w$ prices expected error $\mathbb{E}[\ell]$ (`CORE.md:29, 41`), active memory holding ($\kappa I_{\mathrm{mem}}$), read/review cost ($A$), and link/coordination cost ($L$) stay as separate summands outside the physical heat floor (`CORE.md:33-44`), and the ruin cap $P(\mathrm{ruin})\le\varepsilon$ sits outside the sum as a hard admissibility constraint (`CORE.md:27, 44, 66, 112`).

Checking what follows from $J$ versus what is a sharpened correction or a process choice:

1. **Vocabulary (`prediction` → `outcome` → `miss` / `hit` → `update`).** *Follows from the act-before-arrival structure (`CORE.md:5, 11`); the exact word `'miss'` is a vocabulary choice.* A memory must commit before its world arrives (`CORE.md:5`). Locking a **prediction** (with a band, interval, or stated odds where feasible) before seeing the **outcome** is what gives a result predictive content. The signed gap between outcome and locked prediction is a **miss**—the signed error signal $\ell$ that tells us magnitude and direction for the **update**. Calling an unexpected outcome a `'kill'` treats error as an ending instead of a learning signal; calling it a `'puzzle'` hides its sign and size. (Formal gate statuses in `measurement/FRAMEWORK.md` §2.3 and `measurement/CLAIM_MAP_v2.md`—`PROXY-FAIL`, `SIM-FAIL`, `NOT A TEST`, `INCONCLUSIVE`, `FIELD-FAIL`—remain unchanged as gate classifications.)

2. **Recording cost and write-up depth.** *Depth scaling follows from `CORE.md:54, 91`; logging every miss, even tiny ones, is an anti-bias process rule.* Two refinements to a naive "heat of remembering" reading:
   - Passive disk storage has near-zero ongoing heat once written (`CORE.md:78`); the real research costs are updating ($\dot I_M$, `CORE.md:70`), holding active working context ($\kappa I_{\mathrm{mem}}$), and paying human/agent read and review costs ($A+L$, `CORE.md:33-44`).
   - Pure unconstrained optimization stays blind below the threshold $x = wv/(kTa) = 1$ (`CORE.md:91, 96`). Skipping small misses, however, creates silent selection bias and destroys the repetition signal needed in item 3.
   - **Rule:** record *every* miss (and hit) with one minimal fixed-schema line (`prediction_id`, `outcome`, signed `miss`, `location`), and scale diagnosis and write-up depth with $\text{stake}\times\text{information}$ (`CORE.md:54`). Never skip a miss; never bloat a low-stake one.

3. **Deliberate updates scaled to miss size, repetition, and stake.** *Follows from noise filtering (`CORE.md:76, 82`), fixed update cost (`CORE.md:100`), and net learning (`CORE.md:70`).* Under noisy observations, chasing a single small miss overfits noise and raises future $w\,\mathbb{E}[\ell]$; under lumpy update/review cost $k$, small deviations sit inside an inaction band (`CORE.md:100`, $T^*=\sqrt{6k/(w\sigma^2)}$) and do not justify a rewrite; and by $\dot Q_M \ge kT\,\dot I_M$ (`CORE.md:70`), genuine net learning has a positive cost floor while back-and-forth oscillation (updating then reverting) produces zero net $\dot I_M$ for wasted unsigned traffic (`CORE.md:70`). Repeated misses in the same direction average down noise and cross the band, so update size scales with miss magnitude, repetition, and stake $w$ (`CORE.md:54`).

4. **Ruin cap: miss versus breach.** *Follows directly from $P(\mathrm{ruin})\le\varepsilon$ sitting outside $J$ (`CORE.md:27, 44, 66, 112`).* A **miss** is an admissible error inside locked rules—paid as $w\ell$ on that prediction and learned from. A **breach**—patching a prediction post hoc, editing a locked preregistration, fabricating or cherry-picking data, leaking private data, or making a false public claim—violates the hard admissibility constraint (`CORE.md:112`). Breaches are prevented by structural rules (hash locks, branch protection, independent review, privacy boundaries), never traded off against speed or convenience.

5. **Hits carry information only in proportion to risk.** *Follows from Shannon surprise ($-\ln p$) and `MV10` (`measurement/FRAMEWORK.md:87`).* A sure-thing hit ($p\to 1$, such as a by-construction check labeled `NOT EVIDENCE`) yields $-\ln p \to 0$ bits and wastes read/review cost $A+L$ for zero learning. A hit carries information only when the locked prediction excludes a named rival (`CORE.md:138`, `MV8`, `MV10`). Log hits on the same minimal ledger so base rates stay visible, and state odds, intervals, or rival false-positive bounds in preregs where feasible (qualified by *where feasible*, because objective priors are not always well-defined for novel theoretical claims).

6. **Locate the miss (`model`, `measurement/code`, or `process`).** *Follows from the $T\wedge M\wedge A$ conjunction (`measurement/FRAMEWORK.md:26-31`) and cost nesting (`CORE.md:48`, CT34), bounded by the anti-rescue rule (`measurement/FRAMEWORK.md:89`).* A miss can sit in the **model** (in-model math or Part-2 empirical prediction), **measurement/code** (proxy invalidity or code bug), or **process** (our own execution and reporting loop—for example, stale hand-kept summaries, answering from memory instead of files, or mislabeling a self-review as independent). Process misses are logged with the exact same schema. **Guardrail:** for a locked scientific test, attributing a miss to `measurement/code` or `process` is admissible only when a pre-declared validity gate (`MV1`–`MV8`) or reproducible bug actually fired (`measurement/FRAMEWORK.md:89`), never as a post-hoc rescue.

7. **Look cadence timed to stakes and drift.** *Follows from the refresh-vs-drift trade-off (`CORE.md:96, 100`, CT11 / layer lifetime $T^*=\sqrt{6k/(w\sigma^2)}$), extended by T68 (`theory/CLOCK_TERM_2026-11-23.md:11-14`).* Optimal look rate scales with drift and stakes rather than running on a fixed wall-clock schedule: quiet periods cost near zero when left unpolled (`CORE.md:78`), whereas high drift or high stakes trigger a fresh look. When looks are expensive ($c>c^*$ fixed, or $>4\kappa/\lambda$ nats random), T68 (`theory/CLOCK_TERM_2026-11-23.md:11-14`) adds an internal clock/model carrying predictable change between drift- and stake-triggered looks (note that T68's onset $c^*$ is independent of $w$, while look rate $f^*$ scales with $w$). In repository workflow, facts that drift at every merge are read live (`tools/brief.py`) rather than refreshed, and the checks run at stake-triggered points: before a PR is marked ready and before a summary goes out (§4).

## 2. Vocabulary and wording rules

| Rule | Standard | Disallowed in new / maintained text |
|---|---|---|
| Hypothesis sentence | Byte-identical: `The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.` | Paraphrasing or dropping `(hypothesis)` |
| Theory / `'law'` | Call GTAO a **theory**; use `'law'` only inside the labeled hypothesis sentence or prior-art / physics names | Never call GTAO a `'law'` or a `'theory of everything'` |
| Cost / `'solved'` | Say **cost** (not `'bill'`); never claim GTAO or an open problem is `'solved'` (negations such as `'not solved'` are fine) | `'bill'` for cost; `'solved'` for open problems |
| Errors & outcomes | Call a prediction error a **miss** (with signed size, location, and update); log hits too | `'puzzle'`, `'kill'`, `'failure'` as a generic outcome label, or an unlabeled bare `'verdict'` |
| Constraint breaches | Call rule violations (editing locked preregs, post-hoc patching, leaks, fabricated data) **breaches** | Treating breaches as ordinary learnable misses |

Meanings of the scientific terms (memory, record, model, layer, level, nesting, scale, fractal, swarm) are fixed in [`process/VOCABULARY.md`](VOCABULARY.md). Historical files, `THEORY.md`, `CORE.md`, past memos, and locked preregs keep their existing text and are not rewritten. Formal test-gate statuses (`PROXY-FAIL`, `SIM-FAIL`, `NOT A TEST`, `INCONCLUSIVE`, `FIELD-FAIL`, `FIELD-PASS`) stay intact in `measurement/FRAMEWORK.md` §2.3 and `measurement/CLAIM_MAP_v2.md`.

## 3. Minimal miss / hit record and template

Every new test write-up, `DEVIATIONS.md`, or process-miss log records each prediction outcome using the eight fields in [`process/MISS_LOG_TEMPLATE.md`](MISS_LOG_TEMPLATE.md): `prediction_id`, `locked_prediction` (value/band and odds where feasible), `outcome`, `miss` (signed size and direction, or `HIT` with information/rival margin), `location` (`model` \| `measurement/code` \| `process`), `stake_x_info` (`low` \| `medium` \| `high`, governing depth), `update` (what changed, or `none yet`), and `breach_check`.

## 4. One source per fact

**Rule (25 November 2026), replacing the 24 November refresh rule:** each fact has one hand-kept source, and every other copy is deleted ([design memo](https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/a0508fd264fd840b84e60a136a83ef4f17b1fde2/history/2026-11-25_DRIFT_MEMO.md)). The visible repo is the current theory; git holds history.
- Facts that change at every merge are never committed: the `main` SHA, the open-PR list, PR heads and review state come live from `python3 tools/brief.py`.
- Claim statuses live in the `measurement/CLAIM_MAP_v2.md` headline ledger. Other pages link to it and carry no copy of it.
- The direction, the ranked work, and the "Waiting on Chad" list live in `README.md`. Versions live in the `THEORY.md` title and the latest CLAIM_MAP note. The Lean total lives in `formal/lean/AUDIT.json`.
- A path that a dated record names but that is no longer in the tree resolves at its permalink: `https://github.com/Chad-Mitchell/theory-of-adaptive-organization/blob/1eed183f3888e8e3eead5956bbf1e8cb4233510a/<path>`.

**Checks (all must pass before a PR is marked ready):** `tools/check_fresh.py`, `tools/check_pending.py`, `tools/check_consistency.py`, `tools/verify_locks.py`, `tools/banned_words.py`, `tools/check_claims.py`, and `python3 -m pytest -q`.
- `check_fresh.py` fails on any maintained page that hand-keeps a SHA of a recent `main` commit or the head of an open PR (in any wording), an open-PR list, a hand-typed PR head, a version string, or a Lean declaration total. It also fails on a root `.md` file outside its allow-list and on a `STATUS.md` or `OPEN_WORK.md` in any folder. Dated entries sit inside `<!-- history:begin -->` … `<!-- history:end -->` and are skipped. Without network it prints `RESULT: PARTIAL`.
- `check_claims.py` fails on a claims view, a second copy of the direction line, a ranking outside `README.md`, a `README.md` ranked-gaps or Waiting-on-Chad row ID used as a table row or ordered-list item on another page, a summary that judges the theory as a whole, or a claim without its exact ledger status.
- `banned_words.py` runs on its own (`python3 tools/banned_words.py`) and inside `check_consistency.py`.
- Run `python3 tools/check_pending.py --pr N --body-file BODY.md`. It fails when that PR's own `README.md` row is still "In flight", when that PR has a passing review older than 24 hours that no longer covers its head, or when its body breaks the summary rule. Other PRs' findings only warn. A run that could not fetch or reach GitHub prints `RESULT: PARTIAL`, never PASS.

**Parked work and parked PRs (25 November 2026; moved here from the retired parked-PR page).**
- A row tagged `data` in the `README.md` ranked table stays `parked` until its restart condition is met. Each parked row names a restart condition and a decider. DATA-ONE and RS-SCREEN are parked. Restart: Chad's sign-off; decider: Chad.
- A PR held on purpose is listed in the table below, as `upstream#N` or `fork#N`. A listed PR is exempt from the check that flags a PR reviewed but unmerged for more than 24 hours (`tools/check_pending.py` reads this table). Add a row only when someone has decided to hold the PR. Each row needs a reason, the date (YYYY-MM-DD) and who decided. Remove the row when the PR moves.

| PR | reason | date | decided by |
|---|---|---|---|


**Rule (24 November 2026):** every process miss gets an entry in [`process/FAILURES.md`](FAILURES.md): date, locked prediction, outcome, miss with size and cost, cause, location, `stake_x_info`, the update scaled to size, repetition and stake, and `breach_check` (the eight fields of `MISS_LOG_TEMPLATE.md`, plus date and cause).

**Rule (24 November 2026):** no commit message or PR body uses a GitHub closing keyword (`close`, `fix` or `resolve`, in any tense) followed by a PR or issue number unless that number is the PR itself or the text says `closes-ok: #N` and why. A merge closes whatever such a keyword names. Before opening or updating a PR run `python3 tools/check_pending.py --closing-keywords origin/main..HEAD --pr N --body-file BODY.md`; the online run of `check_pending.py --pr N` checks that PR the same way and only warns about other open PRs. Write "see #N" or "update the state of #N" instead.
