from textblob import TextBlob,Word

# text="Anna is mw moother"
# t=TextBlob(text)
# print(t.correct())
txt=["She","is","mw","moom"]
for w in txt:
    word=Word(w)
    print(word.spellcheck())