#!/usr/bin/env python3
"""SURPRISE-GUIDED-SEARCH (SG) ranking rule for the GTAO queue — protocol v2 (15 Nov 2026).

Protocol v2 applies the fixes in reviews/night2/AUDIT_REFEREE.md §6.5. Ledger entries 0-5 are PRE-PROTOCOL
and excluded from scoring; the scoring clock starts at the first entry of kind "protocol" (entry 6).
Locked parameters below; any change needs a ledger entry of kind "rule_change" BEFORE use.

Index  I_k = w_k * P_k * v_k * L_k / c_k     (definitions unchanged from v1)
  w  stakes: 3 = could change a THEORY.md §0/§2 headline claim or a §8b candidate row;
             2 = any other CLAIM_MAP row; 1 = process/infrastructure only.
  P  never tested on a valid instrument -> 0.5; otherwise the surprise-updated decreasing-hazard prior
       p0 = 1 - ((a+A0)/(a+DELTA+A0))**GAMMA (Lomax model; a modelling choice), P = LR*p0/(1-p0+LR*p0)
  v  validity; L exposure (1 + dependent items/rows); c cost in weekly-usage points (floor 0.5).
Surprise scale (LR): none 1; weak 3; strong 10; decisive 30.
GAMMA = 0.4 rounds SELF P1b's -0.39, which was INCONCLUSIVE and measured on a statement-time proxy;
sensitivity ranks at GAMMA in {0.2, 0.8} are logged with every ranking.

Commands
  python3 sg_rank.py rank  items.json                 print the ranking
  python3 sg_rank.py log   items.json ENTRY UNAIDED   append a rule_rank entry (ENTRY = new entry number;
                                                      UNAIDED = number of the unaided_order entry, which must
                                                      already be in the ledger with an earlier time)
  python3 sg_rank.py score                            score once >= 15 post-protocol outcomes exist

Uniform baseline (frozen convention): random.Random(20261115 + ENTRY).shuffle(sorted(ids)); the full permutation
is stored, so every item has a uniform rank.

Pick cycle (post-protocol picks counted from 1): picks 1, 2 -> rule's top; pick 3 -> unaided top (rule's top if
the same); pick 4 -> top of the stored uniform permutation; repeat.

Scoring (locked): predictor = each item's FIRST-SEEN post-protocol score (rule index, unaided rank, uniform rank)
from the first rule_rank entry that contains it. Population = items with an outcome record; unpicked items are
counted and reported, not imputed. Outcome = any CLAIM_MAP_v2 status changed (proxy; useful work that leaves a row
OPEN scores 0). An outcome entry may record this as `status_changed` or, in one logged case, `claim_map_status_changed`; `score` accepts either and does not crash if both are missing (that entry is reported and skipped). AUC with 2,000 item-bootstrap resamples (seed 20261115). PASS: rule AUC > 0.5 with CI excluding 0.5
and rule AUC >= unaided AUC. KILL: rule AUC <= 0.5, or below unaided by > 0.1. Else INCONCLUSIVE. A pass tests this
operational rule including the judgment factors w, v, L, c, not the bare SG clock; the clock is scored separately on
items whose P was not flat (n reported; no verdict if n < 8).
"""
import hashlib, json, os, random, sys, datetime

GAMMA, A0, DELTA = 0.4, 1.0, 1.0
LR = {"none": 1, "weak": 3, "strong": 10, "decisive": 30}
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "LEDGER.jsonl")
SEED0 = 20261115

def prob(it, gamma=GAMMA):
    if it.get("untested", False):
        return 0.5
    a = max(it["age_days"], 0.1)
    p0 = 1 - ((a + A0) / (a + DELTA + A0)) ** gamma
    lr = LR[it["surprise"]]
    return lr * p0 / (1 - p0 + lr * p0)

def rank(items, gamma=GAMMA):
    out = []
    for it in items:
        P = prob(it, gamma)
        out.append({**it, "P": P, "index": it["w"] * P * it["v"] * it["L"] / max(it["c"], 0.5)})
    return sorted(out, key=lambda r: (-r["index"], r["id"]))

def uniform_perm(entry, ids):
    ids = sorted(ids)
    random.Random(SEED0 + entry).shuffle(ids)
    return ids

def read_ledger():
    return [json.loads(l) for l in open(LEDGER) if l.strip()]

