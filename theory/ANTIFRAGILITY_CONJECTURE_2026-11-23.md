# Gaining from disorder

*Monday 23 November 2026. Canonical statement of a named conjecture, and of what the cost already says about when a system gains from disorder. Draft wording. A self-check, not an independent review. No new computation. The hypothesis sentence is unchanged. `THEORY.md` and the master equation are not edited. This note's open-work row is T50.*

Labels: **PROVED** (proved inside the class named with it), **PROVED (in-model)** (the same, at a frozen point), **KNOWN** (published and credited, only for what that source states), **CONJECTURE** (a named bet, not a result), **OPEN** (not derived or not scored).

The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment.

## 1. The use

The cost of judgment predicts when a system gains from disorder and when it does not. That is a use of the same cost that yields layers, holographic memory, a sufficient boundary, and turnover under the ruin cap. It is not a separate principle.

Write the cost, find its minimum, and read off the design. In named classes the minimum already says when a spread or a rise in volatility lowers the cost, when it raises the cost, and when a popular recipe does not help. The ruin cap comes first. No gain counts that breaks it.

This page is the canonical home for that use and for the conjecture in §3. `CORE.md` §4 carries the same synthesis as part of the theory's reach. The pieces cited below are proved in their own notes; this page does not re-prove them.

## 2. What the cost already says

### Option route (PROVED (in-model), KNOWN, linear-Gaussian class, ruin slack)

Taleb and Douady 2013 (doi 10.1080/14697688.2013.800219) define antifragility as convexity of the payoff in a stressor. Applied to this cost: a concave cost gains from a spread of the stressor (`theory/ROBUSTNESS.md` §6, CT40).

In the linear-Gaussian class, with the ruin cap slack, the minimized cost \(J^*\) is concave in volatility, so a spread of volatility lowers expected cost if the system can redesign per regime (Jensen). In this class \(J^*\) is also nondecreasing: more volatility never lowers the best attainable cost. With one fixed design there is no such gain. That is the Oi–Hartman–Abel effect, read inside this cost (Oi 1961, doi 10.2307/1907687; Hartman 1972, doi 10.1016/0022-0531(72)90105-6; Abel 1984, doi 10.1016/0165-1889(84)90047-2). The option to redesign is worth buying only when redesign is faster than the regime and cheaper than the Jensen gain. The cost of redesign is not in \(J\) (**OPEN**). A binding ruin cap can break this concavity.

A naked option, premium 1 against \(\mathbb{E}[\max(X,0)]=\sqrt{\theta/(2\pi)}\), drops in level with no channel and no heat. The sign bet is a capped loss, and the financial name for that bet adds no comparison the cost does not already make.

### Learning route (PROVED for the level drop, open-loop probe class; convexity at the scored point is PROVED (in-model))

In a worked open-loop probe model — fixed observation noise, a probe price that is not proportional to the variance, and a loss that at fixed fraction depends on the variance only through that fraction — the probe price of a learned fraction falls as \(1/\theta\), and that fall is the derivative of the minimized sign cost (`theory/ACTING_MEMORY_2026-11-22.md`). In that same model \(J^*\) is strictly decreasing in \(\theta\) (Proposition AM-decrease), so a rise in the level of volatility lowers the minimized cost. \(J^*\) is not concave on any right half-line (AM-not-concave). At the scored point \(\theta=1\) it is convex (AM-convex-here, PROVED (in-model)), so a spread of volatility around that point raises the cost.

The world equation contains no action. The scored object is an open-loop intensity. This level drop is not evidence from closing the loop. The choice of \(\alpha=(4-\pi)/(6\pi)\) places a critical point at \(r^*=1/2\), \(\theta=1\); it is not the source of the \(1/\theta\) identity. Controls that make the probe price proportional to the variance, or that scale the observation noise with \(\theta\), remove the fall. A gap above the heat floor that grew with \(\theta\) could reverse the level drop; that case is **OPEN**. The result is in-model, not adopted into `THEORY.md`.

### Rebuild under the ruin cap (PROVED (in-model), T43)

Under the ruin cap, replacing identical units can lower the long-run cost: at rate 1, cost 15.473978 with ruin probability 0.020940, against the inadmissible zero at cost 16 (`theory/antifragility_checks/RESULTS.md`). The unconstrained grid minimum is inadmissible. The heterogeneous arm minimizes at no shock, cost 13. The open miss at this cap: heat is proportional to precision, and the admissible points keep the more precise units.

