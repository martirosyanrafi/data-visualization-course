import dash

import filter
import home
import model
import styles
import sidebar
import mileage
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

df = pd.read_csv('data/dataset.csv', index_col=0)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'US Cars'

sidebar = sidebar.get_html_content()
content = html.Div(id="page-content", style=styles.CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(filter.get_output('home'), filter.get_inputs('home'))
def update_output(brand, color, state, year, price):
    return home.get_output_content(filter.get_df(df, brand, color, state, year, price))


@app.callback(filter.get_output('model'), filter.get_inputs('model'))
def update_output(brand, color, state, year, price):
    return model.get_output_content(filter.get_df(df, brand, color, state, year, price))


@app.callback(filter.get_output('mileage'), filter.get_inputs('mileage'))
def update_output(brand, color, state, year, price):
    return mileage.get_output_content(filter.get_df(df, brand, color, state, year, price))


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.get_html_content(df)
    elif pathname == "/model":
        return model.get_html_content(df)
    elif pathname == "/mileage":
        return mileage.get_html_content(df)

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)
