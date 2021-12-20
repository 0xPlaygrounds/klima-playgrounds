# Import all required packages for this page
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
from millify import millify
from app import app

from components.disclaimer import short_disclaimer_row

# Build the layout for the app. Using dash bootstrap container here instead of the standard html div.
# Container looks better
layout = dbc.Container([
    # Create a tab so we can have two sections for the klima growth/rewards simulation
    dbc.Tabs([
        dbc.Tab(label='(3,3) Simulator',
                label_style={'background': 'linear-gradient(71.9deg, #00CC33 24.64%, #00771E 92.66%)'},
                tab_style={'background': 'linear-gradient(71.9deg, #00CC33 24.64%, #00771E 92.66%)',
                           'fontSize': '30px'},
                active_tab_style={'color': '#0ba1ff'},
                active_label_style={'color': '#222222'},
                children=[
                    dbc.Row([
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Klima growth simulation results: Charts'),
                            dbc.CardBody([
                                dcc.Graph(id='graph1', style={"height": "100%", "width": "auto"}),
                            ], style={"height": "auto", "width": "auto"})
                        ], outline=False, color='#232b2b', style={"height": "100%", "width": "auto",
                                                                  'border-color': '#00cc33'}),
                            style={'padding': '10px'},
                            xs=12, sm=12, md=12, lg=8, xl=8),
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Simulation Controls'),
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        dcc.Markdown('''
                                        ##### Klima growth forecast controls
                                        ___
                                        '''),
                                    ]),
                                ]),
                                dbc.Row([
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
                                   dbc.Col(
                                       dbc.Label('Initial Klima')
                                   ),
                                   dbc.Col(
                                       dbc.Label('APY (%)')
                                   ),
                                   dbc.Col(
                                       dbc.Label('RFV (BCT)')
                                   )
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Input(
                                            id='initialKlima',
                                            placeholder='1.0',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=1, style={'background-color': '#222222', 'color': 'white',
                                                            'width': '100%'})]),
                                    dbc.Col([
                                        dbc.Input(
                                            id='user_apy',
                                            placeholder='40000',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=40000, style={'background-color': '#222222',
                                                                'color': 'white',
                                                                'width': '100%'})]),
                                    dbc.Col([
                                        dbc.Input(
                                            id='user_rfv',
                                            placeholder='5',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=5, style={'background-color': '#222222',
                                                            'color': 'white',
                                                            'width': '100%'})]),
                                ], className="g-2"),
                                dbc.Row([
                                   dbc.Col([
                                       html.Br(),
                                       dcc.Markdown('''
                                       ##### Profit taking controls
                                       '''),
                                   ])
                                ]),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Label('Amount (%)'),
                                    ),
                                    dbc.Col(
                                        dbc.Label('Cadence (Days)'),
                                    )
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Input(
                                            id='percentSale',
                                            placeholder='5',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=5,
                                            style={'background-color': '#222222', 'color': 'white',
                                                   'width': '100%'}),
                                    ]),
                                    dbc.Col([
                                        dbc.Input(
                                            id='sellDays',
                                            placeholder='30',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=30,
                                            style={'background-color': '#222222', 'color': 'white',
                                                   'width': '100%'}),
                                    ]),
                                ]),
                                dbc.Row([
                                    dbc.Col([
                                        dcc.Markdown('''---''')
                                    ]),
                                ]),
                                dbc.Label('Dollar cost averaging controls'),
                                dbc.Row([
                                    dbc.Label('Klima Price ($)'),
                                    dbc.Input(
                                        id='klimaPrice_DCA',
                                        placeholder='1000',
                                        type='number',
                                        min=1,
                                        step=0.001,
                                        debounce=True,
                                        value=1000, style={'background-color': '#222222',
                                                           'color': 'white',
                                                           'width': '100%'})
                                ]),
                                dbc.Row([
                                    dbc.Label('Purchase Amount ($)'),
                                    dbc.Input(
                                        id='valBuy',
                                        placeholder='1000',
                                        type='number',
                                        min=1,
                                        step=0.001,
                                        debounce=True,
                                        value=1000, style={'background-color': '#222222',
                                                           'color': 'white',
                                                           'width': '100%'}),
                                ]),
                                dbc.Row([
                                    dbc.Label('Cadence (Days)'),
                                    dbc.Input(
                                        id='buyDays',
                                        placeholder='30',
                                        type='number',
                                        min=1,
                                        value=30, style={'background-color': '#222222',
                                                         'color': 'white',
                                                         'width': '100%'}),
                                ])
                            ])
                        ], outline=False, color='#232b2b', style={"height": "100%", "width": "auto",
                                                                  'border-color': '#00cc33'}),
                            style={'padding': '10px'},
                            xs=12, sm=12, md=12, lg=4, xl=4)]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader('Klima growth simulation results: ROI',
                                               className='enclosure_card_topic'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Daily ROI',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='dailyROI'),
                                                        )
                                                    ], style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic")
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Klima Gained',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='dailyKlima'),
                                                        )
                                                    ]),
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('7 Day ROI',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='sevendayROI')
                                                        )
                                                    ], style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic")
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Klima Gained',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='sevendayKlima')
                                                        ),
                                                    ]),
                                                ], className='emission_card_style'),
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6)]),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Monthly ROI',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='monthlyROI')
                                                        ),
                                                    ], style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic")
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Klima Gained',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='monthlyKlima')
                                                        ),
                                                    ]),
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Annual ROI', className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='annualROI')
                                                        ),
                                                    ], style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic")),
                                                    dbc.Row([
                                                        dbc.Col(
                                                            dbc.Label('Klima Gained',
                                                                      className='emission_card_topic'),
                                                        ),
                                                        dbc.Col(
                                                            html.Div(className='emission_card_metric',
                                                                     id='annualKlima')
                                                        ),
                                                    ]),
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                    ]),
                                ]),
                            ], outline=False, style={'border-color': '#00cc33'})],
                            style={'padding': '10px', 'height': '100%'},
                            xs=12, sm=12, md=12, lg=6, xl=6),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('Klima to CO2 emissions equivalency',
                                               className='enclosure_card_topic'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(dbc.Label('Emissions from passenger vehicles driven',
                                                                      className="emission_card_topic"),
                                                            style={"height": "45%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic"),
                                                            style={"height": "10%"},
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.Div(className="emission_card_metric",
                                                                     id='passenger_vehicle_annual'),
                                                        ]),
                                                    ], style={"height": "45%"})
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(dbc.Label('Avg. miles driven'
                                                                      ' per passenger vehicle',
                                                                      className="emission_card_topic"),
                                                            style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic"),
                                                            style={"height": "10%"},
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.Div(className="emission_card_metric",
                                                                     id='passenger_miles_annual'),
                                                        ]),
                                                    ], style={"height": "50%"})
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(dbc.Label('Gallons of gasoline consumed',
                                                                      className="emission_card_topic"),
                                                            style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic"),
                                                            style={"height": "10%"},
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.Div(className="emission_card_metric",
                                                                     id='gasoline_consumed_annual'),
                                                        ]),
                                                    ], style={"height": "50%"})
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(dbc.Label('Acres of U.S. forest sequestering CO2'
                                                                      ' for one year',
                                                                      className="emission_card_topic"),
                                                            style={"height": "50%"}),
                                                    dbc.Row(dcc.Markdown(''' --- ''',
                                                                         className="emission_card_topic"),
                                                            style={"height": "10%"},
                                                            ),
                                                    dbc.Row([
                                                        dbc.Col([
                                                            html.Div(id='trees_co_captured',
                                                                     className="emission_card_metric"),
                                                        ]),
                                                    ], style={"height": "50%"})
                                                ], className='emission_card_style')
                                            ], style={"height": "100%", "padding": "10px"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                    ]),
                                ])
                            ], outline=False, style={'border-color': '#00cc33', 'height': '100%', 'width': '100%'}),
                            style={'padding': '10px'},
                            xs=12, sm=12, md=12, lg=6, xl=6)
                    ]),
                    dbc.Row([
                        dbc.Col(dbc.Label('Rewards Strategizer',
                                          className="page_section_topic"))
                    ]),
                    dbc.Row([
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('Rewards strategy results'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(
                                                        dbc.Label('Days until USDC Value',
                                                                  style={'color': 'white', 'fontSize': 15,
                                                                         'textAlign': 'center'}),
                                                    ),
                                                    dbc.Row(
                                                        html.Div(style={'color': 'white', 'fontSize': 50,
                                                                        'textAlign': 'center'},
                                                                 id='rewardsUSD'),
                                                    ),
                                                ], className='align-self-center'),
                                            ], style={'width': '100%', 'padding': '10px'})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(
                                                        dbc.Label('Days until KLIMA amount',
                                                                  style={'color': 'white', 'fontSize': 15,
                                                                         'textAlign': 'center'}),
                                                    ),
                                                    dbc.Row(
                                                        html.Div(style={'color': 'white', 'fontSize': 50,
                                                                        'textAlign': 'center'},
                                                                 id='rewardsKLIMA'),
                                                    ),
                                                ], className='align-self-center')
                                            ], style={'width': '100%', 'padding': '10px'})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(
                                                        dbc.Label('Days until your desired daily rewards',
                                                                  style={'color': 'white', 'fontSize': 15,
                                                                         'textAlign': 'center'}),
                                                    ),
                                                    dbc.Row(
                                                        html.Div(style={'color': 'white', 'fontSize': 50,
                                                                        'textAlign': 'center'},
                                                                 id='rewardsDaily'),
                                                    ),
                                                    dbc.Row(
                                                        dbc.Label('Required KLIMA for desired daily rewards',
                                                                  style={'color': 'white', 'fontSize': 15,
                                                                         'textAlign': 'center'}),
                                                    ),
                                                    dbc.Row(
                                                        html.Div(style={'color': 'white', 'fontSize': 50,
                                                                        'textAlign': 'center'},
                                                                 id='requiredDaily'),
                                                    ),
                                                ], className='align-self-center')
                                            ], style={'padding': '10px', 'height': "100%"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6, style={'height': "100%"}),
                                        dbc.Col([
                                            dbc.Card([
                                                dbc.CardBody([
                                                    dbc.Row(
                                                        dbc.Label('Days until your desired weekly rewards',
                                                                  style={'color': 'white', 'fontSize': 15,
                                                                         'textAlign': 'center'}
                                                                  ),
                                                    ),
                                                    dbc.Row(
                                                        html.Div(style={'color': 'white', 'fontSize': 50,
                                                                        'textAlign': 'center'},
                                                                 id='rewardsWeekly'),
                                                    ),
                                                    dbc.Row(
                                                        dbc.Label('Required KLIMA for desired weekly rewards',
                                                                  style={'color': 'white', 'fontSize': 15,
                                                                         'textAlign': 'center'}
                                                                  ),
                                                    ),
                                                    dbc.Row(
                                                        html.Div(style={'color': 'white', 'fontSize': 50,
                                                                        'textAlign': 'center'},
                                                                 id='requiredWeekly'),
                                                    ),
                                                ], className='align-self-center')
                                            ], style={'padding': '10px', 'height': "100%"})
                                        ], xs=12, sm=12, md=12, lg=6, xl=6, style={'height': "100%"})
                                    ])
                                ])
                            ], outline=True, color='success', style={"height": "auto"}), style={'padding': '10px'}),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('Rewards strategizer controls'),
                                dbc.CardBody([
                                    dbc.Form([
                                        dbc.Card(
                                            dbc.CardBody([
                                                dbc.Row([
                                                    dbc.Col(
                                                        dbc.Label('Price of Klima (USDC)'),
                                                    ),
                                                    dbc.Col(
                                                        dbc.Label('Price of Matic (USDC)'),
                                                    ),
                                                ]),
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Input(
                                                            id='priceKlima',
                                                            placeholder='1000',
                                                            type='number',
                                                            min=1,
                                                            step=0.001,
                                                            debounce=True,
                                                            value=1000,
                                                            style={'background-color': '#222222',
                                                                   'color': 'white',
                                                                   'width': '100%',
                                                                   'padding': '10px'})]),
                                                    dbc.Col([
                                                        dbc.Input(
                                                            id='priceofETH',
                                                            placeholder='10',
                                                            type='number',
                                                            min=1,
                                                            step=0.001,
                                                            debounce=True,
                                                            value=10,
                                                            style={'background-color': '#222222',
                                                                   'color': 'white',
                                                                   'width': '100%',
                                                                   'padding': '10px'})])
                                                ]),
                                                dbc.Row([
                                                    dbc.Col(
                                                        dbc.Label('Desired KLIMA Value (USDC)'),
                                                    ),
                                                    dbc.Col(
                                                        dbc.Label('Desired KLIMA Amount (Units)'),
                                                    ),
                                                ], style={'padding': '10px'}),
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Input(
                                                            id='desired_klima_usdc',
                                                            placeholder='500.0',
                                                            type='number',
                                                            min=1,
                                                            step=0.001,
                                                            debounce=True,
                                                            value=10000, style={'background-color': '#222222',
                                                                                'color': 'white',
                                                                                'width': '100%',
                                                                                'padding': '10px'})]),
                                                    dbc.Col([
                                                        dbc.Input(
                                                            id='desired_klima_unit',
                                                            placeholder='500.0',
                                                            type='number',
                                                            min=1,
                                                            step=0.001,
                                                            debounce=True,
                                                            value=500, style={'background-color': '#222222',
                                                                              'color': 'white',
                                                                              'width': '100%',
                                                                              'padding': '10px'})])]),
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Label('Desired daily staking rewards (USDC)'),
                                                    ]),
                                                    dbc.Col([
                                                        dbc.Label('Desired daily staking rewards (USDC)'),
                                                    ]),
                                                ], style={'padding': '10px'}),
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Input(
                                                            id='desired_daily_rewards_usdc',
                                                            placeholder='5000',
                                                            type='number',
                                                            min=1,
                                                            step=0.001,
                                                            debounce=True,
                                                            value=5000, style={'background-color': '#222222',
                                                                               'color': 'white',
                                                                               'width': '100%',
                                                                               'padding': '10px'})]),
                                                    dbc.Col([
                                                        dbc.Input(
                                                            id='desired_weekly_rewards_usdc',
                                                            placeholder='5000',
                                                            type='number',
                                                            min=1,
                                                            step=0.001,
                                                            debounce=True,
                                                            value=50000, style={'background-color': '#222222',
                                                                                'color': 'white',
                                                                                'width': '100%',
                                                                                'padding': '10px'})])])
                                            ]), style={'padding': '10px'}
                                        )
                                    ])
                                ])
                            ], outline=True, color='success', style={"height": "100%", "width": "100%"}),
                            style={'padding': '10px'},
                            xs=12, sm=12, md=12, lg=6, xl=6),
                    ]),
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
                        ], outline=True, color='success'), xs=12, sm=12, md=12, lg=12, xl=12)
                    ], className="mb-5"),
                ]),

        dbc.Tab(label='Guide',
                label_style={'background': 'linear-gradient(71.9deg, #00CC33 24.64%, #00771E 92.66%)',
                             'fontSize': '30px'},
                tab_style={'background': 'linear-gradient(71.9deg, #00CC33 24.64%, #00771E 92.66%)'},
                active_tab_style={'background': '#0ba1ff', 'fontSize': '30px'},
                active_label_style={'color': '#222222'},
                children=[
                    dbc.Row([
                        html.Div(html.Img(src=app.get_asset_url('PG_Staking_Learn.png'),
                                          style={'height': '100%',
                                                 'width': '100%',
                                                 'padding': '10px'}))])
                ])
    ], className='mb-4'),
], fluid=True)  # Responsive ui control


