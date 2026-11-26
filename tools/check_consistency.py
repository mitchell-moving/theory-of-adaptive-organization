#!/usr/bin/env python3
"""Consistency check for the GTAO repository (stdlib only).

Run from the repo root:  python3 tools/check_consistency.py
Exit code 0 = no FAIL in the maintained (canonical) documents.

What it checks
  1. Versions: THEORY.md's title version and CLAIM_MAP_v2.md's latest "vN note"
     agree with the two copies in files this repo may not edit (CORE.md, THEORY.md);
     every other copy is a hand pointer (tools/check_fresh.py).
  2. Banned wording in maintained docs:
       - "law" used of GTAO (any bare 'law' not in an allow-listed compound
         such as 'power law', 'area law', 'law firm', a named physical law,
         or a negation such as 'not a law' / never 'law'; a sentence that
         labels itself a hypothesis may name the law: Chad t1979u, 19 Nov 2026);
       - "theory of everything" unless negated ('not a theory of everything');
       - "solved" claimed of GTAO / the theory unless negated or quoted as a rule;
       - a field-test name next to passed/failed/confirmed/refuted/killed in
         the same sentence without a proxy / in-model / gate / tier label
         ('miss' is allowed; puzzle, bill, kill, dead and verdict are banned by
         tools/banned_words.py, below);
       - the MV gates described as awaiting Chad's sign-off (they bind as of
         18 Nov 2026, Chad t1927).
       - stale scope phrases ('silent on black holes', 'nothing is keeping
         score', 'no predictions about black holes').
  2b. Banned words (tools/banned_words.py): 'puzzle' in any maintained doc, and
     puzzle, bill, kill, dead or verdict on any .md line added since origin/main,
     unless quoted, in backticks, or marked <!-- banned-ok: reason -->.
  3. CLAIM_MAP N-rows: every 'N<k>' cited with a CLAIM_MAP context in a
     maintained doc exists in CLAIM_MAP section N, and wherever a maintained
     doc states a status right after a CLAIM_MAP N-number, the base status
     matches the CLAIM_MAP row.
  4. Process rules (lock pass, 18 Nov 2026; reviews/lock_2026-11-18/PROCESS.md):
     R1 no self-review is called independent; R2 the CLAIM_MAP current tally
     equals the rows; R3 table rows have as many cells as their header; R4 no
     named GTAO relation is called a 'law'; R5 the repo is not called private.
  5. Core rules (THEORY v2.0, 19 Nov 2026): R6 every ID in THEORY Appendix C
     is in CLAIM_MAP section O (and back) with the same base status and
     counted row; R7 length report (a soft warning, never a failure: the
     old 5,500-word THEORY cap and 900-word README cap are now advisory
     reference lengths; the main text is kept tight on merit, and the
     '## Appendix A.' heading that ends it must exist); R8 the keep / hold / know table appears only in THEORY §1 and
     README.
Frozen history (locked tests, preregs, review records, night-1/2 working
files, older theory notes) is scanned for the same wording and reported as
INFO only: those files are dated records and are not edited.
"""
import glob, os, re, sys

# Maintained docs: edited to stay current. check_fresh.py and check_claims.py import this list.
MAINTAINED_DOCS = [
    "README.md", "THEORY.md", "CORE.md", "process/PROCESS.md", "process/VOCABULARY.md", "process/FAILURES.md", "process/MISS_LOG_TEMPLATE.md",
    "measurement/FRAMEWORK.md", "measurement/CLAIM_MAP_v2.md",
    "theory/SCALE_ENDS.md", "theory/PHYSICS_CHAIN_2026-11-23.md",
    "applications/README.md", "tests/README.md", "reviews/README.md",
    "litmap/LITMAP.md", "litmap/PRIOR_ART.md", "litmap/THREATS.md",
    "litmap/LEFT_ON_THE_TABLE.md", "theory/BOOKENDS.md",
    "theory/REACH.md", "theory/HT_INDEX.md", "theory/COSMIC_WEB.md", "theory/WORMHOLES.md", "theory/TORUS.md",
    "theory/GENERAL_THEOREM.md", "theory/INTERNAL_MODEL.md", "theory/COADAPTATION.md", "theory/REPRESENTATION.md", "theory/MATH_ATTACK.md",
    "reviews/night1/formal/AXIOMS.md", "reviews/night1/formal/THEOREMS.md", "reviews/night1/formal/checks/README.md",
    "process/LOCK_ERRATA.md",
]


