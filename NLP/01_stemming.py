# Write a program to implement the concept of Stemming

import os

os.system("cls")


# Stemming function
def stem(word):

    suffixes = [
        "ingly",
        "edly",
        "ing",
        "ed",
        "ly",
        "es",
        "s"
    ]

    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]

    return word


# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.lower().split()

# Apply stemming
print("\nOriginal words and their stems:")

for word in words:
    print(word, "->", stem(word))