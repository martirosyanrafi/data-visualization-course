import filter
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html


def get_html_content(df):
    return html.Div([
        filter.get_html_content(df, 'model'),
        html.Div(id='model-output-container')
    ])


def get_output_content(df):
    if df.empty:
        return html.Div('Models with these filters don\'t exist.')
    else:
        fig = px.bar(x=df.model.unique(), y=df.model.value_counts())
        return dcc.Graph(figure=fig)
