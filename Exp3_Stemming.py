from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
text="Hello! I am SHADE, Your personal AI companion."
words=word_tokenize(text)
ps=PorterStemmer()
for w in words:
    print(ps.stem(w))
