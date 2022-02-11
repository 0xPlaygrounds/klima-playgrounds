from dash import dcc
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import Input, Output, State, html
from app import app

# Lotties: Emil at https://github.com/thedirtyfew/dash-extensions
url_sunlight = "https://assets8.lottiefiles.com/packages/lf20_bknKi1.json"
url_earth = "https://assets10.lottiefiles.com/datafiles/xjh641xEDuQg4qg/data.json"
url5 = "https://assets8.lottiefiles.com/packages/lf20_q6y5ptrh.json"
url6 = "https://assets4.lottiefiles.com/packages/lf20_tN5Ofx.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

learn_card_1 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                        html.Button('What is KlimaDAO?', id='open_learn_card_1', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is KlimaDAO?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Klima DAO is a Decentralized Autonomous Organization to drive climate action,
via our carbon-backed, algorithmic currency- the KLIMA token.
As the protocol grows, Klima DAO will solve the critical problems of the carbon markets:
- **Illiquidity**: Carbon Credits come in many different varieties; carbon brokers and
middlemen are used by buyers and sellers, fragmenting the total liquidity of the market.
- **Opacity**: Trades occur often behind closed doors, allowing buyers to underbuy the market.
- **Inefficiency**: buying and retiring carbon credits comes with friction and barriers,
by utilizing the polygon ecosystem, it removes this friction for all users

In delivery of its objectives, Klima DAO will become the single biggest disruptor of the
carbon markets and set a precedent for a new monetary system backed by carbon.
Klima DAO will serve the web3 ecosystem by offering accountability for those that
contribute, rewards for stakeholders, and a stake in governance for those that participate.
Klima DAO was inspired by Olympus DAO. It was conceptualized and built by a
distributed pseudo-anonymous team.
Klima is DAO-governed by it's community. All decisions are formed by community members on
 the forum and made by KLIMA holders through snapshot voting.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_1',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_1",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': "102px"}
)
learn_card_2 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Why KlimaDAO?', id='open_learn_card_2', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is the point of KlimaDAO?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
                            1. Driven Climate Action:
                            Klima DAO incentivizes new supply of Base Carbon Tonnes (BCT) on the blockchain
                            through the KLIMA token. By driving demand into BCT, it incentivizes carbon offset
                            producers to produce more carbon credits, assisting the adoption of new carbon mitigating
                            or sequestering technology, and disincentivizes companies wanting to offset their carbon
                            footprint with only C.Cs, and forces them to perform environmentally friendly actions.
                            KLIMA is the first building block for unlocking the carbon economy — an economy where more
                            economic activity leads to an acceleration in planetary regeneration rather than more
                            amage to our planet. Before, monetary incentives and environmental incentives aren't
                            typically aligned.
                            2. Become a Carbon-Based Reserve Currency:
                            The KLIMA ecosystem and monetary policy are managed by the Klima DAO.
                            This way we guarantee transparent decision making and long-term stability.
                            In the long term, we can use this system to optimize stability, to transition to a global
                            unit of account and medium of exchange. Currently, in the short term, we're focused on
                            growth and wealth creation, to incentivize users to join the new wave of carbon currency.
                            3. Facilitate the Climate Market:
                            The current carbon (and the climate in general) markets are illiquid, fragmented,
                            inefficient, and opaque. Because of this, we feel that carbon tonnage is heavily
                             undervalued, and is forced down because of these issues. By eliminating these issues,
                             the true price can be achieved.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_2',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_2",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_3 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('What is Klima?', id='open_learn_card_3', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is Klima?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
                            KLIMA is an algorithmic carbon-backed currency,
                            inspired by [Olympus DAO](https://www.olympusdao.finance/) and their token mechanics.
                            KlimaDAO incentivises new supply of Base Carbon Tonnes (BCT) on the blockchain through
                            bonding with the Protocol. Each KLIMA token is backed at a 1:1 ratio with a BCT in the
                            treasury.

                            KlimaDAO leverages the [Toucan Protocol's](https://docs.toucan.earth/protocol/)
                            Carbon Bridge to retire real world Verified Carbon Units (VCUs) and convert them to a
                            tokenized form on the blockchain, VCUs can be verified from reputable carbon markets in a
                            transparent and traceable manner.  The credits are then absorbed through the protocols'
                            bonding mechanism, building a treasury of verified tokenized carbon reductions.
                            This increases the amount of carbon assets locked within the treasury, thereby
                            reducing supply on the open market and leading to price appreciation within the
                            Voluntary Carbon Markets.

                            In summary, Klima serves two main purposes:

                            1. It serves as a floating currency and a form of money backed at a 1:1 ratio by voluntary
                            carbon credits.

                            2. It is used to govern the protocol and confer voting power to influence decisions on
                            various policies including supply expansion mechanics.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_3',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_3",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_4 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('How do I participate?', id='open_learn_card_4', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('How do I participate in KlimaDAO?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
                            1. Klima DAO development:
                            Join the  Discord to become a Klimate and hear about Protocol developments.
                            Those who wish to be involved in Protocol Governance should also join the Discord
                            to be onboarded by a member of the team.
                            2. Participation in the carbon economy:
                            BCTs are the underlying asset within the KlimaDAO treasury and their flow into the treasury
                            underpins protocol growth. BCTs can be created from real-world Verified Carbon Units (VCUs)
                            via the Toucan Protocol. Bonders provide BCT LP or BCT tokens in exchange for discounted
                            KLIMA tokens after a fixed vesting period. Once KLIMA tokens are held, stakers stake
                            their KLIMA tokens in return for more KLIMA tokens.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_4',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_4",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_5 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('What is Staking?', id='open_learn_card_5', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is Staking?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
- Staking is the primary profit distribution mechanism of the protocol. It is designed
to be the primary mechanism of value accural for the majority of users.
For most, the best thing to do is to simply stake and compound the KLIMA acquired.

- Whenever the protocol has an excess of reserve per token, the protocol will mint
and distribute tokens to the stakers. The amount minted and distributed is controlled
by a variable called the reward rate.
The reward rate is the % percent supply that is rebased.

For a step by step guide on how to stake KLIMA, see the
[Community guide](https://klima-dao.notion.site/I-m-new-to-KLIMA-How-do-I-participate-bcf8881862e941a5b5550d1179e123f9)
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_5',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_5",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_6 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('What is Bonding?', id='open_learn_card_6', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is Bonding?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
What is Bonding?
Bonding is the process of trading assets to the protocol for KLIMA. The protocol will quote you an amount of KLIMA
 for your asset, and the vesting period for the trade. Today, the protocol takes in:

1. Reserve Assets: BCT (Base Carbon Tonnes)
2. Liquidity Assets: KLIMA/BCT and BCT/USDC sushiswap LP pairs.

Bonding allows you to buy KLIMA at a lower cost basis. Because the protocol can sell at a discount to the market
price (as it can mint KLIMA at IV),you are able to more cheaply buy KLIMA
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_6',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_6",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_7 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('What is Rebasing?', id='open_learn_card_7', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is Rebasing?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
                            KLIMA is an algorithmic carbon-backed currency,
                            inspired by [Olympus DAO](https://www.olympusdao.finance/) and their token mechanics.
                            KlimaDAO incentivises new supply of Base Carbon Tonnes (BCT) on the blockchain through
                            bonding with the Protocol. Each KLIMA token is backed at a 1:1 ratio with a BCT in the
                            treasury.

                            KlimaDAO leverages the [Toucan Protocol's](https://docs.toucan.earth/protocol/)
                            Carbon Bridge to retire real world Verified Carbon Units (VCUs) and convert them to a
                            tokenized form on the blockchain, VCUs can be verified from reputable carbon markets in a
                            transparent and traceable manner.  The credits are then absorbed through the protocols'
                            bonding mechanism, building a treasury of verified tokenized carbon reductions.
                            This increases the amount of carbon assets locked within the treasury, thereby
                            reducing supply on the open market and leading to price appreciation within the
                            Voluntary Carbon Markets.

                            In summary, Klima serves two main purposes:

                            1. It serves as a floating currency and a form of money backed at a 1:1 ratio by voluntary
                            carbon credits.
                            2. It is used to govern the protocol and confer voting power to influence decisions on
                            various policies including supply expansion mechanics.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_7',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_7",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_8 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Participant Goals?', id='open_learn_card_8', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Participant Goals?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Stakers care primarily about their KLIMA balance. While price is important in valuing their KLIMA and indicating
the market's perception of Klima DAO's utility and impact, it is not the main goal in the shorter-term.

**KLIMA is a long-term play, and maximizing holdings is the objective of stakers.**

A higher price of carbon will be achieved by increasing the quality of carbon removal projects, and creating a system
for producing carbon offsets at scale. A robust system will see a higher BCT price and a higher KLIMA price.

A smart staker cares about the long-term price exploration of BCT tokens and the quality of the TCO2s flowing into the
ecosystem.

Bonders care primarily about the On-chain Carbon Tonne supply and their KLIMA balance. Bonders have their KLIMA and
carbon assets locked in for a period of time, but can redeem KLIMA at a better rate than a staker by relinquishing
their BCTs to the treasury to lock it away indefinitely. Their carbon impact and KLIMA returns from bonding are
proportional to the amount bonded.

In the case where demand is greater than supply, purchasing BCTs and bonding them for new KLIMA will be cheaper
than purchasing KLIMA on the free market.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_8',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_8",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_9 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('What are Carbon Markets?', id='open_learn_card_9', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What are Carbon Markets?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Carbon markets are a greenhouse gas trading system implemented to reduce CO2 and other greenhouse gas emissions by
putting a price on releasing carbon in the form of carbon offsets, sometimes called carbon credits.

Carbon markets are “Cap and Trade” markets. In this system the number of carbon offsets are capped for a particular
entity; a company, government, etc… This allows the entity to release a set amount of emissions.
If the entity wants to exceed their set emission level they need to trade carbon offsets with other
entities who are not using their carbon offsets or face a fine.

Extra credits can be created if participants voluntarily reduce their emissions by using cleaner energy sources or
other pollution controls. Over time the cap for emissions will be slowly lowered making carbon offsets more scarce
and more expensive, creating an economic incentive for entities to voluntarily reduce their emissions.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_9',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    )
                ],
                    id="body_learn_card_9",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_10 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('What are Carbon Offsets?', id='open_learn_card_10', className='learn_card_btn')],
                    style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('What is a Carbon Offset?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
A carbon offset represents the removal of one tonne of carbon dioxide equivalent from the atmosphere or the avoidance
of one tonne of emissions.

The term “carbon dioxide equivalent” is used because there are multiple greenhouse gasses,
all with a different Global Warming Potential (GWP), which illustrates impacts of different greenhouse gasses.

For instance methane has a GWP 28 times that of CO2. This means a company would need 28 carbon offsets to
emit 1 tonne of methane.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_10',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_10",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_11 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Carbon Offsets and Renewable energy',
                                id='open_learn_card_11', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('How are carbon offsets and renewable energy different?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Renewable energy sources produce energy from natural sources, like wind or solar, with little to no carbon emissions.

Carbon offsets create a way to reduce the acceptable levels of current emissions over time, provide economic
incentive to reduce voluntarily and fund sources of renewable energy.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_11',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_11",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_12 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Carbon offsets and Climate change',
                                id='open_learn_card_12', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('How does carbon offsetting fight climate change?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Offsets are a valuable tool to cover hard-to-abate emissions, i.e., emissions which may be challenging to eliminate
with current technology. Purchased offsets lead to measurable and accountable emissions reductions.

One of the most powerful economic levers we have in the fight against climate change is pricing carbon.

Indirectly, the voluntary carbon market helps price-in the negative externalities of emitting greenhouse gases into
the atmosphere. As more actors decide to do this, the carbon price will increase steadily and eventually reach a point
where the price of offsets accurately accounts for economic and social costs. This is the fundamental role of the
infrastructure which Klima DAO is building.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_12',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_12",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_13 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Market Cap',
                                id='open_learn_card_13', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Market Cap')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Total KLIMA Supply multiplied by Price per KLIMA.

Price / KLIMA can be misleading. Market cap captures valuation better because of the high growth of KLIMA supply.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_13',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_13",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_14 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Circulating / Total Supply',
                                id='open_learn_card_14', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('How does carbon offsetting fight climate change?')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Total Supply = Total KLIMA minted to date.
Non-Circulating Supply = KLIMA held by DAO and KLIMA yet to be vested to the bonders
Circulating Supply = Total Supply minus Non-Circulating Supply

Staking rewards are only paid to Stakers in staked KLIMA (sKLIMA).
The DAO does not collect any of these staking rewards.
When a user purchases a bond, KLIMA will be minted and are vested to the bonders over a five-day period.
KLIMA that are still vesting count towards the total supply.
This ratio helps us see what % of the supply is held by the DAO and bond contracts.
                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_14',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_14",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_15 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Current Index',
                                id='open_learn_card_15', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Current Index')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
1 KLIMA staked on launch date (18 October 2021) would be equal to the value of the Current Index after all
rebases up to present.

Useful for stakers to note the index they bought in at. 
Stakers can track their index-adjusted value by using the index they bought at vs the current index.

                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_15',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_15",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)
learn_card_16 = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row([
                    html.Button('Percent KLIMA Staked',
                                id='open_learn_card_16', className='learn_card_btn')],
                        style={'justify-content': 'center', 'text-align': 'center', 'padding': '10px'}),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Percent KLIMA Staked')),
                    dbc.ModalBody(
                        dcc.Markdown(
                            '''
Number of KLIMA staked in the protocol divided by Circulating Supply

At the end of every epoch, a fixed number of KLIMA will be distributed among all stakers.
When the % of KLIMA staked in the protocol is high, each staker will receive less KLIMA. 
Conversely, if the % of KLIMA staked in the protocol is low, each staker will receive more KLIMA.

                            '''
                        ),
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            'close',
                            id='close_learn_card_16',
                            className='ms-auto',
                            n_clicks=0,
                        )
                    ),
                ],
                    id="body_learn_card_16",
                    scrollable=True,
                    is_open=False,
                ),
            ]
        ),
    ],
    className='emission_card_style_v2',
    style={'height': '102px'}
)


