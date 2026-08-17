# Write a program to implement Naive Bayes Algorithm

import os

os.system("cls")

# Input number of training samples
n = int(input("Enter number of training samples: "))

data = []

# Input training data
print("\nEnter training data:")
print("Format: Feature1 Feature2 Class")

for i in range(n):
    values = input(f"Sample {i + 1}: ").split()

    features = values[:-1]
    label = values[-1]

    data.append((features, label))


# Input test data
test = input("\nEnter test data (features only): ").split()


# Find unique classes
classes = set(label for features, label in data)

probabilities = {}

for cls in classes:

    # Get samples belonging to current class
    class_data = [
        features for features, label in data
        if label == cls
    ]

    # Prior probability
    prior = len(class_data) / n

    probability = prior

    # Calculate conditional probabilities
    for i in range(len(test)):

        count = 0

        for features in class_data:
            if features[i] == test[i]:
                count += 1

        probability *= count / len(class_data)

    probabilities[cls] = probability


# Normalize probabilities
total = sum(probabilities.values())

print("\nProbabilities:")

for cls in probabilities:
    probabilities[cls] = probabilities[cls] / total
    print(cls, ":", probabilities[cls])


# Find class with highest probability
prediction = max(probabilities, key=probabilities.get)

print("\nPredicted class:", prediction)