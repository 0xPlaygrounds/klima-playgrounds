import dash  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
import base64

url = "https://assets6.lottiefiles.com/packages/lf20_0ac4xdrp.json"
image_filename = 'assets/Forest Playground 2.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/Forest Playground 1.png",
                                top=True,
                                style={"opacity": 0.1},
                            ),
                            dbc.CardImgOverlay(
                                dbc.CardBody([
                                    html.P('WELCOME TO YOUR', className='homepage_topic',
                                           style={'text-align': 'center'}),
                                    html.P('Playground', className="landing_main_topic",
                                           style={'text-align': 'center'}),
                                    html.P(
                                        'An on-chain data analytics, education,'
                                        ' and simulation environment for KlimaDAO',
                                        style={'font-size': '20px', 'text-align': 'center'}
                                    ),
                                ]),
                            ),
                        ]),
                    ]),
                ], style={'font-size': '20px', 'text-align': 'left', 'height': '330px'}),
            ]),
        ]),
    ], className="homepage_topic", style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardImg(
                        src="/assets/Forest Playground 1.png",
                        top=True,
                    ),
                ]),
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            html.P('ANALYTICS', className="homepage_topic", style={'text-align': 'right'}),
                            html.P(
                                'Klima Playgrounds provides a powerful on-chain data analytics '
                                'environment powered by Subgrounds, an on-chain data extraction, '
                                'transformation and visualization engine designed '
                                'to interface with The Graph Network',
                                style={'font-size': '24px', 'text-align': 'right'}
                            ),
                        ]),
                        dbc.Row([
                            dbc.Button('Analytics',
                                       id='landing_page_learn_btn',
                                       href="/apps/quizzes_experimental",
                                       color='#038523',
                                       className='landing_button_enter', ),
                        ], style={'justify-content': 'right', 'padding-right': '10px'}),
                    ]),
                ], style={'font-size': '24px'}),
            ])
        ], xs=12, sm=12, md=12, lg=12, xl=12),
    ], className="homepage_topic", style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            html.P('SIMULATIONS', className="homepage_topic"),
                            html.P(
                                'Klima Playgrounds provides a powerful simulation environment to forecast KLIMA rewards'
                                ' growth over time and your equivalent carbon offsets from holding and staking KLIMA',
                                style={'font-size': '24px', 'text-align': 'left'}
                            ),
                        ]),
                        dbc.Row([
                            dbc.Button('Simulators',
                                       id='landing_page_learn_btn',
                                       href="/apps/quizzes_experimental",
                                       color='#038523',
                                       className='landing_button_enter', ),
                        ], style={'justify-content': 'left', 'padding-left': '10px'}),
                    ]),
                ], style={'font-size': '24px'}),
                dbc.Card([
                    dbc.CardImg(
                        src="/assets/Slide River.png",
                        top=True,
                    ),
                ]),
            ])
        ], xs=12, sm=12, md=12, lg=12, xl=12),
    ], className="homepage_topic", style={'padding': '10px'}),
], id='page_content', fluid=True)
