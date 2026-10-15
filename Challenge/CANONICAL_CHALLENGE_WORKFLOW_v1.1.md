# Canonical Challenge / Competition Workflow v1.1

**Status:** PROPOSED CANONICAL (ready for review and project adoption)\
**Version:** 1.1\
**Date:** 2026-10-15\
**Origin:** v1.0 (2026-10-03), preserved as immutable historical baseline\
**Version lineage:** Challenge v1.0 → Challenge v1.1. The newly introduced Agent Execution Protocol starts at its own independent v1.0.\
**Release notes:** `CHANGELOG.md`\
**Companion:** `CANONICAL_AGENT_EXECUTION_PROTOCOL_v1.0.md`\
**Scope:** AI/ML competitions, benchmarks, shared tasks, Kaggle-style challenges, VLSP/Zalo-style competitions, leaderboard-driven evaluation tasks.

---

<details>
<summary>Table of contents</summary>

- [0. Purpose](#0-purpose)
- [1. Core Philosophy](#1-core-philosophy)
- [2. Canonical Lifecycle](#2-canonical-lifecycle)
- [3. State A — Competition Truth](#3-state-a--competition-truth)
- [4. State B — Measurement Trust](#4-state-b--measurement-trust)
- [5. State C — Competitive Anchor](#5-state-c--competitive-anchor)
- [6. State D — Evidence-Driven Optimization Loop](#6-state-d--evidence-driven-optimization-loop)
- [7. Evidence Hierarchy](#7-evidence-hierarchy)
- [8. Experiment Promotion](#8-experiment-promotion)
- [9. Kill Discipline](#9-kill-discipline)
- [10. Failure Characterization and Error Budget](#10-failure-characterization-and-error-budget)
- [11. Uncertainty Register](#11-uncertainty-register)
- [12. Data-Centric Interventions](#12-data-centric-interventions)
- [13. Resource Economics](#13-resource-economics)
- [14. Leaderboard Strategy](#14-leaderboard-strategy)
- [15. Adaptive Overfitting](#15-adaptive-overfitting)
- [16. Evidence Debt](#16-evidence-debt)
- [17. Strategic Review](#17-strategic-review)
- [18. Operating Modes](#18-operating-modes)
- [19. Final System Selection](#19-final-system-selection)
- [20. Ensemble Discipline](#20-ensemble-discipline)
- [21. Project Stop / Deprioritize Criterion](#21-project-stop--deprioritize-criterion)
- [22. Rollback Rules](#22-rollback-rules)
- [23. Minimal Canonical Artifacts](#23-minimal-canonical-artifacts)
- [24. Experiment Card](#24-experiment-card)
- [25. Agent Operating Contract](#25-agent-operating-contract)
- [26. Anti-Patterns](#26-anti-patterns)
- [27. Progress Definition](#27-progress-definition)
- [28. Adversarial Stress Tests for the Workflow](#28-adversarial-stress-tests-for-the-workflow)
- [29. Canonical Control Loop](#29-canonical-control-loop)
- [30. Core Invariants](#30-core-invariants)
- [31. Operational Mantra](#31-operational-mantra)
- [32. v1.1 Execution Architecture](#32-v11-execution-architecture--domain-decisions-versus-implementation-evidence)
- [33. Project protocol from the first truthful day](#33-project-protocol-from-the-first-truthful-day)
- [34. Experiment execution classes and pre-result commitments](#34-experiment-execution-classes-and-pre-result-commitments)
- [35. Git and artifact provenance as experimental controls](#35-git-and-artifact-provenance-as-experimental-controls)
- [36. Incumbent protection, promotion and rollback](#36-incumbent-protection-promotion-and-rollback)
- [37. Resource isolation, reproducibility and long jobs](#37-resource-isolation-reproducibility-and-long-jobs)
- [38. Agent handoff and autonomy envelope](#38-agent-handoff-and-autonomy-envelope)
- [39. Failure response, evidence integrity and recovery](#39-failure-response-evidence-integrity-and-recovery)
- [40. Lightweight adoption and migration](#40-lightweight-adoption-and-migration)
- [41. Version history and compatibility](#41-version-history-and-compatibility)

</details>

## 0. Purpose

This document defines the canonical workflow for challenge/competition projects.

A challenge is treated as a **constrained empirical optimization problem under partial observability**.

The true objective is normally performance on a hidden final/private evaluation distribution. Local validation and public leaderboard results are only imperfect observations of that target.

The workflow therefore optimizes neither experiment count, engineering activity, local score, nor peak public leaderboard score in isolation.

The governing objective is:

$$
\boxed{
\text{Maximize expected final performance by efficiently reducing decision-relevant uncertainty}
}
$$

subject to:

$$
\text{rules, data, compute, runtime, time, submission budget, engineering complexity, and team bandwidth}.
$$

---

## 1. Core Philosophy

### 1.1 Measure before optimizing

Do not optimize what has not earned trust.

Before serious modeling begins, establish:

- the official task definition;
- exact metric semantics;
- evaluator behavior;
- submission format;
- legality constraints;
- available data;
- trustworthy local evaluation.

A high local score is meaningless if the local evaluation does not measure the competition objective.

---

### 1.2 Attack bottlenecks, not attractive ideas

An implementation should not begin merely because a technique sounds promising.

The default reasoning sequence is:

$$
Observation
\rightarrow Explanation
\rightarrow Prediction
\rightarrow Discriminating\ Test
\rightarrow Evidence
\rightarrow Decision
$$

Ideas are candidate interventions, not evidence.

---

### 1.3 Experiments exist to support decisions

Every substantial experiment should answer a decision-relevant question.

A useful experiment should materially affect at least one of:

- belief about a failure mechanism;
- priority of a bottleneck;
- whether a direction should continue;
- whether an intervention deserves escalation;
- which system should be promoted;
- whether local validation can be trusted;
- whether an external submission is justified.

Experiments that cannot change a decision are not automatically progress.

---

### 1.4 Complexity must earn its place

Every added component introduces cost and failure surface.

Examples include:

- larger models;
- additional prompts;
- retrieval stages;
- rerankers;
- tools;
- preprocessing modules;
- ensembles;
- test-time scaling;
- synthetic-data pipelines;
- post-processing rules.

Complexity is retained only when justified by evidence.

---

### 1.5 Expensive actions require stronger evidence

The greater the cost of the next action, the stronger the evidence required before escalation.

A twenty-minute prototype may be justified by limited evidence.

A multi-day training run, large-model deployment, expensive ensemble, or major architectural rewrite requires much stronger evidence.

---

### 1.6 Negative evidence is first-class evidence

A failed hypothesis can be highly valuable if it eliminates a direction.

Past investment is never evidence for future investment.

A killed direction should remain closed unless new evidence shows that a relevant premise has changed.

---

### 1.7 Final/private performance is the real target

Public leaderboard performance is an external observation, not the final objective.

The workflow targets:

$$
E[\text{Final / Private Performance}]
$$

rather than:

$$
\max(\text{Observed Public LB})
$$

Repeated adaptation to public leaderboard feedback can itself create competition-level overfitting.

---

### 1.8 Measure only what can change a decision

Challenge work does not require publication-grade ablation of every component.

Isolation is required when attribution will affect future decisions.

Near a deadline, a verified bundled gain may be retained even if full attribution is incomplete.

---

## 2. Canonical Lifecycle

The workflow has five major states:

```text
A. Competition Truth
        ↓
B. Measurement Trust
        ↓
C. Competitive Anchor
        ↓
D. Evidence-Driven Optimization Loop
        ↓
E. Consolidation & Finalization
```

This is **not a rigid linear pipeline**.

Evidence may trigger rollback:

```text
Truth conflict       → A
Measurement conflict → B
Baseline conflict    → C
Stagnation           → Strategic Review
Critical late issue  → D
```

The purpose of lifecycle states is to expose what kind of uncertainty currently dominates the project.

---

## 3. State A — Competition Truth

### Objective

Know exactly what game is being played.

### Establish

- task definition;
- input schema;
- output schema;
- official metric;
- official evaluator;
- submission schema;
- train/validation/public/private structure;
- external-data policy;
- pretrained-model policy;
- API/internet/tool restrictions;
- runtime/inference limits;
- hardware constraints;
- submission quota;
- competition phases;
- deadline;
- leakage risks;
- rule ambiguities;
- licensing constraints where relevant.

### Exit criterion

The team can explain:

> Given a prediction submission, how is the official score produced, and what determines whether that submission is legal?

State A is never permanently closed. New official information can invalidate previous assumptions.

---

## 4. State B — Measurement Trust

### Objective

Build a measurement system trustworthy enough to choose between competing interventions.

Three questions must be addressed.

#### B1. Evaluator fidelity

Does local evaluation reproduce official scoring behavior?

#### B2. Validation representativeness

Does local validation reasonably approximate the hidden target distribution?

#### B3. Measurement sensitivity

Can the validation setup reliably distinguish improvements of the scale being investigated?

Where relevant, estimate:

- seed variation;
- sampling noise;
- split variance;
- metric uncertainty;
- sensitivity to preprocessing;
- slice imbalance.

---

### 4.1 Validation stack

As the project matures, validation may include:

#### Anchor set

Stable across the project for historical comparability.

#### Representative set

Best current approximation of hidden evaluation.

#### Stress sets

Known difficult, shifted, rare, or high-risk conditions.

#### Diagnostic sets

Small targeted subsets used to test mechanisms.

Not every competition needs all four.

---

### 4.2 Validation may evolve

Validation design is not sacred.

If external evidence repeatedly contradicts local decisions, the validation system should be reconsidered.

However, when validation evolves, preserve a stable anchor whenever possible so historical regressions remain visible.

---

### Exit criterion

The project can meaningfully answer:

> Which of two systems should we prefer, and how confident are we that this preference is relevant to hidden-test performance?

---

## 5. State C — Competitive Anchor

### Objective

Establish a working system strong and transparent enough for meaningful diagnosis.

Three useful baseline levels may exist.

#### Sanity baseline

Proves that:

- data loading works;
- inference works;
- evaluation works;
- submission generation works.

#### Reference baseline

Reproduces an official, public, literature, or strong open-source baseline when available.

#### Competitive anchor

A system strong enough that its remaining errors reflect meaningful competition bottlenecks rather than trivial implementation defects.

---

### 5.1 Baseline principle

A baseline is a **measurement instrument**, not a checkbox.

A strong baseline is useful because it exposes meaningful remaining failures.

---

### 5.2 Competitive frontier

The competitive frontier is contextual evidence derived from credible sources such as:

- official baselines;
- strong public baselines;
- leaderboard performance;
- public writeups;
- released code;
- organizer information;
- reproducible published methods.

It is used to estimate:

- how much headroom remains;
- whether incremental optimization is appropriately scaled;
- whether a major capability may be missing.

It must **not** be used to invent unsupported claims about what top teams are doing.

A leaderboard gap is evidence of headroom, not evidence of mechanism.

---

### Exit criterion

The team knows:

- current verified performance;
- distance from credible reference performance;
- dominant failure categories;
- whether the present solution class remains plausible.

---

## 6. State D — Evidence-Driven Optimization Loop

This is the core engine of the workflow.

Each meaningful iteration follows:

```text
1. Observe
2. Prioritize
3. Explain
4. Predict
5. Test cheaply
6. Update belief
7. Decide
```

---

### 6.1 Observe

Use evidence such as:

- aggregate metrics;
- slice metrics;
- per-example failures;
- parser/execution errors;
- latency;
- calibration;
- model behavior;
- data-quality problems;
- leaderboard transfer;
- robustness failures.

Observation describes what happens.

It does not automatically explain why.

---

### 6.2 Prioritize

Estimate the expected value of attacking each failure.

A useful qualitative model is:

$$
Priority
\propto
\frac{
Frequency
\times Recoverability
\times ScoreImpact
\times Confidence
}{
Cost
}
$$

Exact numerical scoring is optional.

The purpose is disciplined comparison.

---

### 6.3 Explain

Generate one or more mechanism hypotheses.

Weak:

> Hard questions fail because the model is weak.

Better:

> When chart values are manually corrected, downstream reasoning succeeds, suggesting chart-value extraction rather than reasoning is the dominant failure mechanism.

When uncertainty is high, maintain competing hypotheses rather than committing prematurely.

---

### 6.4 Predict

Every serious hypothesis must produce observable consequences.

Example:

> If extraction error is the main mechanism, replacing extracted values with ground-truth values should strongly improve chart-heavy examples while having little effect on text-only examples.

No measurable prediction means the hypothesis is insufficiently specified.

---

### 6.5 Test cheaply

Use the cheapest experiment capable of distinguishing the active explanations.

Preferred escalation order:

```text
Observation
→ Diagnostic probe
→ Oracle / ceiling test
→ Cheap prototype
→ Controlled experiment
→ Full validation
→ External transfer probe
```

Do not jump to expensive implementation if a cheaper discriminating test exists.

---

### 6.6 Update belief

After an experiment, record whether the hypothesis is:

- supported;
- partially supported;
- refuted;
- unresolved;
- invalidated by measurement problems.

Unexpected outcomes should update the model of the problem rather than disappear into logs.

---

### 6.7 Decide

Valid decisions are:

#### KEEP

Retain the intervention.

#### REVISE

The mechanism remains plausible, but the hypothesis or implementation needs modification.

#### KILL

Further investment is not justified.

#### ESCALATE

Evidence is strong enough to justify a more expensive experiment.

#### ROLLBACK

Evidence undermines a foundational assumption about evaluation, baseline, or competition truth.

#### STOP / DEPRIORITIZE

Further work is not justified relative to opportunity cost, deadline, resource budget, or expected attainable gain.

---

## 7. Evidence Hierarchy

### E0 — Observation

Identifies a phenomenon.

Example:

> 38% of failed samples contain incorrect extracted values.

---

### E1 — Diagnostic evidence

Separates competing explanations.

Example:

> Replacing extracted values manually causes downstream reasoning to succeed.

---

### E2 — Oracle / ceiling evidence

Estimates maximum recoverable benefit from solving a subsystem.

Examples:

- oracle OCR;
- oracle retrieval;
- oracle routing;
- oracle program;
- oracle ensemble;
- oracle normalization.

Oracle evidence establishes headroom, not practical attainability.

---

### E3 — Cheap practical prototype

Tests whether a meaningful fraction of oracle headroom can be recovered using a low-cost implementation.

---

### E4 — Controlled experiment

Tests an intervention with enough control that attribution is meaningful.

Change the smallest meaningful set of variables necessary to test the active hypothesis.

---

### E5 — Full-scale / robustness validation

Evaluate on the canonical validation setup and important slices.

Consider:

- aggregate gain;
- regressions;
- variance;
- runtime;
- memory;
- reliability;
- compute cost.

---

### E6 — External leaderboard probe

Use a submission to test external transfer.

Every submission should have a decision-relevant purpose.

---

### E7 — Confirmation

When necessary, verify that an important gain survives:

- alternate splits;
- multiple seeds;
- repeated evaluation;
- public leaderboard;
- stress tests;
- distribution shifts.

Not every intervention requires E7.

---

## 8. Experiment Promotion

A hypothesis does not automatically advance to a more expensive experiment.

Typical logic:

```text
Meaningful failure?
      ↓
Plausible mechanism?
      ↓
Meaningful oracle ceiling?
      ↓
Practical prototype recovers useful fraction?
      ↓
Controlled gain survives?
      ↓
Full validation robust?
      ↓
External transfer worth testing?
```

At every point:

```text
PROMOTE
REVISE
KILL
```

should remain possible.

Avoid:

```text
TRY
→ TRY MORE
→ TRY BIGGER
```

---

## 9. Kill Discipline

Before expensive work, define conditions that would justify stopping.

Example:

```text
Continue only if:

oracle ceiling is meaningful
AND
prototype recovers a useful fraction of that ceiling
AND
major regressions remain acceptable
AND
resource cost is justified by expected gain.
```

Thresholds depend on:

- metric scale;
- uncertainty;
- competitive gap;
- compute;
- deadline;
- inference budget;
- opportunity cost.

Killed hypotheses remain closed unless new evidence changes their premises.

---

## 10. Failure Characterization and Error Budget

Failure analysis must lead to prioritization.

For each meaningful failure class, estimate:

```text
frequency
recoverability
potential score impact
confidence
implementation difficulty
resource cost
```

The output should form an **error budget**, not merely an error taxonomy.

A failure mode should not dominate engineering effort merely because it is technically interesting.

---

## 11. Uncertainty Register

The project should distinguish:

### Known

Supported by evidence.

### Believed

Plausible but not established.

### Unknown

Important unresolved questions.

Each major uncertainty should record:

```text
question
importance
current belief
supporting evidence
cheap next test
```

The active work queue should be driven primarily by high-value uncertainty, not by whichever implementation is easiest to start.

---

## 12. Data-Centric Interventions

Data work is subject to the same evidence discipline as model work.

Examples include:

- label cleaning;
- duplicate removal;
- leakage removal;
- data filtering;
- augmentation;
- synthetic data;
- pseudo-labeling;
- hard-example mining;
- resampling;
- curriculum changes;
- train/validation redesign;
- external data inclusion.

A data intervention should answer:

1. What observed failure suggests a data problem?
2. What mechanism is proposed?
3. What measurable change is predicted?
4. What is the cheapest test?
5. What legality or leakage risks exist?
6. Does the intervention improve representative validation rather than only training behavior?

Synthetic or external data should never be added merely because more data appears beneficial.

---

## 13. Resource Economics

Score is not the only scarce resource.

The workflow treats all of the following as part of the decision budget:

- GPU-hours;
- accelerator availability;
- wall-clock time;
- inference latency;
- memory;
- API cost;
- engineering complexity;
- maintenance burden;
- failure surface;
- submission quota;
- human attention.

A useful intervention can still be strategically poor if its cost is disproportionate to expected gain.

For two candidate actions, reason approximately about:

$$
Expected\ Value
\approx
P(\text{success})
\times
Expected\ Gain
-
Resource\ Cost
-
Operational\ Risk
-
Opportunity\ Cost
$$

This is a reasoning aid, not a requirement to invent artificial numeric precision.

---

## 14. Leaderboard Strategy

### 14.1 Public leaderboard role

Public LB is a low-frequency external sensor.

Local validation is a high-frequency internal sensor.

Neither should replace the other.

---

### 14.2 Submission taxonomy

Useful submission purposes include:

#### Sanity submission

Verify formatting and pipeline.

#### Baseline submission

Establish an external reference.

#### Transfer probe

Test whether a locally verified gain transfers.

#### Paradigm probe

Compare fundamentally different solution classes.

#### Final candidate

Evaluate a mature candidate for final selection.

A submission without a decision-relevant purpose should normally not consume quota.

---

### 14.3 Transfer tracking

For meaningful system changes, track:

```text
Local delta
Expected leaderboard behavior
Observed leaderboard delta
Relevant slices
Interpretation
Transfer confidence
```

Leaderboard evidence should gradually improve understanding of which local measurements predict external performance.

---

### 14.4 Local–LB disagreement

#### Local ↑ / LB ↑

Supports transfer.

#### Local ↑ / LB flat or ↓

Possible causes include:

- non-transfer;
- validation mismatch;
- noise;
- slice imbalance;
- evaluator mismatch.

Investigate before making broad changes.

#### Local ↓ / LB ↑

Strong evidence that local validation preference may be misaligned.

Repeated occurrences trigger rollback to Measurement Trust.

---

## 15. Adaptive Overfitting

Three distinct risks exist.

### Model overfitting

The model adapts excessively to training data.

### Researcher overfitting

Project decisions adapt excessively to a repeatedly reused validation set.

### Competition overfitting

The project adapts excessively to public leaderboard feedback.

As validation or leaderboard exposure increases, increase reliance on fresh evidence such as:

- held-out data;
- alternate splits;
- cross-validation;
- robustness testing;
- independent stress sets.

---

## 16. Evidence Debt

Evidence debt is created when multiple simultaneous changes accumulate without knowing which changes caused the gain.

Evidence debt may be acceptable when:

- deadline is near;
- bundled gain is large and verified;
- attribution will not affect remaining decisions.

Evidence debt is dangerous when:

- early in the competition;
- architecture is still changing;
- future decisions depend on understanding component value.

Accumulate evidence debt deliberately, not accidentally.

---

## 17. Strategic Review

Strategic Review is triggered when meaningful optimization cycles repeatedly fail to produce verified progress.

The exact trigger depends on experiment cost and competition duration.

Review:

1. Are we optimizing the correct metric?
2. Is validation trustworthy?
3. Are we attacking the dominant bottleneck?
4. Is the current solution class fundamentally weak?
5. Is there a strong public/reference capability we have failed to reproduce?
6. Which major assumption, if false, would best explain stagnation?
7. Is the scale of our intervention consistent with the competitive gap?
8. Are data quality or data construction the real bottleneck?
9. Has resource allocation become irrational relative to expected gain?

Strategic Review may justify a paradigm shift, but not because the team is bored with the current approach.

---

## 18. Operating Modes

These modes describe optimization policy, not lifecycle stage.

### Exploration

Use when uncertainty is high.

Optimize approximately for:

$$
\frac{\text{decision-relevant information}}
{\text{time + compute + submission cost}}
$$

Typical actions:

- diagnostic probes;
- oracle tests;
- competing hypotheses;
- cheap prototypes;
- data audits.

---

### Exploitation

Use when important bottlenecks and mechanisms are reasonably established.

Optimize approximately for:

$$
\frac{\text{verified score gain}}
{\text{time + compute}}
$$

Typical actions:

- strengthen proven mechanisms;
- larger runs;
- targeted fine-tuning;
- justified data interventions;
- system integration;
- justified ensembles.

---

### Consolidation

Use when deadline pressure and system maturity are high.

Optimize:

$$
ExpectedFinalPerformance
-
RegressionRisk
-
OperationalRisk
$$

Typical actions:

- freeze stable core;
- verify reproducibility;
- validate runtime;
- eliminate fragile dependencies;
- verify final artifacts;
- select robust ensemble/fallback behavior.

A project may move between Exploration and Exploitation multiple times.

---

## 19. Final System Selection

The highest observed public-LB system is not automatically the best final/private system.

Final candidates should be evaluated using:

- representative local performance;
- external transfer;
- variance;
- slice robustness;
- validation exposure;
- leaderboard exposure;
- distribution sensitivity;
- runtime;
- compute cost;
- operational reliability;
- ensemble diversity.

When possible, final candidates should represent meaningfully different risk profiles rather than near-identical leaderboard-tuned variants.

---

## 20. Ensemble Discipline

Ensembling is justified by complementary error structure, not simply by combining strong models.

Before investing heavily, estimate oracle ensemble headroom.

If two systems fail on nearly identical examples, expected ensemble gain is limited.

If their errors are complementary, ensemble or routing work may be justified.

---

## 21. Project Stop / Deprioritize Criterion

A challenge should not be assumed worthy of unlimited continued effort.

STOP or DEPRIORITIZE becomes valid when evidence suggests that:

- expected attainable gain is too small relative to remaining effort;
- competitive gap is unlikely to close under available compute/time;
- rules or resource constraints make the intended approach infeasible;
- external evaluation repeatedly contradicts the project’s strongest local evidence;
- the opportunity cost of continuing exceeds the strategic value of the challenge;
- another project has substantially higher expected value;
- a hard deadline makes further exploration irrational.

Stopping is not failure when it is an evidence-based allocation decision.

A stopped project should preserve:

- best known system;
- current score;
- key evidence;
- unresolved uncertainties;
- reason for stopping;
- conditions under which reopening would be justified.

---

## 22. Rollback Rules

### Return to Competition Truth when

- metric interpretation changes;
- official rules change;
- hidden submission behavior contradicts assumptions;
- legality constraints are newly discovered.

### Return to Measurement Trust when

- local gains repeatedly fail externally;
- validation results are unstable;
- split leakage is suspected;
- expected and observed transfer diverge systematically.

### Return to Competitive Anchor when

- baseline implementation is found incorrect;
- a credible public baseline is dramatically stronger;
- core architectural assumptions prove invalid.

### Return from Finalization to Optimization when

a critical regression or high-value new piece of evidence materially changes expected final performance.

---

## 23. Minimal Canonical Artifacts

Keep the workflow lightweight. **The tree below is a potential mature-state layout, not a compulsory scaffold.** Bootstrap a truthful `docs/challenge_protocol.md` first (see §33); create each other artifact only when it has actual decision-useful content.

Recommended state:

```text
artifacts/
├── project_state.json
├── uncertainty_register.md
├── error_budget.md
├── experiment_log.csv
├── submission_log.csv
└── decisions/
```

---

### project_state.json

Contains current state only:

```text
workflow_version
lifecycle_state
operating_mode
best_verified_local_system
best_external_result
current_system
active_bottleneck
active_hypotheses
major_uncertainties
resource_budget
deadline
submission_budget
```

It is not a diary.

---

### experiment_log.csv

Minimal fields:

```text
experiment_id
decision_question
hypothesis
intervention
prediction
result
interpretation
decision
```

---

### submission_log.csv

Minimal fields:

```text
system_id
submission_purpose
local_performance
expected_external_behavior
public_score
delta
interpretation
transfer_confidence
```

---

### decisions/

Store durable consequential decisions:

- killed hypotheses;
- architecture changes;
- evaluator corrections;
- strategic pivots;
- stop/deprioritize decisions.

---

## 24. Experiment Card

Before a meaningful experiment:

```text
Experiment ID:

Decision question:

Observation:

Hypothesis:

Existing evidence:

Prediction:
If the hypothesis is true, what should happen?

Minimal test:

Primary metric:

Relevant slices:

Controls:

Resource cost:

Promotion criterion:

Kill criterion:
```

After execution:

```text
Result:

Interpretation:

Decision:
KEEP / REVISE / KILL / ESCALATE / ROLLBACK / STOP
```

For decision-bearing runs, promotion and kill criteria **must** be fixed before the relevant outcome is observed. For scratch/diagnostic work they are encouraged but may remain exploratory when clearly labeled. Preserve pre-result plans and post-result judgments as distinguishable records (see §§34–35).

---

## 25. Agent Operating Contract

### Research / Experiment Lead

Responsible for:

- deciding which uncertainty matters;
- selecting hypotheses;
- prioritizing experiments;
- interpreting evidence;
- deciding promotion, kill, rollback, strategic review, or stop.

### Coding Agent

Responsible for:

- faithfully implementing the specified experiment;
- preserving controls and invariants;
- running requested checks;
- reporting artifacts and results.

The coding agent should not autonomously create a new research direction merely because it is technically feasible.

Coding is an experimental instrument, not the source of strategic direction. Within a properly scoped work order, the coding agent should execute end-to-end without asking for approval on routine implementation details, but must escalate unauthorized strategy, dataset, metric, submission, spending, or deployment changes. See §§35–39 and the execution companion.

---

## 26. Anti-Patterns

Explicitly discouraged:

### Idea-first experimentation

> “Let's try X.”

without an observation or decision question.

### Architecture hopping

Changing solution class without evidence that the current class is inadequate.

### Scale rescue

Responding to ambiguous evidence by immediately using a larger model or more compute.

### Benchmark theater

Producing many experiments, tables, and metrics without changing decisions.

### Submission spam

Using leaderboard quota merely to inspect scores.

### Local metric worship

Treating local performance as the true objective after transfer evidence contradicts it.

### Public-LB worship

Selecting systems solely by peak public score.

### Sunk-cost continuation

Continuing because substantial effort has already been invested.

### Uncontrolled bundles

Changing many variables simultaneously when attribution matters.

### Ablation obsession

Isolating effects when the answer cannot alter remaining decisions.

### Endless incrementalism

Continuing tiny optimizations when the scale of the competitive gap suggests a missing capability.

### Data expansion without evidence

Adding synthetic/external data simply because more data appears desirable.

### Resource blindness

Accepting tiny gains at disproportionate runtime, engineering, or compute cost without justification.

---

## 27. Progress Definition

Two forms of progress are legitimate.

### Epistemic progress

The project becomes materially less uncertain about:

- failure mechanisms;
- validation quality;
- hidden distribution;
- data quality;
- solution-class viability.

### Performance progress

Credible evidence shows improvement in expected final performance.

A healthy project may temporarily produce epistemic progress without score gain.

However, prolonged epistemic activity without verified performance improvement must trigger Strategic Review.

---

## 28. Adversarial Stress Tests for the Workflow

Before declaring the workflow healthy in a project, check the following cases.

### Case 1 — Public data releases late

Continue only with work that does not require unreleased data:

- rules verification;
- evaluator study;
- literature;
- reference-system planning;
- infrastructure preparation;
- hypothesis preparation.

Do not fabricate dataset-dependent conclusions.

---

### Case 2 — Local metric is noisy

Increase repeated evaluation, larger validation coverage, or uncertainty estimation before treating small deltas as real.

Do not chase sub-noise improvements.

---

### Case 3 — Submission quota is tiny

Reserve submissions for high-information transfer probes and mature candidates.

Local measurement quality becomes more important.

---

### Case 4 — Submission quota is huge

Do not treat abundance as permission for leaderboard training.

Adaptive overfitting remains possible.

---

### Case 5 — Compute is severely limited

Increase reliance on:

- oracle tests;
- small discriminating probes;
- frozen-model diagnostics;
- data analysis;
- low-cost prototypes.

High-cost experiments must clear a higher evidence bar.

---

### Case 6 — Large gap to frontier

Before tuning small details, ask whether a missing capability, baseline reproduction failure, data issue, or solution-class mismatch explains the scale of the gap.

---

### Case 7 — Local improvements repeatedly fail on LB

Rollback to Measurement Trust.

Do not continue adding model complexity until the transfer problem is understood.

---

### Case 8 — A bundled system suddenly scores much higher

Keep the gain if necessary, but explicitly mark evidence debt.

Repay the debt only if attribution still matters for future decisions.

---

## 29. Canonical Control Loop

```text
Competition truth
        ↓
Measurement system
        ↓
Competitive system
        ↓
Observe behavior
        ↓
Identify highest-value uncertainty
        ↓
Form competing explanations
        ↓
Design cheapest discriminating evidence
        ↓
Update beliefs
        ↓
Choose intervention
        ↓
Validate
        ↓
External transfer probe when justified
        ↓
Update validation + beliefs
        └──────────────→ repeat
```

The challenge workflow is therefore best understood as a **closed-loop control system**, not a sequential checklist.

---

## 30. Core Invariants

1. Official rules and evaluator semantics define the legal scoring objective.
2. Do not optimize measurements that have not earned trust.
3. Observation precedes intervention.
4. Every substantial experiment must support a decision.
5. Hypotheses must produce measurable predictions.
6. Prefer the cheapest experiment capable of falsifying the active explanation.
7. Expensive actions require proportionally stronger evidence.
8. Complexity must earn its place through evidence.
9. Negative evidence is preserved and respected.
10. Public leaderboard feedback updates beliefs; it does not issue commands.
11. Repeated local–external disagreement triggers examination of measurement before random model changes.
12. Submission quota is an experimental resource.
13. Past cost does not justify future investment.
14. Evidence must not be generalized beyond the population actually tested.
15. Repeated lack of verified progress triggers strategic review.
16. Near deadline, preserving verified performance dominates speculative novelty.
17. Final selection targets expected private performance, not peak public leaderboard score.
18. Measure only what can change a decision.
19. Data interventions require the same evidence discipline as model interventions.
20. Resource cost is part of the objective, not an afterthought.
21. STOP or DEPRIORITIZE is valid when supported by evidence and opportunity cost.
22. Distinguish code correctness, measurement validity, and competition-relevant evidence.
23. A decision-bearing run must identify code, resolved configuration, data, model, evaluator and raw results.
24. Do not silently edit raw cited outputs, revise criteria after inspecting results, or convert dirty diagnostics into clean evidence.
25. Preserve a restorable incumbent and exact external-submission lineage across failed challengers.
26. Grow the project repository from actual needs, not template-driven empty files.
27. Coding agents execute authorized work autonomously but do not self-authorize strategic directions, external submissions, or destructive shared-resource actions.

---

## 31. Operational Mantra

> **Measure truthfully. Attack the bottleneck. Let evidence decide.**

Stricter form:

> **Do not optimize what you cannot trust, and do not build what you have not justified.**

---

## 32. v1.1 Execution Architecture — domain decisions versus implementation evidence

The canonical Challenge workflow remains the decision authority. It governs which uncertainty matters, what a valid improvement means, when exploration should end, and how public/private leaderboard information is used. The **Canonical Agent Execution & Evidence Protocol v1.0** (companion document) governs safe repository work, Git/run provenance, data/model lineage, and coding-agent handoff.

The two contracts operate together:

```text
Competition Truth ──► Measurement Trust ──► Competitive Anchor
                           │                         │
                           └────────► Evidence-Driven Optimization
                                                │
                                    [decision-bearing work order]
                                                ▼
                      Agent Execution & Evidence Protocol
                   audit → plan → implement → verify → commit
                       → clean run → analyze → preserve → report
                                                │
                                  evidence / invalidation
                                                ▼
                        KEEP / REVISE / KILL / ESCALATE
                           / ROLLBACK / STOP / PROMOTE
                                                │
                                   back into domain loop
```

The arrows depict dependencies **not** a compulsory stage-by-stage schedule. A small diagnostic can take minutes and leave no new file. A promotion-grade run may need all technical controls. Neither coding throughput nor commit count is a score of competition progress.

**Source of authority when rules conflict:** official competition rules and law/data permissions > user-authorized scope and safety > this Challenge workflow's decision principles > the generic execution companion > local coding preferences. Escalate rather than silently choose an incompatible interpretation.

### 32.1 What to reuse from academic research

Reuse: falsifiable questions, explicit alternative explanations, honest negative results, distinction between exploratory/confirmatory evidence, measurement validity, reversible decisions, and source-anchored claims. **Do not import** paper novelty obligations, researcher-mastery checks, publication-tier ambitions, venue selection, or full scientific pre-registration as universal competition requirements. A Challenge's primary end is expected **legal private/final performance** under resource and deadline constraints.

### 32.2 Three independent validity axes

For consequential work, distinguish:

1. **Code correctness:** implementation and invariant tests pass.
2. **Measurement trust:** evaluator, dataset identity, split boundaries, comparison design and uncertainty are adequate.
3. **Competition relevance:** improvement plausibly transfers to the official hidden target at acceptable rules/runtime cost.

A pass on one axis cannot be used to claim a pass on another. This makes bugs, metric problems and model limitations distinguishable rather than burying all three in a single 'score'.

## 33. Project protocol from the first truthful day

At a new Challenge project's start, create a concise `docs/challenge_protocol.md` **with real content**, after inspecting the workspace and known organizer information. It is both the evolving project-specific interpretation of this canonical workflow and the interface through which the lead delegates decision-bearing work. It should begin with known facts and explicit unknowns rather than fabricated dataset or accuracy claims.

It should be able to answer, at the current time:

- **Mission and constraints:** task, legal resources, scoring target, deadlines, quota, target runtime and hardware. Unknown competition rules are marked unverified, not guessed.
- **Evidence state:** observed local, reported organizer/source, inference, hypothesis, decision, unknown. Attach links or artifact IDs to consequential claims.
- **Evaluation contract:** exact official scorer/version, formats, split policy, validation contamination risks and what local metrics can/cannot demonstrate.
- **Current verified anchor:** baseline identity, source SHA, model/data/evaluator references and outstanding reproduction limitations.
- **Highest-value uncertainty:** active bottleneck, competing explanations, cheapest discriminating experiment and why it matters.
- **Decision record:** pre-decided criteria for meaningful tests, negative results, belief updates, accepted trade-offs and explicit closed directions.
- **Candidate status:** incumbent versus experimental challenger, next promotion or external-transfer gate.

This is a **living decision contract**, not an append-every-log dump. Condense durable conclusions in it and link to immutable experiment artifacts. Source code, generated data, raw metrics and executable configurations stay in their proper locations. Do not generate a new protocol per round; Git history and referenced decision entries provide revision lineage.

### 33.1 File naming and just-in-time repository growth

Semantic source names use stable `lower_snake_case` and describe responsibilities (e.g. `scoring.py`, `manifest.py`, `routing.py`, `inference.py`) rather than stage, status or calendar date. Never create `phase_3_final_v7.py` or `best_model_final_final.py`. Dated or hashed **run directories** are appropriate, because run instances genuinely need unique identities.

Do not force the exact `artifacts/` tree in §23 into every new project. Establish only directories required by real files, reuse meaningful existing structures and retain the ability to evolve the organization. Avoid duplicating one evolving metric across protocol, README, dashboard and logs without defining which one is authoritative.

## 34. Experiment execution classes and pre-result commitments

Distinguish experiments by how much consequential trust they must bear:

| Class | Main purpose | Source/run requirements | Allowed conclusion |
| --- | --- | --- | --- |
| Scratch / smoke | Integration feasibility, exceptions and obvious bugs | May run dirty if declared; no mandatory formal card | Engineering feasibility only |
| Diagnostic / oracle | Distinguish mechanisms or estimate upper bounds | Controls, identifiers, scope/limitations; reproducibility proportional to consequence | Bounded exploratory learning, not deployable gain |
| Decision-bearing | Choose method, retire hypothesis, allocate major compute | Document interpretation/promotion rules before seeing this result; source snapshot; immutable run lineage | Evidence for KEEP/REVISE/KILL/ESCALATE |
| Promotion-grade | Replace incumbent or prepare final artifact | Clean pinned source + model/data/config/evaluator; representative + stress checks; reproducible packaging | Candidate may be promoted if all pre-authorized gates pass |
| External submission | Test transfer or submit final system | Legal/runtime/schema checks, immutable exact bytes and submission ID, explicit quota authorization | External evidence; not automatic proof of private gain |

The correct level of rigor depends on decision impact, not a fixed number of minutes, files, seeds, or confidence intervals. Before result exposure, register substantial experiment outcomes that would justify `KEEP`, `REVISE`, `KILL`, `ESCALATE` or `ROLLBACK`. If pilot outcomes are known already, disclose them before fixing confirmatory criteria. Never move a failed pass threshold after reading results and call it pre-registered success.

Near a hard deadline, a **validated bundled improvement** may be retained with explicitly recorded evidence debt, as v1.0 already permits. But runtime/rule validity and revertability cannot be sacrificed merely to reduce paperwork.

## 35. Git and artifact provenance as experimental controls

**Git history is not itself scientific evidence**, but it protects the chronological relation between plan, executable treatment, observation and decision. A reliable official comparison identifies *exactly* what source was used, not just a branch called `main`.

A normal consequential iteration has the following semantic checkpoints (combine low-impact commits where appropriate):

```text
[Baseline protected / worktree audited]
   └─ Plan and criteria fixed  ─────────► commit P
      └─ Code and correctness validated ► commit C
         └─ Clean-source run            ► run_id, source_sha=C
            └─ Raw outputs retained, interpreted under P
               └─ Decision and evidence references ► commit D
                  └─ Promotion, only if approved    ► tag/record S
```

Guardrails:

- Do not assume the execution checkout is the canonical repo; resolve root, remote and existing work first.
- Decision-bearing runs refuse unexpected tracked/staged/untracked **source** changes; ignored results do not make source dirty. A dirty diagnostic run must say so and preserve any relevant patch fingerprint.
- Use meaningful commits; no Git `add .` around huge data, checkpoints, credentials or artifacts. A dedicated branch/worktree isolates risky parallel experiments; branching per stage is unnecessary.
- Every dataset manifest needs a stable digest and data-revision identity; every model needs a revision/hash. A Git commit by itself does **not** identify mutable external inputs.
- Cite run identifiers and config/manifest digests in decisions and promotion records. Raw artifacts must not be rewritten to fit a later interpretation.
- Retain important checkpoints in an appropriate artifact store, with checksum and license/access controls. Public upload requires permission; private evaluation data must not be published accidentally.

The companion provides operational run manifest and ownership fields, plus an optional tested reference clean-source guard at `reference_tools/require_clean_source.py`. Use a repo-level `AGENTS.md`/`CLAUDE.md` only for stable local agent rules after inspecting the actual workspace. This workflow does not mandate a particular orchestrator, tracker, CLI framework or Git hosting platform.

## 36. Incumbent protection, promotion and rollback

A Challenge has four different evolving objects that must not be conflated:

| Object | Meaning | May be overwritten? |
| --- | --- | --- |
| Working candidate | Today's experimental code/model/ensemble | Yes, under normal development control |
| **Incumbent** | Best **verified**, legally usable system according to the decision rule | No; preserve recoverable source/config/model lineage |
| Submission candidate | Packaged, validated version proposed for external upload | No after freeze; create new candidate for changes |
| Submitted artifact | Exact exported bytes used in an official submission | Never silently mutate; store checksum and external ID |

A challenger must earn promotion through metric fidelity, representative performance, key failure slices, variance where material, runtime/memory/inference contract, external-data legality, and reproducible artifact generation. The highest local score is *not* an unconditional promotion. Baseline selection is contextual: a candidate may beat on one slice but be worse for expected private distribution or operational risk.

Decisions must show incumbent vs challenger comparison including known uncertainties. Failures leave the incumbent unchanged; if the incumbent was invalidated, perform a justified rollback to the strongest independently verified fallback. `git revert` alone is not a model rollback: restore config, preprocessing, tokenizer, checkpoint, evaluator and environment as needed.

### 36.1 External leaderboard transfer

Treat every submission as a budgeted experiment with purpose (`sanity`, `baseline`, `transfer_probe`, `paradigm_probe`, `final_candidate`). Before submission freeze the artifact and an expectation about how local gains should transfer. Record external ID, time, score, quota spent and delta, keeping local metrics and public/private scores **separately labelled**. Repeated disagreement returns the project to State B; never blindly tune against public feedback. If the organizer disallows reuse of validation/test signals, those restrictions outrank local preferences.

## 37. Resource isolation, reproducibility and long jobs

A run is not reproducible merely because `seed` and a Git SHA were written down. For decision-bearing runs, use a lineage chain covering code, resolved config, data split/manifest, model/tokenizer weights, evaluator, stochasticity, hardware/software environment and raw predictions. On meaningful promotions, perform a restoration/rerun check when feasible rather than treating metadata completeness as proof.

Before costly execution, inspect shared GPU load, memory, relevant jobs and disk headroom. Do not kill or pause other people's jobs. Prefer isolated checkouts and unique run directories for background training or inference; append-only results and checkpoints must survive interruption without pretending partial progress is a complete run. Record contention and instrumentation conditions where timing matters; distinguish estimated performance models from measured end-to-end latency.

A partial or interrupted run can be retained as diagnostic evidence only with a clear `interrupted`/`partial` status, completed-ID accounting and resumption checks. Never reuse a run ID for a logically changed experiment. Prefer new corrected analysis or superseding runs rather than in-place edits.

## 38. Agent handoff and autonomy envelope

The lead sends a **bounded, decision-bearing work order**: current truth, requested goal, permitted experiments/compute/data, protected invariants, tests/metrics, stopping criteria and escalation boundary. The coding agent then autonomously performs the approved steps to completion, including routine test/debug/documentation/commit actions; it does not invent a strategic successor experiment merely because GPU time is available.

Each work order produces one main report:

```text
Verdict (pass/fail/revise/blocked + one-sentence takeaway)
Implemented (real paths and change scope)
Checks (correctness vs measurement validity vs result)
Run evidence (actual values, denominators, uncertainty/limitations)
Provenance (commit SHA, run IDs, model/data/config/evaluator identities)
Interpretation (what changed belief, what does not follow)
Decision / next action (only strategic owner approval if required)
```

The agent must not report nonexistent commits, fabricated official runs, or unverified benchmark improvements. If a report is based on a dirty/partial/synthetic run, say so plainly. The lead reviews the scientific/competition interpretation rather than trusting an agent's recommendation as an automatic decision.

## 39. Failure response, evidence integrity and recovery

When a bug or new organizer rule invalidates prior results, do not hide the failure. Keep the original run and mark it superseded/invalid; identify dependent decisions, manifests, promoted candidates and submissions. Fix the contract/evaluator or code, add regression coverage, rerun comparisons from verified states and explicitly update beliefs. The evidence trail must show *what was believed before*, *what was discovered*, and *what was changed*.

Classify at least: implementation defect, evaluator/scorer mismatch, data leakage or distribution problem, unstable measurements, environment/runtime confound, true hypothesis failure, strategy mismatch. This prevents routine code repair from being confused with method improvement, and prevents weak metrics from being presented as strong evidence.

Even after the official competition closes, retain enough information to reconstruct the final entry, score and key negative results. Retention must respect data licenses and privacy/secret policies; do not archive prohibited private challenge samples.

## 40. Lightweight adoption and migration

For a **new project**, a truthful protocol and safe repository baseline are sufficient to start. Add tests/manifests/configs/registries/trackers when actual work demands them. A challenge that never receives public training data may stay in State A without pretending to have measured a baseline.

For an **existing messy project**, do not instantly rename every folder or rebuild the pipeline. First reconstruct current state, audit rule/evaluator truth, protect working checkpoints, choose the best verifiable baseline, establish Git source of truth, then migrate one meaningful component at a time. Maintain working behavior during migration and capture the before/after lineage.

For an **active competition under deadline**, use an adoption priority ladder: (1) legality/evaluator and viable submission, (2) preserve best artifact, (3) record model/source/config lineage, (4) reliable validation and promotion tests, (5) improve layout and documentation where it reduces real risk. Full ceremony must not displace expected final score.

### 40.1 Minimal readiness test

A project is ready for trustworthy agent-driven optimization when the team can answer:

1. What is the exact legal scoring objective and official evaluator?
2. What verified system is the incumbent and can it be restored?
3. What observed bottleneck and competing explanations justify the next test?
4. Will the planned run tell us a decision-relevant answer, and were the criteria fixed before relevant outcomes were seen?
5. Can we identify and re-score that run from source/config/data/model/evaluator hashes?
6. If the challenger fails or a job is interrupted, can we resume or roll back without losing the incumbent?
7. What external evidence may transfer to the private test, and what is the remaining deadline/quota budget?

“No” is not an invitation to manufacture an artifact; it reveals the highest-value missing prerequisite.

## 41. Version history and compatibility

### v1.1 — 2026-10-15 (proposed)

**Preserved from v1.0:** competition-specific truth and measurement gates, competitive anchor, the evidence-driven decision loop, E0–E7 evidence hierarchy, oracle/ceiling discipline, data-centric interventions, deadline/resource economics, public/private leaderboard epistemology, STOP/ROLLBACK rules and the separation of experiment lead from coding agent.

**Added/clarified:** (1) a domain-vs-execution architecture; (2) truthful, continuously updated project protocol; (3) just-in-time filesystem semantics; (4) proportional scratch/diagnostic/decision/promotion/submission evidence classes; (5) Git clean-source and pre-result decision chronology; (6) run lineage and immutable artifacts; (7) incumbent/challenger/submission identities and promotion/rollback; (8) shared compute ownership and interrupted-run controls; (9) bounded coding-agent autonomy and a verifiable handoff; (10) fault correction and pragmatic adoption from existing repos.

**Not added:** mandatory phase-named files, one branch per stage, one pre-registration file per trivial test, empty folders, publication-style novelty obligations, prescribed Git hosting or tracker tools. The external companion is **normative for consequential agent-executed work when adopted**, but does not claim to have been installed or tested in a project.

### v1.0 — 2026-10-03

Initial frozen canonical Challenge/Competition workflow. Historical v1.0 file remains unchanged as a rollback/reference point.

---

> **v1.1 operating identity:** Optimize expected private performance using evidence that can be traced to an executable system. Protect the incumbent; let failed experiments change beliefs; let source/run history preserve the truth rather than manufacture progress.
