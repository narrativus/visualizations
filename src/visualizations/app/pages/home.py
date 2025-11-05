from __future__ import annotations

import dash
from dash import html


dash.register_page(__name__, path="/")

layout = html.Div(
    [
        html.P("Welcome to Visualizations."),
        html.P("This is a placeholder home page."),
    ]
)
