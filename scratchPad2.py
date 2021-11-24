# Import all necessary libraries : User interface components
import dash
import dash_core_components as dcc # Dash components we use dash for ui design
import dash_html_components as html # Dash html components
import dash_bootstrap_components as dbc # bootstrap!!
from dash.dependencies import Input, Output, State, ClientsideFunction # Dash i/o components
import dash_table as dt # Dash table components
import dash_table.FormatTemplate as FormatTemplate # dash table formatter

# Import all necessary libraries Maths, arrays, data tables, plots
import math  # Needed for basic math operations\n",
import pandas as pd  # Needed fpr dataframe creation and operations\n",
import numpy as np  # Needed for array manipulations\n",
from itertools import islice  # Needed for more complex row and coloumn slicing\n",
import matplotlib.pyplot as plt  # Needed for quickly ploting results"
import pathlib  # url management
import plotly.express as px  # cleaner graphs
import plotly.graph_objects as go  # cleaner graphs

# Coingecko API
from pycoingecko import CoinGeckoAPI

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css" # Nice font for out UI design
external_stylesheets = [dbc.themes.SPACELAB, FONT_AWESOME]

footer = html.Div(
    dcc.Markdown(
        ''' Klima Playground is intended solely as general information for educational
        and entertainment purposes only and is not a substitute for professional advice and
        services from qualified financial services providers familiar with your financial
        situation. Questions? Suggestions? Please visit OlympusDAO discord server!
    '''),
    className="p-2 pl-5 pr-5 bg-light text-black",
)

playgroundIntroduction_text = dcc.Markdown(''' 
    (3,3) Playground is a simulator for staking, and incooom strategies.
    Use this simulator to:
    - Forcast ROI ar current and future reward yield percent
    - klima growth over time
    - klima and USD value over time

    We love the incooom, use this simulator to strategize:
    - Required staked klima to reach desired daily incooom
    - Count down until you are earning desired daily incooom
    - Required staked klima to reach desired weekly incooom
    - Count down until you are earning desired weekly incooom

    Learn more here: https://docs.olympusdao.finance/protocol-internals/market-dynamics
    ''')

equationReference_text = dcc.Markdown('''
    References to system governing equations can be found here
    [OlympusDAO Gitbook:](https://docs.olympusdao.finance/) The gitbook is a the best source for due diligence and understanding
    the mechanics of Olympus protocol
    ''')

simulationParameters_text = dcc.Markdown("""
    > **[Asset allocation (klima staked)](https://docs.olympusdao.finance/basics/staking)**, **[APY](https://docs.olympusdao.finance/basics/basics#what-is-apy)**,
    and **[Rebase Rate](https://docs.olympusdao.finance/basics/basics#what-is-a-rebase)** are main factors that determine returns and incooom over time.
    Play with the simulator and see how your starting klima affects your projected accured value over time.
    Additionally, use the incooom parameters to forcast daily and weekly incooom from (3,3) alone. 

    > Hover your mouse over the chart trend lines to see live feedback on Total klimas accumulated vs days.
    Use the slider and number input boxes to adjust your goals and see the results displayed on the incoom charts and table. 
    """)


incooomInput_card = html.Div(
    dbc.Card(
        [
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Current Price of klima :', style={'width': 275}),
                        addon_type="prepend"),
                    dbc.Input(id="klimaPrice",
                              placeholder="$1",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=1,
                              step=0.0001,
                              value=100,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Start Amount (klima) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='initialklimas',
                        placeholder='Min 0.01 klima',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=0.0001,
                        step=0.0001,
                        value=1,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Rebase Rate (%) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='rewardYield',
                        placeholder='0.4583',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=0.0019,
                        max=0.4583,
                        step=0.0001,
                        value=0.3058,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Desired Target (USD) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='desiredUSDTarget',
                        placeholder='10000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=1,
                        step=0.0001,
                        value=10000,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Desired Target (klima) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='desiredklimaTarget',
                        placeholder='1000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=1,
                        step=0.0001,
                        value=100,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Desired Daily Incooom (USD) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='desiredDailyIncooom',
                        placeholder='1000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=1,
                        step=0.0001,
                        value=1000,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(
                        dbc.InputGroupText('Desired Weekly Incooom (USD) :',
                                           style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='desiredWeeklyIncooom',
                        placeholder='1000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=1,
                        step=0.0001,
                        value=100,
                    ),
                ],
                className='mb-3',
            ),
        ],
        body=True,
        className='mt-4',
    ))


