import dash
import dash_bootstrap_components as dbc

from components.disclaimer import long_disclaimer_row

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container([
    long_disclaimer_row()
])
