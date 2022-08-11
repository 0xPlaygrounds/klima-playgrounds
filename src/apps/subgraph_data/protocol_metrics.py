from subgrounds.subgrounds import Subgrounds
from subgrounds.subgraph import SyntheticField
from src.apps.util.cache import time_cache

from src.apps.util.constants import BCT_ERC20_CONTRACT, KLIMA_PROTOCOL_SUBGRAPH
from src.apps.util.time_util import get_date_timestamp_string

sg = Subgrounds()
protocol_metrics_subgraph = sg.load_subgraph(KLIMA_PROTOCOL_SUBGRAPH)

# Define useful synthetic fields
# Protocol metrics
protocol_metrics_subgraph.ProtocolMetric.datetime = SyntheticField(
    lambda timestamp: get_date_timestamp_string(timestamp),
    SyntheticField.STRING,
    protocol_metrics_subgraph.ProtocolMetric.timestamp,
)

protocol_metrics_subgraph.ProtocolMetric.staked_supply_percent = \
    SyntheticField(
        lambda sklima_supply, total_supply: 100 * sklima_supply / total_supply,
        SyntheticField.FLOAT,
        [
            protocol_metrics_subgraph.ProtocolMetric.sKlimaCirculatingSupply,
            protocol_metrics_subgraph.ProtocolMetric.totalSupply
        ],
        default=100.0)

protocol_metrics_subgraph.ProtocolMetric.klima_in_lp_percent = SyntheticField(
    lambda klima_in_lp, total_supply: 100 * klima_in_lp / total_supply,
    SyntheticField.FLOAT,
    [
        protocol_metrics_subgraph.ProtocolMetric.totalKlimaInLP,
        protocol_metrics_subgraph.ProtocolMetric.totalSupply
    ],
    default=100.0
)

# Treasury asset
protocol_metrics_subgraph.TreasuryAsset.datetime = SyntheticField(
    lambda timestamp: get_date_timestamp_string(timestamp),
    SyntheticField.STRING,
    protocol_metrics_subgraph.TreasuryAsset.timestamp,
)

protocol_metrics_subgraph.TreasuryAsset.formatted_market_value = SyntheticField(
    lambda marketValue: round(marketValue / float(1000000), 4),
    SyntheticField.FLOAT,
    protocol_metrics_subgraph.TreasuryAsset.marketValue,
)

protocol_metrics_subgraph.ProtocolMetric.unstaked_supply_percent = \
    100 - \
    (protocol_metrics_subgraph.ProtocolMetric.staked_supply_percent +
     protocol_metrics_subgraph.ProtocolMetric.klima_in_lp_percent)

# Treasury CC per klima and ratio
protocol_metrics_subgraph.ProtocolMetric.cc_per_klima = \
    SyntheticField(
        lambda treasury_cc, total_supply:
        treasury_cc / total_supply if treasury_cc / total_supply > 1 else 0,
        SyntheticField.FLOAT,
        [protocol_metrics_subgraph.ProtocolMetric.treasuryCarbonCustodied,
         protocol_metrics_subgraph.ProtocolMetric.totalSupply])

protocol_metrics_subgraph.ProtocolMetric.price_cc_ratio = \
    100 * protocol_metrics_subgraph.ProtocolMetric.klimaPrice \
    / protocol_metrics_subgraph.ProtocolMetric.cc_per_klima

# Treasury market value per klima and ratio
protocol_metrics_subgraph.ProtocolMetric.tmv_per_klima = \
    protocol_metrics_subgraph.ProtocolMetric.treasuryMarketValue \
    / protocol_metrics_subgraph.ProtocolMetric.totalSupply

protocol_metrics_subgraph.ProtocolMetric.price_tmv_ratio = \
    100 * protocol_metrics_subgraph.ProtocolMetric.klimaPrice \
    / protocol_metrics_subgraph.ProtocolMetric.tmv_per_klima

protocol_metrics_1year = protocol_metrics_subgraph.Query.protocolMetrics(
    orderBy=protocol_metrics_subgraph.ProtocolMetric.timestamp,
    orderDirection='desc',
    first=365
)

last_metric = protocol_metrics_subgraph.Query.protocolMetrics(
    orderBy=protocol_metrics_subgraph.ProtocolMetric.timestamp,
    orderDirection='desc',
    first=1
)

staked_metrics_df = sg.query_df([
    protocol_metrics_1year.datetime,
    protocol_metrics_1year.staked_supply_percent])

supply_and_index_metrics = sg.query_df([
    protocol_metrics_1year.datetime,
    protocol_metrics_1year.totalSupply,
    protocol_metrics_1year.klimaIndex])


def get_protocol_metrics_1_year():
    return protocol_metrics_subgraph.Query.protocolMetrics(
        orderBy=protocol_metrics_subgraph.ProtocolMetric.timestamp,
        orderDirection='desc',
        first=365
    )


def get_df_for_treasury_asset_by_address(address):
    treasury_df = get_treasury_df()

    asset_df = treasury_df[treasury_df['treasuryAssets_token']
                           == address]

    return asset_df


@time_cache(600)
def get_treasury_df():
    treasury_assets = protocol_metrics_subgraph.Query.treasuryAssets(
        orderBy=protocol_metrics_subgraph.TreasuryAsset.timestamp,
        orderDirection='asc',
        first=10000000
    )

    return sg.query_df([
        treasury_assets.datetime,
        treasury_assets.token,
        treasury_assets.carbonCustodied,
        treasury_assets.formatted_market_value])


@time_cache(600)
def get_bct_treasury():
    return protocol_metrics_subgraph.Query.treasuryAssets(
        where=[protocol_metrics_subgraph.TreasuryAsset.token == BCT_ERC20_CONTRACT],
        orderBy=protocol_metrics_subgraph.TreasuryAsset.timestamp,
        orderDirection='asc',
        first=10000000
    )