introLearn_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("Welcome to (3,3) Playground", ),
            dbc.CardBody(playgroundIntroduction_text),
        ],
        outline=True,
        className="mt-4",
    ))

simulationParameters_card = html.Div(
    dbc.Card(
        dbc.CardBody(
            html.Div(
                html.Div(simulationParameters_text, className='ml-3 mt-2'), )),
        className='mt-4',
    ))

bondingIntroduction_text = dcc.Markdown(''' 
    Bonding is the process of locking in a fixed reward in klima. You trade in DAI for klima at a discount
    and the klima is vested linearly over a period of 5 days.

    As a bonder, you win if price of klima increases during your vesting period; when this happens you benefits the
    discounted on klima and the increase in price. You also win if price remains flat during the vesting period.
    This is becuase profits are still gained from the discount.

    As a bonder, you loose if price of klima decreases during your vesting period. If this happens, you will have to 
    decide between klima and SLP (whichever is worth more). 

    **So what is (4,4) and what does it have to do with Bonding?** 
    The (4,4) strategy is a maximizing strategy that combines the benefits of staking (3,3) and bonding (1,1). 
    (4,4) simply means staking available klimaS during the vesting period to capture staking rewards during the vesting period.

    Use this simulator to strategize (4,4) profitability. 

    * This is a far more complex and active strategy when compared to (3,3). Please ensure you understand the system mechanics completely*

    Use this simulator to:
    - Forcast additional gains from using (4,4) compared to (3,3)
    - Forcast additional gains from staking bonding emissions every epoch
    - Forcast additional gains from staking bonding emissions once a day
    - Forcast additional gains from staking bonding emissions on day 2.5
    - klima growth over time with (4,4) strategy

    Learn more here: https://docs.olympusdao.finance/protocol-internals/market-dynamics

    ''')

bondingsimulationParameters_text = dcc.Markdown("""
    > **[Asset allocation (klima staked)](https://docs.olympusdao.finance/basics/staking)**, **[Gas Price](https://ethereum.org/en/developers/docs/gas/)**,
    Prices of ETH and klima, **[Bond ROI](https://docs.olympusdao.finance/references/equations#bonding)**, **[Rebase Yields](https://docs.olympusdao.finance/basics/basics#what-is-a-rebase)** and Network Gas Fees** 
    are main factors that determine (4,4) gains over time.
    Play with the simulator and find the parameters that maximize profitability.
    Additionally, use the chart provided to compare (3,3) gains with (4,4) gains. 

    > Hover your mouse over the chart trend lines to see live feedback on Total klimas accumulated vs days.
    Use the slider and number input boxes to adjust parameters and see the results displayed. 
    """)

bondingincooomInput_card = html.Div(
    dbc.Card(
        [
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Discounted klima Price (USD) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='discountedklimaPrice',
                        placeholder='1 USD',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=0.0001,
                        step=0.0001,
                        value=1,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Amount Bonded (USD) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='amountUSDBonded',
                        placeholder='1',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=0.0001,
                        step=0.0001,
                        value=0.3,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Current Price of ETH (USD) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='priceofETH',
                        placeholder='10000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=1,
                        step=0.0001,
                        value=10000,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Gas Price (ETH) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='gasPrice',
                        placeholder='1000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=1,
                        step=0.0001,
                        value=100,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Bond ROI% :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='bondROI',
                        placeholder='1000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=0.0001,
                        step=0.0001,
                        value=1000,
                    ),
                ],
                className='mb-3',
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        'Rebase Rate (%) :', style={'width': 275}),
                        addon_type='prepend'),
                    dbc.Input(
                        id='bondRebaseRate',
                        placeholder='1000',
                        type='number',
                        persistence=True,
                        persistence_type='session',
                        min=0.0019,
                        max=0.4583,
                        step=0.0001,
                        value=0.3058,
                    ),
                ],
                className='mb-3',
            ),
        ],
        body=True,
        className='mt-4',
    ))

