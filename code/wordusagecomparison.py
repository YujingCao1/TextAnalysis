# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:19:40 2017

@author: caoyujin

Text Analysis
"""

#%%
# Import all the modules
import nltk,re, string, scipy
import numpy as np
from tkinter import filedialog
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from scipy.stats import chi2_contingency

# Function clean_data can be used to import analysis or reference text (baseline)
# Remove stop words and punctuations

def clean_data():
    
    print("You'll need to fine the necessary data files on your own copmuter")
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    file = open(root.filename, "r")
    file_string = file.read().lower()
    translator = str.maketrans('', '', string.punctuation) # Remove punctuations
    file_string_no_punct = file_string.translate(translator) # string
    file_string_no_stopwords = re.findall(r'\b[a-z]{3,15}\b', file_string_no_punct) # list. Remove all the words that only have one or two letters.
    file_string_no_stopwords = ' '.join(file_string_no_stopwords) # convert a list to string
    tokenize_file = word_tokenize(file_string_no_stopwords) # Tokenize words
    stop_words = set(stopwords.words('English')) # Remove stop words
    tokenize_file_clean = [w for w in tokenize_file if not w in stop_words]
    return tokenize_file_clean

# Function fdist_top(file, top_n) finds the top n most occurring words

def fdist_top(file, top_n):
    
    """
    Parameters:   
       file: file name 
       top_n: the number of most occurring words
    """
    fdist = nltk.FreqDist(file)
    most_common_words = fdist.most_common(top_n)
    return most_common_words

# Function log_likelihood_ratio returns G-test
# Parameter: wordVec is a list of word for usage comparisons

def log_likelihood_ratio(wordVec, file1, file2):
    
    """
    Parameter:
        wordVec: a list of words for usage comparisons
        file1: tokenized analysis text
        file2: tokenized reference text (baseline)
    
    Output:
        g_dict: a dictionary to store words and corresponding log likelihood ratio
    """
    g_test = []
    
    file1_dist = nltk.FreqDist(file1) # frequency distribution of all the words
    file2_dist = nltk.FreqDist(file2)
    
    file1_len = len(file1)
    file2_len = len(file2)
    
    for w in wordVec:
        file1_w = file1_dist[w]
        file1_no_w = file1_len - file1_w
        file2_w = file2_dist[w]
        file2_no_w = file2_len - file2_w
        
        contigency_table = np.array([[file1_w, file1_no_w],
                                [file2_w, file2_no_w]])
        g, p, dof, expected = chi2_contingency(contigency_table, lambda_= 'log-likelihood')
        g_test.append(g)
    g_dict = dict(zip(wordVec, g_test))
    return g_dict

#%%
#Testing Example:
    
emma = clean_data()
caesar = clean_data()
word_list = fdist_top(emma, 10)
word_list_test = [word_list[i][0] for i in range(len(word_list))]
g_stats = log_likelihood_ratio(wordVec = word_list_test, file1 = emma, file2 = caesar)   
print(g_stats)
