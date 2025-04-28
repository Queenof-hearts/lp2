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
