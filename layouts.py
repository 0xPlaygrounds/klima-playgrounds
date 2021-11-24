import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
import plotly.graph_objects as go  # cleaner graphs
import plotly.figure_factory as ff
from simTest import df, df2
from stakingSimulator import klimaGrowth_Projection
from stakingRewards_Simulator import incooomProjection
import base64


#####################################
# Add your data
#####################################

# example iris dataset
#df = px.data.iris()
klimaGrowthResult_df,klimaGrowth_df_CSV = klimaGrowth_Projection(initialklimas=1, userAPY=7000, klimaGrowthDays=365, minAPY=1000, maxAPY=10000,percentSale=5, sellDays=30, klimaPrice_DCA=500, valBuy=200, buyDays=60, gwei=40, priceofETH=4000)
klimaGrowth_X = klimaGrowthResult_df.Days
klimaGrowth_Y = klimaGrowthResult_df.Total_klimas
ProfitAdjusted_klimaGrowth_Y = klimaGrowthResult_df.Profit_Adjusted_Total_klimas
dollarCostAverage_klimaGrowth_Y = klimaGrowthResult_df.DCA_Adjusted_Total_klimas
minklimaGrowth_Y = klimaGrowthResult_df.Min_klimaGrowth
maxklimaGrowth_Y = klimaGrowthResult_df.Max_klimaGrowth

roiSimulationResult_df,incooomSimulationResult_df,rewardYield = incooomProjection(klimaPrice=1000,userAPY=7000, initialklimas=1, desiredUSDTarget=10000,desiredklimaTarget=100, desiredDailyIncooom=1000,desiredWeeklyIncooom=5000)
dailyROI = float(roiSimulationResult_df.Percentage[0])
fiveDayROI = float(roiSimulationResult_df.Percentage[1])
sevenDayROI = float(roiSimulationResult_df.Percentage[2])
oneMonthROI = float(roiSimulationResult_df.Percentage[3])
oneYearROI = float(roiSimulationResult_df.Percentage[4])

forcastUSDTarget = float(incooomSimulationResult_df.Results[0])
forcastklimaTarget = float(incooomSimulationResult_df.Results[1])
requiredklimaDailyIncooom = float(incooomSimulationResult_df.Results[2])
forcastDailyIncooom = float(incooomSimulationResult_df.Results[3])
requiredklimaWeeklyIncooom = float(incooomSimulationResult_df.Results[4])
forcastWeeklyIncooom = float(incooomSimulationResult_df.Results[5])

#####################################
# Styles & Colors
#####################################

NAVBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "color": "#518e55",
    #"background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "top": 0,
    "margin-top": '2rem',
    "margin-left": "18rem",
    "margin-right": "2rem",
    "color": "#518e55",
}


#####################################
# Create Auxiliary Components Here
#####################################

def nav_bar():
    """
    Creates Navigation bar
    """
    navbar = html.Div(
        [
            html.H4("Klima Playground Navigation", className="display-10", style={'textAlign': 'center'}),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Staking: Playground", href="/page1", active="exact", external_link=True),
                    dbc.NavLink("Staking: Learn", href="/page2", active="exact", external_link=True)
                ],
                pills=True,
                vertical=True
            ),
        ],
        style=NAVBAR_STYLE,
    )
    return navbar


klimaGrowthForecastChart_Controls1 = [
    dbc.CardHeader("Klima Growth Simulator controls"),
    dbc.CardBody(
        [
            dcc.Input(
                id = 'valIn',
                type = 'number',
                placeholder= 'days',
            ),
            html.Br(),
            html.Div(id='valOut'),
        ]
    ),
]

