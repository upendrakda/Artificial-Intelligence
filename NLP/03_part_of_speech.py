# Write a program to implement the concept of Part of Speech (POS) Tagging

import os
import nltk

os.system("cls")

# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Apply POS tagging
tags = nltk.pos_tag(words)

# Display result
print("\nPOS Tagging Result")
print(f"{'Word':<20}{'POS Tag':<10}")
print("-" * 30)

for word, tag in tags:
    print(f"{word:<20}{tag:<10}")