# Write a program to implement Greedy Best First Search

import os
import heapq

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

# Input goal vertex
goal = int(input("Enter goal vertex: "))

# Greedy Best First Search
visited = [False] * n
priority_queue = []

# Add starting vertex
heapq.heappush(priority_queue, (heuristic[start], start))

print("GBFS Traversal:", end=" ")

while priority_queue:
    h, vertex = heapq.heappop(priority_queue)

    if visited[vertex]:
        continue

    visited[vertex] = True
    print(vertex, end=" ")

    # Check whether goal is reached
    if vertex == goal:
        print("\nGoal found!")
        break

    # Add unvisited neighbors
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            heapq.heappush(
                priority_queue,
                (heuristic[neighbor], neighbor)
            )
else:
    print("\nGoal not found!")