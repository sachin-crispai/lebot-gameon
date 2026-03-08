# Operations Notebook

This notebook tracks accepted operational commands and standard run patterns.
Update this file over time as new command workflows are approved.

## Current Accepted Commands

### Named Aliases
- `THEBIBLE` → `books/openenv-redbook/openenv-redbook-a4.pdf`
  - Refers to the compiled OpenEnv redbook (A4 landscape, all partner slides).
  - Use in any viewer command, e.g. `skim left THEBIBLE`.
- `mastra` → `books/downloads/agents-redbook.pdf`
  - Refers to the Mastra agents cookbook/redbook bundle.
  - Use in any viewer command, e.g. `skim left mastra`.
- Alias resolution is case-insensitive (for example: `bible`, `THEBIBLE`, `Mastra`).
- New domain tags/aliases should be added here as stable shortcuts to frequently used docs.

### Document Readers
- `skimread <file>`
  - Command: `open -a Skim <file>`
  - Windowing rule: open as a separate window, not a tab.

- `skim left <file>`
  - Open command: `open -a Skim <file>`
  - Snap-left command (AppleScript):
    - activate Skim, then set window `{x=0, y=0, width=screenW/2, height=screenH}`
  - View settings (AppleScript, apply after snap):
    ```applescript
    tell application "Skim"
      set view settings of front document to {display mode:two up continuous, displays page breaks:true, auto scales:true}
    end tell
    ```
  - This sets two-page continuous mode with page breaks and auto-scales to fill the half-screen window.
  - Windowing rule: keep this as its own window (never tab into another doc).

- `skim right <file>`
  - Open command: `open -a Skim <file>`
  - Snap-right command (AppleScript):
    - activate Skim, then set window `{x=screenW/2, y=0, width=screenW/2, height=screenH}`
  - View settings: same as `skim left` (two up continuous, page breaks, auto scales)
  - Windowing rule: keep this as its own window (never tab into another doc).

- `skim split <left-file> <right-file>`
  - Opens both files in separate Skim windows for parallel reading (no tabs).
  - Left window: snap to left half with standard Skim view settings.
  - Right window: snap to right half with standard Skim view settings.
  - Supports aliases on both sides (case-insensitive), e.g. `skim split mastra bible`.

- `skim focus left`
  - Brings the left-side Skim window to front (active focus) in split mode.
  - Useful after opening right-side docs when you want keyboard/navigation control on the left.

- `skim focus right`
  - Brings the right-side Skim window to front (active focus) in split mode.
  - Useful for toggling active reading pane without changing window layout.

- `test_skim`
  - Validation workflow for monitor/layout changes.
  - Opens `mastra` on the left and `bible` on the right in separate Skim windows (not tabs).
  - Applies standard view settings to both windows.
  - Includes an untab fallback (`Move Tab to New Window`) if Skim auto-tabs.

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

### Execution Preference
- All viewer/browser open commands (`skimread`, `skim left`, `skim right`, `atlasread`, `atlas left`, `atlas right`) should run immediately without in-chat confirmation prompts.
- Explicitly: do not ask for confirmation before running any `skim*` command.
- If a system-level sandbox/OS approval dialog appears, proceed through that required platform prompt and continue.

### sync_operations
`sync_operations` is the command to keep this notebook in sync with actual usage. When the user says `sync_operations` (or asks to sync operations), Claude should:
1. Review recent commands used in the session that are not yet documented.
2. Add any missing command patterns to the appropriate section above.
3. Update `CLAUDE.md` Local UX Convention section to match.
4. Log the change in the Change Log below.

### refresh_operations
`refresh_operations` is the command to reload operational context. When the user says `refresh_operations`, agents should:
1. Re-read `OPERATIONS_NOTEBOOK.md` and `CLAUDE.md`.
2. Summarize any operational deltas currently in the working tree versus `HEAD`.
3. Confirm the active command mappings/aliases they will use for subsequent commands.

### Quick Examples
- `skim left mastra`
- `skim right bible`
- `skim split mastra bible`
- `skim focus left`
- `skim focus right`
- `test_skim`
- `refresh_operations`
- Sequential equivalent:
  - `skim left mastra` then `skim right bible`

### Diff Display Preference
- Always show diffs in a single unified window (standard `git diff` format).
- Never use side-by-side diff mode.
- Keep diff output compact — one fenced code block, not split panels.

### checkin
`checkin` means "everything looks good — wrap it up". When the user says `checkin`, Claude should:
1. Run `sync_operations` to flush any undocumented commands from the session.
2. Commit all staged/unstaged changes with a conventional commit message.
3. Check `gh issue list` and `gh pr list` — create issue and/or PR if none exist for the current work.
4. Add a summary comment to the open PR and linked issue describing what changed.
5. Check consistency between `OPERATIONS_NOTEBOOK.md` and `CLAUDE.md`.
6. Run relevant tests (`test_skim` for Skim workflows, `pytest` for code changes).
7. Log the checkin in the Change Log.

### Fix Verification Rule
- After any fix, always verify it by running the relevant command.
- For Skim-related fixes, this means running `test_skim` and confirming clean output.

### Notebook Hygiene
- Keep this notebook synchronized with the latest user workflow preferences, accepted commands, and operational best practices.
- After any new command is used and confirmed working, run `sync_operations` to record it.

## Post-Push Verification Standard

- After pushing, run `atlas left` on at least one file URL from the pushed/merged PR to verify remote visibility.

## Change Log

- 2026-03-08: Added `skimread`, `atlasread`, `atlas left`, `atlas right`, and post-push verification rule.
- 2026-03-08: Added preference to execute Atlas open commands without in-chat confirmation and keep notebook guidance in sync with user preferences.
- 2026-03-08: Added `skim left`, `skim right` commands. Defined `sync_operations` workflow. Extended execution preference to all viewer/browser open commands.
- 2026-03-08: Added Skim view settings for `skim left`/`skim right`: two up continuous, displays page breaks, auto scales to fill window. Confirmed working AppleScript via `view settings` record property.
- 2026-03-08: Added diff display preference: single unified window, compact mode, no side-by-side.
- 2026-03-08: Defined THEBIBLE alias → openenv-redbook-a4.pdf. Confirmed `skim left THEBIBLE` works end-to-end.
- 2026-03-08: sync_operations update: clarified no in-chat confirmation for all `skim*` commands.
- 2026-03-08: Added `mastra` alias → `books/downloads/agents-redbook.pdf` and documented general case-insensitive tagging/alias convention.
- 2026-03-08: Added `skim split <left-file> <right-file>` for two-window parallel reading, with examples (`mastra` left, `bible` right).
- 2026-03-08: Added `skim focus left` and `skim focus right` commands to switch active Skim window in split layout.
- 2026-03-08: Added explicit productivity preference: Skim workflows use separate windows, not tabs.
- 2026-03-08: Added `test_skim` command for end-to-end split-window validation (`mastra` left, `bible` right) during monitor changes.
- 2026-03-08: Added `refresh_operations` command so agents can reload and confirm the latest operations context on demand.
- 2026-03-08: Fixed AppleScript boolean-to-string coercion bug in test_skim verify step. Added Fix Verification Rule: always run test_skim after Skim-related fixes.
- 2026-03-08: Defined `checkin` command as the standard wrap-up workflow (sync, commit, PR/issue, comments, consistency check, tests).
