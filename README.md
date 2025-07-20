# Project 2

**Author:** Oscar Nolen  
**Course:** ITCS 6114  
**Project:** Graph Algorithms

## Overview

This project implements graph algorithms for shortest paths and minimum spanning trees. It includes the Bellman-Ford algorithm for shortest paths and Kruskal's algorithm for minimum spanning trees, with visualization capabilities for both.

## Project Structure

```
project_2/
├── run_shortest_path.py     # Main program for shortest-path tree
├── run_spanning_tree.py     # Main program for minimum spanning tree
├── algorithms/
│   ├── shortest_path.py     # Bellman-Ford algorithm
│   └── spanning_tree.py     # Kruskal's algorithm
├── utils/
│   ├── build_graph.py       # Graph parsing from text files
│   └── visualize_graph.py   # Graph visualization tools
└── graphs/
    ├── one.txt              # Sample undirected graph
    ├── two.txt              # Sample directed graph
    ├── three.txt            # Complex directed graph
    └── four.txt             # Complex undirected graph
```

## Graph File Format

The graph text files follow a standardized format:

```
<num_vertices> <num_edges> <graph_type>
<vertex1> <vertex2> <weight>
<vertex1> <vertex2> <weight>
...
source : <source_vertex>
```

**Format Details:**
- **Header line:** Number of vertices, number of edges, and graph type (`U` for undirected, `D` for directed)
- **Edge lines:** Each line specifies an edge with two vertices and the weight between them
- **Source line:** Specifies the source vertex for shortest path calculations

**Example:**
```
6 10 U
A B 1
A C 2
B C 1
source : A
```

This represents an undirected graph with 6 vertices and 10 edges, where vertex A is the source for shortest path calculations.

## Dependencies

Install required dependencies:
```bash
# create venv, activate
python3 -m venv .venv
source .venv/bin/activate

pip install matplotlib networkx
```

## Algorithm Implementation

### Bellman-Ford Algorithm

The Bellman-Ford algorithm finds shortest paths from a single source vertex to all other vertices in a weighted graph.

### Kruskal's Algorithm

Kruskal's algorithm finds the minimum spanning tree of an undirected weighted graph using a greedy approach with Union-Find data structure.

### Core Functions

**Shortest Path Functions:**
- `bellman_ford()`: Main algorithm implementation
- `relax()`: Edge relaxation helper function  
- `get_path()`: Path reconstruction from predecessors
- `print_shortest_paths()`: Formatted output and shortest path tree generation

**Minimum Spanning Tree Functions:**
- `kruskal_mst()`: Main MST algorithm implementation
- `UnionFind`: Data structure for cycle detection
- `print_mst()`: Formatted output and MST generation

## Testing the Algorithm

### Running with Sample Graphs

```bash
# Run shortest path analysis
python run_shortest_path.py

# Run minimum spanning tree analysis
python run_spanning_tree.py

# Change graph files in main sections to test different cases
```

### Sample Test Cases

1. **one.txt**: 6-vertex undirected graph, good for basic testing
2. **two.txt**: 4-vertex directed graph with cycles (shortest path only)
3. **three.txt**: 6-vertex directed graph with multiple paths (shortest path only)
4. **four.txt**: 7-vertex undirected graph with varied weights

### Expected Output Format

**Shortest Path Tree:**
```
Shortest paths from A:
A: 0 (A)
B: 2 (A -> C -> B)
C: 1 (A -> C)
D: 3 (A -> C -> D)
```

**Minimum Spanning Tree:**
```
Minimum Spanning Tree:
Total cost: 10
Edges in MST:
  A -- B : 2
  B -- C : 1
  C -- D : 2
```

Both programs generate output files and display visualizations of the original graph and resulting tree.

## Graph Visualization

The project includes visualization capabilities using matplotlib and networkx. Both programs automatically display the original graph and computed tree structures.