incooomResultsROI_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("% ROI based on % Reward Yield", ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Daily ROI (%) :", style={'width': 175}),
                        addon_type='prepend'),
                    dbc.Input(id="dailyROI_P",
                              placeholder="0.01",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "5 Day % ROI (%) :", style={'width': 175}),
                        addon_type='prepend'),
                    dbc.Input(id="fivedayROI_P",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "7 Day % ROI (%) :", style={'width': 175}),
                        addon_type='prepend'),
                    dbc.Input(id="sevendayROI_P",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "1 Month % ROI (%) :", style={'width': 175}),
                        addon_type='prepend'),
                    dbc.Input(id="monthlyROI_P",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "1 Year % ROI (%) :", style={'width': 175}),
                        addon_type='prepend'),
                    dbc.Input(id="annualROI_P",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
        ],
        body=True,
        className="mt-4",
    ))

incooomResultsForcast_card = html.Div(
    dbc.Card(
        [
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Days to reach desired USD Target :",
                        style={'width': 375}),
                        addon_type='prepend'),
                    dbc.Input(id="forcastUSDTarget",
                              placeholder="10",
                              type="number",
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Days to reach desired klima Target :",
                        style={'width': 375}),
                        addon_type='prepend'),
                    dbc.Input(id="forcastklimaTarget",
                              placeholder="10",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Days to reach desired daily Incooom :",
                        style={'width': 375}),
                        addon_type='prepend'),
                    dbc.Input(id="forcastDailyIncooom",
                              placeholder="10",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Required klima for desired Incooom",
                        style={'width': 375}),
                        addon_type='prepend'),
                    dbc.Input(id="requiredklimaDailyIncooom",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Days to reach desired weekly Incooom :",
                        style={'width': 375}),
                        addon_type='prepend'),
                    dbc.Input(id="forcastWeeklyIncooom",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon(dbc.InputGroupText(
                        "Required klima for desired weekly Incooom :",
                        style={'width': 375}),
                        addon_type='prepend'),
                    dbc.Input(id="requiredklimaWeeklyIncooom",
                              placeholder="0.01%",
                              type="number",
                              persistence=True,
                              persistence_type="session",
                              min=0,
                              step=0.0001,
                              value=0.0001,
                              disabled=True),
                ],
                className="mb-3",
            ),
        ],
        body=True,
        className="mt-4",
    ))

bondingLearn_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("Welcome to (4,4) Playground", ),
            dbc.CardBody(bondingIntroduction_text),
        ],
        outline=True,
        className="mt-4",
    ))

bondingsimulationParameters_card = html.Div(
    dbc.Card(
        dbc.CardBody(
            html.Div(
                html.Div(bondingsimulationParameters_text,
                         className='ml-3 mt-2'), )),
        className='mt-4',
    ))

tabs = html.Div(
    dbc.Tabs(
        [
            dbc.Tab(
                introLearn_card,
                tab_id='introLearn_tab',
                label='Learn: The (3,3) Strategy',
                label_style={
                    "font-size": "120%",
                    "width": "250px"
                },
            ),
            dbc.Tab(
                [simulationParameters_card, incooomInput_card],
                tab_id='simulationParameters_tab',
                label='Play',
                label_style={
                    "font-size": "150%",
                    "width": "125px"
                },
            ),
        ],
        id='tabs',
        active_tab='introLearn_tab',
    ),
    style={"minHeight": "800px"},)

