# Visualizations: DS/DA portfolio with Dash and MCP

This repository showcases end-to-end data science/analytics:
- Ingest data via MCP tools (REST/SQL)
- Transform and model (classification/regression)
- Publish interactive results with Plotly Dash
- Deploy to Render; subdomain via Cloudflare (`app.narrativus.me`)

Quickstart
- Install Poetry (https://python-poetry.org)
- Python 3.12+
- make setup
- make run  # http://localhost:8050

Deploy (Render)
- Push to GitHub (public repo)
- In Render: New Web Service → From Repo → use Dockerfile
- After first deploy: add custom domain `app.narrativus.me` in Render
- In Cloudflare DNS: CNAME `app` → `your-service.onrender.com`
- SSL/TLS: Full (strict) → switch proxy to orange once cert is issued

Structure
- src/visualizations/...  # app, data, features, models, viz
- configs/                # project + MCP configs
- data/{raw,interim,processed} (gitignored)
- models/                 (gitignored)
- tests/

Notes
- MIT License
- GH Actions: lint, type-check, test
- Pre-commit: ruff, black, isort, mypy, nbstripout

See AGENTS.md for agent guidance, and configs/project.yaml to set task/source.
