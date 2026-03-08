# Operations Notebook

This notebook tracks accepted operational commands and standard run patterns.
Update this file over time as new command workflows are approved.

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

## Change Log

- 2026-03-08: Added `skimread`, `atlasread`, `atlas left`, `atlas right`, and post-push verification rule.
