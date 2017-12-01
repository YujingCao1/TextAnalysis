# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:24:40 2017

@author: caoyujin
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import wordusagecomparison as wd
import pandas as pd

#emma = wd.clean_data()
#caesar = wd.clean_data()
#emma_top10 = wd.fdist_top(emma, 20)
#word_list = [emma_top10[i][0] for i in range(0,len(emma_top10))]
#likelihood_ratio = wd.log_likelihood_ratio(word_list, emma, caesar)
#lr_df = pd.DataFrame(likelihood_ratio, index=[1])
#lr_word = lr_df.columns.get_values().tolist()
#lr_value = round(lr_df.loc[1,:],3).tolist()
#lr_df_reshape = pd.DataFrame({
#        'Likelihood Ratio': lr_value,
#        'Word': lr_word})


def generate_table(dataframe, max_rows=50):
    return html.Table(
            # Header
            [html.Tr([html.Th(col) for col in dataframe.columns])] + 
            
            # Body
            [html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))]
            )

app = dash.Dash()

app.layout = html.Div([
        html.Div([
                 dcc.Upload(html.Button(id = 'submit-Button1', n_clicks = 0, children = 'Select an Analysis File')),
                 html.Div(id = 'analysis-file')
                ],
            style = {
                    'width': '30%',
                    'height': '30%',
                    'textAlign': 'center'
                    }),
        
        html.Div([
                   dcc.Upload(html.Button(id = 'submit-Button2', n_clicks = 0, children = 'Select a Reference File')),
                   html.Div(id = 'reference-file')
                ]),
    
        html.Div([
                 html.Label('List the Top N Most Occuring Words'),
                 html.Br(),
                 dcc.Input(id = 'no_words', type = 'text', value = 10)
                ]),
        
       html.Div([ html.H4(children='Word Usage Comparison')
        ])
    ])
    
if __name__ == "__main__":
    app.run_server(debug=True)
    


