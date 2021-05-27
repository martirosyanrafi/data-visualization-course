import filter
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html


def get_html_content(df):
    return html.Div([
        filter.get_html_content(df, 'color'),
        html.Div(id='color-output-container')
    ])


def get_output_content(df):
    if df.empty:
        return html.Div('Cars with these filters don\'t exist.')
    else:
        color_df = df.groupby('color').count().sort_values('country', ascending=False).head(10)
        fig = px.bar(x=color_df.index.to_list(), y=color_df.country.to_list(), labels={"x": "Color", "y": "Count"})

        return dcc.Graph(figure=fig)
