# T81 memo: the record ratio measured as a return flow

*Tuesday 24 November 2026. Self-check, not an independent review. The lock is `PREREG.md` (sha256 `2e31c41bbc175722a421b7547af1670551cf14d5b912a3158d7085b62dff501c`, commit `22993a8`), before `measured_checks.py`. That file was not edited after the commit. A review of head `f625bb7` is recorded below, and it did not change the lock or the scored stdout.*

> "The law of adaptive organization (hypothesis): strongly selected systems minimize the cost of judgment." (`CORE.md:7`)

Nothing here derives general relativity, quantum mechanics, holography, or gravity. A miss is a puzzle. Every number below is in-model.

## Why this approach

Chad's framing, a hypothesis: \(q\) is the share of destruction that comes back to cost whoever did it. T74–T80 inferred a set of prices from a chosen angle. Forge's pivot, open to course-correction, is to measure the flow on a finite reversible walk and to keep T78's open sink as the case where destruction stays gone.

## Can it fail

Can it fail: yes. The collapse, the shape, the fixed-point cells, and the histogram were all able to miss. Three of the scored lines did. The six locked fixed-point cells passed, and a horizon between two of them cycles.

Cheapest way: two reservoirs at one nominal \(x\) whose returns differ by more than \(0.08\).

## Circularity and what could fail

The decoupled clock is not the return. \(\tau_{\mathrm{mix}}\) is \(1/(1-\lambda_2)\) of the environment path with the agent deleted and both ends reflecting. The committed `G-decouple` line builds the difference it reports: it copies the decoupled matrix, subtracts \(0.25\) from entry \((0,0)\), and sets the contact row sum to the literal \(0.75\). An environment block taken from the full path, built on its own, differs from that decoupled matrix by \(0.25\) at the same entry, and its contact row sums to \(0.75\). At \(N=32\) the gap clock is \(415.345062233342\). The two operators are not the same object. The committed line does not compare them.

| Check | Could it fail? | What happened |
|---|---|---|
| M1-closed | No. A finite walk that can reach the contact hits it eventually. | holds by construction. At \(N=12\) and \(N=48\), \(q=1\) and \(0.9999999999998\). Not evidence. |
| M1-sink | No. The contact step is absent, so the agent counter stays at 0. | holds by construction. Both horizons print \(0\). Not evidence. |
| M1-scale | Yes. | FAIL. The five returns fall: \(0.081686009166\), \(0.024811974888\), \(0.001090083804\), \(0.000015717030\), \(0.000000000043\). The last gap is \(1.572\times 10^{-5}\), under the locked \(10^{-4}\). The fall is real. The bar on the last step is the miss. |
| M2-collapse | Yes. | PASS. \(\rho=0.052051664190\), under \(0.08\). Eight nominal \(x\) stayed paired. Evidence. |
| M2-shape | Yes. The series is not the chain. | PASS. Maximum gap \(0.006720277156\) on 20 cells, under \(0.08\). Evidence. |
| M2-interior | Yes. | PASS. At \(N=32\), \(q(0.5)=0.095799965060\) and \(q(1)=0.239059227845\), both inside \((0.05,0.95)\). Evidence. |
| M3-conv | Yes. A step map can cycle or split. | PASS on the four locked cells. Each terminal is the entrance fraction of one extreme packet, and \(\Phi\) is constant there. Off that grid the same map cycles. The pass is not evidence of a unique fixed point on this menu. Existence of a root was not scored. |
| M3-corner | Yes. A corner can cycle. | PASS. Both corners are `POINT` (\(5.869\times 10^{-6}\) and \(0.866153244874\)), again the extreme-packet return. A set would also have passed. |
| M4 | Yes. Closedness need not act only through \(x\). | FAIL. Total variation \(0.909090909091\). Evidence that the pushforward misses. |
| E-pair | Not scored. | Same \(x\), same closedness, two starts: \(0.239059227845\) and \(0.048343059332\), difference \(0.190716168513\). The difference is a finite-horizon transient. |
| G-gap | Yes. An instrument bar. | FAIL. At \(N=48\) the Jacobi and power clocks differ by \(1.221\times 10^{-8}\), past \(10^{-8}\). The miss is the conditioning of \(1/(1-\lambda_2)\). Smaller \(N\) sit under the bar. Horizons do not move. |

`G-equiv` passes with both sides at 0. The locked cell is \(N=12\), \(T=5\), and the start is six sites from the contact, so five steps cannot arrive. A post-score readout, not a scored line, compares a positive hit: at \(T=7\) both sides equal \((1/4)^7=6.103515625\times 10^{-5}\), and at \(T=12\), \(20\), and \(40\) they agree.

## PROVED (in-model)

`G-form`. `closed_form_ant` and `functionals` differ by at most \(5.551\times 10^{-17}\) on the locked angles.

`G-rev` and `G-cons`. The lazy matrix is symmetric with residual 0, every row sums to 1, and twenty steps keep mass 1. Those checks follow from the way the matrix is built.

