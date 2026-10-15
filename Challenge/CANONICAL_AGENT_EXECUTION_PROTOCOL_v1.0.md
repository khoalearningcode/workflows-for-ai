# Canonical Agent Execution & Evidence Protocol v1.0

**Status:** Proposed reusable operating contract  
**Version:** 1.0  
**Prepared:** 2026-10-15  
**Applies to:** coding-agent execution for Challenge/Competition, Pure Academic Research, and Production Engineering projects.  
**Governing rule:** The applicable *domain workflow* determines objectives and the strength of evidence required. This protocol determines how authorized work is executed, traced, and handed back.

> **Identity:** A coding agent changes a controlled system and creates inspectable evidence. Source code, experiment configurations, results, and decisions must remain attributable, resumable, and reversible without creating unnecessary ceremony.

## 0. Separation of authority

A domain lead (research/competition/engineering owner) decides *what is worth doing* and which trade-offs are acceptable. The execution agent decides *how to perform an approved, bounded task safely*. The execution agent may detect flaws, propose corrections, and implement routine repairs within the approved envelope. It must not silently substitute a different scientific claim, competition strategy, metric, data source, policy, or deployment target.

For academia, scientific validity and human ownership of interpretation take precedence over throughput. For challenges, expected private performance under rules and deadline dominates paperwork. For production, user/system behavior and deployment safety dominate experimental neatness. **This protocol never overrides those distinctions.**

### Decision rights

| Decision | Agent can proceed autonomously? | Rule |
| --- | --- | --- |
| Read/inspect repository, test existing behavior, reproduce a reported issue | Yes, within access permissions | Avoid modifying shared resources without coordination |
| Create semantic files needed by approved task, write tests, refactor locally | Yes | Preserve interface/contracts; no fabricated files |
| Repair errors that make the approved test invalid | Yes | Document root cause, changed assumptions, and reruns |
| Change experiment metric, dataset split, controls, or acceptance threshold after seeing results | **No** | Escalate; preserve original plan/result |
| Substitute a new research direction, training regime, or external dataset | **No** | Requires owner approval and legality review |
| Promote challenger to canonical/best system | Only under pre-authorized promotion rule | Otherwise report a candidate and request decision |
| Submit externally, spend substantial new quota/budget, share data, deploy, overwrite remote state | Only with explicit scoped authorization | Defaults to no |
| Kill someone else's GPU jobs or change unrelated infrastructure | **No** | Coordinate, defer, or use safe isolation |

## 1. Repository onboarding / truth reconstruction

Before significant edits, inspect the actual workspace rather than imposing a prebuilt scaffold:

1. Confirm repository root and tracked/untracked state; check remotes/branches and ownership. **Never initialize Git over a repository or nested subproject without inspecting it.**
2. Identify executable entry points, tests, baseline path, evaluator, configurations, external dependencies, data/checkpoint locations, hardware and current live jobs.
3. Separate facts observed directly, facts reported by owner/docs, inferences, and unknowns. State any discrepancy before planning against it.
4. Establish the currently reproducible baseline, canonical metric, invariant contracts, and known protected artifacts.
5. If the repo is not versioned and permission to initialize is within scope, create Git only after choosing a correct root and safe `.gitignore`; do not make a giant unexplained initial commit of unrelated data.
6. For an existing repo, preserve its conventions when reasonable; migrate only when the benefit and risks are explicit.

### Protocol bootstrap: real content on day one

Create or update the project protocol at the start of a new project **only when it can truthfully contain** the objective, scope, known constraints, observed state, unresolved unknowns, and next decision. Example semantic filenames: `docs/challenge_protocol.md` for challenge, `docs/research_protocol.md` for academic research. This is a living *contract*, **not** a required long stage checklist and not a substitute for code/tests. A filename is recommended, not a universal hard-coded dependency.

When an agent-instruction file such as `AGENTS.md` or `CLAUDE.md` is useful, create it only after the real repository and stable constraints are known. It should describe durable permissions, commands, tests and invariants; changing experiment hypotheses/results belong in the project protocol instead. Do not pre-create empty directories, placeholder logs, example results or TODO documents merely to resemble a template. Conceptual workflow objects need physical files only when they serve a present purpose. Use stable `lower_snake_case` semantic filenames; dates or IDs belong in **run instances**, not source filenames.

## 2. Work order and proportional rigor

