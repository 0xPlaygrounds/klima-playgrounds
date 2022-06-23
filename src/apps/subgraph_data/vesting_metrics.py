from subgrounds.subgrounds import Subgrounds
from subgrounds.subgraph import SyntheticField

from src.apps.util.constants import KLIMA_VESTING_SUBGRAPH, VESTING_PLATFORM_C02_COMPOUND, VESTING_PLATFORM_C3
from src.apps.util.time_util import get_date_timestamp_string

sg = Subgrounds()
vesting_metric_subgraph = sg.load_subgraph(KLIMA_VESTING_SUBGRAPH)

# Define useful synthetic fields
vesting_metric_subgraph.VestingMetric.datetime = SyntheticField(
  lambda timestamp: get_date_timestamp_string(timestamp),
  SyntheticField.STRING,
  vesting_metric_subgraph.VestingMetric.timestamp,
)

vesting_metric_subgraph.VestingMetric.total_supply_in_klima = SyntheticField(
  lambda total_supply, index: total_supply * index,
  SyntheticField.FLOAT,
  [
    vesting_metric_subgraph.VestingMetric.totalSupply,
    vesting_metric_subgraph.VestingMetric.index,
  ],
  default=100.0
)

vesting_metric_subgraph.VestingMetric.total_locked_amount_in_klima = SyntheticField(
  lambda amount_locked, index: amount_locked * index,
  SyntheticField.FLOAT,
  [
    vesting_metric_subgraph.VestingMetric.totalAmountLocked,
    vesting_metric_subgraph.VestingMetric.index,
  ],
  default=100.0
)

vesting_metric_subgraph.VestingMetric.locked_percentage = SyntheticField(
  lambda total_amount_locked, total_supply: 100 * total_amount_locked / total_supply,
  SyntheticField.FLOAT,
  [
    vesting_metric_subgraph.VestingMetric.total_locked_amount_in_klima,
    vesting_metric_subgraph.VestingMetric.total_supply_in_klima
  ],
  default=100.0
)

#C3 Vesting metrics
c3_vesting_metrics_1_year = vesting_metric_subgraph.Query.vestingMetrics(
  where=[vesting_metric_subgraph.VestingMetric.inFuture == False,
        vesting_metric_subgraph.VestingMetric.platform == VESTING_PLATFORM_C3],
  orderBy=vesting_metric_subgraph.VestingMetric.timestamp,
  orderDirection='asc',
  first=365
)

#C02 Compound Vesting metrics
co2Compound_vesting_metrics_1_year = vesting_metric_subgraph.Query.vestingMetrics(
  where=[vesting_metric_subgraph.VestingMetric.inFuture == False,
        vesting_metric_subgraph.VestingMetric.platform == VESTING_PLATFORM_C02_COMPOUND],
  orderBy=vesting_metric_subgraph.VestingMetric.timestamp,
  orderDirection='asc',
  first=365
)

co2_compound_df = sg.query_df([co2Compound_vesting_metrics_1_year.datetime,
 co2Compound_vesting_metrics_1_year.totalAmountLocked,
 co2Compound_vesting_metrics_1_year.locked_percentage])

c3_df = sg.query_df([c3_vesting_metrics_1_year.datetime,
 c3_vesting_metrics_1_year.totalAmountLocked,
 c3_vesting_metrics_1_year.locked_percentage])



# Functions used for modifying data 
def expand_vesting_metrics(filler_df, vesting_metric_df):
    '''
    Modify Vesting Metric chart in order to be compatible with Protocol Metric chart
    '''
    expanded_vesting_metric_df = filler_df.append(vesting_metric_df, ignore_index = True).sort_values(by=['vestingMetrics_datetime'])
    fill_vesting_df(expanded_vesting_metric_df)
    expanded_vesting_metric_df.set_index('vestingMetrics_datetime', inplace=True, drop=False)
    expanded_vesting_metric_df = expanded_vesting_metric_df.groupby(expanded_vesting_metric_df.index).first()
    return expanded_vesting_metric_df



def fill_vesting_df(vesting_metrics_df):
    '''
    Fills EMPTY values with the previous non zero value
    This is required since vesting DF is merged with staking dataframe
    which may have datetimes that are not maintained within Vesting DF
    therefore we would be having 0 locked amount for such datetimes
    this function fixes that issue
    '''
    EMPTY = 'EMPTY'
    vesting_metrics_df.fillna(EMPTY, inplace=True)
    current_value = 0
    for index, row in vesting_metrics_df.iterrows():
        if row["vestingMetrics_totalAmountLocked"] == EMPTY:
            vesting_metrics_df.at[index, "vestingMetrics_totalAmountLocked"] = current_value
        else:
            current_value = row["vestingMetrics_totalAmountLocked"]
        if row['vestingMetrics_locked_percentage'] == EMPTY:
            vesting_metrics_df.at[index, "vestingMetrics_locked_percentage"] = \
            ((row["vestingMetrics_totalAmountLocked"]*row["protocolMetrics_klimaIndex"]) / row["protocolMetrics_totalSupply"]) * 100


def subtract_vested_from_stake(staking_df, dataframes):
      for index, row in staking_df.iterrows():
        total_locked_for_date = total_vested_locked_for_index(index, dataframes)
        currentStakingValue = row['protocolMetrics_staked_supply_percent']
        staking_df.at[index, 'protocolMetrics_staked_supply_percent'] = currentStakingValue - total_locked_for_date

def total_vested_locked_for_index(index, dataframes):
    total = 0
    for vested_df in dataframes:
        total+=vested_df.vestingMetrics_locked_percentage.get(index, 0)
    return total