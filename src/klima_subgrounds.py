from textwrap import fill
from more_itertools import strip
import src.apps.subgraph_data.protocol_metrics as protocol_metrics
import src.apps.subgraph_data.vesting_metrics as vesting_metrics

#Charts are dependent on protocol metric Subgraph
sg = protocol_metrics.sg

# Uncomment to get logs into `subgrounds.log` WARNING! This generates a LOOOT of logs
# import logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     filename='subgrounds.log',
#     level=logging.INFO
# )
# logger = logging.getLogger('subgrounds')
# logger.setLevel(logging.DEBUG)

# Protocol metric Subgraph data
protocol_metrics_1year = protocol_metrics.protocol_metrics_1year
last_metric = protocol_metrics.last_metric

# Vesting Metric Subgraph data
# Create Filler DF from Staking DF that will be used to expand Vesting metrics
staked_metrics_df = protocol_metrics.staked_metrics_df
vesting_filler_df = staked_metrics_df.rename(
  columns={"protocolMetrics_datetime": "vestingMetrics_datetime", "protocolMetrics_staked_supply_percent": "vestingMetrics_locked_percentage"})
vesting_filler_df = vesting_filler_df.assign(vestingMetrics_locked_percentage=0)

expanded_co2_compound_df = vesting_metrics.expand_vesting_metrics(vesting_filler_df, vesting_metrics.co2_compound_df)
expanded_c3_df = vesting_metrics.expand_vesting_metrics(vesting_filler_df, vesting_metrics.c3_df)

#Subtract Staking locked percentage and total vested lock percentage via expanded DF
staked_metrics_df.set_index('protocolMetrics_datetime', inplace=True, drop=False)
vesting_metrics.subtract_vested_from_stake(staked_metrics_df, [expanded_c3_df, expanded_co2_compound_df])

