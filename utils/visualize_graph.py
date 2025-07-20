"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

import matplotlib.pyplot as plt
import networkx as nx
from .build_graph import build_graph


def visualize_graph(file_path):
    """Visualizes graph from file using matplotlib and networkx."""

    # build graph from file
    graph, edge_weights, meta = build_graph(file_path)

    # create networkx graph
    if meta["directed"]:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    # add nodes and edges
    for u in graph:
        for v in graph[u]:
            # get edge weight
            weight_key = f"{u}{v}" if u < v or meta["directed"] else f"{v}{u}"
            weight = edge_weights.get(weight_key, 1)
            G.add_edge(u, v, weight=weight)

    # set up plot
    plt.figure(figsize=(10, 8))
    plt.title(
        f"Graph from {file_path.split('/')[-1]} ({'Directed' if meta['directed'] else 'Undirected'})"
    )

    # position nodes using spring layout
    pos = nx.spring_layout(G, seed=42)

    # draw nodes
    source = meta.get("source")
    node_colors = ["red" if node == source else "lightblue" for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800)

    # draw edges
    if meta["directed"]:
        nx.draw_networkx_edges(
            G,
            pos,
            edge_color="gray",
            arrows=True,
            arrowsize=20,
            arrowstyle="->",
        )
    else:
        nx.draw_networkx_edges(
            G,
            pos,
            edge_color="gray",
        )

    # draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

    # draw edge weights
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)

    # add legend
    if source:
        plt.text(
            0.02,
            0.98,
            f"Source: {source} (red)",
            transform=plt.gca().transAxes,
            verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor="white"),
        )

    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    graph = "../graphs/four.txt"
    print(f"Visualizing graph from {graph}...")
    visualize_graph(graph)
