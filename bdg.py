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

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
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

all_bigrams_list = []
# IDEA: use for loop to go thru each one
for current_file in all_transcripts:
    logging.DEBUG("file running: %s" % (current_file[:20]))
    # list comprehension: joins words in file
    all_word_list = '\n'.join([item for item in current_file]))

    # TODO: remove stop-words from lists
    removed_list = [word for word in all_word_list if word not in stop_words]
    logging.INFO("file after stop_wordss removed: ")
    
    # TODO: use bigram? trigram? model << try bi first then tri
    file_bigram = nltk.bigrams(removed_list)
    all_bigrams_list.append(file_bigram)

master_cfd = nltk.ConditionalFreqDist(all_bigrams_list[1])
print(master_cfd)

# TODO: function for generating text - params: cfd, length of generated text, 
#           starting word, sz << sz is how many words from cfd are grabbed
def script_generator(cfd, script_length, start_word='', size=10):
    # TODO: if no starting word, get random one
    
    pass
    # TODO: loop thru num of desired words and use prev word as next key

    # TODO: call function and print out result (to file?)