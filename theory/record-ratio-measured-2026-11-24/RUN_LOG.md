# T81 run log

`PREREG.md` was not edited after commit `22993a8a63213db260f55daad402a9bdef0d6e9e`. Its sha256 is `2e31c41bbc175722a421b7547af1670551cf14d5b912a3158d7085b62dff501c`.

The scored script is `measured_checks.py`. Stdout is `measured_checks.out`. Seed `20261124` is set and not drawn from. The script imports no random module. Two consecutive runs matched byte for byte.

No deviation. The list is `DEVIATIONS.md`.

`G-gap`, `M1-scale`, and `M4` miss the locked bars. Those misses were not repaired by editing the lock or the bars.

After the review of head `f625bb7`, the memo was corrected. The six locked fixed-point cells remain `POINT`, and each terminal is the entrance fraction of one extreme packet. At \(T=500\), between locked horizons 415 and 831, the same map 2-cycles. That readout is in `DEVIATIONS.md`. It is not a change to a locked bar.
