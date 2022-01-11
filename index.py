from dash import dcc
import dash_bootstrap_components as dbc
from dash import State, html
from dash.dependencies import Input, Output
from app import app

from apps import playgroundSimulation_KlimaGrowthOverTime, \
                 playgroundsSimulation_KlimaBonding, quizzes_experimental, disclaimerPage
from components.disclaimer import short_disclaimer_row

CONTENT_STYLE = {
    "position": "relative",
    "margin-right": "0rem",
    "margin-left": "0rem",
    "padding": "1rem 1rem",
    "background-color": "#202020;"
}
FOOTER_STYLE = {
    "position": "relative",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": "6rem",
    "padding": "1rem 1rem",
    "background-color": "#232b2b",
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/apps/homePage")),
        dbc.NavItem(dbc.NavLink("Staking Simulator", href="/apps/playgroundSimulation_KlimaGrowthOverTime")),
        dbc.NavItem(dbc.NavLink("Bonding Simulator", href="/apps/playgroundsSimulation_KlimaBonding")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("KlimaDAO", href="https://www.klimadao.finance/#/stake"),
                dbc.DropdownMenuItem("Learn More", href="https://docs.klimadao.finance/"),
                dbc.DropdownMenuItem("Classroom", href="/apps/quizzes_experimental"),
                dbc.DropdownMenuItem("Feedback", href="https://forms.gle/UTyj7HvCfBNa1rt17"),
                dbc.DropdownMenuItem("Disclaimer", href="/disclaimer"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Playgrounds",
    brand_style={"fontSize": "35px", 'padding': '10px'},
    color="#00cc33",
    dark=True,
    style={"width": "auto", "fontSize": "30px", 'font-family': 'Nunito, sans-serif'}
)

menu_bar = dbc.DropdownMenu(
               children=[
                   dbc.DropdownMenuItem("Staking Simulator",
                                        href="/apps/playgroundSimulation_KlimaGrowthOverTime"),
                   dbc.DropdownMenuItem("Bonding Simulator",
                                        href="/apps/playgroundsSimulation_KlimaBonding"),
                   dbc.DropdownMenuItem("Learning Hub",
                                        href="/apps/quizzes_experimental"),
                   dbc.DropdownMenuItem("KlimaDAO",
                                        href="https://www.klimadao.finance/#/stake"),
                   dbc.DropdownMenuItem("Learn More",
                                        href="https://docs.klimadao.finance/"),
                   dbc.DropdownMenuItem("Feedback",
                                        href="https://forms.gle/UTyj7HvCfBNa1rt17"),
                   dbc.DropdownMenuItem("Disclaimer",
                                        href="/disclaimer"),
               ],
               nav=True,
               in_navbar=True,
               label="Menu",
               toggle_style={"color": "#00cc33"},
               align_end=True,
               style={"text-align": "right"},
               className="navbar_link_topic",
           ),

navbar2 = dbc.Navbar(
    dbc.Container([
            dbc.Row([
                dbc.Col(html.Img(src=app.get_asset_url('Klima_PG_trans_no_box.png'),
                                 height="85px")),
            ],
                align="center",
                className="g-0",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(menu_bar, className='ms-auto', navbar=True),
                id="navbar_collapse",
                is_open=False,
                navbar=True
            ),
    ], fluid=True),
    color="dark",
    dark=True,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar2,
    content,
    html.Footer(short_disclaimer_row(),
                className='footer_style')
])


@app.callback(
    Output("navbar_collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar_collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/apps/playgroundSimulation_KlimaGrowthOverTime':
        return playgroundSimulation_KlimaGrowthOverTime.layout
    elif pathname == '/apps/playgroundsSimulation_KlimaBonding':
        return playgroundsSimulation_KlimaBonding.layout
    elif pathname == '/disclaimer':
        return disclaimerPage.layout
    elif pathname == '/apps/quizzes_experimental':
        return quizzes_experimental.layout
    else:
        return playgroundSimulation_KlimaGrowthOverTime.layout


# For Gunicorn to reference
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
