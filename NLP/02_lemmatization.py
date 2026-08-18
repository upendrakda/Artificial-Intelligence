# Write a program to implement the concept of Lemmatization

import os

os.system("cls")

# Dictionary containing words and their base forms
lemma_dict = {
    "students": "student",
    "studies": "study",
    "studying": "study",
    "studied": "study",
    "playing": "play",
    "played": "play",
    "plays": "play",
    "games": "game",
    "better": "good",
    "best": "good",
    "mice": "mouse",
    "children": "child",
    "men": "man",
    "women": "woman",
    "cars": "car",
    "running": "run",
    "ran": "run",
    "eating": "eat",
    "ate": "eat"
}


# Lemmatization function
def lemmatize_word(word):
    word = word.lower()
    word = word.strip(".,!?")

    if word in lemma_dict:
        return lemma_dict[word]

    return word


# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

print("\nLemmatization Result")
print(f"{'Word':<20}{'Lemma':<15}")
print("-" * 35)

for word in words:
    lemma = lemmatize_word(word)
    print(f"{word:<20}{lemma:<15}")