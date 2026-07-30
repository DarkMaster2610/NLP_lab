from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
text="Hello! I am SHADE, Your personal AI companion."
words=word_tokenize(text)
stop_words=set(stopwords.words("english"))
stop_words_in_text=[a for a in words if a in stop_words]
print("Stop word in your input text:")
print(stop_words_in_text)

