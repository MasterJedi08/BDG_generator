import stop
from nltk import tokenize
import random as rand

def sense_words_lite(cfd, current_script, script_size, size=3):
    first_word = current_script[0]
    print(first_word)
    # check if first word in verbs or not captitalized
    while first_word in stop.verbs or (first_word[0].isupper() == False):
        first_word = rand.choice(cfd[first_word].most_common()[:size])[0]
        current_script[0] = first_word
        print("changed first word" + first_word)


    
    str_script = (' '.join([item for item in current_script]))
    sent_script = tokenize.sent_tokenize(str_script)
    print(sent_script)
    end_word = current_script[-1]
    print(end_word)

    redone_last = False

    count = 0
    # last word not a conjuction verb or other "dont end word" found in stop.py
    while end_word in stop.dont_end or end_word in stop.conjunction or end_word in stop.verbs:
        last_sent = sent_script[-1]
        print("redo" + last_sent)
        last_sent = last_sent.split(' ')
        new_last_sent = " "
        
        for x in last_sent:
            word = rand.choice(cfd[first_word].most_common()[:10])[0]
            new_last_sent = new_last_sent + word

        new_last_sent += "."
        sent_script[-1] = new_last_sent
        redone_last = True
        # failsafe if it cant find any other words (it kept breaking VS code)
        count+=1
        if count == 10:
            print("failsafe break")
            redone_last == False
            break

    # add period at end if not redone
    if redone_last == False:
        last_sent = sent_script[-1]
        last_sent += "."
        sent_script[-1] = last_sent
        print("added period: " + last_sent)

    return (' '.join([item for item in sent_script]))




def max_sensible_words(cfd, current_script, script_size):
    first_word = current_script[0]
    new_script = []
    
    # check if first word in verbs or not captitalized
    while first_word in stop.verbs or first_word[0].isupper():
        first_word = rand.choice(cfd[first_word].most_common()[:size])[0]
        new_script.append(first_word)
        print("changed first word")
    
    str_script = (' '.join([item for item in current_script]))
    sent_script = tokenize.sent_tokenize(str_script)
    print(sent_script)

    for i in range(0, len(sent_script)):        
        incorrect_syntax = True
        sentence = sent_script[i]
        sent_list = sentence.split(' ')

        #check if more than one verb in sentence (not seperated by and or but or so)
        while incorrect_syntax == True:
            count = 0
            verbs = []

            for word in sentence:
                if word in stop.verbs:
                    count += 1
                    verbs.append(word)
                    

            if count > 1:
                prev_verb = 0
                for x in range(len(verbs)):
                    verb1 = sent_list.index(verb[x])
                    if prev_verb != 0:
                        safe = False
                        false_safe = False
                        while safe==False:
                            for word in range(prev_verb+1, verb1-1):                                
                                if sent_list[word] in stop.conjunction:
                                    safe = True
                                elif sent_list.index(word) == (verb1-1):
                                    safe = True
                                    false_safe = True
                                else:
                                    pass
                        if false_safe == True:
                            new_word = rand.choice(cfd[first_word].most_common()[:size])[0]
                            sent[verb1] = new_word

    return new_script

                                
                                





