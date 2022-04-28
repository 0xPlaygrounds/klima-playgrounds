import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import State
from dash.dependencies import Input, Output
from dash import html
from millify import millify
from ..app import app
from ..klima_subgrounds import sg, immediate, last_metric
from .data_plots import mkt_cap_plot, klimaPrice, current_runway, current_AKR, treasury_total_carbon, tmv, \
    tCC, tmv_per_klima, cc_per_klima, staked_percent

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col(dbc.Label(
                'Analytics: General',
                className="page_section_topic"
            ))
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('Mkt Cap', className='analytics_card_topic'),
                        html.H4('$' +
                                millify(
                                    immediate(sg, last_metric.marketCap),
                                    precision=2),
                                style={'text-align': 'center'},
                                className='analytics_card_metric'
                                ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('Price', className='analytics_card_topic'),
                        html.H4('$' +
                                millify(
                                    immediate(sg, last_metric.klimaPrice),
                                    precision=2),
                                style={'text-align': 'center'},
                                className='analytics_card_metric'
                                ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('TVD', className='analytics_card_topic'),
                        html.H4('$' +
                                millify(
                                    immediate(sg, last_metric.totalValueLocked),
                                    precision=2),
                                style={'text-align': 'center'}, className='analytics_card_metric'
                                ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('Runway', className='analytics_card_topic'),
                        html.H4(
                            millify(
                                immediate(sg, last_metric.runwayCurrent),
                                precision=2) + ' days',
                            style={'text-align': 'center'}, className='analytics_card_metric'
                        ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('Market Cap',
                                           id='market_cap_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([mkt_cap_plot], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('Market Cap')),
                        dbc.ModalBody(mkt_cap_plot),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True)
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('KLIMA Price Over Time',
                                           id='klimaPrice_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([klimaPrice], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('Klima Price', className='analytics_card_topic')),
                        dbc.ModalBody(klimaPrice),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="klimaPrice_close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='klimaPrice_modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('Current Runway',
                                           id='current_runway_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([current_runway], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('Current Runway', className='analytics_card_topic')),
                        dbc.ModalBody(current_runway),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="current_runway_close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='current_runway_modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True)
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('Current AKR%',
                                           id='current_AKR_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([current_AKR], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('Current AKR', className='analytics_card_topic')),
                        dbc.ModalBody(current_AKR),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="current_AKR_close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='current_AKR_modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True)
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
        dbc.Row([
            dbc.Col(dbc.Label(
                'Analytics: Treasury',
                className="page_section_topic"
            ))
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('Treasury Total Carbon',
                                           id='treasury_total_carbon_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([treasury_total_carbon], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('Treasury Total Carbon', className='analytics_card_topic')),
                        dbc.ModalBody(treasury_total_carbon),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="treasury_total_carbon_close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='treasury_total_carbon_modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True)
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('Mkt Value of Treasury Assets (USD)',
                                       id='tmv_btn',
                                       className='analytics_card_topic',
                                       color='link',
                                       n_clicks=0,
                                       style={'color': '#FFFFFF',
                                              'background-color': '#2A2A2A',
                                              'font-weight': '500',
                                              'font-size': '24px',
                                              'font-style': 'normal'})
                        ]),
                    ]),
                ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                dbc.CardBody([tmv], style={'font-size': '20px', 'border-radius': '20px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Mkt Value of Treasury Assets', className='analytics_card_topic')),
                    dbc.ModalBody(tmv),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="tmv_close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                    id='tmv_modal',
                    is_open=False,
                    size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                )
            ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
        dbc.Row([
            dbc.Col([dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('Backing Asstes in Treasury (Carbon Base)',
                                       id='tCC_btn',
                                       className='analytics_card_topic',
                                       color='link',
                                       n_clicks=0,
                                       style={'color': '#FFFFFF',
                                              'background-color': '#2A2A2A',
                                              'font-weight': '500',
                                              'font-size': '26px',
                                              'font-style': 'normal'})
                        ]),
                    ]),
                ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                dbc.CardBody([tCC], style={'font-size': '20px', 'border-radius': '20px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Backing Asstes in Treasury (Carbon Base)',
                                                   className='analytics_card_topic')),
                    dbc.ModalBody(tCC),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="tCC_close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                    id='tCC_modal',
                    is_open=False,
                    size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                )
            ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('TMV/KLIMA vs KLIMA Price',
                                           id='tmv_per_klima_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([tmv_per_klima], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('TMV/KLIMA vs KLIMA Price', className='analytics_card_topic')),
                        dbc.ModalBody(tmv_per_klima),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="tmv_per_klima_close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='tmv_per_klima_modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
        dbc.Row([
            dbc.Col(dbc.Label(
                'Analytics: Insight',
                className="page_section_topic"
            ))
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('CC/KLIMA vs KLIMA Price',
                                           id='cc_per_klima_btn',
                                           className='analytics_card_topic',
                                           color='link',
                                           n_clicks=0,
                                           style={'color': '#FFFFFF',
                                                  'background-color': '#2A2A2A',
                                                  'font-weight': '500',
                                                  'font-size': '24px',
                                                  'font-style': 'normal'})
                            ]),
                        ]),
                    ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                    dbc.CardBody([cc_per_klima], style={'font-size': '20px', 'border-radius': '20px'}),
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle('CC/Klima', className='analytics_card_topic')),
                        dbc.ModalBody(cc_per_klima),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close", id="cc_per_klima_close", className="ms-auto", n_clicks=0
                            )
                        ),
                    ],
                        id='cc_per_klima_modal',
                        is_open=False,
                        size="xl", style={'font-size': '20px', 'border-radius': '20px'}
                    )
                ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('Staked KLIMA (%): ',
                                       id='staked_percent_btn',
                                       className='analytics_card_topic',
                                       color='link',
                                       n_clicks=0,
                                       style={'color': '#FFFFFF',
                                              'background-color': '#2A2A2A',
                                              'font-weight': '500',
                                              'font-size': '24px',
                                              'font-style': 'normal'})
                        ]),
                    ]),
                ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
                dbc.CardBody([staked_percent], style={'font-size': '20px', 'border-radius': '20px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Staked vs Unstaked Klima'), className='analytics_card_topic'),
                    dbc.ModalBody(staked_percent),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="staked_percent_close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                    id='staked_percent_modal',
                    is_open=False,
                    size="xl", style={'font-size': '20px', 'border-radius': '20px'}, className='analytics_card_topic'
                )
            ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
    ], className='center_2'),
], id='page_content_analytics', fluid=True)