@app.callback(
    Output('body_learn_card_1', 'is_open'),
    [
        Input('open_learn_card_1', 'n_clicks'),
        Input('close_learn_card_1', 'n_clicks'),
    ],
    [State('body_learn_card_1', 'is_open')],
)
def toggle_modal1(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_2', 'is_open'),
    [
        Input('open_learn_card_2', 'n_clicks'),
        Input('close_learn_card_2', 'n_clicks'),
    ],
    [State('body_learn_card_2', 'is_open')],
)
def toggle_modal2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_3', 'is_open'),
    [
        Input('open_learn_card_3', 'n_clicks'),
        Input('close_learn_card_3', 'n_clicks'),
    ],
    [State('body_learn_card_3', 'is_open')],
)
def toggle_modal3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_4', 'is_open'),
    [
        Input('open_learn_card_4', 'n_clicks'),
        Input('close_learn_card_4', 'n_clicks'),
    ],
    [State('body_learn_card_4', 'is_open')],
)
def toggle_modal4(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_5', 'is_open'),
    [
        Input('open_learn_card_5', 'n_clicks'),
        Input('close_learn_card_5', 'n_clicks'),
    ],
    [State('body_learn_card_5', 'is_open')],
)
def toggle_modal5(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_6', 'is_open'),
    [
        Input('open_learn_card_6', 'n_clicks'),
        Input('close_learn_card_6', 'n_clicks'),
    ],
    [State('body_learn_card_6', 'is_open')],
)
def toggle_modal6(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_7', 'is_open'),
    [
        Input('open_learn_card_7', 'n_clicks'),
        Input('close_learn_card_7', 'n_clicks'),
    ],
    [State('body_learn_card_7', 'is_open')],
)
def toggle_modal7(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_8', 'is_open'),
    [
        Input('open_learn_card_8', 'n_clicks'),
        Input('close_learn_card_8', 'n_clicks'),
    ],
    [State('body_learn_card_8', 'is_open')],
)
def toggle_modal8(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_9', 'is_open'),
    [
        Input('open_learn_card_9', 'n_clicks'),
        Input('close_learn_card_9', 'n_clicks'),
    ],
    [State('body_learn_card_9', 'is_open')],
)
def toggle_modal9(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_10', 'is_open'),
    [
        Input('open_learn_card_10', 'n_clicks'),
        Input('close_learn_card_10', 'n_clicks'),
    ],
    [State('body_learn_card_10', 'is_open')],
)
def toggle_modal10(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_11', 'is_open'),
    [
        Input('open_learn_card_11', 'n_clicks'),
        Input('close_learn_card_11', 'n_clicks'),
    ],
    [State('body_learn_card_11', 'is_open')],
)
def toggle_modal11(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_12', 'is_open'),
    [
        Input('open_learn_card_12', 'n_clicks'),
        Input('close_learn_card_12', 'n_clicks'),
    ],
    [State('body_learn_card_12', 'is_open')],
)
def toggle_modal12(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_13', 'is_open'),
    [
        Input('open_learn_card_13', 'n_clicks'),
        Input('close_learn_card_13', 'n_clicks'),
    ],
    [State('body_learn_card_13', 'is_open')],
)
def toggle_modal13(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_14', 'is_open'),
    [
        Input('open_learn_card_14', 'n_clicks'),
        Input('close_learn_card_14', 'n_clicks'),
    ],
    [State('body_learn_card_14', 'is_open')],
)
def toggle_modal14(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_15', 'is_open'),
    [
        Input('open_learn_card_15', 'n_clicks'),
        Input('close_learn_card_15', 'n_clicks'),
    ],
    [State('body_learn_card_15', 'is_open')],
)
def toggle_modal15(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output('body_learn_card_16', 'is_open'),
    [
        Input('open_learn_card_16', 'n_clicks'),
        Input('close_learn_card_16', 'n_clicks'),
    ],
    [State('body_learn_card_16', 'is_open')],
)
def toggle_modal15(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Label('Foundations',
                          className="page_section_topic"))
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardHeader('Learn the fundamentals of KlimaDAO', className='enclosure_card_topic'),
            dbc.CardBody([
               dbc.Row([
                   dbc.Col(learn_card_1, xs=12, sm=12, md=12, lg=3, xl=3,
                           style={'padding': '10px', 'height': '100%'}),
                   dbc.Col(learn_card_2, xs=12, sm=12, md=12, lg=3, xl=3,
                           style={'padding': '10px', 'height': '100%'}),
                   dbc.Col(learn_card_3, xs=12, sm=12, md=12, lg=3, xl=3,
                           style={'padding': '10px', 'height': '100%'}),
                   dbc.Col(learn_card_4, xs=12, sm=12, md=12, lg=3, xl=3,
                           style={'padding': '10px', 'height': '100%'})
               ])
            ])
        ]),
    ]),
    dbc.Row([
        dbc.Col(dbc.Label('Protocol Mechanics',
                          className="page_section_topic"))
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardHeader('Understand the principles of the Klima Protocol'),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(learn_card_5, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'}),
                    dbc.Col(learn_card_6, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'}),
                    dbc.Col(learn_card_7, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'}),
                    dbc.Col(learn_card_8, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'})
                ])
            ])
        ]),
    ]),
    dbc.Row([
        dbc.Col(dbc.Label('Carbon Markets',
                          className="page_section_topic"))
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardHeader('Get caught up on the Carbon Market and its significance'),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(learn_card_9, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'}),
                    dbc.Col(learn_card_10, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'}),
                    dbc.Col(learn_card_11, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'}),
                    dbc.Col(learn_card_12, xs=12, sm=12, md=12, lg=3, xl=3,
                            style={'padding': '10px', 'height': '100%'})
                ])
            ])
        ]),
    ]),
    dbc.Row([
        dbc.Col(dbc.Label('Dune Metrics Guide',
                          className="page_section_topic"))
    ]),
    dbc.Row([
        dbc.Card([
            dbc.CardHeader('Important protocol metrics you should understand - by Cujo'),
            dbc.CardBody([
                    dbc.Row([
                        dbc.Col(learn_card_13, xs=12, sm=12, md=12, lg=3, xl=3,
                                style={'padding': '10px', 'height': '100%'}),
                        dbc.Col(learn_card_14, xs=12, sm=12, md=12, lg=3, xl=3,
                                style={'padding': '10px', 'height': '100%'}),
                        dbc.Col(learn_card_15, xs=12, sm=12, md=12, lg=3, xl=3,
                                style={'padding': '10px', 'height': '100%'}),
                        dbc.Col(learn_card_16, xs=12, sm=12, md=12, lg=3, xl=3,
                                style={'padding': '10px', 'height': '100%'})
                ])
            ])
        ]),
    ]),
])
