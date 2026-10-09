# Change Spec Template v1.0

Companion to [Production Engineering Workflow v1.0](../CANONICAL_PRODUCTION_ENGINEERING_WORKFLOW_v1.0.md).

Copy this template into the project for a non-trivial change. Keep only sections relevant to its impact; replace bracketed prompts with concrete information and evidence links.

## Outcome and current truth

- **Change:** [Name and type]
- **Desired outcome:** [Observable user/system behavior]
- **Current truth:** [Observed behavior, reproduction, and evidence]
- **Impact:** [I0–I4 and rationale]

## Behavior contract

- **Acceptance criteria:** [Observable conditions for success]
- **Failure behavior:** [Expected behavior when relevant operations fail]
- **Invariants:** [Compatibility, data, authorization, or resource requirements]

## Scope and design

- **In scope:** [Allowed files and surfaces]
- **Out of scope / frozen:** [Boundaries]
- **Design:** [Smallest safe change and why]
- **Implementation slices:** [Ordered, independently verifiable steps]

## Validation and delivery

| Required evidence | Check / command | Pass condition | Result / artifact |
| :--- | :--- | :--- | :--- |
| [Relevant validation level] | [How to check] | [Expected behavior] | [Fill after execution] |

- **Deployment:** [Target environment, source revision, artifact, and promotion steps]
- **Observability:** [How success and failure will be detected]
- **Recovery:** [Rollback, restore, reconciliation, or compensating action]

## Stop and completion

- **STOP conditions:** [Evidence that requires returning to diagnosis, design, or scope review]
- **DONE evidence:** [Exact evidence needed to satisfy the behavior contract and required verification]
- **Open questions:** [Unresolved assumptions or blockers]
