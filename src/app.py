# import dash
import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, TriggerTransform, ServersideOutputTransform, PrefixIdTransform

app = DashProxy(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    suppress_callback_exceptions=True,
    title="Klima Playgrounds",
    transforms=[
        TriggerTransform(),
        ServersideOutputTransform()],
    meta_tags=[
        {
            'name': 'viewport',
            'content':
            'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
        },
        {"property": "og:type", "content": "website"},
        {"property": "og:site_name", "content": "Klima Playgrounds"},
        {"property": "og:title", "content": "Analytics & simulation environment for the KlimaDAO protocol"},
        {
            "property": "og:description",
            "content":
            "Data visualizations, analytics and simulators that shed light on the inner workings of "
            "KlimaDAO's carbon-backed reserve currency protocol."
        },
        {
            "property": "og:image",
            "content": "https://www.klimadao.finance/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fdk34t4vc%2Fproduction%2Ffabb9013880c981edd36d25e89df6b7e6efe5892-2156x1080.png&w=1920&q=75"  # noqa: E501
        },
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@discord"},
        {"name": "twitter:creator", "content": "@Playgrounds0x"}
    ]
)
