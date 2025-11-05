from __future__ import annotations

import os
from typing import Any

import dash
from dash import Dash, dcc, html


def create_app() -> Dash:
    app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

    app.layout = html.Div(
        [
            html.H1("Visualizations"),
            html.Div(
                [
                    dcc.Link(
                        children=html.Button(page["name"]), href=page["path"],
                    )
                    for page in dash.page_registry.values()
                ]
            ),
            dash.page_container,
        ]
    )

    return app


# Import pages to register them
try:
    from .pages import home  # noqa: F401
except Exception:
    # Pages are optional; home will be created by tests or later
    pass


_app: Dash = create_app()
server: Any = _app.server


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8050"))
    _app.run_server(host="0.0.0.0", port=port, debug=True)