bondingtabs = html.Div(
    dbc.Tabs(
        [
            dbc.Tab(
                bondingLearn_card,
                tab_id='bondingLearn_tab',
                label='Learn: The (4,4) Strategy',
                label_style={
                    "font-size": "120%",
                    "width": "250px"
                },
            ),
            dbc.Tab(
                [bondingsimulationParameters_card, bondingincooomInput_card],
                tab_id='bondingsimulationParameters_tab',
                label='Play',
                label_style={
                    "font-size": "150%",
                    "width": "125px"
                },
            ),
        ],
        id='bondingtabs',
        active_tab='bondingLearn_tab',
    ),
    style={"minHeight": "800px"},)

external_stylesheets = [dbc.themes.SPACELAB, FONT_AWESOME]
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server = app.server
app.layout = dbc.Container(
    [

        # -------------------------------------------Row 1 = Main Header Begin-----------------------------------------
        # Title row
        dbc.Row(
            dbc.Col(html.H1("OlympusDAO Playground",
                            className="text-center bg-light text-black p-2"),
                    width=12)),
        # -------------------------------------------Row 1 = Main Header End-------------------------------------------

        # -------------------------------------------Row 2 = (3,3) Tab and klima growth chart Begin----------------------
        # Instruction and klima growth chart row
        dbc.Row(
            [
                # Welcome message and Instructions column
                dbc.Col(
                    tabs,
                    width={
                        "size": 4,
                        "order": 1
                    },
                    className="mt-4 border",
                ),
                # klima growth output column
                dbc.Col(
                    [
                        dcc.Graph(id='klimaGrowthChart', className='mb-2'),
                        # ROI output column
                        dbc.Row([
                            dbc.Col(incooomResultsROI_card, width=4),
                            dbc.Col(incooomResultsForcast_card, width=8),
                        ])
                    ],
                    width={
                        "size": 8,
                        "order": 2
                    },
                    className="pt-4 ",
                ),
            ],
            className='ml-4',
            align='center'),
        # -------------------------------------------Row 2 = (3,3) Tab and klima growth chart End----------------------

        # -------------------------------------------Row 3 = Bonding Header Begin-------------------------------
        # Title row
        dbc.Row(
            dbc.Col(html.H1("Bonding Simulator",
                            className="text-center bg-light text-black p-1"),
                    width=12)),
        # -------------------------------------------Row 3 = Bonding Header End---------------------------------

        # -------------------------------------------Row 4 = Bonding Tabs and Results Begin---------------------
        # Instruction and klima growth chart row
        dbc.Row(
            [
                # Welcome message and Instructions column
                dbc.Col(
                    bondingtabs,
                    width={
                        "size": 4,
                        "order": 1
                    },
                    className="mt-4 border",
                ),
                # klima growth output column
                dbc.Col(
                    [
                        dcc.Graph(id='bondingAPYChart', className='mb-2'),
                    ],
                    width={
                        "size": 8,
                        "order": 2
                    },
                    className="pt-4 ",
                ),
            ],
            className='ml-4',
            align='center'),
        # -------------------------------------------Row 4 = Bonding Tabs and Results End-----------------------

        # ------------------------------Footer Begin------------------------------------------------------------
        dbc.Row(dbc.Col(footer, className='text-center mt-5')),
        # -------------------------------Footer End-------------------------------------------------------------

    ],
    fluid=True)

# Data frame to hold all required data point. Data required would be Epochs since rebase are distributed every Epoch
klimaGrowth_df = pd.DataFrame(np.arange(1096), columns=[
    'Epochs'
])  # In this case let's consider 1096 Epochs which is 365 days
klimaGrowth_df[
    'Days'] = klimaGrowth_df.Epochs / 3  # There are 3 Epochs per day so divide by 3 to get Days

