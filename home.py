import filter
import dash_table
import dash_html_components as html


def get_html_content(df):
    return html.Div([
        filter.get_html_content(df, 'home'),
        html.Div(id='home-output-container')
    ])


def get_output_content(df):
    if df.empty:
        return html.Div('Cars with these filters don\'t exist.')
    else:
        return dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=20
        )
