"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

from algorithms import bellman_ford, get_path
from utils import visualize_graph, build_graph


def build_shortest_path_tree(predecessors, distances):
    """Builds shortest path tree from predecessors and distances."""

    # shortest path tree as adjacency list
    tree = {}
    # edge weights for the tree
    tree_weights = {}

    for vertex, predecessor in predecessors.items():
        if predecessor is not None:
            # add edge from predecessor to vertex
            if predecessor not in tree:
                tree[predecessor] = []
            tree[predecessor].append(vertex)

            # calculate edge weight as distance difference
            weight = distances[vertex] - distances[predecessor]
            weight_key = f"{predecessor}{vertex}"
            tree_weights[weight_key] = weight

    return tree, tree_weights


def print_shortest_paths(graph, edge_weights, meta, source=None):
    """Prints shortest path tree from source vertex and returns tree structure."""

    if source is None:
        source = meta.get("source")

    if source is None:
        print("Error: No source vertex specified")
        return None, None, None, None, None

    distances, predecessors, negative_cycle = bellman_ford(
        graph, edge_weights, source, meta
    )

    if negative_cycle:
        print("WARNING: Negative cycle detected!")
        print()

    print(f"Shortest paths from {source}:")
    vertices = sorted(distances.keys())

    for vertex in vertices:
        if vertex == source:
            print(f"{vertex}: 0 ({vertex})")
        elif distances[vertex] == float("inf"):
            print(f"{vertex}: ∞ (no path)")
        else:
            path = get_path(predecessors, source, vertex)
            path_str = " -> ".join(path) if path else "no path"
            print(f"{vertex}: {distances[vertex]} ({path_str})")

    # Build and return the shortest path tree
    tree, tree_weights = build_shortest_path_tree(predecessors, distances)
    return distances, predecessors, negative_cycle, tree, tree_weights


def write_tree_to_file(tree, tree_weights, meta, source, file_path):
    """Writes shortest path tree to file in graph format."""

    # count edges in the tree
    num_edges = sum(len(neighbors) for neighbors in tree.values())

    # get all vertices in tree
    vertices = set([source])
    for u in tree:
        vertices.add(u)
        for v in tree[u]:
            vertices.add(v)

    num_vertices = len(vertices)

    with open(file_path, "w") as file:
        # write header: vertices, edges, direction (always directed for tree)
        file.write(f"{num_vertices} {num_edges} D\n")

        # write edges
        for u in tree:
            for v in tree[u]:
                weight_key = f"{u}{v}"
                weight = tree_weights.get(weight_key, 1)
                file.write(f"{u} {v} {weight}\n")

        # write source
        file.write(f"source : {source}\n")


def analyze_graph_and_visualize(graph_file):
    """Main function to analyze graph, build shortest path tree, and visualize results."""

    print(f"Loading graph from {graph_file}...")
    graph, edge_weights, meta = build_graph(graph_file)

    print("\nOriginal Graph Analysis:")
    print("=" * 40)
    _, _, _, tree, tree_weights = print_shortest_paths(graph, edge_weights, meta)

    if tree is not None:
        print("\nShortest Path Tree:")
        print("=" * 40)

        # write shortest path tree to file
        tree_file = f"graphs/{graph_file.split("/")[-1].replace(".txt", "_spt.txt")}"
        source = meta.get("source")
        write_tree_to_file(tree, tree_weights, meta, source, tree_file)

        print(f"Shortest path tree written to {tree_file}")
        print(f"Tree edges: {sum(len(neighbors) for neighbors in tree.values())}")
        print(
            f"Tree vertices: {len(set([source] + [u for u in tree] + [v for neighbors in tree.values() for v in neighbors]))}"
        )

        # visualize original graph
        print(f"\nVisualizing original graph from {graph_file}...")
        visualize_graph(graph_file)

        # visualize shortest path tree
        print(f"Visualizing shortest path tree from {tree_file}...")
        visualize_graph(tree_file)
    else:
        print("Error: Could not build shortest path tree")


if __name__ == "__main__":
    # analyze graph and visualize results
    graph_file = "graphs/one.txt"
    analyze_graph_and_visualize(graph_file)
