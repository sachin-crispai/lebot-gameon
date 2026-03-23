# Claims Adjudication Workflow Simulator

## Snapshot
- Example ID: `claims-adjudication-workflow`
- Status: `candidate`
- Last Updated: `2026-03-08`

## Problem
Claims adjudication is a long-horizon, policy-constrained workflow with partial observability: an agent must review case context, request missing evidence, apply changing rules, and decide approval/denial/escalation.

## Environment Proposal
- Agent objective: maximize correct, policy-compliant adjudication decisions while minimizing avoidable escalations.
- State/observation: claim metadata, policy excerpts, prior correspondence, missing-document flags, and time-to-deadline.
- Actions: request document, ask clarification, apply policy rule, approve, deny, escalate.
- Reward design:
  - positive: correct final decision, compliant rationale, timely closure;
  - negative: policy violation, unsupported denial, unnecessary back-and-forth, deadline miss.
- Episode termination: final decision issued or deadline exceeded.

## Why It Matters
This environment directly stresses world modeling and long-horizon instruction-following under realistic enterprise constraints.

## Next Step
Draft a minimal OpenEnv `state/reset/step` spec with a synthetic claim schema and 3 policy scenarios.
