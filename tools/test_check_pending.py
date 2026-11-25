#!/usr/bin/env python3
"""Tests for tools/check_pending.py (offline; the GitHub API is faked).

Run:  python3 -m pytest -q tools/test_check_pending.py
"""
from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_pending as cp  # noqa: E402

NOW = datetime(2026, 11, 26, 12, 0, tzinfo=timezone.utc)


def ts(hours_ago):
    return (NOW - timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- (b) Lean
def _lean_tree(tmp_path, status_count=10, record=10):
    root = tmp_path / "r"
    (root / "formal" / "lean" / "GTAO").mkdir(parents=True)
    (root / "formal" / "lean" / "GTAO.lean").write_text("import GTAO.A\n")
    (root / "formal" / "lean" / "GTAO" / "A.lean").write_text("theorem t : True := trivial\n")
    (root / "STATUS.md").write_text("machine-checks **%d declarations** (AxiomAudit)\n" % status_count)
    if record is not None:
        cp.record_audit(str(root), record, commit="abc1234")
    return root


def test_real_repo_lean_count_matches_audit():
    assert cp.check_lean(ROOT) == []


def test_lean_count_match_passes(tmp_path):
    root = _lean_tree(tmp_path)
    assert cp.check_lean(str(root)) == []


def test_status_count_mismatch_fails(tmp_path):
    # The 24 November miss: STATUS kept 757 after the audit count moved.
    root = _lean_tree(tmp_path, status_count=757, record=1185)
    fails = cp.check_lean(str(root))
    assert any("757" in f and "1185" in f for f in fails)


def test_lean_source_change_without_new_audit_fails(tmp_path):
    root = _lean_tree(tmp_path)
    (root / "formal" / "lean" / "GTAO" / "B.lean").write_text("theorem u : True := trivial\n")
    fails = cp.check_lean(str(root))
    assert any("sources changed" in f for f in fails)


def test_missing_audit_file_fails(tmp_path):
    root = _lean_tree(tmp_path, record=None)
    assert any("AUDIT.json is missing" in f for f in cp.check_lean(str(root)))


def test_status_without_lean_total_fails(tmp_path):
    root = _lean_tree(tmp_path)
    (root / "STATUS.md").write_text("no total here\n")
    assert any("no '**N declarations**'" in f for f in cp.check_lean(str(root)))


def test_status_count_parses_commas():
    assert cp.status_lean_count("checks **1,185 declarations** today") == 1185


# ---------------------------------------------------------------- (a) OPEN_WORK
def _git(repo, *a):
    e = dict(os.environ, GIT_AUTHOR_NAME="T", GIT_AUTHOR_EMAIL="t@e", GIT_COMMITTER_NAME="T", GIT_COMMITTER_EMAIL="t@e")
    r = subprocess.run(["git", *a], cwd=repo, capture_output=True, text=True, env=e)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


def _repo(tmp_path, n):
    repo = str(tmp_path / "g")
    os.makedirs(repo)
    _git(repo, "init", "-b", "main")
    shas = []
    for i in range(n):
        open(os.path.join(repo, "f%d" % i), "w").write(str(i))
        _git(repo, "add", ".")
        _git(repo, "commit", "-m", str(i))
        shas.append(_git(repo, "rev-parse", "HEAD"))
    return repo, shas


def test_open_work_pointer_in_window_passes(tmp_path):
    repo, shas = _repo(tmp_path, 4)
    open(os.path.join(repo, "STATUS.md"), "w").write("`main` is `%s`\n" % shas[-1][:7])
    open(os.path.join(repo, "OPEN_WORK.md"), "w").write("# OW\n\n**As of:** x, on `main` `%s` (PR #1).\n" % shas[0][:7])
    assert cp.check_pointers(repo) == []


def test_open_work_pointer_out_of_window_fails(tmp_path):
    repo, shas = _repo(tmp_path, cp.OPEN_WORK_WINDOW + 2)
    open(os.path.join(repo, "STATUS.md"), "w").write("`main` is `%s`\n" % shas[-1][:7])
    open(os.path.join(repo, "OPEN_WORK.md"), "w").write("# OW\n\n**As of:** x, on `main` `%s`.\n" % shas[0][:7])
    fails = cp.check_pointers(repo)
    assert any("OPEN_WORK.md header" in f for f in fails)


# ---------------------------------------------------------------- (c) pending
class FakeGH:
    """A tiny GitHub: open PRs, their files, commits and comments, with real paging."""

    def __init__(self):
        self.pulls = {cp.UPSTREAM: [], cp.FORK: []}
        self.files, self.commits, self.comments, self.contents = {}, {}, {}, {}
        self.calls = 0

    def pr(self, repo, n, title, head_ref, head_sha, base_ref="main", age_h=30, owner=None, draft=False):
        owner = owner or repo.split("/")[0]
        p = {"number": n, "title": title, "created_at": ts(age_h), "draft": draft,
             "head": {"ref": head_ref, "sha": head_sha.ljust(40, "0"),
                      "repo": {"owner": {"login": owner}, "full_name": "%s/x" % owner}},
             "base": {"ref": base_ref, "repo": {"owner": {"login": repo.split("/")[0]}}}}
        self.pulls[repo].append(p)
        self.commits[(repo, n)] = [{"sha": head_sha.ljust(40, "0")}]
        return p

    def review_file(self, repo, n, text, name="theory/reviews/REVIEW.md"):
        self.files[(repo, n)] = [{"filename": name, "status": "added"}]
        p = [x for x in self.pulls[repo] if x["number"] == n][0]
        self.contents[("%s/x" % p["head"]["repo"]["owner"]["login"], name, p["head"]["sha"])] = text

    def __call__(self, path):
        self.calls += 1
        base, _, q = path.partition("?")
        qs = dict(x.split("=", 1) for x in q.split("&") if "=" in x)
        page, per = int(qs.get("page", 1)), int(qs.get("per_page", 30))

        def cut(items):
            return items[(page - 1) * per: page * per]
        parts = base.strip("/").split("/")
        if parts[3] == "pulls" and len(parts) == 4:
            return cut(self.pulls["/".join(parts[1:3])])
        repo = "/".join(parts[1:3])
        if parts[3] == "pulls" and parts[5] == "files":
            return cut(self.files.get((repo, int(parts[4])), []))
        if parts[3] == "pulls" and parts[5] == "commits":
            return cut(self.commits.get((repo, int(parts[4])), []))
        if parts[3] == "issues":
            return cut(self.comments.get((repo, int(parts[4])), []))
        if parts[3] == "contents":
            name = "/".join(parts[4:])
            t = self.contents[(repo, name, qs["ref"])]
            return {"content": base64.b64encode(t.encode()).decode()}
        raise AssertionError(path)


def pass_text(head="caea9c0", n=0):
    return "Reviewed head `%s` on x.\n\nBlockers remaining: %d\n" % (head, n)


def lean_pair(g, work_title="Lean batch 2", rev_title="Independent review of Lean batch 2", rev_base="batch2",
              rev_age=30, text=None):
    g.pr(cp.FORK, 30, work_title, "batch2", "6663d0e", "batch1")
    g.pr(cp.FORK, 32, rev_title, "batch2-review", "295c968", rev_base, age_h=rev_age)
    g.review_file(cp.FORK, 32, text or pass_text())
    return g


def test_reviewed_unmerged_over_24h_is_listed():
    g = lean_pair(FakeGH())
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1 and "fork#30" in items[0] and "head moved" in items[0]


def test_reviewed_under_24h_is_not_listed():
    g = lean_pair(FakeGH(), rev_age=3)
    assert cp.collect(g, now=NOW)[0] == []


def test_review_with_blockers_is_not_listed():
    g = lean_pair(FakeGH(), text=pass_text(n=2))
    assert cp.collect(g, now=NOW)[0] == []


def test_work_pr_with_review_in_its_title_is_still_reported():
    # Reproduces B-272-2 (1): a title heuristic would call this a review and hide it.
    g = lean_pair(FakeGH(), work_title="Address review comments on Lean batch 2")
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1 and "fork#30" in items[0]


def test_review_pr_without_the_word_review_in_its_title_counts():
    # B-272-2 (2)
    g = lean_pair(FakeGH(), rev_title="Second look at batch 2")
    assert len(cp.collect(g, now=NOW)[0]) == 1


def test_review_based_on_main_matches_by_reviewed_head():
    # B-272-2 (3): fork #24 is based on main, not on the work branch.
    g = lean_pair(FakeGH(), rev_base="main", text=pass_text("6663d0e"))
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1 and "fork#30" in items[0] and "head moved" not in items[0]


def test_review_based_on_main_matches_by_branch_name():
    g = lean_pair(FakeGH(), rev_base="main", text="See `batch2`.\nBlockers remaining: 0\n")
    assert len(cp.collect(g, now=NOW)[0]) == 1


def test_unrelated_review_based_on_main_does_not_match():
    g = lean_pair(FakeGH(), rev_base="main", text=pass_text("1234567"))
    assert cp.collect(g, now=NOW)[0] == []


def test_work_pr_that_adds_a_review_file_among_others_is_work():
    g = FakeGH()
    g.pr(cp.FORK, 5, "T99 note", "t99", "aaaaaaa")
    g.files[(cp.FORK, 5)] = [{"filename": "theory/T99.md", "status": "added"},
                             {"filename": "theory/reviews/R.md", "status": "added"}]
    g.contents[("mitchell-moving/x", "theory/reviews/R.md", "aaaaaaa".ljust(40, "0"))] = pass_text("aaaaaaa")
    items, _ = cp.collect(g, now=NOW)
    assert items == []  # no review record, no comment: nothing is reviewed


def test_latest_review_governs():
    g = lean_pair(FakeGH(), rev_age=40)
    g.comments[(cp.FORK, 30)] = [{"body": "Blockers remaining: 1", "created_at": ts(26)}]
    assert cp.collect(g, now=NOW)[0] == []


def test_passing_review_comment_counts():
    g = FakeGH()
    g.pr(cp.FORK, 30, "Lean batch 2", "batch2", "6663d0e", "batch1")
    g.comments[(cp.FORK, 30)] = [{"body": "Head `6663d0e`\nBlockers remaining: 0", "created_at": ts(25), "html_url": "u"}]
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1 and "head moved" not in items[0]


def test_comments_are_paginated():
    # B-272-2 (4): the passing review is comment 151; the first page holds 100 blockers.
    g = FakeGH()
    g.pr(cp.FORK, 30, "Lean batch 2", "batch2", "6663d0e", "batch1")
    old = [{"body": "Blockers remaining: 3", "created_at": ts(100 - i * 0.1)} for i in range(150)]
    g.comments[(cp.FORK, 30)] = old + [{"body": "Blockers remaining: 0", "created_at": ts(26), "html_url": "late"}]
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1


def test_open_prs_are_paginated():
    g = FakeGH()
    for i in range(130):
        g.pr(cp.UPSTREAM, i + 1, "w%d" % i, "b%d" % i, "%07x" % i)
    _, open_up = cp.collect(g, now=NOW)
    assert len(open_up) == 130


def test_parked_pr_is_exempt(tmp_path):
    g = lean_pair(FakeGH())
    items, _ = cp.collect(g, now=NOW, parked={("fork", 30): "parked"})
    assert items == []


def _parked(tmp_path, body):
    root = tmp_path / "p"
    (root / "process").mkdir(parents=True)
    (root / "process" / "PARKED.md").write_text("# Parked\n\n| PR | reason | date | decided by |\n|---|---|---|---|\n" + body)
    return str(root)


def test_parked_file_parses(tmp_path):
    root = _parked(tmp_path, "| fork#16 | torus parked pending a stake test | 2026-11-24 | Chad |\n")
    parked, problems = cp.read_parked(root)
    assert parked == {("fork", 16): "torus parked pending a stake test"} and problems == []


def test_parked_row_without_date_or_decider_fails(tmp_path):
    root = _parked(tmp_path, "| fork#16 | because | soon |  |\n")
    parked, problems = cp.read_parked(root)
    assert parked == {} and problems and "PARKED.md" in problems[0]


def _status(tmp_path, text):
    root = tmp_path / "s"
    root.mkdir(exist_ok=True)
    (root / "STATUS.md").write_text(text)
    return str(root)


def test_status_list_matches_live_list(tmp_path):
    root = _status(tmp_path, "x. Open upstream PRs not yet merged: #253 (T72) and #257 (T75). Earlier merge logs are in history.\n")
    live = [{"number": 253, "title": "a", "created_at": ts(30)}, {"number": 257, "title": "b", "created_at": ts(30)}]
    assert cp.check_status_list(root, live, {}, now=NOW) == []


def test_status_list_missing_an_old_open_pr_fails(tmp_path):
    root = _status(tmp_path, "Open upstream PRs not yet merged: #253 (T72).\n")
    live = [{"number": 253, "title": "a", "created_at": ts(30)}, {"number": 263, "title": "gate", "created_at": ts(30)}]
    fails = cp.check_status_list(root, live, {}, now=NOW)
    assert len(fails) == 1 and "#263" in fails[0]


def test_status_list_ignores_new_or_parked_prs(tmp_path):
    root = _status(tmp_path, "Open upstream PRs not yet merged: #253 (T72).\n")
    live = [{"number": 253, "title": "a", "created_at": ts(30)}, {"number": 270, "title": "new", "created_at": ts(2)},
            {"number": 263, "title": "gate", "created_at": ts(30)}]
    assert cp.check_status_list(root, live, {("upstream", 263): "r"}, now=NOW) == []


def test_status_list_naming_a_closed_pr_fails(tmp_path):
    # The 24 November #253 error in reverse: STATUS names a PR that is no longer open.
    root = _status(tmp_path, "Open upstream PRs not yet merged: #253 (T72) and #999 (gone).\n")
    live = [{"number": 253, "title": "a", "created_at": ts(30)}]
    fails = cp.check_status_list(root, live, {}, now=NOW)
    assert len(fails) == 1 and "#999" in fails[0]


# ---------------------------------------------------------------- result line
def _run_main(monkeypatch, capsys, argv, online=None, fetch=None):
    monkeypatch.setattr(cp, "fetch_origin", lambda root: fetch)
    monkeypatch.setattr(cp, "check_pointers", lambda root: [])
    monkeypatch.setattr(cp, "check_lean", lambda root: [])
    monkeypatch.setattr(cp, "check_online", online or (lambda root: ([], [])))
    rc = cp.main(argv)
    return rc, capsys.readouterr().out


def test_offline_flag_never_prints_pass(monkeypatch, capsys):
    rc, out = _run_main(monkeypatch, capsys, ["--offline"])
    assert "RESULT: PARTIAL" in out and "PASS" not in out and rc == 0


def test_strict_makes_partial_exit_2(monkeypatch, capsys):
    rc, out = _run_main(monkeypatch, capsys, ["--offline", "--strict"])
    assert rc == 2


def test_no_network_is_partial_not_pass(monkeypatch, capsys):
    rc, out = _run_main(monkeypatch, capsys, [], online=lambda root: ([], ["open-PR check not run (no network)"]))
    assert "RESULT: PARTIAL" in out and "RESULT: PASS" not in out and rc == 2   # not asked for: non-zero


def test_no_gh_exits_nonzero_by_default_and_zero_with_allow_partial(monkeypatch, capsys):
    off = lambda root: ([], ["open-PR check not run (gh not installed)"])  # noqa: E731
    rc, out = _run_main(monkeypatch, capsys, [], online=off)
    assert rc == 2 and "PARTIAL" in out
    rc, out = _run_main(monkeypatch, capsys, ["--allow-partial"], online=off)
    assert rc == 0 and "RESULT: PARTIAL" in out and "RESULT: PASS" not in out


def test_failed_fetch_is_partial(monkeypatch, capsys):
    rc, out = _run_main(monkeypatch, capsys, [], fetch="git fetch origin main failed: offline")
    assert "RESULT: PARTIAL" in out and "fetch" in out


def test_full_online_run_is_pass(monkeypatch, capsys):
    rc, out = _run_main(monkeypatch, capsys, [])
    assert "RESULT: PASS" in out and rc == 0


def test_failure_beats_partial(monkeypatch, capsys):
    rc, out = _run_main(monkeypatch, capsys, ["--offline"], )
    monkeypatch.setattr(cp, "check_lean", lambda root: ["lean: boom"])
    rc = cp.main(["--offline"])
    assert rc == 1 and "RESULT: FAIL" in capsys.readouterr().out


def test_api_error_is_partial_not_failure(tmp_path):
    def api(path):
        raise cp.Offline("no network")
    fails, partial = cp.check_online(str(tmp_path), api=api, now=NOW)
    assert fails == [] and partial and "not run" in partial[0]


def test_unexpected_api_error_is_partial(tmp_path):
    def api(path):
        raise OSError("boom")
    fails, partial = cp.check_online(str(tmp_path), api=api, now=NOW)
    assert fails == [] and "not run" in partial[0]


def test_pr_whose_head_is_already_in_main_is_not_pending():
    g = lean_pair(FakeGH())
    items, _ = cp.collect(g, now=NOW, is_merged=lambda sha: sha.startswith("6663d0e"))
    assert items == []


def test_in_main_uses_git_ancestry(tmp_path):
    repo, shas = _repo(tmp_path, 3)
    _git(repo, "update-ref", "refs/remotes/origin/main", shas[1])
    assert cp.in_main(repo, shas[0]) and cp.in_main(repo, shas[1])
    assert not cp.in_main(repo, shas[2]) and not cp.in_main(repo, "deadbeef")


# ---------------------------------------------------------------- review-record detection (round 2 non-blockers)
def test_review_record_that_modifies_an_existing_file_is_a_record():
    g = FakeGH()
    g.pr(cp.FORK, 30, "Lean batch 2", "batch2", "6663d0e", "batch1")
    g.pr(cp.FORK, 32, "Re-check", "batch2-review", "295c968", "batch2", age_h=30)
    g.files[(cp.FORK, 32)] = [{"filename": "theory/reviews/BATCH2_REVIEW.md", "status": "modified"}]
    g.contents[("mitchell-moving/x", "theory/reviews/BATCH2_REVIEW.md", "295c968".ljust(40, "0"))] = pass_text("6663d0e")
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1 and "fork#30" in items[0]


def test_review_record_whose_file_name_lacks_review_is_a_record():
    g = FakeGH()
    g.pr(cp.FORK, 30, "Lean batch 2", "batch2", "6663d0e", "batch1")
    g.pr(cp.FORK, 32, "Second look", "batch2-look", "295c968", "batch2", age_h=30)
    g.files[(cp.FORK, 32)] = [{"filename": "notes/BATCH2_CHECK.md", "status": "added",
                               "patch": "@@ -0,0 +1 @@\n+Blockers remaining: 0"}]
    g.contents[("mitchell-moving/x", "notes/BATCH2_CHECK.md", "295c968".ljust(40, "0"))] = pass_text("6663d0e")
    items, _ = cp.collect(g, now=NOW)
    assert len(items) == 1 and "fork#30" in items[0]


def test_work_pr_with_a_text_file_quoting_the_line_is_still_work():
    g = FakeGH()
    g.pr(cp.FORK, 5, "T99", "t99", "aaaaaaa")
    g.files[(cp.FORK, 5)] = [{"filename": "theory/T99.md", "status": "added", "patch": "+Blockers remaining: 0"},
                             {"filename": "tools/t99.py", "status": "added"}]
    g.contents[("mitchell-moving/x", "theory/T99.md", "aaaaaaa".ljust(40, "0"))] = "Blockers remaining: 0\n"
    items, _ = cp.collect(g, now=NOW)
    assert items == []        # a code file makes it work, and nothing reviewed it


# ---------------------------------------------------------------- quoted or negated results
def test_quoted_blockers_line_is_not_a_result():
    for text in ('The reviewer must write "Blockers remaining: 0" at the end.',
                 "Write `Blockers remaining: 0` when done.",
                 "> Blockers remaining: 0",
                 "```\nBlockers remaining: 0\n```",
                 "This is not Blockers remaining: 0.",
                 "Do not merge until Blockers remaining: 0 appears.",
                 "\u201cBlockers remaining: 0\u201d is the phrase to look for."):
        assert cp.blockers_found(text) == [], text
        assert cp.review_result(text) == (None, [])


def test_real_result_forms_still_count():
    for text, want in (("Blockers remaining: 0", [0]),
                       ("Reviewed. **Blockers remaining: 2**", [2]),
                       ("Delta review of `d12642b` gives **Blockers remaining: 0**.", [0]),
                       ("one commit) is in: **Blockers remaining: 0.** Review", [0]),
                       ("Blockers remaining: 3\n\nlater\n\nBlockers remaining: 0", [3, 0])):
        assert cp.blockers_found(text) == want, text


def test_quoted_passing_comment_does_not_make_a_pr_pending():
    g = FakeGH()
    g.pr(cp.FORK, 30, "Lean batch 2", "batch2", "6663d0e", "batch1")
    g.comments[(cp.FORK, 30)] = [{"body": 'Please add "Blockers remaining: 0" once done.', "created_at": ts(40)}]
    assert cp.collect(g, now=NOW)[0] == []


# ---------------------------------------------------------------- closing keywords (REPO-CURRENT-3)
def test_closing_keyword_naming_another_pr_is_flagged():
    got = cp.closing_refs("STATUS, OPEN_WORK: fix #253 and #257 state", self_number=270)
    assert got == [("fix", cp.UPSTREAM, 253)]


def test_every_keyword_and_tense_is_flagged():
    for kw in ("close", "closes", "closed", "fix", "fixes", "fixed", "resolve", "resolves", "resolved", "Fixes", "CLOSES"):
        assert cp.closing_refs("%s #12" % kw, 1), kw
        assert cp.closing_refs("%s: #12" % kw, 1), kw


def test_other_repo_and_url_forms_are_flagged():
    assert cp.closing_refs("fixes mitchell-moving/theory-of-adaptive-organization#9", 1)[0][2] == 9
    assert cp.closing_refs("closes https://github.com/Chad-Mitchell/theory-of-adaptive-organization/pull/253", 1)[0][2] == 253


def test_own_number_and_plain_mentions_are_not_flagged():
    assert cp.closing_refs("fixes #270", self_number=270) == []
    assert cp.closing_refs("see #253; follows #257; prefix #12; the fix for #5 is below", 1) == []
    assert cp.closing_refs("Pointer refresh after #270, #271 and #275", 1) == []


def test_closes_ok_marker_allows_a_stated_number():
    assert cp.closing_refs("closes #12\ncloses-ok: #12 the issue is really done", 1) == []
    assert len(cp.closing_refs("closes #12 and fixes #13\ncloses-ok: #12 reason", 1)) == 1


def test_online_check_reads_title_body_and_commits():
    g = FakeGH()
    g.pr(cp.UPSTREAM, 270, "STATUS rebuild", "s270", "98d349a")
    g.pulls[cp.UPSTREAM][0]["body"] = "Rebuilds STATUS. Fixes #253 as a side effect."
    g.commits[(cp.UPSTREAM, 270)] = [{"sha": "a" * 40, "commit": {"message": "fix #253 and #257 state"}},
                                      {"sha": "b" * 40, "commit": {"message": "reword"}}]
    fails = cp.check_closing_online(g)
    assert len(fails) == 2 and any("commit aaaaaaa" in f for f in fails) and any("title/body" in f for f in fails)


def test_online_check_clean_pr_passes():
    g = FakeGH()
    g.pr(cp.UPSTREAM, 270, "STATUS rebuild", "s270", "98d349a")
    g.pulls[cp.UPSTREAM][0]["body"] = "Rebuilds STATUS. See #253."
    g.commits[(cp.UPSTREAM, 270)] = [{"sha": "a" * 40, "commit": {"message": "update state of #253"}}]
    assert cp.check_closing_online(g) == []


def test_check_online_includes_the_closing_check(tmp_path):
    g = FakeGH()
    g.pr(cp.UPSTREAM, 270, "STATUS rebuild", "s270", "98d349a", age_h=1)
    g.commits[(cp.UPSTREAM, 270)] = [{"sha": "a" * 40, "commit": {"message": "fix #253"}}]
    fails, _ = cp.check_online(str(tmp_path), api=g, now=NOW)
    assert any(f.startswith("closing:") for f in fails)


def test_local_pre_merge_check_reads_commits_and_body(tmp_path):
    repo, shas = _repo(tmp_path, 1)
    _git(repo, "update-ref", "refs/remotes/origin/main", "HEAD")
    open(os.path.join(repo, "g"), "w").write("x")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "STATUS: fix #253 and #257 state")
    assert len(cp.local_closing_check(repo, "origin/main..HEAD", 270)) == 1
    body = tmp_path / "body.md"
    body.write_text("Rebuild. Closes #263.\n")
    assert len(cp.local_closing_check(repo, "origin/main..HEAD", 270, str(body))) == 2
    _git(repo, "commit", "--amend", "-m", "STATUS: update state of #253 and #257")
    assert cp.local_closing_check(repo, "origin/main..HEAD", 270) == []


