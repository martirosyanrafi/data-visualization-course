import styles
import dash_html_components as html
import dash_bootstrap_components as dbc


def get_html_content():
    return html.Div(
        [
            html.H2("US Cars", className="display-4"),
            html.Hr(),
            html.P(
                "Scraped from AUCTION EXPORT.com", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Model", href="/model", active="exact"),
                    dbc.NavLink("Mileage", href="/mileage", active="exact"),
                    dbc.NavLink("Color", href="/color", active="exact"),
                    dbc.NavLink("State", href="/state", active="exact")
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=styles.SIDEBAR_STYLE,
    )
