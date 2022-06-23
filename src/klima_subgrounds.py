from textwrap import fill
from more_itertools import strip
from src.apps.util.cache import time_cache
import src.apps.subgraph_data.protocol_metrics as protocol_metrics
import src.apps.subgraph_data.vesting_metrics as vesting_metrics

# Uncomment to get logs into `subgrounds.log` WARNING! This generates a LOOOT of logs
# import logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     filename='subgrounds.log',
#     level=logging.INFO
# )
# logger = logging.getLogger('subgrounds')
# logger.setLevel(logging.DEBUG)


#Charts are dependent on protocol metric Subgraph
sg = protocol_metrics.sg

# Protocol metric Subgraph data
protocol_metrics_1year = protocol_metrics.protocol_metrics_1year
last_metric = protocol_metrics.last_metric


@time_cache(300)
def get_klima_breakdown_df():
  protocol_metrics_1year = protocol_metrics.get_protocol_metrics_1_year()
  staked_metrics_df = sg.query_df([protocol_metrics_1year.datetime, protocol_metrics_1year.staked_supply_percent])
  supply_and_index_metrics = sg.query_df([protocol_metrics_1year.datetime, protocol_metrics_1year.totalSupply, protocol_metrics_1year.klimaIndex])

  vesting_filler_df = supply_and_index_metrics.rename(
    columns={"protocolMetrics_datetime": "vestingMetrics_datetime"})

  #create expanded vesting df
  expanded_co2_compound_df = vesting_metrics.expand_vesting_metrics(vesting_filler_df, vesting_metrics.co2_compound_df)
  expanded_c3_df = vesting_metrics.expand_vesting_metrics(vesting_filler_df, vesting_metrics.c3_df)

  #Subtract Staking locked percentage and total vested lock percentage via expanded DF
  staked_metrics_df.set_index('protocolMetrics_datetime', inplace=True, drop=False)
  vesting_metrics.subtract_vested_from_stake(staked_metrics_df, [expanded_c3_df, expanded_co2_compound_df])

  return staked_metrics_df, expanded_c3_df, expanded_co2_compound_df
