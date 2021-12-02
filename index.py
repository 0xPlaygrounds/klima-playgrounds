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
    "width": "15rem",
    "height": "100%",
    "padding": "0.5rem 1rem",
    "background-color": "#20272B",
}

CONTENT_STYLE = {
    "position": "relative",
    "margin-right": "1rem",
    "margin-left": "1rem",
    "padding": "1rem 1rem"
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Staking Simulator", href="/apps/playgroundSimulation_KlimaGrowthOverTime")),
        dbc.NavItem(dbc.NavLink("Bonding Simulator", href="/apps/playgroundsSimulation_KlimaBonding")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Klima Playgrounds",
    brand_href="#",
    color="#20272B",
    dark=True,
    style={"width": "auto"}
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    content
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/apps/playgroundSimulation_KlimaGrowthOverTime':
        return playgroundSimulation_KlimaGrowthOverTime.layout
    elif pathname == '/apps/playgroundsSimulation_KlimaBonding':
        return playgroundsSimulation_KlimaBonding.layout
    else:
        return '404'


# For Gunicorn to reference
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True)
