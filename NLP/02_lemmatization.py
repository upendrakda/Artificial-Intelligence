# Write a program to implement the concept of Lemmatization

import os
import nltk
from nltk.stem import WordNetLemmatizer

os.system("cls")

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

print("\nLemmatization Result")
print(f"{'Word':<20}{'Lemma':<15}")
print("-" * 35)

# Apply lemmatization
for word in words:
    clean_word = word.lower().strip(".,!?")
    lemma = lemmatizer.lemmatize(clean_word)

    print(f"{word:<20}{lemma:<15}")