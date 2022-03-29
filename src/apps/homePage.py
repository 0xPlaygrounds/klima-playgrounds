import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
import base64

from ..app import app

url = "https://assets6.lottiefiles.com/packages/lf20_0ac4xdrp.json"
image_filename = 'src/assets/Forest Playground 2.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col([
               html.Div([
                   dbc.Card([
                       dbc.CardImg(
                           src=app.get_asset_url('bannerimage.jpg'),
                           top=True,
                           className='landing_main_image',
                       ),
                       dbc.CardImgOverlay(
                         dbc.CardBody([
                             html.Div([
                                 html.P('WELCOME TO YOUR', className='homepage_topic',
                                        style={'text-align': 'center',
                                               'padding-top': '10px',
                                               'padding-bottom': '5px'}),
                                 html.Img(src=app.get_asset_url('Green playgrounds.svg'),
                                          height="120px",
                                          className='banner_logo',
                                          style={'text-align': 'center', 'padding-bottom': '20px'}),
                                 html.Div([
                                     html.Span(
                                         'An on-chain data analytics, education,'
                                         ' and simulation environment for ',
                                         className='landing_main_paragraph_v2'),
                                     html.Span('KlimaDAO', style={'font-weight': 'bold'}),
                                 ], style={'font-size': '20px', 'text-align': 'center'}),
                             ], style={'text-align': 'center'}),
                         ]),
                       )
                   ], style={'width': '100%', 'height': '300px', 'object-fit': 'cover', 'border-radius': '20px'}),
               ], className='center'),
            ], sm=12, md=12, lg=12, xl=12),
        ], style={'padding': '20px', 'padding-top': '0px'}),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Row([
                            dbc.CardGroup([
                                    dbc.Card([
                                        dbc.CardBody([
                                            dbc.Row([
                                                html.P('ANALYTICS',
                                                       className="landing_main_topic_2",
                                                       style={'text-align': 'left'}),
                                                html.P(
                                                    'Klima Playgrounds provides a powerful on-chain data analytics '
                                                    'environment powered by Subgrounds, an on-chain data extraction, '
                                                    'transformation and visualization engine designed '
                                                    'to interface with The Graph Network',
                                                    className='landing_main_paragraph_v2',
                                                    style={'text-align': 'left'}
                                                )
                                            ], style={'padding': '10px'}),
                                            dbc.Row([
                                                dbc.Button('ANALYTICS',
                                                           id='landing_page_learn_btn',
                                                           href="/apps/quizzes_experimental",
                                                           color='#038523',
                                                           className='landing_button_enter', )
                                            ], style={'justify-content': 'left', 'padding': '20px'})
                                        ])
                                    ], style={'font-size': '24px'}),
                                    dbc.Card([
                                        dbc.CardImg(
                                            src=app.get_asset_url("analyticsimage2.jpg"),
                                            top=True,
                                            style={'object-fit': 'fill'}
                                        ),
                                    ]),
                            ], style={'border-radius': '20px'})
                            ], className='row-eq-height'),
                ], className='center')
            ], sm=12, md=12, lg=12, xl=12)
        ], style={'padding': '20px'}),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Row([
                        dbc.CardGroup([
                                dbc.Card([
                                        dbc.CardImg(
                                            src=app.get_asset_url("simulationimage.jpg"),
                                        ),
                                ]),
                                dbc.Card([
                                    dbc.CardBody([
                                        dbc.Row([
                                            html.P('SIMULATIONS',
                                                   className="landing_main_topic_2",
                                                   style={'text-align': 'right'}),
                                            html.P(
                                                'Klima Playgrounds provides a powerful'
                                                ' simulation environment to forecast KLIMA rewards'
                                                ' growth over time and your equivalent carbon'
                                                ' offsets from holding and staking KLIMA',
                                                className='landing_main_paragraph_v2',
                                                style={'text-align': 'right'}
                                            )
                                        ], style={'padding': '10px'}),
                                        dbc.Row([
                                            dbc.Button('SIMULATIONS',
                                                       id='landing_page_learn_btn',
                                                       href="/apps/playgroundSimulation_KlimaGrowthOverTime",
                                                       color='#038523',
                                                       className='landing_button_enter', )
                                        ], style={'justify-content': 'right', 'padding': '20px'})
                                    ])
                                ]),
                        ], style={'border-radius': '20px'}),
                    ], className='row-eq-height'),
                ], className='center')
            ], sm=12, md=12, lg=12, xl=12)
        ], style={'padding': '20px'}),
    ], className='center_2'),
], id='page_content', fluid=True)
