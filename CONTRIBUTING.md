# Contributing to lebot-gameon

This project supports contributions from both human developers and LLM agents (Claude, Codex, Gemini, GPT, etc.).

## For LLM Agents

1. Read `AGENTS.md` first for full context
2. Check `gh issue list` for available work
3. Check `gh pr list` to avoid conflicts
4. Branch from `main`: `git checkout -b feat/your-feature main`
5. Make changes, run tests
6. Open a PR using the template, tag yourself as the agent
7. Respect local UX convention: `skimread <file>` means open with `open -a Skim <file>`

## For Human Developers

1. Read `README.md` for project overview
2. Pick an open issue or create one
3. Follow the same branching and PR conventions

## Rules for All Contributors

- **One issue per PR** — keep changes focused
- **Tests must pass** — `PYTHONPATH=. uv run pytest tests/ -v`
- **Don't break the API contract** — `reset()`, `step()`, `state()` signatures are stable
- **Don't add deps without justification** — keep `pyproject.toml` lean
- **Tag your work** — include which agent/human authored the change

## PR Checklist

- [ ] Branch is based on latest `main`
- [ ] Tests pass locally
- [ ] PR description filled out with template
- [ ] Related issue referenced
- [ ] No unrelated changes included
