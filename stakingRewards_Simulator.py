# ==============THE LIBRARIES
# region Description: Import all required libraries for this simulator
# from pycoingecko import CoinGeckoAPI # Coin gecko API: Pulls live data from coin gecko
import math  # Needed for basic math operations\n",
import pandas as pd  # Needed fpr dataframe creation and operations\n",
import numpy as np  # Needed for array manipulations\n",
from itertools import islice  # Needed for more complex row and coloumn slicing\n",
import matplotlib.pyplot as plt  # Needed for quickly ploting results"
import base64
from PIL import Image
import pathlib  # url management
from pathlib import Path
import plotly.express as px  # cleaner graphs
import plotly.graph_objects as go  # cleaner graphs
import plotly.figure_factory as ff
import requests
# endregion


def incooomProjection(klimaPrice,userAPY, initialklimas, desiredUSDTarget,desiredklimaTarget, desiredDailyIncooom,desiredWeeklyIncooom):

    klimaStakedInit = initialklimas
    userAPY = userAPY / 100
    rewardYield = ((1 + userAPY) ** (1 / float(1095))) - 1
    rewardYield = round(rewardYield, 5)
    rebaseConst = 1 + rewardYield
    # current staking %APY. Need to make this read from a source or user entry
    #currentAPY = 17407 / 100

    # Let's get some ROI Outputs starting with the daily
    dailyROI = (1+rewardYield)**3 -1  # Equation to calculate your daily ROI based on reward Yield
    dailyROI_P = round(dailyROI * 100, 1)  # daily ROI in Percentage
    # ================================================================================

    # 5 day ROI
    fivedayROI = (1+rewardYield)**(5*3)-1   # Equation to calculate your 5 day ROI based on reward Yield
    fivedayROI_P = round(fivedayROI * 100, 1)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    sevendayROI = (1+rewardYield)**( 7 * 3)-1  # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI_P = round(sevendayROI * 100, 1)  # 7 day ROI in Percentage
    # ================================================================================

    # 30 day ROI
    monthlyROI = (1+rewardYield)**( 30 *3)-1  # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI_P = round(monthlyROI * 100, 1)  # 30 day ROI in Percentage
    # ================================================================================

    # Annual ROI
    annualROI = (1+rewardYield)**( 365 *3)-1  # Equation to calculate your annual ROI based on reward Yield
    annualROI_P = round(annualROI * 100, 1)  # Equation to calculate your annual ROI based on reward Yield
    # ================================================================================

    # Let's create a nice looking table to view the results of our calculations. The table will contain the ROIs and the percentages
    roiData = [['Daily', dailyROI_P],
               ['5 Day', fivedayROI_P],
               ['7 Day', sevendayROI_P],
               ['1 Month', monthlyROI_P],
               ['1 Year', annualROI_P]]
    roiTabulated_df = pd.DataFrame(roiData, columns=['Cadence', 'Percentage'])
    roiDataTable = roiTabulated_df.to_dict('rows')
    columns = [{'name': i,'id': i,} for i in (roiTabulated_df.columns)]
    # ================================================================================
    # Days until you reach target USD by staking only
    forcastUSDTarget = round((math.log(desiredUSDTarget / (klimaStakedInit * klimaPrice), rebaseConst) /3))
    # ================================================================================
    # Days until you reach target klima by staking only
    forcastklimaTarget = round(math.log(desiredklimaTarget / (klimaStakedInit), rebaseConst) / 3)
    # ================================================================================
    # Daily Incooom calculations
    # Required klimas until you are earning your desired daily incooom
    requiredklimaDailyIncooom = round((desiredDailyIncooom / dailyROI) / klimaPrice)
    # Days until you are earning your desired daily incooom from your current initial staked klima amount
    forcastDailyIncooom = round(math.log((requiredklimaDailyIncooom / klimaStakedInit), rebaseConst) / 3)
    requiredUSDForDailyIncooom = requiredklimaDailyIncooom * klimaPrice
    # ================================================================================
    # Weekly Incooom calculations
    # Required klimas until you are earning your desired weekly incooom
    requiredklimaWeeklyIncooom = round((desiredWeeklyIncooom / sevendayROI) / klimaPrice)
    # Days until you are earning your desired weekly incooom from your current initial staked klima amount
    forcastWeeklyIncooom = round(math.log((requiredklimaWeeklyIncooom / klimaStakedInit), rebaseConst) / 3)
    requiredUSDForWeeklyIncooom = requiredklimaWeeklyIncooom * klimaPrice
    # ================================================================================
    # Let's create a nice looking table to view the results of our calculations. The table will contain the ROIs and the percentages
    incooomForcastData = [['USD Target($)', forcastUSDTarget],
                          ['klima Target(klima)', forcastklimaTarget],
                          ['Required klima for desired daily incooom', requiredklimaDailyIncooom],
                          ['Days until desired daily incooom goal', forcastDailyIncooom],
                          ['Required klima for weekly incooom goal', requiredklimaWeeklyIncooom],
                          ['Days until desired weekly incooom goal', forcastWeeklyIncooom]]

    incooomForcastData_df = pd.DataFrame(incooomForcastData, columns=['Forcast', 'Results'])
    incooomForcastDataDataTable = incooomForcastData_df.to_dict('rows')
    columns = [{'name': i,'id': i,} for i in (incooomForcastData_df.columns)]

    return roiTabulated_df,incooomForcastData_df, rewardYield