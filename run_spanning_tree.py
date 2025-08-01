"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

from algorithms import kruskal_mst, build_mst_graph
from utils import build_graph, visualize_graph


def write_mst_to_file(mst_graph, mst_weights, meta, source, file_path):
    """Writes MST to file in the original graph format."""

    num_edges = sum(len(neighbors) for neighbors in mst_graph.values()) // 2
    num_vertices = len(mst_graph)

    with open(file_path, "w") as f:
        f.write(f"{num_vertices} {num_edges} U\n")
        written = set()

        for u in mst_graph:
            for v in mst_graph[u]:
                if (u, v) not in written and (v, u) not in written:
                    key = f"{u}{v}" if u < v else f"{v}{u}"
                    weight = mst_weights.get(key, 1)
                    f.write(f"{u} {v} {weight}\n")
                    written.add((u, v))

        f.write(f"source : {source}\n")


def print_mst(graph, edge_weights, meta, source=None):
    """Prints and builds the MST using Kruskal's algorithm."""

    if source is None:
        source = meta.get("source", list(graph.keys())[0])

    print("Computing Minimum Spanning Tree using Kruskal's algorithm...")
    mst_edges, total_cost = kruskal_mst(graph, edge_weights, meta)

    print("\nMinimum Spanning Tree:")
    print("=" * 40)
    print(f"Total cost: {total_cost}")
    for u, v, weight in mst_edges:
        print(f"  {u} -- {v} : {weight}")

    mst_graph, mst_weights = build_mst_graph(mst_edges)
    return mst_edges, total_cost, mst_graph, mst_weights


def analyze_mst_and_visualize(graph_file):
    """Main workflow: load graph, run MST, write and visualize results."""

    print(f"Loading graph from {graph_file}...")
    graph, edge_weights, meta = build_graph(graph_file)

    if meta["directed"]:
        print("Warning: MST algorithm requires undirected graph.")
        return

    print("\nOriginal Graph Analysis:")
    print("=" * 40)
    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)

    total_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    total_weight = sum(edge_weights.values())

    print(f"Vertices: {len(vertices)}")
    print(f"Edges: {total_edges}")
    print(f"Total weight of all edges: {total_weight}")

    mst_edges, total_cost, mst_graph, mst_weights = print_mst(graph, edge_weights, meta)

    if mst_graph:
        print("\nMST Statistics:")
        print("=" * 40)
        print(f"MST edges: {len(mst_edges)}")
        print(f"MST vertices: {len(mst_graph)}")
        print(
            f"Weight reduction: {total_weight - total_cost} "
            f"({((total_weight - total_cost) / total_weight) * 100:.1f}%)"
        )

        source = meta.get("source", list(graph.keys())[0])
        mst_file = f"graphs/{graph_file.split('/')[-1].replace('.txt', '_mst.txt')}"
        write_mst_to_file(mst_graph, mst_weights, meta, source, mst_file)

        print(f"MST written to {mst_file}")

        print(f"\nVisualizing original graph from {graph_file}...")
        visualize_graph(graph_file)

        print(f"Visualizing MST from {mst_file}...")
        visualize_graph(mst_file)
    else:
        print("Error: Could not build MST.")


if __name__ == "__main__":
    graph_file = "graphs/one.txt"
    # graph_file = "graphs/four.txt"
    # graph_file = "graphs/five.txt"
    # graph_file = "graphs/six.txt"
    analyze_mst_and_visualize(graph_file)
