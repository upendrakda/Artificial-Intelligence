# Write a program to implement BFS

import os
from collections import deque

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

# BFS
visited = [False] * n
queue = deque()

visited[start] = True
queue.append(start)

print("BFS Traversal:", end=" ")

while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)