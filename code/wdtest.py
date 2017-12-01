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
import base64
import io,os
import nltk,re, string, scipy
import numpy as np
from tkinter import filedialog
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from scipy.stats import chi2_contingency


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
                 html.Button(id = 'button1', n_clicks = 0 ,children = 'Select an Analysis File'),
                 html.Div(id = 'analysis-file')
            ]),
        
        html.Div([
                  html.Button(id = 'button2', n_clicks = 0, children = 'Select a Reference File'),
                   html.Div(id = 'reference-file')
                ]),
    
        html.Div([
                 html.Label('List the Top N Most Occuring Words'),
                 html.Br(),
                 dcc.Input(id = 'no_words', type = 'text', value = 10)
                ]),
        
       html.Div([ html.H4(children='Word Usage Comparison'),
        ])
    ])
    
def parse_contents():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    try:
        if filename.endswith('.txt'):
            file = open(filename, "r")
            file_string = file.read().lower()
            translator = str.maketrans('', '', string.punctuation) # Remove punctuations
            file_string_no_punct = file_string.translate(translator) # string
            file_string_no_stopwords = re.findall(r'\b[a-z]{2,15}\b', file_string_no_punct) # list. Remove all the words that only have one letter.
            file_string_no_stopwords = ' '.join(file_string_no_stopwords) # convert a list to string
            tokenize_file = word_tokenize(file_string_no_stopwords) # Tokenize words
            stop_words = set(stopwords.words('English')) # Remove stop words
            tokenize_file_clean = [w for w in tokenize_file if not w in stop_words]
            
    except Exception as e:
        print(e)
        return html.Div([
                'There was an error processing this file.'
                ])
    return html.Div([
            html.H5(os.path.basename(filename))]
    )

@app.callback(
    Output(component_id='analysis-file', component_property='children'),
    [Input('button1', 'n_clicks')]
)
def update_analysis(no_click):
    if no_click != 0:
        children = [
                parse_contents()
                ]
        return children

@app.callback(
        Output(component_id='reference-file', component_property='children'),
        [Input('button2', 'n_clicks')]
)
def update_reference(no_click):
    if no_click!=0:
        children = [
                parse_contents()
                ]
        return children
    
if __name__ == "__main__":
    app.run_server(debug=True)
    


