# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:37:11 2017

@author: caoyujin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:26:55 2017

@author: caoyujin

Use this file to find the overpresented words
"""

# Text Analysis

#%%
import os
os.chdir("C:\\Users\\caoyujin\\Desktop\\TextAnalysis")

#%%
# file choose in Python. A Tk dialoge will open and allow users to select a file
from tkinter import filedialog
from tkinter import *
print("You'll need to fine the necessary data files on your own copmuter")
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))

# Read a text file into a data frame 
import nltk
import re

emma = open(root.filename, "r")
emma_string = emma.read().lower()


# Remove punctuations
import string
translator = str.maketrans('', '', string.punctuation)
emma_string_no_punct = emma_string.translate(translator) # string
emma_string_no_stopwords = re.findall(r'\b[a-z]{3,15}\b', emma_string_no_punct) # list. Remove all the words that only have one or two letters.
emma_string_no_stopwords = ' '.join(emma_string_no_stopwords) # convert a list to string

# Tokenize the words
from nltk.tokenize import word_tokenize
tokenize_emma = word_tokenize(emma_string_no_stopwords)

# Remove stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('English'))
tokenize_emma_clean = [w for w in tokenize_emma if not w in stop_words]

# Calculate word frequency
fdist = nltk.FreqDist(tokenize_emma_clean)
fdist.most_common(20) # Find the top 10 most occuring words
#len(tokenize_emma_clean)

    
#%%

# Import reference text
# Use shakespeare-caesar as reference text
from tkinter import filedialog
from tkinter import *
print("You'll need to fine the necessary data files on your own copmuter")
root1 = Tk()
root1.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))

#%%
# Read a text file into a data frame 
import nltk
import re

caesar = open(root1.filename, "r")
caesar_string = caesar.read().lower()

# Remove punctuations
import string
translator = str.maketrans('', '', string.punctuation)
caesar_string_no_punct = caesar_string.translate(translator) # string
caesar_string_no_stopwords = re.findall(r'\b[a-z]{3,15}\b', caesar_string_no_punct) # list. Remove all the words that only have one or two letters.
caesar_string_no_stopwords = ' '.join(caesar_string_no_stopwords) # convert a list to string

# Tokenize the words
from nltk.tokenize import word_tokenize
tokenize_caesar = word_tokenize(caesar_string_no_stopwords)

# Remove stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('English'))
tokenize_caesar_clean = [w for w in tokenize_caesar if not w in stop_words]
#%%
fdist_caesar = nltk.FreqDist(tokenize_caesar_clean)
fdist_caesar.most_common(20)

#%%
# Word Usage Comparison
# Use "could" as an example
emma_could = fdist['could']
emma_no_could = len(tokenize_emma_clean) - emma_could

caesar_could = fdist_caesar['could']
caesar_no_could = len(tokenize_caesar_clean) - caesar_could

import numpy as np
import scipy
from scipy.stats import chi2_contingency
caeser_emma = np.array([[emma_could, emma_no_could],
                       [caesar_could, caesar_no_could]])
g, p, dof, expected = chi2_contingency(caeser_emma, lambda_= 'log-likelihood')
# Note p is significantly less than 0.0001, thus occurrences of 'could' in Emma and Caeser is different.

#%%
# Calculate log likelihood ratio (G-test)
# G = 2*sum(O_i*ln(O_i/E_i))
import math
2*(emma_could*math.log(emma_could/expected[0,0]) + caesar_could*math.log(caesar_could/expected[1,0]))

#%%


#%%
# Define a function to get G-test for a list of words

