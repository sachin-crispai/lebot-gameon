# Examples Documentation System

This directory tracks environment examples with durable summaries, evidence, and change history.

## Goals
- Keep one canonical folder per example.
- Preserve a dated history trail for every material change.
- Separate direct evidence from inferred ideas.
- Make it easy for multiple agents to extend without conflict.

## Structure
- `docs/examples/<domain>/INDEX.md`: domain catalog and status table.
- `docs/examples/<domain>/_template/`: starter files for new examples.
- `docs/examples/<domain>/<example-id>/summary.md`: current state and recommendation.
- `docs/examples/<domain>/<example-id>/evidence.md`: source-backed facts and confidence.
- `docs/examples/<domain>/<example-id>/history/YYYY-MM-DD-<note>.md`: immutable snapshots.
- `docs/examples/<domain>/sources/`: raw extraction notes and source scans.

## Status Model
- `candidate`: interesting idea, not validated.
- `validated`: enough evidence to justify building.
- `implemented`: example has a working implementation.

## Evidence Confidence
- `direct`: explicitly present in source material.
- `partial`: related hints exist; specifics are extrapolated.
- `inferred`: not present in source; proposed from context.

## Update Protocol
1. Add or update an example's `summary.md`.
2. Append a new dated history file under that example's `history/`.
3. Update the domain `INDEX.md` row and `Last Updated` date.
4. If source research changed, add/update notes in `sources/`.
