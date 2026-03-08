# Northflank Extra Information Runbook

Operational runbook derived from the “Extra information” pages of the Northflank OpenEnv hackathon doc.

## Goal

Get a working Northflank CLI workflow for the `lebot-gameon` team and establish a stable service setup path.

## Phase 1: Local Prerequisites

1. Confirm Node.js tooling is available:
- `node --version`
- `npm --version`

2. Install Northflank CLI (pick one):
- `npm i -g @northflank/cli`
- `yarn global add @northflank/cli`

3. Verify CLI binary:
- `northflank --version`

Use helper script:
- `bash books/openenv-redbook/partners/northflank/30-operations/scripts/setup_northflank_cli.sh`

## Phase 2: Authentication

1. Run:
- `northflank login`

2. Complete browser auth and return to terminal.

3. Confirm auth state:
- `northflank whoami` (if supported)
- or run any read command and confirm non-auth failure.

## Phase 3: Team/Project Access Check

Target objects:
- Team: `lebot-gameon`
- Project: `Hackathon`

Checks:
1. Confirm team appears in dashboard/CLI project list.
2. Confirm project `Hackathon` is visible.
3. Confirm membership status for `navitha@crispai.com` in Team -> Settings -> Members (Invited/Active).

## Phase 4: Service Baseline (Recommended Path)

Recommended first service:
- Jupyter Notebook with PyTorch image.

Minimum checks:
1. Resource plan has enough CPU/memory.
2. GPU allocation is exactly one H100 (default team quota).
3. Ephemeral storage set to at least 5-10 GB.
4. If required, set entrypoint/command override for diagnostics.
5. If persistence is required, add persistent storage mount.

## Phase 5: Remote Access + Validation

1. SSH access configured per Northflank docs.
2. Connect from VSCode/Cursor.
3. Validate logs/metrics in service UI.
4. Validate exposed HTTP ports when applicable.

## Troubleshooting Checklist

- Restart loop:
  - check runtime command/entrypoint override.
- OOM or startup failures:
  - raise CPU/memory plan and ephemeral storage.
- Lost data after restart:
  - use persistent storage volume.
- GPU unavailable:
  - confirm only one GPU service running, coordinate with organizers for capacity.

## Evidence to Capture

For each run, save in this folder:
- timestamped command output snippets
- screenshots of team/project visibility
- notes on blockers + resolutions

Storage locations:
- logs: `books/openenv-redbook/partners/northflank/40-evidence/logs/`
- screenshots: `books/openenv-redbook/partners/northflank/40-evidence/screenshots/`

## Current Status

- CLI execution steps prepared.
- Live account execution completed for phases 1-3.
- Phase 4 baseline service created (`lebot-gameon-jupyter`) with GPU plan.
- Phase 4 runtime is still blocked: service exits immediately and endpoint returns `503`.
- Awaiting live membership verification (`navitha@crispai.com`) in Northflank UI.
