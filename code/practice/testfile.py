import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

import datetime
import base64
import json
import pandas as pd
import plotly
import io
from chardet.universaldetector import UniversalDetector

app = dash.Dash()

app.scripts.config.serve_locally = True

app.layout = html.Div([
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
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

def encodingDetectorByLine(filename):
    """
    filename: name of the file that needs to be decided what encode method is
    
    return the encode method name
    """
    detector = UniversalDetector()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    encodeName = detector.result['encoding']
    return encodeName

def parse_contents(filename):
    encodeRule = encodingDetectorByLine(filename)
    file = open(filename, "r", encoding = encodeRule)
    file_string = file.read().lower()
    return html.Div([
        html.H5(filename),
        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(file_string + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all',
            'whiteSpace': 'normal'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'filename')])

def update_output(list_of_names):
    children = [
        parse_contents(list_of_names)]
    return children


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)