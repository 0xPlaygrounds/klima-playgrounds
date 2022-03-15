import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
from millify import millify

from config import RFV_TERM, RFV_WORDS


def klimaGrowth_Projection(growthDays, initialKlima,
                           user_apy, min_apy, max_apy, user_rfv,
                           percentSale, switch, sellDays, klimaPrice_DCA,
                           valBuy, buyDays,
                           priceKlima, priceofETH,
                           desired_klima_usdc, desired_klima_unit,
                           desired_daily_rewards_usdc,
                           desired_weekly_rewards_usdc):
    # ===========================Variable definitions and prep===============================
    # In this section we take the input variables and do any kind of prep work
    klimaGrowthEpochs = (growthDays * 3.28) + 1
    sellEpochs = sellDays * 3.28
    buyEpochs = buyDays * 3.28
    cadenceConst = sellEpochs
    cadenceConst_BUY = buyEpochs
    sellAmount = percentSale
    sellType = '%'
    dcaAmount = valBuy / klimaPrice_DCA
    user_apy = user_apy / 100
    minAPY = min_apy / 100
    maxAPY = max_apy / 100
    gwei = 1
    reward_yield = ((1 + user_apy) ** (1 / float(1197.2))) - 1
    reward_yield = round(reward_yield, 5)
    rebase_const = 1 + reward_yield
