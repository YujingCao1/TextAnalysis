# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:19:40 2017

@author: caoyujing

Text Analysis
"""
#%%
# Download nltk corpora
# This step is not necessary if you have your own corpus. 
#import nltk
#nltk.download()

#%%
# Import all the modules
import nltk,re, string, scipy
import pandas as pd
import numpy as np
from tkinter import filedialog
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from scipy.stats import chi2_contingency, mannwhitneyu
import os
from chardet.universaldetector import UniversalDetector
from statsmodels.sandbox.stats.multicomp import multipletests
# Function clean_data can be used to import analysis or reference text (baseline)
# Remove stop words and punctuations

def clean_data():
    """
    output: clean file without stop words or punctuations
    """
    
    print("Please Select analysis/reference file")
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
    encodeRule = encodingDetectorByLine(root.filename)
    file = open(root.filename, "r", encoding = encodeRule)
    file_string = file.read().lower()
    translator = str.maketrans('', '', string.punctuation) # Remove punctuations
    file_string_no_punct = file_string.translate(translator) # string
    file_string_no_stopwords = re.findall(r'\b[a-z]{2,15}\b', file_string_no_punct) # list. Remove all the words that only have one letter.
    file_string_no_stopwords = ' '.join(file_string_no_stopwords) # convert a list to string
    tokenize_file = word_tokenize(file_string_no_stopwords) # Tokenize words
    stop_words = set(stopwords.words('English')) # Remove stop words
    tokenize_file_clean = [w for w in tokenize_file if not w in stop_words]
    return tokenize_file_clean

# Function fdist_top(file, top_n) finds the top n most occurring words

def fdist_top(file, top_n):
    
    """
    Parameters:   
       file: file name of a tokenized file
       top_n: a number that defines how many most common words shown
    """
    fdist = nltk.FreqDist(file)
    most_common_words = fdist.most_common(top_n)
    return most_common_words

# Function log_likelihood_ratio returns G-test statistics
def log_likelihood_ratio(wordVec, file1, file2):
    
    """
    Parameter:
        wordVec: a list of words for usage comparisons
        file1: analysis text that has been cleaned by clean_data()
        file2: clean reference text (baseline) that has been cleaned by clean_data()
    
    Output:
        g_dict: a dictionary to store words and corresponding log likelihood ratios
    """
    g_test = []
    p_test = []
    
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
        p_test.append(p)
        g_test.append(g)
    
    # Multiple testing adjustment with Bonferroni test
    p_test_adjust = multipletests(p_test, alpha = 0.05, method = 'bonferroni', is_sorted = False, returnsorted = False)
    adjust_pval = np.asarray(p_test_adjust)[1] # Extract adjusted p-values from tuple
    g_dict = dict(zip(wordVec, g_test))
    p_dict = dict(zip(wordVec, adjust_pval))
    return g_dict, p_dict
        

# Function ftag_dist finds the top n most occurring words based on the tag name
# For example, top 10 most common used adjective

def ftag_dist(file, tag_name, top_n):
    
    """
    parameter:
        file: tokenized words 
        tag_name: JJ(adjective), RB(adverb), CC(conjunction), IN(preposition), NN(noun) etc.
        top_n: a number that defines how many most common words shown

    Post-Of-Speech Tag    
    
    This function is slow because of the tagging and tokenization part.
    It needs to be revised. Something is not right!
    """
    file_tag = nltk.pos_tag(file)
    word_list = [word for (word,tag) in file_tag if tag == tag_name]
    word_string = ' '.join(word_list)
    word_tokenize = nltk.word_tokenize(word_string)
    word_fdist = nltk.FreqDist(word_tokenize)
    most_commn_words = word_fdist.most_common(top_n)
    return(most_commn_words)

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


#==============================================================================
#   #%%
#    emma = clean_data()
#    caesar = clean_data()
#    emma_top10 = fdist_top(emma, 20)
#    word_list = [emma_top10[i][0] for i in range(0,len(emma_top10))]
#    #%%
#    likelihood_ratio = log_likelihood_ratio(word_list, emma, caesar)
#    #print(likelihood_ratio[1])
#    #%%
#    lr_df = pd.DataFrame(np.asarray(likelihood_ratio)[0], index=[1])
#    print(lr_df)
#    lr_word = lr_df.columns.get_values().tolist()
#    lr_value = round(lr_df.loc[1,:],3).tolist()
#    
#    pval_df = pd.DataFrame(np.asarray(likelihood_ratio)[1], index=[1])
#    print(pval_df)
#    p_value = pval_df.loc[1,:].tolist()
#    #%%
#    lr_df_reshape = pd.DataFrame({
#            'Word': lr_word,
#            'Likelihood Ratio': lr_value,
#            'P-value': p_value
#            })
#    print(lr_df_reshape)
#    
#    #%%
#    mann_whitney_rho(word_list, emma, caesar)
#    #%%
#    mannwhitneyu(np.arange(1), np.arange(1,2))[1]
#   
#==============================================================================
