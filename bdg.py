# -------------------------------------------------------
# Author: Ashley Jablonski
# Program: bdg.py
# Description: NLP-based program to create a script of 
#       Brian David Gilbert's Polygon Unraveled videos
# -------------------------------------------------------

# IMPORTS
from pathlib import Path
import nltk, random
from stop import stop_words

import logging
logging.basicConfig(filename = "log_bdg14.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename = "log_bdg14.txt", level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug("Start of program")
 
# TODO: get transcripts + transcripts into lists
bowser = open("bowser.txt", encoding="utf8")
castlevania = open("castlevania.txt", encoding="utf8")
dark_souls = open("dark_souls.txt", encoding="utf8")
e3 = open("e3.txt", encoding="utf8")
fallout = open("fallout.txt", encoding="utf8")
fire_emblem = open("fire_emblem.txt", encoding="utf8")
game_calculations = open("game_calculations.txt", encoding="utf8")
gamer_space = open("gamer_space.txt", encoding="utf8")
kingdom_hearts = open("kingdom_hearts.txt", encoding="utf8")
kirby = open("kirby.txt", encoding="utf8")
mario_retire = open("mario_retire.txt", encoding="utf8")
megaman = open("megaman.txt", encoding="utf8")
osha_violations = open("osha_violations.txt", encoding="utf8")
pet_hp = open("pet_hp.txt", encoding="utf8")
sims = open("sims.txt", encoding="utf8")
skyrim_book_report = open("skyrim_book_report.txt", encoding="utf8")
sonic = open("sonic.txt", encoding="utf8")
stamina = open("stamina.txt", encoding="utf8")
waluigi = open("waluigi.txt", encoding="utf8")
zelda = open("zelda.txt", encoding="utf8")

all_transcripts = [bowser, castlevania, dark_souls, e3, fallout, fire_emblem, game_calculations, gamer_space,
    kingdom_hearts, kirby, mario_retire, megaman, osha_violations, pet_hp, sims, skyrim_book_report, sonic,
    stamina, waluigi, zelda]

transcripts_list = []
transcript_word_count = 0

for current_file in all_transcripts:    
    # list comprehension: joins words in file
    word_list = (' '.join([item for item in current_file]))
    word_list = word_list.split(' ')
    transcript_word_count += (len(word_list))
    for i in range(len(word_list)):
        transcripts_list.append(word_list[i])
    
logging.debug("completed adding to all transcripts list: %s" %(transcripts_list))
logging.debug("completed adding transcript length to list: %s" %(transcript_word_count))

# word for word in transcripts_list if word not in stop_words
transcripts_removed_list = []
for word in transcripts_list:
    if word in stop_words:
        pass
    else:
        transcripts_removed_list.append(word)

logging.debug("file after stop_words removed: %s" %(transcripts_removed_list))

# TODO: use bigram? trigram? model << try bi first then tri
transcripts_bigram = nltk.bigrams(transcripts_removed_list)
logging.debug("file bigram: %s" %(transcripts_bigram))

master_cfd = nltk.ConditionalFreqDist(transcripts_bigram)
logging.debug("cfd created %s" %(master_cfd))

#----COPIED FROM SETHS NLP----WILL CHANGE LATER
def generate_text(cfd, n, word='', sz=10):
  # if no starting word specified, use a random word in the conditional freq distrib
  if not word or not cfd[word]:
    # get random key
    r = random.randint(0, len(cfd.keys())-1)
    word = list(cfd.keys())[r]
  
  # loop through number of desired words, and use previous word as next key
  for i in range(n):
    # print current word
    yield word
    # index to get most common "sz" words and randomly select one as next word
    word = random.choice(cfd[word].most_common()[:sz])[0]

# 2670 = calculated avg word count of transcript
print(' '.join([item for item in generate_text(master_cfd, 2670)]))

# TODO: function for generating text - params: cfd, length of generated text, 
#           starting word, sz << sz is how many words from cfd are grabbed
def script_generator(cfd, script_length, start_word='', size=10):
    # TODO: if no starting word, get random one
    pass
    # TODO: loop thru num of desired words and use prev word as next key

    # TODO: call function and print out result (to file?)