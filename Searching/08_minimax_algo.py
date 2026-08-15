# Write a program to implement the concept of Minimax Algorithm

import os

os.system("cls")

# Minimax function
def minimax(depth, node, is_max, values, max_depth):

    # If leaf node is reached
    if depth == max_depth:
        return values[node]

    if is_max:
        return max(
            minimax(depth + 1, node * 2, False, values, max_depth),
            minimax(depth + 1, node * 2 + 1, False, values, max_depth)
        )

    else:
        return min(
            minimax(depth + 1, node * 2, True, values, max_depth),
            minimax(depth + 1, node * 2 + 1, True, values, max_depth)
        )


# Input depth of game tree
depth = int(input("Enter depth of game tree: "))

# Number of leaf nodes
num_leaves = 2 ** depth

# Input leaf node values
values = []

print("Enter values of leaf nodes:")
for i in range(num_leaves):
    value = int(input(f"Leaf {i + 1}: "))
    values.append(value)

# Calculate best value
result = minimax(0, 0, True, values, depth)

print("Optimal value for MAX player:", result)