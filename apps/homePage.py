import dash  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
from app import app
from apps import playgroundSimulation_KlimaGrowthOverTime, \
                 playgroundsSimulation_KlimaBonding, quizzes_experimental, disclaimerPage, homePage

url = "https://assets6.lottiefiles.com/packages/lf20_0ac4xdrp.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

layout = html.Div([
    html.H1('Welcome to your', className="landing_welcome_topic"),
    html.H1('playground.', className="landing_main_topic"),
    html.P('An education and simulation environment for KlimaDAO', className="landing_main_paragraph1"),
    dbc.Row([
        dbc.Col([
            dbc.Button('Learning Hub',
                       id='landing_page_learn_btn',
                       href="/apps/quizzes_experimental",
                       className='landing_button_enter'),
            dbc.Button('Simulation Hub',
                       id='landing_page_sim_btn',
                       href="/apps/playgroundSimulation_KlimaGrowthOverTime",
                       className='landing_button_enter')
        ], xs=12, sm=12, md=12, lg=6, xl=6),
    ]),
], id='showcase')
