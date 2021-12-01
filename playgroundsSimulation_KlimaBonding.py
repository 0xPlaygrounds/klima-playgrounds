# Import all required packages for this page
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
from millify import millify

# Create link to CSS style sheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Build the layout for the app. Using dash bootstrap container here instead of the standard html div.
# Container looks better
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Playground: Staking", className='text-center, mb-4'))
    ]),
    # Create a tab so we can have two sections for the klima growth/rewards simulation
    dcc.Tabs([
        dcc.Tab(label='Klima rewards simulator',
                selected_style={'color': 'green', 'fontSize': '30px', 'height': '70px'},
                style={'color': 'green', 'fontSize': '30px', 'height': '70px'}, children=[
                    dbc.Row([
                        dbc.Col(dcc.Markdown('''
                        ## Predicted Growth
                        ---
                        '''))
                    ], className='mb-5'),
                    dbc.Row([
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Klima growth simulation results: Charts'),
                            dbc.CardBody([
                                dcc.Graph(id='graph1'),
                                html.Div(id='table')
                            ])
                        ], outline=True, color='success', style={"height": "570px"}), className='w-50'),
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Simulation controls'),
                            dbc.CardBody([
                                # use form for controls
                                dbc.Form([
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                # dbc.Label('Growth over time'),
                                                dbc.Col([
                                                    dbc.Label('Days'),
                                                    dcc.Slider(
                                                        id='growthDays',
                                                        min=1,
                                                        max=1000,
                                                        value=365,
                                                        tooltip={'placement': 'top', 'always_visible': True}), ],
                                                    width='12')]),
                                            dbc.Row([
                                                dbc.Col([
                                                    dbc.Label('Initial Klima'),
                                                    dbc.Input(
                                                        id='initialKlima',
                                                        placeholder='1.0',
                                                        type='number',
                                                        min=1,
                                                        value=1, style={'background-color': '#222222', 'color': 'white',
                                                                        'width': '100%'})]),
                                                dbc.Col([
                                                    dbc.Label('Simulated APY(%)'),
                                                    dbc.Input(
                                                        id='currentAPY',
                                                        placeholder='40000',
                                                        type='number',
                                                        min=1,
                                                        value=40000, style={'background-color': '#222222',
                                                                            'color': 'white',
                                                                            'width': '100%'})]),
                                            ], className="g-2"),
                                        ]), className='w-100'),
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Label('Profit taking controls'),
                                                dbc.Col([
                                                    dbc.Label('Profit taking amount (%)'),
                                                    dbc.Input(
                                                        id='percentSale',
                                                        placeholder='5',
                                                        type='number',
                                                        min=1,
                                                        value=5,
                                                        style={'background-color': '#222222', 'color': 'white',
                                                               'width': '100%'}),
                                                ]),
                                                dbc.Col([
                                                    dbc.Label('Profit taking cadence (Days)'),
                                                    dbc.Input(
                                                        id='sellDays',
                                                        placeholder='30',
                                                        type='number',
                                                        min=1,
                                                        value=30,
                                                        style={'background-color': '#222222', 'color': 'white',
                                                               'width': '100%'}),
                                                ])
                                            ], className="g-2")]), className='w-100'),
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Label('Dollar cost averaging controls'),
                                                dbc.Col([
                                                    dbc.Label('Dollar cost averaging price (USDC)'),
                                                    dbc.Input(
                                                        id='klimaPrice_DCA',
                                                        placeholder='1000',
                                                        type='number',
                                                        min=1,
                                                        value=1000, style={'background-color': '#222222',
                                                                           'color': 'white',
                                                                           'width': '100%'})]),
                                                dbc.Col([
                                                    dbc.Label('USDC worth to buy'),
                                                    dbc.Input(
                                                        id='valBuy',
                                                        placeholder='1000',
                                                        type='number',
                                                        min=1,
                                                        value=1000, style={'background-color': '#222222',
                                                                           'color': 'white',
                                                                           'width': '100%'})]),
                                                dbc.Col([
                                                    dbc.Label('Dollar cost averaging cadence (Days)'),
                                                    dbc.Input(
                                                        id='buyDays',
                                                        placeholder='30',
                                                        type='number',
                                                        min=1,
                                                        value=30, style={'background-color': '#222222',
                                                                         'color': 'white',
                                                                         'width': '100%'})]),
                                            ], className="g-2")]), className='w-100'),
                                ]),
                            ])
                        ], outline=True, color='success', style={"height": "auto"}), className='w-50'),
                    ], className="mb-5"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader('Klima growth simulation results: ROI'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Daily', style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50}, id='dailyROI')
                                                ])
                                            ])
                                        ], width=2),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Five day', style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50}, id='fivedayROI')
                                                ])
                                            ])
                                        ], width=2),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Seven day', style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50}, id='sevendayROI')
                                                ])
                                            ])
                                        ], width=2),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Monthly', style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50}, id='monthlyROI')
                                                ])
                                            ])
                                        ], width=2),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Annual', style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50}, id='annualROI')
                                                ])
                                            ])
                                        ], width=2),
                                    ], className="g-2", justify='center'),
                                ]),
                            ], outline=True, color='success', style={"height": "250px"}), ]),
                    ], className="mb-5"),
                    dbc.Row([
                        dbc.Col(dcc.Markdown('''
                        ## Rewards Strategizer
                        ---
                        '''))
                    ], className='mb-5'),
                    dbc.Row([
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('Rewards strategy results'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Days until USDC Value',
                                                          style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50}, id='rewardsUSD'),
                                                ])
                                            ])
                                        ], className='w-100'),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.Label('Days until KLIMA amount',
                                                          style={'color': 'white', 'fontSize': 15}),
                                                dbc.CardBody([
                                                    html.Div(style={'color': 'white', 'fontSize': 50},
                                                             id='rewardsKLIMA'),
                                                ])
                                            ])
                                        ], className='w-100'),
                                    ], style={'padding': '25px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                # dbc.Label('Daily rewards requirements'),
                                                dbc.CardBody([
                                                    dbc.Label('Days until your desired daily rewards'),
                                                    html.Div(style={'color': 'white', 'fontSize': 50},
                                                             id='rewardsDaily'),
                                                    dbc.Label('Required KLIMA for desired daily rewards'),
                                                    html.Div(style={'color': 'white', 'fontSize': 50},
                                                             id='requiredDaily'),
                                                ])
                                            ])
                                        ], className='w-100'),
                                        dbc.Col([
                                            dbc.Card([
                                                # dbc.Label('Daily rewards requirements'),
                                                dbc.CardBody([
                                                    dbc.Label('Days until your desired weekly rewards'),
                                                    html.Div(style={'color': 'white', 'fontSize': 50},
                                                             id='rewardsWeekly'),
                                                    dbc.Label('Required KLIMA for desired weekly rewards'),
                                                    html.Div(style={'color': 'white', 'fontSize': 50},
                                                             id='requiredWeekly'),
                                                ])
                                            ])
                                        ], className='w-100')
                                    ], style={'padding': '25px'})
                                ])
                            ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('Rewards strategizer controls'),
                                dbc.CardBody([
                                    dbc.Form([
                                        dbc.Card(
                                            dbc.CardBody([
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Label('Price of Klima (USDC)'),
                                                        dbc.Input(
                                                            id='priceKlima',
                                                            placeholder='1000',
                                                            type='number',
                                                            min=1,
                                                            value=1000,
                                                            style={'background-color': '#222222', 'color': 'white',
                                                                   'width': '100%'}
                                                        )
                                                    ], className='w-100'),
                                                    dbc.Col([
                                                        dbc.Label('Price of Matic(USDC)'),
                                                        dbc.Input(
                                                            id='priceofETH',
                                                            placeholder='10',
                                                            type='number',
                                                            min=1,
                                                            value=10,
                                                            style={'background-color': '#222222', 'color': 'white',
                                                                   'width': '100%'}
                                                        )
                                                    ], className='w-100'),
                                                ], style={'padding': '25px'}),
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Label('Desired KLIMA Value (USDC)'),
                                                        dbc.Input(
                                                            id='desired_klima_usdc',
                                                            placeholder='500.0',
                                                            type='number',
                                                            min=1,
                                                            value=10000, style={'color': 'white', 'width': '100%'}
                                                        )
                                                    ], className='w-100'),
                                                    dbc.Col([
                                                        dbc.Label('Desired KLIMA Amount (Units)'),
                                                        dbc.Input(
                                                            id='desired_klima_unit',
                                                            placeholder='500.0',
                                                            type='number',
                                                            min=1,
                                                            value=500, style={'color': 'white', 'width': '100%'}
                                                        )
                                                    ], className='w-100')
                                                ], style={'padding': '25px'}),
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Label('Desired daily staking rewards (USDC)'),
                                                        dbc.Input(
                                                            id='desired_daily_rewards_usdc',
                                                            placeholder='5000',
                                                            type='number',
                                                            min=1,
                                                            value=5000, style={'color': 'white', 'width': '100%'}
                                                        )
                                                    ], className='w-100'),
                                                    dbc.Col([
                                                        dbc.Label('Desired daily staking rewards (USDC)'),
                                                        dbc.Input(
                                                            id='desired_weekly_rewards_usdc',
                                                            placeholder='5000',
                                                            type='number',
                                                            min=1,
                                                            value=50000, style={'color': 'white', 'width': '100%'}
                                                        )
                                                    ], className='w-100')
                                                ], style={'padding': '25px'})
                                            ]), style={'padding': '25px'}
                                        )
                                    ])
                                ])
                            ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
                    ], className='mb-5'),
                    dbc.Row([
                        dbc.Col(dcc.Markdown('''
                        ## Explanations
                        ---
                        '''))
                    ], className='mb-5'),
                    dbc.Row([
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Chart Explanation'),
                            dbc.CardBody([
                                dcc.Markdown('''
                    - The chart shows you the Klima growth projection over 365.0 days. Projection is calculated based
                    on your selected APY of 7000% (Equivalent to a reward yield of 0.5%) and an initial 1.0 Klima.
                    - The (3,3) Profit adjusted ROI trend line shows you the adjusted Klima growth if you decide to
                    sell a percentage of your Klima at a fixed interval (For example, 5% every 30 days).
                    - The Min Growth Rate shows you the estimated Klima growth rate if the APY was on the minimum APY
                    of the current dictated KIP-3 Reward Rate Framework.
                    - The Max Growth Rate shows you the estimated Klima growth rate if the APY was on the maximum APY
                    of the current dictated KIP-3 Reward Rate Framework.
                    ''')
                            ])
                        ], outline=True, color='success'), className='w-50')
                    ], className="mb-5"),
                ]),

        dcc.Tab(label='Rewards Simulator guide',
                selected_style={'color': 'green', 'fontSize': '30px', 'height': '70px'},
                style={'color': 'green', 'fontSize': '30px', 'height': '70px'},
                children=[
                    dbc.Row([
                        html.Div(html.Img(src=app.get_asset_url('New_Klima_staking_page-01.png'),
                                          style={'height': '100%',
                                                 'width': '100%',
                                                 'padding': '50px'}))], className='w-100')
                ])
    ], className='mb-4'),
], fluid=True)  # Responsive ui control
