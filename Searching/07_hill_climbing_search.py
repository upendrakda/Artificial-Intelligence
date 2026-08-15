# Write a program to implement Hill Climbing Search

import os

os.system("cls")

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Create graph
graph = [[] for _ in range(n)]

# Input number of edges
e = int(input("Enter number of edges: "))

# Input edges
print("Enter edges (u v):")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)   # Remove this line for directed graph

# Input heuristic values
heuristic = []

print("Enter heuristic values:")
for i in range(n):
    h = int(input(f"Heuristic of vertex {i}: "))
    heuristic.append(h)

# Input starting vertex
start = int(input("Enter starting vertex: "))

# Hill Climbing Search
current = start

print("Hill Climbing Traversal:", end=" ")

while True:
    print(current, end=" ")

    # Find the best neighbor
    best_neighbor = current

    for neighbor in graph[current]:
        if heuristic[neighbor] < heuristic[best_neighbor]:
            best_neighbor = neighbor

    # Stop if no better neighbor exists
    if best_neighbor == current:
        print("\nSearch stopped at vertex:", current)
        break

    current = best_neighbor