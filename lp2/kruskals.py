# 🔹 Kruskal's Algorithm with Disjoint Set – Theory in Points
# ✅ Disjoint Set (Union-Find) – class DisjointSet
# Purpose:
# Efficiently tracks connected components of a graph to detect cycles.

# __init__(self, n):
# Initializes n elements, each in its own set (parent[i] = i).

# find(u):

# Returns the root of the set containing u.

# Uses path compression to flatten the structure, making future operations faster.

# union(u, v):

# Connects the sets containing u and v by linking their roots.

# Ensures no cycle is formed when building MST.

# ✅ Kruskal’s Algorithm – kruskal(graph_edges, num_vertices)
# Purpose:
# Finds a Minimum Spanning Tree (MST) by choosing the lowest weight edges without forming cycles.

# Input:

# graph_edges: List of (weight, u, v) tuples.

# num_vertices: Total number of vertices in the graph.

# Steps:

# Sort all edges by increasing weight.

# Initialize a Disjoint Set to track connected components.

# For each edge:

# If u and v are in different sets (no cycle), include the edge in MST.

# Perform union(u, v) to merge the sets.

# Output:

# Returns a list of MST edges and the total minimum weight.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            self.parent[v_root] = u_root

def kruskal(graph_edges, num_vertices):
    # graph_edges = list of (weight, u, v)
    graph_edges.sort()
    ds = DisjointSet(num_vertices)
    mst = []
    mst_weight = 0

    for weight, u, v in graph_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight

# Example usage
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]
mst, total_weight = kruskal(edges, 4)
print("MST Edges:", mst)
print("Total Weight:", total_weight)
