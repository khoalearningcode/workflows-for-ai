# Workflows for AI

Three frameworks for three different kinds of work: scientific research, competitive optimization, and production engineering.

Each framework has its own objective and evidence standard. Choose the one that matches the work you are doing.

## Explore the workflows

| Workflow | Primary objective | Read the framework |
| :--- | :--- | :--- |
| **Research** | Develop a defensible scientific contribution and a stronger independent researcher. | [Research framework · v1.1](Research/Canonical_Pure_Academic_Research_Framework_v1.1.md) |
| **Challenge** | Improve expected final/private performance under competition constraints. | [Challenge workflow · v1.1](Challenge/CANONICAL_CHALLENGE_WORKFLOW_v1.1.md) |
| **Production** | Deliver correct, reliable, maintainable, and operable system behavior. | [Production workflow · v1.0](Production/CANONICAL_PRODUCTION_ENGINEERING_WORKFLOW_v1.0.md) |

## At a glance

### Research

**Understand → Question → Experiment → Update beliefs**

An iterative scientific process built around deep understanding, competing explanations, bounded claims, and researcher development.

[Full framework](Research/Canonical_Pure_Academic_Research_Framework_v1.1.md) · [Quick reference](Research/Pure_Academic_Research_Quick_Reference_v1.1.md)

### Challenge

**Measure truthfully → Attack the bottleneck → Let evidence decide**

A closed-loop optimization process built around measurement trust, informative experiments, resource constraints, and hidden-test performance.

[Full workflow](Challenge/CANONICAL_CHALLENGE_WORKFLOW_v1.1.md) · [Quick reference](Challenge/CHALLENGE_QUICK_REFERENCE_v1.1.md) · [Agent execution protocol · v1.0](Challenge/CANONICAL_AGENT_EXECUTION_PROTOCOL_v1.0.md) · [Changelog](Challenge/CHANGELOG.md) · [v1.0 baseline](Challenge/CANONICAL_CHALLENGE_WORKFLOW_v1.0.md)

### Production

**Understand behavior → Make a safe change → Verify the real system**

An engineering process built around observable contracts, validation proportional to impact, traceable releases, and recovery.

[Full workflow](Production/CANONICAL_PRODUCTION_ENGINEERING_WORKFLOW_v1.0.md) · [Change spec](Production/templates/change_spec.md) · [Incident note](Production/templates/incident_note.md) · [Closure note](Production/templates/closure_note.md)

## Choose a starting point

- **A scientific question or paper:** start with Research.
- **A competition, benchmark, or leaderboard task:** start with Challenge.
- **A feature, bug, service, migration, or operational fix:** start with Production.
- **A hybrid project:** use the relevant frameworks while keeping their objectives and success criteria separate.

The full documents are the canonical references. The Research and Challenge quick references are companions for everyday use. The Agent Execution Protocol is an independently versioned, cross-domain companion; `Challenge/reference_tools/` holds an optional, tested clean-source gate. Production templates are copyable starting points for project-specific records.

Version numbers in document titles and filenames identify each framework independently: Challenge **v1.1** (v1.0 kept as a frozen baseline), Agent Execution Protocol **v1.0**, Production **v1.0**, and Research **v1.1**.

## Repository map

```text
.
├── README.md
├── Challenge/
│   ├── CANONICAL_CHALLENGE_WORKFLOW_v1.1.md
│   ├── CHALLENGE_QUICK_REFERENCE_v1.1.md
│   ├── CANONICAL_AGENT_EXECUTION_PROTOCOL_v1.0.md
│   ├── CANONICAL_CHALLENGE_WORKFLOW_v1.0.md
│   ├── CHANGELOG.md
│   └── reference_tools/
│       ├── require_clean_source.py
│       └── test_require_clean_source.py
├── Production/
│   ├── CANONICAL_PRODUCTION_ENGINEERING_WORKFLOW_v1.0.md
│   └── templates/
│       ├── change_spec.md
│       ├── incident_note.md
│       └── closure_note.md
└── Research/
    ├── Canonical_Pure_Academic_Research_Framework_v1.1.md
    └── Pure_Academic_Research_Quick_Reference_v1.1.md
```