# Data frame to hold OIP-18
# Start by creating a dictionary
oip18_dict = {'Total klima supply range min': ['0',
                                             '1,000,000',
                                             '10,000,000',
                                             '100,000,000',
                                             '1,000,000,000',
                                             '10,000,000,000',
                                             '100,000,000,000'],

              'Total klima supply range max': ['1,000,000',
                                             '10,000,000',
                                             '100,000,000',
                                             '1,000,000,000',
                                             '10,000,000,000',
                                             '100,000,000,000',
                                             '1,000,000,000,000'],

              'Min Reward Rate (%)': [0.3058,
                                      0.1587,
                                      0.1186,
                                      0.0458,
                                      0.0148,
                                      0.0039,
                                      0.0019],

              'Max Reward Rate (%)': [0.4583,
                                      0.3058,
                                      0.1587,
                                      0.1186,
                                      0.0458,
                                      0.0148,
                                      0.0039],

              'Min APY% (Assuming 90% Staked)': [10000,
                                                 1000,
                                                 500,
                                                 100,
                                                 25,
                                                 6,
                                                 3],

              'Max APY% (Assumung 90% Staked)': [100000,
                                                 10000,
                                                 1000,
                                                 500,
                                                 100,
                                                 25,
                                                 6],

              }
# Then convert to pandas data frame
oip18_dataFrame = pd.DataFrame(oip18_dict)

# Define callback to update the klimaGrowthChart. As user changes the initial staked klima, the chart updates dynamically
@app.callback(Output('klimaGrowthChart', 'figure'),
              Input("initialklimas", "value"), Input('rewardYield', 'value'))
# ================================================================================
# This function calculates and generates the klima growth over time using the initial staked klima as a starting point
def update_figure(initialklimas, rewardYield):

    # To Calculate the klima growth over 3000 Epochs or 1000 days, we loop through the exponential klima growth equation every epoch

    totalklimas = [
    ]  # create an empty array that will hold the componded rewards
    rewardYield = round(rewardYield / 100, 5)

    klimaStakedGrowth = initialklimas  # Initial staked klimas used to project growth over time
    # Initialize the for loop to have loops equal to number of rows or number of epochs
    for elements in klimaGrowth_df.Epochs:
        totalklimas.append(
            klimaStakedGrowth
        )  # populate the empty array with calclated values each iteration
        klimaStakedGrowth = klimaStakedGrowth * (
            1 + rewardYield)  # compound the total amount of klimas
    klimaGrowth_df[
        'Total_klimas'] = totalklimas  # Clean up and add the new array to the main data frame
    klimaGrowth_df.Days = np.around(
        klimaGrowth_df.Days, decimals=1
    )  # Python is funny so let's round up our numbers . 1 decimal place for days",
    klimaGrowth_df.Total_klimas = np.around(
        klimaGrowth_df.Total_klimas, decimals=3
    )  # Python is funny so let's round up our numbers . 3 decimal place for klimas"

    # ================================================================================

    return px.line(klimaGrowth_df,
                   x="Days",
                   y="Total_klimas",
                   render_mode="webgl",
                   title="Accumulated klimas")

# Define ROI callbacks to update the roi output objects and incooom forcasts.
@app.callback(Output('dailyROI_P', 'value'), Output('fivedayROI_P', 'value'),
              Output('sevendayROI_P', 'value'), Output('monthlyROI_P','value'),
              Output('annualROI_P', 'value'),
              Output('forcastUSDTarget', 'value'),
              Output('forcastklimaTarget', 'value'),
              Output('forcastDailyIncooom', 'value'),
              Output('requiredklimaDailyIncooom', 'value'),
              Output('forcastWeeklyIncooom', 'value'),
              Output('requiredklimaWeeklyIncooom', 'value'),
              Input("rewardYield", "value"), Input("initialklimas", "value"),
              Input("desiredUSDTarget", "value"),
              Input("desiredklimaTarget", "value"),
              Input("desiredDailyIncooom", "value"),
              Input("desiredWeeklyIncooom", "value"))
