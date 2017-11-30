# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:21:27 2017

@author: caoyujin
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
        dcc.Input(id = 'my-id', value = 'Enter your text here', type = 'text'),
        html.Div(id = 'my-div')
        ]
)

@app.callback(
        Output(component_id='my-div', component_property='children'),
        [Input(component_id='my-id', component_property='value')]
)

def update_output_value(input_value):
    return 'You have entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)
    
