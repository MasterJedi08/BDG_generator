
from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

bowser = open("training_scripts/bowser.txt", encoding="utf8")
castlevania = open("training_scripts/castlevania.txt", encoding="utf8")
dark_souls = open("training_scripts/dark_souls.txt", encoding="utf8")
e3 = open("training_scripts/e3.txt", encoding="utf8")
fallout = open("training_scripts/fallout.txt", encoding="utf8")
fire_emblem = open("training_scripts/fire_emblem.txt", encoding="utf8")
game_calculations = open("training_scripts/game_calculations.txt", encoding="utf8")
gamer_space = open("training_scripts/gamer_space.txt", encoding="utf8")
kingdom_hearts = open("training_scripts/kingdom_hearts.txt", encoding="utf8")
kirby = open("training_scripts/kirby.txt", encoding="utf8")
mario_retire = open("training_scripts/mario_retire.txt", encoding="utf8")
megaman = open("training_scripts/megaman.txt", encoding="utf8")
osha_violations = open("training_scripts/osha_violations.txt", encoding="utf8")
pet_hp = open("training_scripts/pet_hp.txt", encoding="utf8")
sims = open("training_scripts/sims.txt", encoding="utf8")
skyrim_book_report = open("training_scripts/skyrim_book_report.txt", encoding="utf8")
sonic = open("training_scripts/sonic.txt", encoding="utf8")
stamina = open("training_scripts/stamina.txt", encoding="utf8")
waluigi = open("training_scripts/waluigi.txt", encoding="utf8")
zelda = open("training_scripts/zelda.txt", encoding="utf8")

all_transcripts = [bowser, castlevania, dark_souls, e3, fallout, fire_emblem, game_calculations, gamer_space,
    kingdom_hearts, kirby, mario_retire, megaman, osha_violations, pet_hp, sims, skyrim_book_report, sonic,
    stamina, waluigi, zelda]

lines = ""

for in_filename in all_transcripts:
    doc = load_doc(in_filename)
    n_lines = doc.split('\n')
    lines = lines+ n_lines

# integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)
# vocabulary size
vocab_size = len(tokenizer.word_index) + 1
 
# separate into input and output
sequences = array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]
 
# define model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, batch_size=128, epochs=10)