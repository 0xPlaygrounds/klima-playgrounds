from dash import dcc

from config import RFV_TERM


what_is_bonding_intro = dcc.Markdown(
    '''
    Bonding is the process of trading assets directly to the protocol for KLIMA.

    Click learn more for an overview on bonding
    '''
)
what_is_bonding = dcc.Markdown(
    '''
    Bonding is the process of trading assets directly to the protocol for KLIMA.
    On the Dapp’s bond interface, the protocol will quote you a price in KLIMA for your asset,
    with the resulting KLIMA paid out linearly over a vesting period.

    #### How does it really work?

    In V1 of the protocol, the vesting period is fixed at approximately 5 days.
    So if you bonded for 5 KLIMA, you would be able to claim ~1 KLIMA after the first day.

    As of this writing, the treasury accepts bonds for the following assets:

    - Reserve Assets: BCT (Base Carbon Tonnes)
    - Liquidity Assets: KLIMA/BCT and BCT/USDC SushiSwap LP pairs.
    '''
)
why_should_i_bond_intro = dcc.Markdown(
    '''
    Bonding may allow you to buy KLIMA at a discount to current market prices.

    Click learn more for an overview on why bonding is important
    '''
)
why_should_i_bond = dcc.Markdown(
    '''
    Bonding may allow you to buy KLIMA at a discount to current market prices.

    This discount rate varies for each asset that can be bonded, fluctuating in real time based on current demand
    to bond that asset, as well as the bond capacity for that asset set by the Klima policy team.
    See the [Klima] (https://docs.klimadao.finance/tokenomics-and-mechanisms/primer-on-bonding#bonding-dynamics)
    documentation for more details.

    #### NOTE: It is typically _not profitable_ to bond when discounts are negative.

    A negative discount means current demand for bonds exceeds the treasury's capacity for that bond type.
    Over time, discounts will go up if/when the amount of that asset being bonded drops, or if that bond’s capacity
    is increased by the Klima policy team.
    '''
)
why_should_treasury_bond_intro = dcc.Markdown(
    '''
    Bonding is the primary revenue stream for the treasury, providing additional reserves

    Click learn more for an overview on why bonding is important for the treasury
    '''
)
why_should_treasury_bond = dcc.Markdown(
    f'''
    Bonding is the primary revenue stream for the treasury, providing additional reserves
    (which increase {RFV_TERM} and can eventually be paid out to bondrs via rebases),
    as well as additional liquidity tokens (which generate trading fees and deepen liquidity).

    The price that the protocol pays to accumulate these assets is “dilution” - minting new KLIMA that is *not*
    paid out to existing stakers.

    In order to manage dilution and control which assets are accumulated the most, the treasury can only accept
    a certain amount of bonding for each asset at any given time - hence the adjustable “capacity” for each bond type,
    and a dynamic discount that changes in response to demand.
    '''
)
how_can_i_bond_intro = dcc.Markdown(
    '''
    Bonding your KLIMA is a straight forward process. Assuming you already have KLIMA, visit
    [Klima](https://dapp.klimadao.finance/#/bond) to bond.

    Click learn more for a step by step guide
    '''
)
how_can_i_bond = dcc.Markdown(
    '''
    Bonding is one of the primary method for participating in KlimaDAO.

    It is important to note that all transactions with
    KlimaDAO occurs on the Polygon network and you need to have KLIMA in your wallet before you can bond.

    A quick step by step guide on getting KLIMA bondd is as follows:

    1. Make sure your wallet is connected to the Polygon network. If you are using metamask, follow these instructions
    2. Make sure your wallet is connected to the dAPP by clicking on "Connect wallet"
    3. While on the bond tab, identify the type of bond you will like to participate in. For example, you might be
    interested in the following bonds:

    - BCT (Bond your BCT token to get KLIMA in return)
    - BCT/KLIMA LP (Bond your LP token to get KLIMA in return)
    - BCT/USDC LP (Bond your LP token to get KLIMA in return)
    - MCO2 (Bond your MCO2 to get KLIMA in return)

    If you do not have the available bond tokens, you can obtain them on Sushiswap, Uniswap or Quickswap.

    For single tokens such as BCT and MCO2, you can acquire these on the AMMs listed above.

    For LP tokens, you would need to provide liquidity on Sushiswap, Uniswap or Quickswap to obtain the LP. For example,
    providing BCT AND KLIMA liquidity on Sushiswap will get you BCT/KLIMA LP token

    4. Once you have the bond tokens you need, you bond them on the KlimaDAO dAPP.

    *Remember that when you bond, your KLIMA is released to you on a vest period of 5 days*
    '''
)
bonding_dynamics_intro = dcc.Markdown(
    '''
    Bonding is a great strategy for participating in KlimaDAO. Bonding benefits both you the participant
    and the protocol.

    Click learn more for an overview of the game theory behind bonding
    '''
)
bonding_dynamics = dcc.Markdown(
    '''
    At a high level users have 3 possible actions when interacting with the protocol:

    - Stake
    - Bond
    - Sell

    In general, participants are more likely to do the following:

    - Buy and bond KLIMA when it's price is increasing
    - Sell when price is decreasing
    - bond when price is neutral or expected to increase

    However, it is important to emphasize that regardless of all likely actions, bonding remains the most beneficial
    action for the protocol and participants

    Bonding aligns incentives between the protocol and participants.
    Participants benefit from receiving rewards and the protocol benefits from accumulating treasury assets


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
    are worth more than what they are selling for. Klima bondr shave a guarantee price will return to above IV because
    the protocol can use reserves to buy below IV to return the price of KLIMA to it’s IV.

    An increase in bonding is generally preceded by purchases of KLIMA. This increases the price of KLIMA and thus the
    yield for bondrs. At the same time, rising prices increase bond discounts and capacity for new bonds. This, in turn,
    allows KLIMA to grow its POL and treasury.

    This positive price-liquidity feedback loop should serve to create sustainable expansionary periods.
    However, it works both ways. Falling demand decreases bonding yield and bond capacity,
    causing demand to fall further.
    This is an unavoidable fact of systems like this; even the most established (i.e. Bitcoin) experience
    significant declines after periods of expansion.

    But Klima’s tokenomics work to mitigate busts. The anticipated growth in demand for carbon offsets is expected to
    ensure that there is demand for KLIMA and the intrinsic value will trend upwards overtime.
    '''
)
