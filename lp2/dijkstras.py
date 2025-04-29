#  Dijkstra’s Algorithm – Theory in Points
# Purpose:
# Finds the shortest path from a source node to all other nodes in a weighted graph (no negative weights).

# Data Structure Used:
# Uses a priority queue (min-heap via heapq) to always process the node with the smallest known distance.

# Initialization:

# Set the distance to all nodes as infinity (∞).

# Distance to the source node is set to 0.

# Priority Queue:
# Starts with the source node in the queue with distance 0.

# Main Loop:

# Pop the node with the smallest distance.

# Skip if a better path has already been found.

# For each neighbor, calculate the new possible distance via the current node.

# Relaxation:
# If the new distance to a neighbor is smaller, update it and push the neighbor into the queue.

# Termination:
# Continues until all nodes have been visited with the shortest possible distance.

# Output:
# A dictionary mapping each node to its shortest distance from the source.

# Time Complexity:

# Using a min-heap: O((V + E) log V), where V = number of vertices, E = number of edges.

# Limitation:
# Does not work with graphs having negative weight edges.

import heapq

def dijkstra(graph, start):
    # Distance to all nodes initially infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to get the node with the smallest distance
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If new distance is smaller, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Define the graph as an adjacency list
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
    'C': [('A', 5), ('B', 11), ('E', 3)],
    'D': [('B', 9), ('F', 2)],
    'E': [('B', 7), ('C', 3), ('F', 6)],
    'F': [('D', 2), ('E', 6)]
}

# Run Dijkstra from source node 'A'
distances = dijkstra(graph, 'A')

print("Shortest distances from A:")
for node in distances:
    print(f"{node}: {distances[node]}")
