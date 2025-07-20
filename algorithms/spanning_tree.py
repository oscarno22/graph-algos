"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

class UnionFind:
    """Union-Find (Disjoint Set) data structure for Kruskal's algorithm."""

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        """Find the representative (with path compression)."""
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        """Union by rank. Returns True if merged, False if already in same set."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        # Merge smaller rank tree under larger rank tree
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal_mst(graph, edge_weights, meta):
    """Implements Kruskal's algorithm for finding Minimum Spanning Tree."""

    # Step 1: Extract all unique vertices
    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)

    # Step 2: Extract all unique edges (u, v, weight)
    edge_list = []
    for u in graph:
        for v in graph[u]:
            if u < v:
                key = f"{u}{v}"
                weight = edge_weights.get(key, float('inf'))
                edge_list.append((u, v, weight))

    # Step 3: Sort edges by weight
    edge_list.sort(key=lambda edge: edge[2])

    # Step 4: Kruskal's algorithm
    uf = UnionFind(vertices)
    mst_edges = []
    total_cost = 0

    for u, v, w in edge_list:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_cost += w
            if len(mst_edges) == len(vertices) - 1:
                break

    return mst_edges, total_cost


def build_mst_graph(mst_edges):
    """Construct adjacency list and weight map from MST edge list."""

    mst_graph = {}
    mst_weights = {}

    for u, v, weight in mst_edges:
        for a, b in [(u, v), (v, u)]:
            if a not in mst_graph:
                mst_graph[a] = []
            mst_graph[a].append(b)

        key = f"{u}{v}" if u < v else f"{v}{u}"
        mst_weights[key] = weight

    return mst_graph, mst_weights
