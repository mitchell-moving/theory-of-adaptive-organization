# ONSET PREREG: is the symmetric-accounting 4 the Poisson look onset?

*Tuesday 24 November 2026 (UTC). Own file. `PREREG.md`, `ADDENDUM_PREREG.md`, and `ADDENDUM_REVIEW_PREREG.md` are not edited. Commit this file before any script that scores the bars below. Branch `forge-dephasing-refresh`. `THEORY.md` and `CORE.md` are not edited. A later change to a prediction or a bar is appended in `DEVIATIONS.md`. Open-work id **T84b**. Self-check, not an independent review. The result is observed in-model until an independent review clears it.*

Can it fail: the boundary price can still scale with the stake, the exponential-age coefficient can differ from the uniform-age coefficient, and a half-slope loss can move the refresh limit off 4 while \(c^*\) stays at 4.

Cheapest way to fail it: keep \((a,b)=(1,2)\) and replace only the short-time loss coefficient by \(1/8\). No bath Hilbert space and no Monte Carlo.

## Why this approach

`theory/CLOCK_TERM_2026-11-23.md:126` says the information onset is the fixed-price Poisson onset \(c^*=4\kappa kT\) (section 2, the \(a=1\), \(b=2\) branch) with the look price replaced by \(\lambda kT\) times the information. Class RF has a symmetric-accounting threshold that tends to 4 (`PREREG.md:86-98`). The labeled hypothesis is that this 4 is that onset in disguise. The named rival is a coincidence of the constant 4: one 4 from \(2b/a\), the other from the \((\gamma T)^2\) expansion of the Hamming time average. Equating the integers does not decide which one it is. The bars below use the variable map and then change one input the onset is not allowed to follow if the two 4s are one object.

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. The qubit and the dephasing channel are inputs. The record price is a cost.

## 1. Variable map

Class CK, fixed price per look (`theory/CLOCK_TERM_2026-11-23.md:40-45`). Loss \(a(\omega-\omega')^2/f^2+b\,D/f\). For squared error just before a look, and for time-averaged squared error when looks are Poisson (age exponential), \(a=1\), \(b=2\). With \(K=\kappa kT\),

\[
c^*=2K\,b/a=4\kappa kT.
\]

Line 126 replaces \(c\) by \(\lambda kT\,I_0\) and keeps the same 4. The onset does not depend on the stake \(w\), the frequency, or a diffusion constant (`theory/CLOCK_TERM_2026-11-23.md:60`).

Class RF, symmetric accounting (`PREREG.md:45-56`, not edited). Refresh heat \(A=\lambda kT\,I_0\). Dimensionless group \(\Pi=w\gamma T^2/A\). Boundary

\[
\Pi_c(\Theta)=\frac{2\Theta^2}{1-(1+\Theta)e^{-\Theta}},\qquad \Theta=\gamma T.
\]

The parent series says \(\Pi_c\to 4\) as \(\Theta\to 0\). That sentence is an input, not a new fit.

| Clock onset | Refresh threshold | What the hypothesis identifies |
|---|---|---|
| look price \(c\) | refresh heat \(A\) | one price per reset |
| energy unit \(\kappa kT\) | the same unit, at \(\lambda=I_0=1\) | \(c^*/(\kappa kT)\) against a pure number |
| \(a=1\), \(b=2\), age exponential | Hamming loss, age uniform on the interval (`PREREG.md:35`) | one scoring |
| \(c^*\) independent of \(w\) | \(A_c=w\gamma T^2/\Pi_c(\gamma T)\) | one stake-free boundary |

Prior odds, stated before the script: 4:1 for the rival on M2, M3, and M4 (hypothesis weight 0.2). The two source formulas take different inputs, so a shared integer is the cheaper reading. M1 is the integer match itself and is not given those odds.

## 2. Bars

\(\kappa=\lambda=kT=1\). Then \(c^*/(\kappa kT)=4\).

**M1.** \(|\Pi_c(0.01)-4|\le 0.05\) and \(|c^*/(\kappa kT)-4|\le 10^{-12}\). Necessary for a shared 4. Not sufficient.

**M2.** Stake elasticity of the boundary price at \(\Theta=0.01\),

\[
e_A=\frac{\partial\ln A_c}{\partial\ln w},\qquad A_c=\frac{w\gamma T^2}{\Pi_c(\gamma T)}.
\]

The hypothesis says \(|e_A-0|\le 0.05\). A residual near \(+1\) is the rival: \(\Pi_c\) carries no \(w\), so \(A_c\) scales with \(w\), while \(c^*\) does not.

**M3.** Age law. Uniform-age coefficient \(\alpha_U=\lim_{u\to 0}\bar L(u)/u\), with \(\bar L\) the locked Hamming average. Exponential-age coefficient, the Poisson age in `theory/CLOCK_TERM_2026-11-23.md:40`,

\[
\alpha_E=\lim_{f\to\infty}\frac{f}{\gamma}\int_0^\infty f e^{-ft}\,\frac{1-e^{-\gamma t}}{2}\,dt.
\]

The hypothesis says both equal \(a/(2b)=1/4\), each within \(10^{-9}\). If \(|\alpha_E-\alpha_U|>10^{-3}\), M3 misses. The script evaluates the integral. It does not import a stored value.

**M4.** Cheapest separation. Keep \((a,b)=(1,2)\), so \(c^*/(\kappa kT)\) stays 4. Set the short-time loss to \(\beta\gamma\tau\) with \(\beta=1/8\). The refresh limit in the same \(\Pi\) is \(1/\beta\). The hypothesis says \(|1/\beta-4|\le 0.05\). The rival says the limit moves with \(\beta\) and the clock onset does not.

Headline `HIT_SAME_ONSET` only if M1–M4 all hold. If M1 holds and any later bar misses, the headline is `MISS_COINCIDENCE`. If M1 misses, the headline is `MISS_NUMBER`. The script builds the headline from the booleans. Observed in-model either way.

## 3. Which square-root class the refresh rate sits in

This section names the class. It does not rescore the parent identities, and it does not move R3.

Short-time Hamming loss grows as one power of the age (`PREREG.md:110-116`). The balance of a fixed heat \(A/\tau\) against a loss linear in \(\tau\) is the square-root balance. That is the square-root/EOQ class: slow modes of a random-walk world (`theory/INTERNAL_MODEL.md:45`, `:180`) and continuous diffusive tracking, where \(J^*\propto w^{1/2}\) (`theory/CLOCK_TERM_2026-11-23.md:55`). It is not class CK. Class CK's no-clock rate comes from a lag that grows as \(1/f^2\), and that rate scales as \(w^{1/3}\) (`theory/CLOCK_TERM_2026-11-23.md:40-47`, `:55`).

So \(\tau^*\sim 2\sqrt{A/(w\gamma)}\) and \(J^*\sim\sqrt{A w\gamma}\) are the elementary balance of the square-root class. Scoring them against that balance is `NOT A TEST`.
