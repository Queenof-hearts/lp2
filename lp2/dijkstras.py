# import heapq

# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     min_heap = [(0, start)]

#     print("Graph structure:")
#     for node in graph:
#         print(f"{node} --> {graph[node]}")
#     print()

#     while min_heap:
#         current_distance, current_node = heapq.heappop(min_heap)

#         if current_distance > distances[current_node]:
#             continue

#         for neighbor, weight in graph[current_node]:
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(min_heap, (distance, neighbor))

#     return distances

# # Example graph (Adjacency List)
# graph = {
#     'A': [('B', 4), ('C', 1)],
#     'B': [('A', 4), ('C', 2), ('D', 5)],
#     'C': [('A', 1), ('B', 2), ('D', 8), ('E', 10)],
#     'D': [('B', 5), ('C', 8), ('E', 2)],
#     'E': [('C', 10), ('D', 2)]
# }

# start_node = 'A'
# print("Shortest distances from start node:", dijkstra(graph, start_node))


import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, u = heapq.heappop(pq)

        if current_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))

    return distances

# Example usage
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 2), (3, 4)],
    2: [(0, 3), (1, 2), (3, 5)],
    3: [(1, 4), (2, 5)]
}
start_node = 0
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":", distances)