from dash import dcc

what_is_staking_intro = dcc.Markdown(
    '''
    staking is the primary protocol profit distribution mechanism

    Click learn more for an overview on staking
    '''
)
what_is_staking = dcc.Markdown(
    '''
    Staking is the primary profit distribution mechanism of the protocol.
    It is designed to be the primary mechanism of value accrual for the majority of users.
    For most, the best thing to do is to simply stake and compound the KLIMA acquired via rewards.

    #### How does it really work?

    When the Risk Free Value (RFV) of the treasury is higher than the assets needed
    to back each KLIMA, the protocol will mint and distribute KLIMA tokens to all stakers.

    The amount minted and distributed is controlled by a variable called the reward rate.

    The reward rate is the percentage of supply that is rebased. The process of rebasing and rewarding
    stakers is a powerful tool used to maintain system stability and prevent over expansion of supply.
    '''
)
why_should_i_stake_intro = dcc.Markdown(
    '''
    Participating in staking helps you accumulate more KLIMA and lock more carbon offsets.

    Click learn more for an overview on why staking is important
    '''
)
why_should_i_stake = dcc.Markdown(
    '''
    By participating in KlimaDAO and staking your KLIMA tokens, you are doing the following:

    1. Enabling economic activity within the Klima ecosystem which in turn, increases use case for KLIMA and creates
    new incentives for bridging carbon on-chain

    2. Participating in the profit distribution system of klimaDAO. staking is designed to incentivise long term holding
    of KLIMA while giving participant exposure to the increasing price of carbon. The longer you stake, the more KLIMA
    you compound and the more carbon you are exposed to

    3. Reducing effective circulating supply which in turn reduces selling pressure of KLIMA token.
    This is good for price stability during the expansion phase of the protocol
    '''
)
how_can_i_stake_intro = dcc.Markdown(
    '''
    staking your KLIMA is a straight forward process. Assuming you already have KLIMA, visit
    [Klima](https://dapp.klimadao.finance/#/stake) to stake.

    Click learn more for a step by step guide
    '''
)
how_can_i_stake = dcc.Markdown(
    '''
    staking is the primary method for participating in KlimaDAO.

    It is important to note that all transactions with
    KlimaDAO occurs on the Polygon network and you need to have KLIMA in your wallet before you can stake.

    A quick step by step guide on getting KLIMA staked is as follows:

    1. Make sure your wallet is connected to the Polygon network. If you are using metamask, follow these instructions
    2. Make sure you have KLIMA in your wallet. If you do not have KLIMA, visit sushiswap and purchase some. The best
    pairing is BCT/KLIMA or USDC/KLIMA
    3. Now that you have KLIMA in your wallet, visit the Klima dAPP and click stake. Make sure your wallet is connected
    to the dAPP by clicking on "Connect wallet" found on the top right of the app interface
    4. While on the stake tab, designate the amount of KLIMA you would like to stake, click stake, and approve
    the transaction on your wallet
    '''
)
staking_dynamics_intro = dcc.Markdown(
    '''
    staking is the best strategy for participating in KlimaDAO. staking benefits both you the participant
    and the protocol.

    Click learn more for an overview of the game theory behind staking
    '''
)
staking_dynamics = dcc.Markdown(
    '''
At a high level users have 3 possible actions when interacting with the protocol:

- Stake
- Bond
- Sell

In general, participants are more likely to do the following:

- Buy and stake KLIMA when it's price is increasing
- Sell when price is decreasing
- stake when price is neutral or expected to increase

However, it is important to emphasize that regardless of all likely actions, staking remains the most beneficial action
for the protocol and participants

staking aligns incentives between the protocol and participants.
Participants benefit from receiving rewards and the protocol benefits from decreased sell pressure

The Game Theory of staking coined (3,3) illustrates and provides a narrative; *the best strategies are cooperative*

Simply put, (3,3) means If everyone stakes, you and everyone else benefits

#### Market Dynamics

KLIMA is backed by Base Carbon Token (BCT), a tokenized carbon credit representing one tonne of carbon.

The cost of BCT is dependent on the price of carbon in the market (see Understanding Carbon).
Overtime, demand for carbon reduction increases and carbon offsets become more scarce,
this creates buy pressure on an increasingly scarce asset.

If you know the most basic laws of supply and demand, this equated to an increase in the price of carbon thus the
price of BCT. The result of this dynamic is an increase in value of the asset that backs KLIMA,
giving KLIMA a higher intrinsic value.

Another important variable at a play is the intrinsic value of KLIMA. The increasing intrinsic value (IV) creates a
loose floor price of KLIMA. Sellers are selling at a great loss if they sell below IV because the backing assets
are worth more than what they are selling for. Klima staker shave a guarantee price will return to above IV because
the protocol can use reserves to buy below IV to return the price of KLIMA to it’s IV.

An increase in staking is generally preceded by purchases of KLIMA. This increases the price of KLIMA and thus the
yield for stakers. At the same time, rising prices increase stake discounts and capacity for new stakes. This, in turn,
allows KLIMA to grow its POL and treasury.

This positive price-liquidity feedback loop should serve to create sustainable expansionary periods. However, it works
both ways. Falling demand decreases staking yield and stake capacity, causing demand to fall further.
This is an unavoidable fact of systems like this; even the most established (i.e. Bitcoin) experience
significant declines after periods of expansion.

But Klima’s tokenomics work to mitigate busts. The anticipated growth in demand for carbon offsets is expected to
ensure that there is demand for KLIMA and the intrinsic value will trend upwards overtime.
    '''
)
