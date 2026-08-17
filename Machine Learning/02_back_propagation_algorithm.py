# Write a program to implement Back Propagation Algorithm

import os
import math
import random

os.system("cls")


# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)


# Input number of training samples
samples = int(input("Enter number of training samples: "))

# Input number of input features
inputs = int(input("Enter number of input features: "))

# Input number of hidden neurons
hidden = int(input("Enter number of hidden neurons: "))

# Input training data
print("\nEnter training data:")

X = []
Y = []

for i in range(samples):
    x = list(map(float, input(f"Input {i + 1}: ").split()))
    y = float(input(f"Target {i + 1}: "))

    X.append(x)
    Y.append(y)


# Input learning parameters
learning_rate = float(input("\nEnter learning rate: "))
epochs = int(input("Enter number of epochs: "))


# Initialize weights randomly
hidden_weights = [
    [random.uniform(-1, 1) for _ in range(hidden)]
    for _ in range(inputs)
]

hidden_bias = [random.uniform(-1, 1) for _ in range(hidden)]

output_weights = [
    random.uniform(-1, 1) for _ in range(hidden)
]

output_bias = random.uniform(-1, 1)


# Training
for epoch in range(epochs):

    total_error = 0

    for sample in range(samples):

        # ---------------- FORWARD PASS ----------------

        hidden_output = []

        for j in range(hidden):

            total = hidden_bias[j]

            for i in range(inputs):
                total += X[sample][i] * hidden_weights[i][j]

            hidden_output.append(sigmoid(total))

        # Calculate output
        output_sum = output_bias

        for j in range(hidden):
            output_sum += hidden_output[j] * output_weights[j]

        output = sigmoid(output_sum)

        # Calculate error
        error = Y[sample] - output
        total_error += error ** 2

        # ---------------- BACKWARD PASS ----------------

        # Output layer delta
        output_delta = error * sigmoid_derivative(output)

        # Hidden layer deltas
        hidden_delta = []

        for j in range(hidden):
            delta = (
                output_delta
                * output_weights[j]
                * sigmoid_derivative(hidden_output[j])
            )

            hidden_delta.append(delta)

        # ---------------- UPDATE WEIGHTS ----------------

        # Update output weights
        for j in range(hidden):
            output_weights[j] += (
                learning_rate
                * output_delta
                * hidden_output[j]
            )

        # Update output bias
        output_bias += learning_rate * output_delta

        # Update hidden weights
        for i in range(inputs):
            for j in range(hidden):
                hidden_weights[i][j] += (
                    learning_rate
                    * hidden_delta[j]
                    * X[sample][i]
                )

        # Update hidden biases
        for j in range(hidden):
            hidden_bias[j] += learning_rate * hidden_delta[j]


# Display results
print("\nTraining completed!")

print("\nPredictions:")

for sample in range(samples):

    hidden_output = []

    for j in range(hidden):

        total = hidden_bias[j]

        for i in range(inputs):
            total += X[sample][i] * hidden_weights[i][j]

        hidden_output.append(sigmoid(total))

    output_sum = output_bias

    for j in range(hidden):
        output_sum += hidden_output[j] * output_weights[j]

    output = sigmoid(output_sum)

    print(
        "Input:", X[sample],
        "Target:", Y[sample],
        "Output:", round(output, 4)
    )