The scored \(q\) is a first-entrance fraction. At \(T=415\), \(N=32\), from the midpoint, that fraction is \(0.239059227845\) and the probability the excitation occupies an agent site is \(0.08197114\). Stationary occupation is \(4/36=1/9\). Entrance tends to 1, which is the construction result. Occupation tends to \(1/9\).

## NUMERICAL

`measured_checks.out`, `FAILS 3`.

**Model implication.** On this path the cumulative return of the midpoint start is a function of \(x=T/\tau_{\mathrm{mix}}\) to within \(0.052\), and the continuum series tracks it to within \(0.0067\). Those two comparisons can fail, and on this grid they did not.

**M3, puzzle.** The six locked cells are `POINT`, and the numbers are right: \(0.106409485164\), \(0.246706007043\), \(0.422916079022\) at nominal \(x=0.5,1,2\), with \(w=1\) printing the same value as \(w=2\) at \(x=1\). For \(w=2\) the minimizing width depends on \(q\) only from \(0.280\) to \(0.364\). For \(w=1\) that window sits from \(0.640\) to \(0.682\). On every locked cell the band of returns across widths 1 through 9 lies wholly below that window or wholly above it, so \(\Phi\) is constant. Below the window the terminal is the widest block, shared by widths 8 and 9. Above it the terminal is width 1. Five starts agree because each start lands on that constant. The widest of those bands is \(0.01061\), under the \(0.02\) diameter bar, so a stopped run on these cells meets `POINT`. The `CLASS` line still says evidence, because the lock told the script to print that tag.

Off the locked grid, at \(N=32\), \(T=500\), \(w=2\), between the locked horizons 415 and 831, every start enters a 2-cycle. The block of widths 6 and 7 returns \(0.288951536270\). The block of widths 8 and 9 returns \(0.291620058685\). The step is \(2.668522\times 10^{-3}\), above the stop tolerance \(10^{-4}\), so the locked rule calls the run `CYCLE`. A unique fixed point on the six locked horizons is the corner of the menu where the width no longer depends on \(q\). It is not evidence that this map has one fixed point.

**M4, puzzle.** For \(c<1\) the decoupled leak time is \(1713\) to \(2741\), so \(x(c)\) sits near \(0.15\) to \(0.24\) and the M2 curve predicts a return under \(0.2\). At \(c=1\), \(x=0.999169215516\) and the curve predicts \(0.226\). The measured fixed points stay near \(0.245\) for every \(c\), because a horizon of one closed-world relaxation does not let the far-end leak change a midpoint hit. Ten predicted masses sit in the first bin and the measurements sit in the second. Closedness did not act as a pure rescaling of \(x\).

**E-pair, not scored.** Two equally closed worlds at the same \(x\) do not share \(q\) once the start moves from the middle to the far site. The scored collapse is inside one start rule. The locked difference is a transient. At the same \(N\) and \(c\), the absolute difference is \(0.200853\) at nominal \(x=2\), \(1.448\times 10^{-4}\) at \(x=32\), and \(3.664\times 10^{-15}\) at \(x=200\), where both entrance fractions equal 1. Equally closed worlds can differ at a finite horizon and still share the eventual entrance fraction, which is the construction result.

**G-gap, puzzle.** At \(N=48\), \(1/\sin^2(\pi/96)=934.109433187964\). Jacobi prints \(934.109433200061\), \(1.210\times 10^{-8}\) above that closed form. Power iteration prints \(934.109433187855\), \(1.092\times 10^{-10}\) below it. The scored gap \(1.221\times 10^{-8}\) is this conditioning: \(\tau=1/(1-\lambda_2)\) turns an eigenvalue error near \(10^{-14}\) into a clock error near \(10^{-8}\). The eight nominal horizons at \(N=48\) are the same integers under the Jacobi clock and under the closed form. The fail stands. It is not the same kind of miss as M4.

Section 9 says the run will not set a reverse rate equal to a forward rate. The script builds one symmetric matrix and no reverse table. Under the uniform measure a symmetric generator has equal rates on an edge and on its reverse. The starts are point masses, out of that measure. `G-start` prints total variation \(0.9375\).

## Report, not scored

Distances to the T79 singleton \(0.30\) and to the parent's root \(0.6\):

| cell | \(q^\star\) | to \(0.30\) | to \(0.6\) |
|---|---|---|---|
| m3-a | \(0.106409485164\) | \(0.193590514836\) | \(0.493590514836\) |
| m3-b | \(0.246706007043\) | \(0.053293992957\) | \(0.353293992957\) |
| m3-c | \(0.422916079022\) | \(0.122916079022\) | \(0.177083920978\) |
| m3-d | \(0.246706007043\) | \(0.053293992957\) | \(0.353293992957\) |

Neither figure was a target. The nearest approach to \(0.30\) is \(0.053\). The nearest approach to \(0.6\) is \(0.177\).

## Errata

The lock was not edited. After the review of head `f625bb7`, this memo, the run log, and the deviation list record the decision window, the cycle at \(T=500\), the full-path environment block, the long-horizon E-pair differences, the occupation at \(T=415\), and the positive-hit comparisons. The script, the stored stdout, and the fail count were not changed.
