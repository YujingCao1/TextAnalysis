# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:32:02 2017

@author: caoyujin
"""

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

all_options = {
        'America': ['New York City', 'San Francisco', 'Cincinnati'],
        'Canada': ['Montreal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
        dcc.RadioItems(
                id = 'countries-dropdown',
                options = [{'label': k, 'value': k} for k in all_options.keys()],
                value = 'America'),
                
        html.Hr(),
        
        dcc.RadioItems(id = 'cities-dropdown'),
        
        html.Hr(),
        
        html.Div(id = 'display-selected-values')
        
])


@app.callback(
        dash.dependencies.Output('cities-dropdown', 'options'),
        [dash.dependencies.Input('countries-dropdown', 'value')])

def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
        dash.dependencies.Output('display-selected-values', 'children'),
        [dash.dependencies.Input('countries-dropdown','value'),
         dash.dependencies.Input('cities-dropdown', 'value')])
    
def set_display_children(selected_country, selected_city):
    return '{} is a city in {}'.format(
            selected_city, selected_country,
            )
    
    
if __name__ == "__main__":
    app.run_server(debug=True)