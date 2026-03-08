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

Useful checks after start:
- `northflank phase4 status`
  - `northflank get service --project hackathon --service lebot-gameon-jupyter --output json`
- `northflank phase4 logs`
  - `northflank get service logs --project hackathon --service lebot-gameon-jupyter --lineLimit 120 --output json`
- `northflank phase4 endpoint`
  - `curl -I -s https://jupyter--lebot-gameon-jupyter--k5y6xz4rg776.code.run`

## Phase 4 Exception Notes (2026-03-08)

Observed exceptions and repeatable actions:

1. `getaddrinfo ENOTFOUND api.northflank.com`
- Meaning: CLI call failed due to sandbox network restrictions.
- Action: rerun with network-enabled/escalated execution.

2. `zsh:1: read-only variable: status`
- Meaning: polling script used reserved zsh variable name.
- Action: run poll loop in `bash` and use variable `state`.

3. `too many arguments for 'logs'. Expected 0 arguments but got 1`
- Meaning: invalid `logs` flag usage.
- Action: use `--lineLimit <n>` or `-f` (tail stream), not `--tail <n>`.

4. Deployment update succeeded but override not applied
- Symptoms:
  - `northflank update service deployment` returns success
  - `northflank get service deployment` remains `docker.configType: default`
  - logs show repeated `Process terminated with exit code 0`
  - endpoint stays `HTTP 503`
- Action:
  - treat as runtime-config blocker
  - collect evidence logs
  - apply command override in Northflank UI as next fallback path
  - rerun status/log/endpoint checks
