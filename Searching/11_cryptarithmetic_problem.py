# Write a program to implement Cryptarithmetic Problem

import os
from itertools import permutations

os.system("cls")

# Input words
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

# Get all unique letters
letters = set(word1 + word2 + result)

# Cryptarithmetic cannot have more than 10 unique letters
if len(letters) > 10:
    print("Too many unique letters! Maximum is 10.")
    exit()

letters = list(letters)

# First letters cannot be zero
first_letters = {word1[0], word2[0], result[0]}


# Convert word into its numerical value
def word_value(word, mapping):
    value = 0

    for letter in word:
        value = value * 10 + mapping[letter]

    return value


# Try all possible digit assignments
found = False

for digits in permutations(range(10), len(letters)):

    mapping = dict(zip(letters, digits))

    # Leading letters cannot be zero
    if any(mapping[letter] == 0 for letter in first_letters):
        continue

    num1 = word_value(word1, mapping)
    num2 = word_value(word2, mapping)
    num_result = word_value(result, mapping)

    # Check equation
    if num1 + num2 == num_result:

        found = True

        print("\nSolution found:")
        for letter in sorted(mapping):
            print(letter, "=", mapping[letter])

        print("\nEquation:")
        print(num1, "+", num2, "=", num_result)

        break


if not found:
    print("\nNo solution exists.")