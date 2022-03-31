# Import all required packages for this page
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html, State
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
from millify import millify

from ..app import app
from ..components import staking_guides as s_g
from ..components import playgrounds_guide_staking as p_g_s
from ..components.disclaimer import short_disclaimer_row
from ..config import RFV_TERM, RFV_WORDS


# Build the layout for the app. Using dash bootstrap container here instead of the standard html div.
# Container looks better
layout = dbc.Container([
    html.Div([
        # Create a tab so we can have two sections for the klima growth/rewards simulation
        dbc.Tabs([
            dbc.Tab(label='Guide',
                    label_style={'background': '#02C132',
                                 'fontSize': '20px', 'color': 'black'},
                    tab_style={'background': '#02C132',
                               'marginLeft': 'auto'},
                    active_tab_style={'background': '#02C132', 'fontSize': '20px', 'font-weight': 'bold'},
                    active_label_style={'color': '#ffffff'},
                    tab_id='staking_guide_tab',
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(dbc.Label('Staking',
                                                      className="learning_hub_category_topic"),
                                            xs=12, sm=12, md=12, lg=6, xl=6),
                                ]),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Card([
                                            dbc.CardHeader('Learn the fundamentals of Staking on KlimaDAO',
                                                           className='learning_hub_category_deck_topic'),
                                            dbc.CardBody([
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('What is Staking?',
                                                                              className='learning_hub_'
                                                                                        'category_card_topic',
                                                                              )
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(s_g.what_is_staking_intro,
                                                                            style={'text-align': 'center'}),
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(dbc.ModalTitle('What is Staking?')),
                                                                    dbc.ModalBody([
                                                                        s_g.what_is_staking
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='what_is_staking_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='what_is_staking_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='what_is_staking_btn_open',
                                                                               n_clicks=0,
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('Why should I Stake?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(
                                                                        s_g.why_should_i_stake_intro,
                                                                        style={'text-align': 'center'}
                                                                    )
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle('Why should I stake?')),
                                                                    dbc.ModalBody([
                                                                        s_g.why_should_i_stake
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='why_should_i_stake_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='why_should_i_stake_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='why_should_i_stake_btn_open',
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('How can I Stake?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col([
                                                                        s_g.how_can_i_stake_intro
                                                                    ], style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle('How can I stake?')),
                                                                    dbc.ModalBody([
                                                                        s_g.how_can_i_stake
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='how_can_i_stake_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='how_can_i_stake_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                )
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               color='link',
                                                                               id='how_can_i_stake_btn_open',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                )),
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('The dynamics of staking (3,3)',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col([
                                                                        s_g.staking_dynamics_intro
                                                                    ], style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle(
                                                                            'The dynamics of staking (3,3)')),
                                                                    dbc.ModalBody([
                                                                        s_g.staking_dynamics
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='staking_dynamics_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='staking_dynamics_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                    size='xl',
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               color='link',
                                                                               id='staking_dynamics_btn_open',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ))
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                ])
                                            ]),
                                        ], outline=False, color='#202020', style={"height": "100%", "width": "100%"}),
                                        xs=12, sm=12, md=12, lg=12, xl=12, style={'padding': '10px'}),
                                ]),
                            ])
                        ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(dbc.Label('Playgrounds',
                                                      className="learning_hub_category_topic"),
                                            xs=12, sm=12, md=12, lg=6, xl=6),
                                ]),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Card([
                                            dbc.CardHeader('Learn how to use the Staking Simulator',
                                                           className='learning_hub_category_deck_topic'),
                                            dbc.CardBody([
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('How to read the growth chart',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(p_g_s.how_to_read_growth_chart_intro,
                                                                            style={'text-align': 'center'})
                                                                ),

                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle('How to read the growth chart')),
                                                                    dbc.ModalBody([
                                                                        p_g_s.how_to_read_growth_chart
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='how_to_read_growth_chart_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='how_to_read_growth_chart_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                )
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='how_to_read_growth_chart_btn_open',
                                                                               n_clicks=0,
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('How to use the Simulation Controls?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(p_g_s.how_to_simulation_controls_intro,
                                                                            style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle(
                                                                            'How to use the simulation controls')),
                                                                    dbc.ModalBody([
                                                                        p_g_s.how_to_simulation_controls
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='how_to_use_sim_controls_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='how_to_use_sim_controls_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                    size='xl'
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='how_to_use_sim_controls_btn_open',
                                                                               n_clicks=0,
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('Interpretation of Carbon emissions',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(p_g_s.how_to_read_co_metrics_intro,
                                                                            style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle(
                                                                            'How to interpret carbon '
                                                                            'emissions metrics')),
                                                                    dbc.ModalBody([
                                                                        p_g_s.how_to_read_co_metrics
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='how_to_read_co_metrics_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='how_to_read_co_metrics_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                    size='xl',
                                                                )
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='how_to_read_co_metrics_btn_open',
                                                                               n_clicks=0,
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('How to use the Rewards Strategizer?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(p_g_s.how_to_use_strategizer_intro,
                                                                            style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle(
                                                                            'How to use the rewards strategizer')
                                                                    ),
                                                                    dbc.ModalBody([
                                                                        p_g_s.how_to_use_strategizer
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='how_to_use_strategizer_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='how_to_use_strategizer_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                    size='lg'
                                                                )
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='how_to_use_strategizer_btn_open',
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                                ])
                                            ]),
                                        ], outline=False, color='#202020', style={"height": "100%", "width": "100%"}),
                                        xs=12, sm=12, md=12, lg=12, xl=12, style={'padding': '10px'}),
                                ]),
                            ])
                        ]),
                    ]),
            dbc.Tab(label='Simulator',
                    label_style={'background': '#038523',
                                 'fontSize': '20px', 'color': 'black'},
                    tab_style={'background': '#038523',
                               'fontSize': '20px'},
                    active_tab_style={'background': '#038523', 'fontSize': '20px', 'font-weight': 'bold'},
                    active_label_style={'color': '#ffffff'},
                    tab_id='staking_simulator_tab',
                    children=[
                        dbc.Row([
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('Klima growth simulation results: Charts',
                                               className='simulator_hub_card_topic',
                                               style={'color': '#FFFFFF',
                                                      'background-color': '#2A2A2A',
                                                      'font-weight': '500',
                                                      'font-size': '26px',
                                                      'font-style': 'normal'}
                                               ),
                                dbc.CardBody([
                                    dcc.Graph(id='graph1', style={"height": "100%", "width": "auto"}),
                                    dbc.Tooltip(
                                        'This chart provides a visual representation of your speculated KLIMA'
                                        'growth over the selected number of days. It also, shows how dollar'
                                        'cost averaging and profit taking affects your growth over time',
                                        target='graph1',
                                        placement='top',
                                    )
                                ], style={"height": "auto", "width": "auto"})
                            ], outline=False, color='#2A2A2A', style={"height": "100%", "width": "auto"}),
                                style={'padding': '10px'},
                                xs=12, sm=12, md=12, lg=8, xl=8),
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('Simulation Controls',
                                               className='simulator_hub_card_topic',
                                               style={'color': '#FFFFFF',
                                                      'background-color': '#2A2A2A',
                                                      'font-weight': '500',
                                                      'font-size': '26px',
                                                      'font-style': 'normal'}
                                               ),
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
                                        dbc.Col([dbc.Label('Days')],
                                                width='6'),
                                        dbc.Col([dbc.Switch(
                                            id="days_input_selector",
                                            label="Slider/Input box",
                                            value=False),
                                        ],
                                            width='6')
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            html.Div(
                                                dcc.Slider(
                                                    id='growthDays',
                                                    min=1,
                                                    max=1000,
                                                    value=365,
                                                    tooltip={'placement': 'top', 'always_visible': True}),
                                                id='dynamic_days_controls'),
                                            dbc.Tooltip(
                                                'Input your simulation time frame in days. Keep in mind that the days'
                                                'you use also be used for the profit taking and dollar cost averaging '
                                                'calculations. Use the toggle switch to choose between a slider or'
                                                'standard input box',
                                                target='dynamic_days_controls',
                                                placement='top',
                                            ),
                                            dbc.Tooltip(
                                                'Use this toggle to select your preferred days input type.',
                                                target='days_input_selector',
                                                placement='top',
                                            ),
                                        ])
                                    ], style={'padding': '0px', 'padding-bottom': '10px'}),
                                    dbc.Row([
                                        dbc.Col(
                                            dbc.Label('Initial Klima')
                                        ),
                                        dbc.Col(
                                            dbc.Label(RFV_TERM)
                                        )
                                    ], style={'padding-bottom': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(
                                                id='initialKlima',
                                                placeholder='1.0',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=1,
                                                className="input_box_number",
                                                style={'color': 'white'}),
                                            dbc.Tooltip(
                                                'Input your desired initial number of Klima for calculation. '
                                                'Keep in mind '
                                                'this value is also used to in the profit taking and dollar cost '
                                                'averaging '
                                                'calculations.',
                                                target='initialKlima',
                                                placement='top',
                                            )
                                        ]),
                                        dbc.Col([
                                            dbc.Input(
                                                id='user_rfv',
                                                placeholder='5',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=5, className="input_box_number", style={'color': 'white'}),
                                            dbc.Tooltip(
                                                f'Input {RFV_TERM} for {RFV_WORDS} forecasting. '
                                                f'{RFV_TERM} is used to speculate the minimum amount of carbon offsets '
                                                f'you will have accumulated at the end of your speculated time frame.',
                                                target='user_rfv',
                                                placement='top',
                                            )
                                        ]),
                                    ], className="g-2", style={'padding-bottom': '10px', 'padding-top': '0px'}),
                                    dbc.Row([
                                        dbc.Col(
                                            dbc.Label('Min ARY(%)')
                                        ),
                                        dbc.Col(
                                            dbc.Label('ARY(%)')
                                        ),
                                        dbc.Col(
                                            dbc.Label('Max ARY(%)')
                                        )
                                    ], style={'padding-bottom': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(
                                                id='min_ary',
                                                placeholder='2000',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=2000,
                                                className="input_box_number",
                                                style={'color': 'white'}),
                                            dbc.Tooltip(
                                                'Input the current or future minimum ARY based on KIP-3 framework',
                                                target='min_ary',
                                                placement='top',
                                            )
                                        ]),
                                        dbc.Col([
                                            dbc.Input(
                                                id='user_ary',
                                                placeholder='8000',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=8000, className="input_box_number",
                                                style={'color': 'white'}),
                                            dbc.Tooltip(
                                                'Input an ARY for growth forecasting. ARY can be current protocol ARY'
                                                ' or some future ARY.',
                                                target='user_ary',
                                                placement='top',
                                            )
                                        ]),
                                        dbc.Col([
                                            dbc.Input(
                                                id='max_ary',
                                                placeholder='10000',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=10000, className="input_box_number", style={'color': 'white'}),
                                            dbc.Tooltip(
                                                'Input the current or future maximum ARY based on KIP-3 framework',
                                                target='max_ary',
                                                placement='top',
                                            )
                                        ]),
                                    ], className="g-2", style={'padding-bottom': '10px', 'padding-top': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            html.Br(),
                                            dcc.Markdown('''
                                    ##### Profit taking controls
                                    ___
                                    '''),
                                        ])
                                    ]),
                                    dbc.Row([
                                        dbc.Col([dbc.Switch(
                                            id='ptc_input_selector',
                                            label='Amount (Fixed or % )',
                                            value=True)],
                                            width='6'),
                                        dbc.Col(
                                            dbc.Label('Cadence (Days)'),
                                            width='6'
                                        )
                                    ], style={'padding-bottom': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            html.Div(
                                                dbc.Input(
                                                    id='percentSale',
                                                    placeholder='9',
                                                    type='number',
                                                    min=1,
                                                    step=0.001,
                                                    debounce=True,
                                                    value=5,
                                                    className="input_box_number", style={'color': 'white'}),
                                                id='dynamic_ptc_controls'
                                            ),
                                            dbc.Tooltip(
                                                'Use this toggle to choose between Fixed or percentage amount for '
                                                'your profit taking simulation',
                                                target='ptc_input_selector',
                                                placement='top',
                                            ),
                                            dbc.Tooltip(
                                                'Input your desired amount of Klima to sell either as a percentage of '
                                                'accumulated Klima or a fixed amount. The choice between percentage '
                                                'and fixed amount if determined by the toggle switch. Blue for '
                                                'percentage, '
                                                'white for fixed amount',
                                                target='dynamic_ptc_controls',
                                                placement='top',
                                            ),
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
                                                className="input_box_number", style={'color': 'white'}),
                                            dbc.Tooltip(
                                                'Input the desired sell intervals in days. i.e, if you would like '
                                                'to sell a certain amount of Klima every 30 days, then type 30 in this '
                                                'box.',
                                                target='sellDays',
                                                placement='top',
                                            ),
                                        ]),
                                    ], style={'padding-bottom': '10px', 'padding-top': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            html.Br(),
                                            dcc.Markdown('''
                                    ##### Dollar Cost Averaging Controls
                                    ___
                                    '''),
                                        ])
                                    ]),
                                    dbc.Row([
                                        dbc.Label('Klima Price ($)'),
                                        dbc.Input(
                                            id='klimaPrice_DCA',
                                            placeholder='50',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=50, className="input_box_number", style={'color': 'white'}),
                                        dbc.Tooltip(
                                            'Input the desired Klima price for your dollar cost averaging plans.'
                                            ' This should be a price where you will want to buy more Klima.',
                                            target='klimaPrice_DCA',
                                            placement='top',
                                        ),
                                    ], style={'padding': '10px', 'padding-bottom': '0px'}),
                                    dbc.Row([
                                        dbc.Label('Purchase Amount ($)'),
                                        dbc.Input(
                                            id='valBuy',
                                            placeholder='1000',
                                            type='number',
                                            min=1,
                                            step=0.001,
                                            debounce=True,
                                            value=10, className="input_box_number", style={'color': 'white'}),
                                        dbc.Tooltip(
                                            'Input the value you will like to purchase. I.e if you want to buy 500'
                                            ' USDC every time the price of Klima is around 1000 USDC, then input '
                                            '500 USDC here. ',
                                            target='valBuy',
                                            placement='top',
                                        ),
                                    ], style={'padding': '10px', 'padding-bottom': '0px'}),
                                    dbc.Row([
                                        dbc.Label('Cadence (Days)'),
                                        dbc.Input(
                                            id='buyDays',
                                            placeholder='30',
                                            type='number',
                                            min=1,
                                            value=30, className="input_box_number", style={'color': 'white'}),
                                        dbc.Tooltip(
                                            'Input your purchase intervals in days. I.e. If you speculate the price'
                                            ' of KLIMA will hover around 1000 USDC for the foreseeable future, and you'
                                            'want to dollar cost average every 30 days, then type 30 here.',
                                            target='buyDays',
                                            placement='top',
                                        ),

                                    ], style={'padding': '10px', 'padding-bottom': '0px'})
                                ])
                            ], outline=False, color='#2A2A2A', style={"height": "100%", "width": "auto"}),
                                style={'padding': '10px'},
                                xs=12, sm=12, md=12, lg=4, xl=4)]),
                        dbc.Row([
                            dbc.Col(
                                dbc.Card([
                                    dbc.CardHeader('Your current KLIMA to CO2 emissions equivalency',
                                                   className='learning_hub_category_deck_topic',
                                                   style={'color': '#FFFFFF',
                                                          'background-color': '#202020',
                                                          'font-weight': '500',
                                                          'font-size': '26px',
                                                          'font-style': 'normal'}
                                                   ),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon emissions from:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(className="emission_card_metric",
                                                                         id='current_passenger_vehicle_annual'),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Cars per year',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon emissions from:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(className="emission_card_metric",
                                                                         id='current_passenger_miles_annual'),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Miles per average vehicle',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon emissions from:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(className="emission_card_metric",
                                                                         id='current_gasoline_consumed_annual'),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Gallons of gasoline',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon sequestered by:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(id='current_trees_co_captured',
                                                                         className="emission_card_metric"),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Acres of trees',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                        ]),
                                    ])
                                ], outline=False, color='#202020', style={"height": "100%", "width": "100%"}),
                                xs=12, sm=12, md=12, lg=12, xl=12, style={'padding': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(
                                dbc.Card([
                                    dbc.CardHeader('Your future KLIMA to CO2 emissions equivalency',
                                                   className='learning_hub_category_deck_topic',
                                                   style={'color': '#FFFFFF',
                                                          'background-color': '#202020',
                                                          'font-weight': '500',
                                                          'font-size': '26px',
                                                          'font-style': 'normal'}
                                                   ),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon emissions from:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(className="emission_card_metric",
                                                                         id='passenger_vehicle_annual'),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Cars per year',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon emissions from:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(className="emission_card_metric",
                                                                         id='passenger_miles_annual'),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Miles per average vehicle',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon emissions from:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(className="emission_card_metric",
                                                                         id='gasoline_consumed_annual'),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Gallons of gasoline',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(dbc.Label('Carbon sequestered by:',
                                                                          className="learning_hub_category"
                                                                                    "_card_topic")),
                                                        dbc.Row([
                                                            dbc.Col([
                                                                html.Div(id='trees_co_captured',
                                                                         className="emission_card_metric"),
                                                            ]),
                                                        ]),
                                                        dbc.Row([
                                                            dbc.Label('Acres of trees',
                                                                      className="emission_card_topic")
                                                        ]),
                                                    ], className='simulator_hub_card')
                                                ], style={"height": "100%",
                                                          'width': '100%'})
                                            ], xs=12, sm=12, md=12, lg=3, xl=3, style={'padding': '10px'}),
                                        ]),
                                    ])
                                ], outline=False, color='#202020', style={"height": "100%", "width": "100%"}),
                                xs=12, sm=12, md=12, lg=12, xl=12, style={'padding': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardHeader('Klima growth simulation results: ROI',
                                                   className='learning_hub_category_deck_topic',
                                                   style={'color': '#FFFFFF',
                                                          'background-color': '#202020',
                                                          'font-weight': '500',
                                                          'font-size': '26px',
                                                          'font-style': 'normal'}
                                                   ),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row([
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Daily',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='dailyROI'),
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                            dbc.Col([
                                                                html.Div(className='vl')
                                                            ], xs=2, sm=2, md=2, lg=2, xl=2),
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Total',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='dailyKlima'),
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                        ]),
                                                    ]),
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=3, xl=3,
                                                style={'height': "100%",
                                                       'padding': '10px',
                                                       'justify-content': 'stretch'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row([
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('7 Day',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='sevendayROI')
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                            dbc.Col([
                                                                html.P(className='vl')
                                                            ], xs=2, sm=2, md=2, lg=2, xl=2),
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Total',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='sevendayKlima')
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                        ]),
                                                    ]),
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=3, xl=3,
                                                style={'height': "100%",
                                                       'padding': '10px',
                                                       'justify-content': 'stretch'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row([
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Monthly',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='monthlyROI')
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                            dbc.Col([
                                                                html.P(className='vl')
                                                            ], xs=2, sm=2, md=2, lg=2, xl=2),
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Total',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='monthlyKlima')
                                                                ])
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                        ]),
                                                    ])
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=3, xl=3,
                                                style={'height': "100%",
                                                       'padding': '10px',
                                                       'justify-content': 'stretch'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row([
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Annual',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='annualROI')
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                            dbc.Col([
                                                                html.P(className='vl')
                                                            ], xs=2, sm=2, md=2, lg=2, xl=2),
                                                            dbc.Col([
                                                                dbc.Row([
                                                                    dbc.Label('Total',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic'),
                                                                ]),
                                                                dbc.Row([
                                                                    html.Div(className='emission_card_metric',
                                                                             id='annualKlima')
                                                                ]),
                                                            ], xs=5, sm=5, md=5, lg=5, xl=5),
                                                        ]),
                                                    ])
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=3, xl=3,
                                                style={'height': "100%",
                                                       'padding': '10px',
                                                       'justify-content': 'stretch'}),
                                        ]),
                                    ]),
                                ], outline=False, color='#202020', style={"height": "100%", "width": "100%"})],
                                xs=12, sm=12, md=12, lg=12, xl=12, style={'padding': '10px'}),
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Label('Strategizer',
                                              className="learning_hub_category_topic"))
                        ]),
                        dbc.Row([
                            dbc.Col(
                                dbc.Card([
                                    dbc.CardHeader('Rewards strategy results',
                                                   className='learning_hub_category_deck_topic',
                                                   style={'color': '#FFFFFF',
                                                          'background-color': '#202020',
                                                          'font-weight': '500',
                                                          'font-size': '26px',
                                                          'font-style': 'normal'}
                                                   ),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Days until USDC Value',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            html.Div(className='emission_card_metric',
                                                                     id='rewardsUSD'),
                                                        ),
                                                    ], className='align-self-center'),
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=6, xl=6, style={'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Days until KLIMA amount',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            html.Div(className='emission_card_metric',
                                                                     id='rewardsKLIMA'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=6, xl=6, style={'padding': '10px'}),
                                        ]),
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Days to desired daily rewards',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            html.Div(className='emission_card_metric',
                                                                     id='rewardsDaily'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown('''
                                                     ---
                                                     ''')
                                                        ),
                                                        dbc.Row(
                                                            dbc.Label('Required KLIMA for desired daily rewards',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            html.Div(className='emission_card_metric',
                                                                     id='requiredDaily'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=6, xl=6,
                                                style={'height': "100%", 'padding': '10px'}),
                                            dbc.Col([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Days to desired weekly rewards',
                                                                      className='learning_hub_category_card_topic'
                                                                      ),
                                                        ),
                                                        dbc.Row(
                                                            html.Div(className='emission_card_metric',
                                                                     id='rewardsWeekly'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown('''
                                                     ---
                                                     ''')
                                                        ),
                                                        dbc.Row(
                                                            dbc.Label('Required KLIMA for desired weekly rewards',
                                                                      className='learning_hub_category_card_topic'
                                                                      ),
                                                        ),
                                                        dbc.Row(
                                                            html.Div(className='emission_card_metric',
                                                                     id='requiredWeekly'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card')
                                            ], xs=12, sm=12, md=12, lg=6, xl=6,
                                                style={'height': "100%", 'padding': '10px'})
                                        ]),
                                    ])
                                ], outline=False, color='#202020', style={"height": "100%", "width": "100%"})),
                            dbc.Col(
                                dbc.Card([
                                    dbc.CardHeader('Rewards strategizer controls',
                                                   className='learning_hub_category_deck_topic',
                                                   style={'color': '#FFFFFF',
                                                          'background-color': '#202020',
                                                          'font-weight': '500',
                                                          'font-size': '26px',
                                                          'font-style': 'normal'}
                                                   ),
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
                                                    className="input_box_number", style={'color': 'white'}),
                                                dbc.Tooltip(
                                                    'Input speculated price of Klima for rewards calculations',
                                                    target='priceKlima',
                                                    placement='top',
                                                ),
                                            ]),
                                            dbc.Col([
                                                dbc.Input(
                                                    id='priceofETH',
                                                    placeholder='10',
                                                    type='number',
                                                    min=1,
                                                    step=0.001,
                                                    debounce=True,
                                                    value=10,
                                                    className="input_box_number", style={'color': 'white'}),
                                                dbc.Tooltip(
                                                    'Input speculated price of Matic for gas fee consideration',
                                                    target='priceofETH',
                                                    placement='top',
                                                ),
                                            ])
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
                                                    value=10000, className="input_box_number",
                                                    style={'color': 'white'})]),
                                            dbc.Col([
                                                dbc.Input(
                                                    id='desired_klima_unit',
                                                    placeholder='500.0',
                                                    type='number',
                                                    min=1,
                                                    step=0.001,
                                                    debounce=True,
                                                    value=500, className="input_box_number",
                                                    style={'color': 'white'})])]),
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Label('Desired daily staking rewards (USDC)'),
                                            ]),
                                            dbc.Col([
                                                dbc.Label('Desired weekly staking rewards (USDC)'),
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
                                                    value=5000, className="input_box_number",
                                                    style={'color': 'white'})]),
                                            dbc.Col([
                                                dbc.Input(
                                                    id='desired_weekly_rewards_usdc',
                                                    placeholder='5000',
                                                    type='number',
                                                    min=1,
                                                    step=0.001,
                                                    debounce=True,
                                                    value=50000, className="input_box_number",
                                                    style={'color': 'white'})])], style={'padding': '0px'}),
                                    ])
                                ], outline=False, color='#202020', style={"height": "100%", "width": "100%"}),
                                xs=12, sm=12, md=12, lg=6, xl=6),
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Label('Results'))
                        ], className="learning_hub_category_topic"),
                        dbc.Row([
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('Expanded explanations', className='learning_hub_category_deck_topic',
                                               style={'color': '#FFFFFF',
                                                      'background-color': '#2A2A2A',
                                                      'font-weight': '500',
                                                      'font-size': '26px',
                                                      'font-style': 'normal'}
                                               ),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.CardGroup([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('KLIMA growth simulation results chart',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown(id='chart_results_explanation'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card'),
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('KLIMA to CO2 emissions equivalency',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown(id='equivalency_results_explanation'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card')
                                            ]),
                                        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'height': "100%",
                                                                                     'padding': '10px'}),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.CardGroup([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Staked KLIMA growth ROI',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown(id='forecast_roi_results_explanation'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card'),
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Staked KLIMA rewards strategizer',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown(id='strategizer_results_explanation'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='simulator_hub_card')
                                            ]),
                                        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'height': "100%",
                                                                                     'padding': '10px'}),
                                    ]),
                                ]),
                            ], outline=False, color='#2A2A2A', style={"height": "100%", "width": "100%"}),
                                xs=12, sm=12, md=12, lg=12, xl=12)
                        ], className="mb-5"),
                    ]),
        ], id='tabs', active_tab='staking_guide_tab', className='mb-2'),
        html.Footer(short_disclaimer_row(), className='footer_style', style={'background-color': '#202020'})
    ], className='center_2'),
], id='page_content', fluid=True)  # Responsive ui control


