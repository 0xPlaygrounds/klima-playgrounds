# Import all required packages for this page
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
from millify import millify

# Create link to CSS style sheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Build the layout for the app. Using dash bootstrap container here instead of the standard html div. Container looks better
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Playground: Staking", className='text-center, mb-4'))
    ]),
    # Create a tab so we can have two sections for the klima growth/rewards simulation
    dcc.Tabs([
        dcc.Tab(label='Klima growth over time', children=[
            dbc.Row([
                dbc.Col(dcc.Markdown('''
                ## Predicted Growth
                ---
                '''))
            ], className='mb-5'),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader('Klima growth simulation results: Charts'),
                    dbc.CardBody([
                        dcc.Graph(id='graph1'),
                        html.Div(id='table')
                    ])
                ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
                dbc.Col(dbc.Card([
                    dbc.CardHeader('Simulation controls'),
                    dbc.CardBody([
                        # use form for controls
                        dbc.Form([

                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Label('Growth over time'),
                                        dbc.Col([
                                            dcc.Slider(
                                                id='growthDays',
                                                min=1,
                                                max=1000,
                                                value=365,
                                                tooltip={'placement': 'top', 'always_visible': True}), ], width='12')]),
                                    dbc.Row([
                                        dbc.Col([
                                            # dbc.Label('Initial Klima'),
                                            dcc.Input(
                                                id='initialKlima',
                                                placeholder='1.0',
                                                type='number',
                                                min=1,
                                                value=1, style={'width': '100%'})]),
                                        dbc.Col([
                                            # dbc.Label('Simulated APY(%)'),
                                            dcc.Input(
                                                id='currentAPY',
                                                placeholder='40000',
                                                type='number',
                                                min=1,
                                                value=40000, style={'width': '100%'})]),
                                    ], className="g-2"),
                                ]), className='w-100'),
                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Label('Profit taking controls'),
                                        dbc.Col([
                                            dcc.Input(
                                                id='percentSale',
                                                placeholder='5',
                                                type='number',
                                                min=1,
                                                value=5,
                                                style={'width': '100%'}),
                                        ]),
                                        dbc.Col([
                                            dcc.Input(
                                                id='sellDays',
                                                placeholder='30',
                                                type='number',
                                                min=1,
                                                value=30,
                                                style={'width': '100%'}),
                                        ])
                                    ], className="g-2")]), className='w-100'),

                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Label('Dollar cost averaging'),
                                        dbc.Col([
                                            dcc.Input(
                                                id='klimaPrice_DCA',
                                                placeholder='1000',
                                                type='number',
                                                min=1,
                                                value=1000, style={'width': '100%'})]),
                                        dbc.Col([
                                            dcc.Input(
                                                id='valBuy',
                                                placeholder='1000',
                                                type='number',
                                                min=1,
                                                value=1000, style={'width': '100%'})]),
                                        dbc.Col([
                                            dcc.Input(
                                                id='buyDays',
                                                placeholder='30',
                                                type='number',
                                                min=1,
                                                value=30, style={'width': '100%'})]),
                                    ], className="g-2")]), className='w-100'),

                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Label('Staking rewards controls'),
                                        dbc.Col([
                                            dcc.Input(
                                                id='priceKlima',
                                                placeholder='1000',
                                                type='number',
                                                min=1,
                                                value=1000, style={'width': '100%'}
                                            )]),
                                        dbc.Col([
                                            dcc.Input(
                                                id='priceofETH',
                                                placeholder='10',
                                                type='number',
                                                min=1,
                                                value=10, style={'width': '100%'}
                                            ),
                                        ]),
                                    ], className="g-2")]), className='w-100'),
                        ]),
                    ])
                ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
            ], className="mb-5"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Klima growth simulation results: ROI'),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Daily', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='dailyROI')
                                        ])
                                    ])
                                ], width=2),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Five day', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='fivedayROI')
                                        ])
                                    ])
                                ], width=2),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Seven day', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='sevendayROI')
                                        ])
                                    ])
                                ], width=2),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Monthly', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='monthlyROI')
                                        ])
                                    ])
                                ], width=2),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Annual', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='annualROI')
                                        ])
                                    ])
                                ], width=2),
                            ], className="g-2", justify='center'),
                        ]),
                    ], outline=True, color='success', style={"height": "250px"}), ]),
            ], className="mb-5"),
            dbc.Row([
                dbc.Col(dcc.Markdown('''
                ## Rewards Strategizer
                ---
                '''))
            ], className='mb-5'),
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader('Rewards strategy results'),
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Days until USDC Value', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='rewardsUSD'),
                                        ])
                                    ])
                                ], className='w-100'),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.Label('Days until KLIMA amount', style={'color': 'white', 'fontSize': 15}),
                                        dbc.CardBody([
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='rewardsKLIMA'),
                                        ])
                                    ])
                                ], className='w-100'),
                            ], style={'padding': '25px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Card([
                                        # dbc.Label('Daily rewards requirements'),
                                        dbc.CardBody([
                                            dbc.Label('Days until your desired daily rewards'),
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='rewardsDaily'),
                                            dbc.Label('Required KLIMA for desired daily rewards'),
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='requiredDaily'),
                                        ])
                                    ])
                                ], className='w-100'),
                                dbc.Col([
                                    dbc.Card([
                                        # dbc.Label('Daily rewards requirements'),
                                        dbc.CardBody([
                                            dbc.Label('Days until your desired weekly rewards'),
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='rewardsWeekly'),
                                            dbc.Label('Required KLIMA for desired weekly rewards'),
                                            html.Div(style={'color': 'white', 'fontSize': 50}, id='requiredWeekly'),
                                        ])
                                    ])
                                ], className='w-100')
                            ], style={'padding': '25px'})

                        ])
                    ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader('Rewards strategizer controls'),
                        dbc.CardBody([
                        ])
                    ], outline=True, color='success', style={"height": "600px"}), className='w-50'),
            ], className='mb-5'),
            dbc.Row([
                dbc.Col(dcc.Markdown(''' 
                ## Explanations
                ---
                '''))
            ], className='mb-5'),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader('Chart Explanation'),
                    dbc.CardBody([
                        dcc.Markdown('''
            The chart shows you the Klima growth projection over 365.0 days. Projection is calculated based
            on your selected APY of 7000% (Equivalent to a reward yield of 0.5%) and an initial 1.0 Klima.

            The (3,3) Profit adjusted ROI trend line shows you the adjusted Klima growth if you decide to 
            sell a percentage of your Klima at a fixed interval (For example, 5% every 30 days).

            The Min Growth Rate shows you the estimated Klima growth rate if the APY was on the minimum APY
            of the current dictated KIP-3 Reward Rate Framework.

            The Max Growth Rate shows you the estimated Klima growth rate if the APY was on the maximum APY
            of the current dictated KIP-3 Reward Rate Framework.
            ''')
                    ])
                ], outline=True, color='success'), className='w-50')
            ], className="mb-5"),
        ]),

        dcc.Tab(label='Klima staking rewards', children=[
            dbc.Row([

                dbc.Col([dbc.Card([
                    dbc.CardHeader('Staking rewards forecast controls'),
                    dbc.CardBody([
                        dbc.Row([
                            html.Label('Desired KLIMA Value (USDC)'),
                            dcc.Input(
                                id='desiredKlimaUSDC',
                                placeholder='10000',
                                type='number',
                                min=1000,
                                value=10000, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('Desired amount of KLIMA (Units)'),
                            dcc.Input(
                                id='desiredKlimaUnit',
                                placeholder='500.0',
                                type='number',
                                min=1,
                                value=500, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('Desired daily staking rewards (USDC)'),
                            dcc.Input(
                                id='desiredDailyRewardsUSDC',
                                placeholder='5000',
                                type='number',
                                min=1,
                                value=5000, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('Desired weekly staking rewards (USDC)'),
                            dcc.Input(
                                id='desiredWeeklyRewardsUSDC',
                                placeholder='5000',
                                type='number',
                                min=1,
                                value=5000, style={'width': '100%'}
                            )]),
                    ]),
                ])], width=3)
            ]),
        ], className='mb-4'),
    ])
], fluid=True)  # Responsive ui control


