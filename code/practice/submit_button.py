# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:50:02 2017

@author: caoyujin
"""

import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
        dcc.Input(id = 'input-1', type = 'text', value = 'New York City'),
        dcc.Input(id = 'input-2', type = 'text', value = 'America'),
        html.Button(id = 'submit-Button', n_clicks = 0, children = 'Submit'),
        html.Div(id = 'output-display')
])

@app.callback(
        Output('output-display', 'children'),
        [Input('submit-Button', 'n_clicks')],
        [State('input-1', 'value'),
         State('input-2', 'value')
        ])

def update_output(no_clicks, selected_city, selected_country):
    return '''The button has been clicked {} times,
            {} is a city in {}'''.format(no_clicks, selected_city, selected_country)
            
if __name__ == '__main__':
    app.run_server(debug=True)