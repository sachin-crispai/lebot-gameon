# Phase 4 Service Baseline Status

Date: 2026-03-08
Project: `Hackathon` (`hackathon`)

## Service Created

- Service ID: `lebot-gameon-jupyter`
- Service type: `deployment`
- Image: `pytorch/pytorch:2.8.0-cuda12.6-cudnn9-runtime`
- Plan: `nf-gpu-hack-16-32`
- GPU: `h100`, non-timesliced
- Instances: `1`
- Port: `8888` (`HTTP`, public)
- DNS: `jupyter--lebot-gameon-jupyter--k5y6xz4rg776.code.run`

## Deployment State

- Latest capture (2026-03-08 10:31 PT): `COMPLETED` with reason `DEPLOYING`.
- Runtime behavior from logs: container starts then exits with code `0`, repeating.
- Public endpoint check: `HTTP/2 503` from `https://jupyter--lebot-gameon-jupyter--k5y6xz4rg776.code.run`

## Phase 4 Checklist

- [x] Service baseline created in target project
- [x] Public port and DNS assigned
- [x] Logs captured for startup behavior
- [x] Metrics capture attempted
- [ ] Service reaches stable `RUNNING`/healthy runtime state
- [ ] Endpoint returns success (currently `503`)
- [ ] Confirm command/entrypoint override path with Northflank support/docs

## Notes

- Multiple `northflank update service deployment` runs returned HTTP `200` but `get service deployment` still reports `docker.configType: default`.
- Because docker override did not persist, Phase 4 is partially complete and currently blocked on runtime command control for this image/service.
- Persistent storage decision for this baseline: not required yet, defer until runtime is stable.

## Evidence

- `40-evidence/logs/phase4-services-after-create.log`
- `40-evidence/logs/phase4-service-details.yaml`
- `40-evidence/logs/phase4-service-ports.yaml`
- `40-evidence/logs/phase4-service-status-latest.json`
- `40-evidence/logs/phase4-service-deployment.yaml`
- `40-evidence/logs/phase4-service-logs.json`
- `40-evidence/logs/phase4-service-metrics.json`
- `40-evidence/logs/phase4-endpoint-head.log`
