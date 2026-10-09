# Canonical Production Engineering Workflow v1.0

**Status:** Canonical\
**Version:** 1.0\
**Purpose:** Real / production engineering projects\
**Core objective:** Turn a real need into a system that is correct, reliable, maintainable, operable, safely deliverable, and understandable by the next engineer.

---

<details>
<summary>Table of contents</summary>

- [0. Scope and Positioning](#0-scope-and-positioning)
- [1. Canonical Engineering Loop](#1-canonical-engineering-loop)
- [2. Stage 1 — Work Intake and Change Classification](#2-stage-1--work-intake-and-change-classification)
- [3. Stage 2 — System Truth / Current-State Reconstruction](#3-stage-2--system-truth--current-state-reconstruction)
- [4. Stage 3 — Behavior Contract and Acceptance Criteria](#4-stage-3--behavior-contract-and-acceptance-criteria)
- [5. Stage 4 — Impact Classification](#5-stage-4--impact-classification)
- [6. Stage 5 — Validation Ladder](#6-stage-5--validation-ladder)
- [7. Stage 6 — Engineering Design and Risk Review](#7-stage-6--engineering-design-and-risk-review)
- [8. Stage 7 — Executable Change Spec](#8-stage-7--executable-change-spec)
- [9. Stage 8 — Controlled Implementation Loop](#9-stage-8--controlled-implementation-loop)
- [10. STOP Rules](#10-stop-rules)
- [11. Stage 9 — Operational and Failure-Mode Review](#11-stage-9--operational-and-failure-mode-review)
- [12. Stage 10 — Release Candidate Preparation](#12-stage-10--release-candidate-preparation)
- [13. Promotion Rules](#13-promotion-rules)
- [14. Recovery Is Broader Than Git Revert](#14-recovery-is-broader-than-git-revert)
- [15. Definition of Ready](#15-definition-of-ready)
- [16. Definition of Done](#16-definition-of-done)
- [17. Incident Fast Path](#17-incident-fast-path)
- [18. Project Bootstrap Rules](#18-project-bootstrap-rules)
- [19. Dynamic State](#19-dynamic-state)
- [20. Durable Decision Records](#20-durable-decision-records)
- [21. Coding-Agent Contract](#21-coding-agent-contract)
- [22. Closure Format](#22-closure-format)
- [23. Production Invariants](#23-production-invariants)
- [24. Workflow Selection Rule](#24-workflow-selection-rule)
- [25. Final Principle](#25-final-principle)

</details>

## 0. Scope and Positioning

This workflow is for production-oriented engineering work: web applications, backends, APIs, AI services, desktop software, infrastructure, deployment systems, internal tooling, integrations, performance work, migrations, and operational fixes.

It is intentionally different from:

- **Academic Research:** optimize for truthful understanding and scientifically defensible contribution.
- **Challenge / Competition:** optimize for valid leaderboard transfer and competition performance under official rules.
- **Production Engineering:** optimize for correct user/system behavior, safe change, reliability, maintainability, operability, and delivery.

Production work must not collapse into either of these two failure modes:

1. **Code-first implementation:** issue → edit files → run some tests → declare done.
2. **Process theatre:** forcing every small change through heavyweight documents and ceremonies.

The governing principle is:

> **Rigor scales with impact. Documentation scales with consequence.**

---

## 1. Canonical Engineering Loop

Every production change follows the same conceptual loop:

```text
UNDERSTAND
    ↓
ESTABLISH SYSTEM TRUTH
    ↓
DEFINE BEHAVIOR CONTRACT
    ↓
CLASSIFY IMPACT
    ↓
SELECT REQUIRED EVIDENCE
    ↓
DESIGN SMALLEST SAFE CHANGE
    ↓
WRITE EXECUTABLE CHANGE SPEC
    ↓
IMPLEMENT IN VERIFIED SLICES
    ↓
VALIDATE
    │
    ├── evidence contradicts assumptions
    │         ↓
    └──── REVISE MODEL / DESIGN
              ↓
         IMPLEMENT AGAIN
    ↓
BUILD FROM CANONICAL SOURCE
    ↓
PROMOTE THROUGH REQUIRED ENVIRONMENTS
    ↓
VERIFY REAL BEHAVIOR
    ↓
CLOSE + PRESERVE DURABLE LEARNING
```

This is not a strictly linear pipeline. Evidence may force a return to an earlier stage.

---

## 2. Stage 1 — Work Intake and Change Classification

Before coding, identify the nature of the work.

Typical classes:

- Feature
- Bug fix
- Refactor
- Migration
- Integration
- Performance work
- Infrastructure change
- Security change
- Incident / hotfix

For every non-trivial task, establish:

- desired user/system outcome;
- current problem or limitation;
- explicit scope;
- explicit non-scope;
- known constraints;
- external dependencies;
- frozen areas that must not be modified;
- initial impact level.

Do not allow an implementation agent to infer project scope from a vague issue title alone.

---

## 3. Stage 2 — System Truth / Current-State Reconstruction

Understand the system that actually exists before changing it.

Relevant evidence may include:

- repository structure;
- runtime path;
- request/data flow;
- current API contracts;
- current state transitions;
- configuration;
- database schema;
- tests;
- logs;
- build process;
- deployment model;
- integration boundaries;
- observed user behavior.

When the task is a bug, reproduce it when reasonably possible.

When the task is performance-related, establish a baseline before optimization.

The gate is passed only when the engineer can answer:

> **What does the system do today, and why does this change need to exist?**

Assumptions must be labeled as assumptions until verified.

---

## 4. Stage 3 — Behavior Contract and Acceptance Criteria

Convert the request into observable behavior.

Define, when relevant:

- expected inputs;
- expected outputs;
- state transitions;
- failure behavior;
- authorization behavior;
- compatibility requirements;
- user-visible behavior;
- data invariants;
- latency/resource requirements;
- concurrency behavior;
- security properties.

Acceptance criteria must exist before implementation for non-trivial changes.

Do not confuse implementation detail with acceptance criteria.

Bad:

> Add a helper class and cache the response.

Better:

> Repeated requests for the same immutable object must return the same data while reducing upstream calls without serving stale data beyond the allowed TTL.

---

## 5. Stage 4 — Impact Classification

Use the highest consequential dimension as the minimum impact level.

### I0 — Trivial

Characteristics:

- isolated;
- obvious;
- reversible;
- negligible blast radius.

Examples:

- typo;
- copy change;
- isolated styling fix.

### I1 — Low

Characteristics:

- localized behavior change;
- small and understood blast radius;
- no meaningful data/security/deployment risk.

Examples:

- local form validation;
- isolated component logic.

### I2 — Moderate

Characteristics:

- meaningful user flow;
- multiple components;
- business logic;
- simple persistence;
- integration surface with manageable risk.

Examples:

- UI + API feature;
- new state transition;
- non-destructive persistence change.

### I3 — High

Characteristics:

- cross-system behavior;
- authentication or authorization;
- schema migration;
- concurrency;
- external production dependency;
- deployment-sensitive change;
- significant compatibility concern.

### I4 — Critical

Characteristics:

- realistic risk of broad outage;
- irreversible or hard-to-reverse mutation;
- serious data loss risk;
- critical identity, payment, security, or infrastructure path.

#### Impact rule

> **Impact can only be downgraded by evidence, never by optimism.**

If new evidence reveals a larger blast radius, raise the impact level immediately.

---

## 6. Stage 5 — Validation Ladder

Validation is evidence. Each layer proves only what it actually exercises.

### V0 — Static

Examples:

- syntax;
- type checks;
- lint;
- build viability.

### V1 — Focused

Proves the changed logic itself.

Examples:

- focused unit test;
- targeted reproduction;
- deterministic local check.

### V2 — Component + Relevant Regression

Proves the affected component still satisfies its contract and protects nearby existing behavior.

### V3 — Integration

Proves boundaries between real components or dependencies.

Examples:

- backend ↔ database;
- frontend ↔ backend;
- service ↔ provider.

### V4 — System / E2E / Staging

Proves critical user journeys in an environment representative enough to expose system-level failures.

### V5 — Production Verification

Proves the released behavior actually works in the target environment.

Typical minimum mapping:

| Impact | Minimum evidence floor |
|---|---|
| I0 | V0–V1 |
| I1 | V0–V2 |
| I2 | V0–V3 |
| I3 | V0–V4 |
| I4 | V0–V5 |

This is a floor, not a ceiling.

#### Evidence invariants

- Unit test pass ≠ integration pass.
- Mock integration pass ≠ real dependency pass.
- Build success ≠ user flow works.
- Staging pass ≠ production pass.
- Deployment command success ≠ production behavior correct.

---

## 7. Stage 6 — Engineering Design and Risk Review

Choose the **smallest safe design** that satisfies the behavior contract.

Review only dimensions relevant to the change:

- API contract;
- storage/schema;
- state ownership;
- frontend/backend boundaries;
- concurrency;
- dependency behavior;
- failure propagation;
- deployment;
- migration;
- rollback/recovery;
- observability;
- security;
- compatibility.

Architecture work should scale with consequence.

A CSS fix does not need an ADR.

A cross-service state migration may require one.

Record durable decisions only when future engineers would reasonably need the rationale.

---

## 8. Stage 7 — Executable Change Spec

Every non-trivial change should have an executable Change Spec.

The spec is a **change-local artifact**, not a project-wide permanent rule.

It should define:

- outcome;
- current truth;
- target contract;
- scope;
- frozen files/surfaces;
- invariants;
- chosen design;
- implementation slices;
- required validation;
- deployment/recovery;
- observability;
- STOP conditions;
- exact DONE evidence.

See [Change spec template](templates/change_spec.md).

---

## 9. Stage 8 — Controlled Implementation Loop

Implement in small, independently verifiable slices.

For each slice:

```text
implement
    ↓
validate
    ↓
inspect evidence
    ↓
continue only if the mental model still holds
```

Rules:

- Do not mix unrelated cleanup into the requested change.
- Do not silently expand scope.
- Do not edit frozen files without explicit scope review.
- Do not add workaround after workaround when evidence points to a wrong root-cause model.
- Do not keep coding when a STOP condition fires.

---

## 10. STOP Rules

Implementation must stop and return to reasoning when any of the following occurs.

| Trigger | Return to |
|---|---|
| Cannot reproduce the assumed current behavior | System Truth |
| Acceptance criteria are contradictory or undefined | Behavior Contract |
| Actual architecture differs materially from assumptions | System Truth / Design |
| Required change crosses a frozen boundary | Scope review |
| Blast radius is larger than classified | Impact Classification |
| Test failures invalidate the current mental model | Diagnosis / Design |
| A second workaround is needed to support the first workaround | Root-cause analysis |
| Migration can lose/corrupt data and recovery is undefined | Design |
| A new auth/security boundary appears | Risk review |
| Real dependency behaves differently from mocks | Integration analysis |
| Build artifact cannot be traced to tested source | Release preparation |
| Staging or production verification fails | Do not promote / recover |

A STOP is not failure.

It means:

> **Evidence invalidated an assumption. Update the model before continuing.**

---

## 11. Stage 9 — Operational and Failure-Mode Review

For changes where relevant, ask:

> **When this fails in real life, how does it fail, and how will we know?**

Review:

- authentication and authorization;
- secrets;
- data integrity;
- retries;
- idempotency;
- timeout behavior;
- concurrency;
- partial failure;
- rate limits;
- resource limits;
- queue/backpressure behavior;
- schema compatibility;
- migration safety;
- observability;
- rollback/recovery.

Do not add mechanisms that have no demonstrated relevance to the change.

---

## 12. Stage 10 — Release Candidate Preparation

A release candidate must be derived from canonical source.

Rules:

- Build/package deterministically where practical.
- Know which source revision produced the artifact.
- Keep config explicit.
- Validate migrations before promotion.
- Do not manually patch generated build/dist/application artifacts after build.
- Do not treat an untraceable artifact as release-ready.

Generated artifacts are outputs, not alternate source-of-truth copies.

---

## 13. Promotion Rules

### Implementation → Candidate

Require:

- behavior contract implemented;
- focused tests pass;
- relevant regressions pass;
- no known unresolved critical defect;
- source tree understandable and controlled.

### Candidate → Integration / Staging

Require, when applicable:

- deterministic build/package;
- config resolved;
- migration verified;
- dependency contract confirmed;
- artifact traceable to tested source.

### Staging → Production

For changes requiring staging:

- critical journey passes;
- production-like or real required dependencies are verified;
- recovery path exists;
- required observability is available;
- no blocking regression remains.

### Production → CLOSED

Require appropriate production evidence:

- smoke check;
- expected data/state;
- relevant logs/metrics;
- no immediate critical regression;
- evidence recorded.

A successful deployment command is not sufficient.

---

## 14. Recovery Is Broader Than Git Revert

Ask:

> **How do we recover from this change?**

Examples:

| Change type | Typical recovery |
|---|---|
| Stateless code | revert / redeploy |
| Config | restore known-good config |
| Database | backward-compatible migration, restore, or compensating migration |
| External side effect | reconciliation or compensating action |
| Infrastructure | rollback, failover, restore, or rebuild |

Recovery must match the actual failure mode.

---

## 15. Definition of Ready

For I2+ work, coding should normally not start until the team can answer:

1. What are we changing?
2. Why does the current behavior need to change?
3. What is the observable target behavior?
4. What must not change?
5. What surfaces can this affect?
6. What evidence will tell us it works?

Implementation details do not need to be fully known yet.

The behavioral problem and validation intent do.

---

## 16. Definition of Done

Canonical Definition of Done:

> **A production change is DONE only when its behavioral contract is satisfied, required regressions are protected, required integrations are proven at the appropriate evidence level, the released artifact is traceable to canonical source, operational risks have an acceptable recovery path, the target environment has been verified where required, and the project state is left clean and understandable.**

Projects may strengthen this definition.

They should not weaken it without an explicit reason.

---

## 17. Incident Fast Path

Incidents are not processed like ordinary feature work.

Canonical incident flow:

```text
DETECT
   ↓
ASSESS BLAST RADIUS
   ↓
CONTAIN
   ↓
RESTORE SERVICE
   ↓
DIAGNOSE
   ↓
PERMANENT FIX
   ↓
REGRESSION PROOF
   ↓
POST-INCIDENT LEARNING
```

During an incident:

> **Restore safe service before pursuing architectural elegance when the two conflict.**

After stabilization, the permanent fix returns to the normal production workflow.

A hotfix does not erase the need for root-cause correction, regression protection, and cleanup.

See [Incident note template](templates/incident_note.md).

---

## 18. Project Bootstrap Rules

At project initialization, inspect the repository/project before creating agent instructions.

Bootstrap responsibilities include:

- project mission;
- project type;
- repository structure;
- environment;
- upstream conventions;
- build/test commands;
- deployment model;
- frozen/sensitive areas;
- production invariants;
- evaluation/verification rules;
- safety/destructive-operation boundaries.

### `AGENTS.md`

`AGENTS.md` is the stable project contract.

It should contain durable rules such as:

- mission;
- engineering invariants;
- repo conventions;
- verification expectations;
- deployment rules;
- source-of-truth rules;
- safety constraints;
- workflow rules.

It must not be used for transient state.

Do not store in `AGENTS.md`:

- current phase;
- current issue;
- TODO list;
- active parameters;
- latest experiment/test result;
- timestamps;
- chronological history;
- temporary blockers.

### `CLAUDE.md`

`CLAUDE.md` should normally be a thin wrapper:

```text
@AGENTS.md
```

plus only stable Claude-specific instructions when required.

Do not duplicate the entire project contract.

---

## 19. Dynamic State

Dynamic state belongs in dedicated artifacts, for example:

```text
artifacts/
    project_state.json
    validation/
    releases/
    incidents/
    handoffs/

docs/
    architecture/
    decisions/
    runbooks/
```

Create only what the project needs.

Do not manufacture empty bureaucracy.

A minimal `project_state.json` may track:

```json
{
  "active_change": null,
  "change_type": null,
  "impact_level": null,
  "status": "idle",
  "acceptance_contract": null,
  "current_blockers": [],
  "latest_validation": null,
  "deployment_state": null,
  "next_action": null
}
```

This file describes **now**.

It is not a historical diary.

Use Git, issue trackers, decision notes, release history, and logs for history.

---

## 20. Durable Decision Records

Create a decision record only when the decision is consequential and likely to matter later.

Good candidates:

- architecture boundary;
- persistence model;
- compatibility strategy;
- irreversible vendor choice;
- migration strategy;
- security model;
- deployment model.

Do not create decision records for routine implementation details.

---

## 21. Coding-Agent Contract

For significant changes, provide the coding agent with:

1. Objective / outcome
2. Current truth
3. Scope
4. Allowed files/surfaces
5. Frozen files/surfaces
6. Invariants
7. Design intent
8. Implementation slices
9. Commands
10. Required tests
11. Required artifacts
12. STOP conditions
13. Exact completion evidence

The agent must not invent project scope or architecture without evidence.

For large changes, deliver a repository/ZIP handoff when appropriate.

For small changes, provide exact file paths and patches.

---

## 22. Closure Format

Keep closure concise.

Recommended form:

```text
STATUS: CLOSED / PASS

Outcome:
- ...

Evidence:
- ...

Known limitations:
- None / ...

Next:
- ...
```

Do not turn closure notes into a chronological project diary.

See [Closure note template](templates/closure_note.md).

---

## 23. Production Invariants

These rules are canonical:

> **No code-first.**

> **No unexplained architecture rewrite.**

> **No hidden scope expansion.**

> **No manual patching of generated artifacts.**

> **No claiming DONE from mock-only evidence when real integration matters.**

> **No risky irreversible change without recovery thinking.**

> **No transient state inside stable agent contracts.**

> **No endless symptom patching when evidence invalidates the current mental model.**

> **No production completion claim without target-environment verification when the change requires it.**

And equally important:

> **No unnecessary process. Rigor scales with impact.**

---

## 24. Workflow Selection Rule

At the beginning of a new project or major workstream:

1. Classify it as:
   - Academic Research
   - Challenge / Competition
   - Real / Production Engineering
   - Explicit Hybrid
2. Use the matching canonical workflow.
3. For hybrids, keep the optimization criteria separate even when code/data are shared.
4. Do not silently import research or competition success criteria into production engineering.

---

## 25. Final Principle

Production engineering is not complete when code exists.

It is complete when the intended behavior is safely part of the real system, supported by evidence strong enough for the impact of the change, and understandable enough for the next engineer to operate and evolve it.
