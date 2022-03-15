from datetime import datetime

import dash
from dash import html

from subgrounds.dash_wrappers import Graph
from subgrounds.plotly_wrappers import Figure, Scatter, Indicator
from subgrounds.schema import TypeRef
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds

sg = Subgrounds()
klimaDAO = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/cujowolf/klima-graph')


def immediate(sg: Subgrounds, fpath: FieldPath):
    data = sg.execute(sg.mk_request([fpath]))
    return fpath.extract_data(data)[0]


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

# Treasury RFV per klima and ratio
klimaDAO.ProtocolMetric.rfv_per_klima = SyntheticField(
  lambda treasury_rfv, total_supply: treasury_rfv / total_supply if treasury_rfv / total_supply > 1 else 0,
  SyntheticField.FLOAT,
  [
    klimaDAO.ProtocolMetric.treasuryRiskFreeValue,
    klimaDAO.ProtocolMetric.totalSupply
  ]
)

klimaDAO.ProtocolMetric.price_rfv_ratio = \
    100 * klimaDAO.ProtocolMetric.klimaPrice / klimaDAO.ProtocolMetric.rfv_per_klima

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
