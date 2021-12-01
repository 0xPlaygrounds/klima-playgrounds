from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import playgroundSimulation_KlimaGrowthOverTime, playgroundsSimulation_KlimaBonding

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right": 0,
    "bottom": 0,
    "width": "25rem",
    "padding": "2rem 1rem",
    "background-color": "#20272B",
}

CONTENT_STYLE = {
    "position": "relative",
    "margin-right": "5rem",
    "margin-left": "30rem",
    "padding": "1rem 1rem"
}

sidebar = html.Div(
    [
        html.H2("Klima Playgrounds", className="display-4"),
        html.Hr(),
        html.P(
            "Welcome to your playground", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Staking Simulator", href='/apps/playgroundSimulation_KlimaGrowthOverTime', active="exact"),
                dbc.NavLink("Bonding Simulator", href='/apps/playgroundsSimulation_KlimaBonding', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/playgroundSimulation_KlimaGrowthOverTime':
        return playgroundSimulation_KlimaGrowthOverTime.layout
    elif pathname == '/apps/playgroundsSimulation_KlimaBonding':
        return playgroundsSimulation_KlimaBonding.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
