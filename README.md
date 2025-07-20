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

- **Handles negative weights**: Unlike Dijkstra's algorithm, Bellman-Ford can process negative edge weights
- **Detects negative cycles**: The algorithm can identify if the graph contains negative-weight cycles
- **Works with both directed and undirected graphs**: Automatically handles graph type based on input format

### Core Functions

- `bellman_ford()`: Main algorithm implementation
- `relax()`: Edge relaxation helper function  
- `get_path()`: Path reconstruction from predecessors
- `print_shortest_paths()`: Formatted output of results

## Testing the Algorithm

### Running with Sample Graphs

```bash
# Test with the default graph (four.txt)
python shortest_path.py

# Test with specific graphs by modifying the main section
# Edit the file path in shortest_path.py:
graph, edge_weights, meta = build_graph("graphs/one.txt")
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

## Graph File Format

### Structure

```
<num_vertices> <num_edges> <D|U>
<vertex1> <vertex2> <weight>
<vertex1> <vertex2> <weight>
...
source : <source_vertex>
```

### Example: Directed Graph

```
4 5 D
A B 1
A C 2
A D 5
C A 2
C D 1
source : A
```

### Example: Undirected Graph

```
6 10 U
A B 1
A C 2
B C 1
B D 3
B E 2
C D 1
C E 2
D E 4
D F 3
E F 3
source : A
```

## Creating Custom Test Graphs

### Guidelines

1. **Choose graph type**: Decide between directed (`D`) or undirected (`U`)
2. **Plan connectivity**: Ensure interesting paths exist between vertices
3. **Weight selection**: 
   - Use positive weights for basic testing
   - Include negative weights to test advanced features
   - Avoid negative cycles unless testing detection
4. **Size considerations**: Start small (4-8 vertices) for easier verification

### Testing Strategy

1. **Manual verification**: Calculate expected shortest paths by hand for small graphs
2. **Edge cases**: Test with:
   - Disconnected vertices
   - Self-loops
   - Multiple paths of same cost
   - Negative weights
3. **Incremental testing**: Start simple, then add complexity

## Graph Visualization

The project includes visualization capabilities using matplotlib and networkx:

```python
from utils.visualize_graph import visualize_graph
visualize_graph("graphs/your_graph.txt")
```
