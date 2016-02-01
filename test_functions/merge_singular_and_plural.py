__author__ = 'JI'

# frequency-combining-singular-and-plural-verb-and-adverb

import nltk

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
lemmatizer = nltk.stem.WordNetLemmatizer()
test = "That aggressive person walk by the house over there, one of many houses aggressively"
tokens = tokenizer.tokenize(test)
lemmas = [lemmatizer.lemmatize(t) for t in tokens]
fdist = nltk.FreqDist(lemmas)
common = fdist.most_common(100)

print(common)
