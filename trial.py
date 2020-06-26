# -------------------------------------------------------
# Author: Ashley Jablonski
# Program: bdg.py
# Description: NLP-based program to create a script of 
#       Brian David Gilbert's Polygon Unraveled videos
# -------------------------------------------------------

# IMPORTS
from pathlib import Path
import nltk
from stop import stop_words
# print(stop_words)

import logging
logging.basicConfig(filename = "log_trial.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename = "log_trial.txt", level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start of program")
 
# TODO: get transcripts + transcripts into lists
bowser = open("bowser.txt", encoding="utf8")
    
# list comprehension: joins words in file
all_word_list = '\n'.join([item for item in bowser])
logging.debug("file running: %s" %(all_word_list))

# TODO: remove stop-words from lists
removed_list = [word for word in all_word_list if word not in stop_words]
logging.debug("file after stop_words removed: %s" %(removed_list))

# TODO: use bigram? trigram? model << try bi first then tri
file_bigram = nltk.bigrams(removed_list)
logging.debug("file bigram: %s" %(file_bigram))


master_cfd = nltk.ConditionalFreqDist(file_bigram)
print(master_cfd)
logging.debug("trial with 0 index as only input to cfd... %s" %(master_cfd))
logging.debug("trial of entering next string as master_cfd[0][1]: %s" %(master_cfd[0][1]))
logging.error("master_cfd doesn't hold all data; ValueError: too many values to unpack (expected 2)")

# TODO: function for generating text - params: cfd, length of generated text, 
#           starting word, sz << sz is how many words from cfd are grabbed
def script_generator(cfd, script_length, start_word='', size=10):
    # TODO: if no starting word, get random one
    
    pass
    # TODO: loop thru num of desired words and use prev word as next key

    # TODO: call function and print out result (to file?)