# graph 1
#klimaGrowthForecastChart_Sim1 = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
klimaGrowthForecastChart_Sim1 = go.Figure()
klimaGrowthForecastChart_Sim1.add_trace(go.Scatter(x=klimaGrowthResult_df.Days, y=klimaGrowthResult_df.Total_klimas, name='(3,3) ROI  ', fill=None ))
klimaGrowthForecastChart_Sim1.add_trace(go.Scatter(x=klimaGrowthResult_df.Days, y=klimaGrowthResult_df.Profit_Adjusted_Total_klimas, name='(3,3) Profit adjusted ROI  '))
klimaGrowthForecastChart_Sim1.add_trace(go.Scatter(x=klimaGrowthResult_df.Days, y=klimaGrowthResult_df.DCA_Adjusted_Total_klimas,name='(3,3) DCA adjusted ROI  '))
klimaGrowthForecastChart_Sim1.add_trace(go.Scatter(x=klimaGrowthResult_df.Days, y=klimaGrowthResult_df.Min_klimaGrowth, name='Min Growth Rate  ', fill=None, ))
klimaGrowthForecastChart_Sim1.add_trace(go.Scatter(x=klimaGrowthResult_df.Days, y=klimaGrowthResult_df.Max_klimaGrowth, name='Max Growth Rate  ', fill=None, ))

klimaGrowthForecastChart_Sim1.update_layout(autosize=True, showlegend=True, margin=dict(l=20, r=30, t=10, b=20))
klimaGrowthForecastChart_Sim1.update_layout({'paper_bgcolor': 'rgba(0,0,0,0)', 'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
klimaGrowthForecastChart_Sim1.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01), xaxis_title = "Days", yaxis_title = "Total klimas")
klimaGrowthForecastChart_Sim1.update_xaxes(showline=True, linewidth=0.1, linecolor='#31333F', showgrid=False, gridwidth=0.01,mirror=True)
klimaGrowthForecastChart_Sim1.update_yaxes(showline=True, linewidth=0.1, linecolor='#31333F', showgrid=False, gridwidth=0.01,mirror=True, zeroline=False)

klimaGrowthForecastChart_Explanation1 = [
    dbc.CardHeader("Results Explanation"),
    dbc.CardBody(
        [
            dcc.Markdown(f''' 
        The (3,3) Profit adjusted ROI trend line shows you the adjusted KLIMA growth if you decide to sell a Percentage of your KLIMA at a fixed interval (For example, 5% every 30 days).
        
        The Min Growth Rate shows you the estimated KLIMA growth rate if the APY was on the minimum APY of the current tier dictated by the OIP-18 Reward Rate Framework.
        
        The MAX Growth Rate shows you the estimated KLIMA growth rate if the APY was on the Maximum APY of the current tier dictated by OIP-18 Reward Rate Framework.
            '''),
        ]
    ),
]



klimaGrowthForecastResultCard_Sim1 = html.Div(
    [
        dcc.Markdown('''# Staking Rewards Forecast'''),
        dbc.Alert(f'''Days until desired USD value: {forcastUSDTarget}''', color="success"),
        dbc.Alert(f'''Days until desired Klima value: {forcastklimaTarget}''', color="success"),
        dbc.Alert(f'''Days until desired daily staking rewards: {forcastDailyIncooom}''', color="success"),
        dbc.Alert(f'''Days until desired weekly staking rewards: {forcastWeeklyIncooom}''', color="success"),

    ]
)

klimaGrowthForecastResultCard_Sim2 = html.Div(
    [
        dbc.Alert(dcc.Markdown(f'''
            - Daily ROI: {dailyROI},
            - 5 Day ROI: {fiveDayROI},
            - 7 Day ROI: {sevenDayROI},
            - 1 Month ROI: {oneMonthROI}
            '''), color="success"),
    ]
)

klimaGrowthForecastResultCard_Sim3 = html.Div(
    [
        dcc.Markdown(f'''
        # Staking Rewards Forecast Explanation
        Based on your control parameters, these are the predicted outcomes assuming market stability and your parameters 
        - It would take {forcastUSDTarget} days until you accumulate enough KLIMA worth your target.  
        - It would take {forcastklimaTarget} days until you accumulate your desired KLIMA**. 
        - To start earning your daily rewards, you will need {requiredklimaDailyIncooom} KLIMA, and based on the APY% you entered; it would take {forcastDailyIncooom} days to reach your goal. 
        - To start earning your weekly rewards, you will need {requiredklimaWeeklyIncooom} KLIMA, and based on the APY% you entered; it would take {forcastWeeklyIncooom} days to reach your goal. 
        '''),
    ]
)


