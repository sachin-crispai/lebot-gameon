# Phase 3 Team and Project Access

Date: 2026-03-08

## Targets

- Team: `lebot-gameon`
- Project: `Hackathon` (`hackathon`)
- Member to verify: `navitha@crispai.com`

## CLI Verification Results

### Project visibility
- Command: `northflank list projects`
- Result: project found
  - ID: `hackathon`
  - Name: `Hackathon`

### Service visibility in project
- Command: `northflank list services --project hackathon`
- Result: command succeeded, currently no services found.

## Member Access Verification

- Status: **Pending (UI check required)**
- Reason: current CLI output used in this run does not expose team-members list directly.
- Next manual step:
  1. Open Northflank app
  2. Team `lebot-gameon` -> Settings -> Members
  3. Confirm `navitha@crispai.com` is `Invited` or `Active`

## Evidence Logs

- `40-evidence/logs/phase3-projects-list.log`
- `40-evidence/logs/phase3-projects-filtered.log`
- `40-evidence/logs/phase3-services-hackathon.log`
