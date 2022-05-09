from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds.subgrounds import Subgrounds

# Uncomment to get logs into `subgrounds.log` WARNING! This generates a LOOOT of logs
# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='subgrounds.log', level=logging.INFO)
# logger = logging.getLogger('subgrounds')
# logger.setLevel(logging.DEBUG)

sg = Subgrounds()
klimaDAO = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/cujowolf/klima-protocol-metrics')
# users = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/0xaurelius/klimadao-users')


# Define useful synthetic fields
klimaDAO.ProtocolMetric.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.STRING,
  klimaDAO.ProtocolMetric.timestamp,
)

klimaDAO.ProtocolMetric.staked_supply_percent = SyntheticField(
  lambda sklima_supply, total_supply: 100 * sklima_supply / total_supply,
  SyntheticField.FLOAT,
  [
    klimaDAO.ProtocolMetric.sKlimaCirculatingSupply,
    klimaDAO.ProtocolMetric.totalSupply
  ],
  default=100.0
)


klimaDAO.ProtocolMetric.unstaked_supply_percent = 100 - klimaDAO.ProtocolMetric.staked_supply_percent

# Treasury CC per klima and ratio
klimaDAO.ProtocolMetric.cc_per_klima = SyntheticField(
  lambda treasury_cc, total_supply: treasury_cc / total_supply if treasury_cc / total_supply > 1 else 0,
  SyntheticField.FLOAT,
  [klimaDAO.ProtocolMetric.treasuryCarbonCustodied,
   klimaDAO.ProtocolMetric.totalSupply]
)

klimaDAO.ProtocolMetric.price_cc_ratio = \
    100 * klimaDAO.ProtocolMetric.klimaPrice / klimaDAO.ProtocolMetric.cc_per_klima

# Treasury market value per klima and ratio
klimaDAO.ProtocolMetric.tmv_per_klima = \
    klimaDAO.ProtocolMetric.treasuryMarketValue / klimaDAO.ProtocolMetric.totalSupply
klimaDAO.ProtocolMetric.price_tmv_ratio = \
    100 * klimaDAO.ProtocolMetric.klimaPrice / klimaDAO.ProtocolMetric.tmv_per_klima

protocol_metrics_1year = klimaDAO.Query.protocolMetrics(
  orderBy=klimaDAO.ProtocolMetric.timestamp,
  orderDirection='desc',
  first=365
)

last_metric = klimaDAO.Query.protocolMetrics(
  orderBy=klimaDAO.ProtocolMetric.timestamp,
  orderDirection='desc',
  first=1
)
