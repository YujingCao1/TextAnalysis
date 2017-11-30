# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:27:03 2017

@author: caoyujin
"""
import wordusagecomparison as wd
import dash
import dash_core_components as dcc
import dash_html_components as html


import pandas as pd

emma = wd.clean_data()
caesar = wd.clean_data()
emma_top10 = wd.fdist_top(emma, 20)
word_list = [emma_top10[i][0] for i in range(0,len(emma_top10))]
likelihood_ratio = wd.log_likelihood_ratio(word_list, emma, caesar)
lr_df = pd.DataFrame(likelihood_ratio, index=[1])
lr_word = lr_df.columns.get_values().tolist()
lr_value = round(lr_df.loc[1,:],3).tolist()
lr_df_reshape = pd.DataFrame({
        'Likelihood Ratio': lr_value,
        'Word': lr_word})


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

app.scripts.config.serve_locally = True

markdown_text = '''

Word usage comparison app allows users to upload the artical of interest to copmare
words usage with reference files.

'''
    
app.layout = html.Div(children = [
        html.H4(children='Word Usage Comparison'),
        dcc.Markdown(children = markdown_text),
        generate_table(lr_df_reshape)
])
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    


