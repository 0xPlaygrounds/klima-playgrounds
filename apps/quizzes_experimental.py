from dash import dcc
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import State, html
from app import app
from dash.dependencies import Input, Output
from millify import millify

from subgrounds.dash_wrappers import Graph
from subgrounds.plotly_wrappers import Figure, Scatter

from klima_subgrounds import sg, protocol_metrics_1year, last_metric, immediate

# Lotties: Emil at https://github.com/thedirtyfew/dash-extensions
url_sunlight = "https://assets8.lottiefiles.com/packages/lf20_bknKi1.json"
url_earth = "https://assets10.lottiefiles.com/datafiles/xjh641xEDuQg4qg/data.json"
url5 = "https://assets8.lottiefiles.com/packages/lf20_q6y5ptrh.json"
url6 = "https://assets4.lottiefiles.com/packages/lf20_tN5Ofx.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Label('Analytics',
                          className="page_section_topic"))
    ]),
    dbc.Row([
        dbc.Col([dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Backing Assets in Treasury (Carbon Base)'),
                    ]),
                ]),
            ], style={'color': '#FFFFFF',
                      'background-color': '#2A2A2A',
                      'font-weight': '500',
                      'font-size': '26px',
                      'font-style': 'normal'}),
            dbc.CardBody([
                Graph(Figure(
                    subgrounds=sg,
                    traces=[
                        # Risk-free value treasury assets
                        Scatter(
                            name='Total Reserves',
                            x=protocol_metrics_1year.datetime,
                            y=protocol_metrics_1year.treasuryRiskFreeValue,
                            mode='lines',
                            line={'width': 0.5, 'color': 'rgb(0, 128, 255)'},
                            stackgroup='one',
                        ),
                    ],
                    layout={
                        'showlegend': True,
                        'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                        'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                  'title': 'Total Reserves'},
                        'legend.font.color': 'white',
                        'paper_bgcolor': 'rgba(0,0,0,0)',
                        'plot_bgcolor': 'rgba(0,0,0,0)',
                    }
                ))
            ]),
        ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=9, xl=9),
        dbc.Col([dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Backing Assets in Treasury (Carbon Base)', className="analytics_card_topic"),
                    ]),
                ], style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        millify(
                            immediate(sg, last_metric.treasuryRiskFreeValue),
                            precision=2)
                    ])
                ], className="analytics_card_metric", style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Label('Total Carbon in Treasury (Carbon Tonnes)', className="analytics_card_topic"),
                ], style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        millify(
                            immediate(sg, last_metric.treasuryCarbon),
                            precision=2)
                    ]),
                ], className="analytics_card_metric", style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Total Treasury Market Value (USD)', className="analytics_card_topic"),
                    ]),
                ], style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        millify(
                            immediate(sg, last_metric.treasuryMarketValue),
                            precision=2)
                    ]),
                ], className="analytics_card_metric", style={'text-align': 'center'}),
            ], style={'text-align': 'center'}),
        ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=3, xl=3),
    ], style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Market Cap (USD)', className="analytics_card_topic"),
                    ]),
                ], style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        millify(
                            immediate(sg, last_metric.marketCap),
                            precision=2)
                    ]),
                ], className="analytics_card_metric", style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        dbc.Label('KLIMA Price (USD)', className="analytics_card_topic"),
                    ]),
                ], style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        millify(
                            immediate(sg, last_metric.klimaPrice),
                            precision=2)
                    ]),
                ], className="analytics_card_metric", style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Current APY (%)', className="analytics_card_topic"),
                    ]),
                ], style={'text-align': 'center'}),
                dbc.Row([
                    dbc.Col([
                        millify(
                            immediate(sg, last_metric.currentAPY),
                            precision=2)
                    ]),
                ], className="analytics_card_metric", style={'text-align': 'center'})
            ]),
        ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=3, xl=3),
        dbc.Col([dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Market Value Of Treasury Assets (USD)'),
                    ]),
                ]),
            ], style={'color': '#FFFFFF',
                      'background-color': '#2A2A2A',
                      'font-weight': '500',
                      'font-size': '24px',
                      'font-style': 'normal'}),
            dbc.CardBody([
                Graph(Figure(
                    subgrounds=sg,
                    traces=[
                        # Market value treasury assets
                        Scatter(
                            name='Total_mv',
                            x=protocol_metrics_1year.datetime,
                            y=protocol_metrics_1year.treasuryMarketValue,
                            mode='lines',
                            line={'width': 0.5, 'color': 'rgb(255, 0, 255)'},
                            stackgroup='one',
                        ),
                    ],
                    layout={
                        'showlegend': True,
                        'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                        'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                  'title': 'MV of Treasury Assets'},
                        'legend.font.color': 'white',
                        'paper_bgcolor': 'rgba(0,0,0,0)',
                        'plot_bgcolor': 'rgba(0,0,0,0)',
                    }
                ))
            ]),
        ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=9, xl=9),
    ], style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Treasury Total Carbon'),
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            Scatter(
                                name='Treasury Total Carbon',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.treasuryCarbon,
                                line={'width': 0.5, 'color': 'rgb(255, 128, 64)'},
                                stackgroup='one',
                            ),
                        ],
                        layout={
                            'showlegend': True,
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'Treasury Total Carbon'},
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True)
        ], xs=12, sm=12, md=12, lg=6, xl=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Treasury Market Value per KLIMA vs KLIMA Price'),
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            Scatter(
                                name='Treasury Market Value per KLIMA',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.tmv_per_klima,
                                line={'width': 0.5, 'color': 'rgb(255, 0, 255)'},
                                stackgroup='one',
                            ),
                            Scatter(
                                name='KLIMA Price',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.klimaPrice,
                                line={'width': 0.5, 'color': 'rgb(2, 193, 50)'},
                                stackgroup='one',
                            ),
                        ],
                        layout={
                            'showlegend': True,
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'Treasury Market Value per KLIMA vs KLIMA Price'},
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=6, xl=6),
    ], style={'padding': '10px'}),
    dbc.Row([
            dbc.Col([dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Staked KLIMA (%): '),
                        ]),
                        dbc.Col([
                            millify(
                                immediate(sg, last_metric.sKlimaCirculatingSupply),
                                precision=2)
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            # Risk-free value treasury assets
                            Scatter(
                                name='Staked_supply_percent',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.staked_supply_percent,
                                mode='lines',
                                line={'width': 0.5, 'color': 'rgb(0, 128, 255)'},
                                stackgroup='one',
                            ),
                            Scatter(
                                name='Unstaked_supply_percent',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.unstaked_supply_percent,
                                mode='lines',
                                line={'width': 0.5, 'color': 'rgb(255, 0, 0)'},
                                stackgroup='one',
                            )
                        ],
                        layout={
                            'showlegend': True,
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'Staked KLIMA(%)'},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('RFV/KLIMA vs KLIMA Price'),
                            ]),
                        ]),
                    ], style={'color': '#FFFFFF',
                              'background-color': '#2A2A2A',
                              'font-weight': '500',
                              'font-size': '24px',
                              'font-style': 'normal'}),
                    dbc.CardBody([
                        Graph(Figure(
                            subgrounds=sg,
                            traces=[
                                Scatter(
                                    name='Risk-Free Value per KLIMA',
                                    x=protocol_metrics_1year.datetime,
                                    y=protocol_metrics_1year.rfv_per_klima,
                                    line={'width': 0.5, 'color': 'blue'},
                                    stackgroup='one',
                                ),
                                Scatter(
                                    name='KLIMA Price',
                                    x=protocol_metrics_1year.datetime,
                                    y=protocol_metrics_1year.klimaPrice,
                                    line={'width': 0.5, 'color': 'rgb(2, 193, 50)'},
                                    stackgroup='one',
                                ),
                            ],
                            layout={
                                'showlegend': True,
                                'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'title': 'RFV/KLIMA and KLIMA Price'},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                            }
                        ))
                    ]),
                ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
    ], style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('KLIMA Price / RFV per KLIMA (%)'),
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            Scatter(
                                name='KLIMA Price / Risk-Free Value per KLIMA (%)',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.price_rfv_ratio,
                                line={'width': 0.5, 'color': 'rgb(0, 128, 255)'},
                                stackgroup='one',
                            ),
                        ],
                        layout={
                            'showlegend': True,
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'KLIMA Price / RFV per KLIMA (%)'},
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=6, xl=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('KLIMA Price Over Time'),
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            Scatter(
                                name='KLIMA Price',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.klimaPrice,
                                line={'width': 0.5, 'color': 'rgb(2, 193, 50)'},
                                stackgroup='one',
                            ),
                        ],
                        layout={
                            'showlegend': True,
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'KLIMA Price'},
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
        ], xs=12, sm=12, md=12, lg=6, xl=6),
    ], style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Current Runway'),
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            Scatter(
                                name='Current Runway',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.runwayCurrent,
                                line={'width': 0.5, 'color': 'rgb(0, 128, 255)'},
                                stackgroup='one',
                            ),
                        ],
                        layout={
                            'showlegend': True,
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'Current Runway'},
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True)
        ], xs=12, sm=12, md=12, lg=6, xl=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Market Cap'),
                        ]),
                    ]),
                ], style={'color': '#FFFFFF',
                          'background-color': '#2A2A2A',
                          'font-weight': '500',
                          'font-size': '24px',
                          'font-style': 'normal'}),
                dbc.CardBody([
                    Graph(Figure(
                        subgrounds=sg,
                        traces=[
                            Scatter(
                                name='Market Cap',
                                x=protocol_metrics_1year.datetime,
                                y=protocol_metrics_1year.marketCap,
                                line={'width': 0.5, 'color': 'rgb(255, 0, 255)'},
                                stackgroup='one',
                            ),
                        ],
                        layout={
                            'showlegend': True,
                            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                      'title': 'Market Cap'},
                            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True)
        ], xs=12, sm=12, md=12, lg=6, xl=6)
    ], style={'padding': '10px'})
])
