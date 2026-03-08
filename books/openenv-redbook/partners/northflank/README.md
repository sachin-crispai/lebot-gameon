# Northflank Partner Workspace

Structured workspace for Northflank access/setup and future partner-scale operations.

## Directory Layout

- `00-sources/`: canonical source docs and PDFs
- `10-plan/`: digests, runbooks, phased execution plans
- `20-environment/`: local environment checks and setup state
- `30-operations/`: executable scripts and operational commands
- `40-evidence/`: run logs and screenshots
- `90-archive/`: raw fetch artifacts and historical snapshots

## Start Here

1. Read `10-plan/EXTRA_INFO_RUNBOOK.md`
2. Run Phase 1 scripts from `30-operations/scripts/`
3. Save logs to `40-evidence/logs/`
4. Update `20-environment/local/PHASE1_LOCAL_PREREQUISITES.md`

## Current Progress

- Phase 1 local prerequisites executed.
- Node/npm detected and Northflank CLI installed.
- Remaining Phase 1 item: `northflank login` authentication.
