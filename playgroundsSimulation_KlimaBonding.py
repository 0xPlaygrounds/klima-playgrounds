# Import all required packages for this page
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
# import math
# from millify import millify

# Create link to CSS style sheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Build the layout for the app. Using dash bootstrap container here instead of the standard html div.
# Container looks better
app.layout = dbc.Container([
    dbc.Row([
        html.Div(html.Img(src=app.get_asset_url('playgroundsBondingLogo.png'),
                          style={'height': '100%',
                                 'width': '30%',
                                 'padding': '10px'}))
    ]),
    # Create a tab so we can have two sections for the klima growth/rewards simulation
    dcc.Tabs([
        dcc.Tab(label='Klima (4,4) Simulator',
                selected_style={'color': 'green', 'fontSize': '30px', 'height': '70px'},
                style={'color': 'green', 'fontSize': '30px', 'height': '70px'}, children=[
                    dbc.Row([
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('(4,4) Simulation parameters'),
                            dbc.CardBody([
                                # use form for controls
                                dbc.Form([
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col([
                                                    dbc.Label('KLIMA Bond Price (USDC)'),
                                                    dbc.Input(
                                                        id='klima_price',
                                                        placeholder='1000',
                                                        type='number',
                                                        min=1,
                                                        value=800, style={'background-color': '#222222',
                                                                          'color': 'white',
                                                                          'width': '100%'})]),
                                                dbc.Col([
                                                    dbc.Label('Starting amount of KLIMA (Units)'),
                                                    dbc.Input(
                                                        id='initial_klima',
                                                        placeholder='1',
                                                        type='number',
                                                        min=1,
                                                        value=10, style={'background-color': '#222222',
                                                                         'color': 'white',
                                                                         'width': '100%'})]),
                                            ], className="g-2"),
                                        ]), className='w-100'),
                                    dbc.Card(
                                        dbc.CardBody([
                                            dbc.Row([
                                                dbc.Col([
                                                    dbc.Label('Bond ROI (%)'),
                                                    dbc.Input(
                                                        id='bond_roi',
                                                        placeholder='5',
                                                        type='number',
                                                        min=1,
                                                        value=5,
                                                        style={'background-color': '#222222',
                                                               'color': 'white',
                                                               'width': '100%'}),
                                                ]),
                                                dbc.Col([
                                                    dbc.Label('Rebase Rate (%)'),
                                                    dbc.Input(
                                                        id='reward_yield',
                                                        placeholder='0.5',
                                                        type='number',
                                                        min=0.01,
                                                        value=0.5,
                                                        style={'background-color': '#222222',
                                                               'color': 'white',
                                                               'width': '100%'}),
                                                ])
                                            ], className="g-2")]), className='w-100'),
                                ]),
                            ])
                        ], outline=True, color='success', style={"height": "100%"}), className='w-50'),
                    ], style={'padding': '25px'}),
                    dbc.Row([
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('(3,3) and (4,4) Growth comparison'),
                            dbc.CardBody([
                                dcc.Graph(id='graph2'),
                                html.Div(id='table2')
                            ])
                        ], outline=True, color='success', style={"height": "570px"}), className='w-50'),
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Growth Comparison Summary'),
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        dbc.Label('Max (3,3) ROI (%)', style={'color': 'white', 'fontSize': 40}),
                                        html.Div(style={'color': 'white', 'fontSize': 100},
                                                 id='max_33_growth'),
                                    ], className='w-100'),
                                    dbc.Col([
                                        dbc.Label('Max (4,4) ROI (%)', style={'color': 'white', 'fontSize': 40}),
                                        html.Div(style={'color': 'white', 'fontSize': 100},
                                                 id='max_44_growth'),
                                    ], className='w-100'),
                                    dbc.Col([
                                        dbc.Label('Bonus Klima', style={'color': 'white', 'fontSize': 40}),
                                        html.Div(style={'color': 'white', 'fontSize': 100},
                                                 id='bonus_gained'),
                                    ], className='w-100')
                                ], style={'padding': '25px'})
                            ])
                        ], outline=True, color='success', style={"height": "570px"}), className='w-50')
                    ], style={'padding': '25px'}),
                    dbc.Row([
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('(3,3) and (4,4) ROI Comparison'),
                                dbc.CardBody([
                                    dcc.Graph(id='graph3'),
                                    html.Div(id='table3')
                                ])
                            ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
                        dbc.Col(
                            dbc.Card([
                                dbc.CardHeader('(3,3) and (4,4) ROI Summary'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Label('(3,3) ROI (%)', style={'color': 'white', 'fontSize': 40}),
                                            html.Div(style={'color': 'white', 'fontSize': 100},
                                                     id='33_roi'),
                                        ], className='w-100'),
                                        dbc.Col([
                                            dbc.Label('Bond ROI (%)', style={'color': 'white', 'fontSize': 40}),
                                            html.Div(style={'color': 'white', 'fontSize': 100},
                                                     id='bonding_roi'),
                                        ], className='w-100'),
                                        dbc.Col([
                                            dbc.Label('Max (4,4) ROI (%)', style={'color': 'white', 'fontSize': 40}),
                                            html.Div(style={'color': 'white', 'fontSize': 100},
                                                     id='max_44_roi'),
                                        ], className='w-100')
                                    ], style={'padding': '25px'})
                                ])
                            ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
                    ], style={'padding': '25px'}),
                    dbc.Row([
                        dbc.Col(dcc.Markdown('''
                                    ## Explanations
                                    ---
                                    '''))
                    ], style={'padding': '25px'}),
                    dbc.Row([
                        dbc.Col(dbc.Card([
                            dbc.CardHeader('Chart Explanation'),
                            dbc.CardBody([
                                dcc.Markdown('''
                                - The chart shows you the Klima growth projection over 365.0 days.
                                Projection is calculated
                                based
                                on your selected APY of 7000% (Equivalent to a reward yield of 0.5%) and
                                an initial 1.0 Klima.
                                - The (3,3) Profit adjusted ROI trend line shows you the adjusted
                                Klima growth if you decide to
                                sell a percentage of your Klima at a fixed interval (For example, 5% every 30 days).
                                - The Min Growth Rate shows you the estimated Klima growth rate if the APY was on the
                                minimum APY
                                of the current dictated KIP-3 Reward Rate Framework.
                                - The Max Growth Rate shows you the estimated Klima growth rate if the APY was on the
                                maximum APY
                                of the current dictated KIP-3 Reward Rate Framework.
                                ''')
                            ])
                        ], outline=True, color='success'), className='w-50')
                    ], style={'padding': '25px'}),
                ]),

        dcc.Tab(label='Rewards Simulator guide',
                selected_style={'color': 'green', 'fontSize': '30px', 'height': '70px'},
                style={'color': 'green', 'fontSize': '30px', 'height': '70px'},
                children=[
                    dbc.Row([
                        html.Div(html.Img(src=app.get_asset_url('Klima_staking_page-01.png'),
                                          style={'height': '100%',
                                                 'width': '100%',
                                                 'padding': '50px'}))], className='w-100')
                ])
    ], className='mb-4'),
], fluid=True)  # Responsive ui control


