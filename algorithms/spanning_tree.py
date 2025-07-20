"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

class UnionFind:
    """Union-Find (Disjoint Set) data structure for Kruskal's algorithm."""

    def __init__(self, vertices):
        """Initialize with given vertices."""
        self.parent = {}
        self.rank = {}

        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        """Find root of vertex with path compression."""
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        """Union two sets by rank."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        # union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal_mst(graph, edge_weights, meta):
    """Kruskal's algorithm for minimum spanning tree."""

    # collect all vertices
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v in graph[u]:
            vertices.add(v)

    # collect all edges with weights
    edges = []
    for u in graph:
        for v in graph[u]:
            # avoid duplicate edges in undirected graph
            if u < v:
                weight_key = f"{u}{v}"
                weight = edge_weights.get(weight_key, float("inf"))
                edges.append((weight, u, v))

    # sort edges by weight
    edges.sort()

    # initialize union-find
    uf = UnionFind(vertices)

    # build MST
    mst_edges = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight

            # stop when we have n-1 edges
            if len(mst_edges) == len(vertices) - 1:
                break

    return mst_edges, total_cost


def build_mst_graph(mst_edges):
    """Builds MST as adjacency list and edge weights."""

    mst_graph = {}
    mst_weights = {}

    for u, v, weight in mst_edges:
        # add edge u -> v
        if u not in mst_graph:
            mst_graph[u] = []
        mst_graph[u].append(v)

        # add edge v -> u (undirected)
        if v not in mst_graph:
            mst_graph[v] = []
        mst_graph[v].append(u)

        # save edge weight with consistent key
        weight_key = f"{u}{v}" if u < v else f"{v}{u}"
        mst_weights[weight_key] = weight

    return mst_graph, mst_weights