def cmd_log(items_path, entry, unaided):
    items = json.load(open(items_path))
    led = read_ledger()
    assert all(e["entry"] != entry for e in led), "entry number already used"
    ua = [e for e in led if e["entry"] == unaided and e["kind"] == "unaided_order"]
    assert ua, "unaided_order entry must be logged first"
    ids = [i["id"] for i in items]
    assert sorted(ua[0]["order"]) == sorted(ids), "unaided order must cover exactly the ranked items"
    r = rank(items)
    rec = {"entry": entry, "time_et": datetime.datetime.now().astimezone().isoformat(timespec="minutes"),
           "kind": "rule_rank", "protocol": 2, "rule": "sg_rank.py protocol v2",
           "params": {"GAMMA": GAMMA, "A0": A0, "DELTA": DELTA},
           "items_sha256": hashlib.sha256(open(items_path, "rb").read()).hexdigest(),
           "unaided_entry": unaided,
           "order": [x["id"] for x in r],
           "index": {x["id"]: round(x["index"], 6) for x in r},
           "P": {x["id"]: round(x["P"], 6) for x in r},
           "unaided_rank": {k: i + 1 for i, k in enumerate(ua[0]["order"])},
           "uniform_seed": SEED0 + entry, "uniform_perm": uniform_perm(entry, ids),
           "sensitivity_order": {str(g): [x["id"] for x in rank(items, g)] for g in (0.2, 0.8)}}
    with open(LEDGER, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec, indent=1))

def auc(scores, y):
    pos = [s for s, t in zip(scores, y) if t]; neg = [s for s, t in zip(scores, y) if not t]
    if not pos or not neg:
        return float("nan")
    return sum((p > n) + 0.5 * (p == n) for p in pos for n in neg) / (len(pos) * len(neg))

def outcome_status_changed(e):
    """Return (found, value). Prefer status_changed; accept claim_map_status_changed."""
    if "status_changed" in e:
        return True, bool(e["status_changed"])
    if "claim_map_status_changed" in e:
        return True, bool(e["claim_map_status_changed"])
    return False, None

def cmd_score():
    led = read_ledger()
    start = min(e["entry"] for e in led if e["kind"] == "protocol")
    first = {}
    for e in sorted(led, key=lambda e: e["entry"]):
        if e["entry"] > start and e["kind"] == "rule_rank" and e.get("protocol") == 2:
            for k in e["order"]:
                if k not in first:
                    n = len(e["order"])
                    first[k] = (e["index"][k], n + 1 - e["unaided_rank"][k],
                                n - e["uniform_perm"].index(k), e["P"][k] != 0.5)
    outs = {}
    missing = []
    aliased = []
    for e in led:
        if e["entry"] > start and e["kind"] == "outcome" and e.get("item") in first:
            found, val = outcome_status_changed(e)
            if not found:
                missing.append(e.get("entry"))
                continue
            if "status_changed" not in e:
                aliased.append(e.get("entry"))
            outs[e["item"]] = val
    if aliased:
        print("outcome entries using claim_map_status_changed (accepted): " +
              ", ".join(str(x) for x in aliased))
    if missing:
        print("warning: outcome entries missing status_changed and "
              "claim_map_status_changed (skipped): " +
              ", ".join(str(x) for x in missing))
    ids = sorted(outs)
    print(f"post-protocol items ranked: {len(first)}; with outcomes: {len(ids)}; unpicked: {len(first) - len(ids)}")
    if len(ids) < 15:
        print("fewer than 15 outcomes: no verdict"); return
    y = [outs[k] for k in ids]
    rng = random.Random(SEED0)
    for name, j in (("rule", 0), ("unaided", 1), ("uniform", 2)):
        s = [first[k][j] for k in ids]
        bs = [auc([s[i] for i in b], [y[i] for i in b])
              for b in ([rng.randrange(len(ids)) for _ in ids] for _ in range(2000))]
        bs = sorted(x for x in bs if x == x)  # drop NaN BEFORE sorting (ledger 74 rule_change; NaN garbles sorted())
        print(f"{name:8s} AUC {auc(s, y):.3f}  95% CI {bs[int(.025*len(bs))]:.3f}-{bs[int(.975*len(bs))]:.3f}")
    nf = [k for k in ids if first[k][3]]
    print(f"items with non-flat P (SG clock subset): {len(nf)}" + ("" if len(nf) >= 8 else " (< 8: no clock verdict)"))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "rank"
    if cmd == "rank":
        for i, r in enumerate(rank(json.load(open(sys.argv[2] if len(sys.argv) > 2 else "items.json"))), 1):
            print(f'{i:2d}. {r["id"]:22s} I={r["index"]:6.3f}  w={r["w"]} P={r["P"]:.3f} v={r["v"]} L={r["L"]} c={r["c"]}')
    elif cmd == "log":
        cmd_log(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif cmd == "score":
        cmd_score()
    else:
        print(__doc__)
