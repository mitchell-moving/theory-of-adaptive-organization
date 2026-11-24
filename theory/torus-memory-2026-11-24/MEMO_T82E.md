# T82e: one island, then the set splits

*24 November 2026 (UTC). Self-check, not an independent review. Locked in `PREREG_T82E.md`, sha256 `748514c79a5dd1d3393614207f9c0a814f1a49969da453bdf5af4fe37bbb4421`, commit `f8acadc`, before the orbits. In-model only. This is a toy Hamiltonian. It is not a claim about a physical pendulum, a fluid, or a celestial resonance.*

## Scores

| Item | Result | Number | Where |
|---|---|---|---|
| P-width | miss | \(\varepsilon=0.01\) width \(0.285000000000\) against \(0.282842712475\); \(\varepsilon=0.04\) has 4 plateaus; \(\varepsilon=0.09\) has 9 | `t82e_checks.out:20-23` |
| P-scale | miss | the \(0.04\) width is not one plateau, so the ratio is not formed | `:24` |
| P-higher | hit | count 0 at each positive coupling | `:25-28` |
| P-eps0 | hit | count 1, signed 0 | `:29` |
| P-record | miss | the cost gap is not formed, because the \(1/1\) set is not one plateau | `:30` |
| P-refine | miss | the fine grid also has 4 plateaus | `:31-35` |

Four misses (`t82e_checks.out:36-37`).

## What was measured

At zero coupling, one grid value has rotation number within \(0.002\) of \(1\) (`:2`, `:29`). At coupling \(0.01\) there is one \(1/1\) plateau, from \(0.860\) to \(1.140\), width \(0.285000000000\). The signed residual against \(2\sqrt{2}\sqrt{\varepsilon}\) is \(+0.002157287525\), relative \(0.007627163191\), inside the \(30\) percent band (`:4`, `:20`).

At coupling \(0.04\) the same test finds four plateaus (`:6-9`). The longest runs from \(0.775\) to \(1.225\). At coupling \(0.09\) there are nine (`:11-19`). The longest runs from \(0.820\) to \(1.270\). No plateau has denominator \(2\), \(3\), \(4\), or \(5\) (`:25-27`). The extra plateaus are still at \(1/1\): the set is split, not a staircase of other rationals.

The finer step and the finer grid at coupling \(0.04\) again find four plateaus (`:31-34`). The cost comparison needs one plateau, and there is not one (`:30`).

## Update

The \(1/1\) row misses: the coupling \(0.01\) width is inside the band, and couplings \(0.04\) and \(0.09\) do not form one plateau, so the square-root ratio is not formed (`PREREG_T82E.md:17`). The resonance thread on this toy is shelved. The next look is not another rational scan of this Hamiltonian. It is whether the continuous record is a smooth coordinate of the conserved actions, and that look needs its own preregistration. This lock and this scoreboard are not edited. No claim of a staircase is made from the split \(1/1\) set.
