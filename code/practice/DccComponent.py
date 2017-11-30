# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:02:40 2017

@author: caoyujin
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
        html.Label('Dropdown'),
        dcc.Dropdown(
                options = [
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal',  'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SFO'}
                        ],
                value = 'MTL'
                ),
        
        html.Label('Multiple Dropdown'),
        dcc.Dropdown(
                options = [
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SFO'}
                        ],
                value = ['MTL', 'SFO'],
                multi = True
                ),
        
        html.Label('Radio Items'),
        dcc.RadioItems(
                options = [
                        {'label': 'New Yokr City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SFO'}
                        ],
                value = 'MTL'
                ),
        
        html.Label('Checkbox'),
        dcc.Checklist(
                options = [
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SFO'}
                        ],
                values = ['MTL', 'SFO']
                ),
        
        html.Label('Text Input'),
        dcc.Input(value = 'MTL', type = 'text'),
        
        html.Label('Sliding Bar'),
        dcc.Slider(
                min = 0,
                max = 9,
                marks = {i: 'Label{}'.format(i) if i==1 else str(i) for i in range(1,6)},
                value = 5,
            ),
        ],style = {'columnCount': 2})
        

if __name__ == '__main__':
    app.run_server(debug=True)