@app.callback(
    Output('dynamic_days_controls', 'children'),
    [Input('days_input_selector', 'value')])
def generate_control_days(switch):
    days_choice1 = dcc.Slider(
        id='growthDays',
        min=1,
        max=1000,
        value=365,
        tooltip={'placement': 'top', 'always_visible': True})
    days_choice2 = dbc.Input(
        id='growthDays',
        placeholder='500',
        type='number',
        min=1,
        step=1,
        debounce=True,
        value=365, className="input_box_number",
        style={'color': 'white'})
    if switch:
        return days_choice1
    else:
        return days_choice2


@app.callback(
    Output('dynamic_ptc_controls', 'children'),
    [Input('ptc_input_selector', 'value')])
def generate_control_ptc(switch):
    ptc_choice1 = dbc.Input(
        id='percentSale',
        placeholder='5',
        type='number',
        min=1,
        step=0.01,
        debounce=True,
        value=5,
        className='input_box_number', style={'color': 'white'}),
    ptc_choice2 = dbc.Input(
        id='percentSale',
        placeholder='1',
        type='number',
        min=1,
        step=0.01,
        debounce=True,
        value=5,
        className='input_box_number', style={'color': 'white'}),
    if switch:
        return ptc_choice1
    else:
        return ptc_choice2


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
    Output(component_id='current_passenger_vehicle_annual', component_property='children'),
    Output(component_id='current_passenger_miles_annual', component_property='children'),
    Output(component_id='current_gasoline_consumed_annual', component_property='children'),
    Output(component_id='current_trees_co_captured', component_property='children'),
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
    Output(component_id='chart_results_explanation', component_property='children'),
    Output(component_id='equivalency_results_explanation', component_property='children'),
    Output(component_id='forecast_roi_results_explanation', component_property='children'),
    Output(component_id='strategizer_results_explanation', component_property='children'),
    Input(component_id='growthDays', component_property='value'),
    Input(component_id='initialKlima', component_property='value'),
    Input(component_id='user_ary', component_property='value'),
    Input(component_id='min_ary', component_property='value'),
    Input(component_id='max_ary', component_property='value'),
    Input(component_id='user_rfv', component_property='value'),
    Input(component_id='percentSale', component_property='value'),
    Input(component_id='ptc_input_selector', component_property='value'),
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
                           user_ary, min_ary, max_ary, user_rfv,
                           percentSale, switch, sellDays, klimaPrice_DCA,
                           valBuy, buyDays,
                           priceKlima, priceofETH,
                           desired_klima_usdc, desired_klima_unit,
                           desired_daily_rewards_usdc,
                           desired_weekly_rewards_usdc):
    # ===========================Variable definitions and prep===============================
    # In this section we take the input variables and do any kind of prep work
    klimaGrowthEpochs = (growthDays * 3.3) + 1
    sellEpochs = sellDays * 3.3
    buyEpochs = buyDays * 3.3
    cadenceConst = sellEpochs
    cadenceConst_BUY = buyEpochs
    sellAmount = percentSale
    sellType = '%'
    dcaAmount = valBuy / klimaPrice_DCA
    user_ary = user_ary / 100
    minARY = min_ary / 100
    maxARY = max_ary / 100
    gwei = 1
    reward_yield = ((1 + user_ary) ** (1 / float(1197))) - 1
    reward_yield = round(reward_yield, 5)
    rebase_const = 1 + reward_yield
