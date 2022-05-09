import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
import base64

from ..app import app

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
                                               'padding-top': '5px',
                                               'padding-bottom': '5px'}),
                                 html.Img(src=app.get_asset_url('Green playgrounds.svg'),
                                          height="140px",
                                          className='banner_logo',
                                          style={'text-align': 'center', 'padding-bottom': '5px'}),
                                 html.Div([
                                     html.Span(
                                         'An on-chain data analytics, education,'
                                         ' and simulation environment for ',
                                         className='landing_main_paragraph_v2'),
                                     html.Span('KlimaDAO', style={'font-weight': 'bold', 'padding-bottom': '20px'}),
                                 ], style={'font-size': '20px', 'text-align': 'center', 'padding-bottom': '30px'}),
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
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    dbc.Row([
                                        html.P('ANALYTICS',
                                               className="homepage_topic",
                                               style={'text-align': 'left'}),
                                        html.P(
                                            'Access on-chain data analytics powered by '
                                            'Playgrounds and The Graph Network ',
                                            className='landing_main_paragraph_v2',
                                            style={'text-align': 'left'}
                                        )
                                    ], style={'padding': '10px'}),
                                    dbc.Row([
                                        dbc.Button('ANALYTICS',
                                                   id='landing_page_learn_btn',
                                                   href="/apps/analytics",
                                                   color='#038523',
                                                   className='landing_button_enter',
                                                   style={'text-align': 'center'})
                                    ], style={'justify-content': 'left', 'padding': '20px',
                                              'padding-bottom': '10px'})
                                ])
                            ], style={'font-size': '20px', 'border-radius': '20px'}),
                        ], sm=12, md=12, lg=6, xl=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    dbc.Row([
                                        html.P('SIMULATIONS',
                                               className="homepage_topic"),
                                        html.P(
                                            'Gain insight on protcol interactions using the built in simulation tool',
                                            className='landing_main_paragraph_v2',
                                            style={'text-align': 'left'}
                                        )
                                    ], style={'padding': '10px'}),
                                    dbc.Row([
                                        dbc.Button('SIMULATIONS',
                                                   id='landing_page_learn_btn',
                                                   href="/apps/staking",
                                                   color='#038523',
                                                   className='landing_button_enter', )
                                    ], style={'justify-content': 'left', 'padding': '20px',
                                              'padding-bottom': '10px'})
                                ])
                            ], style={'font-size': '20px', 'border-radius': '20px'}),
                        ], sm=12, md=12, lg=6, xl=6),
                    ], className='row-eq-height'),
                ], className='center')
            ], sm=12, md=12, lg=12, xl=12)
        ], style={'padding': '20px'}),
    ], className='center_2'),
], id='page_content', fluid=True)
