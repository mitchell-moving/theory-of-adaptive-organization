# T84b: when refreshing a dephasing phase beats holding it

*Tuesday 24 November 2026. Self-check, not an independent review. Preregistered in `PREREG.md` (commit `612b82e`, sha256 `b2e96d76234da1e4a2521b990bb9cf456ca1c9c60a334ebf475f49b159dcab8f`) before this run. `THEORY.md` and `CORE.md` are unchanged. The qubit and the dephasing channel are inputs. Nothing here derives general relativity, quantum mechanics, holography, or gravity.*

## Why this approach

The candidates were unreviewed, so the threshold was derived before the lock (`PREREG.md:23-25`). The score is the rate \(\dot Q+w\,\mathbb E[\mathrm{loss}]\), with Hamming loss \((1-e^{-\gamma t})/2\) averaged over the age since the last refresh (`PREREG.md:31-41`). That is not T84's stock \(\kappa I+q\kappa P_D+w L\).

## Results

Headline `CLUE_REFRESH` (`dephasing_refresh_checks.out:11`). `FAILS 0` (`:12`). Checks R0–R9 pass.

**R0. PASS.** \(\bar L'\) matches a centered difference to \(1.550\times 10^{-11}\), and \(s_*\) matches \(1/(u^2\bar L')\) exactly. \(\bar L''<0\) on the locked \(u\) grid (`:1`).

**R1. PASS. Finite-hold threshold.** Accountings A and B, which charge the opening preparation to both policies or to neither, share one boundary

\[
\Pi_c(\Theta)=\frac{2\Theta^2}{1-(1+\Theta)e^{-\Theta}},\qquad \Theta=\gamma T_{\mathrm{hold}}.
\]

Below it every shorter period loses. Above it the interior period wins. The two accountings agree to \(1.137\times 10^{-13}\) (`:2`). Observed in-model, pending independent review. The closed form is the one locked before the script.

**R2. PASS. The small-window limit is 4, not 16.** \(\Pi_c(0.01)=4.02674456\), within \(1.186\times 10^{-7}\) of \(4+(8/3)(0.01)+(7/9)(0.01)^2\) (`:3`). The series tends to 4.

**R3. PASS. The candidate period and rate, as the leading term.** At \(u=0.01\), \(u\sqrt{s_*}/2=1.003338\) and \(J^*/\sqrt{A w\gamma}=0.998337\) (`:4`). So \(\tau^*\sim 2\sqrt{A/(w\gamma)}\) and \(J^*\sim\sqrt{A w\gamma}\) hold in the short-period limit. The exact period is the \(u\) with \(s_*(u)=w/(\gamma A)\), not the square root, once \(\gamma\tau_*\) is finite.

**R4. PASS. The band \(0.50\pm 0.05\) is only the short-period side.** Elasticity \(e(0.01)=0.50083\), \(e(0.5)=0.54149\), \(e(1)=0.58198\) (`:5`). At \(\gamma\tau_*=1\) the exact elasticity is outside the candidate band. T68's no-clock branch is \(w^{1/3}\) (`theory/CLOCK_TERM_2026-11-23.md:53-55`) because a deterministic lag grows as the square of the gap. Short-time dephasing grows as one power of the age.

**R5. PASS, as the other reading.** Accounting C drops \(A/T\) on the unrefreshed side only. Its own boundary gives \(\Pi=16.001600\) at \(u=10^{-4}\) and \(\Pi=16.160893\) at \(u=0.01\) (`:6`). That is the candidate \(\sim 16\). It is not the finite-hold threshold of A or B (`PREREG.md:120`).

**R6. PASS. Non-Markovian probe.** With coherence \(e^{-(\gamma t)^2}\), the short-time balance has loss share \(1/3\), gap \(5.551\times 10^{-17}\) (`:7`). The exponent \(1/2\) fails on this probe. The \(1/3\) is the same power T68 gets from a quadratic lag, from a different loss. The probe is the defined Gaussian envelope, not a fitted \(1/f\) spectrum (`PREREG.md:127-133`).

**R7. PASS. Unitary heat.** With \(H_u=A\) on every refresh, and \(\Pi\) still built from the Landauer piece alone, the small-window threshold doubles: \(2\Pi_c(0.01)=8.05348913\), within \(2.372\times 10^{-7}\) of the doubled series (`:8`). A quote of 4 that ignores \(H_u\) is wrong on this route.

