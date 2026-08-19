# Write a program to implement the concept of Stemming

import os
from nltk.stem import PorterStemmer

os.system("cls")

# Create stemmer
stemmer = PorterStemmer()

# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.lower().split()

# Apply stemming
print("\nOriginal words and their stems:")

for word in words:
    print(word, "->", stemmer.stem(word))