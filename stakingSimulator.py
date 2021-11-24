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

# region Description: Function to calculate klima growth over time
def klimaGrowth_Projection(initialklimas, userAPY, klimaGrowthDays, minAPY, maxAPY,percentSale, sellDays, klimaPrice_DCA, valBuy, buyDays, gwei, priceofETH):
#def klimaGrowth_Projection(initialklimas=1, userAPY=7000, klimaGrowthDays=365, minAPY=1000, maxAPY=10000,percentSale=5, sellDays=30, klimaPrice_DCA=500, valBuy=200, buyDays=60, gwei=40, priceofETH=4000):

    # Data frame to hold all required data point. Data required would be Epochs since rebase are distributed every Epoch
    klimaGrowthEpochs = (klimaGrowthDays * 3)+1
    sellEpochs = sellDays * 3
    buyEpochs = buyDays * 3
    cadenceConst = sellEpochs
    cadenceConst_BUY = buyEpochs
    dcaAmount = valBuy/klimaPrice_DCA
    percentSale = percentSale/100
    userAPY = userAPY/100
    minAPY = minAPY/100
    maxAPY = maxAPY/100

    gwei = 100
    priceofETH = 4000
    stakingGasFee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    stakingGasFee_klimaAmount = stakingGasFee/klimaPrice_DCA
    #unstakingGasFee = 89654 * ((gwei * priceofETH) / (10 ** 9))


    rewardYield = ((1+userAPY)**(1/float(1095)))-1
    minOIPYield = ((1 + minAPY) ** (1 / float(1095))) - 1
    maxOIPYield = ((1 + maxAPY) ** (1 / float(1095))) - 1


    klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs),columns=['Epochs'])  # In this case let's consider 1096 Epochs which is 365 days
    klimaGrowth_df['Days'] = klimaGrowth_df.Epochs / 3  # There are 3 Epochs per day so divide by 3 to get Days

    profitAdjusted_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs),columns=['Epochs'])
    profitAdjusted_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    dollarCostAVG_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs),columns=['Epochs'])
    dollarCostAVG_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    # To Calculate the klima growth over 3000 Epochs or 1000 days, we loop through the exponential klima growth equation every epoch
    totalklimas = []  # create an empty array that will hold the componded rewards
    pA_totalklimas = []
    dcA_totalklimas = []

    rewardYield = round(rewardYield, 5)
    klimaStakedGrowth = initialklimas  # Initial staked klimas used to project growth over time
    pA_klimaStakedGrowth = initialklimas
    dcA_klimaStakedGrowth = initialklimas


    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas.append(klimaStakedGrowth)  # populate the empty array with calclated values each iteration
        pA_totalklimas.append(pA_klimaStakedGrowth)
        dcA_totalklimas.append(dcA_klimaStakedGrowth)


        klimaStakedGrowth = klimaStakedGrowth * (1 + rewardYield)  # compound the total amount of klimas
        pA_klimaStakedGrowth = pA_klimaStakedGrowth * (1 + rewardYield)
        dcA_klimaStakedGrowth = dcA_klimaStakedGrowth * (1 + rewardYield)

        if elements == sellEpochs:
            sellEpochs = sellEpochs + cadenceConst
            #print(totalklimas[-1] - (totalklimas[-1] * percentSale))
            pA_klimaStakedGrowth = pA_totalklimas[-1] - (pA_totalklimas[-1]*percentSale)
        else:
            pass

        if elements == buyEpochs:
            buyEpochs = buyEpochs + cadenceConst_BUY
            #print(dcA_klimaStakedGrowth)
            dcA_klimaStakedGrowth = (dcA_klimaStakedGrowth + (dcaAmount-stakingGasFee_klimaAmount))
            #st.write(stakingGasFee_klimaAmount)
            #print(dcA_klimaStakedGrowth)
        else:
            pass

    klimaGrowth_df['Total_klimas'] = totalklimas  # Clean up and add the new array to the main data frame
    klimaGrowth_df['Profit_Adjusted_Total_klimas'] = pA_totalklimas
    klimaGrowth_df['DCA_Adjusted_Total_klimas'] = dcA_totalklimas
    klimaGrowth_df.Days = np.around( klimaGrowth_df.Days, decimals=1)  # Python is funny so let's round up our numbers . 1 decimal place for days",
    klimaGrowth_df.Total_klimas = np.around( klimaGrowth_df.Total_klimas, decimals=3 )  # Python is funny so let's round up our numbers . 3 decimal place for klimas"
    klimaGrowth_df.Profit_Adjusted_Total_klimas = np.around(klimaGrowth_df.Profit_Adjusted_Total_klimas, decimals=3)
    klimaGrowth_df.DCA_Adjusted_Total_klimas = np.around(klimaGrowth_df.DCA_Adjusted_Total_klimas, decimals=3)


    totalklimas_minOIPRate = []
    minOIPYield = round(minOIPYield, 5)
    klimaStakedGrowth_minOIPRate = initialklimas  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_minOIPRate.append(
            klimaStakedGrowth_minOIPRate)  # populate the empty array with calclated values each iteration
        klimaStakedGrowth_minOIPRate = klimaStakedGrowth_minOIPRate * (1 + minOIPYield)  # compound the total amount of klimas
    klimaGrowth_df['Min_klimaGrowth'] = totalklimas_minOIPRate  # Clean up and add the new array to the main data frame

    totalklimas_maxOIPRate = []
    maxOIPYield = round(maxOIPYield, 5)
    klimaStakedGrowth_maxOIPRate = initialklimas  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_maxOIPRate.append(
            klimaStakedGrowth_maxOIPRate)  # populate the empty array with calclated values each iteration
        klimaStakedGrowth_maxOIPRate = klimaStakedGrowth_maxOIPRate * (1 + maxOIPYield)  # compound the total amount of klimas
    klimaGrowth_df['Max_klimaGrowth'] = totalklimas_maxOIPRate  # Clean up and add the new array to the main data frame

    klimaGrowth_df_CSV = klimaGrowth_df.to_csv().encode('utf-8')
    # ================================================================================


    return klimaGrowth_df,klimaGrowth_df_CSV
# end region