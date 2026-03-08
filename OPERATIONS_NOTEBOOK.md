# Operations Notebook

This notebook tracks accepted operational commands and standard run patterns.
Update this file over time as new command workflows are approved.

## Best Practices Baseline

- Prefer deterministic, repeatable commands over ad-hoc manual steps.
- Save operational evidence under partner `40-evidence/logs/`.
- Keep secrets local-only; never commit tokens or credentials.
- After every push, perform remote visibility verification via `atlas left` on a file URL from the pushed PR.
- Use dedicated issue + PR tracking for partner integration workstreams.

## Current Accepted Commands

### Document Readers
- `skimread <file>`
  - Command: `open -a Skim <file>`

### Atlas Browser
- `atlasread <url>`
  - Command: `open -a "ChatGPT Atlas.app" "<url>"`

- `atlas left <website>`
  - Open command:
    - `open -a "/Applications/ChatGPT Atlas.app" "<website>"`
  - Snap-left command (AppleScript):
    - activate Atlas, then set window `{x=0, y=0, width=screenW/2, height=screenH}`

- `atlas right <website>`
  - Open command:
    - `open -a "/Applications/ChatGPT Atlas.app" "<website>"`
  - Snap-right command (AppleScript):
    - activate Atlas, then set window `{x=screenW/2, y=0, width=screenW/2, height=screenH}`

## Post-Push Verification Standard

- After pushing, run `atlas left` on at least one file URL from the pushed/merged PR to verify remote visibility.

## Accepted Operational Command Patterns

### GitHub Tracking
- Create issue:
  - `gh issue create --title "<title>" --body-file <file>`
- Comment on issue:
  - `gh issue comment <issue-number> --body-file <file>`
- Create PR:
  - `gh pr create --base <base> --head <branch> --title "<title>" --body-file <file>`
- Comment on PR:
  - `gh pr comment <pr-number> --body-file <file>`
- Merge PR:
  - `gh pr merge <pr-number> --merge --delete-branch`

### Northflank CLI Workflow
- Login (manual URL flow):
  - `northflank login --do-not-open-browser`
- List projects:
  - `northflank list projects`
- List services in project:
  - `northflank list services --project hackathon`
- Show active context:
  - `northflank context show`

### Local Northflank Scripts
- CLI setup:
  - `bash books/openenv-redbook/partners/northflank/30-operations/scripts/setup_northflank_cli.sh`
- Preflight:
  - `bash books/openenv-redbook/partners/northflank/30-operations/scripts/preflight_check.sh`

## Northflank Abbreviated Commands

Use `northflank <operation> <action>` as the human-facing shorthand.  
These map to concrete commands/scripts.

- `northflank auth`
  - Run CLI auth flow:
    - `northflank login --do-not-open-browser`
  - Open printed login URL in Atlas if needed.

- `northflank preflight`
  - `bash books/openenv-redbook/partners/northflank/30-operations/scripts/preflight_check.sh`

- `northflank setup cli`
  - `bash books/openenv-redbook/partners/northflank/30-operations/scripts/setup_northflank_cli.sh`

- `northflank projects list`
  - `northflank list projects`

- `northflank project services`
  - `northflank list services --project hackathon`

- `northflank context show`
  - `northflank context show`

- `northflank phase4 start`
  - Follow `books/openenv-redbook/partners/northflank/10-plan/EXTRA_INFO_RUNBOOK.md` Phase 4:
    - create first service (recommended Jupyter + PyTorch)
    - set CPU/memory plan
    - assign one H100
    - set ephemeral storage (5-10 GB)
    - configure persistent storage if needed

- `northflank phase4 status`
  - `northflank get service --project hackathon --service lebot-gameon-jupyter --output json`

- `northflank phase4 logs`
  - `northflank get service logs --project hackathon --service lebot-gameon-jupyter --lineLimit 120 --output json`

- `northflank phase4 endpoint`
  - `curl -I -s https://jupyter--lebot-gameon-jupyter--k5y6xz4rg776.code.run`

## Northflank Phase 4 Exception Playbook

Use this as the repeatable exception/debug sequence for `lebot-gameon-jupyter`.

1. Confirm current state:
   - `northflank get service --project hackathon --service lebot-gameon-jupyter --output json`
   - `northflank get service deployment --project hackathon --service lebot-gameon-jupyter --output yaml`
   - `northflank get service logs --project hackathon --service lebot-gameon-jupyter --lineLimit 120 --output json`
   - `curl -I -s https://jupyter--lebot-gameon-jupyter--k5y6xz4rg776.code.run`

2. Exception: network/DNS failure in sandboxed shell
   - Error signature:
     - `getaddrinfo ENOTFOUND api.northflank.com`
   - Root cause:
     - sandboxed command has restricted outbound DNS/network.
   - Workaround used:
     - rerun required `northflank` command with escalated permissions.

3. Exception: zsh loop script failure while polling
   - Error signature:
     - `zsh:1: read-only variable: status`
   - Root cause:
     - `status` is reserved/read-only in zsh.
   - Fix used:
     - use `bash` polling script and variable `state` instead of `status`.

4. Exception: invalid logs command usage
   - Error signature:
     - `too many arguments for 'logs'. Expected 0 arguments but got 1`
   - Root cause:
     - wrong CLI syntax (`--tail 80` treated as extra argument).
   - Fix used:
     - use `--lineLimit 80` (or `-f` for streaming) with:
     - `northflank get service logs --project hackathon --service lebot-gameon-jupyter --lineLimit 120 --output json`

5. Exception: deployment update reports success but runtime config unchanged
   - Error signature:
     - update command returns HTTP 200 / success
     - `get service deployment` still shows `docker.configType: default`
   - Root cause (observed):
     - command/entrypoint override not persisted through current CLI update path for this service.
   - Workaround used:
     - captured full evidence and treated as platform/CLI behavior blocker:
       - `phase4-service-deployment.yaml`
       - `phase4-service-logs.json`
       - `phase4-endpoint-head.log`
   - Next repeatable step:
     - open Northflank UI, edit deployment command there, then re-run phase4 status/log/endpoint checks.

6. Exception: service appears deployed but endpoint stays unavailable
   - Error signature:
     - service status includes `COMPLETED`
     - logs show `Process terminated with exit code 0` repeatedly
     - endpoint returns `HTTP/2 503`
   - Root cause:
     - container process exits immediately; no long-running server bound to port 8888.
   - Workaround used:
     - documented as partial Phase 4 completion; do not mark runtime healthy until endpoint returns non-503.

7. Evidence discipline (mandatory)
   - Save each check output to `books/openenv-redbook/partners/northflank/40-evidence/logs/`.
   - Comment issue and PR with blocker details and links to evidence files.

## Change Log

- 2026-03-08: Added `skimread`, `atlasread`, `atlas left`, `atlas right`, and post-push verification rule.
- 2026-03-08: Added best-practice baseline and accepted command patterns (GitHub tracking + Northflank operations).
- 2026-03-08: Added Northflank Phase 4 exception/error playbook with root-cause and workaround steps.
