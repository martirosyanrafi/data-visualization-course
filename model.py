import dash_html_components as html
import dash_core_components as dcc


def get_html(df):
    return html.Div([
        dcc.Dropdown(
            id='demo-dropdown',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='NYC'
        ),
        html.Div(id='dd-output-container')
    ])
