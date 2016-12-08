
#https://github.com/smilli/py-corenlp
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer

# https://stackoverflow.com/questions/1902967/nltk-how-to-find-out-what-corpora-are-installed-from-within-python

import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


file_text = open("../source.txt", 'r').read()

#nltk.download
#if wordnet corpus not present

def nltk_tokenize(text):
    tokens = []

    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(text)
    return tokens

def nltk_lemmatize(tokens):
    wnl = WordNetLemmatizer()
    for i in range(len(tokens)):
        tokens[i] = wnl.lemmatize(tokens[i])
    return tokens


if __name__ == '__main__':	
	tokens = nltk_tokenize(file_text)
	print 'tokenized: ', tokens

	tokens = nltk_lemmatize(tokens)
	print 'lemmatized', tokens
