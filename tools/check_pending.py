#!/usr/bin/env python3
"""Pending-work check for the GTAO repository.

Added 24 November 2026 after reviewed Lean batches sat unmerged on the fork
(process/FAILURES.md, REPO-CURRENT-1). Since 25 November 2026 no page keeps the
main SHA or the open-PR list by hand (tools/check_fresh.py), so this check no
longer compares them.

Checks
  (b) Lean: formal/lean/AUDIT.json records the AxiomAudit count and a sha256 of
      the Lean sources; the sources must still hash to it (otherwise rerun
      tools/check_lean.sh in /tmp/gtao-lean and --record-audit N).
  own row (--pr N): the PR's own README.md row is no longer "In flight".
  summary (--body-file F): the PR body passes check_claims.summary_fails.
  (c) live, via gh: an open PR whose latest independent review says
      "Blockers remaining: 0" and is older than PENDING_HOURS, unless parked in
      the parked-PR table in process/PROCESS.md §4; and closing keywords in open upstream PRs. Only findings
      about the PR named by --pr fail; the rest print as WARN (tools/brief.py
      lists them too). A review is found by content: a PR whose changes are all
      added review files, one of whose text has a "Blockers remaining: N" line,
      is a review record, and so is a comment with that line.

Before comparing, the run does `git fetch origin main`. If it cannot fetch, or
has no network or no gh, the result is PARTIAL, never PASS.

Run from the repo root:
  python3 tools/check_pending.py [--pr N] [--body-file F]
  python3 tools/check_pending.py --offline    # (b) and own row only: PARTIAL
  python3 tools/check_pending.py --strict     # PARTIAL exits 2
  python3 tools/check_pending.py --closing-keywords [RANGE] [--pr N] [--body-file F]
  python3 tools/check_pending.py --record-audit 1370
Exit 0 = PASS (or PARTIAL because --offline was asked for), 1 = FAIL, 2 = PARTIAL that was not
asked for. `--allow-partial` makes that exit 0 again; the RESULT line still says PARTIAL.
"""
from __future__ import annotations

import base64
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

UPSTREAM = "Chad-Mitchell/theory-of-adaptive-organization"
FORK = "mitchell-moving/theory-of-adaptive-organization"
PENDING_HOURS = 24
AUDIT_FILE = os.path.join("formal", "lean", "AUDIT.json")

BLOCKERS_RE = re.compile(r"Blockers remaining:?\**\s*\**(\d+)", re.I)
REVIEWED_HEAD_RE = re.compile(r"(?:Reviewed head|^Head|^Re-check of head)\s+`([0-9a-f]{7,40})`", re.I | re.M)


def repo_root():
    return os.path.dirname(HERE)


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)


def is_git_repo(root):
    """True inside a git work tree (moved here from the retired pointer check, 25 November 2026)."""
    try:
        return git(root, "rev-parse", "--is-inside-work-tree").stdout.strip() == "true"
    except OSError:
        return False


# ------------------------------------------------------------------ own row
def own_row_check(root, pr):
    """A PR moves its own README.md row in the same PR: fail if a row naming upstream #pr is still 'In flight'."""
    path = os.path.join(root, "README.md")
    if pr is None or not os.path.exists(path):
        return []
    rx = re.compile(r"(?:\bPR\s+|\bupstream\s+(?:draft\s+)?(?:PR\s+)?|/pull/)#?%d\b" % pr, re.I)
    fails = []
    for ln, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if line.startswith("|") and rx.search(line) and re.search(r"\bin flight\b", line, re.I):
            fails.append("own row: README.md:%d still marks the row for #%d 'In flight'; move it in this PR as if "
                         "it were the one merged" % (ln, pr))
    return fails


# ------------------------------------------------------------------ (b)
def lean_source_files(root):
    lean = os.path.join(root, "formal", "lean")
    files = [os.path.join(lean, "GTAO.lean")]
    # Recursive: modules in subfolders (GTAO/Rnd/**) are sources too. With no subfolder this is the old list.
    files += sorted(glob.glob(os.path.join(lean, "GTAO", "**", "*.lean"), recursive=True))
    for extra in ("scripts/AxiomAudit.lean", "lakefile.toml", "lake-manifest.json", "lean-toolchain"):
        files.append(os.path.join(lean, extra))
    return [f for f in files if os.path.exists(f)]


