# Incident Note Template v1.0

Companion to [Production Engineering Workflow v1.0](../CANONICAL_PRODUCTION_ENGINEERING_WORKFLOW_v1.0.md).

Copy this template into the project when handling an incident. Record facts as they become known; label hypotheses and keep unknowns explicit. Use timestamps with a timezone.

## Assessment

- **Incident:** [Name / ID]
- **Status:** [Investigating / contained / service restored / closed]
- **Detected at:** [Timestamp and timezone]
- **Affected behavior:** [Observed symptoms and supporting evidence]
- **Blast radius:** [Affected users, services, and data]
- **Owner:** [Responsible person or team]

## Containment and restoration

- **Containment:** [Action, timestamp, and observed effect]
- **Restoration:** [Action, timestamp, and observed effect]
- **Verification:** [Real behavior, metrics, logs, and data/state checks]
- **Remaining risk:** [Unresolved impact or follow-up monitoring]

## Diagnosis and permanent fix

- **Verified root cause:** [Cause and evidence, or explicitly unknown]
- **Contributing factors:** [Supporting evidence]
- **Permanent fix:** [Change spec / patch reference]
- **Regression evidence:** [Checks that protect the failure mode]
- **Recovery / reconciliation:** [Any data or external effects requiring repair]

## Learning and follow-up

| Action | Owner | Completion evidence |
| :--- | :--- | :--- |
| [Concrete follow-up] | [Owner] | [Evidence / link] |

- **Lessons:** [Changes to detection, prevention, or response]
- **Closure evidence:** [Why the incident can be considered closed]