Every meaningful assignment identifies: decision question/desired behavior, approved scope/non-scope, observed baseline, protected invariants, available resources, required checks, acceptance/kill criteria, and reporting expectation. The agent may select minimal implementation details consistent with the order.

| Execution class | Examples | Before execution | Validation & evidence |
| --- | --- | --- | --- |
| **Scratch / smoke** | import check, 1–2 sample integration, quick profiling | State question and obvious side effects | May run dirty; clearly label provisional; cannot support a headline claim or promotion |
| **Diagnostic** | isolated failure slice, oracle ceiling, fast probe | Record hypothesis and controls proportionally | Store interpretable outputs; identify measurement limitations; commit if consequential |
| **Decision-bearing** | controlled comparison affecting system choice | Freeze config, metrics, interpretation and stopping rules **before** result exposure | Prefer clean source commit, output lineage, repeatability checks and explicit verdict |
| **Promotion / external release** | chosen candidate, final inference/submission | Pre-authorized promotion/submission gate, runtime/rule validation | Clean pinned source and dependencies, verify artifact hashes, dry-run, rollback/fallback |

Decision-bearing experiments can use brief in-protocol registration rather than standalone cards. For exploratory competitions, not every tiny probe needs a formal pre-registration. A result observed before criteria were fixed remains exploratory; do not retrospectively relabel it confirmatory.

## 3. Implementation and Git transaction discipline

**Semantic commits** record meaningful changes, not arbitrary stage completion. Recommended transaction:

```text
A. Audit working tree and protect original baseline.
B. Record decision-bearing plan, criteria and experimental controls.
C. Commit the plan (when decision-bearing) before evaluating the outcome.
D. Implement smallest coherent code/test slice; validate; commit source.
E. Run from this clean source commit; record source_sha in each run.
F. Analyze *without rewriting* original run objects; record verdict.
G. Commit analysis/decision and versioned lightweight evidence manifest.
H. Promote candidate only after a separate gate; otherwise retain incumbent.
```

Examples of informative commit subjects:

```text
Document official scoring contract and baseline constraints
Add manifest generator with stable sample grouping
Verify evaluator against accepted scoring examples
Pre-register chart routing comparison
Implement routing control and invariant tests
Record chart routing outcome and decision
Promote verified candidate for final submission
```

Do **not** require exactly seven commits per experiment, a branch for every stage, or one commit per agent message. Small, related, correct changes may share a commit. Major experimental plan/result distinction must stay visible in history, whether by separate commits or immutable timestamped records tied to commits.

### Clean-source gate

For decision-bearing/promotion runs, refuse unexpected changes in **tracked** source and unexpected untracked source files. Intentionally ignored output/cache files may exist. A project may explicitly allow a dirty diagnostic run only if `git_dirty=true`, a source patch/diff fingerprint is captured when feasible, and the run is excluded from promotion-grade evidence until reproduced cleanly.

The exact guard must be tested against: (i) modified tracked code, (ii) staged changes, (iii) untracked nonignored source/config, (iv) ignored outputs, (v) externally referenced checkpoint paths. An **optional tested reference implementation** is bundled at `reference_tools/require_clean_source.py`, with `reference_tools/test_require_clean_source.py` (5 local tests passed on 2026-10-15). Copy/adapt it **only when a project actually needs a source gate**; it cannot validate datasets, weights or environment. `git status --porcelain` alone does not validate mutable external datasets or checkpoint revisions.

### Branches, tags, checkpoints

- **Commit** = immutable source history (if protected by repository retention). Do not force-rewrite published history or amend evidence that downstream artifacts cite.
- **Branch/worktree** = isolation of concurrent or risky changes; use when necessary, not for each stage by default.
- **Tag** = human-readable checkpoint for a stable baseline, promoted system or submission; add sparingly and never let a tag replace immutable hashes.
- **Model checkpoint** = data artifact with a digest, model revision and producing run; may live outside Git. Do not pretend a Git commit alone versions large weights.
- **Rollback** = point system selection to a known-good, re-creatable source/config/checkpoint combination, not merely a source commit.

Before commit, inspect `git diff --stat`, staged diff, ignored files, file size and secret scans where relevant. Use selective staging; never blindly `git add .` around datasets/secrets/model weights. Preserve the owner's unrelated dirty work; never hard-reset or clean it away by default.

## 4. Run manifest and artifact immutability

