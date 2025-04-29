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