from textblob import TextBlob
from textblob.wordnet import VERB,ADV,ADJ,NOUN
from textblob import Word
import textblob

text="Ana is here. She is happy."
t=TextBlob(text)
for word in t.tags:
    word=word[0].lower()
    print(word)
    w=Word(word[0])
    print(w.get_synsets())