# Northflank Operations Shortcuts

This is the abbreviated command guide for Northflank operations.

Pattern:
- `northflank <operation> <action>`

These are shorthand labels used in planning and execution notes.  
Run the mapped command shown below.

## Authentication and Local Setup

- `northflank auth`
  - `northflank login --do-not-open-browser`
  - Complete browser login from the printed URL.

- `northflank setup cli`
  - `bash books/openenv-redbook/partners/northflank/30-operations/scripts/setup_northflank_cli.sh`

- `northflank preflight`
  - `bash books/openenv-redbook/partners/northflank/30-operations/scripts/preflight_check.sh`

## Access and Visibility

- `northflank projects list`
  - `northflank list projects`

- `northflank project services`
  - `northflank list services --project hackathon`

- `northflank context show`
  - `northflank context show`

## Phase 4 (Service Baseline) Explained

`northflank phase4 start` means: create the first working GPU service in the `Hackathon` project with safe defaults.

Checklist:
1. Start with Jupyter + PyTorch image (recommended baseline).
2. Set enough CPU/memory plan.
3. Assign one H100 GPU.
4. Set ephemeral storage to 5-10 GB.
5. Add persistent volume if model/data must survive restarts.
6. If startup fails, set command/entrypoint override for debugging.
7. Validate logs/metrics and service reachability.
