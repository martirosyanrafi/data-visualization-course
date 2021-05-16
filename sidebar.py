import dash_html_components as html
import dash_bootstrap_components as dbc
import styles


def get_html():
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
                    dbc.NavLink("Page 2", href="/page-2", active="exact")
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=styles.SIDEBAR_STYLE,
    )
