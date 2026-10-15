# Canonical Challenge / Competition — Quick Reference v1.1

**Version:** 1.1 (proposed, 2026-10-15)  
**Governing documents:** `CANONICAL_CHALLENGE_WORKFLOW_v1.1.md` + `CANONICAL_AGENT_EXECUTION_PROTOCOL_v1.0.md`  
**Versioning:** Challenge has advanced from v1.0 to v1.1. Agent Execution is a new, separately versioned component at v1.0, not an outdated Challenge document. See `CHANGELOG.md`.  
**Applies to:** leaderboard/hidden-test AI challenges and benchmarks (VLSP, Zalo-style competitions, other officially organized shared tasks).  
**Not:** Pure Academic Research or Production Engineering; use their distinct domain workflows.

## Identity

**Maximize expected legal private/final performance while efficiently reducing decision-relevant uncertainty** under time, quota, compute, runtime and team constraints. Neither local score nor public leaderboard peak alone is the target.

## Current lifecycle (not a linear checklist)

```text
A Competition Truth
↕ B Measurement Trust
↕ C Competitive Anchor
↕ D Evidence-Driven Optimization
↕ E Consolidation / Finalization
```

Rollback when facts, evaluator, baseline or external transfer contradict assumptions.

## Think before implementing

```text
OBSERVE → PRIORITIZE → EXPLAIN → PREDICT
        → CHEAP DISCRIMINATING TEST
        → UPDATE BELIEF → DECIDE
```

Decisions: **KEEP / REVISE / KILL / ESCALATE / ROLLBACK / STOP**. Separately **PROMOTE** a challenger only after verifying its eligibility, score/reliability and reproducible artifact lineage.

**Three truth axes:** (1) implementation correct? (2) measurement valid? (3) expected private-transfer evidence strong enough? One does not prove the next.

## Git + coding agent: the 20-second contract

- Inspect the real repo and its dirty state. Protect the **incumbent** and all unrelated owner work.
- Bootstrap `docs/challenge_protocol.md` with real competition facts, unresolved unknowns, measured baseline, evaluator contract and next decision. Grow this single living contract; no artificial stage files.
- For consequential experiments, **fix criteria before relevant results**, implement/test, commit source, run from **clean** SHA, preserve raw outputs and run manifest, interpret, and commit the decision.
- Every decision-bearing run identifies **source SHA + resolved config + model/data/evaluator versions + seed/environment + output IDs**.
- A dirty/partial run is allowed for diagnosis when explicitly labeled, never silently promoted as clean evidence.
- Source files use semantic names; run directories may use unique timestamps. No empty scaffold, no phase-based file naming, no `git add .` across data/secrets. Optional tested clean-run reference: `reference_tools/require_clean_source.py`.
- Avoid overwriting last-known-good model or submission bytes. Submit only with authorized quota, legal/rule check and exact checksum.
- Coding agent autonomously executes **approved scope**, but does not invent new strategy, relax post-hoc thresholds, spend quota, kill other jobs or publish private data.

## Right rigor for the right experiment

| Class | Evidence minimum | Use |
| --- | --- | --- |
| Scratch/smoke | Explicitly provisional, can be dirty | Test that code runs |
| Diagnostic | Hypothesis/control, relevant failure examples | Identify mechanism or oracle ceiling |
| Decision-bearing | Pre-result rule, clean code snapshot, reproducible run | Decide next investment |
| Promotion | Representative validation, risk/runtime/rules, artifact recovery | Replace incumbent |
| External submission | Frozen exact bytes, expectation, ID/quota log | Validate transfer/final entry |

Challenge ≠ paper: do not waste deadline on publication-grade ablations with no decision value. But do not sacrifice legality or reproducibility of the final system.

## External leaderboard hygiene

**Public leaderboard is an imperfect sensor.** Local up/public down ⇒ audit validation transfer, uncertainty, slices, evaluator and exposure. Repeated submissions are not a substitute for a trustworthy local validation set. Keep private holdouts, group leakage controls and submission budget disciplined.

## Standard coding-agent round

```text
LEAD chooses high-value decision
    ↓ bounded work order
AGENT audits repo and existing evidence
    ↓ plan + criteria committed when meaningful
AGENT implements + tests, commits code
    ↓ runs from clean pinned source
AGENT records raw outputs, manifest and verdict
    ↓ one report with source SHA/run IDs/limits
LEAD confirms strategy / promotion / next round
```

### Paste-ready handoff

```text
Workflow: Canonical Challenge / Competition Workflow v1.1
Execution: Canonical Agent Execution & Evidence Protocol v1.0

Decision to resolve: ...
Known source of truth / incumbent: ...
Authorized scope and resources: ...
Non-scope and protected invariants: ...
Evaluator, split, metric and controls: ...
Success/failure/promotion criteria (or exploratory status): ...

Audit before editing. Execute all approved steps autonomously.
Use semantic file names and selective Git commits. Run meaningful
comparisons from a clean source commit with run provenance.
Preserve raw/failed results, avoid overwriting the incumbent,
and report once: verdict, actual changes, tests, evidence,
source SHA/run IDs, limitations and the decision needing approval.
Do not make unauthorized submissions or strategic pivots.
```

## Healthy end state

Can you restore the incumbent, explain why it is preferred, reproduce the evaluator, identify every consequential result's source/data/model, reconstruct final submission bytes, and distinguish unknowns from proved gains? If not, fix the *most decision-critical* missing element—not every possible artifact.

## Version note

v1.1 **preserves** Challenge v1.0's A–E lifecycle, E0–E7 evidence hierarchy, data/resource/leaderboard rules, negative evidence and stopping logic. It adds execution discipline: truthful project protocol, bounded agent autonomy, clean-source Git, immutable run lineage, incumbent promotion/rollback, and auditably exact submissions. The 2026-10-03 v1.0 backup remains unchanged.
