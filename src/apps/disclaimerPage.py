import dash_bootstrap_components as dbc

from ..components.disclaimer import long_disclaimer_row


layout = dbc.Container([
    long_disclaimer_row()
])
