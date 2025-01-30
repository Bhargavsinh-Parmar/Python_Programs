import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import base64
import io
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Upload CSV or Excel File to Update Graph"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
                    
        },
        multiple=False  # Single file upload
    ),
    html.Div(id='output-data-upload'),
    html.Label('Select Plot Type:'),
    dcc.Dropdown(
        id='plot-type',
        options=[
            {'label': 'Bar Plot', 'value': 'bar'},
            {'label': 'Line Plot', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'}
        ],
        value='bar'
    ),
    dcc.Graph(id='output-graph')
])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an Excel file
            df = pd.read_excel(io.BytesIO(decoded))
        return df
    except Exception as e:
        print(e)
        return None

@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def display_table(contents, filename):
    if contents is None:
        return html.Div()

    df = parse_contents(contents, filename)
    if df is None:
        return html.Div(['There was an error processing this file.'])

    return html.Div([
        html.H5(filename),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10
        )
    ])

@app.callback(
    Output('output-graph', 'figure'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    Input('plot-type', 'value')
)
def update_graph(contents, filename, plot_type):
    if contents is None:
        return {}

    df = parse_contents(contents, filename)
    if df is None:
        return {}

    if plot_type == 'bar':
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title='Uploaded Data Graph')
    elif plot_type == 'line':
        fig = px.line(df, x=df.columns[0], y=df.columns[1], title='Uploaded Data Graph')
    elif plot_type == 'scatter':
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title='Uploaded Data Graph')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