Every *decision-bearing* run must have a stable `run_id` and a machine-readable manifest. Example of a concrete schema (fields nullable only when genuinely inapplicable):

```json
{
  "run_id": "routing_comparison_20261015T072000Z",
  "run_class": "decision_bearing",
  "decision_id": "routing_comparison",
  "source_sha": "<full Git commit hash captured at run start>",
  "git_dirty": false,
  "config_sha256": "<digest of resolved config>",
  "dataset_id": "<version, split, manifest hash>",
  "model_id": "<checkpoint revision or artifact digest>",
  "evaluator_id": "<official code/version plus local patch digest>",
  "seed": 20261015,
  "environment": {"python": "<version>", "packages_lock": "<hash>", "hardware": "<device>"},
  "method": {"metric": "<exact definition>", "sample_count": 0},
  "result_status": "completed",
  "artifacts": {"predictions": "<relative path>", "metrics": "<relative path>"},
  "limitations": []
}
```

Values in angle brackets above are **schema illustrations, not real data**: do not write this sample as a purported run. Use a local format appropriate to the project (`run.json`, JSONL or tracker metadata) and omit irrelevant fields instead of faking values. For distributed/interruptible jobs, additionally record completed item IDs, resumability, failure status and output integrity.

**Lineage chain:** `decision/plan → source_sha + resolved config + dataset/model/evaluator identity → run_id → raw outputs → analysis → interpretation → promotion/submission`. The chain must distinguish model training, model selection and inference artifact creation when these are separate runs.

Raw run outputs are **append-only** once cited or used for a decision. If analysis was wrong, create a new corrected analysis with reference to the original; do not modify raw predictions/metrics invisibly. If artifact storage is mutable, keep checksums and/or write-protected exports for important results.

Large files belong in appropriate artifact stores or Git LFS/DVC/Hugging Face (subject to license/privacy), with cryptographic checksums and recoverable references. **A public model/data repo is not automatically lawful or safe**; comply with dataset licenses and organizers' redistribution policies. Credentials live in secret management, not committed configs.

## 5. Correctness, measurement validity and outcome

Keep three separate truth claims:

1. **Implementation correctness:** Does code obey the intended contract? Unit/property/invariant tests, reference parity, smoke checks.
2. **Measurement validity:** Does the evaluation measure what the decision requires? Official metric fidelity, leakage controls, sample identity, paired comparisons, uncertainty and instrumentation validity.
3. **Outcome evidence:** Is the observed improvement robust, useful and relevant to the true goal (private score, scientific claim, or operational reliability)?

Passing (1) never implies (2); passing (2) never implies (3). When a surprising result appears, first audit controls, evaluator and data before inventing a rescue explanation. Negative results count as durable evidence. Mark estimates from an oracle, cost model, leaked annotation or synthetic proxy as such; do not call them deployable or measured improvements.

### Invalidation and correction

If a bug, scoring mismatch, leakage, benchmark drift, wrong environment or artifact corruption is found:

- Preserve the original run and note it is invalid/superseded, with the exact reason.
- Establish the blast radius: which runs, decisions, and submissions relied on it?
- Fix code/contract and add a regression test when feasible; commit the correction.
- Rerun affected decisive comparisons from a clean snapshot; revise the belief/decision explicitly.
- If an external submission already occurred, preserve its historical fact; do not silently reinterpret its score.

## 6. Incumbent / challenger promotion and final artifact lineage

Maintain separate identities for:

- **Working candidate**: current experimental code/model; may be unstable.
- **Incumbent**: best verified system under the project's actual decision rule; preserved until a challenger passes promotion.
- **Submission candidate**: fully built inference pipeline and artifact chosen for external evaluation, including packaging and runtime requirements.
- **Submitted artifact**: exact bytes/checksums and external submission ID/result; immutable historical event.

**Promotion** requires verified metric comparison (including uncertainty when necessary), key slice/regression checks, rule compliance, runtime/memory/resource compliance, an intact source/data/model/config lineage, and a reproducible packaging/inference test. Score alone is insufficient. If promotion fails, retain the incumbent and record why. When the deadline is near, prioritize stable verified expected private score over speculative local peaks.

A rollback must restore the full **environment/config/model/source/data preprocessing** combination, not just revert a line of code. Do not overwrite last-known-good artifacts in place.

## 7. Compute ownership and long-running jobs

