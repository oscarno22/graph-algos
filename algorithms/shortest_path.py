"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

def relax(u, v, edge_weights, distances, predecessors, directed):
    """Relaxes edge (u, v) if a shorter path is found."""

    # consistent key for edge weight lookup
    weight_key = f"{u}{v}" if u < v or directed else f"{v}{u}"
    weight = edge_weights.get(weight_key, float("inf"))

    # perform relaxation
    if distances[u] + weight < distances[v]:
        distances[v] = distances[u] + weight
        predecessors[v] = u


def bellman_ford(graph, edge_weights, source, meta):
    """Bellman-Ford algorithm for single-source shortest paths."""

    # initialize distances and predecessors
    distances = {}
    predecessors = {}

    # collect all vertices
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v in graph[u]:
            vertices.add(v)

    for vertex in vertices:
        distances[vertex] = float("inf")
        predecessors[vertex] = None
    distances[source] = 0

    # relax all edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, edge_weights, distances, predecessors, meta["directed"])

    # final pass to detect negative-weight cycles
    negative_cycle = False
    for u in graph:
        for v in graph[u]:
            weight_key = f"{u}{v}" if u < v or meta["directed"] else f"{v}{u}"
            weight = edge_weights.get(weight_key, float("inf"))
            if distances[u] + weight < distances[v]:
                negative_cycle = True
                break
        if negative_cycle:
            break

    return distances, predecessors, negative_cycle


def get_path(predecessors, source, target):
    """Reconstructs path from source to target using predecessors."""

    if target not in predecessors:
        return None

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()

    # check if path starts at source
    if not path or path[0] != source:
        return None

    return path
