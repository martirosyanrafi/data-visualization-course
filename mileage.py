import filter
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html


def get_html_content(df):
    return html.Div([
        html.H1('Mileage'),
        html.Br(),
        filter.get_html_content(df, 'mileage'),
        html.Div(id='mileage-output-container'),
        html.Br(),
        html.Br(),
        html.H6('This chart shows the mileages of cars in US based on the selected filters.')
    ])


def get_output_content(df):
    if df.empty:
        return html.Div('Cars with these filters don\'t exist.')
    else:
        key = 'model' if len(df.brand.unique()) == 1 else 'brand'
        fig = px.scatter(x=df[key], y=df.mileage, labels={"x": "Model", "y": "Mileage"})
        return dcc.Graph(figure=fig)
