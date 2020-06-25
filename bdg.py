# -------------------------------------------------------
# Author: Ashley Jablonski
# Program: bdg.py
# Description: NLP-based program to create a script of 
#       Brian David Gilbert's Polygon Unraveled videos
# -------------------------------------------------------

# IMPORTS
import pylab
import nltk
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('treebank')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('all')
from nltk.book import *
from nltk.probability import FreqDist
import random
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# TODO: get transcripts + transcripts into lists

# IDEA: use for loop to go thru each one

# TODO: tokenize words ??

# TODO: remove stop-words from lists

# TODO: use bigram? trigram? model << try bi first then tri

# TODO: add to Conditional Freq Model (CFD)

# TODO: function for generating text - params: cfd, length of generated text, 
#           starting word, sz

# TODO: if no starting word, get random one

# TODO: loop thru num of desired words and use prev word as next key

# TODO: call function and print out result (to file?)