import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np
from millify import millify

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
card = dbc.Card([dbc.CardHeader("Header"), dbc.CardBody("Body")])

app.layout = dbc.Container([
    html.H2("Playground: Staking"),
    dcc.Tabs([
        dcc.Tab(label='Klima growth over time', children=[
            dcc.Markdown('''

            ## Predicted Growth
            ___
            '''),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader('Klima growth simulation results'),
                    dbc.CardBody([
                      dcc.Graph(id='graph1'),
                      html.Div(id='table')
                    ])
                ], outline=True, color='success', style={"height": "600px"}), width=10),

                dbc.Col(dbc.Card([
                    dbc.CardHeader('Simulation controls'),
                    dbc.CardBody([
                        dbc.Row([
                            html.Label('Days'),
                            dcc.Input(
                                id='growthDays',
                                placeholder='365',
                                type='number',
                                min=1,
                                value=365, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('Starting Klima (Units)'),
                            dcc.Input(
                                id='initialKlima',
                                placeholder='1.0',
                                type='number',
                                min=1,
                                value=1, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('Current APY(%): '),
                            dcc.Input(
                                id='currentAPY',
                                placeholder='40000',
                                type='number',
                                min=1,
                                value=40000, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('percentSale'),
                            dcc.Input(
                                id='percentSale',
                                placeholder='5',
                                type='number',
                                min=1,
                                value=5, style={'width': '100%'}
                            )]),
                        dbc.Row([
                            html.Label('sellDays'),
                            dcc.Input(
                                id='sellDays',
                                placeholder='30',
                                type='number',
                                min=1,
                                value=30, style={'width': '100%'}
                            )
                        ]),
                        dbc.Row([
                            html.Label('klimaPrice_DCA'),
                            dcc.Input(
                                id='klimaPrice_DCA',
                                placeholder='1000',
                                type='number',
                                min=1,
                                value=1000, style={'width': '100%'}
                            )
                        ]),
                        dbc.Row([
                            html.Label('valBuy'),
                            dcc.Input(
                                id='valBuy',
                                placeholder='1000',
                                type='number',
                                min=1,
                                value=1000, style={'width': '100%'}
                            )
                        ]),
                        dbc.Row([
                            html.Label('buyDays'),
                            dcc.Input(
                                id='buyDays',
                                placeholder='30',
                                type='number',
                                min=1,
                                value=30, style={'width': '100%'}
                            )
                        ]),
                        dbc.Row([
                            html.Label('Gas (gwei)'),
                            dcc.Input(
                                id='gwei',
                                placeholder='1',
                                type='number',
                                min=1,
                                value=1, style={'width': '100%'}
                            )
                        ]),
                        dbc.Row([
                            html.Label('priceofETH'),
                            dcc.Input(
                                id='priceofETH',
                                placeholder='10',
                                type='number',
                                min=1,
                                value=10, style={'width': '100%'}
                            )
                        ]),
                    ])
                ], outline=True, color='success', style={"height": "600px"}), width=2),
            ],
                className="mb-4",),

            dbc.Row([
                dcc.Markdown('''
                ## Predicted ROI
                ___
                '''),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Daily ROI', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='dailyROI')
                        ])
                    ])
                ], width=2),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Five day ROI', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='fivedayROI')
                        ])
                    ])
                ], width=2),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Seven day ROI', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='sevendayROI')
                        ])
                    ])
                ], width=2),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Monthly day ROI', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='monthlyROI')
                        ])
                    ])
                ], width=2),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Annual ROI', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='annualROI')
                        ])
                    ])
                ], width=2),
            ]),

            dbc.Row([
                dcc.Markdown('''
                                ## Explanation
                                ___
                                '''),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Explanation'),
                        dbc.CardBody([
                            dcc.Markdown('''
                            The chart shows you the Klima growth projection over 365.0 days. Projection is calculated
                            based on your selected APY of 7000% (Equivalent to a reward yield of 0.5%) and an initial
                            1.0 Klima.

                            The (3,3) Profit adjusted ROI trend line shows you the adjusted Klima growth if you decide
                            to sell a percentage of your Klima at a fixed interval (For example, 5% every 30 days).

                            The Min Growth Rate shows you the estimated Klima growth rate if the APY was on the
                            minimum APY of the current dictated KIP-3 Reward Rate Framework.

                            The Max Growth Rate shows you the estimated Klima growth rate if the APY was on the
                            maximum APY of the current dictated KIP-3 Reward Rate Framework.
                            ''')
                        ])
                    ])
                ], width=10)
            ])






        ]),



        dcc.Tab(label='Klima staking rewards', children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Days until desired USD value in rewards', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='rewardsUSD')
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Days until desired KLIMA balance in rewards', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='rewardsKLIMA')
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Days until desired daily staking rewards', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(style={'color': 'green',
                                            'fontSize': 50}, id='rewardsDaily')
                        ])
                    ])
                ], width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('Days until desired weekly staking rewards', style={
                                       'color': 'white', 'fontSize': 15}),
                        dbc.CardBody([
                            html.Div(
                                style={'color': 'green', 'fontSize': 50}, id='rewardsWeekly')
                        ])
                    ])
                ], width=3),

            ]),

        ])
    ]),
])