def test_local_check_cli_exit_codes(tmp_path, capsys):
    repo, shas = _repo(tmp_path, 1)
    _git(repo, "update-ref", "refs/remotes/origin/main", "HEAD")
    open(os.path.join(repo, "g"), "w").write("x")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "resolves #253")
    real = cp.repo_root
    cp.repo_root = lambda: repo
    try:
        assert cp.main(["--closing-keywords", "origin/main..HEAD", "--pr", "270"]) == 1
        assert "FAIL" in capsys.readouterr().out
        _git(repo, "commit", "--amend", "-m", "see #253")
        assert cp.main(["--closing-keywords"]) == 0
    finally:
        cp.repo_root = real


def test_will_when_if_should_must_before_blockers_is_not_a_result():
    for text in ("I will report Blockers remaining: 0",
                 "The note says when Blockers remaining: 0 the work can merge.",
                 "Merge only if Blockers remaining: 0.",
                 "The reviewer should write Blockers remaining: 0.",
                 "The reviewer must write Blockers remaining: 0"):
        assert cp.blockers_found(text) == [], text


def test_fixes_without_space_is_flagged():
    for text in ("Fixes:#12", "fixes:#12", "Closes:#12", "Resolves:#12"):
        got = cp.closing_refs(text, self_number=1)
        assert len(got) == 1 and got[0][2] == 12, text


def test_quoted_or_fenced_closing_keyword_is_not_flagged():
    for text in ('The headline contained "fix #253" in ordinary English.',
                 "The headline contained `fix #253`.",
                 "```\nfix #253\n```",
                 "> fix #253",
                 "Do not write “fix #253” in a commit message."):
        assert cp.closing_refs(text, self_number=1) == [], text
    # an unquoted keyword in the same text as a quoted one still flags
    got = cp.closing_refs('See "fix #253". Also fix #257 in the same body.', 1)
    assert len(got) == 1 and got[0][2] == 257
