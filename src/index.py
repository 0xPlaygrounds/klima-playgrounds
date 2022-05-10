from dash import dcc
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Input, Output, State, html
from .app import app
from .apps import staking, bonding, analytics, disclaimer, home

CONTENT_STYLE = {
    "position": "relative",
    "margin-right": "0rem",
    "margin-left": "0rem",
    "background-color": "#202020",
    "height": "100vh"
}
FOOTER_STYLE = {
    "position": "relative",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": "6rem",
    "padding": "1rem 1rem",
    "background-color": "#202020",
}

menu_bar = dbc.DropdownMenu(
               children=[
                   dbc.DropdownMenuItem("Home Page",
                                        href="/apps/home"),
                   dbc.DropdownMenuItem("Analytics",
                                        href="/apps/analytics"),
                   dbc.DropdownMenuItem("Staking Simulator",
                                        href="/apps/staking"),
                   dbc.DropdownMenuItem("Bonding Simulator",
                                        href="/apps/bonding"),
                   dbc.DropdownMenuItem("KlimaDAO",
                                        href="https://www.klimadao.finance/"),
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
               style={"text-align": "right", 'margin-right': '160px'},
               className="navbar_link_topic",
           ),

navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(html.Img(src=app.get_asset_url('klimaPGLogo.svg'),
                                 height="55px", className='navbar_logo_mobile')),
            ],
                align="center",
                className="g-0",
            ),
            href="/apps/home"
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0, style={"justify-content": "right"}),
        dbc.Collapse(
                dbc.Nav(menu_bar, navbar=True, style={"justify-content": "right"}),
                id="navbar_collapse",
                is_open=False,
                navbar=True,
                style={"justify-content": "right"}
            ),
    ], fluid=True),
    color="#ffffff00",
    dark=True,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    content,
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
    if pathname == '/apps/home':
        return home.layout
    elif pathname == '/apps/analytics':
        return analytics.layout
    elif pathname == '/apps/staking':
        return staking.layout
    elif pathname == '/apps/bonding':
        return bonding.layout
    elif pathname == '/disclaimer':
        return disclaimer.layout
    else:
        return home.layout


# For Gunicorn to reference
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
