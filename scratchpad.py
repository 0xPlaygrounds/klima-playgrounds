import dash
from dash import html
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px


# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])

# Text field
def drawText():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Text 1"),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

def drawText2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Text 1"),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

# Data source
df = px.data.iris()

# Build App
app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        html.H1('Playgrounds Explorer'),
        html.Div([
            html.P('Explore the olympus protocol'),
            html.P("Discover your own insight")
            ])
    ]),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Markdown('''

                        # This is an <h1> tag

                        ## This is an <h2> tag

                        ###### This is an <h6> tag
                    ''')

                ], width=3),
                dbc.Col([
                    drawText()
                ], width=3),
                dbc.Col([
                    drawText()
                ], width=3),
                dbc.Col([
                    drawText()
                ], width=3),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=3),
                dbc.Col([
                    drawFigure()
                ], width=3),
                dbc.Col([
                    drawFigure()
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=9),
                dbc.Col([
                    drawFigure()
                ], width=3),
            ], align='center'),
        ]), color='dark'
    ),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText()
                ], width=3),
                dbc.Col([
                    drawText()
                ], width=3),
                dbc.Col([
                    drawText()
                ], width=3),
                dbc.Col([
                    drawText()
                ], width=3),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=3),
                dbc.Col([
                    drawFigure()
                ], width=3),
                dbc.Col([
                    drawFigure()
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=9),
                dbc.Col([
                    drawFigure()
                ], width=3),
            ], align='center'),
        ]), color = 'dark'
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)