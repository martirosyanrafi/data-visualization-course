import filter
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html


def get_html_content(df):
    return html.Div([
        html.H1('Model'),
        html.Br(),
        filter.get_html_content(df, 'model'),
        html.Div(id='model-output-container'),
        html.Br(),
        html.Br(),
        html.H6('This chart shows the counts of models in US based on the selected filters.')
    ])


def get_output_content(df):
    if df.empty:
        return html.Div('Cars with these filters don\'t exist.')
    else:
        fig = px.bar(x=df.model.unique(), y=df.model.value_counts(), labels={"x": "Model", "y": "Count"})
        return dcc.Graph(figure=fig)
