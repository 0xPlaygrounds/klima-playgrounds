import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import html
from subgrounds.dash_wrappers import Graph
from subgrounds.plotly_wrappers import Figure, Scatter
from millify import millify

from ..klima_subgrounds import sg, protocol_metrics_1year, immediate, last_metric

# Lotties: Emil at https://github.com/thedirtyfew/dash-extensions
url_sunlight = "https://assets8.lottiefiles.com/packages/lf20_bknKi1.json"
url_earth = "https://assets10.lottiefiles.com/datafiles/xjh641xEDuQg4qg/data.json"
url5 = "https://assets8.lottiefiles.com/packages/lf20_q6y5ptrh.json"
url6 = "https://assets4.lottiefiles.com/packages/lf20_tN5Ofx.json"
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
                        html.H2('Market Cap', className='analytics_card_metric'),
                        html.H4('$' +
                                millify(
                                    immediate(sg, last_metric.marketCap),
                                    precision=2),
                                style={'text-align': 'center'}
                                ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('Price', className='analytics_card_metric'),
                        html.H4('$' +
                                millify(
                                    immediate(sg, last_metric.klimaPrice),
                                    precision=2),
                                style={'text-align': 'center'}
                                ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('Klimates', className='analytics_card_metric'),
                        html.H4(
                                millify(
                                    immediate(sg, last_metric.holders),
                                    precision=2),
                                style={'text-align': 'center'}
                                ),
                    ]),
                ], className='simulator_hub_card',
                    style={'height': '100%', 'width': '100%'}, inverse=True),
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('Runway', className='analytics_card_metric'),
                        html.H4(
                            millify(
                                immediate(sg, last_metric.runwayCurrent),
                                precision=2) + ' days',
                            style={'text-align': 'center'}
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
                                          'title': 'Market Cap', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                                'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
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
                                'showlegend': False,
                                'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'title': 'KLIMA Price', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                            }
                        ), style={'width': '100%'})
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
                                          'title': 'Current Runway', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                                'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
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
                                dbc.Label('Current APY%'),
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
                                    name='Current APY%',
                                    x=protocol_metrics_1year.datetime,
                                    y=protocol_metrics_1year.currentAPY,
                                    line={'width': 0.5, 'color': 'rgb(0, 128, 255)'},
                                    stackgroup='one',
                                ),
                            ],
                            layout={
                                'showlegend': True,
                                'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'title': 'Current APY', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                                'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                            }
                        ))
                    ]),
                ], style={'height': '100%'}, color='#2A2A2A', inverse=True)
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
                                          'title': 'Treasury Total Carbon', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                                'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                            }
                        ))
                    ]),
                ], style={'height': '100%'}, color='#2A2A2A', inverse=True)
            ], xs=12, sm=12, md=12, lg=6, xl=6),
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
                                      'title': 'MV of Treasury Assets', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                            'autosize': True,
                            'margin': dict(l=20, r=30, t=10, b=20),
                            'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
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
                                      'title': 'Total Reserves', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                            'autosize': True,
                            'margin': dict(l=20, r=30, t=10, b=20),
                            'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
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
                                dbc.Label('TMV/KLIMA vs KLIMA Price'),
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
                                    name='TMV/KLIMA',
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
                                          'title': 'Treasury Market Value per KLIMA vs KLIMA Price', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                                'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                            }
                        ))
                    ]),
                ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
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
                                          'title': 'RFV/KLIMA and KLIMA Price', 'showgrid': False},
                                'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                                          'showgrid': False},
                                'legend.font.color': 'white',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                'autosize': True,
                                'margin': dict(l=20, r=30, t=10, b=20),
                                'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                            }
                        ))
                    ]),
                ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Staked KLIMA (%): '),
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
                                      'title': 'Staked KLIMA(%)', 'showgrid': False},
                            'legend.font.color': 'white',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                            'autosize': True,
                            'margin': dict(l=20, r=30, t=10, b=20),
                            'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                        }
                    ))
                ]),
            ], style={'height': '100%'}, color='#2A2A2A', inverse=True),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
    ], className='center_2'),
], id='page_content_analytics', fluid=True)