def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


app.callback(
    Output("modal", "is_open"),
    [Input("market_cap_btn", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("klimaPrice_modal", "is_open"),
    [Input("klimaPrice_btn", "n_clicks"), Input("klimaPrice_close", "n_clicks")],
    [State("klimaPrice_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("current_runway_modal", "is_open"),
    [Input("current_runway_btn", "n_clicks"), Input("current_runway_close", "n_clicks")],
    [State("current_runway_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("current_AKR_modal", "is_open"),
    [Input("current_AKR_btn", "n_clicks"), Input("current_AKR_close", "n_clicks")],
    [State("current_AKR_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("treasury_total_carbon_modal", "is_open"),
    [Input("treasury_total_carbon_btn", "n_clicks"), Input("treasury_total_carbon_close", "n_clicks")],
    [State("treasury_total_carbon_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("tmv_modal", "is_open"),
    [Input("tmv_btn", "n_clicks"), Input("tmv_close", "n_clicks")],
    [State("tmv_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("tCC_modal", "is_open"),
    [Input("tCC_btn", "n_clicks"), Input("tCC_close", "n_clicks")],
    [State("tCC_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("tmv_per_klima_modal", "is_open"),
    [Input("tmv_per_klima_btn", "n_clicks"), Input("tmv_per_klima_close", "n_clicks")],
    [State("tmv_per_klima_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("cc_per_klima_modal", "is_open"),
    [Input("cc_per_klima_btn", "n_clicks"), Input("cc_per_klima_close", "n_clicks")],
    [State("cc_per_klima_modal", "is_open")],
)(toggle_modal)

app.callback(
    Output("staked_percent_modal", "is_open"),
    [Input("staked_percent_btn", "n_clicks"), Input("staked_percent_close", "n_clicks")],
    [State("staked_percent_modal", "is_open")],
)(toggle_modal)
