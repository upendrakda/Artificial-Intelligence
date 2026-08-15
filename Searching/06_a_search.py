# Write a program to implement A* Search

import os
import heapq

os.system("cls")

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Create graph
graph = [[] for _ in range(n)]

# Input number of edges
e = int(input("Enter number of edges: "))

# Input edges and their costs
print("Enter edges (u v cost):")
for i in range(e):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))   # Remove this line for directed graph

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

# A* Search
priority_queue = []

# (f(n), g(n), vertex)
heapq.heappush(priority_queue, (heuristic[start], 0, start))

g_cost = [float('inf')] * n
g_cost[start] = 0

visited = [False] * n

print("A* Traversal:", end=" ")

while priority_queue:
    f, current_cost, vertex = heapq.heappop(priority_queue)

    if visited[vertex]:
        continue

    visited[vertex] = True
    print(vertex, end=" ")

    # Check if goal is reached
    if vertex == goal:
        print("\nGoal found!")
        print("Total cost:", current_cost)
        break

    # Explore neighbors
    for neighbor, cost in graph[vertex]:

        new_cost = current_cost + cost

        if new_cost < g_cost[neighbor]:
            g_cost[neighbor] = new_cost

            f_cost = new_cost + heuristic[neighbor]

            heapq.heappush(
                priority_queue,
                (f_cost, new_cost, neighbor)
            )

else:
    print("\nGoal not found!")