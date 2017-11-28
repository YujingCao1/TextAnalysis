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

#==============================================================================
# df = pd.read_csv(
#         'https://gist.githubusercontent.com/chriddyp/'
#     'c78bf172206ce24f77d6363a2d754b59/raw/'
#     'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
#     'usa-agricultural-exports-2011.csv')
#==============================================================================

emma = wd.clean_data()
caesar = wd.clean_data()
emma_top10 = wd.fdist_top(emma, 10)
word_list = [emma_top10[i][0] for i in range(0,len(emma_top10))]
likelihood_ratio = wd.log_likelihood_ratio(word_list, emma, caesar)
lr_df = pd.DataFrame(likelihood_ratio, index=[1])
lr_word = lr_df.columns.get_values().tolist()
lr_value = round(lr_df.loc[1,:],3).tolist()
lr_df_reshape = pd.DataFrame({
        'Likelihood Ratio': lr_value,
        'Word': lr_word})


def generate_table(dataframe, max_rows=10):
    return html.Table(
            # Header
            [html.Tr([html.Th(col) for col in dataframe.columns])] + 
            
            # Body
            [html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))]
            )

    
app = dash.Dash()

app.layout = html.Div(children = [
        html.H4(children='Word Usage Comparison'),
        generate_table(lr_df_reshape)
])
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    
#%%
# newdict = {1:0,2:0,3:0}
# for key in newdict.keys():
#     print
# import pandas as pd
# s = pd.Series(newdict, name = 'Likelihood Ratio')
# s.index.name = 'Word'
# s.reset_index()
 