klimaLearn_stakingStrategy = [
    dbc.CardHeader("The (3,3) Strategy"),
    dbc.CardBody(
        [
            dcc.Markdown('''
                    **Staking is the primary value accrual strategy of Olympus, we call staking (3,3)**. Stakers stake their klima on the Olympus website to earn rebase rewards. 
                            The rebase rewards come from the proceeds of bond sales, and can vary based on the number of klima staked in the protocol and the reward rate set by the protocol.

                    **Staking is a passive, long-term strategy**. The increase in your stake of klima translates into a constantly falling cost basis converging on zero. 
                            This means even if the market price of klima drops below your initial purchase price, given a long enough staking period, the increase in your staked klima balance should eventually outpace the fall in price.

                    **When you stake, you lock klima and receive an equal amount of sklima**. Your sklima balance compounds  automatically at the end of every epoch. 
                            sklima is transferable and therefore composable with other DeFi protocols such as Rari or Abracadabra. 
                            sklima continues to rebase while being used in other DeFi protocols or even in your hardware wallet.

                    **When you unstake, you burn sklima and receive an equal amount of klima**. Unstaking means the user will forfeit the upcoming rebase reward.
                             Note that the forfeited reward is only applicable to the unstaked amount; the remaining staked klima (if any) will continue to receive rebase rewards.
                    ''')
        ]
    ),
]

klimaLearn_stakingStrategy2 = [
    dbc.CardHeader("What is Staking Playground?"),
    dbc.CardBody(
        [
            dcc.Markdown('''
                **(3,3) Playground is a simulator for staking, and reward strategies**
                Use this simulator to forecast:
                - ROI at current and future reward yield percent
                - OHM growth over time
                - OHM and USD value over time
                
                Also, use this simulator to strategize:
                - Required staked OHM to reach desired daily staking rewards
                - Time until you are earning your desired daily staking rewards
                - Required staked OHM to reach desired weekly staking rewards
                - Time until you are earning your desired weekly staking rewards
                    ''')
        ]
    ),
]


#####################################
# Create Page Layouts Here
#####################################

### Layout 1 This is the layout for the Staking Playground page
layout1 = html.Div([
    html.H2("Playground: Staking"),
    html.Hr(),
    # create bootstrap grid 1Row x 2 cols
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                # create tabs
                                dbc.Tabs(
                                    [
                                        # graphs will go here eventually using callbacks
                                        dbc.Tab(
                                            [
                                            dbc.Row([dbc.Col(dcc.Graph(figure=klimaGrowthForecastChart_Sim1, id='graph'), width=8),
                                                     dbc.Col(dbc.Card(klimaGrowthForecastChart_Controls1, color="success", outline=True), width=4)]),

                                            dbc.Row([dbc.Col(dbc.Card(klimaGrowthForecastChart_Explanation1, color="success", outline=True), width="auto")]),

                                            dbc.Row([html.Div([
                                                html.H6("Change the value in the text box to see callbacks in action!"),
                                                html.Div(["Input: ",dcc.Input(id='my-input', value='initial value', type='text')]),
                                                html.Br(),
                                                html.Div(id='my-output'),
                                            ])])
                                            ],
                                            label='Klima Growth Forecast', tab_id='klimaGrowthForecast_Tab'),

                                        dbc.Tab(
                                            [
                                            dbc.Row([dbc.Col(klimaGrowthForecastResultCard_Sim1, width=10),]),
                                            dbc.Row([dbc.Col(klimaGrowthForecastResultCard_Sim3, width="auto"),]),
                                            ],
                                            label='Klima Rewards Forecast', tab_id='klimaRewardsForecast_Tab'),
                                    ],
                                    id="tabs",
                                    active_tab='klimaGrowthForecast_Tab',
                                ),
                                html.Div(id="tab-content", className="p-4")
                            ]
                        ),
                    ],
                    width=12  # half page
                ),
            ],
        ),
    ]),
])

### Layout 2 This is the layout for the Staking Learn page
layout2 = html.Div(
    [
        html.H2('Playground: Staking'),
        html.Hr(),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(klimaLearn_stakingStrategy,width=8),
                        dbc.Col(
                            [
                                html.Img(src=app.get_asset_url('klimaStakingStrategyImage.png'), style={'height':'80%', 'width':'100%'}),
                            ],
                        )
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url('klimaStakingStrategyImage2.png'),style={'height': '80%', 'width': '100%'}),width=4),
                        dbc.Col(klimaLearn_stakingStrategy2, width=8),
                    ]
                ),
            ]
        )
    ])