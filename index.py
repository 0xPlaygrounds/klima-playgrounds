import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import playgroundSimulation_KlimaGrowthOverTime, playgroundsSimulation_KlimaBonding


app.layout = html.Div([
    html.Div([
        dcc.Link('Staking', href='/apps/playgroundSimulation_KlimaGrowthOverTime'),
        dcc.Link('Bonding', href='/apps/playgroundsSimulation_KlimaBonding'),
    ], className='row'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/playgroundSimulation_KlimaGrowthOverTime':
        return playgroundSimulation_KlimaGrowthOverTime.layout
    elif pathname == '/apps/playgroundsSimulation_klimaBonding':
        return playgroundsSimulation_klimaBonding.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
