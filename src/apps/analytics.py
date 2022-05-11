import pandas as pd
from typing import Callable
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc
from dash import State
# from dash.dependencies import Input, Output
from dash_extensions.enrich import DashBlueprint, ServersideOutput, Output, Input, Trigger, html
# from dash import html
from millify import millify
from subgrounds.subgraph import FieldPath
from ..app import app
from ..klima_subgrounds import sg, last_metric
from .data import mkt_cap_plot, klima_price, current_runway, current_AKR, time_cache, treasury_total_carbon, tmv, \
    tCC, tmv_per_klima, cc_per_klima, staked_percent

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

def identity(x):
    return x

def analytics_card_metric(
    label: str,
    id: str,
    value: FieldPath,
    format_data: Callable[[float | int], str] = identity
) -> DashBlueprint:
    bp = DashBlueprint()
    bp.layout = dbc.Card([
        html.Div(id=f'{id}_onload'),
        dcc.Store(id=f'{id}_store'),
        dbc.CardBody([
            html.H2(label, className='analytics_card_topic'),
            html.H4(
                style={'text-align': 'center'},
                className='analytics_card_metric',
                id=id
            ),
        ])
    ], className='simulator_hub_card', style={'height': '100%', 'width': '100%'}, inverse=True)

    @bp.callback(ServersideOutput(f'{id}_store', "data"), Trigger(f'{id}_onload', "children"))
    @time_cache(seconds=60)
    def query_data():
        print(f'Querying metric {label}')
        return sg.query([value])
    
    @bp.callback(Output(id, 'children'), Input(f'{id}_store', "data"))
    def display_data(data):
        return format_data(data)

    bp.register_callbacks(app)

    return bp.layout

def fmt_dollar_value(value):
    return '$' + millify(value, precision=2)

def fmt_days_value(value):
    return millify(value, precision=2) + ' days'

