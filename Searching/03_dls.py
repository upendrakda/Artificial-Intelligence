# Write a program to implement Depth Limited Search

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

# Input depth limit
limit = int(input("Enter depth limit: "))

# DLS
visited = [False] * n
stack = [(start, 0)]

print("DLS Traversal:", end=" ")

while stack:
    vertex, depth = stack.pop()

    if visited[vertex]:
        continue

    visited[vertex] = True
    print(vertex, end=" ")

    # Expand only if depth limit is not reached
    if depth < limit:
        for neighbor in reversed(graph[vertex]):
            if not visited[neighbor]:
                stack.append((neighbor, depth + 1))