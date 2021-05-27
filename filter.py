import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


def get_html_content(df, name):
    return html.Div([
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id=name + '-brand-dropdown',
                    multi=True,
                    placeholder='Brand',
                    options=np.vectorize(lambda v: {'label': v.title(), 'value': v})(df.brand.unique())
                )
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=name + '-color-dropdown',
                    multi=True,
                    placeholder='Color',
                    options=np.vectorize(lambda v: {'label': v, 'value': v})(np.sort(df.color.unique()))
                )
            ),
            dbc.Col(
                dcc.Dropdown(
                    id=name + '-state-dropdown',
                    multi=True,
                    placeholder='State',
                    options=np.vectorize(lambda v: {'label': v.title(), 'value': v})(df.state.unique())
                )
            )
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.P("Price"),
                dcc.RangeSlider(
                    id=name + '-price-range-slider',
                    min=1000,
                    max=100000,
                    value=[1000, 100000],
                    marks={
                        1000: '1000$',
                        100000: '100000$'
                    }
                )
            ]),
            dbc.Col([
                html.P("Year"),
                dcc.RangeSlider(
                    id=name + '-year-range-slider',
                    min=1970,
                    max=2020,
                    value=[1970, 2020],
                    marks={
                        1970: '1970',
                        2020: '2020'
                    }
                )
            ])
        ]),
        html.Br()
    ])


def get_df(df, brand, color, state, year, price):
    return df[(brand is None or df.brand.isin(brand)) &
              (color is None or df.color.isin(color)) &
              (state is None or df.state.isin(state)) &
              (df.price > price[0]) &
              (df.price < price[1]) &
              (df.year > year[0]) & (df.year < year[1])]


def get_output(name):
    return Output(name + '-output-container', 'children')


def get_inputs(name):
    return [
        Input(name + '-brand-dropdown', 'value'),
        Input(name + '-color-dropdown', 'value'),
        Input(name + '-state-dropdown', 'value'),
        Input(name + '-year-range-slider', 'value'),
        Input(name + '-price-range-slider', 'value')
    ]
