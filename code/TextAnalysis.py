# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:41:07 2017

@author: Yujing Cao

This is a file to test how to work with Stanford NER in Python
"""


#%%
# Stanford Named Entity Recognizer

import nltk
import scrapy

nltk.download()

# Use NLTK for performing Named Entity Recognition
import re
import time

exampleArray = ['The incredibly intimidating NLP scares people away who are sissies.']
 
contentArray =['Starbucks is not doing very well lately.',
               'Overall, while it may seem there is already a Starbucks on every corner, Starbucks still has a lot of room to grow.',
               'They just began expansion into food products, which has been going quite well so far for them.',
               'I can attest that my own expenditure when going to Starbucks has increased, in lieu of these food products.',
               'Starbucks is also indeed expanding their number of stores as well.',
               'Starbucks still sees strong sales growth here in the united states, and intends to actually continue increasing this.',
               'Starbucks also has one of the more successful loyalty programs, which accounts for 30%  of all transactions being loyalty-program-based.',
               'As if news could not get any more positive for the company, Brazilian weather has become ideal for producing coffee beans.',
               'Brazil is the world\'s #1 coffee producer, the source of about 1/3rd of the entire world\'s supply!',
               'Given the dry weather, coffee farmers have amped up production, to take as much of an advantage as possible with the dry weather.',
               'Increase in supply... well you know the rules...',]

def processLanguage():
    try:
        for item in contentArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            
            print(tagged)
            
            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()
            
            time.sleep(1)
            
    except Exception as e:
        print(str(e))

processLanguage()

#%%
# Using Stanford NER module with NLTK
#import nltk
from nltk.tokenize import word_tokenize
from nltk.tag.stanford import StanfordNERTagger

#nltk.download() # download modules

# Set the JAVAHOME environment variable
import os
java_path = "C:\\Program Files\\Java\\jre1.8.0_141\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

stanford_classifier = 'C:\\Users\\caoyujin\\Desktop\\NER\\stanford-ner-2017-06-09\\stanford-ner-2017-06-09\\classifiers\\english.all.3class.distsim.crf.ser.gz'
stanford_ner_path = 'C:\\Users\\caoyujin\\Desktop\\NER\\stanford-ner-2017-06-09\\stanford-ner-2017-06-09\\stanford-ner.jar'


st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding = 'utf-8')

tokenzied_text = word_tokenize("While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.")
classified_text = st.tag(tokenzied_text)

print(classified_text)
print(pos_tag(tokenzied_text)) # Part-of-speech tag

#%%
store = []
for i in range(0,len(classified_text)):
    tag = classified_text[i][1]
    if tag == 'LOCATION':
        print(classified_text[i])
        store.append(classified_text[i][0])
print(store)

