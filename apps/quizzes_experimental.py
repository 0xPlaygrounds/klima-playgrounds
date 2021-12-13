import dash  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
from dash import dcc
import dash_extensions as de  # pip install dash-extensions

# Lotties: Emil at https://github.com/thedirtyfew/dash-extensions
url = "https://assets1.lottiefiles.com/private_files/lf30_WdTEui.json"
url2 = "https://assets9.lottiefiles.com/packages/lf20_CYBIbn.json"
url3 = "https://assets8.lottiefiles.com/packages/lf20_bknKi1.json"
url4 = "https://assets10.lottiefiles.com/datafiles/xjh641xEDuQg4qg/data.json"
url5 = "https://assets8.lottiefiles.com/packages/lf20_q6y5ptrh.json"
url6 = "https://assets4.lottiefiles.com/packages/lf20_tN5Ofx.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card_main = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url3)),
                html.H4("Introduction to KlimaDAO", className="card-title"),
                html.H6("Lesson 1:", className="card-subtitle"),
                html.P(
                    "Learn about KlimaDAO and its vision to change the world",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="success",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main2 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url4)),
                html.H4("KlimaDAO Ecosystem", className="card-title"),
                html.H6("Lesson 2:", className="card-subtitle"),
                html.P(
                    "Learn about the mechanics governing KlimaDAO",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="success",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main3 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url5)),
                html.H4("Carbon offsets and carbon markets", className="card-title"),
                html.H6("Lesson 3:", className="card-subtitle"),
                html.P(
                    "Dive deep into the world of carbon markets",
                    className="card-text",
                ),
            ]
        )
    ],
    color="success",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main4 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url6)),
                html.H4("How to participate in KlimaDAO", className="card-title"),
                html.H6("Lesson 4:", className="card-subtitle"),
                html.P(
                    "Learn the step by step process to becoming a Klimate",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="success",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main5 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url)),
                html.H4("Introduction to KlimaDAO", className="card-title"),
                html.H6("Challenge 1:", className="card-subtitle"),
                html.P(
                    "Welcome! let's have some fun reviewing",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="secondary",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main6 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url)),
                html.H4("Carbon offsets and carbon markets", className="card-title"),
                html.H6("Challenge 2:", className="card-subtitle"),
                html.P(
                    "The carbon market is a curious place. Test your knowledge",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="secondary",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main7 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url)),
                html.H4("All about carbon", className="card-title"),
                html.H6("Challenge 3:", className="card-subtitle"),
                html.P(
                    "Deeper challenges on carbon market.",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="secondary",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main8 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url)),
                html.H4("How to participate in KlimaDAO", className="card-title"),
                html.H6("Challenge 4:", className="card-subtitle"),
                html.P(
                    "Think you know how to get started? show us!",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="secondary",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)
card_main9 = dbc.Card(
    [

        dbc.CardBody(
            [
                html.Div(de.Lottie(options=options, width="50%", height="50%", url=url)),
                html.H4("How to participate in KlimaDAO", className="card-title"),
                html.H6("Challenge 4:", className="card-subtitle"),
                html.P(
                    "Validate what you've learned",
                    className="card-text",
                ),
            ]
        ),
    ],
    color="success",   # https://bootswatch.com/default/ for more card colors
    inverse=True,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
    className="mt-3",
    style={'height': '90%', 'padding': "10px"},
)


layout = html.Div([
    dbc.Row([
        dbc.Col(card_main, width=3),
        dbc.Col(card_main2, width=3),
        dbc.Col(card_main3, width=3),
        dbc.Col(card_main4, width=3),
        dbc.Col(card_main5, width=3),
        dbc.Col(card_main6, width=3),
        dbc.Col(card_main7, width=3),
        dbc.Col(card_main8, width=3),
             ])
])
