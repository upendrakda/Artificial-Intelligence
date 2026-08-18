# Write a program to implement the concept of Part of Speech (POS) Tagging

import os

os.system("cls")


# Dictionary containing common words and their POS tags
pos_dict = {
    "the": "DT",
    "a": "DT",
    "an": "DT",
    "student": "NN",
    "students": "NNS",
    "teacher": "NN",
    "school": "NN",
    "book": "NN",
    "cat": "NN",
    "dog": "NN",
    "is": "VBZ",
    "are": "VBP",
    "was": "VBD",
    "were": "VBD",
    "playing": "VBG",
    "studying": "VBG",
    "eating": "VBG",
    "played": "VBD",
    "runs": "VBZ",
    "quickly": "RB",
    "slowly": "RB",
    "good": "JJ",
    "beautiful": "JJ",
    "happy": "JJ",
    "and": "CC",
    "but": "CC",
    "in": "IN",
    "on": "IN",
    "with": "IN"
}


# POS tagging function
def pos_tag(word):

    word = word.lower()
    word = word.strip(".,!?")

    # Check dictionary
    if word in pos_dict:
        return pos_dict[word]

    # Simple rules for unknown words
    if word.endswith("ing"):
        return "VBG"
    elif word.endswith("ed"):
        return "VBD"
    elif word.endswith("ly"):
        return "RB"
    elif word.endswith("s"):
        return "NNS"
    else:
        return "NN"


# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

print("\nPOS Tagging Result")
print(f"{'Word':<20}{'POS Tag':<10}")
print("-" * 30)

for word in words:
    tag = pos_tag(word)
    print(f"{word:<20}{tag:<10}")