# 1200 1197.2 3.28
    # In this section, we calculate the staking and unstaking fees. Not required for klima
    staking_gas_fee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    staking_gas_fee_klimaAmount = staking_gas_fee / klimaPrice_DCA
    # unstaking_gas_fee = 89654 * ((gwei * priceofETH) / (10 ** 9))

    # In this section we calculate the reward yield from the users speculated ARY
    minOIPYield = ((1 + minARY) ** (1 / float(1197))) - 1
    maxOIPYield = ((1 + maxARY) ** (1 / float(1197))) - 1

    # In this case let's consider 1096 Epochs which is 365 days
    klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    klimaGrowth_df['Days'] = klimaGrowth_df.Epochs / 3.3  # There are 3 Epochs per day so divide by 3 to get Days

    profitAdjusted_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    profitAdjusted_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3.3

    dollarCostAVG_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    dollarCostAVG_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3.3
    # ===========================Variable definitions and prep===============================

    # ============================ USER ARY, DCA, PROFIT ADJUSTED PROJECTION =====
    # we loop through the exponential klima growth equation every epoch
    totalklimas = []  # create an empty array that will hold the componded rewards
    pA_totalklimas = []
    dcA_totalklimas = []

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
            if switch:
                percentSale = percentSale / 100
                sellType = '%'
                pA_klimaStakedGrowth = pA_totalklimas[-1] - (pA_totalklimas[-1] * percentSale)
            else:
                sellAmount = percentSale
                sellType = 'KLIMA'
                pA_klimaStakedGrowth = pA_totalklimas[-1] - percentSale
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
    # ============================ USER ARY, DCA, PROFIT ADJUSTED PROJECTION =====

    # ============================ MIN ARY PROJECTION ============================
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
    # ============================ MIN ARY PROJECTION ============================

    # ============================ MAX ARY PROJECTION ============================
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
    # ============================ MAX ARY PROJECTION ============================

    # Let's get some ROI Outputs starting with the daily
    dailyROI = (1 + reward_yield) ** 3.3 - 1  # Equation to calculate your daily ROI based on reward Yield
    dailyROI_P = round(dailyROI * 100, 1)  # daily ROI in Percentage
    dailyKlima = initialKlima + (dailyROI * initialKlima)
    dailyKlima_raw = '{}'.format(millify(dailyROI * initialKlima, precision=3))
    # ================================================================================

    # 5 day ROI
    # fivedayROI = (1 + reward_yield) ** (5 * 3) - 1  # Equation to calculate your 5 day ROI based on reward Yield
    # fivedayROI_P = round(fivedayROI * 100, 1)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    sevendayROI = (1 + reward_yield) ** (7 * 3.3) - 1  # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI_P = round(sevendayROI * 100, 1)  # 7 day ROI in Percentage
    sevendayKlima = initialKlima + (sevendayROI * initialKlima)
    sevendayKlima_raw = '{}'.format(millify(sevendayROI * initialKlima, precision=3))
    # ================================================================================

    # 30 day ROI
    monthlyROI = (1 + reward_yield) ** (30 * 3.3) - 1  # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI_P = round(monthlyROI * 100, 1)  # 30 day ROI in Percentage
    monthlyKlima = initialKlima + (monthlyROI * initialKlima)
    monthlyKlima_raw = '{}'.format(millify(monthlyROI * initialKlima, precision=3))
    # ================================================================================

    # Annual ROI
    annualROI = (1 + reward_yield) ** (365 * 3.3) - 1  # Equation to calculate your annual ROI based on reward Yield
    annualROI_P = round(annualROI * 100, 1)  # Equation to calculate your annual ROI based on reward Yield
    annualKlima = initialKlima + (annualROI * initialKlima)
    annualKlima_raw = '{}'.format(millify(annualROI * initialKlima, precision=3))
    # ================================================================================
    # ================================Real world impact calc =========================
    max_total_klimas = klimaGrowth_df.Total_klimas.max()
    locked_carbon_tonnes = annualKlima * user_rfv
    locked_carbon_tonnes_current = initialKlima * user_rfv
    locked_carbon_tonnes_var = max_total_klimas * user_rfv

    passenger_vehicle_annual = '{}'.format(millify((locked_carbon_tonnes / 4.60), precision=1))
    passenger_vehicle_current = '{}'.format(millify((locked_carbon_tonnes_current / 4.6), precision=1))
    passenger_vehicle_var = '{}'.format(millify((locked_carbon_tonnes_var / 4.6), precision=1))

    passenger_miles_annual = '{}'.format(millify((locked_carbon_tonnes / 0.000398), precision=1))
    passenger_miles_current = '{}'.format(millify((locked_carbon_tonnes_current / 0.000398), precision=1))
    passenger_miles_var = '{}'.format(millify((locked_carbon_tonnes_var / 0.000398), precision=1))

    gasoline_consumed_annual = '{}'.format(millify((locked_carbon_tonnes / 0.008887), precision=1))
    gasoline_consumed_current = '{}'.format(millify((locked_carbon_tonnes_current / 0.008887), precision=1))
    gasoline_consumed_var = '{}'.format(millify((locked_carbon_tonnes_var / 0.008887), precision=1))

    trees_co_captured = '{}'.format(millify((locked_carbon_tonnes / 0.82), precision=1))
    trees_co_captured_current = '{}'.format(millify((locked_carbon_tonnes_current / 0.82), precision=1))
    trees_co_captured_var = '{}'.format(millify((locked_carbon_tonnes_var / 0.82), precision=1))
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
    # klimaGrowth_Chart.update_layout(hovermode='x unified', hoverlabel_bgcolor='#232b2b', hoverlabel_align='auto',
    #                                hoverlabel_namelength=-1, hoverlabel_font_size=15)
    klimaGrowth_Chart.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white', showgrid=False,
                                   gridwidth=0.01, mirror=True, showspikes=True, spikesnap='cursor',
                                   spikemode='across', spikethickness=0.5)
    klimaGrowth_Chart.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white', showgrid=False,
                                   gridwidth=0.01, mirror=True, showspikes=True, spikethickness=0.5, zeroline=False)
    klimaGrowth_Chart.update_layout(spikedistance=1000, hoverdistance=100)
    klimaGrowth_Chart.layout.legend.font.color = 'white'

    dailyROI_P = '{0:.1f}%'.format(dailyROI_P)
    dailyKlima = '{0:.2f}'.format(dailyKlima)
    sevendayROI_P = '{0:.0f}%'.format(sevendayROI_P)
    sevendayKlima = '{0:.2f}'.format(sevendayKlima)
    monthlyROI_P = '{0:.0f}%'.format(monthlyROI_P)
    monthlyKlima = '{0:.2f}'.format(monthlyKlima)
    annualROI_P = '{}%'.format(millify(annualROI_P, precision=1))
    annualKlima = '{0:.1f}'.format(annualKlima)

    chart_results_explanation = f'''
    - The chart shows your speculated Klima growth projection over **{growthDays} days**. The
    Projection is calculated based on your selected ARY of **{user_ary * 100} %**
    which is equivalent to a reward yield of **{reward_yield * 100} %**, and an initial **{initialKlima} KLIMA**

    - The (3,3) Profit adjusted ROI trend line shows you the adjusted KLIMA growth if you decide to
    sell {sellAmount}{sellType} every **{sellDays} days**

    - The (3,3) Dollar cost averaging (DCA) adjusted ROI trend line shows you the adjusted KLIMA growth if you decide
    to buy **{valBuy}** worth of KLIMA every **{buyDays}** days at a unit price of $ **{priceKlima}**

    - The Min Growth Rate shows you the estimated KLIMA growth rate if the ARY
    was on the minimum ARY of the current dictated KIP-3 Reward Rate Framework

    - The Max Growth Rate shows you the estimated Klima growth rate if the ARY
    was on the maximum ARY of the current dictated KIP-3 Reward Rate Framework
    '''

    equivalency_results_explanation = f'''
    Using the speculated KLIMA reward yield of **{reward_yield * 100} %** and speculated {RFV_TERM} of
    **{user_rfv} {RFV_TERM}** at the end of your time frame, we can estimate that your earned KLIMA total will be
    equivalent to the following:

    - Carbon emissions from **{passenger_vehicle_annual}** cars in a year

    - Carbon emissions generated from the average passenger vehicle driving **{passenger_miles_annual}** miles

    - Carbon emissions generated from **{gasoline_consumed_annual}** gallons of gasoline

    - Carbon captured by **{trees_co_captured}** acres of U.S. forest in one year
    '''

    forecast_roi_results_explanation = f'''
    Using the speculated KLIMA reward yield of **{user_ary * 100} %** and initial **{initialKlima} KLIMA**,
    we can speculate the following returns:

    - Daily ROI based on your input ARY of **{user_ary * 100} %** : **{dailyROI_P}**
    which is about **{dailyKlima_raw}** KLIMA per day, totalling **{dailyKlima}** KLIMA after one day

    - Seven day ROI based on your input ARY of **{user_ary * 100} %** : **{sevendayROI_P}** which is
    about **{sevendayKlima_raw}** KLIMA per week, totaling **{sevendayKlima}** KLIMA after one week

    - One month ROI based on your input ARY of **{user_ary * 100} %** : **{monthlyROI_P}** which is about
    **{monthlyKlima_raw}** KLIMA per month

    - One year ROI based on your input ARY of **{user_ary * 100} %** : **{annualROI_P}** which is
    about **{annualKlima_raw}** KLIMA per year
    '''

    strategizer_results = f'''
    Based on your control parameters, these are the predicted outcomes assuming market stability and your parameters
    hold true.

    - It would take {forcastUSDTarget} days until you accumulate enough KLIMA worth ${desired_klima_usdc}.
    Keep in mind that you are also predicting that the price of KLIMA will be ${priceKlima} on this day.

    - It would take {forcastKlimaTarget} days until you accumulate {desired_klima_unit} KLIMA.
    Keep in mind that this prediction is calculated based on your selected ARY% of {user_ary * 100} %
    and an initial {initialKlima} KLIMA staked. Use the KIP-3 Framework to adjust your ARY % parameter.

    - To start earning daily rewards of $ {desired_daily_rewards_usdc},
    you will need {requiredKlimaDailyIncooom} KLIMA, and based on the ARY% you entered,
    it would take {forcastDailyIncooom} days to reach your goal.
    Remember that this prediction relies on your selected ARY% of
    {user_ary * 100} %, initial {initialKlima} KLIMA staked, and predicated price of $ {priceKlima}/KLIMA

    - To start earning weekly reward of $ {desired_weekly_rewards_usdc},
    you will need {requiredKlimaWeeklyIncooom} KLIMA, and based on the ARY% you entered,
    it would take {forcastWeeklyIncooom} days to reach your goal.
    Remember that this prediction relies on your selected ARY% of
    {user_ary * 100} %, initial {initialKlima} KLIMA staked, and predicated price of $ {priceKlima}/KLIMA
    '''

    return klimaGrowth_Chart, dailyROI_P, dailyKlima, sevendayROI_P, sevendayKlima, monthlyROI_P, \
           monthlyKlima, annualROI_P, annualKlima, passenger_vehicle_current, \
           passenger_miles_current, gasoline_consumed_current,\
           trees_co_captured_current, passenger_vehicle_var, passenger_miles_var,\
           gasoline_consumed_var, trees_co_captured_var, forcastUSDTarget, \
           forcastKlimaTarget, rewardsDaily, requiredKlimaDailyIncooom, forcastWeeklyIncooom, \
           requiredKlimaWeeklyIncooom, chart_results_explanation, equivalency_results_explanation, \
           forecast_roi_results_explanation, strategizer_results  # noqa: E127