# call back for klima growth controls and strategizer
@app.callback([
    Output(component_id='graph1', component_property='figure'),
    Output(component_id='dailyROI', component_property='children'),
    Output(component_id='dailyKlima', component_property='children'),
    Output(component_id='sevendayROI', component_property='children'),
    Output(component_id='sevendayKlima', component_property='children'),
    Output(component_id='monthlyROI', component_property='children'),
    Output(component_id='monthlyKlima', component_property='children'),
    Output(component_id='annualROI', component_property='children'),
    Output(component_id='annualKlima', component_property='children'),
    Output(component_id='passenger_vehicle_annual', component_property='children'),
    Output(component_id='passenger_miles_annual', component_property='children'),
    Output(component_id='gasoline_consumed_annual', component_property='children'),
    Output(component_id='trees_co_captured', component_property='children'),
    Output(component_id='rewardsUSD', component_property='children'),
    Output(component_id='rewardsKLIMA', component_property='children'),
    Output(component_id='rewardsDaily', component_property='children'),
    Output(component_id='requiredDaily', component_property='children'),
    Output(component_id='rewardsWeekly', component_property='children'),
    Output(component_id='requiredWeekly', component_property='children'),
    Input(component_id='growthDays', component_property='value'),
    Input(component_id='initialKlima', component_property='value'),
    Input(component_id='user_apy', component_property='value'),
    Input(component_id='user_rfv', component_property='value'),
    Input(component_id='percentSale', component_property='value'),
    Input(component_id='sellDays', component_property='value'),
    Input(component_id='klimaPrice_DCA', component_property='value'),
    Input(component_id='valBuy', component_property='value'),
    Input(component_id='buyDays', component_property='value'),
    Input(component_id='priceKlima', component_property='value'),
    Input(component_id='priceofETH', component_property='value'),
    Input(component_id='desired_klima_usdc', component_property='value'),
    Input(component_id='desired_klima_unit', component_property='value'),
    Input(component_id='desired_daily_rewards_usdc', component_property='value'),
    Input(component_id='desired_weekly_rewards_usdc', component_property='value'),
])
# function to calculate klima growth over user specified number of days
def klimaGrowth_Projection(growthDays, initialKlima,
                           user_apy, user_rfv,
                           percentSale, sellDays, klimaPrice_DCA,
                           valBuy, buyDays,
                           priceKlima, priceofETH,
                           desired_klima_usdc, desired_klima_unit,
                           desired_daily_rewards_usdc,
                           desired_weekly_rewards_usdc):
    # ===========================Variable definitions and prep===============================
    # In this section we take the input variables and do any kind of prep work
    klimaGrowthEpochs = (growthDays * 3) + 1
    sellEpochs = sellDays * 3
    buyEpochs = buyDays * 3
    cadenceConst = sellEpochs
    cadenceConst_BUY = buyEpochs
    dcaAmount = valBuy / klimaPrice_DCA
    percentSale = percentSale / 100
    user_apy = user_apy / 100
    minAPY = 1000 / 100
    maxAPY = 10000 / 100
    gwei = 1
    reward_yield = ((1 + user_apy) ** (1 / float(1095))) - 1
    reward_yield = round(reward_yield, 5)
    rebase_const = 1 + reward_yield

    # In this section, we calculate the staking and unstaking fees. Not required for klima
    staking_gas_fee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    staking_gas_fee_klimaAmount = staking_gas_fee / klimaPrice_DCA
    # unstaking_gas_fee = 89654 * ((gwei * priceofETH) / (10 ** 9))

    # In this section we calculate the reward yield from the users speculated APY
    reward_yield = ((1 + user_apy) ** (1 / float(1095))) - 1
    minOIPYield = ((1 + minAPY) ** (1 / float(1095))) - 1
    maxOIPYield = ((1 + maxAPY) ** (1 / float(1095))) - 1

    # In this case let's consider 1096 Epochs which is 365 days
    klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    klimaGrowth_df['Days'] = klimaGrowth_df.Epochs / 3  # There are 3 Epochs per day so divide by 3 to get Days

    profitAdjusted_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    profitAdjusted_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    dollarCostAVG_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    dollarCostAVG_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3
    # ===========================Variable definitions and prep===============================

    # ============================ USER APY, DCA, PROFIT ADJUSTED PROJECTION =====
    # we loop through the exponential klima growth equation every epoch
    totalklimas = []  # create an empty array that will hold the componded rewards
    pA_totalklimas = []
    dcA_totalklimas = []

    reward_yield = round(reward_yield, 5)
    klimaStakedGrowth = initialKlima  # Initial staked klimas used to project growth over time
    pA_klimaStakedGrowth = initialKlima
    dcA_klimaStakedGrowth = initialKlima
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas.append(klimaStakedGrowth)  # populate the empty array with calclated values each iteration
        pA_totalklimas.append(pA_klimaStakedGrowth)
        dcA_totalklimas.append(dcA_klimaStakedGrowth)

        klimaStakedGrowth = klimaStakedGrowth * (1 + reward_yield)  # compound the total amount of klimas
        pA_klimaStakedGrowth = pA_klimaStakedGrowth * (1 + reward_yield)
        dcA_klimaStakedGrowth = dcA_klimaStakedGrowth * (1 + reward_yield)

        if elements == sellEpochs:
            sellEpochs = sellEpochs + cadenceConst
            pA_klimaStakedGrowth = pA_totalklimas[-1] - (pA_totalklimas[-1] * percentSale)
        else:
            pass

        if elements == buyEpochs:
            buyEpochs = buyEpochs + cadenceConst_BUY
            dcA_klimaStakedGrowth = (dcA_klimaStakedGrowth + (dcaAmount - staking_gas_fee_klimaAmount))
        else:
            pass

    klimaGrowth_df['Total_klimas'] = totalklimas  # Clean up and add the new array to the main data frame
    klimaGrowth_df['Profit_Adjusted_Total_klimas'] = pA_totalklimas
    klimaGrowth_df['DCA_Adjusted_Total_klimas'] = dcA_totalklimas
    # Python is funny so let's round up our numbers . 1 decimal place for days",
    klimaGrowth_df.Days = np.around(klimaGrowth_df.Days,
                                    decimals=1)
    # Python is funny so let's round up our numbers . 3 decimal place for klimas"
    klimaGrowth_df.Total_klimas = np.around(klimaGrowth_df.Total_klimas,
                                            decimals=3)
    klimaGrowth_df.Profit_Adjusted_Total_klimas = np.around(klimaGrowth_df.Profit_Adjusted_Total_klimas, decimals=3)
    klimaGrowth_df.DCA_Adjusted_Total_klimas = np.around(klimaGrowth_df.DCA_Adjusted_Total_klimas, decimals=3)
    # ============================ USER APY, DCA, PROFIT ADJUSTED PROJECTION =====

    # ============================ MIN APY PROJECTION ============================
    totalklimas_minOIPRate = []
    minOIPYield = round(minOIPYield, 5)
    klimaStakedGrowth_minOIPRate = initialKlima  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_minOIPRate.append(
            klimaStakedGrowth_minOIPRate)  # populate the empty array with calculated values each iteration
        klimaStakedGrowth_minOIPRate = klimaStakedGrowth_minOIPRate * (
                1 + minOIPYield)  # compound the total amount of klimas
    klimaGrowth_df['Min_klimaGrowth'] = totalklimas_minOIPRate  # Clean up and add the new array to the main data frame
    # ============================ MIN APY PROJECTION ============================

    # ============================ MAX APY PROJECTION ============================
    totalklimas_maxOIPRate = []
    maxOIPYield = round(maxOIPYield, 5)
    klimaStakedGrowth_maxOIPRate = initialKlima  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_maxOIPRate.append(
            klimaStakedGrowth_maxOIPRate)  # populate the empty array with calculated values each iteration
        klimaStakedGrowth_maxOIPRate = klimaStakedGrowth_maxOIPRate * (
                1 + maxOIPYield)  # compound the total amount of klimas
    klimaGrowth_df['Max_klimaGrowth'] = totalklimas_maxOIPRate  # Clean up and add the new array to the main data frame
    # ============================ MAX APY PROJECTION ============================

    # Let's get some ROI Outputs starting with the daily
    dailyROI = (1 + reward_yield) ** 3 - 1  # Equation to calculate your daily ROI based on reward Yield
    dailyROI_P = round(dailyROI * 100, 1)  # daily ROI in Percentage
    dailyKlima = initialKlima + (dailyROI * initialKlima)
    # ================================================================================

    # 5 day ROI
    # fivedayROI = (1 + reward_yield) ** (5 * 3) - 1  # Equation to calculate your 5 day ROI based on reward Yield
    # fivedayROI_P = round(fivedayROI * 100, 1)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    sevendayROI = (1 + reward_yield) ** (7 * 3) - 1  # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI_P = round(sevendayROI * 100, 1)  # 7 day ROI in Percentage
    sevendayKlima = initialKlima + (sevendayROI * initialKlima)
    # ================================================================================

    # 30 day ROI
    monthlyROI = (1 + reward_yield) ** (30 * 3) - 1  # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI_P = round(monthlyROI * 100, 1)  # 30 day ROI in Percentage
    monthlyKlima = initialKlima + (monthlyROI * initialKlima)
    # ================================================================================

    # Annual ROI
    annualROI = (1 + reward_yield) ** (365 * 3) - 1  # Equation to calculate your annual ROI based on reward Yield
    annualROI_P = round(annualROI * 100, 1)  # Equation to calculate your annual ROI based on reward Yield
    annualKlima = initialKlima + (annualROI * initialKlima)
    # ================================================================================
    # ================================Real world impact calc =========================
    locked_carbon_tonnes = annualKlima * user_rfv
    passenger_vehicle_annual = '{}'.format(millify((locked_carbon_tonnes / 4.60), precision=1))
    passenger_miles_annual = '{}'.format(millify((locked_carbon_tonnes / 0.000398), precision=1))
    gasoline_consumed_annual = '{}'.format(millify((locked_carbon_tonnes / 0.008887), precision=1))
    # home_energy_annual = '{}'.format(millify((locked_carbon_tonnes / 8.30), precision=1))
    # home_electricity_annual = '{}'.format(millify((locked_carbon_tonnes / 5.505), precision=1))
    # oil_consumed_annual = '{}'.format(millify((locked_carbon_tonnes / 0.43), precision=1))
    # coals_burned_annual = '{}'.format(millify((locked_carbon_tonnes / 0.000905), precision=1))
    trees_co_captured = '{}'.format(millify((locked_carbon_tonnes / 0.82), precision=1))
    # ================================Real world impact calc =========================

    # ================================Rewards strategizer=============================
    # ================================================================================
    # Days until you reach target USD by staking only
    forcastUSDTarget = round((math.log(desired_klima_usdc / (initialKlima * priceKlima), rebase_const) / 3))
    # ================================================================================
    # Days until you reach target Klima by staking only
    forcastKlimaTarget = round((math.log(desired_klima_unit / initialKlima, rebase_const) / 3))
    # ================================================================================
    # Daily Incooom calculations
    # Required Klimas until you are earning your desired daily incooom
    requiredKlimaDailyIncooom = round((desired_daily_rewards_usdc / dailyROI) / priceKlima)
    # Days until you are earning your desired daily incooom from your current initial staked Klima amount
    forcastDailyIncooom = round(math.log((requiredKlimaDailyIncooom / initialKlima), rebase_const) / 3)
    rewardsDaily = forcastDailyIncooom
    # requiredUSDForDailyIncooom = requiredKlimaDailyIncooom * priceKlima
    # ================================================================================
    # Weekly Incooom calculations
    # Required Klimas until you are earning your desired weekly incooom
    requiredKlimaWeeklyIncooom = round((desired_weekly_rewards_usdc / sevendayROI) / priceKlima)
    # Days until you are earning your desired weekly incooom from your current initial staked Klima amount
    forcastWeeklyIncooom = round(math.log((requiredKlimaWeeklyIncooom / initialKlima), rebase_const) / 3)
    # requiredUSDForWeeklyIncooom = requiredKlimaWeeklyIncooom * priceKlima
    # ================================Rewards strategizer=============================

    # =============================OUTPUT FORMATTING===================================

    klimaGrowth_Chart = go.Figure()
    klimaGrowth_Chart.add_trace(
        go.Scatter(x=klimaGrowth_df.Days, y=klimaGrowth_df.Total_klimas, name='(3,3) ROI', fill=None))
    klimaGrowth_Chart.add_trace(go.Scatter(x=klimaGrowth_df.Days, y=klimaGrowth_df.Profit_Adjusted_Total_klimas,
                                           name='(3,3) Profit adjusted ROI  ', fill=None))
    klimaGrowth_Chart.add_trace(
        go.Scatter(x=klimaGrowth_df.Days, y=klimaGrowth_df.DCA_Adjusted_Total_klimas, name='(3,3) DCA adjusted ROI  ',
                   fill=None))
    klimaGrowth_Chart.add_trace(
        go.Scatter(x=klimaGrowth_df.Days, y=klimaGrowth_df.Min_klimaGrowth, name='Min Growth Rate  ', fill=None))
    klimaGrowth_Chart.add_trace(
        go.Scatter(x=klimaGrowth_df.Days, y=klimaGrowth_df.Max_klimaGrowth, name='Max Growth Rate  ', fill=None))

    klimaGrowth_Chart.update_layout(autosize=True, showlegend=True, margin=dict(l=20, r=30, t=10, b=20))
    klimaGrowth_Chart.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    klimaGrowth_Chart.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01, ), xaxis_title="Days",
                                    yaxis_title="Total klimas")
    klimaGrowth_Chart.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white', showgrid=False,
                                   gridwidth=0.01, mirror=True)
    klimaGrowth_Chart.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white', showgrid=False,
                                   gridwidth=0.01, mirror=True, zeroline=False)
    klimaGrowth_Chart.layout.legend.font.color = 'white'

    dailyROI_P = '{} %'.format(dailyROI_P)
    dailyKlima = '{0:.2f}'.format(dailyKlima)
    sevendayROI_P = '{} %'.format(sevendayROI_P)
    sevendayKlima = '{0:.2f}'.format(sevendayKlima)
    monthlyROI_P = '{} %'.format(monthlyROI_P)
    monthlyKlima = '{0:.2f}'.format(monthlyKlima)
    annualROI_P = '{} %'.format(millify(annualROI_P, precision=1))
    annualKlima = '{0:.1f}'.format(annualKlima)

    return klimaGrowth_Chart, dailyROI_P, dailyKlima, sevendayROI_P, sevendayKlima, monthlyROI_P, \
           monthlyKlima, annualROI_P, annualKlima, passenger_vehicle_annual, passenger_miles_annual,\
           gasoline_consumed_annual, trees_co_captured, forcastUSDTarget, \
           forcastKlimaTarget, rewardsDaily, requiredKlimaDailyIncooom, forcastWeeklyIncooom, \
           requiredKlimaWeeklyIncooom  # noqa: E127
