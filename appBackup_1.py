import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import html
import plotly.express as px
import pandas as pd
from datetime import datetime
from pycoingecko import CoinGeckoAPI

# Pull price feed from coingecko
# App server variable
cg = CoinGeckoAPI()
app = dash.Dash(__name__)

# Set up data frames and plot figure
hist_klimaData = cg.get_coin_market_chart_by_id(id='olympus', vs_currency='usd', days='100')
hist_klimaData = pd.DataFrame.from_dict(hist_klimaData)
hist_klimaPrice = pd.DataFrame(hist_klimaData.prices.to_list(), columns=['time', 'prices'])
fig_2 = px.line(hist_klimaPrice.prices)

# Create app components using dash core and bootstrap
infoCard = dbc.Card(
    [
        dbc.CardHeader("klima Price Chart"),
        dbc.CardBody(
            [
                html.H4("Historical klima price data ", className="card-title"),
                html.P("Some important information on klima price action", className="card-text"),
            ]
        ),
        dbc.CardFooter("Reference link or something good for footer"),
    ],
    style={"width": "18rem"}
)

# Layout and place app components
app.layout = html.Div(children=[
    html.H1(children='Welcome to Olympus Playgrounds'),

    html.Div(children='''
        An interactive learning and simulation environment for the Olympus protocol
    '''),

    dcc.Graph(
        id='example-graph_2',
        figure=fig_2
    ),
    infoCard
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)