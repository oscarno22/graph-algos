# Project 2

**Author:** Oscar Nolen  
**Course:** ITCS 6114  
**Project:** Graph Algorithms

## Overview

This project implements the Bellman-Ford algorithm for finding shortest paths in weighted graphs. The implementation supports both directed and undirected graphs, builds shortest path trees, and includes visualization capabilities.

## Project Structure

```
project_2/
├── run_shortest_path.py          # Main program for shortest-path tree
├── utils/
│   ├── build_graph.py        # Graph parsing from text files
│   └── visualize_graph.py    # Graph visualization tools
└── graphs/
    ├── one.txt              # Sample undirected graph
    ├── two.txt              # Sample directed graph
    ├── three.txt            # Complex directed graph
    └── four.txt             # Complex undirected graph
└── algorithms/
    ├── shortest_path.py     # Bellman-Ford algorithm
    └── spanning_tree.py     # Prim's algorithm
```

## Dependencies

Install required dependencies:
```bash
pip install matplotlib networkx
```

## Algorithm Implementation

### Bellman-Ford Algorithm

The Bellman-Ford algorithm finds shortest paths from a single source vertex to all other vertices in a weighted graph. Key features of this implementation:

### Core Functions

- `bellman_ford()`: Main algorithm implementation
- `relax()`: Edge relaxation helper function  
- `get_path()`: Path reconstruction from predecessors
- `print_shortest_paths()`: Formatted output and shortest path tree generation
- `build_shortest_path_tree()`: Constructs tree from algorithm results
- `write_tree_to_file()`: Exports tree in graph format for visualization

## Testing the Algorithm

### Running with Sample Graphs

```bash
# Run analysis with visualization
python shortest_path.py

# Change graph in main section to test different cases
# Edit the graph_file variable in analyze_graph_and_visualize()
```

### Sample Test Cases

1. **one.txt**: 6-vertex undirected graph, good for basic testing
2. **two.txt**: 4-vertex directed graph with cycles
3. **three.txt**: 6-vertex directed graph with multiple paths
4. **four.txt**: 7-vertex undirected graph with varied weights

### Expected Output Format

```
Shortest paths from A:
A: 0 (A)
B: 2 (A -> C -> B)
C: 1 (A -> C)
D: 3 (A -> C -> D)
E: 4 (A -> C -> B -> E)
F: 4 (A -> C -> D -> F)

Shortest Path Tree:
Tree edges: 5
Tree vertices: 6
```

The program also generates a shortest path tree file and displays visualizations of both the original graph and the resulting shortest path tree.

## Graph Visualization

This project includes visualization capabilities using matplotlib and networkx. The program automatically displays both the original graph and the computed shortest path tree.
