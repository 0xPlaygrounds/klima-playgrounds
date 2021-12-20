import dash  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
# import dash_extensions as de  # pip install dash-extensions

from components.disclaimer import short_disclaimer_row

url = "https://assets6.lottiefiles.com/packages/lf20_0ac4xdrp.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

layout = dbc.Container(
    html.Div(className='overlay')
)
