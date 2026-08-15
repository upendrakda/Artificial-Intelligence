# Write a program to implement Water Jug Problem

import os
from collections import deque

os.system("cls")

# Input jug capacities
capacity_a = int(input("Enter capacity of jug A: "))
capacity_b = int(input("Enter capacity of jug B: "))

# Input target amount
target = int(input("Enter target amount: "))


# BFS for Water Jug Problem
def water_jug(a_capacity, b_capacity, target):

    queue = deque()
    visited = set()

    # Initial state
    queue.append((0, 0, []))
    visited.add((0, 0))

    while queue:

        a, b, path = queue.popleft()

        # Check target
        if a == target or b == target:
            path.append((a, b))
            return path

        # Possible operations
        states = [
            (a_capacity, b),                         # Fill A
            (a, b_capacity),                         # Fill B
            (0, b),                                  # Empty A
            (a, 0),                                  # Empty B

            # Pour A -> B
            (
                a - min(a, b_capacity - b),
                b + min(a, b_capacity - b)
            ),

            # Pour B -> A
            (
                a + min(b, a_capacity - a),
                b - min(b, a_capacity - a)
            )
        ]

        for new_a, new_b in states:

            if (new_a, new_b) not in visited:
                visited.add((new_a, new_b))
                queue.append(
                    (new_a, new_b, path + [(a, b)])
                )

    return None


# Find solution
solution = water_jug(capacity_a, capacity_b, target)

if solution:
    print("\nSolution:")
    for state in solution:
        print("Jug A:", state[0], "Jug B:", state[1])
else:
    print("\nNo solution exists.")