@app.callback(
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
    Input(component_id='gwei', component_property='value'),
    Input(component_id='priceofETH', component_property='value'),
)
def klimaGrowth_Projection(growthDays, initialKlima, currentAPY, percentSale, sellDays,
                           klimaPrice_DCA, valBuy, buyDays, gwei, priceofETH):
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

    stakingGasFee = 179123 * ((gwei * priceofETH) / (10 ** 9))
    stakingGasFee_klimaAmount = stakingGasFee / klimaPrice_DCA
    # unstakingGasFee = 89654 * ((gwei * priceofETH) / (10 ** 9))

    rewardYield = ((1+userAPY)**(1/float(1095)))-1
    minOIPYield = ((1 + minAPY) ** (1 / float(1095))) - 1
    maxOIPYield = ((1 + maxAPY) ** (1 / float(1095))) - 1

    # In this case let's consider 1096 Epochs which is 365 days
    klimaGrowth_df = pd.DataFrame(
        np.arange(klimaGrowthEpochs), columns=['Epochs'])
    # There are 3 Epochs per day so divide by 3 to get Days
    klimaGrowth_df['Days'] = klimaGrowth_df.Epochs / 3

    profitAdjusted_klimaGrowth_df = pd.DataFrame(
        np.arange(klimaGrowthEpochs), columns=['Epochs'])
    profitAdjusted_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    dollarCostAVG_klimaGrowth_df = pd.DataFrame(
        np.arange(klimaGrowthEpochs), columns=['Epochs'])
    dollarCostAVG_klimaGrowth_df['Days'] = profitAdjusted_klimaGrowth_df.Epochs / 3

    # To Calculate the klima growth over 3000 Epochs or 1000 days,
    # we loop through the exponential growth equation every epoch
    totalklimas = []  # create an empty array that will hold the componded rewards
    pA_totalklimas = []
    dcA_totalklimas = []

    rewardYield = round(rewardYield, 5)
    # Initial staked klimas used to project growth over time
    klimaStakedGrowth = initialKlima
    pA_klimaStakedGrowth = initialKlima
    dcA_klimaStakedGrowth = initialKlima

    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        # populate the empty array with calclated values each iteration
        totalklimas.append(klimaStakedGrowth)
        pA_totalklimas.append(pA_klimaStakedGrowth)
        dcA_totalklimas.append(dcA_klimaStakedGrowth)

        # compound the total amount of klimas
        klimaStakedGrowth = klimaStakedGrowth * (1 + rewardYield)
        pA_klimaStakedGrowth = pA_klimaStakedGrowth * (1 + rewardYield)
        dcA_klimaStakedGrowth = dcA_klimaStakedGrowth * (1 + rewardYield)

        if elements == sellEpochs:
            sellEpochs = sellEpochs + cadenceConst
            # print(totalklimas[-1] - (totalklimas[-1] * percentSale))
            pA_klimaStakedGrowth = pA_totalklimas[-1] - \
                (pA_totalklimas[-1] * percentSale)
        else:
            pass

        if elements == buyEpochs:
            buyEpochs = buyEpochs + cadenceConst_BUY
            # print(dcA_klimaStakedGrowth)
            dcA_klimaStakedGrowth = (
                dcA_klimaStakedGrowth + (dcaAmount - stakingGasFee_klimaAmount))
            # st.write(stakingGasFee_klimaAmount)
            # print(dcA_klimaStakedGrowth)
        else:
            pass

    # Clean up and add the new array to the main data frame
    klimaGrowth_df['Total_klimas'] = totalklimas
    klimaGrowth_df['Profit_Adjusted_Total_klimas'] = pA_totalklimas
    klimaGrowth_df['DCA_Adjusted_Total_klimas'] = dcA_totalklimas
    # Python is funny so let's round up our numbers . 1 decimal place for days",
    klimaGrowth_df.Days = np.around(klimaGrowth_df.Days, decimals=1)
    # Python is funny so let's round up our numbers . 3 decimal place for klimas"
    klimaGrowth_df.Total_klimas = np.around(
        klimaGrowth_df.Total_klimas, decimals=3)
    klimaGrowth_df.Profit_Adjusted_Total_klimas = np.around(
        klimaGrowth_df.Profit_Adjusted_Total_klimas, decimals=3)
    klimaGrowth_df.DCA_Adjusted_Total_klimas = np.around(
        klimaGrowth_df.DCA_Adjusted_Total_klimas, decimals=3)

    totalklimas_minOIPRate = []
    minOIPYield = round(minOIPYield, 5)
    # Initial staked klimas used to project growth over time
    klimaStakedGrowth_minOIPRate = initialKlima
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_minOIPRate.append(
            klimaStakedGrowth_minOIPRate)  # populate the empty array with calclated values each iteration
        klimaStakedGrowth_minOIPRate = klimaStakedGrowth_minOIPRate * \
            (1 + minOIPYield)  # compound the total amount of klimas
    # Clean up and add the new array to the main data frame
    klimaGrowth_df['Min_klimaGrowth'] = totalklimas_minOIPRate

    totalklimas_maxOIPRate = []
    maxOIPYield = round(maxOIPYield, 5)
    # Initial staked klimas used to project growth over time
    klimaStakedGrowth_maxOIPRate = initialKlima
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas_maxOIPRate.append(
            klimaStakedGrowth_maxOIPRate)  # populate the empty array with calclated values each iteration
        klimaStakedGrowth_maxOIPRate = klimaStakedGrowth_maxOIPRate * \
            (1 + maxOIPYield)  # compound the total amount of klimas
    # Clean up and add the new array to the main data frame
    klimaGrowth_df['Max_klimaGrowth'] = totalklimas_maxOIPRate
    # ================================================================================

    # Let's get some ROI Outputs starting with the daily
    # Equation to calculate your daily ROI based on reward Yield
    dailyROI = dailyROI = (1+rewardYield)**3 - 1
    dailyROI = round(dailyROI * 100, 1)  # daily ROI in Percentage
    # ================================================================================

    # 5 day ROI
    # Equation to calculate your 5 day ROI based on reward Yield
    fivedayROI = (1+rewardYield)**(5*3) - 1
    fivedayROI = round(fivedayROI * 100, 1)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI = (1+rewardYield)**(7 * 3) - 1
    sevendayROI = round(sevendayROI * 100, 1)  # 7 day ROI in Percentage
    # ================================================================================

    # 30 day ROI
    # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI = (1+rewardYield)**(30 * 3) - 1
    monthlyROI = round(monthlyROI * 100, 1)  # 30 day ROI in Percentage
    # ================================================================================

    # Annual ROI
    # Equation to calculate your annual ROI based on reward Yield
    annualROI = (1+rewardYield)**(365 * 3) - 1
    # Equation to calculate your annual ROI based on reward Yield
    annualROI = round(annualROI * 100, 1)
    # ================================================================================

    # Commented out for now since it is unused
    # Let's create a nice looking table to view the results of our calculations.
    # The table will contain the ROIs and the percentages
    # roiData = [['Daily', dailyROI],
    #            ['5 Day', fivedayROI],
    #            ['7 Day', sevendayROI],
    #            ['1 Month', monthlyROI],
    #            ['1 Year', annualROI]]
    # roiTabulated_df = pd.DataFrame(roiData, columns=['Cadence', 'Percentage'])

    dailyROI = '{} %'.format(dailyROI)
    fivedayROI = '{} %'.format(fivedayROI)
    sevendayROI = '{} %'.format(sevendayROI)
    monthlyROI = '{} %'.format(monthlyROI)
    annualROI = '{} %'.format(millify(annualROI, precision=1))
    # ================================================================================

    fig = px.scatter(klimaGrowth_df, x=klimaGrowth_df.Days,  # noqa: F841
                     y=klimaGrowth_df.Total_klimas)

    klimaGrowth_Chart = go.Figure()
    klimaGrowth_Chart.add_trace(go.Scatter(
        x=klimaGrowth_df.Days, y=klimaGrowth_df.Total_klimas, name='(3,3) ROI', fill=None))
    klimaGrowth_Chart.add_trace(go.Scatter(
        x=klimaGrowth_df.Days,
        y=klimaGrowth_df.Profit_Adjusted_Total_klimas, name='(3,3) Profit adjusted ROI  ', fill=None
    ))
    klimaGrowth_Chart.add_trace(go.Scatter(
        x=klimaGrowth_df.Days, y=klimaGrowth_df.DCA_Adjusted_Total_klimas, name='(3,3) DCA adjusted ROI  ', fill=None))
    klimaGrowth_Chart.add_trace(go.Scatter(
        x=klimaGrowth_df.Days, y=klimaGrowth_df.Min_klimaGrowth, name='Min Growth Rate  ', fill=None))
    klimaGrowth_Chart.add_trace(go.Scatter(
        x=klimaGrowth_df.Days, y=klimaGrowth_df.Max_klimaGrowth, name='Max Growth Rate  ', fill=None))

    klimaGrowth_Chart.update_layout(
        autosize=True, showlegend=True, margin=dict(l=20, r=30, t=10, b=20))
    klimaGrowth_Chart.update_layout(
        {'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    klimaGrowth_Chart.update_layout(legend=dict(
        yanchor="top", y=0.99, xanchor="left", x=0.01,), xaxis_title="Days", yaxis_title="Total klimas")
    klimaGrowth_Chart.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F',
                                   color='white', showgrid=False, gridwidth=0.01, mirror=True)
    klimaGrowth_Chart.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F',
                                   color='white', showgrid=False, gridwidth=0.01, mirror=True, zeroline=False)

    klimaGrowth_Chart.layout.legend.font.color = 'white'

    return klimaGrowth_Chart, dailyROI, fivedayROI, sevendayROI, monthlyROI, annualROI


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