A failure time independent of the world adds nothing about the world. A failure that depends on the state cuts the variance, in the one Cox comparison that was scored (`theory/ACTING_LOOP_2026-11-22.md` §6, T46), and the part is then gone.

### Closed loop, scored so far (PROVED (in-model), linear-quadratic-Gaussian class)

Closing the loop, in the scored linear-quadratic-Gaussian model, shrinks the information stock \(\tfrac12\log(v/p)\) that memory must carry and does not shrink the learning-rate heat (`theory/ACTING_LOOP_2026-11-22.md`). At unit stake and \((a,\theta)=(1,1)\), with heat and probe charged, the loop is dearer than sensing at every fraction, and the minimum is the blind cost \(q\theta\). That function rises with volatility and its second derivative is 0, so a spread does not lower the cost the hypothesis minimizes at that scored point. At stake 4 the loop is slightly cheaper, by 0.033889928154 at the minimizing fraction. A fixed-intensity slice at stake 1 is concave, but that concavity belongs to a design the cost does not select. The spread of the minimizing closed loop was not scored.

### Barbell (not a general result)

The barbell is not a general result of this cost (`theory/DYNAMICS.md`; independently reviewed with PR #117). Where the cost-versus-ruin frontier is convex, mixing two extremes gains exactly zero. A discrete mix can shave a little (6.555 mean copies against 7 at \(\varepsilon=5\times 10^{-4}\)) only if the cap binds before the draw. A system that then drew 6 copies has ruin probability \(10^{-3}\), which exceeds \(\varepsilon\). The condition is ex-ante against ex-post binding. That is randomization, not a safe-plus-speculative barbell. An earlier scan's "population-frequency" wording is superseded.

## 3. The conjecture

**CONJECTURE.** Antifragility is not a separate principle. It falls out of minimizing the cost of judgment once a system closes the predict-act-correct loop.

This is a bet, not a result. The proved pieces in §2 do not jointly show that closing the loop is what produces a gain from disorder. The option route is a known convexity effect, read inside this cost, and needs the option to redesign. The learning-route level drop is open-loop, and in that class a spread raises the cost. In the scored closed-loop model, at unit stake, the minimizing cost rises with volatility.

The joining theorem that would tie both routes to acting on the world is **OPEN**. It is the synthesis already named as a conjecture in `theory/ACTING_LOOP_2026-11-22.md` §8, not a proof. If the conjecture holds, it would explain why systems that last look antifragile. That sentence is a consequence of the bet, not a measurement.

### Closed loop with payoff (follow-up, 23 November 2026)

`theory/ANTIFRAGILE_LOOP_2026-11-23.md` closes the loop with a payoff that depends on the action and the world (independently reviewed on PR #241). In that class the bet holds conditionally: with a payoff convex in the world's state for every action (an owned option), a memory family closed under the world's amplitude, and a slack ruin cap or bounded downside, the optimized value \(V^*=-J^*\) is nondecreasing and convex in amplitude, so the minimized cost is nonincreasing and concave in it (PROVED (in-model)). It does not hold for losses paid to stay correct (the level hurts), for convexity bought at prices that scale with volatility (neutral), for faster churn at fixed amplitude (the level hurts), or inside a window where the ruin cap binds on unbounded losses (NUMERICAL). The barbell is the optimum in form only at a hard cap. This section does not change the statement above.

## 4. What is not ready, and the next test

No dated field prediction is ready. No system has been shown to qualify under THEORY §3, and a field test of the bet would need its own locked preregistration. Inventing a public field prediction here would break that rule.

The cheapest next test of the conjecture is in-model: score the spread of the minimizing closed loop in the linear-quadratic-Gaussian class already used in the acting-loop note. That comparison was not scored. It should be preregistered before any new computation.

## 5. Where this sits

- `CORE.md` §4, "Rebuild, and gaining from shocks," and "Where this is going" item 5, carry this synthesis.
- Option route: `theory/ROBUSTNESS.md` §6, CT40.
- Learning route: `theory/ACTING_MEMORY_2026-11-22.md` (T45).
- Closed loop and the joining conjecture: `theory/ACTING_LOOP_2026-11-22.md` (T46), especially §5 and §8.
- Rebuild: `theory/antifragility_checks/RESULTS.md` (T43).
- Barbell: `theory/DYNAMICS.md`.
- Closed loop with payoff: `theory/ANTIFRAGILE_LOOP_2026-11-23.md`.
- Open work: T50 in `OPEN_WORK.md`.