@app.callback([
    Output(component_id='graph2', component_property='figure'),
    Output(component_id='graph3', component_property='figure'),
    Output(component_id='max_33_growth', component_property='children'),
    Output(component_id='max_44_growth', component_property='children'),
    Output(component_id='bonus_gained', component_property='children'),
    Output(component_id='33_roi', component_property='children'),
    Output(component_id='bonding_roi', component_property='children'),
    Output(component_id='max_44_roi', component_property='children'),
    Input(component_id='klima_price', component_property='value'),
    Input(component_id='initial_klima', component_property='value'),
    Input(component_id='bond_roi', component_property='value'),
    Input(component_id='reward_yield', component_property='value'),
])
# region Description: Function to calculate ohm growth over time
def bonding_simulation(klima_price, initial_klima, bond_roi, reward_yield):
    # Protocol and ohm calcs:
    usd_bonded = klima_price * initial_klima
    bond_roi = (bond_roi / 100)
    bond_price = klima_price / (1 + bond_roi)
    bonded_klima = usd_bonded / bond_price
    bonded_klimaValue = bonded_klima * klima_price
    gwei = 0
    priceofETH = 1
    # ========================================================================================
    # Calculate the rebase rate and Current APY (next epoch rebase pulled from hippo data source)
    reward_yield = reward_yield / 100
    # rebase_const = 1 + reward_yield  # calculate a constant for use in APY calculation
    # user_apy = rebase_const ** 1095  # current APY equation
    # user_apy_P = user_apy * 100  # convert to %
    # ========================================================================================
    # Calculate fees
    staking_gas_fee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    unstaking_gas_fee = 89654 * ((gwei * priceofETH) / (10 ** 9))
    swapping_gas_fee = 225748 * ((gwei * priceofETH) / (10 ** 9)) + ((0.3 / 100) * bonded_klimaValue)
    claim_gas_fee = 80209 * ((gwei * priceofETH) / (10 ** 9))
    bonding_gas_fee = 258057 * ((gwei * priceofETH) / (10 ** 9))
    # miscFee = 823373 * ((gwei*priceofETH)/(10**9))
    # ================================================================================

    claim_stake_gas_fee = staking_gas_fee + claim_gas_fee
    remaining_gas_fee = bonding_gas_fee + unstaking_gas_fee + swapping_gas_fee
    # ================================================================================
    # (3,3) Rate for the 15 epochs
    staking_reward_rate = (1 + reward_yield) ** 15 - 1
    staking_reward_rate_P = round(staking_reward_rate * 100, 2)
    # stakingOhmsGained = round(((initOhmValue - staking_gas_fee) * (stakingRate / initOhmValue) - 1),4)

    # (3,3) Ohm gained after 15 epochs
    # staking_klima_growth = round(staking_reward_rate * bonded_klimaValue / klima_price, 4)
    # staking_klima_growth = round(staking_klima_growth, 4)
    # ================================================================================
    vested_klima_df = pd.DataFrame(np.arange(1, 16), columns=['Epochs'])
    vested_klima_df['Days'] = vested_klima_df.Epochs / 3
    vested_klima_growth = np.array([], dtype=np.float64)
    bond_roi_growth = np.array([], dtype=np.float64)

    staked_klima_roi_df = pd.DataFrame(np.arange(1, 16), columns=['Epochs'])
    staked_klima_roi_df['Days'] = staked_klima_roi_df.Epochs / 3
    staked_roi_adjusted_growth = np.array([], dtype=np.float64)
    stake_roi_growth = np.array([], dtype=np.float64)
    staked_klima_growth = np.array([], dtype=np.float64)
    stake_growth = initial_klima

    for epochs in vested_klima_df.Epochs:
        vested_klima = ((bonded_klima / (1 + epochs)) * (((1 + reward_yield) ** 15) - 1)) \
                       / ((1 + reward_yield) ** (15 / (1 + epochs)) - 1)
        vested_klima_roi = (((vested_klima * klima_price - epochs * claim_stake_gas_fee
                              - remaining_gas_fee) / usd_bonded) - 1) * 100
        vested_klima_growth = np.append(vested_klima_growth, vested_klima)
        bond_roi_growth = np.append(bond_roi_growth, vested_klima_roi)
    vested_klima_df['vested_klimas'] = vested_klima_growth
    vested_klima_df['Bond_ROI'] = bond_roi_growth

    for epochs in staked_klima_roi_df.Epochs:
        staked_klima_growth = np.append(staked_klima_growth, stake_growth)
        staked_roi_adjusted = ((usd_bonded - staking_gas_fee) * (((1 + reward_yield) ** 15) / usd_bonded) - 1) * 100
        stake_roi = staking_reward_rate * 100
        stake_growth = stake_growth * (1 + reward_yield)
        staked_roi_adjusted_growth = np.append(staked_roi_adjusted_growth, staked_roi_adjusted)
        stake_roi_growth = np.append(stake_roi_growth, stake_roi)
    staked_klima_roi_df['Stake_ROI'] = stake_roi_growth
    staked_klima_roi_df['Staked_feeAdjustedROI'] = staked_roi_adjusted_growth
    staked_klima_roi_df['Stake_Growth'] = staked_klima_growth
    # ================================================================================

    cols_to_use = staked_klima_roi_df.columns.difference(vested_klima_df.columns)
    stake_bond_df = pd.merge(vested_klima_df, staked_klima_roi_df[cols_to_use],
                             left_index=True, right_index=True, how='outer')
    # stake_bond_df = pd.concat([vested_klima_df,staked_klima_roi_df],axis = 1, join = 'inner')

    maxbond_roi = round(stake_bond_df.Bond_ROI.max(), 2)
    maxstake_growth = round(stake_bond_df.Stake_Growth.max(), 2)
    maxBondGrowth = round(stake_bond_df.vested_klimas.max(), 2)
    klimaGained = round((stake_bond_df.vested_klimas.max() - stake_bond_df.Stake_Growth.max()), 2)
    # staking_gas_fee = round(staking_gas_fee, 2)
    # unstaking_gas_fee = round(unstaking_gas_fee, 2)
    # swapping_gas_fee = round(swapping_gas_fee, 2)
    # claim_gas_fee = round(claim_gas_fee, 2)
    # bonding_gas_fee = round(bonding_gas_fee, 2)
    bond_roi_percent = bond_roi * 100

    # vested_klima_df_CSV = vested_klima_df.to_csv().encode('utf-8')
    # staked_klima_roi_df_CSV = staked_klima_roi_df.to_csv().encode('utf-8')

    stake_bond_chart = go.Figure()
    stake_bond_chart.add_trace(go.Scatter(x=stake_bond_df.Epochs, y=stake_bond_df.vested_klimas,
                                          name='(4,4) Growth', fill=None, line=dict(color='#00aff3', width=2)))
    stake_bond_chart.add_trace(go.Scatter(x=stake_bond_df.Epochs, y=stake_bond_df.Stake_Growth,
                                          name='(3,3) Growth', line=dict(color='#ff2a0a', width=2)))

    stake_bond_chart.update_layout(autosize=True, showlegend=True, margin=dict(l=20, r=30, t=10, b=20))
    stake_bond_chart.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                                   xaxis_title="Epochs (Vesting period)", yaxis_title="Total Klimas")
    stake_bond_chart.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})

    stake_bond_chart.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white',
                                  showgrid=False, gridwidth=0.1, mirror=True)
    stake_bond_chart.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white',
                                  showgrid=False, gridwidth=0.01, mirror=True)
    stake_bond_chart.layout.legend.font.color = 'white'

    # =============================

    stake_bond_roi_chart = go.Figure()

    stake_bond_roi_chart.add_trace(go.Scatter(x=stake_bond_df.Epochs, y=stake_bond_df.Bond_ROI, name='(4,4) ROI ',
                                              line=dict(color='#00aff3', width=2)))
    stake_bond_roi_chart.add_trace(go.Scatter(x=stake_bond_df.Epochs, y=stake_bond_df.Stake_ROI, name='(3,3) ROI ',
                                              fill=None, line=dict(color='#ff2a0a', width=2)))

    stake_bond_roi_chart.update_layout(autosize=True, showlegend=True, margin=dict(l=20, r=30, t=10, b=20))
    stake_bond_roi_chart.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                                       xaxis_title="Epochs (Vesting period)",
                                       yaxis_title="ROI based on claim/stake frequency")
    stake_bond_roi_chart.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})

    stake_bond_roi_chart.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white',
                                      showgrid=False, gridwidth=0.1, mirror=True)
    stake_bond_roi_chart.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white',
                                      showgrid=False, gridwidth=0.01, mirror=True)
    stake_bond_roi_chart.layout.legend.font.color = 'white'

    return stake_bond_chart, stake_bond_roi_chart, maxstake_growth, maxBondGrowth, \
        klimaGained, staking_reward_rate_P, \
        bond_roi_percent, maxbond_roi


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
