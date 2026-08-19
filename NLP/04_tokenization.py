# Write a program to implement the concept of Tokenization

import os
import nltk
from nltk.tokenize import word_tokenize

os.system("cls")

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenization
tokens = word_tokenize(sentence)

# Display tokens
print("\nTokens:")

for i, token in enumerate(tokens, 1):
    print(f"Token {i}: {token}")