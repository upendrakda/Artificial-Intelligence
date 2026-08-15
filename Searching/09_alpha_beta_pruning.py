# Write a program to implement the concept of Alpha-Beta Pruning

import os

os.system("cls")


# Alpha-Beta Pruning function
def alpha_beta(depth, node, is_max, values, max_depth, alpha, beta):

    # If leaf node is reached
    if depth == max_depth:
        return values[node]

    if is_max:
        best = float('-inf')

        for child in [node * 2, node * 2 + 1]:
            value = alpha_beta(
                depth + 1, child, False,
                values, max_depth, alpha, beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta cutoff
            if beta <= alpha:
                print("Branch pruned at node:", child)
                break

        return best

    else:
        best = float('inf')

        for child in [node * 2, node * 2 + 1]:
            value = alpha_beta(
                depth + 1, child, True,
                values, max_depth, alpha, beta
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha cutoff
            if beta <= alpha:
                print("Branch pruned at node:", child)
                break

        return best


# Input depth of game tree
depth = int(input("Enter depth of game tree: "))

# Number of leaf nodes
num_leaves = 2 ** depth

# Input leaf values
values = []

print("Enter values of leaf nodes:")
for i in range(num_leaves):
    value = int(input(f"Leaf {i + 1}: "))
    values.append(value)

# Initial alpha and beta values
alpha = float('-inf')
beta = float('inf')

# Calculate optimal value
result = alpha_beta(
    0, 0, True,
    values, depth,
    alpha, beta
)

print("Optimal value for MAX player:", result)