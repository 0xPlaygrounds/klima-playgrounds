# import dash
import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, TriggerTransform, ServersideOutputTransform

app = DashProxy(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    suppress_callback_exceptions=True,
    title="Klima Playgrounds",
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
    }],
    transforms=[
        TriggerTransform(),
        ServersideOutputTransform()
    ]
)