def data_plot(
    label: str,
    id: str,
    mk_figure: Callable[[], go.Figure]
) -> DashBlueprint:
    placeholder_figure = go.Figure(layout={
        'showlegend': True,
        'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False, 'mirror': True,
                'showspikes': True, 'spikesnap': 'cursor',
                'spikemode': 'across', 'spikethickness': 0.5},
        'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                'title': 'Staked KLIMA(%)', 'showgrid': False, 'mirror': True,
                'showspikes': True, 'spikesnap': 'cursor',
                'spikemode': 'across', 'spikethickness': 0.5},
        'legend.font.color': 'white',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'autosize': True,
        'margin': dict(l=20, r=30, t=10, b=20),
        'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        'modebar_add': ['drawline',
                        'drawopenpath',
                        'drawclosedpath',
                        'drawcircle',
                        'drawrect',
                        'eraseshape'
                        ],
    })

    bp = DashBlueprint()
    bp.layout = dbc.Card([
        html.Div(id=f'{id}_onload'),
        dcc.Store(id=f'{id}_store'),
        dbc.CardHeader([
            dbc.Row([
                dbc.Col([
                    dbc.Button(
                        label,
                        id=f'{id}_btn',
                        className='analytics_card_topic',
                        color='link',
                        n_clicks=0,
                        style={
                            'color': '#FFFFFF',
                            'background-color': '#2A2A2A',
                            'font-weight': '500',
                            'font-size': '24px',
                            'font-style': 'normal'
                        }
                    )
                ]),
            ]),
        ], style={'background-color': '#2A2A2A', 'border-radius': '20px'}),
        dbc.CardBody([
            dcc.Graph(figure=placeholder_figure, id=f'{id}_plot')
        ], style={'font-size': '20px', 'border-radius': '20px'}),
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle(label)),
            dbc.ModalBody(dcc.Graph(figure=placeholder_figure, id=f'{id}_plot_modal')),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id=f"{id}_close", className="ms-auto", n_clicks=0
                )
            ),
        ], id=f'{id}_modal', is_open=False, size="xl", style={'font-size': '20px', 'border-radius': '20px'})
    ], style={'height': '100%', 'border-radius': '20px'}, color='#2A2A2A', inverse=True)

    @bp.callback(ServersideOutput(f'{id}_store', "data"), Trigger(f'{id}_onload', "children"))
    @time_cache(seconds=60)
    def query_data():
        print(f'Querying plot {label}')
        return mk_figure()

    @bp.callback([
        Output(f'{id}_plot', 'figure'),
        Output(f'{id}_plot_modal', 'figure'),
        Input(f'{id}_store', "data")
    ])
    def display_data(fig):
        return [fig, fig]

    @bp.callback(
        Output(f"{id}_modal", "is_open"),
        [
            Input(f"{id}_btn", "n_clicks"),
            Input(f"{id}_close", "n_clicks")
        ],
        [State(f"{id}_modal", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    bp.register_callbacks(app)

    return bp.layout

layout = dbc.Container([
    dcc.Store(id="data_store"),
    html.Div(id='onload'),
    html.Div([
        dbc.Row([
            dbc.Col(dbc.Label(
                'Analytics: General',
                className="page_section_topic"
            ))
        ]),
        dbc.Row([
            dbc.Col([
                analytics_card_metric(
                    label='Mkt Cap',
                    id='mkt_cap_indicator',
                    value=last_metric.marketCap,
                    format_data=fmt_dollar_value
                )
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                analytics_card_metric(
                    label='Price',
                    id='price_indicator',
                    value=last_metric.klimaPrice,
                    format_data=fmt_dollar_value
                )
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                analytics_card_metric(
                    label='TVD',
                    id='TVD_indicator',
                    value=last_metric.totalValueLocked,
                    format_data=fmt_dollar_value
                )
            ], xs=12, sm=12, md=12, lg=3, xl=3),
            dbc.Col([
                analytics_card_metric(
                    label='Runway',
                    id='runway_indicator',
                    value=last_metric.runwayCurrent,
                    format_data=fmt_days_value
                )
            ], xs=12, sm=12, md=12, lg=3, xl=3),
        ]),
        dbc.Row([
            dbc.Col([
                data_plot(
                    label='Market Cap',
                    id='historical_mkt_cap',
                    mk_figure=mkt_cap_plot
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                data_plot(
                    label='KLIMA Price Over Time',
                    id='historical_klima_price',
                    mk_figure=klima_price
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
        dbc.Row([
            dbc.Col([
                data_plot(
                    label='Current Runway',
                    id='historical_runway',
                    mk_figure=current_runway
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                data_plot(
                    label='Current AKR%',
                    id='historical_AKR',
                    mk_figure=current_AKR
                ),
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
                data_plot(
                    label='Treasury Total Carbon',
                    id='treasury_total_carbon',
                    mk_figure=treasury_total_carbon
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                data_plot(
                    label='Mkt Value of Treasury Assets (USD)',
                    id='tmv',
                    mk_figure=tmv
                ),                
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
        dbc.Row([
            dbc.Col([
                data_plot(
                    label='Backing Assets in Treasury (Carbon Custodied)',
                    id='tCC',
                    mk_figure=tCC
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                data_plot(
                    label='TMV/KLIMA vs KLIMA Price',
                    id='tmv_per_klima',
                    mk_figure=tmv_per_klima
                ),
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
                data_plot(
                    label='CC/KLIMA vs KLIMA Price',
                    id='cc_per_klima',
                    mk_figure=cc_per_klima
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
            dbc.Col([
                data_plot(
                    label='Staked KLIMA (%)',
                    id='staked_percent',
                    mk_figure=staked_percent
                ),
            ], xs=12, sm=12, md=12, lg=6, xl=6),
        ], style={'padding': '10px'}),
    ], className='center_2'),
], id='page_content_analytics', fluid=True)