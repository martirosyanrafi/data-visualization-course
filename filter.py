import numpy as np
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def get_html(df):
    return html.Div([
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='brand-dropdown',
                    placeholder='Brand',
                    options=np.vectorize(lambda v: {'label': v.title(), 'value': v})(df.brand.unique())
                )
            ),
            dbc.Col(
                dcc.Dropdown(
                    id='color-dropdown',
                    placeholder='Color',
                    options=np.vectorize(lambda v: {'label': v, 'value': v})(np.sort(df.color.unique()))
                )
            ),
            dbc.Col(
                dcc.Dropdown(
                    id='state-dropdown',
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
                    id='price-range-slider',
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
                    id='year-range-slider',
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