# ================================================================================
def update_Incooom(rewardYield, initialklimas, desiredUSDTarget,
                   desiredklimaTarget, desiredDailyIncooom,
                   desiredWeeklyIncooom):
    klimaPrice = 325
    klimaStakedInit = initialklimas
    rewardYield = round(rewardYield / 100, 5)
    rebaseConst = 1 + rewardYield
    # current staking %APY. Need to make this read from a source or user entry
    currentAPY = 17407 / 100

    # Let's get some ROI Outputs starting with the daily
    dailyROI = (
        1 + rewardYield
    )**3 - 1  # Equation to calculate your daily ROI based on reward Yield
    dailyROI_P = round(dailyROI * 100, 2)  # daily ROI in Percentage
    # ================================================================================

    # 5 day ROI
    fivedayROI = (1 + rewardYield)**(
        5 *
        3) - 1  # Equation to calculate your 5 day ROI based on reward Yield
    fivedayROI_P = round(fivedayROI * 100, 2)  # 5 day ROI in Percentage
    # ================================================================================

    # 7 day ROI
    sevendayROI = (1 + rewardYield)**(
        7 *
        3) - 1  # Equation to calculate your 7 day ROI based on reward Yield
    sevendayROI_P = round(sevendayROI * 100, 2)  # 7 day ROI in Percentage
    # ================================================================================

    # 30 day ROI
    monthlyROI = (1 + rewardYield)**(
        30 *
        3) - 1  # Equation to calculate your 30 day ROI based on reward Yield
    monthlyROI_P = round(monthlyROI * 100, 2)  # 30 day ROI in Percentage
    # ================================================================================

    # Annual ROI
    annualROI = (1 + rewardYield)**(
        365 *
        3) - 1  # Equation to calculate your annual ROI based on reward Yield
    annualROI_P = round(
        annualROI * 100,
        2)  # Equation to calculate your annual ROI based on reward Yield
    # ================================================================================

    # Let's create a nice looking table to view the results of our calculations. The table will contain the ROIs and the percentages
    roiData = [['Daily', dailyROI_P], ['5 Day', fivedayROI_P],
               ['7 Day', sevendayROI_P], ['1 Month', monthlyROI_P],
               ['1 Year', annualROI_P]]
    roiTabulated_df = pd.DataFrame(roiData, columns=['Cadence', 'Percentage'])
    roiDataTable = roiTabulated_df.to_dict('rows')
    columns = [{
        'name': i,
        'id': i,
    } for i in (roiTabulated_df.columns)]
    # ================================================================================
    # Days until you reach target USD by staking only
    forcastUSDTarget = round(
        (math.log(desiredUSDTarget / (klimaStakedInit * klimaPrice), rebaseConst) /
         3))
    # ================================================================================
    # Days until you reach target klima by staking only
    forcastklimaTarget = round(
        math.log(desiredklimaTarget / (klimaStakedInit), rebaseConst) / 3)
    # ================================================================================
    # Daily Incooom calculations
    # Required klimas until you are earning your desired daily incooom
    requiredklimaDailyIncooom = round(
        (desiredDailyIncooom / dailyROI) / klimaPrice)
    # Days until you are earning your desired daily incooom from your current initial staked klima amount
    forcastDailyIncooom = round(
        math.log((requiredklimaDailyIncooom / klimaStakedInit), rebaseConst) / 3)
    requiredUSDForDailyIncooom = requiredklimaDailyIncooom * klimaPrice
    # ================================================================================
    # Weekly Incooom calculations
    # Required klimas until you are earning your desired weekly incooom
    requiredklimaWeeklyIncooom = round(
        (desiredWeeklyIncooom / sevendayROI) / klimaPrice)
    # Days until you are earning your desired weekly incooom from your current initial staked klima amount
    forcastWeeklyIncooom = round(
        math.log((requiredklimaWeeklyIncooom / klimaStakedInit), rebaseConst) / 3)
    requiredUSDForWeeklyIncooom = requiredklimaWeeklyIncooom * klimaPrice
    # ================================================================================

    return dailyROI_P, fivedayROI_P, sevendayROI_P, monthlyROI_P, annualROI_P, forcastUSDTarget, forcastklimaTarget, forcastDailyIncooom, requiredklimaDailyIncooom, forcastWeeklyIncooom, requiredklimaWeeklyIncooom

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)