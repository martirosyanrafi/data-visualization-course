import json
import filter
import numpy as np
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

with open('data/states.json') as f:
    states = json.load(f)


def get_html_content(df):
    return html.Div([
        html.H1('State'),
        html.Br(),
        filter.get_html_content(df, 'state'),
        html.Div(id='state-output-container'),
        html.Br(),
        html.Br(),
        html.H6('This map shows the distribution of cars in US by states based on the selected filters.')
    ])


def get_output_content(df):
    if df.empty:
        return html.Div('Cars with these filters don\'t exist.')
    else:
        state_df = df.groupby('state').count()
        locations = np.vectorize(lambda state: states[state] if state in states else None)(np.array(state_df.index))

        fig = px.choropleth(locations=locations, locationmode="USA-states", color=state_df.country, scope="usa")

        return dcc.Graph(figure=fig)
