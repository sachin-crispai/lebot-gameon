# Contributing to lebot-gameon

This project supports contributions from both human developers and LLM agents (Claude, Codex, Gemini, GPT, etc.).

## For LLM Agents

1. Read `AGENTS.md` first for full context
2. Follow `OPERATIONS_NOTEBOOK.md` for accepted operational command procedures
3. Check `gh issue list` for available work
4. Check `gh pr list` to avoid conflicts
5. Branch from `main`: `git checkout -b feat/your-feature main`
6. Make changes, run tests
7. Open a PR using the template, tag yourself as the agent
8. Respect local UX convention: `skimread <file>` means open with `open -a Skim <file>`
9. Respect local UX convention: `atlasread <url>` means open with `open -a "ChatGPT Atlas.app" "<url>"`
10. Respect local UX convention: `atlas left <website>` and `atlas right <website>` mean open Atlas via `/Applications/ChatGPT Atlas.app` and snap window to left/right half.
11. After pushing, run `atlas left <file-url-from-pr>` on at least one checked-in file to confirm it is visible remotely.

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
- **OpenEnv redbook standard** — build `books/openenv-redbook/openenv-redbook-a4.pdf` as A4 landscape from ordered source PDFs in `books/openenv-redbook/sources/`, and keep partner resources organized under `books/openenv-redbook/partners/`

## PR Checklist

- [ ] Branch is based on latest `main`
- [ ] Tests pass locally
- [ ] PR description filled out with template
- [ ] Related issue referenced
- [ ] No unrelated changes included
