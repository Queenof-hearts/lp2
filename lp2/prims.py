# Prim's Algorithm – Theory in Points (Using heapq)
# Purpose:
# Finds the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph — the subset of edges that connects all vertices with minimum total weight and no cycles.

# Data Structure Used:

# Min-heap (heapq) to always choose the next edge with the lowest weight.

# Visited set to track already included nodes.

# Initialization:

# Start with an empty visited set.

# Push (0, start_node) into the heap.

# Initialize total_cost = 0.

# Heap Operation:

# Pop the smallest edge from the heap.

# If the vertex is not visited, include it in MST and add its edge cost to total_cost.

# Neighbor Exploration:

# For the current vertex, push all unvisited neighbors and their edge weights into the heap.

# Repeat Until MST Complete:

# Loop continues until all nodes are visited and the MST is built.

# Output:

# Returns the total cost (sum of weights) of the minimum spanning tree.

# Time Complexity:

# O(E log V) using a min-heap, where E is number of edges and V is number of vertices.

# Properties of MST:

# Connects all nodes.

# No cycles.

# Has exactly V - 1 edges.

# Limitation:

# Only works on connected, undirected graphs.

# Does not support negative-weight edges in terms of logic issues (though technically allowed).

import heapq

def prims_algorithm(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (cost, vertex)
    total_cost = 0

    print("Graph structure:")
    for node in graph:
        print(f"{node} --> {graph[node]}")
    print()

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            total_cost += cost

            for v, weight in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))

    return total_cost

# Example graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

start_node = 'A'
print("Minimum cost to connect all nodes:", prims_algorithm(graph, start_node))