**R8. PASS. The clock sentence does not govern this rate.** A TUR term \(\kappa kT\,\omega'^2/D\) (`theory/CLOCK_TERM_2026-11-23.md:19-21`) is zero at \(\omega'=0\) and positive for the probe \(\omega'=D=1\), at \(I_0\in\{1,4,10\}\). It does not lower \(J^*\). The class-CK arithmetic gives onset \(4\kappa kT\) (`:9`; `theory/CLOCK_TERM_2026-11-23.md:45`, `:125`). That onset stays in class CK.

**R9. PASS. Not T84's boundary.** At \(\Theta=0.01\), T84's \(h(\varepsilon)/\varepsilon=6.300822\) and \(\Pi_c=4.026745\). At \(\Theta=1\), \(t=1.973877\) and \(\Pi_c=7.568845\) (`:10`). On the locked grid, \(t\) falls and \(\Pi_c\) rises, and the difference changes sign. T84's \(w/\kappa>h(\varepsilon)/\varepsilon\) (`theory/dephasing-crossover-2026-11-24/PREREG.md:100-104`) is a stock comparison at one horizon. \(\Pi_c\) is a rate comparison of repeated preparation. They are not the same boundary in other variables.

## What the candidates got right

The definitions \(\Pi=w\gamma T_{\mathrm{hold}}^2/A\), \(\tau^*\sim 2\sqrt{A/(w\gamma)}\) and \(J^*\sim\sqrt{A w\gamma}\) are the short-period expansion of this derivation (`PREREG.md:101-104`). The stake exponent is \(1/2\) in that limit, against T68's \(1/3\). The Gaussian probe and a unitary heat \(H_u=A\) move the claim, as the failure routes said they would.

## Addendum: the holding floor is not the clock term

Locked in `ADDENDUM_PREREG.md` (commit `9619565`, sha256 `62871c9de3ad1d29046d2f73162139b5f0ae4d897a3204ca05859f3a9c5e63b2`) before `dephasing_refresh_addendum_checks.py`. The parent preregistration was not edited.

**Observed in-model.** Headline `OBSERVED_NOT_CLOCK` (`dephasing_refresh_addendum_checks.out:3`). `FAILS 0`.

The noiseless holding cost, computed from T84's \(J_H\) at \(\gamma\tau=0\), is \(F=0.693147180560=\ln 2\) (`:1`). The line-125 onset is 4 nats. The gap is \(3.306853\), above the bar of 3. The clock heat at \(\omega'=0\) is 0, and \(|F-0|=\ln 2\ge 0.5\). At \((\omega',D)=(1,1)\) the clock heat is 1 and at \((1,2)\) it is \(1/2\), so it moves with \(D\) while \(F\) does not (`theory/CLOCK_TERM_2026-11-23.md:19-21`, `:125`; `theory/dephasing-crossover-2026-11-24/PREREG.md:134`).

The guard forms fail the bars the stock floor passes (`:2`). Reading the floor as \(4\kappa/\lambda\) makes the gap to 4 equal to 0, so bar B2 fails. Reading it as the frozen ongoing heat, which is 0 (`CORE.md:78`), makes the gap to a clock that is off equal to 0, so bar B3 fails. The comparison separates the stock floor from those two forms, so the headline is not a consistency check.

The stake exponent and the \(\gamma,T_{\mathrm{hold}}\) scaling were not refit here. They remain the parent locks: short-period elasticity \(1/2\), with \(e(1)>0.55\) so the band is not uniform and is not T68's \(1/3\); \(w_c\sim 4A/(\gamma T_{\mathrm{hold}}^2)\) at small \(\gamma T_{\mathrm{hold}}\) (`PREREG.md` R2, R4; `ADDENDUM_PREREG.md` section C).

## Review fold-in

Locked in `ADDENDUM_REVIEW_PREREG.md` (commit `6fb397b`, sha256 `fc82c94bcf0ff3e639d6512475d8060228164b27c0a8f973dc4adc0b1f371dfd`) before `dephasing_refresh_review_checks.py`. The parent preregistration and the clock addendum were not edited. The independent review is fork PR #22 comment `7144884461`, write-up `theory/reviews/DEPHASING_CROSSOVER_REVIEW_2026-11-24.md` on `forge-dephasing-review` at `4513933`.

**Observed in-model.** Headline `OBSERVED_ALT_FLIPS` (`dephasing_refresh_review_checks.out:6`). `FAILS 0`.

The parent identities, including \(\Pi_c\to 4\) and the short-period elasticity \(1/2\), are consistency checks of the linear time-averaged Hamming cost. They are not a test that could miss inside that cost. T84's sign \(J_P-J_H=h(\varepsilon)-w\varepsilon\) is the same kind of identity. It restates the endpoint comparison for the binary Hamming rate-distortion function \(R(D)=\ln 2-h(D)\). The short-period square root restates a reset cost balanced against a loss linear in the interval. End-of-interval loss gives \(\sqrt{2A w\gamma}\); the time average gives \(\sqrt{A w\gamma}\). T84 locked neither exponent: its preregistration has no `w^{1/2}` and no `T_hold`.

The threshold \(t(\gamma,T)\) depends on \(\gamma\) and \(T\) only through \(\gamma T\): \(t(2,1/2)=t(1/2,2)=1.973877\), and the floor \(2\ln 2=1.386294361120\) does not move with either factor alone (`:2`). At the printed cell \(\gamma\tau=1\), \(w=2\), the stake elasticity is \(0.901222\), at least \(0.3\) from \(1/2\) (`:3`).

Squared Hamming on the refresh rate has loss share \(1/3\) and critical \(\Pi=600\) at \(\gamma T=0.01\), not \(4\) (`:4`). The five nearby one-shot costs flip the locked signs (`:5`): carrier entropy \(J_H=0.939924\) at stake \(1\); linear-leak threshold \(0.193085\); squared one-shot \(J_H=0.269071\) at stake \(2\); stake-dependent rent gap \(1.239472\); linear-coherence threshold \(3.436564\).

## Onset map

Locked in `ONSET_PREREG.md` (commit `a27520c`, sha256 `659ed3e67e40bc03aef71bb69c694eb91e3ee0049a7e907570945d9fd42760fb`) before `dephasing_refresh_onset_checks.py`. The three earlier locks were not edited.

**Observed in-model.** Headline `MISS_COINCIDENCE` (`dephasing_refresh_onset_checks.out`).

The labeled hypothesis was that \(\Pi_c\to 4\) is the Poisson look onset \(c^*=4\kappa kT\) (`theory/CLOCK_TERM_2026-11-23.md:126`, the \(a=1\), \(b=2\) branch). The named rival was a shared integer: \(2b/a=4\) from that branch, and 4 from the \((\gamma T)^2\) expansion of the Hamming average.

M1 holds: \(c^*/(\kappa kT)=4\) and \(\Pi_c(0.01)=4.02674456\), residual \(+0.02674456\), inside \(0.05\). That is the integer match. It does not identify the objects.

M2 misses by \(+1\): the boundary price \(A_c=w\gamma T^2/\Pi_c\) has stake elasticity \(+1.00000000\), and \(c^*\) has elasticity 0. M3 misses by \(+0.250000\): the uniform-age slope is \(1/4\), and the exponential-age slope, which is the Poisson age in `theory/CLOCK_TERM_2026-11-23.md:40`, is \(1/2\). M4 misses by \(+4\): with \((a,b)\) held at \((1,2)\), a short-time slope \(1/8\) moves the refresh limit to 8 and leaves \(c^*\) at 4.

The refresh rate sits in the square-root/EOQ class. Short-time Hamming loss is linear in the age, so \(A/\tau\) against that loss is the balance at `theory/INTERNAL_MODEL.md:45` and `:180`, and the diffusive \(w^{1/2}\) balance at `theory/CLOCK_TERM_2026-11-23.md:55`. It is not the CK balance at `theory/CLOCK_TERM_2026-11-23.md:40-47`, whose lag grows as \(1/f^2\) and whose rate scales as \(w^{1/3}\). The parent identities \(\tau^*\sim 2\sqrt{A/(w\gamma)}\) and \(J^*\sim\sqrt{A w\gamma}\) are that elementary balance. Scoring them is `NOT A TEST`.

## Deviations

None from the locks. `PREREG.md` was not edited after `612b82e`. `ADDENDUM_PREREG.md` was not edited after `9619565`. `ADDENDUM_REVIEW_PREREG.md` was not edited after `6fb397b`. `ONSET_PREREG.md` was not edited after `a27520c`.
