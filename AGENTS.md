# AGENTS.md — Agent Guidance for This Repo

Scope
- Applies to entire repository unless overridden by nested AGENTS.md

Style & Structure
- Python 3.12+, Poetry-managed
- Package root: `src/visualizations`
- Keep modules focused: data/, features/, models/, viz/, app/
- Avoid heavy frameworks beyond declared deps

Dev Rules
- Use Ruff + Black + Isort + Mypy; run `make lint`
- Tests in `tests/`; run `make test`
- Prefer functional, pure transforms; I/O isolated in data/ and app/
- No secrets in repo. Use `.env` (not committed) and GH Secrets

Commits
- Conventional Commits via Commitizen (feat, fix, docs, refactor, chore, test)
- Messages stress the WHY; keep scope small

MCP
- Use `visualizations.data.mcp_client.MCPClient`
- REST endpoints configured in `configs/mcp/rest.yaml`
- SQL sources via DuckDB in `configs/mcp/sql.yaml`

Dash
- Multi-page via `dash.register_page`
- Export WSGI `server` in `visualizations.app.main`

Deploy
- Render with Dockerfile and render.yaml; port exposed via `$PORT`
- Cloudflare CNAME `app` → Render service hostname; SSL Full (strict)

Do Nots
- Do not commit data in `data/` or `models/`
- Do not add new top-level dirs without discussion
- Do not broaden deps casually; justify in README or PR
