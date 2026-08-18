# Write a program to implement the concept of Tokenization

import os

os.system("cls")

# Input sentence
sentence = input("Enter a sentence: ")

# Word tokenization
words = sentence.split()

# Display tokens
print("\nTokens:")
for i, word in enumerate(words, 1):
    print(f"Token {i}: {word}")