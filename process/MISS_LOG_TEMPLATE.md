# Miss, Hit, and Deviations Log Template

*Copy this template for future test `RESULTS.md` / `DEVIATIONS.md` entries and process miss logs. Rules and derivation: [`process/PROCESS.md`](PROCESS.md).*

**Lock reference:** `<branch/commit SHA of locked PREREG.md or baseline state>`  
**Logged at (ET):** `<YYYY-MM-DD HH:MM ET>`  
**Breach check:** `none` *(confirm lock is unedited, no post-hoc prediction patching, no data fabrication or privacy breach)*

## Minimal ledger (every miss and hit gets one row; do not skip small ones)

| prediction_id | locked_prediction (value/band; odds if feasible) | outcome | miss (signed size & direction, or HIT + info) | location (`model` \| `measurement/code` \| `process`) | stake_x_info (`low` \| `medium` \| `high`) | update (what changed, or `none yet`) | breach_check |
|---|---|---|---|---|---|---|---|
| `<ID-1>` | `<point/band; rival/prior odds>` | `<observed value>` | `<outcome - pred, sign & units>` | `<model / measurement/code (MV gate) / process>` | `<low / medium / high>` | `<doc/code changed + commit, or none yet (inside band)>` | `none` |

## Scaled write-up (write only in proportion to `stake_x_info`)

- **`low` (`stake_x_info`):** stop at the ledger row above. Do not bloat low-stake misses; monitor for repetition before updating.
- **`medium` / `high` (`stake_x_info`):** add one concise block per item below:
  1. **Prediction & risk:** what was locked, what named rival or baseline was excluded, and prior odds / `MV10` power if computed.
  2. **Miss & location:** signed residual `outcome - locked_prediction`, and whether it sits in `model`, `measurement/code` (naming the failed `MV1`–`MV8` gate or reproducible bug; anti-rescue rule `measurement/FRAMEWORK.md` §2.2), or `process`.
  3. **Update driven:** what changed (scaled to miss size, repetition, and stake; avoid overfitting a single noisy miss), or why no update is warranted yet.
