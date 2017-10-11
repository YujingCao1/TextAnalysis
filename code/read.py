# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:25:53 2017

@author: Yujing Cao

This is a file to clean dataset and create the corpus.
"""

#%%
import os
os.chdir("C:\\Users\\caoyujin\\Desktop\\NER")

#%%
# file choose in Python. A Tk dialoge will open and allow users to select a file
from tkinter import filedialog
from tkinter import *
print("You'll need to fine the necessary data files on your own copmuter")
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))

#%%
# Read a text file into a data frame 
import pandas as pd
import numpy as np
file = open(root.filename, "r")
colNames = ["Documents", "Authors", "DocDates", "Genres", "TotalsPerDoc", "LongTitles"]
Metadata = pd.read_table(file, sep = '\t', header = None, names = colNames)

# Add a new column to the data from that stores the short title    
Metadata.loc[:,'Titles'] = [element[0:30] for element in Metadata.loc[:,'LongTitles']] # substring

Metadata_df = pd.DataFrame(Metadata, columns = colNames)
Documents = Metadata_df["Documents"]
TotalsPerDoc = Metadata_df["TotalsPerDoc"]
Titles = [element[0:30] for element in Metadata_df['LongTitles']]
LongTitles = Metadata_df["LongTitles"]
Authors = Metadata_df["Authors"]
DocDates = Metadata_df["DocDates"]
Genres = Metadata_df["Genres"]


#%%

# Import NassrData
DummyVar = input("Ready to select NassrData? ")
rootfile = Tk()
rootfile.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))

#%%
Sparse = pd.read_table(rootfile.filename, sep = '\t', header = None)
Sparse_df = pd.DataFrame(Sparse)

DocIDs_unique = Sparse_df[0].unique()
DocIDs = Sparse_df[0]

Words_unique = Sparse_df[1].unique()
Words = Sparse_df[1]

Occurrence = Sparse_df[2]

#%%
from collections import Counter
# The following for llop cycles through all the documents
DocCount = len(Documents)
WordCount = len(Words_unique)
# Unapcking data
occur = np.zeros(shape = (DocCount, WordCount))

for i in range(0, DocCount):
    Doc = Documents[i]
    ThisDocWords = Words[DocIDs == Doc]
    ThisDocOccurrences = Occurrence[DocIDs == Doc]
    ThisDocOccurrences_named = dict(zip(ThisDocWords, ThisDocOccurrences)) # give each element in the list a name
    
    Unpacked = [0]*WordCount # create a list of zeros
    Unpacked_named = dict(zip(Words_unique, Unpacked))
    
    Unpacked_selected = {k: Unpacked_named[k] for k in ThisDocWords}
    
    Unpacked_update = {k: Unpacked_selected.get(k,0) + ThisDocOccurrences_named.get(k,0) for k in set(Unpacked_named)}
    occur[i,:] = list(Unpacked_update.values())
print(occur.shape)
       

#%%

# Create a data frame to store all the tokens and find the most common authors
# name TotalsPerDoc
TotalsPerDoc_named = dict(zip(Documents, TotalsPerDoc))
TotalsPerDoc_selected = {k: TotalsPerDoc_named[k] for k in DocIDs}
TotalsPerDoc_value = list(TotalsPerDoc_selected.values())
dat = {'tokens': TotalsPerDoc_value, 
       'id': DocIDs_unique, 
       'author': Authors,
       'date': DocDates,
       'titel': Titles}
Meta = pd.DataFrame(dat)

BaseDate = DocDates.min()-1
DateRange = DocDates.max() - BaseDate

AuthorTable = Counter(Authors) # Turn a list into table
AuthorTable_sorted = sorted(AuthorTable.items(), key=lambda pair: pair[1], reverse=True) # sort the table by descending

print('Here are a few of the most common authors in this dataset')
print(AuthorTable_sorted[0:20])