Before a substantial run, inspect load and owner of shared GPU/CPU, disk usage, process IDs, and likely runtime. Capture environment and monitor contention if measurements depend on it. Respect the user's running jobs: do not kill them. Pause/queue your own job, ask for resource allocation when needed, or choose a safe low-cost alternative.

Avoid mutating code while a decision-bearing job is reading it unless the job runs from an isolated immutable checkout/worktree/container. Long jobs should use unique output folders, atomic manifests/finalization, checkpointing and robust failure statuses. Partial outputs are not silently counted as completed; resumptions validate previous shards/checksums to avoid duplicates.

## 8. Agent handoff and communication contract

At the completion of an approved work order, provide **one substantive handoff**; do not send minute-by-minute narration unless coordination/risk requires it. Use this fixed order:

1. **Verdict** — what passed/failed/was blocked; differentiate implemented from actually tested.
2. **Work performed** — important code, data, protocol changes; boundaries respected.
3. **Evidence** — criterion → measured value → pass/fail; denominators and uncertainty as appropriate.
4. **Provenance** — relevant source commit(s), run IDs, manifest, checkpoint/config identity, clean/dirty state and location of artifacts.
5. **Interpretation & limits** — what result does and does not justify; unexpected behavior, corrections and negative results.
6. **Decision/next high-value action** — promote/revise/kill/rollback/stop recommendation; ask owner only where authority ends.

Agent must never claim a command ran, a commit exists, a score passed, or an external submission was made unless verified by output. If evidence is incomplete, label partial status and unblockers explicitly.

### Compact work-order message for a coding agent

```text
WORKFLOW: <domain workflow and version>
EXECUTION: Canonical Agent Execution & Evidence Protocol v1.0
GOAL / DECISION: <what this round must resolve>
KNOWN BASELINE: <validated starting point; source refs>
SCOPE: <authorized edits, experiments, data, compute>
NON-SCOPE: <do not start these directions>
INVARIANTS: <what must remain correct>
MEASUREMENT: <metric, evaluator, split, controls, risk>
SUCCESS / STOP: <predefined criteria or explicitly exploratory>
OUTPUT: <source commits, test evidence, run manifest, verdict>
AUTONOMY: execute approved work end-to-end; escalate strategic changes only.
```

This is a **communication template**, not a requirement to create a file for every message. If the agent lacks a needed fact, it should reconstruct it from the repo and flag unresolved facts rather than manufacture them.

## 9. Domain-specific overlays

| Concern | Challenge | Academic research | Production engineering |
| --- | --- | --- | --- |
| Primary value | Expected hidden/private score under rules | Defensible understanding/contribution and researcher growth | Safe reliable behavior in use |
| Experiment gate | Promotion and external transfer | Falsifiable scientific claims and adequate controls | Behavior contract/risk-based acceptance |
| Pre-registration | Decision-bearing runs; proportionate near deadline | Stronger for confirmatory claims | Test/rollout criteria for risky changes |
| Evidence ceiling | Expected final performance and deadline economics | Claim strength bounded by causal/statistical evidence | Reliability, safety and rollback |
| Rollback | Restore best legal submission candidate | Restore validated scientific baseline, update belief | Restore operable deployed version |
| Owner decision | Strategy, submission, legality, expenditure | Question, interpretation, claims, scientific direction | Requirements, risk tolerance and deployment authority |

## 10. Minimal adoption and maturity checks

A small one-person project can begin with a truth-bearing project protocol and a baseline Git commit; add tracking only as real work produces artifacts. Scale up when runs multiply or results guide major decisions.

Before calling an agent execution system **reproducible**, confirm the following through an actual restoration test where feasible: `checkout source_sha → resolve config/data/model/evaluator → rerun representative sample → score correctly → reconstruct promoted artifact`. Capturing metadata without testing restoration is traceability, not proof of reproducibility.

**Anti-patterns:** process theatre; stage-named source files; fake empty schemas; one branch per test; unversioned mutable datasets; dirty source claimed as clean; rewritten raw results; undocumented criterion changes; automatic promotion from single noisy score; conflation of oracle and deployable policy; public LB tuning without exposure control; overwriting last-known-good checkpoint; killing unrelated workloads; unverified claims of agent work.

## 11. Version history

**v1.0 (2026-10-15):** initial reusable execution layer, adapted from the verified strengths of the LLM Serving research protocol and the existing canonical domain workflows. This is a normative design; writing the document **does not** install guards, create repository commits, reproduce runs or validate an existing project.
