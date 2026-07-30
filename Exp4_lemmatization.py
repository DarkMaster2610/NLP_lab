from nltk.stem import WordNetLemmatizer

l = WordNetLemmatizer()
print(l.lemmatize("Cats"))
print(l.lemmatize("Cacti"))
print(l.lemmatize("geese"))
print(l.lemmatize("rocks"))
print(l.lemmatize("python"))
print(l.lemmatize("Better",pos='a'))
print(l.lemmatize("Happy",pos='a'))

