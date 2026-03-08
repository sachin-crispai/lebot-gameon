# Northflank Redbook Digest

Source:
- `Northflank Docs _ OpenEnv Hackathon.pdf`
- Captured from Atlas Browser (Print -> Save as PDF)

## Quick Start

1. Request compute access using the hackathon form.
2. Wait for invite email from `services@northflank.com`.
3. Accept invite and open your Northflank Team dashboard.
4. Open the `Hackathon` project.
5. Deploy exactly one GPU service (single NVIDIA H100 per team by default).

## Recommended Deployment Options

- Jupyter Notebook with PyTorch (recommended baseline).
- Generic Ubuntu image for shell/VM-like access.
- Existing GitHub repo using Docker (CI/CD flow).
- Any public Docker image.

## Remote Access and Dev Workflow

- Use SSH guide to connect from VSCode/Cursor/etc.
- For troubleshooting, use Northflank docs and OpenEnv Discord with Northflank team support.

## Environment and Runtime Notes

- Sandbox base: Ubuntu 22.04.5.
- PyTorch image reference in doc: `pytorch/pytorch:2.8.0-cuda12.6-cudnn9-runtime`.
- Containers are ephemeral; non-persistent changes are lost on restart.
- Use persistent storage for models/data that must survive restarts.

## CLI Notes

- Install CLI: `@northflank/cli` via npm/yarn.
- Authenticate with `northflank login`.
- CLI can help upload/download files and forward services locally.

## Practical Deployment Checks

- Set enough CPU/memory plan for workload.
- Increase ephemeral storage (doc suggests ~5-10GB as a common range).
- If container restart loop occurs, set runtime command/entrypoint override (for example shell + sleep for debugging).
- Expose ports via networking/ports settings for HTTP workloads only.

## Constraint to Keep in Mind

- By default, teams get one H100 and one GPU service; ask organizers if extra capacity is needed.