# call back for klima growth controls

@app.callback([
    Output(component_id='graph1', component_property='figure'),
    Output(component_id='dailyROI', component_property='children'),
    Output(component_id='fivedayROI', component_property='children'),
    Output(component_id='sevendayROI', component_property='children'),
    Output(component_id='monthlyROI', component_property='children'),
    Output(component_id='annualROI', component_property='children'),
    Input(component_id='growthDays', component_property='value'),
    Input(component_id='initialKlima', component_property='value'),
    Input(component_id='currentAPY', component_property='value'),
    Input(component_id='percentSale', component_property='value'),
    Input(component_id='sellDays', component_property='value'),
    Input(component_id='klimaPrice_DCA', component_property='value'),
    Input(component_id='valBuy', component_property='value'),
    Input(component_id='buyDays', component_property='value'),
    Input(component_id='priceKlima', component_property='value'),
    Input(component_id='priceofETH', component_property='value'),
])
# function to calculate klima growth over user specified number of days
def klimaGrowth_Projection(growthDays, initialKlima, currentAPY, percentSale, sellDays, klimaPrice_DCA, valBuy, buyDays,
                           priceKlima, priceofETH):
    # Data frame to hold all required data point. Data required would be Epochs since rebase are distributed every Epoch
    klimaGrowthEpochs = (growthDays * 3) + 1
    sellEpochs = sellDays * 3
    buyEpochs = buyDays * 3
    cadenceConst = sellEpochs
    cadenceConst_BUY = buyEpochs
    dcaAmount = valBuy / klimaPrice_DCA
    percentSale = percentSale / 100
    userAPY = currentAPY / 100
    minAPY = 1000 / 100
    maxAPY = 10000 / 100
    gwei = 1

    stakingGasFee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    stakingGasFee_klimaAmount = stakingGasFee / klimaPrice_DCA
    # unstakingGasFee = 89654 * ((gwei * priceofETH) / (10 ** 9))

    rewardYield = ((1 + userAPY) ** (1 / float(1095))) - 1
    minOIPYield = ((1 + minAPY) ** (1 / float(1095))) - 1
    maxOIPYield = ((1 + maxAPY) ** (1 / float(1095))) - 1

    # In this case let's consider 1096 Epochs which is 365 days
    klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    klimaGrowth_df['Days'] = klimaGrowth_df.Epochs / 3  # There are 3 Epochs per day so divide by 3 to get Days

    profitAdjusted_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    profitAdjusted_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    dollarCostAVG_klimaGrowth_df = pd.DataFrame(np.arange(klimaGrowthEpochs), columns=['Epochs'])
    dollarCostAVG_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    # To Calculate the klima growth over 3000 Epochs or 1000 days,
    # we loop through the exponential klima growth equation every epoch
    totalklimas = []  # create an empty array that will hold the componded rewards
    pA_totalklimas = []
    dcA_totalklimas = []

    rewardYield = round(rewardYield, 5)
    klimaStakedGrowth = initialKlima  # Initial staked klimas used to project growth over time
    pA_klimaStakedGrowth = initialKlima
    dcA_klimaStakedGrowth = initialKlima

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
            # print(totalklimas[-1] - (totalklimas[-1] * percentSale))
            pA_klimaStakedGrowth = pA_totalklimas[-1] - (pA_totalklimas[-1] * percentSale)
        else:
            pass

        if elements == buyEpochs:
            buyEpochs = buyEpochs + cadenceConst_BUY
            # print(dcA_klimaStakedGrowth)
            dcA_klimaStakedGrowth = (dcA_klimaStakedGrowth + (dcaAmount - stakingGasFee_klimaAmount))
            # st.write(stakingGasFee_klimaAmount)
            # print(dcA_klimaStakedGrowth)
        else:
            pass

    klimaGrowth_df['Total_klimas'] = totalklimas  # Clean up and add the new array to the main data frame
    klimaGrowth_df['Profit_Adjusted_Total_klimas'] = pA_totalklimas
    klimaGrowth_df['DCA_Adjusted_Total_klimas'] = dcA_totalklimas
    klimaGrowth_df.Days = np.around(klimaGrowth_df.Days,
                                    decimals=1)  # Python is funny so let's round up our numbers . 1 decimal place for days",
    klimaGrowth_df.Total_klimas = np.around(klimaGrowth_df.Total_klimas,
                                            decimals=3)  # Python is funny so let's round up our numbers . 3 decimal place for klimas"
    klimaGrowth_df.Profit_Adjusted_Total_klimas = np.around(klimaGrowth_df.Profit_Adjusted_Total_klimas, decimals=3)
    klimaGrowth_df.DCA_Adjusted_Total_klimas = np.around(klimaGrowth_df.DCA_Adjusted_Total_klimas, decimals=3)

    totalklimas_minOIPRate = []
    minOIPYield = round(minOIPYield, 5)
    klimaStakedGrowth_minOIPRate = initialKlima  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_minOIPRate.append(
            klimaStakedGrowth_minOIPRate)  # populate the empty array with calclated values each iteration
        klimaStakedGrowth_minOIPRate = klimaStakedGrowth_minOIPRate * (
                    1 + minOIPYield)  # compound the total amount of klimas
    klimaGrowth_df['Min_klimaGrowth'] = totalklimas_minOIPRate  # Clean up and add the new array to the main data frame

    totalklimas_maxOIPRate = []
    maxOIPYield = round(maxOIPYield, 5)
    klimaStakedGrowth_maxOIPRate = initialKlima  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_maxOIPRate.append(
            klimaStakedGrowth_maxOIPRate)  # populate the empty array with calclated values each iteration
        klimaStakedGrowth_maxOIPRate = klimaStakedGrowth_maxOIPRate * (
                    1 + maxOIPYield)  # compound the total amount of klimas
    klimaGrowth_df['Max_klimaGrowth'] = totalklimas_maxOIPRate  # Clean up and add the new array to the main data frame
    # ================================================================================

    # Let's get some ROI Outputs starting with the daily
    dailyROI = dailyROI = (1 + rewardYield) ** 3 - 1  # Equation to calculate your daily ROI based on reward Yield
    dailyROI = round(dailyROI * 100, 1)  # daily ROI in Percentage
    # ================================================================================

    # 5 day ROI
    fivedayROI = (1 + rewardYield) ** (5 * 3) - 1  # Equation to calculate your 5 day ROI based on reward Yield
    fivedayROI = round(fivedayROI * 100, 1)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    sevendayROI = (1 + rewardYield) ** (7 * 3) - 1  # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI = round(sevendayROI * 100, 1)  # 7 day ROI in Percentage
    # ================================================================================

    # 30 day ROI
    monthlyROI = (1 + rewardYield) ** (30 * 3) - 1  # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI = round(monthlyROI * 100, 1)  # 30 day ROI in Percentage
    # ================================================================================

    # Annual ROI
    annualROI = (1 + rewardYield) ** (365 * 3) - 1  # Equation to calculate your annual ROI based on reward Yield
    annualROI = round(annualROI * 100, 1)  # Equation to calculate your annual ROI based on reward Yield
    # ================================================================================

    # Let's create a nice looking table to view the results of our calculations. The table will contain the ROIs and the percentages
    roiData = [['Daily', dailyROI],
               ['5 Day', fivedayROI],
               ['7 Day', sevendayROI],
               ['1 Month', monthlyROI],
               ['1 Year', annualROI]]
    roiTabulated_df = pd.DataFrame(roiData, columns=['Cadence', 'Percentage'])

    dailyROI = '{} %'.format(dailyROI)
    fivedayROI = '{} %'.format(fivedayROI)
    sevendayROI = '{} %'.format(sevendayROI)
    monthlyROI = '{} %'.format(monthlyROI)
    annualROI = '{} %'.format(millify(annualROI, precision=1))
    # ================================================================================

    fig = px.scatter(klimaGrowth_df, x=klimaGrowth_df.Days, y=klimaGrowth_df.Total_klimas)
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
    klimaGrowth_Chart.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    klimaGrowth_Chart.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01, ), xaxis_title="Days",
                                    yaxis_title="Total klimas")
    klimaGrowth_Chart.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white', showgrid=False,
                                   gridwidth=0.01, mirror=True)
    klimaGrowth_Chart.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F', color='white', showgrid=False,
                                   gridwidth=0.01, mirror=True, zeroline=False)

    klimaGrowth_Chart.layout.legend.font.color = 'white'

    return klimaGrowth_Chart, dailyROI, fivedayROI, sevendayROI, monthlyROI, annualROI


