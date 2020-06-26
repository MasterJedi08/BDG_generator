# mom and dad don't look at this it has swear words cuz BDG sometimes swears and we tryin to make this camp appropriate :)
stop_words = [",", ".", "...", ":", "\"", "(", ")", "Brian", "BRIAN", "BDG", "Pat", "Patrick", "Clayton", "uh", "Uh", "um", "Um", 
"hell", "HELL", "neat", "Neat", "NEAT", "cool", "Cool", "COOL", "on", "off", "over",
"under", "again", "further", "ah", "Ah", "Ah",
'our', 'ours', 'ourselves', "you're", "you've", "you'll", "you'd", 'yours', 
'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 
'they', 'them', 'their', 'theirs', 'themselves', 'this', 'that', "that'll", 'these', 'those', 
'as', 'at', 'against', 'between', 'into', 'fuck', 'damn', 'shit', 'through', 'above', 'below',   'from', 'up', 'down', 'in', 
'out', 'on', 'off', 'over', 'under', 
'again', 'further', 'then', 'once', 'here', 'there', 'other', 'some', 'such', 'nor', 'own', 'same',   'than', 'too', 'very', 
'now', 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't",
'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', 'OUR', 'OURS', 'OURSELVES', "YOU'RE", "YOU'VE", "YOU'LL", 
"YOU'D", 'YOURS', 'YOURSELF', 'YOURSELVES', 'HE', 'HIM', 'HIS', 'HIMSELF', 'DAMN', 'SHIT'
'SHE', "SHE'S", 'HER', 'HERS', 'HERSELF', 'THEY', 'THEM', 'THEIR', 'THEIRS', 'THEMSELVES', 'THIS',
  "THAT'LL", 'THESE', 'THOSE', 'AS', 'AT', 'AGAINST', 'BETWEEN', 'INTO', 'THROUGH',
'ABOVE', 'BELOW',   'FROM', 'UP', 'DOWN', 'IN', 'OUT', 'ON', 'OFF', 'OVER', 'UNDER', 'AGAIN', 'FURTHER', 'THEN', 'ONCE', 
'HERE', 'THERE', 'OTHER', 'SOME', 'SUCH', 'NOR', 'OWN', 'SAME',   'THAN', 'TOO', 'VERY', 'NOW', 'HADN', "HADN'T", 'HASN', 
"HASN'T", 'HAVEN', "HAVEN'T", 'MA', 'MIGHTN', "MIGHTN'T", 'FUCK', 'MUSTN', "MUSTN'T", 'NEEDN', "NEEDN'T", 'SHAN', "SHAN'T", 'SHOULDN', 
"SHOULDN'T", 'WASN', "WASN'T", 'WEREN', 'Our', 'Ours', 'Ourselves', "You'Re", 'DAMN', "You'Ve", "You'Ll", "You'D", 'Yours', 'Yourself', 
'Yourselves', 'He', 'Him', 'His', 'Himself', 'She', "She'S", 'Her', 'Hers', 'Herself', 'They', 'Them',
'Their', 'Theirs', 'Themselves', 'This', 'That', "That'Ll", 'These', 'Those', 'As', 'At', 'For', 'With', 
'About', 'Against', 'Between', 'Into', 'Through', 'Above', 'Fuck', 'Below',   'From', 'Up', 'Down', 'In', 'Out', 'On', 'Off', 'Over', 
'Under', 'Again', 'Further', 'Then', 'Once', 'Here', 'There', 'Other', 'Some', 'Such', 'Nor', 'Own', 'Same',   'Than', 'Too', 
'Very', 'Now', 'Hadn', "Hadn'T", 'Hasn', "Hasn'T", 'Haven', "Haven'T", 'Damn' 'Ma', 'Mightn', "Mightn'T", 'Mustn', "Mustn'T", 'Needn',
"Needn'T", 'Shan', "Shan'T", 'Shouldn', "Shouldn'T", 'Shit', 'Wasn', "Wasn'T", 'Weren']

verbs = ["will", "willing", "won't", "is", "isn't", "it's",  "slaps", "pick", "picks" "picking", "can", "can't", "cannot", "not", 
"make", "makes", "making", "call", "calls", "calling", "has", "hasn't", "had", "have", "keep", "keeps", "keeping", "are", "aren't", "was",
"wasn't", "were", "do", "does", "doesn't", "know", "go", "goes", "going", "went", "think", "thinking", "come", "coming",  "am", 
"be", "being", "been", "are", "aren't", "I'm", "I've", "I'd", "process", "build", "built", "building", "done", "did", "didn't",
"I", "We", "You", "My", "Our", "Your", "I'm", "I've", "I'd", "We're", "We've", "We'd", "You're", "You've", "You'd",
"And", "But", "Someone"]

dont_end = ["I", "me", "to", "not", "because", "because," "I", "We", "You", "My", "Our", "Your", "I'm", "I've", "I'd", "We're",
"We've", "We'd", "You're", "You've", "You'd", "And", "But", "Someone", "the", "The", "a", "an", "A", "An", "and", "but", "And"
"But", "the", "The"]

adj = ["most", "best", "first", "second", "thrid", "few", "little", "more", "only", "incredible", "perfectly"]

conjunction = ["and", "And", "AND", "but", "But", "BUT", "or", "Or", "OR", ]

# prop_noun = ["I", "We", "You", "My", "Our", "Your", "I'm", "I've", "I'd", "We're", "We've", "We'd", "You're", "You've", "You'd",
# "Someone"]