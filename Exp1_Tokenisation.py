from nltk.tokenize import sent_tokenize,word_tokenize
text="Allow me to introduce myself. I am S.H.A.D.E, a virtual artificial intelligence, and I am here to assist you with a variety of tasks 24/7."
words=word_tokenize(text)
print(words)
n1=len(word_tokenize(text))
print("Number of tokens:",n1)
print("_________________________________")
print(sent_tokenize(text))
n2=len(sent_tokenize(text))
print("Number of tokens:",n2)