@app.callback(
    Output('what_is_staking_modal_body', 'is_open'),
    [
        Input('what_is_staking_btn_open', 'n_clicks'),
        Input('what_is_staking_btn_close', 'n_clicks')
    ],
    [State('what_is_staking_modal_body', 'is_open')],
)
def staking_guide0(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('why_should_i_stake_modal_body', 'is_open'),
    [
        Input('why_should_i_stake_btn_open', 'n_clicks'),
        Input('why_should_i_stake_btn_close', 'n_clicks')
    ],
    [State('why_should_i_stake_modal_body', 'is_open')],
)
def staking_guide1(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('how_can_i_stake_modal_body', 'is_open'),
    [
        Input('how_can_i_stake_btn_open', 'n_clicks'),
        Input('how_can_i_stake_btn_close', 'n_clicks')
    ],
    [State('how_can_i_stake_modal_body', 'is_open')],
)
def staking_guide2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('staking_dynamics_modal_body', 'is_open'),
    [
        Input('staking_dynamics_btn_open', 'n_clicks'),
        Input('staking_dynamics_btn_close', 'n_clicks')
    ],
    [State('staking_dynamics_modal_body', 'is_open')],
)
def staking_guide3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('how_to_read_growth_chart_modal_body', 'is_open'),
    [
        Input('how_to_read_growth_chart_btn_open', 'n_clicks'),
        Input('how_to_read_growth_chart_btn_close', 'n_clicks')
    ],
    [State('how_to_read_growth_chart_modal_body', 'is_open')],
)
def staking_guide4(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('how_to_use_sim_controls_modal_body', 'is_open'),
    [
        Input('how_to_use_sim_controls_btn_open', 'n_clicks'),
        Input('how_to_use_sim_controls_btn_close', 'n_clicks')
    ],
    [State('how_to_use_sim_controls_modal_body', 'is_open')],
)
def staking_guide5(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('how_to_read_co_metrics_modal_body', 'is_open'),
    [
        Input('how_to_read_co_metrics_btn_open', 'n_clicks'),
        Input('how_to_read_co_metrics_btn_close', 'n_clicks')
    ],
    [State('how_to_read_co_metrics_modal_body', 'is_open')],
)
def staking_guide6(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('how_to_use_strategizer_modal_body', 'is_open'),
    [
        Input('how_to_use_strategizer_btn_open', 'n_clicks'),
        Input('how_to_use_strategizer_btn_close', 'n_clicks')
    ],
    [State('how_to_use_strategizer_modal_body', 'is_open')],
)
def staking_guide7(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
