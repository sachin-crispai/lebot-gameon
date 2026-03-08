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

- Current status: `IN_PROGRESS` (`DEPLOYING`) at capture time.

## Remaining Phase 4 Checks

- [ ] Verify service reaches `RUNNING`/healthy state
- [ ] Confirm Jupyter endpoint responsiveness
- [ ] Validate logs/metrics in Northflank UI
- [ ] Decide whether persistent storage is required for this workload

## Evidence

- `40-evidence/logs/phase4-services-after-create.log`
- `40-evidence/logs/phase4-service-details.yaml`
- `40-evidence/logs/phase4-service-ports.yaml`
