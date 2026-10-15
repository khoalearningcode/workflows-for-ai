# Canonical Challenge Workflow — Changelog & Version Map

## Active release (2026-10-15)

| Component | Version | Status | File |
| --- | --- | --- | --- |
| Challenge/Competition domain workflow | **v1.1** | Proposed canonical; ready for project adoption and real-world validation | `CANONICAL_CHALLENGE_WORKFLOW_v1.1.md` |
| Challenge quick reference | **v1.1** | Companion to Challenge v1.1 | `CHALLENGE_QUICK_REFERENCE_v1.1.md` |
| Agent Execution & Evidence Protocol | **v1.0** | New independent reusable component | `CANONICAL_AGENT_EXECUTION_PROTOCOL_v1.0.md` |
| Challenge/Competition historical baseline | **v1.0** | Frozen and preserved separately | `CANONICAL_CHALLENGE_WORKFLOW_v1.0.md` |

**Version rule:** the Challenge workflow and the cross-domain execution protocol are independent artifacts. An increment in one does not automatically increment the other. Quick references track the domain workflow they summarize. Bump a version only for a substantive normative change; minor typo/format repairs may be noted without a new version. Do not silently rewrite an already published frozen baseline.

## Challenge v1.1 — 2026-10-15

**Supersedes Challenge v1.0 for newly adopted projects**, without erasing its original contents or conceptual foundation. The 31 baseline sections remain, followed by ten sections (32–41) that operationalize repository and execution discipline:

1. Domain decisions and agent execution are separated, with independent authority boundaries.
2. A truthful living project protocol is developed incrementally, never filled with fabricated state.
3. Filenames and folders are semantic, created just in time instead of as stage-named placeholders.
4. Evidence and run rigor scale with decision importance and deadline pressure.
5. Planning, implementation, clean Git source and post-run result recording have attributable chronology.
6. Run metadata links code, configuration, data/model revision, evaluator and environment.
7. Incumbent, challenger, checkpoint and submission identities are kept distinct; promotion is evidence-gated and reversible.
8. Shared-compute ownership, interrupted jobs and recovery preserve unrelated workloads.
9. Coding agents receive bounded authority and return a single verifiable handoff.
10. Corrections preserve original observations, and older projects adopt rules through audit rather than destructive restructuring.

**Not a new academic framework:** competition success remains expected legal hidden/private-test performance under evidence, resource and deadline constraints, not publication novelty.

## Agent Execution Protocol v1.0 — 2026-10-15

First independent release. It can be adopted with Challenge, Academic Research or Production Engineering; its evidence rigor is determined by the relevant domain workflow. Its version **must not be mistaken for Challenge v1.0**. This document defines a target operating contract; it does not demonstrate that any given repository has adopted or validated its guardrails.

## Challenge v1.0 — 2026-10-03

Original frozen workflow. Kept unchanged as a historical comparison and rollback/reference source, including the lifecycle, measurement trust, evidence hierarchy, leaderboard transfer, resource economics, evidence debt, STOP/ROLLBACK rules and experiment-lead/coding-agent separation.

## Suggested future version policy

- **v1.1.x** (if using patch versions): compatible clarifications and corrections without changed operating obligations.
- **v1.2:** meaningful new, backward-compatible workflow discipline grounded in actual Challenge operation.
- **v2.0:** incompatible redesign or changed primary operating contract, with a migration note.

Never increment the version solely because a new experiment, project, or guide was added. Such events belong in the individual project's protocol and Git history.
