"""
Oscar Nolen
ITCS 6114
Project 2: Graph Algorithms
"""

def build_graph(file_path: str):
    """Builds graph from text file."""

    # adjacency list
    graph = {}
    # dictionary for weights
    edge_weights = {}
    # metadata
    meta = {}

    with open(file_path, 'r') as file:
        meta = file.readline().strip().split()
        
        # save metadata
        meta = {
            'num_vertices': int(meta[0]),
            'num_edges': int(meta[1]),
            'directed': (meta[2] == 'D')
        }

        for line in file:
            # node u, node v, weight or 'source'
            u, v, k = line.strip().split()

            # if last line, set source
            if u == 'source':
                meta['source'] = k
                continue
            # if not last line, convert weight to int
            weight = int(k)

            if u not in graph:
                graph[u] = []
            graph[u].append(v)

            # if undirected graph, add the reverse edge
            if not meta['directed']:
                if v not in graph:
                    graph[v] = []
                graph[v].append(u)

            # save edge weight with unique, consistent key
            weight_key = f'{u}{v}' if u < v or meta['directed'] else f'{v}{u}'
            edge_weights[weight_key] = weight

    return graph, edge_weights, meta

if __name__ == "__main__":
    graph, edge_weights, meta = build_graph('graphs/three.txt')
    print("GRAPH")
    print(graph)
    print("EDGE WEIGHTS")
    print(edge_weights)
    print("METADATA")
    print(meta)
