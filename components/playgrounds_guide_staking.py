from dash import dcc

how_to_read_growth_chart_intro = dcc.Markdown(
    '''
    The KLIMA growth simulation results chart is interactive and provides a visual representation of
    various ROI calculations.


    Click for an overview on how to read and use the chart
    '''
)
how_to_read_growth_chart = dcc.Markdown(
    '''
    #### The chart is interactive!

    - Click on the legend to hide/show trend lines
    - Access the toolbar (on mouse hover) to:
        - Zoom
        - Pan
        - Compare trend lines
        - Show spike lines
        - Download the chart as PNG
    '''
)
how_to_simulation_controls_intro = dcc.Markdown(
    '''
    The simulation controls allow you to calculate various scenarios that fit your needs.

    Click for a detailed guide on how to use the simulation controls
    '''
)
how_to_simulation_controls = dcc.Markdown(
    '''
    The Klima growth simulation results chart is a visual overview of your simulation results.
    On this chart, you are presented with results from the following calculations:

    - (3,3) ROI
    - (3,3) Profit adjusted ROI
    - (3,3) DCA adjusted ROI

    Additionally, it shows the minimum and maximum rewards you can receive from basic staking as determined by
    the parameters set by policy.

    You could be above or below this depending on you how often you buy or sell.

    Each of these trend lines are meaningful to various participants. To adjust these trend lines, we focus our
    attention to the simulation controls panel on the right side of the dashboard.

    The simulation controls panel is broken into sections for easier access to the ROI type you care about.

    The following guides breakdown each ROI type and how to adjust them to fit your needs:

    1. (3,3) ROI: This is the rewards yield curve (blue colored line) over the specified number of days.
    Essentially, this curve shows you the KLIMA growth from an initial point over any number of days based on
    your selected APY. To adjust this curve to suite your needs, do the following:

    - Adjust the number of days using the slider or input box found on the simulation controls section.
    - Adjust the initial KLIMA to your desired starting amonut of KLIMA.
    - Change the APY to the current APY found on KlimaDAO main site or to any speculated APY of your choice.

    Making these changes will adjust the (3,3) ROI curve and help with visualizing the potential growth of your KLIMA
    over specified number of days. Keep in mind, the APY you put in is subject to change based on the policy of
    KlimaDAO and KIP-3 framework which defines the reward rate reduction at predefined circulating KLIMA milestones.

    2. (3,3) Profit adjusted ROI: This is the reward yield curve (orange colored line) over the specified number of days
    if you decide to sell a certain amount or percentage of accumulated KLIMA at fixed intervals. Essentially, this
    curve shows you the KLIMA growth despite taking profit x number of days. To adjust this curve to suit your needs,
    do the following:

    - Adjust the amount you would like to sell using the input box provided. You can choose between percentage or a fixed
    amount of KLIMA to sell. 
    - Adjust the cadence. The cadence is how often you want to take profit. For instance, if you want to sell
    every 30 days, you will type in 30 days in the cadence input box.

    Making these changes will adjust the profit adjusted ROI curve and help visualize the best profit taking strategy
    for you. This is not an endorsement to sell, but a tool if profit taking is part of your strategy.

    3. (3,3) DCA adjusted ROI: This is the rewards yield curve (green colored line) over a specified number of days if
    you decide to buy a certain amount of KLIMA at fixed intervals. Essentially, this curve shows you the KLIMA growth
    over time as you add to your already compounding KLIMA. To adjust this curve, do the following:

    - Adjust the KLIMA price. This is your target buy in price.
    - Adjust the purchase amount. This is the USDC value of KLIMA you would like to purchase.
    - Adjust the cadence. The cadence is how often you want to buy and stake KLIMA. For instance, if you want to buy
    every 30 days, you will type in 30 days in the cadence input box.
    '''
)
how_to_read_co_metrics_intro = dcc.Markdown(
    '''
    Carbon emissions metrics are used to emphasize how much carbon equivalent each
    KLIMA you stake and earn offsets.

    Click for an overview on how to read and use the chart
    '''
)
how_to_read_co_metrics = dcc.Markdown(
    '''
    Carbon emissions metrics are used to calculate the equivalent carbon emissions offset by your staked KLIMA
    on an annual basis. In other words, it gives real-world examples on how much you will personally offset.

    The calculated carbon emissions equivalencies are as follows:

    - Annual Carbon emitted per passenger vehicles
    - Annual Carbon emitted per mile traveled by a typical passenger vehicle
    - Annual Carbon emitted per gallon of Gasoline combusted
    - Annual Carbon sequestered by average forestry acres

    #### How do I work with these metrics?

    Let's consider the annual carbon emitted per passenger vehicles metric. The variables required to update this metric
    are:

    - Initial KLIMA
    - APY (%)
    - RFV (BCT)

    These variables are found on the simulation controls section of the app (Right side of the chart)

    The calculation is as follows, the APY is used to project the growth of your initial KLIMA over a year. Once the
    projection is complete, the calculator then takes the speculated RFV in BCT (Base Carbon Tonnes) and multiplies your
    total accumulated KLIMA with the RFV. This shows the amount of carbon equivalent that is locked.

    Once the total carbon equivalent locked is determined, we then calculate the equivalent emissions from the average
    passenger vehicle. We used data provided by the
    [EPA] (https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references)
    for all equivalency calculations.
    '''
)
how_to_use_strategizer_intro = dcc.Markdown(
    '''
    The rewards strategizer is a tool used to calculate potential future staking rewards.

    Click for an overview on how to read and use the chart.
    '''
)
how_to_use_strategizer = dcc.Markdown(
    '''
    The rewards strategizer is a tool used to calculate potential future staking rewards. Using the strategizer
     you can predict the following outcomes. Note dollar values are highly speculative and these are not guarantees on
     a return:

    - Days until your staking rewards have reached a certain USDC value.
    - Days until your staking rewards has accumulated to a desired amount.
    - Days until you are earning a desired amount of USDC daily and how much KLIMA is required.
    - Days until you are earning a desired amount of USDC weekly and how much KLIMA is required.

    To use this section of the app, type in your goals in the rewards strategizer controls. Results from the
    calculations are presented on the rewards strategy results card.

    Again, it is important to know that this feature is speculative and based on the assumption that the price of
    KLIMA will either stay at the levels determined in the controls section.
    '''
)
