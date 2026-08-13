# Write a program to implement DFS

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

# DFS
visited = [False] * n
stack = []

visited[start] = True
stack.append(start)

print("DFS Traversal:", end=" ")

while stack:
    vertex = stack.pop()
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            stack.append(neighbor)