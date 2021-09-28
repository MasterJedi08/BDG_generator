# -------------------------------------------------------
# Author: Ashley Jablonski
# Program: bdg.py
# Description: NLP-based program to create a script of 
#       Brian David Gilbert's Polygon Unraveled videos
# -------------------------------------------------------

# IMPORTS
from pathlib import Path
import nltk, re
import random as rand
import stop

import logging
logging.basicConfig(filename = "trilog_bdg1.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename = "trilog_bdg1.txt", level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)
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

# puts all transcripts into one list, seperated by words
for current_file in all_transcripts[1:2]:    
    # list comprehension: joins words in file
    word_list = (' '.join([item for item in current_file]))
    logging.debug("current word list: %s" %(word_list) )
    word_list = word_list.split(' ')
    logging.debug("word list after .split(): %s" %(word_list) )
    transcript_word_count += (len(word_list))
    for i in range(len(word_list)):
        transcripts_list.append(word_list[i])
    
logging.debug("completed adding to all transcripts list: %s" %(transcripts_list))
logging.debug("completed adding transcript length to list: %s" %(transcript_word_count))


# word for word in transcripts_list if word not in stop_words
transcripts_removed_list = []
for word in transcripts_list:
    if word in stop.stop_words:
        pass
    else:
        transcripts_removed_list.append(word)

logging.debug("file after stop_words removed: %s" %(transcripts_removed_list))

# TODO: use bigram? trigram? model << try bi first then tri
transcripts_trigram = nltk.trigrams(transcripts_removed_list)
logging.debug("file trigram: %s" %(transcripts_trigram))

# doesnt support trigrams -- look it up!!
# output tuple -- wrap first two items \\ tuple >> (item item) item
# word net -- snowball -- part of speech
# part of speech as condition to cfd {noun: 4}
# multiple condtitions -- multicfd??
# if doing multiple dif cfds haves to work with probabilities!!
master_cfd = nltk.ConditionalFreqDist(transcripts_trigram)
print(master_cfd)
logging.debug("cfd created %s" %(master_cfd))

# TODO: function for generating text - params: cfd, length of generated text, 
#           starting word, sz << sz is how many words from cfd are grabbed
def script_generator(cfd, script_length, start_word='', size=5):
    # TODO: if no starting word, get random one
    keys = list(cfd.keys())
    if start_word == '' or (start_word not in keys):
        x = rand.randint(0, len(keys) - 1)
        start_word = keys[x]

    final_script = ""
    script_list = []
    # # TODO: loop thru num of desired words and use prev word as next key
    for i in range(script_length):
        yield start_word
        
        # randomly chooses btwn top 5 most common words after previous word
        start_word = rand.choice(cfd[start_word].most_common()[:size])[0]
        
        # checks if word before or two words before are same; if so word is changed
        if len(script_list) >= 3:
            if start_word == script_list[i-2]:
                start_word = rand.choice(cfd[start_word].most_common()[:size])[0]
            elif start_word == script_list[i-1]:
                start_word = rand.choice(cfd[start_word].most_common()[:size])[0]
            else:
                pass
        # if only two words in list, only word before is checked
        elif len(script_list) == 2:
            if start_word == script_list[i-1]:
                start_word = rand.choice(cfd[start_word].most_common()[:size])[0]
            else:
                pass
        
        if i == script_length:
            print("final word")
            while(word in stop.verbs or word in stop.dont_end):                
                start_word = rand.choice(cfd[start_word].most_common()[:size])[0]
                print("retried final word...")

        # adds word to final script so it can be added to txt file
        final_script = final_script + " " + start_word
        script_list.append(start_word)

    # writes script to .txt file
    script_file = open('bdg_unraveled_script5.txt', "w")
    script_file.write(final_script)
    script_file.close()

# TODO: call function and print out result (to file?)
# 2670 = calculated avg length of unraveled script
print(' '.join([item for item in script_generator(master_cfd, 70)]))


# ------------------------------------------------------------------------------------
# IMPROVEMENTS TO MAKE:
# get rid of punctuation before/after words (i.e. "troops.", "*Crash", "No\n")
# DONE -- don't let previous word = following word (i.e. "is is", "and and")
# make it more sensible!!
# can't begin/end with verb or with words like "the or with"
# if word ends with * then words before it should too?
# ------------------------------------------------------------------------------------


# Code I tried but didn't work and will figure out why later:
# final_script = []
    # prev_word = start_word
    # for x in range(script_length):
    #     print(str(prev_word) + " " + str(x))
    #     # randomly chooses btwn top 3 most common words after previous word
    #     # if index doesn't exist, chooses first value of key
    #     try:
    #         new_word = rand.choice(cfd[prev_word].most_common()[:size][0])
    #     except:
    #         new_word = cfd[prev_word][0][0]
    #         print("Exception made: only one possible outcome")
    #     else:
    #         new_word = rand.choice(cfd[prev_word].most_common()[:size][0])
    #     final_script.append(new_word)
    #     prev_word = new_word
    #     print(prev_word)

    # takes list and turns into string

    
# # gets rid of any punctuation at beginning or end of word
# end_char_stops = ['.', '!', '?', '*', '\'', '\"', '(', ')']
# count = 0
# for word in transcripts_list:
#     print(word)
#     for char in end_char_stops:
#         try:
#             if char in word[0]:
#                 transcripts_list[count] = word[1:]
#                 print("B")
#             elif word[-1] == "n" and word[-2] == "\\":
#                 transcripts_list[count] = word[:-2]
#                 print("N")
#             else:
#                 pass
            
#             if char in word[-1]:
#                 transcripts_list[count] = word[:-1]
#                 print("E")
#         except:
#             print("none")

#     count += 1        