# Preregistration v4a: scoring fixes for A-T1‴ (appended to PREREG_4, before any run)

*Wednesday 25 November 2026 (America/New_York). Branch `forge-two-route-prereg`. Append-only note to `PREREG_4.md` (lock `b9a2710`, sha256 `b16b3c2b…0f14914c`, untouched). `PREREG.md`, `PREREG_2.md` and `PREREG_3.md` are also untouched. The v4 independent gate read (`gate_read_287_v4.md`) is a **GATE PASS** on G1–G5 for A-T1‴ (written A-T1″′ in `PREREG_4.md`) and for B-T2′ as carried, with 0 blocking and 6 non-blocking items. It asked that the scoring items be fixed in an appended note before the §6 comparison is scored. This note does that. It changes no model, no grid, no tolerance and no hit band. It changes only the branch odds, the score of the no-settling and mixed branches, the size reported for a mixed result, and one ambiguous clause. Locked in its own commit with `PREREG_4a.sha256`, before any A-T1‴ or B-T2′ script exists. `THEORY.md`, `CORE.md` and the locked blobs are not edited.*

**The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.**

(Byte for byte from `CORE.md:7`.)

## 1. No settling (gate read v4 row 13)

- **Definition, unchanged:** at a given \(w_x\), the alternating best-reply search of `PREREG_2.md` §4 does not stop in 200 undamped rounds and then does not stop in 200 more rounds with damping 0.5.
- **Score.** "No settling" is **resolved (1)** under §6 only if it occurs at **all three** \(w_x\in\{0.5,1,2\}\), each time after the damped phase. No settling at one or two \(w_x\), with the others settled, is a `sensitivity-dependent` open miss and scores **0**, the same as any other mixed result.
- **Route.** The credit, if any, is Route A's one TEST point (A-T1‴ resolved). It is **not** a status change of the CX2 scope row, which is Route B's (`PREREG_2.md:101`), and it gives no scope-row points to either route.
- **Scope of the claim.** The `PREREG_4.md` G5 text "a W2 counterexample to settling for CX2" is withdrawn. No settling here means only that **alternating best-reply iteration did not converge** on W2 at the stated rounds and damping. It says nothing about whether selection dynamics settle when a Nash point exists. It is recorded as a solver result in the A-T1‴ ledger line, not as a CX2 counterexample.

## 2. Hit odds and the full branch split (gate read v4 rows 9, 11)

Option taken: **lower the hit odds**, with the reason, rather than a linearized Nash estimate. A one-shot quadratic best-reply solve at the joint minimum would give a near-value of \(G\) before the run; locking that as the odds would put most of the test's information into a paper number that the run then only confirms. The odds below rest on the paper surpluses the gate reader reproduced and nothing more.

**Reason.** At the joint minimum at each \(w_x\in\{0.5,1,2\}\) (`PREREG_4.md` §1.2, reproduced in gate read v4 rows 6–8):

- the world's 1D own-gradient step gives a fractional surplus of 0.038 / 0.041 / 0.042;
- the memory's 1D own-gradient step in \(c\) gives 0.021 / 0.014 / 0.006 (gate read v4 row 9);
- the naive sum is 0.059 / 0.055 / 0.048, below 0.10 at all three \(w_x\);
- the memory's \(\gamma\)-gradient (0.27 / 0.19 / 0.10) is left out, and the cross term has no definite sign, because \(\Delta g>0\) and \(\Delta c<0\) push \(gc\) in opposite directions.

A HIT needs the Nash fixed point to roughly double the one-step surplus **at all three** \(w_x\). That is possible when both parties move, so the hit odds are not about 0. It is less likely than `PREREG_4.md` §1.2 stated. The "0.04–0.15 regime" upper end in `PREREG_4.md` §1.2 is withdrawn as not derived.

**Branch split (replaces `PREREG_4.md` §1.2 item 2's list; sums to 1.00):**

| Branch | Definition | Odds | §6 |
|---|---|---|---|
| HIT | \(G\ge0.10\) at all three \(w_x\), each settled and interior | **0.20** | 1 if resolved (§4) |
| Clean MISS | \(G<0.10\) at all three \(w_x\), each settled and interior | **0.50** | 1 if resolved (§4) |
| `sensitivity-dependent` open miss | Some \(w_x\) give \(G\ge0.10\) and others \(G<0.10\); or no settling at one or two \(w_x\) | **0.25** | 0 |
| No settling at all three | §1 above | **0.04** | 1 |
| `boundary-hit` open miss | Any joint minimum or Nash point at any \(w_x\) on a box edge or on \(gc=0.999\) | **0.01** | 0 |

Total miss odds (every branch except HIT): **0.80**.

## 3. Size reported for a mixed result (gate read v4 row 12)

For a `sensitivity-dependent` result the signed size is the **range** \([\min_{w_x}G(w_x)-0.10,\ \max_{w_x}G(w_x)-0.10]\) over the settled \(w_x\), with all three \(G(w_x)\) (or "no settling") reported. The single number \(G(1)-0.10\) in `PREREG_4.md` §1.2 is withdrawn. For a clean MISS the signed size stays \(\max_{w_x}G(w_x)-0.10\). For a HIT, report \(\min_{w_x}G(w_x)-0.10\geq0\) and all three values.

## 4. "Resolved" for A-T1‴ (gate read v4 row 14; replaces the clause at `PREREG_4.md:78`)

A HIT or a clean MISS is **resolved (1)** iff, **at every one of the three** \(w_x\in\{0.5,1,2\}\), both (i) \(|G(w_x)-0|>0.02\) and (ii) the half-tolerance check passes (\(G\) moves by at most 0.01). If either fails at any \(w_x\), the outcome keeps its branch label but scores **0** under §6. The alternative "or at \(w_x=1\)" reading is withdrawn. `PREREG_4.md` §2.1's sentence that \(G(1)\) is "the reference-point value used for the §6 resolution check" is replaced by this rule; \(G(1)\) remains the reference value reported first.

## 5. Memory-reply bracket (gate read v4 NB5)

The paper bracket for an interior memory reply covers \(g\in[0.5,1.1]\) only. It is not a proof for every Nash path. The `boundary-hit` branch (§2, odds 0.01) covers any path that leaves it and lands on the guard.

## 6. Unchanged

Everything else in `PREREG_4.md` (model, shared \(w_x\,\mathbb E[x^2]\) modeling choice, \(w_x\) grid, boxes, grids, tolerances, boundary rule, hit band \(G\ge0.10\), rival, gap, resolution), `PREREG_3.md` §2.2 (B-T2′ resolved iff \(|f-0.5|>4\,\mathrm{SE}\); no pre-banked PAPER points) and `PREREG_2.md` §4–§5 (B-T2′ procedure, order and stop rule) stands. Order: (1) A-T1‴ at \(w_x=0.5,1,2\); (2) B-T2′ with the B-C3 code gate; (3) the unscored deliverables.
