# Write a program to implement Iterative Deepening Search

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

# Input starting vertex
start = int(input("Enter starting vertex: "))

# Input goal vertex
goal = int(input("Enter goal vertex: "))


# Depth Limited Search
def dls(start, goal, limit):
    stack = [(start, 0)]
    visited = set()

    while stack:
        vertex, depth = stack.pop()

        if vertex == goal:
            return True

        if vertex in visited:
            continue

        visited.add(vertex)

        if depth < limit:
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))

    return False


# Iterative Deepening Search
depth = 0

while True:
    print("\nSearching at depth:", depth)

    if dls(start, goal, depth):
        print("Goal found at depth:", depth)
        break

    depth += 1