# call backs for desired staking rewards controls
@app.callback([
    Output(component_id='rewardsUSD', component_property='children'),
    Output(component_id='rewardsKLIMA', component_property='children'),
    Output(component_id='rewardsDaily', component_property='children'),
    Output(component_id='requiredDaily', component_property='children'),
    Output(component_id='rewardsWeekly', component_property='children'),
    Output(component_id='requiredWeekly', component_property='children'),
    Input(component_id='desiredKlimaUSDC', component_property='value'),
    Input(component_id='desiredKlimaUnit', component_property='value'),
    Input(component_id='desiredDailyRewardsUSDC', component_property='value'),
    Input(component_id='desiredWeeklyRewardsUSDC', component_property='value'),
])
# This function will calculate the user desired staking rewards. Output will be number of days until user achieves goals
def stakingRewardsProjection(desiredKlimaUSDC, desiredKlimaUnit, desiredDailyRewardsUSDC, desiredWeeklyRewardsUSDC):
    # Some variables are still hard coded i.e initial klime, user apy etc. this will be changed in the next update once chained callbacks are implemented
    initialKlima = 1
    userAPY = 40000 / 100
    rewardYield = ((1 + userAPY) ** (1 / float(1095))) - 1
    rewardYield = round(rewardYield, 5)
    rebaseConst = 1 + rewardYield
    priceKlima = 1000
    dailyROI = 1.7 / 100
    sevendayROI = 12.2 / 100
    # current staking %APY. Need to make this read from a source or user entry

    # ================================================================================
    # Days until you reach target USD by staking only
    forcastUSDTarget = round((math.log(desiredKlimaUSDC / (initialKlima * priceKlima), rebaseConst) / 3))
    # ================================================================================
    # Days until you reach target OHM by staking only
    forcastOHMTarget = round(math.log(desiredKlimaUnit / (initialKlima), rebaseConst) / 3)
    # ================================================================================
    # Daily Incooom calculations
    # Required OHMs until you are earning your desired daily incooom
    requiredOHMDailyIncooom = round((desiredDailyRewardsUSDC / dailyROI) / priceKlima)
    # Days until you are earning your desired daily incooom from your current initial staked OHM amount
    forcastDailyIncooom = round(math.log((requiredOHMDailyIncooom / initialKlima), rebaseConst) / 3)
    requiredUSDForDailyIncooom = requiredOHMDailyIncooom * priceKlima
    # ================================================================================
    # Weekly Incooom calculations
    # Required OHMs until you are earning your desired weekly incooom
    requiredOHMWeeklyIncooom = round((desiredWeeklyRewardsUSDC / sevendayROI) / priceKlima)
    # Days until you are earning your desired weekly incooom from your current initial staked OHM amount
    forcastWeeklyIncooom = round(math.log((requiredOHMWeeklyIncooom / initialKlima), rebaseConst) / 3)
    requiredUSDForWeeklyIncooom = requiredOHMWeeklyIncooom * priceKlima
    # ================================================================================
    # Let's create a nice looking table to view the results of our calculations. The table will contain the ROIs and the percentages
    incooomForcastData = [['USD Target($)', forcastUSDTarget],
                          ['OHM Target(OHM)', forcastOHMTarget],
                          ['Required OHM for desired daily incooom', requiredOHMDailyIncooom],
                          ['Days until desired daily incooom goal', forcastDailyIncooom],
                          ['Required OHM for weekly incooom goal', requiredOHMWeeklyIncooom],
                          ['Days until desired weekly incooom goal', forcastWeeklyIncooom]]

    incooomForcastData_df = pd.DataFrame(incooomForcastData, columns=['Forcast', 'Results'])
    incooomForcastDataDataTable = incooomForcastData_df.to_dict('rows')
    columns = [{'name': i, 'id': i, } for i in (incooomForcastData_df.columns)]

    rewardsUSD = 2
    rewardsKLIMA = 3
    rewardsDaily = 4
    rewardsWeekly = 5
    requiredOHMDailyIncooom = 6
    requiredOHMWeeklyIncooom = 7

    return rewardsUSD, rewardsKLIMA, rewardsDaily, requiredOHMDailyIncooom, rewardsWeekly, requiredOHMWeeklyIncooom


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
