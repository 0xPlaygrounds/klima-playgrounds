# Notes
# This script is short and simple.
# It creates your dash app and connects it to a server.
# If you choose to use Bootstrap CSS styling (or another pre-made CSS stylesheet),you can also do so here.

import dash
import dash_bootstrap_components as dbc



#Instantiates the Dash app and identify the server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server