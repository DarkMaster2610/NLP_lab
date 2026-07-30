import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('average_perception_tagger')
s=input("Enter a sentence: ")
tokens=word_tokenize(s)
pos_tags = nltk.pos_tag(tokens)
print("\nWord\t\t POS tag")
print("-"*30)
for word, tag in pos_tags:
    print(f"{word}\t\t(tag)")