def lean_sources_sha256(root):
    h = hashlib.sha256()
    for f in lean_source_files(root):
        rel = os.path.relpath(f, root).replace(os.sep, "/")
        h.update(rel.encode() + b"\0")
        h.update(open(f, "rb").read())
        h.update(b"\0")
    return h.hexdigest()


def check_lean(root):
    lean_dir = os.path.join(root, "formal", "lean")
    if not os.path.exists(os.path.join(lean_dir, "GTAO.lean")):
        return []
    path = os.path.join(root, AUDIT_FILE)
    if not os.path.exists(path):
        return ["lean: %s is missing; run tools/check_lean.sh, then --record-audit N" % AUDIT_FILE]
    audit = json.load(open(path, encoding="utf-8"))
    fails = []
    now = lean_sources_sha256(root)
    if audit.get("sources_sha256") != now:
        fails.append(
            "lean: Lean sources changed since the recorded audit (%s); rerun tools/check_lean.sh in "
            "/tmp/gtao-lean and record the count with: python3 tools/check_pending.py --record-audit N"
            % audit.get("audited_at", "?"))
    return fails


def record_audit(root, count, commit=None):
    data = {
        "audit_count": int(count),
        "sources_sha256": lean_sources_sha256(root),
        "audited_at": commit or (git(root, "rev-parse", "--short", "HEAD").stdout.strip() or "?"),
        "how": "tools/check_lean.sh in /tmp/gtao-lean; AxiomAudit 'N GTAO declarations'",
    }
    with open(os.path.join(root, AUDIT_FILE), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")
    return data


# ------------------------------------------------------------------ parked
PARKED_FILE = os.path.join("process", "PROCESS.md")  # parked-PR table, section 4
PARKED_ROW_RE = re.compile(r"^\|\s*(upstream|fork)#(\d+)\s*\|(.*)\|\s*$", re.I)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def read_parked(root):
    """({('upstream'|'fork', n): reason}, [problems]) from the parked-PR table in process/PROCESS.md."""
    path = os.path.join(root, PARKED_FILE)
    parked, problems = {}, []
    if not os.path.exists(path):
        return parked, problems
    for ln, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        m = PARKED_ROW_RE.match(line.strip())
        if not m:
            continue
        cells = [c.strip() for c in m.group(3).split("|")]
        if len(cells) < 3 or not cells[0] or not DATE_RE.match(cells[1]) or not cells[2]:
            problems.append("pending: %s:%d needs reason | YYYY-MM-DD | decided by" % (PARKED_FILE, ln))
            continue
        parked[(m.group(1).lower(), int(m.group(2)))] = cells[0]
    return parked, problems


# ------------------------------------------------------------------ (c)
class Offline(Exception):
    pass


def gh_api(path):
    if not shutil.which("gh"):
        raise Offline("gh not installed")
    try:
        r = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github+json", path],
                           capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        raise Offline("gh timed out")
    if r.returncode != 0:
        raise Offline((r.stderr or r.stdout).strip()[:200])
    return json.loads(r.stdout or "null")


def paged(api, path):
    """All items of a list endpoint: follow page=N until a short page."""
    out, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        chunk = api("%s%sper_page=100&page=%d" % (path, sep, page)) or []
        out.extend(chunk)
        if len(chunk) < 100:
            return out
        page += 1


def open_pr_heads(api=gh_api):
    """{head SHA: 'upstream#N' or 'fork#N'} for every open PR in both repos (the live PR list). Raises Offline."""
    out = {}
    for label, repo in (("upstream", UPSTREAM), ("fork", FORK)):
        for p in paged(api, "/repos/%s/pulls?state=open" % repo):
            out[p["head"]["sha"]] = "%s#%d" % (label, p["number"])
    return out


def parse_time(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


HEX_TOKEN_RE = re.compile(r"`([0-9a-f]{7,40})`")


FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
NEGATOR_RE = re.compile(r"\b(not|never|no|until|unless|if|once|when|whether|without|before|should|must|would|will|"
                        r"require[sd]?|expect(?:ed)?|wait(?:s|ing)?|need(?:s|ed)?|until)\b", re.I)


def _inside_quote(head):
    """True when the text before the phrase leaves a quote open on this line."""
    return (head.count("`") % 2 == 1 or head.count('"') % 2 == 1
            or head.count("\u201c") > head.count("\u201d") or head.count("\u2018") > head.count("\u2019"))


def blockers_found(text):
    """[int] of 'Blockers remaining: N' that a reviewer wrote as a result.

    Not counted: text in code fences or block quotes, a phrase that follows a quote mark or a
    backtick on the same line (it is quoted), and a phrase that follows a negator within 50
    characters of the same line ('not Blockers remaining: 0', 'wait for Blockers remaining: 0').
    """
    text = FENCE_RE.sub(" ", text or "")
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith(">"):
            continue
        for m in BLOCKERS_RE.finditer(line):
            head = line[:m.start()]
            if _inside_quote(head) or NEGATOR_RE.search(head[-50:]):
                continue
            out.append(int(m.group(1)))
    return out


def review_result(text):
    """(blockers, [reviewed SHAs]) from the last 'Blockers remaining' in a review text."""
    found = blockers_found(text)
    if not found:
        return None, []
    m = REVIEWED_HEAD_RE.search(text)
    if m:
        shas = [m.group(1)]
    else:  # no explicit "Reviewed head": the first backticked hash of the opening
        shas = HEX_TOKEN_RE.findall((text or "")[:400])[:1]
    return found[-1], shas


def _owner(pr, side):
    r = pr[side].get("repo")
    return r["owner"]["login"] if r else None


def collect(api=gh_api, now=None, hours=PENDING_HOURS, parked=None, is_merged=None):
    """(pending, open_upstream) for both repos.

    pending: strings for open work PRs whose latest independent review
    says 0 blockers and is older than `hours` and which are not parked.
    open_upstream: the open upstream PR dicts.
    is_merged(sha) -> True when that commit is already in main (a fork PR
    whose work landed through another PR is not pending).
    """
    now = now or datetime.now(timezone.utc)
    parked = parked or {}
    prs = {}
    for label, repo in (("upstream", UPSTREAM), ("fork", FORK)):
        for p in paged(api, "/repos/%s/pulls?state=open" % repo):
            prs[(label, p["number"])] = (repo, p)
    # 1. classify by content: a PR that adds a file with a "Blockers remaining" line is a review record
    review_records, work = [], {}
    for key, (repo, p) in prs.items():
        found, other = None, False
        for f in paged(api, "/repos/%s/pulls/%d/files" % (repo, p["number"])):
            name = f["filename"]
            reviewish = re.search(r"review", name, re.I) is not None
            textual = name.lower().endswith((".md", ".txt")) and f.get("status") != "removed"
            # a record may add or MODIFY a file, and its file name need not say "review": read any changed
            # text file that is review-named or whose diff mentions "Blockers remaining"
            if textual and (reviewish or "Blockers remaining" in (f.get("patch") or "")):
                hrepo = p["head"]["repo"]["full_name"] if p["head"]["repo"] else repo
                c = api("/repos/%s/contents/%s?ref=%s" % (hrepo, name, p["head"]["sha"])) or {}
                text = base64.b64decode(c.get("content", "")).decode("utf-8", "replace")
                b, shas = review_result(text)
                if b is not None:
                    found = (b, shas, text)
                    continue
            if not reviewish:
                other = True  # a review record changes only review files (and the file that holds the result)
        if found and not other:
            review_records.append((key, p, found))
        else:
            work[key] = (repo, p)
    # 2. reviews: records matched to work PRs, plus comments on work PRs
    seen = {k: [] for k in work}  # key -> [(time, where, blockers, shas)]
    commits = {}

    def commit_shas(k):
        if k not in commits:
            repo, p = work[k]
            commits[k] = [c["sha"] for c in paged(api, "/repos/%s/pulls/%d/commits" % (repo, p["number"]))]
        return commits[k]

    for key, rp, (b, shas, text) in review_records:
        by_branch = [k for k, (repo, wp) in work.items()
                     if rp["base"]["ref"] == wp["head"]["ref"]
                     and rp["base"]["repo"]["owner"]["login"] == _owner(wp, "head")
                     or ("`%s`" % wp["head"]["ref"]) in text]
        # the reviewed head's commit is the fallback (a review based on main)
        targets = by_branch or [k for k in work if any(c.startswith(x[:7]) for x in shas for c in commit_shas(k))]
        for k in targets:
            seen[k].append((parse_time(rp["created_at"]), "%s#%d" % (key[0], key[1]), b, shas))
    for k, (repo, wp) in work.items():
        for c in paged(api, "/repos/%s/issues/%d/comments" % (repo, wp["number"])):
            b, shas = review_result(c.get("body", ""))
            if b is not None:
                seen[k].append((parse_time(c["created_at"]), c.get("html_url", "comment"), b, shas))
    out = []
    for k, revs in seen.items():
        if not revs or k in parked:
            continue
        t, where, b, shas = max(revs, key=lambda r: r[0])  # the latest review governs
        if b != 0 or now - t <= timedelta(hours=hours):
            continue
        wp = work[k][1]
        cur = wp["head"]["sha"]
        if is_merged and is_merged(cur):
            continue
        stale = shas and not any(cur.startswith(x[:7]) for x in shas)
        out.append("%s#%d (%s) head %s: latest review %s says 0 blockers, %.0f h ago%s" % (
            k[0], k[1], wp["title"][:60], cur[:7], where, (now - t).total_seconds() / 3600,
            "; head moved since that review" if stale else ""))
    open_upstream = [p for (label, n), (repo, p) in prs.items() if label == "upstream"]
    return sorted(out), open_upstream


# ------------------------------------------------------------------ closing keywords
# GitHub closes the referenced issue or PR when a commit message or PR body that reaches the default branch
# says close/fix/resolve (any tense) followed by #N. On 24 November 2026 a commit headline "fix #253 ..." in
# #270 closed an unrelated open PR at merge (process/FAILURES.md, REPO-CURRENT-3).
CLOSING_RE = re.compile(
    r"\b(close[sd]?|fix(?:e[sd])?|resolve[sd]?)\b:?\s*"
    r"(?:(?P<repo>[\w.-]+/[\w.-]+)#(?P<n1>\d+)|#(?P<n2>\d+)|https://github\.com/(?P<urepo>[\w.-]+/[\w.-]+)/(?:issues|pull)/(?P<n3>\d+))",
    re.I)
CLOSES_OK_RE = re.compile(r"closes-ok:\s*#(\d+)", re.I)


def closing_refs(text, self_number=None, self_repo=UPSTREAM):
    """[(keyword, repo, number)] for closing keywords that name something other than the PR itself,
    minus any number the text allows with `closes-ok: #N <reason>`.

    Quoted or fenced keywords are skipped: GitHub does not close on a keyword inside quotes,
    backticks, a code fence or a block quote.
    """
    allowed = {int(x) for x in CLOSES_OK_RE.findall(text or "")}
    body = FENCE_RE.sub(" ", text or "")
    out = []
    for line in body.splitlines():
        if line.lstrip().startswith(">"):
            continue
        for m in CLOSING_RE.finditer(line):
            if _inside_quote(line[:m.start()]):
                continue
            repo = m.group("repo") or m.group("urepo") or self_repo
            n = int(m.group("n1") or m.group("n2") or m.group("n3"))
            if n in allowed or (n == self_number and repo.lower() == self_repo.lower()):
                continue
            out.append((m.group(1).lower(), repo, n))
    return out


def check_closing_texts(items, self_number=None):
    """items: [(where, text)] -> failure strings."""
    fails = []
    for where, text in items:
        for kw, repo, n in closing_refs(text, self_number):
            fails.append("closing keyword '%s %s#%d' in %s would close another PR or issue when merged; reword it "
                         "(say 'see #%d') or, if you mean it, add 'closes-ok: #%d <reason>'" % (kw, repo, n, where, n, n))
    return fails


def local_closing_check(root, rev_range, self_number=None, body_file=None):
    """Pre-merge check on a local branch: commit messages in rev_range (default origin/main..HEAD) and an
    optional PR body file."""
    r = git(root, "log", "--format=%H%x1f%B%x1e", rev_range)
    if r.returncode != 0:
        return ["closing keywords: git log %s failed: %s" % (rev_range, r.stderr.strip()[:120])]
    items = []
    for rec in r.stdout.split("\x1e"):
        rec = rec.strip("\n")
        if "\x1f" in rec:
            sha, msg = rec.split("\x1f", 1)
            items.append(("commit %s" % sha[:7], msg))
    if body_file:
        items.append(("the PR body (%s)" % body_file, open(body_file, encoding="utf-8").read()))
    return check_closing_texts(items, self_number)


def check_closing_online(api=gh_api):
    """Failure strings for every open upstream PR: title, body and commit messages."""
    fails = []
    for p in paged(api, "/repos/%s/pulls?state=open" % UPSTREAM):
        n = p["number"]
        items = [("#%d title/body" % n, "%s\n%s" % (p.get("title") or "", p.get("body") or ""))]
        for c in paged(api, "/repos/%s/pulls/%d/commits" % (UPSTREAM, n)):
            items.append(("#%d commit %s" % (n, c["sha"][:7]), (c.get("commit") or {}).get("message", "")))
        fails += check_closing_texts(items, n)
    return fails


def fetch_origin(root):
    """None if origin/main was refreshed, else the reason it was not."""
    if not is_git_repo(root):
        return None
    try:
        r = git(root, "fetch", "-q", "origin", "main")
    except Exception as e:  # pragma: no cover
        return str(e)
    return None if r.returncode == 0 else ("git fetch origin main failed: " + (r.stderr.strip()[:120] or "?"))


def in_main(root, sha):
    """True when the commit is an ancestor of origin/main (False if unknown locally)."""
    if not is_git_repo(root):
        return False
    r = git(root, "merge-base", "--is-ancestor", sha, "refs/remotes/origin/main")
    return r.returncode == 0


def _about(finding, pr):
    return pr is not None and finding.startswith("upstream#%d " % pr)


def check_online(root, api=gh_api, now=None, pr=None):
    """(fails, warns, partial_reasons) for part (c) and closing keywords.

    Only findings about the PR being merged (--pr N) fail. Other open PRs' findings are warnings: a stale
    PR elsewhere must not make main or an unrelated PR fail (25 November 2026; tools/brief.py shows them)."""
    parked, problems = read_parked(root)
    try:
        pending, _open = collect(api, now=now, parked=parked, is_merged=lambda sha: in_main(root, sha))
    except Offline as e:
        return problems, [], ["open-PR check not run (%s)" % e]
    except Exception as e:
        return problems, [], ["open-PR check not run (%s: %s)" % (type(e).__name__, e)]
    fails, warns = list(problems), []
    for x in pending:
        (fails if _about(x, pr) else warns).append("pending: reviewed but unmerged > %dh: %s" % (PENDING_HOURS, x))
    try:
        for x in check_closing_online(api):
            (fails if pr is not None and x.startswith("closing keyword") and (" in #%d " % pr) in x else warns).append("closing: " + x)
    except Exception as e:
        return fails, warns, ["closing-keyword check not run (%s: %s)" % (type(e).__name__, e)]
    return fails, warns, []


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    root = repo_root()
    if "--record-audit" in argv:
        n = argv[argv.index("--record-audit") + 1]
        d = record_audit(root, n)
        print("recorded %s" % json.dumps(d))
        return 0
    if "--closing-keywords" in argv:
        i = argv.index("--closing-keywords")
        rng = argv[i + 1] if i + 1 < len(argv) and not argv[i + 1].startswith("--") else "origin/main..HEAD"
        pr = int(argv[argv.index("--pr") + 1]) if "--pr" in argv else None
        body = argv[argv.index("--body-file") + 1] if "--body-file" in argv else None
        fl = local_closing_check(root, rng, pr, body) + own_row_check(root, pr)
        if body:
            from check_claims import summary_fails
            fl += ["summary: " + x for x in summary_fails(open(body, encoding="utf-8").read(), root, "the PR body")]
        for f in fl:
            print("  FAIL " + f)
        print("RESULT:", "FAIL" if fl else "PASS")
        return 1 if fl else 0
    pr = int(argv[argv.index("--pr") + 1]) if "--pr" in argv else None
    body = argv[argv.index("--body-file") + 1] if "--body-file" in argv else None
    fails, warns, partial = [], [], []
    online = "--offline" not in argv
    if online:
        err = fetch_origin(root)
        if err:
            partial.append(err)
    else:
        partial.append("open-PR check not run (--offline)")
    fails += check_lean(root)
    fails += own_row_check(root, pr)
    if body:
        from check_claims import summary_fails
        fails += ["summary: " + x for x in summary_fails(open(body, encoding="utf-8").read(), root, "the PR body")]
    if online:
        f, w, p = check_online(root, pr=pr)
        fails += f
        warns += w
        partial += p
    for w in warns:
        print("  WARN " + w)
    for w in partial:
        print("  PARTIAL " + w)
    for f in fails:
        print("  FAIL " + f)
    if fails:
        print("RESULT: FAIL")
        return 1
    if partial:
        print("RESULT: PARTIAL (not everything was checked)")
        asked = not online                       # --offline: the caller asked for the offline subset
        if "--strict" in argv:
            return 2
        return 0 if asked or "--allow-partial" in argv else 2
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