# 1200
    # In this section, we calculate the staking and unstaking fees. Not required for klima
    staking_gas_fee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    staking_gas_fee_klimaAmount = staking_gas_fee / klimaPrice_DCA
    # unstaking_gas_fee = 89654 * ((gwei * priceofETH) / (10 ** 9))

    # In this section we calculate the reward yield from the users speculated APY
    minOIPYield = ((1 + minAPY) ** (1 / float(1197.2))) - 1
    maxOIPYield = ((1 + maxAPY) ** (1 / float(1197.2))) - 1

    # In this case let's consider 1096 Epochs which is 365 days
    klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    klimaGrowth_df['Days'] = klimaGrowth_df.Epochs / 3.28  # There are 3 Epochs per day so divide by 3 to get Days

    profitAdjusted_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    profitAdjusted_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3.28

    dollarCostAVG_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    dollarCostAVG_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3.28
    # ===========================Variable definitions and prep===============================

    # ============================ USER APY, DCA, PROFIT ADJUSTED PROJECTION =====
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
    dailyROI = (1 + reward_yield) ** 3.28 - 1  # Equation to calculate your daily ROI based on reward Yield
    dailyROI_P = round(dailyROI * 100, 1)  # daily ROI in Percentage
    dailyKlima = initialKlima + (dailyROI * initialKlima)
    dailyKlima_raw = '{}'.format(millify(dailyROI * initialKlima, precision=3))
    # ================================================================================

    # 5 day ROI
    # fivedayROI = (1 + reward_yield) ** (5 * 3) - 1  # Equation to calculate your 5 day ROI based on reward Yield
    # fivedayROI_P = round(fivedayROI * 100, 1)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    sevendayROI = (1 + reward_yield) ** (7 * 3.28) - 1  # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI_P = round(sevendayROI * 100, 1)  # 7 day ROI in Percentage
    sevendayKlima = initialKlima + (sevendayROI * initialKlima)
    sevendayKlima_raw = '{}'.format(millify(sevendayROI * initialKlima, precision=3))
    # ================================================================================

    # 30 day ROI
    monthlyROI = (1 + reward_yield) ** (30 * 3.28) - 1  # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI_P = round(monthlyROI * 100, 1)  # 30 day ROI in Percentage
    monthlyKlima = initialKlima + (monthlyROI * initialKlima)
    monthlyKlima_raw = '{}'.format(millify(monthlyROI * initialKlima, precision=3))
    # ================================================================================

    # Annual ROI
    annualROI = (1 + reward_yield) ** (365 * 3.28) - 1  # Equation to calculate your annual ROI based on reward Yield
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
    klimaGrowth_Chart.update_layout({'paper_bgcolor': '#202020', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
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
    Projection is calculated based on your selected APY of **{user_apy * 100} %**
    which is equivalent to a reward yield of **{reward_yield * 100} %**, and an initial **{initialKlima} KLIMA**

    - The (3,3) Profit adjusted ROI trend line shows you the adjusted KLIMA growth if you decide to
    sell {sellAmount}{sellType} every **{sellDays} days**

    - The (3,3) Dollar cost averaging (DCA) adjusted ROI trend line shows you the adjusted KLIMA growth if you decide
    to buy **{valBuy}** worth of KLIMA every **{buyDays}** days at a unit price of $ **{priceKlima}**

    - The Min Growth Rate shows you the estimated KLIMA growth rate if the APY
    was on the minimum APY of the current dictated KIP-3 Reward Rate Framework

    - The Max Growth Rate shows you the estimated Klima growth rate if the APY
    was on the maximum APY of the current dictated KIP-3 Reward Rate Framework
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
    Using the speculated KLIMA reward yield of **{user_apy * 100} %** and initial **{initialKlima} KLIMA**,
    we can speculate the following returns:

    - Daily ROI based on your input APY of **{user_apy * 100} %** : **{dailyROI_P}**
    which is about **{dailyKlima_raw}** KLIMA per day, totalling **{dailyKlima}** KLIMA after one day

    - Seven day ROI based on your input APY of **{user_apy * 100} %** : **{sevendayROI_P}** which is
    about **{sevendayKlima_raw}** KLIMA per week, totaling **{sevendayKlima}** KLIMA after one week

    - One month ROI based on your input APY of **{user_apy * 100} %** : **{monthlyROI_P}** which is about
    **{monthlyKlima_raw}** KLIMA per month

    - One year ROI based on your input APY of **{user_apy * 100} %** : **{annualROI_P}** which is
    about **{annualKlima_raw}** KLIMA per year
    '''

    strategizer_results = f'''
    Based on your control parameters, these are the predicted outcomes assuming market stability and your parameters
    hold true.

    - It would take {forcastUSDTarget} days until you accumulate enough KLIMA worth ${desired_klima_usdc}.
    Keep in mind that you are also predicting that the price of KLIMA will be ${priceKlima} on this day.

    - It would take {forcastKlimaTarget} days until you accumulate {desired_klima_unit} KLIMA.
    Keep in mind that this prediction is calculated based on your selected APY% of {user_apy * 100} %
    and an initial {initialKlima} KLIMA staked. Use the KIP-3 Framework to adjust your APY % parameter.

    - To start earning daily rewards of $ {desired_daily_rewards_usdc},
    you will need {requiredKlimaDailyIncooom} KLIMA, and based on the APY% you entered,
    it would take {forcastDailyIncooom} days to reach your goal.
    Remember that this prediction relies on your selected APY% of
    {user_apy * 100} %, initial {initialKlima} KLIMA staked, and predicated price of $ {priceKlima}/KLIMA

    - To start earning weekly reward of $ {desired_weekly_rewards_usdc},
    you will need {requiredKlimaWeeklyIncooom} KLIMA, and based on the APY% you entered,
    it would take {forcastWeeklyIncooom} days to reach your goal.
    Remember that this prediction relies on your selected APY% of
    {user_apy * 100} %, initial {initialKlima} KLIMA staked, and predicated price of $ {priceKlima}/KLIMA
    '''

    return klimaGrowth_Chart, dailyROI_P, dailyKlima, sevendayROI_P, sevendayKlima, monthlyROI_P, \
           monthlyKlima, annualROI_P, annualKlima, passenger_vehicle_current, \
           passenger_miles_current, gasoline_consumed_current,\
           trees_co_captured_current, passenger_vehicle_var, passenger_miles_var,\
           gasoline_consumed_var, trees_co_captured_var, forcastUSDTarget, \
           forcastKlimaTarget, rewardsDaily, requiredKlimaDailyIncooom, forcastWeeklyIncooom, \
           requiredKlimaWeeklyIncooom, chart_results_explanation, equivalency_results_explanation, \
           forecast_roi_results_explanation, strategizer_results  # noqa: E127