def main(argv=None):
    """Run every check from the repo root; return the exit code (0 = no FAIL).
    Kept inside main() so importing this module (e.g. pytest collection) has no
    side effects: no chdir, no output, no sys.exit."""
    argv = sys.argv if argv is None else argv
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(ROOT)

    MAINTAINED = list(MAINTAINED_DOCS)
    MAINTAINED = [f for f in MAINTAINED if os.path.exists(f)]
    ALL_MD = sorted(p for p in glob.glob("**/*.md", recursive=True))
    FROZEN = [p for p in ALL_MD if p not in MAINTAINED]

    fails, infos = [], []

    def read(p):
        with open(p, encoding="utf-8") as fh:
            return fh.read()

    def lines(p):
        return read(p).split("\n")

    # ---------------------------------------------------------------- 1. versions
    theory = read("THEORY.md")
    m = re.search(r"^# .*? v(\d+\.\d+(?:\.\d+)?[a-z]?) draft", theory, re.M)
    THEORY_V = m.group(1) if m else None
    cm = read("measurement/CLAIM_MAP_v2.md")
    notes = [tuple(int(x) for x in v.split(".")) for v in re.findall(r"^\*\*v(2\.\d+) note", cm, re.M)]
    CM_V = "%d.%d" % max(notes) if notes else None
    print("== 1. Versions")
    print("THEORY.md title: v%s; CLAIM_MAP latest note: v%s" % (THEORY_V, CM_V))
    if not THEORY_V or not CM_V:
        fails.append("versions: could not read THEORY or CLAIM_MAP version")

    # Pointer patterns: (file, regex, which) -- each must match at least once and every match must agree.
    POINTERS = [  # the only version copies left: both sit in files this repo may not edit (tools/check_fresh.py ALLOW)
        ("CORE.md", r"is the canonical statement \(v(\d+\.\d+(?:\.\d+)?[a-z]?) draft\)", "T"),
        ("THEORY.md", r"Claim statuses: `measurement/CLAIM_MAP_v2\.md` \(v(2\.\d+)\)", "C"),
    ]
    for f, rx, which in POINTERS:
        if not os.path.exists(f):
            fails.append("versions: %s missing" % f); continue
        want = THEORY_V if which == "T" else CM_V
        found = re.findall(rx, read(f))
        if not found:
            fails.append("versions: %s has no pointer matching /%s/" % (f, rx)); continue
        bad = [v for v in found if v != want]
        status = "OK" if not bad else "FAIL"
        print("  %-4s %-26s %s -> %s (want v%s)" % (status, f, "THEORY" if which == "T" else "CLAIM_MAP", ",".join("v" + v for v in found), want))
        if bad:
            fails.append("versions: %s points to %s, current is v%s" % (f, ",".join(bad), want))

    # Hash locks: every lock verifies or is accounted for (process/LOCK_ERRATA.md).
    # Needs the real checkout: the mutation test copies only .md and .py files (no .git), so it is skipped there.
    if os.path.exists(os.path.join(ROOT, ".git")):
        from verify_locks import verify as _verify_locks
        lock_fails, _lc, _ln = _verify_locks(ROOT)
        for x in lock_fails:
            print("  FAIL " + x)
            fails.append("FAIL " + x)

    # ---------------------------------------------------------------- 2. wording
    LAW_OK = re.compile(
        r"(power[- ]laws?|area[- ]laws?|law firms?|second law|first law|laws? of (thermodynamics|motion|physics|large numbers|their interaction|nature)|"
        r"(Moore|Kleiber|Zipf|Little|Ohm|Hooke|Fick|Weber|Fechner|Hick|Taylor|Heaps|Benford|Lotka|Bergmann|Cope|Haldane|Newton|Wolff|Landauer|Ashby|Goodhart|Conway|Pareto|Allee|Fitts|Weber.Fechner|Kepler|Planck|Stefan.Boltzmann|Wien|Hubble|Curie|Gibrat|Okun|Wagner|Brooks|Parkinson|Murphy)'?s? laws?|"
        r"case law|by law|in-?laws?|lawyers?|lawful|lawsuit|law-like|legal)", re.I)
    NEG_LAW = re.compile(r"(not (a |called a |presented as a )?['\"“‘]?laws?|never (a |be called a |called a )?['\"“‘]?laws?|no ['\"“‘]?laws?['\"”’]?|['\"“‘]law['\"”’]|“law”|‘law’|\"law\"|'law')", re.I)
    GTAO_LAW = re.compile(r"((GTAO|the theory|this theory|our theory|A Theory of Adaptive Organization)('s)?\b[^.;|]{0,40}\b(is|as|becomes|called|calls itself|a|the)\b[^.;|]{0,15}\b(universal |general |new |fundamental )?laws?\b|\b(universal|fundamental|general) laws? of (adaptive|organi[sz]ation|life|persistence)|\blaw of adaptive organi[sz]ation)", re.I)
    TOE = re.compile(r"theor(y|ies) of everything", re.I)
    TOE_NEG = re.compile(r"(not|never|isn't|is not|no)[^.]{0,40}theor(y|ies) of everything|theor(y|ies) of everything['\"”’]?\)?[^.]{0,30}(imposter|banned|withdrawn)", re.I)
    SOLVED_GTAO = re.compile(r"\b(GTAO|the theory|this theory|our theory|the hypothesis|cost of judgment|adaptive organization)\b[^.;|]{0,40}\b(is |has been |now )?solved\b|\bsolved\s+(GTAO|everything|adaptive organization)\b", re.I)
    SOLVED_NEG = re.compile(r"\b(not|never|isn\'t|is not|nor|no)\b[^.;|]{0,20}\bsolved\b|[\'\"“‘]solved[\'\"”’]", re.I)
    FIELD = re.compile(r"\b(MATCH1|DECISIVE|banks?|glucose|populations|F1|C3b?|BIO1|COLLAPSE1|DRIFT1|measles|PIAAC|Enron|VIGIL[_-]ONA|GITHUB-UPSTREAM|WIKIDATA-BAND|CAISO|SPF|VIX|SENSE-CELL|LANG1|MEASURE-SELF|news(-| )recall|D3S?)\b")
    VERDICT = re.compile(r"(\b(passed|failed|confirmed|refuted|killed|kill fired)\b|\bHIT\b)")
    LABEL = re.compile(r"(failed[- ]bank|proxy|PROXY|in-model|in model|SIM-|simulat|synthetic|dry run|gate|MV\d|Tier|known-groups|prereg|locked|lock |kill rule|joint (kill )?rule|refutation (condition|rule|test)|fair refutation|fails if|qualifying miss|miss to (diagnose|locate)|signed miss|process miss|literal|referee|review|power|not a (theory-specific )?hit|sign-only|INCONCLUSIVE|NOT EVIDENCE|MATH-CORRECTED|withdrawn|premise|by construction|reproduce|replicate|own code|own MC|Monte Carlo|pass rule|wrong-pass|[\"“][^\"”]{0,12}(hit|passed|failed)[^\"”]{0,3}[\"”])", re.I)
    SIGNOFF = re.compile(r"(sign[- ]?off|signs off|signed off|once Chad|until Chad|await(s|ing)? Chad)", re.I)
    GATECTX = re.compile(r"(gate|MV\d|M2\b|binding)", re.I)
    STALE = re.compile(r"(silent on black holes|nothing (is )?keeping score|no predictions? about black holes|makes no predictions about black holes)", re.I)
    STALE_OK = re.compile(r"(superseded|\*\*wrong\*\*|was wrong|Ace told Chad|Ace's line|contradicts the record|Never say|never say|withdrawn|stale)", re.I)

    def sentences(text):
        # crude sentence split that keeps table cells apart
        for para in re.split(r"\n|\|", text):
            for s in re.split(r"(?<=[.;!?])\s+(?=[A-Z*(\"“])", para):
                if s.strip():
                    yield s

    def scan_wording(path, sink, tag):
        hits = 0
        for i, ln in enumerate(lines(path), 1):
            if ln.lstrip().startswith(("http", "<!--")):
                continue
            for s in sentences(ln):
                # law: only 'law' used of GTAO / the theory (probability laws,
                # conservation laws, published scaling laws are not GTAO claims)
                for mm in GTAO_LAW.finditer(s):
                    ctx = s[max(0, mm.start() - 20): mm.end() + 40]
                    lawword = s[max(0, mm.end() - 30): mm.end()]
                    # Chad t1979u (19 Nov 2026): one explicit, labeled hypothesis statement may name the law
                    if LAW_OK.search(lawword) or NEG_LAW.search(s) or re.search(r"WITHDRAWN", ln) or re.search(r"\bhypothes[ie]s\b", s, re.I):
                        continue
                    sink.append("%s %s:%d law: …%s…" % (tag, path, i, ctx.strip())); hits += 1
                if TOE.search(s) and not TOE_NEG.search(s):
                    sink.append("%s %s:%d theory-of-everything: …%s…" % (tag, path, i, s.strip()[:160])); hits += 1
                if SOLVED_GTAO.search(s) and not SOLVED_NEG.search(s):
                    sink.append("%s %s:%d solved-claim: …%s…" % (tag, path, i, s.strip()[:160])); hits += 1
                if FIELD.search(s) and VERDICT.search(s) and not LABEL.search(s):
                    sink.append("%s %s:%d unlabeled field verdict: …%s…" % (tag, path, i, s.strip()[:200])); hits += 1
                if SIGNOFF.search(s) and GATECTX.search(s) and not re.search(r"(no longer|superseded|bind(s|ing)? as of|was:|before 18 Nov|binding since|nothing awaits|treated as binding)", s, re.I):
                    sink.append("%s %s:%d gates-await-sign-off: …%s…" % (tag, path, i, s.strip()[:200])); hits += 1
                if STALE.search(s) and not STALE_OK.search(s):
                    sink.append("%s %s:%d stale-scope: …%s…" % (tag, path, i, s.strip()[:200])); hits += 1
        return hits

    print("\n== 2. Wording (maintained docs: FAIL; frozen records: INFO)")
    wf = []
    for p in MAINTAINED:
        scan_wording(p, wf, "FAIL")
    fails.extend(wf)
    for x in wf:
        print("  " + x)
    print("  maintained docs scanned: %d; wording FAILs: %d" % (len(MAINTAINED), len(wf)))
    fi = []
    for p in FROZEN:
        scan_wording(p, fi, "INFO")
    infos.extend(fi)
    print("  frozen records scanned: %d; INFO hits (not edited, dated records): %d" % (len(FROZEN), len(fi)))

    # 2b. banned words (tools/banned_words.py): puzzle in maintained docs; five words on added lines
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import banned_words as _bw
    bw_fails = _bw.check_puzzle(ROOT, MAINTAINED)
    bw_added, bw_note = _bw.check_added(ROOT)
    for x in bw_fails + bw_added:
        print("  FAIL " + x)
        fails.append("FAIL " + x)
    if bw_note:
        print("  NOTE " + bw_note)
    print("  banned words: %d FAIL(s)%s" % (len(bw_fails) + len(bw_added), "; added-line check skipped" if bw_note else ""))

    # ---------------------------------------------------------------- 3. N rows
    print("\n== 3. CLAIM_MAP section N")
    rows = {}
    for ln in cm.split("\n"):
        mm = re.match(r"^\| (N\d+) \|", ln)
        if mm:
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", ln)]
            rows[mm.group(1)] = cells[4] if len(cells) > 4 else ""
    BASES = ["NOT A TEST", "PROXY-PASS", "PROXY-FAIL", "MATH-CORRECTED", "NOT EVIDENCE", "NOT APPLICABLE", "PRIOR ART", "INCONCLUSIVE", "WITHDRAWN", "DECIDED", "PROVED", "OPEN", "FALSE", "SIM-FAIL", "SIM-PASS", "BINDING"]
    def base(s):
        s = s.replace("*", "")
        for b in BASES:
            if re.search(r"\b" + re.escape(b) + r"\b", s):
                return b
        return None
    print("  rows in CLAIM_MAP section N: %d (%s..%s)" % (len(rows), min(rows, key=lambda k: int(k[1:])), max(rows, key=lambda k: int(k[1:]))))
    cm_ctx = re.compile(r"(CLAIM_MAP|CM)\s*(v2\.\d+\s*)?(rows?\s*)?$")
    nref = re.compile(r"\b(N(\d{1,2}))\b(?:\s*(?:/|,|and|–|-)\s*N\d{1,2})*\s*(?:\(|is |stays |now |moved to |→ |=|:)?\s*\**\s*(NOT A TEST|PROXY-PASS|PROXY-FAIL|MATH-CORRECTED|NOT EVIDENCE|PRIOR ART|INCONCLUSIVE|WITHDRAWN|DECIDED|PROVED|OPEN|SIM-FAIL)\b")
    nchecked, nfail = 0, 0
    for p in MAINTAINED:
        if p == "measurement/CLAIM_MAP_v2.md":
            continue
        in_theory_s1 = False
        for i, ln in enumerate(lines(p), 1):
            if p == "THEORY.md":
                if ln.startswith("## 1."):
                    in_theory_s1 = True
                elif ln.startswith("## ") and not ln.startswith("## 1."):
                    in_theory_s1 = False
                if in_theory_s1 and ln.startswith("| N"):
                    continue  # THEORY §1 rows N1-N6 are that file's own numbering
            for mm in re.finditer(r"(CLAIM_MAP|CM)[^|.;]{0,25}?\b(N\d{1,2})\b", ln):
                nchecked += 1
                if mm.group(2) not in rows:
                    fails.append("N-ref: %s:%d cites CLAIM_MAP %s, which has no row" % (p, i, mm.group(2))); nfail += 1
            # explicit "N<k> STATUS" statements, including grouped forms like N25/N26 PROVED
            for mm in re.finditer(r"\b((?:N\d{1,2}\s*(?:/|,|and)\s*)*N\d{1,2})\s*(?:stays |is |now |\(|:)?\s*\**(NOT A TEST|PROXY-PASS|PROXY-FAIL|MATH-CORRECTED|NOT EVIDENCE|PRIOR ART|INCONCLUSIVE|WITHDRAWN|DECIDED|PROVED|OPEN|SIM-FAIL)\b", ln):
                pre = ln[max(0, mm.start() - 4):mm.start()]
                post = ln[mm.end():mm.end() + 40]
                if "§1 " in pre or "§1" == pre.strip():
                    continue
                if re.match(r"[^→.;|]{0,30}→", post) or re.search(r"(was|Was|from)\s*\**\s*$", ln[max(0, mm.start() - 12):mm.start()]):
                    continue  # a recorded transition (old → new), not a current statement
                ids = re.findall(r"N\d{1,2}", mm.group(1))
                st = mm.group(2)
                for nid in ids:
                    nchecked += 1
                    if nid not in rows:
                        fails.append("N-status: %s:%d says %s %s but CLAIM_MAP has no %s" % (p, i, nid, st, nid)); nfail += 1
                    elif base(rows[nid]) != st:
                        fails.append("N-status: %s:%d says %s %s; CLAIM_MAP says %s" % (p, i, nid, st, rows[nid])); nfail += 1
    print("  N references checked: %d; mismatches: %d" % (nchecked, nfail))


    # ---------------------------------------------------------------- 4. process rules
    # Added in the lock pass (reviews/lock_2026-11-18/PROCESS.md, rules R1-R5):
    # each encodes an error type that recurred in the repo's history.
    print("\n== 4. Process rules (reviews/lock_2026-11-18/PROCESS.md)")
    pf = []

    def split_cells(ln):
        """GitHub splits a table row on every unescaped pipe, even inside backticks."""
        t = ln.strip()
        parts = re.split(r"(?<!\\)\|", t)
        if t.startswith("|"):
            parts = parts[1:]
        if t.endswith("|") and not t.endswith("\\|"):
            parts = parts[:-1]
        return parts

    # R1: a self-review must never be called independent.
    # Header marks of a self-review. Widened in the independent review of the lock
    # pass: "**Not independent**" mid-line and "This audit ... is not independent"
    # were missed, so the four lock-pass files were not treated as self-reviews.
    SELF_MARK = re.compile(r"(Independence:\s*\**\s*NOT independent|This pass is not independent|\(NOT independent\)|same executor that wrote|same executor, reread|^\s*\**Not independent\b|\*\*Not independent\b|\bThis (pass|audit|review|file|self-review|self-check)\b[^.]{0,40}\bis not independent\b)", re.I | re.M)
    self_reviews = []
    for p in sorted(glob.glob("reviews/**/*.md", recursive=True)):
        if SELF_MARK.search("\n".join(lines(p)[:15])):
            self_reviews.append(p)
    INDEP = re.compile(r"\bindependent(ly)?\b", re.I)
    INDEP_OK = re.compile(r"(\bnot\s+(an?\s+)?(fully\s+)?independent|\bno(n-?| )independent|self-review|self-check|was called|called it|isn't independent|same executor)", re.I)
    # words between "independent" and the citation that mean the self-review is
    # being contrasted with, not called, an independent review
    BETWEEN_OK = re.compile(r"(supersed|replac|correct|instead of|unlike|\bthan\b|earlier|re-?deriv|checked|reviewed)", re.I)
    pats = [(sr, re.compile(r"(?<![\w-])(?:reviews/)?" + re.escape(sr[len("reviews/"):]))) for sr in self_reviews]
    for p in MAINTAINED:
        for i, ln in enumerate(lines(p), 1):
            for s_ in sentences(ln):
                if not INDEP.search(s_) or INDEP_OK.search(s_):
                    continue
                for sr, rx in pats:
                    # Flag only when "independent" sits next to the citation
                    # ("the independent review `X`", "`X` is independent"), so a
                    # sentence that merely mentions an independent review and a
                    # self-review side by side is not a false positive.
                    def near(m_):
                        w = s_[max(0, m_.start() - 60):m_.start()]
                        k = [x for x in INDEP.finditer(w)]
                        return bool(k) and not BETWEEN_OK.search(w[k[-1].end():])
                    hit = any(near(m_) or
                              re.match(r"[`)\]]*\s*(\([^)]*\)\s*)?,?\s*((which|that)\s+)?(is|was|are|were)\s+(an?\s+)?(fully\s+)?independent", s_[m_.end():])
                              for m_ in rx.finditer(s_))
                    if hit:
                        pf.append("self-review-called-independent: %s:%d calls %s independent (its header says it is not)" % (p, i, sr))
    print("  self-reviews found by header: %d" % len(self_reviews))

    # R2: the CLAIM_MAP current tally must equal the rows.
    TB = ["NOT A TEST (not qualified; proxy: failed)", "NOT A TEST (qualification not established; proxy: passed)", "NOT A TEST (qualification not established; proxy: failed)", "NOT A TEST (qualification not established; proxy: INVALID)", "NOT A TEST", "PROXY-PASS", "PROXY-FAIL", "MATH-CORRECTED", "NOT EVIDENCE", "NOT APPLICABLE", "PRIOR ART", "SIM-INCONCLUSIVE", "INCONCLUSIVE", "WITHDRAWN", "DECIDED", "PROVED", "OPEN", "FALSE", "SIM-FAIL", "SIM-PASS"]
    counted, sec, unknown = {}, None, []
    for ln in cm.split("\n"):
        mm = re.match(r"^## ([A-Z])\.", ln)
        if mm:
            sec = mm.group(1)
        if ln.startswith("## Counts"):
            sec = None
        mm = re.match(r"^\| ([A-Z]{1,2}\d+[′']?[a-z]?) \|", ln)  # two-letter IDs: section O (CT/CL/CX); alias rows "CTk → X" are not counted
        if mm and sec:
            c = split_cells(ln)
            t = c[3].replace("*", "").strip() if len(c) > 3 else ""
            st = next((b for b in TB if t.startswith(b)), None) or next((b for b in TB if b in t), None)
            if not st:
                unknown.append(mm.group(1)); continue
            counted[st] = counted.get(st, 0) + 1
    mm = re.search(r"<!-- tally:begin -->(.*?)<!-- tally:end -->", cm, re.S)
    if not mm:
        pf.append("tally: CLAIM_MAP has no <!-- tally:begin --> block")
    else:
        stated, total = {}, None
        for ln in mm.group(1).split("\n"):
            c = [x.replace("*", "").strip() for x in split_cells(ln)] if ln.startswith("|") else []
            if len(c) == 2 and c[1].isdigit():
                if c[0] == "Total":
                    total = int(c[1])
                else:
                    stated[next((b for b in TB if c[0].startswith(b)), c[0])] = int(c[1])
        if stated != counted:
            pf.append("tally: CLAIM_MAP current tally %s differs from the rows %s" % (stated, counted))
        if total != sum(counted.values()):
            pf.append("tally: CLAIM_MAP tally total %s, rows %d" % (total, sum(counted.values())))
        print("  CLAIM_MAP rows counted: %d (tally total %s)" % (sum(counted.values()), total))
    for u in unknown:
        pf.append("tally: CLAIM_MAP row %s has no recognised status" % u)

    # R3: every table row in a maintained doc has as many cells as its header
    # (an unescaped pipe silently drops the last cell on GitHub).
    nt = 0
    for p in MAINTAINED:
        L = lines(p); fence = False; n = None
        for i, ln in enumerate(L, 1):
            if ln.lstrip().startswith("```"):
                fence = not fence; n = None; continue
            if fence or not ln.lstrip().startswith("|"):
                n = None; continue
            if n is None:
                if i < len(L) and re.match(r"^\s*\|?\s*:?-{3,}", L[i]):
                    n = len(split_cells(ln)); nt += 1
                continue
            if re.match(r"^\s*\|?\s*:?-{3,}", ln):
                continue
            k = len(split_cells(ln))
            if k != n:
                pf.append("table-cells: %s:%d has %d cells, header has %d (escape a pipe as \\|)" % (p, i, k, n))
    print("  tables checked: %d" % nt)

    # R4: no named GTAO relation is called a 'law' ('the sqrt N law'); use 'rule'.
    NAMED_LAW = re.compile(r"(√N|sqrt\(?N\)?|square[- ]root|trail[- ]fade|fade|shared[- ]memory|freeze[- ]or[- ]hold|read[- ]rate|three[- ]cost)\s+(scaling\s+)?laws?\b", re.I)
    # Published names that contain one of those words are prior art, not GTAO claims
    # (e.g. the inventory "square-root law", Maister 1976).
    NAMED_LAW_OK = re.compile(r"(inventor|Maister|pooling of stock|safety stock)", re.I)
    # R5: the repository is public since 18 Nov 2026; never call it private in the present tense.
    PRIVATE = re.compile(r"\b(repo|repository) (is|remains|stays) (still |currently )?private\b|\bthis private (repo|repository)\b", re.I)
    for p in MAINTAINED:
        for i, ln in enumerate(lines(p), 1):
            for s_ in sentences(ln):
                if NAMED_LAW.search(s_) and not NEG_LAW.search(s_) and not NAMED_LAW_OK.search(s_) and "WITHDRAWN" not in ln:
                    pf.append("law-named: %s:%d …%s…" % (p, i, s_.strip()[:160]))
                mp = PRIVATE.search(s_)
                if mp and not (s_[max(0, mp.start() - 1):mp.start()] in "\"“'" or "→" in s_):  # quoted old wording in a changelog is history
                    pf.append("stale-private: %s:%d …%s…" % (p, i, s_.strip()[:160]))
    for x in pf:
        print("  FAIL " + x)
    print("  process-rule FAILs: %d" % len(pf))
    fails.extend("FAIL " + x for x in pf)

    # ---------------------------------------------------------------- 5. core rules (THEORY v2.0)
    print("\n== 5. Core rules (THEORY v2.0)")
    cf = []
    # R6: THEORY Appendix C claim index <-> CLAIM_MAP section O, same base status and counted row
    sec_o = re.search(r"^## O\. .*?(?=^## )", cm, re.M | re.S)
    o_rows = {}
    if sec_o:
        for ln in sec_o.group(0).split("\n"):
            mo = re.match(r"^\| ((?:CT|CL|CX)\d+)(?: → ([A-Z]{1,2}\d+[′']?[a-z]?))? \|", ln)
            if mo:
                cells = [c.strip() for c in re.split(r"(?<!\\)\|", ln)]
                o_rows[mo.group(1)] = (base(cells[4]) if len(cells) > 4 else None, mo.group(2) or mo.group(1))
    app_c = re.search(r"^## Appendix C\..*", theory, re.M | re.S)
    c_rows = {}
    if app_c:
        for ln in app_c.group(0).split("\n"):
            mo = re.match(r"^\| ((?:CT|CL|CX)\d+) \|", ln)
            if mo:
                cells = [c.strip() for c in re.split(r"(?<!\\)\|", ln)]
                c_rows[mo.group(1)] = (base(cells[4]) if len(cells) > 4 else None, cells[5] if len(cells) > 5 else "")
    if not o_rows:
        cf.append("core-index: CLAIM_MAP has no section O rows")
    if not c_rows:
        cf.append("core-index: THEORY.md has no Appendix C claim index")
    for k, (st, counted) in sorted(c_rows.items()):
        if k not in o_rows:
            cf.append("core-index: THEORY Appendix C lists %s, which CLAIM_MAP section O lacks" % k); continue
        if st != o_rows[k][0]:
            cf.append("core-index: THEORY Appendix C says %s is %s; CLAIM_MAP section O says %s" % (k, st, o_rows[k][0]))
        if counted != o_rows[k][1]:
            cf.append("core-index: THEORY Appendix C counts %s as %s; CLAIM_MAP section O counts it as %s" % (k, counted, o_rows[k][1]))
    for k in sorted(set(o_rows) - set(c_rows)):
        cf.append("core-index: CLAIM_MAP section O has %s, missing from THEORY Appendix C" % k)
    print("  claim index: %d rows in THEORY Appendix C, %d in CLAIM_MAP section O" % (len(c_rows), len(o_rows)))
    # R7: length budgets
    def words(t):
        return len(re.findall(r"\S+", t))
    mi = re.search(r"^## Appendix A\.", theory, re.M)
    main_w = words(theory[:mi.start()] if mi else theory)
    readme_w = words(read("README.md"))
    BUDGET = {"THEORY.md main text (before Appendix A)": (main_w, 5500), "README.md": (readme_w, 900)}
    for name, (n, cap) in BUDGET.items():
        print("  %-4s %-42s %5d words (advisory reference %d)" % ("OK" if n <= cap else "WARN", name, n, cap))
        if n > cap:
            print("  WARN length: %s has %d words, over the advisory reference of %d (soft warning, not a failure)" % (name, n, cap))
    if not mi:
        cf.append("length: THEORY.md has no '## Appendix A.' heading to end the main text")
    # R8: the keep / hold / know table lives only in THEORY §1 and README
    SPINE = re.compile(r"^\|\s*\**(Keep|Hold|Know|Burn)\**\s*\(", re.M)
    for p in MAINTAINED:
        t = read(p)
        hits = [t.count("\n", 0, m_.start()) + 1 for m_ in SPINE.finditer(t)]
        if not hits:
            continue
        if p == "THEORY.md":
            s1 = re.search(r"^## 1\. .*?(?=^## )", t, re.M | re.S)
            lo = t.count("\n", 0, s1.start()) + 1 if s1 else 0
            hi = t.count("\n", 0, s1.end()) + 1 if s1 else -1
            out = [h for h in hits if not lo <= h <= hi]
            if out:
                cf.append("spine-duplicate: THEORY.md has the keep/hold/know table outside §1 (line %s)" % ",".join(map(str, out)))
        elif p != "README.md":
            cf.append("spine-duplicate: %s:%d repeats the keep/hold/know table (only THEORY §1 and README may carry it)" % (p, hits[0]))
        if len(hits) > 3:
            cf.append("spine-duplicate: %s carries the keep/hold/know table more than once" % p)
    for x in cf:
        print("  FAIL " + x)
    print("  core-rule FAILs: %d" % len(cf))
    fails.extend("FAIL " + x for x in cf)

    # Lean sources against formal/lean/AUDIT.json (tools/check_pending.py (b)); skipped without .git.
    from check_pending import check_lean as _lean_check, is_git_repo as _is_git
    if _is_git(ROOT):
        for x in _lean_check(ROOT):
            print("  FAIL " + x)
            fails.append("FAIL " + x)

    # Headline ledger vs front pages (tools/check_claims.py).
    from check_claims import check as _claims_check
    claim_fails = _claims_check(ROOT)
    print("\n== 6. Headline ledger")
    for x in claim_fails:
        print("  FAIL " + x)
        fails.append("FAIL " + x)
    print("  claims: %d FAIL(s)" % len(claim_fails))

    # ---------------------------------------------------------------- summary
    print("\n== Summary")
    print("FAIL: %d   INFO (frozen records): %d" % (len(fails), len(infos)))
    if "-v" in argv:
        for x in infos:
            print("  " + x)
    for x in fails:
        if not x.startswith("FAIL "):
            print("  FAIL " + x)
    print("RESULT:", "PASS" if not fails else "FAIL")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
