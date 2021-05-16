import filter
import dash_table
import dash_html_components as html


def get_html(df):
    return html.Div([
        filter.get_html(df),
        html.Div(id='output-container')
    ])


def get_output_content(df):
    return dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=20
    )
