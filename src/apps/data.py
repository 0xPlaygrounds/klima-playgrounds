from subgrounds.dash_wrappers import AutoUpdate
from subgrounds.plotly_wrappers import Figure, Scatter

from src.apps.subgraph_data.treasury_assets import MODE_ASSET_VALUE_IN_USD, MODE_CARBON_CUSTODIED, TreasuryAssetWrapper

from ..klima_subgrounds import sg, protocol_metrics_1year, get_klima_breakdown_df
from ..app import app
import time
from functools import cache


def time_cache(seconds=3600):
    def decorator(func):
        @cache
        def extra_time_arg_func(time_key):
            return func()

        def wrapper():
            time_key = int(time.time() / seconds)
            return extra_time_arg_func(time_key)

        return wrapper

    return decorator


def wrap_autoupdate(seconds=300):
    def decorator(func):
        def wrapper():
            return AutoUpdate(app, sec_interval=seconds, children=[func()])

        return wrapper

    return decorator


# @wrap_autoupdate(seconds=21600)
def mkt_cap_plot():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='Market Cap',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.marketCap,
                line={'width': 0.5, 'color': '#536C9C'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Market Cap', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True, 'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'legend.font.color': 'white',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'autosize': True,
            'margin': dict(l=20, r=30, t=10, b=20),
            'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
            'newshape_line_color': '#00CC33',
            'modebar_add': ['drawline',
                            'drawopenpath',
                            'drawclosedpath',
                            'drawcircle',
                            'drawrect',
                            'eraseshape'
                            ],
        },
    ).figure


# @wrap_autoupdate(seconds=21600)
def klima_price():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='KLIMA Price',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.klimaPrice,
                line={'width': 0.5, 'color': '#00CC33'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': False,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'KLIMA Price', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'autosize': True,
            'margin': dict(l=20, r=30, t=10, b=20),
            'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
            'newshape_line_color': '#00CC33',
            'modebar_add': ['drawline',
                            'drawopenpath',
                            'drawclosedpath',
                            'drawcircle',
                            'drawrect',
                            'eraseshape'
                            ],
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def current_runway():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='Current Runway',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.runwayCurrent,
                line={'width': 0.5, 'color': '#FEB803'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Current Runway', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'legend.font.color': 'white',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'autosize': True,
            'margin': dict(l=20, r=30, t=10, b=20),
            'legend': dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
            'newshape_line_color': '#00CC33',
            'modebar_add': ['drawline',
                            'drawopenpath',
                            'drawclosedpath',
                            'drawcircle',
                            'drawrect',
                            'eraseshape'
                            ],
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def current_AKR():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='Current AKR%',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.currentAKR,
                line={'width': 0.5, 'color': '#FC8A04'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Current AKR', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def treasury_total_carbon():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='Treasury Total Carbon',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.treasuryCarbon,
                line={'width': 0.5, 'color': '#3EB3FF'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Treasury Total Carbon', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def tmv():
    return Figure(
        subgrounds=sg,
        traces=[
            # Market value treasury assets
            Scatter(
                name='Total_mv',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.treasuryMarketValue,
                mode='lines',
                line={'width': 0.5, 'color': '#00CC33'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'MV of Treasury Assets', 'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def tCC():
    return Figure(
        subgrounds=sg,
        traces=[
            # Risk-free value treasury assets
            Scatter(
                name='Total Reserves',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.treasuryCarbonCustodied,
                mode='lines',
                line={'width': 0.5, 'color': '#536C9C'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Total Reserves', 'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def tmv_klima():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='TMV/KLIMA',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.tmv_per_klima,
                line={'width': 0.5, 'color': '#FEB803'},
                stackgroup='one',
            ),
            Scatter(
                name='KLIMA Price',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.klimaPrice,
                line={'width': 0.5, 'color': '#FC8A0A'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Treasury Market Value per KLIMA vs KLIMA Price', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def tmv_per_klima():
    return Figure(
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
                      'title': 'Treasury Market Value per KLIMA vs KLIMA Price', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def cc_per_klima():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='Risk-Free Value per KLIMA',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.cc_per_klima,
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
                      'title': 'CC/KLIMA and KLIMA Price', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def klima_alloc():

    staked_metrics_df, c3_df, co2_compound_df = get_klima_breakdown_df()
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='NFT Locked',
                x=co2_compound_df.vestingMetrics_datetime,
                y=co2_compound_df.vestingMetrics_locked_percentage,
                mode='lines',
                line={'width': 0.5, 'color': '#eff542'},
                stackgroup='one',
            ),
            Scatter(
                name='C3 Locked',
                x=c3_df.vestingMetrics_datetime,
                y=c3_df.vestingMetrics_locked_percentage,
                mode='lines',
                line={'width': 0.5, 'color': '#FC8A04'},
                stackgroup='one',
            ),
            Scatter(
                name='Staked',
                x=staked_metrics_df.protocolMetrics_datetime,
                y=staked_metrics_df.protocolMetrics_staked_supply_percent,
                mode='lines',
                line={'width': 0.5, 'color': 'rgb(0, 128, 255)'},
                stackgroup='one',
            ),
            Scatter(
                name='In LP',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.klima_in_lp_percent,
                mode='lines',
                line={'width': 0.5, 'color': 'rgb(0, 255, 128)'},
                stackgroup='one',
            ),

            Scatter(
                name='Unstaked',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.unstaked_supply_percent,
                mode='lines',
                line={'width': 0.5, 'color': 'rgb(255, 0, 0)'},
                stackgroup='one',
            )
        ],
        layout={
            'showlegend': True,
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'KLIMA(%)', 'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def treasury_value_in_usd():
    treasury_asset_wrapper = TreasuryAssetWrapper(MODE_ASSET_VALUE_IN_USD)
    return Figure(
        subgrounds=sg,
        traces=treasury_asset_wrapper.create_scatters(),
        layout={
            'showlegend': True,
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Market value (Milions)', 'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def treasury_carbon_custodied():
    treasury_asset_wrapper = TreasuryAssetWrapper(MODE_CARBON_CUSTODIED)
    return Figure(
        subgrounds=sg,
        traces=treasury_asset_wrapper.create_scatters(),
        layout={
            'showlegend': True,
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Carbon custodied in tonnes', 'showgrid': False, 'mirror': True,
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
        }
    ).figure


# @wrap_autoupdate(seconds=21600)
def dao_wallet_balances():
    return Figure(
        subgrounds=sg,
        traces=[
            Scatter(
                name='KLIMA',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.daoBalanceKLIMA,
                line={'width': 0.5, 'color': 'rgb(255, 0, 255)'},
                stackgroup='one',
            ),
            Scatter(
                name='USDC',
                x=protocol_metrics_1year.datetime,
                y=protocol_metrics_1year.daoBalanceUSDC,
                line={'width': 0.5, 'color': 'rgb(2, 193, 50)'},
                stackgroup='one',
            ),
        ],
        layout={
            'showlegend': True,
            'yaxis': {'type': 'linear', 'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'title': 'Amount', 'showgrid': False, 'mirror': True,
                      'showspikes': True, 'spikesnap': 'cursor',
                      'spikemode': 'across', 'spikethickness': 0.5},
            'xaxis': {'linewidth': 0.1, 'linecolor': '#31333F', 'color': 'white',
                      'showgrid': False, 'mirror': True,
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
        }
    ).figure
