# Canonical Challenge / Competition Workflow — Changelog

## v1.0 — 2026-10-03

Initial frozen canonical version.

### Major design decisions
- Replaced a rigid stage pipeline with a revisable lifecycle plus a closed-loop decision engine.
- Defined the challenge objective as expected hidden/final performance under constraints.
- Added Measurement Trust as a first-class state.
- Reframed baselines as measurement instruments rather than checkboxes.
- Introduced the Evidence-Driven Optimization Loop:
  Observe → Prioritize → Explain → Predict → Test cheaply → Update belief → Decide.
- Added an evidence hierarchy from observation through leaderboard transfer.
- Added oracle/ceiling tests as a first-class tool.
- Added promotion, kill, rollback, stop, and strategic-review rules.
- Added uncertainty register and error-budget concepts.
- Formalized leaderboard transfer, adaptive overfitting, and submission-purpose discipline.
- Added evidence debt.
- Added data-centric interventions under the same evidence rules as model interventions.
- Added resource economics: compute, runtime, latency, engineering complexity, submissions, and opportunity cost.
- Added STOP / DEPRIORITIZE as a valid evidence-based project decision.
- Added adversarial stress tests covering late data release, noisy metrics, limited submissions, limited compute, frontier gaps, and local↔LB mismatch.

### Communication shorthand
When a project declares:
`Workflow: Canonical Challenge / Competition Workflow v1.0`

the full contract in `CANONICAL_CHALLENGE_WORKFLOW_v1.0.md` applies unless the project explicitly overrides a rule.
