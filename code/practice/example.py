# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:26:55 2017

@author: caoyujin
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

#%%
# Read a text file into a data frame 
import nltk
import re

file = open(root.filename, "r")
text_string = file.read().lower()

#%%

# Remove punctuations
import string
translator = str.maketrans('', '', string.punctuation)
text_string_no_punct = text_string.translate(translator) # string
text_string_no_stopwords = re.findall(r'\b[a-z]{3,15}\b', text_string_no_punct) # list. Remove all the words that only have one or two letters.
text_string_no_stopwords = ' '.join(text_string_no_stopwords) # convert a list to string

# Tokenize the words
from nltk.tokenize import word_tokenize
tokenize_text = word_tokenize(text_string_no_stopwords)

# Remove stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('English'))
tokenize_text_clean = [w for w in tokenize_text if not w in stop_words]

#%%
# Calculate word frequency
fdist = nltk.FreqDist(tokenize_text_clean)
fdist.most_common(20) # Find the top 10 most occuring words
len(tokenize_text_clean)

    
#%%

