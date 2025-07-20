# Project 2

**Author:** Oscar Nolen  
**Course:** ITCS 6114  
**Project:** Graph Algorithms

## Overview

This project implements the Bellman-Ford algorithm for finding shortest paths in weighted graphs. The implementation supports both directed and undirected graphs and includes visualization capabilities.

## Project Structure

```
project_2/
├── shortest_path.py          # Main Bellman-Ford implementation
├── utils/
│   ├── build_graph.py        # Graph parsing from text files
│   └── visualize_graph.py    # Graph visualization tools
└── graphs/
    ├── one.txt              # Sample undirected graph
    ├── two.txt              # Sample directed graph
    ├── three.txt            # Complex directed graph
    └── four.txt             # Complex undirected graph
```

## Algorithm Implementation

### Bellman-Ford Algorithm

The Bellman-Ford algorithm finds shortest paths from a single source vertex to all other vertices in a weighted graph. Key features of this implementation:

### Core Functions

- `bellman_ford()`: Main algorithm implementation
- `relax()`: Edge relaxation helper function  
- `get_path()`: Path reconstruction from predecessors
- `print_shortest_paths()`: Formatted output of results

## Testing the Algorithm

### Running with Sample Graphs

```bash
# Test with the default graph (one.txt)
python shortest_path.py

# Test with specific graphs by modifying the main section
# Edit the file path in shortest_path.py:
...
graph, edge_weights, meta = build_graph("graphs/one.txt")
...
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
```

## Graph Visualization

This project includes visualization capabilities using matplotlib and network. See `utils/visualize_graph`.
