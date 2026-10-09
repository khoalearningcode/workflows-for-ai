# Canonical Challenge / Competition Workflow v1.0

**Status:** FROZEN\
**Version:** 1.0\
**Date:** 2026-10-03\
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

Keep the workflow lightweight.

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

Promotion and kill criteria should ideally be written before observing the result.

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

Coding is an experimental instrument, not the source of strategic direction.

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

---

## 31. Operational Mantra

> **Measure truthfully. Attack the bottleneck. Let evidence decide.**

Stricter form:

> **Do not optimize what you cannot trust, and do not build what you have not justified.**
