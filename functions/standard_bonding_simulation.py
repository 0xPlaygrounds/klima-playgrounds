import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
from millify import millify

from config import RFV_TERM, RFV_WORDS

def bonding_simulation(klima_price, initial_klima, bond_roi, reward_yield):
    # Protocol and Klima calcs:
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
    # ================================================================================

    claim_stake_gas_fee = staking_gas_fee + claim_gas_fee
    remaining_gas_fee = bonding_gas_fee + unstaking_gas_fee + swapping_gas_fee
    # ================================================================================
    # (3,3) Rate for the 15 epochs
    staking_reward_rate = (1 + reward_yield) ** 15 - 1
    staking_reward_rate_P = round(staking_reward_rate * 100, 2)
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

    maxbond_roi = round(stake_bond_df.Bond_ROI.max(), 2)
    maxstake_growth = round(stake_bond_df.Stake_Growth.max(), 2)
    maxBondGrowth = round(stake_bond_df.vested_klimas.max(), 2)
    klimaGained = round((stake_bond_df.vested_klimas.max() - stake_bond_df.Stake_Growth.max()), 2)
    bond_roi_percent = bond_roi * 100

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
        bond_roi_percent, maxbond_roi  # noqa: E127