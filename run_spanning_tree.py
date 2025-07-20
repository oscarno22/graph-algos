"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

from algorithms import kruskal_mst, build_mst_graph
from utils import build_graph, visualize_graph


def write_mst_to_file(mst_graph, mst_weights, meta, source, file_path):
    """Writes MST to file in graph format."""

    # count edges (divide by 2 since undirected)
    num_edges = sum(len(neighbors) for neighbors in mst_graph.values()) // 2

    # get all vertices
    vertices = set()
    for u in mst_graph:
        vertices.add(u)
        for v in mst_graph[u]:
            vertices.add(v)

    num_vertices = len(vertices)

    with open(file_path, "w") as file:
        # write header: vertices, edges, undirected
        file.write(f"{num_vertices} {num_edges} U\n")

        # write edges (avoid duplicates)
        written_edges = set()
        for u in mst_graph:
            for v in mst_graph[u]:
                if u < v:  # avoid duplicate edges
                    weight_key = f"{u}{v}"
                    weight = mst_weights.get(weight_key, 1)
                    file.write(f"{u} {v} {weight}\n")
                    written_edges.add((u, v))

        # write source
        file.write(f"source : {source}\n")


def print_mst(graph, edge_weights, meta, source=None):
    """Prints minimum spanning tree and returns tree structure."""

    if source is None:
        source = meta.get("source", list(graph.keys())[0])

    print("Computing Minimum Spanning Tree using Kruskal's algorithm...")
    mst_edges, total_cost = kruskal_mst(graph, edge_weights, meta)

    print("\nMinimum Spanning Tree:")
    print("=" * 40)
    print(f"Total cost: {total_cost}")
    print("Edges in MST:")

    for u, v, weight in mst_edges:
        print(f"  {u} -- {v} : {weight}")

    # build MST graph structure
    mst_graph, mst_weights = build_mst_graph(mst_edges)

    return mst_edges, total_cost, mst_graph, mst_weights


def analyze_mst_and_visualize(graph_file):
    """Main function to analyze graph, build MST, and visualize results."""

    print(f"Loading graph from {graph_file}...")
    graph, edge_weights, meta = build_graph(graph_file)

    # ensure graph is undirected
    if meta["directed"]:
        print("Warning: MST algorithm requires undirected graph")
        return

    print("\nOriginal Graph Analysis:")
    print("=" * 40)

    # print graph info
    vertices = set()
    for u in graph:
        vertices.add(u)
        for v in graph[u]:
            vertices.add(v)

    total_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    total_weight = sum(edge_weights.values())

    print(f"Vertices: {len(vertices)}")
    print(f"Edges: {total_edges}")
    print(f"Total weight of all edges: {total_weight}")

    # compute MST
    mst_edges, total_cost, mst_graph, mst_weights = print_mst(graph, edge_weights, meta)

    if mst_graph:
        print("\nMST Statistics:")
        print("=" * 40)

        # write MST to file
        mst_file = f"graphs/{graph_file.split('/')[-1].replace('.txt', '_mst.txt')}"
        source = meta.get("source", list(graph.keys())[0])
        write_mst_to_file(mst_graph, mst_weights, meta, source, mst_file)

        print(f"MST written to {mst_file}")
        print(f"MST edges: {len(mst_edges)}")
        print(
            f"MST vertices: {len(set(u for u, v, w in mst_edges).union(set(v for u, v, w in mst_edges)))}"
        )
        print(
            f"Weight reduction: {total_weight - total_cost} ({((total_weight - total_cost) / total_weight * 100):.1f}%)"
        )

        # visualize original graph
        print(f"\nVisualizing original graph from {graph_file}...")
        visualize_graph(graph_file)

        # visualize MST
        print(f"Visualizing MST from {mst_file}...")
        visualize_graph(mst_file)
    else:
        print("Error: Could not build MST")


if __name__ == "__main__":
    # analyze graph and visualize MST
    graph_file = "graphs/four.txt"
    analyze_mst_and_visualize(graph_file)
