from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from ..app import app
from ..components import bonding_guides as b_g
from ..components.disclaimer import short_disclaimer_row

# Build the layout for the app. Using dash bootstrap container here instead of the standard html div.
# Container looks better
layout = dbc.Container([
    html.Div([
        dbc.Tabs([
            dbc.Tab(label='Guide',
                    label_style={'background': '#02C132',
                                 'fontSize': '20px', 'color': 'black'},
                    tab_style={'background': '#02C132',
                               'marginLeft': 'auto'},
                    active_tab_style={'background': '#02C132', 'fontSize': '20px', 'font-weight': 'bold'},
                    active_label_style={'color': '#ffffff'},
                    tab_id='bonding_guide_tab',
                    children=[
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(dbc.Label('Bonding',
                                                      className="learning_hub_category_topic"),
                                            xs=12, sm=12, md=12, lg=6, xl=6),
                                ]),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Card([
                                            dbc.CardHeader('Learn the fundamentals of Bonding on KlimaDAO',
                                                           className='learning_hub_category_deck_topic'),
                                            dbc.CardBody([
                                                dbc.Row([
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('What is bonding?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(b_g.what_is_bonding_intro,
                                                                            style={'text-align': 'center'}),
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(dbc.ModalTitle('What is bonding?')),
                                                                    dbc.ModalBody([
                                                                        b_g.what_is_bonding
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='what_is_staking_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='what_is_staking_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='what_is_staking_btn_open',
                                                                               n_clicks=0,
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('Why should I bond?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col(
                                                                        b_g.why_should_i_bond_intro,
                                                                        style={'text-align': 'center'}
                                                                    )
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle('Why should I bond?')),
                                                                    dbc.ModalBody([
                                                                        b_g.why_should_i_bond
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='why_should_i_stake_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='why_should_i_stake_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               id='why_should_i_stake_btn_open',
                                                                               color='link',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),
                                                            )
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('How can I bond?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col([
                                                                        b_g.how_can_i_bond_intro
                                                                    ], style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle('How can I bond?')),
                                                                    dbc.ModalBody([
                                                                        b_g.how_can_i_bond
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='how_can_i_stake_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='how_can_i_stake_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                )
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               color='link',
                                                                               id='how_can_i_stake_btn_open',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                )),
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3),
                                                    dbc.Col([
                                                        dbc.Card([
                                                            dbc.CardBody([
                                                                dbc.Row(
                                                                    dbc.Label('Why should the Treasury Bond?',
                                                                              className='learning_hub_category'
                                                                                        '_card_topic')
                                                                ),
                                                                dbc.Row(
                                                                    dbc.Col([
                                                                        b_g.why_should_treasury_bond_intro
                                                                    ], style={'text-align': 'center'})
                                                                ),
                                                                dbc.Modal([
                                                                    dbc.ModalHeader(
                                                                        dbc.ModalTitle(
                                                                            'Why should the Treasury Bond?')),
                                                                    dbc.ModalBody([
                                                                        b_g.why_should_treasury_bond
                                                                    ]),
                                                                    dbc.ModalFooter(
                                                                        dbc.Button(
                                                                            'close',
                                                                            id='staking_dynamics_btn_close',
                                                                            className='ms-auto',
                                                                            n_clicks=0,
                                                                        )
                                                                    )
                                                                ],
                                                                    id='staking_dynamics_modal_body',
                                                                    scrollable=True,
                                                                    is_open=False,
                                                                ),
                                                            ], className='align-self-center'),
                                                            dbc.CardFooter(
                                                                dbc.Row(
                                                                    dbc.Button('Learn more',
                                                                               color='link',
                                                                               id='staking_dynamics_btn_open',
                                                                               style={'color': '#0BA1FF',
                                                                                      'padding': '10px'}),
                                                                ),)
                                                        ], className='simulator_hub_card',
                                                            style={'height': '100%', 'width': '100%'})
                                                    ], xs=12, sm=12, md=12, lg=3, xl=3),
                                                ])
                                            ]),
                                        ], outline=False, color='#202020', style={"height": "100%", "width": "100%"}),
                                        xs=12, sm=12, md=12, lg=12, xl=12, style={'padding': '10px'}),
                                ]),
                            ])
                        ]),
                    ]),
            dbc.Tab(label='Simulator',
                    label_style={'background': '#02C132',
                                 'fontSize': '20px', 'color': 'black'},
                    tab_style={'background': '#02C132',
                               'fontSize': '20px'},
                    active_tab_style={'background': '#02C132', 'fontSize': '20px', 'font-weight': 'bold'},
                    active_label_style={'color': '#ffffff'},
                    tab_id='bonding_simulator_tab',
                    children=[
                        dbc.Row([
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('(4,4) Simulation parameters',
                                               className='learning_hub_category_deck_topic'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Label('Klima price (USDC)')
                                        ]),
                                        dbc.Col([
                                            dbc.Label('Starting amount of Klima (Units)')
                                        ]),
                                    ], style={'padding': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(
                                                id='klima_price',
                                                placeholder='1000',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=800,
                                                className="input_box_number",
                                                style={'color': 'white'})]),
                                        dbc.Col([
                                            dbc.Input(
                                                id='initial_klima',
                                                placeholder='1',
                                                type='number',
                                                min=1,
                                                step=0.001,
                                                debounce=True,
                                                value=10,
                                                className="input_box_number",
                                                style={'color': 'white'})]),
                                    ], style={'padding': '0px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Label('Bond ROI (%)'),
                                        ]),
                                        dbc.Col([
                                            dbc.Label('Rebase Rate (%)'),
                                        ]),
                                    ], style={'padding-top': '20px'}),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(
                                                id='bond_roi',
                                                placeholder='5',
                                                type='number',
                                                step=0.001,
                                                debounce=True,
                                                value=5,
                                                className="input_box_number",
                                                style={'color': 'white'}),
                                        ]),
                                        dbc.Col([
                                            dbc.Input(
                                                id='reward_yield',
                                                placeholder='0.5',
                                                type='number',
                                                step=0.001,
                                                debounce=True,
                                                value=0.5,
                                                className="input_box_number",
                                                style={'color': 'white'}),
                                        ])
                                    ], style={'margin-top': '0px'}),
                                ])
                            ], outline=False, color='#202020', style={"height": "100%", "width": "auto",
                                                                      'border-color': '#00cc33'})),
                        ], style={'padding': '10px'}),
                        dbc.Row([
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('(3,3) and (4,4) Growth comparison',
                                               className='learning_hub_category_deck_topic'),
                                dbc.CardBody([
                                    dcc.Graph(id='graph2', style={"height": "100%", "width": "100%"}),
                                ], style={"height": "100%", "width": "100%"})
                            ], outline=False, color='#202020', style={"height": "100%", "width": "auto",
                                                                      'border-color': '#00cc33'}),
                                xs=12, sm=12, md=12, lg=8, xl=8),
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('Growth Comparison Summary',
                                               className='learning_hub_category_deck_topic'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Label('Max (3,3) ROI (Klima)', className='bonding_roi_card_topic'),
                                        html.Div(className="bonding_roi_card_metrics_secondary",
                                                 id='max_33_growth'),
                                    ], className='text-center'),
                                    dbc.Row([
                                        dbc.Label('Max (4,4) ROI (Klima)', className="bonding_roi_card_topic"),
                                        html.Div(className="bonding_roi_card_metrics_secondary",
                                                 id='max_44_growth'),
                                    ], className='text-center'),
                                    dbc.Row([
                                        dbc.Label('Bonus Klima', className="bonding_roi_card_topic"),
                                        html.Div(className="bonding_roi_card_metrics_secondary",
                                                 id='bonus_gained'),
                                    ], className='text-center')
                                ])
                            ], outline=False, color='#202020', style={"height": "100%", "width": "auto",
                                                                      'border-color': '#00cc33'}))
                        ], style={'padding': '10px'}),
                        dbc.Row([
                            dbc.Col(
                                dbc.Card([
                                    dbc.CardHeader('(3,3) and (4,4) ROI Comparison',
                                                   className='learning_hub_category_deck_topic'),
                                    dbc.CardBody([
                                        dcc.Graph(id='graph3', style={"height": "100%", "width": "100%"}),
                                    ], style={"height": "100%", "width": "100%"})
                                ], outline=False, color='#202020', style={"height": "100%", "width": "auto",
                                                                          'border-color': '#00cc33'}),
                                xs=12, sm=12, md=12, lg=8, xl=8),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardHeader('(3,3) and (4,4) ROI Summary',
                                                   className='learning_hub_category_deck_topic'),
                                    dbc.CardBody([
                                        dbc.Row(
                                            dbc.Label('(3,3) ROI (%)', className='bonding_roi_card_topic'),
                                        ),
                                        dbc.Row(
                                            html.Div(className="bonding_roi_card_metrics_secondary",
                                                     id='33_roi'),
                                        ),
                                        dbc.Row(
                                            dbc.Label('Bond ROI (%)', className="bonding_roi_card_topic"),
                                        ),
                                        dbc.Row(
                                            html.Div(className="bonding_roi_card_metrics_secondary",
                                                     id='bonding_roi'),
                                        ),
                                        dbc.Row(
                                            dbc.Label('Max (4,4) ROI (%)', className="bonding_roi_card_topic"),
                                        ),
                                        dbc.Row(
                                            html.Div(className="bonding_roi_card_metrics_secondary",
                                                     id='max_44_roi'),
                                        ),
                                    ])
                                ], outline=False, color='#202020', style={"height": "100%", "width": "auto",
                                                                          'border-color': '#00cc33'})],
                                xs=12, sm=12, md=12, lg=4, xl=4),
                        ], style={'padding': '10px'}),
                        dbc.Row([
                            dbc.Col(dbc.Label('Results', className='learning_hub_category_topic'))
                        ], className='learning_hub_category_topic'),
                        dbc.Row([
                            dbc.Col(dbc.Card([
                                dbc.CardHeader('Expanded explanations',
                                               className='learning_hub_category_deck_topic'),
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.CardGroup([
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Simple staking vs Bond-Stake Growth Chart',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown('''
                                This chart contains two trend lines, the simple staking Klima Growth and bond-stake
                                strategy Klima Growth throughout the vesting period (In KlimaDAO, the vesting period
                                is 15 epochs, equivalent to 5 days).

                                The bond-stake strategy Klima growth trend line depicts the Klima growth based on
                                claim and stake frequency throughout the vesting period.

                                As learned on the Bond guide page, bonding allows purchasing Klima at
                                a discount from the protocol.

                                Bonding provides an opportunity to acquire more Klimas when compared to market
                                buying.

                                Bonding yields can be enhanced by claiming and staking vested Klimas as they become
                                available to you.

                                 Please see the ROI comparison chart for details on claiming/staking frequency
                                 effects. The simple staking Klima growth trend line depicts Klima growth
                                 throughout the same vesting period.
                                                        ''', id='chart_results_explanation'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='emission_card_style_v3'),
                                                dbc.Card([
                                                    dbc.CardBody([
                                                        dbc.Row(
                                                            dbc.Label('Simple staking vs Bond-Stake ROI Comparison',
                                                                      className='learning_hub_category_card_topic'),
                                                        ),
                                                        dbc.Row(
                                                            dcc.Markdown(
                                                                '''
                                    This chart contains two trend lines, the simple staking Klima Growth and bond-stake
                                    strategy Klima ROI throughout the vesting period (In KlimaDAO, the vesting period is
                                    15 epochs, equivalent to 5 days).

                                    The (4,4) ROI trend line depicts the bonding ROI based on claim/stake frequency
                                    throughout the vesting period.

                                    For example, the highest ROI could be achieved by claiming and staking vested
                                    depending on your control parameters.

                                    There might also be scenarios where it is not profitable to claim and stake at all.

                                    There could be many claim and stake combinations; the chart predicts the best
                                    possible combination.

                                    The (3,3) ROI trend line depicts plain staking ROI throughout the same
                                    vesting period.
                                                                ''',
                                                                id='equivalency_results_explanation'),
                                                        ),
                                                    ], className='align-self-center')
                                                ], className='emission_card_style_v3')
                                            ]),
                                        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'height': "100%",
                                                                                     'padding': '10px'}),
                                    ]),
                                ]),
                            ], outline=False, color='#2A2A2A',
                                style={"height": "100%", 'width': '100%'}),
                                xs=12, sm=12, md=12, lg=12, xl=12)
                        ], className="mb-5"),
                    ]),
        ], id='tabs', active_tab='bonding_guide_tab', className='mb-2'),
        html.Footer(short_disclaimer_row(), className='footer_style', style={'background-color': '#202020'})
    ], className='center_2'),
], id='page_content', fluid=True)  # Responsive ui control


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
# region Description: Function to calculate Klima growth over time
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
    # Calculate the rebase rate and Current ARY (next epoch rebase pulled from hippo data source)
    reward_yield = reward_yield / 100
    # rebase_const = 1 + reward_yield  # calculate a constant for use in ARY calculation
    # user_apy = rebase_const ** 1095  # current ARY equation
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
