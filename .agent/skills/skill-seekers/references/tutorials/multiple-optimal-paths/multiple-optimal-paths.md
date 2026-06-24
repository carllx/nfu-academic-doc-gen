# How To: Multiple Optimal Paths

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that A* algorithm finds any of multiple optimal paths

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests that A* algorithm finds any of multiple optimal paths'

```python
'Tests that A* algorithm finds any of multiple optimal paths'
```

**Verification:**
```python
assert nx.astar_path(graph, 'a', 'd', h) in (path1, path2)
```

### Step 2: Assign heuristic_values = value

```python
heuristic_values = {'a': 1.35, 'b': 1.18, 'c': 0.67, 'd': 0}
```

### Step 3: Assign graph = nx.Graph(...)

```python
graph = nx.Graph()
```

### Step 4: Assign points = value

```python
points = ['a', 'b', 'c', 'd']
```

### Step 5: Assign edges = value

```python
edges = [('a', 'b', 0.18), ('a', 'c', 0.68), ('b', 'c', 0.5), ('c', 'd', 0.67)]
```

### Step 6: Call graph.add_nodes_from()

```python
graph.add_nodes_from(points)
```

### Step 7: Call graph.add_weighted_edges_from()

```python
graph.add_weighted_edges_from(edges)
```

### Step 8: Assign path1 = value

```python
path1 = ['a', 'c', 'd']
```

### Step 9: Assign path2 = value

```python
path2 = ['a', 'b', 'c', 'd']
```

**Verification:**
```python
assert nx.astar_path(graph, 'a', 'd', h) in (path1, path2)
```


## Complete Example

```python
# Workflow
'Tests that A* algorithm finds any of multiple optimal paths'
heuristic_values = {'a': 1.35, 'b': 1.18, 'c': 0.67, 'd': 0}

def h(u, v):
    return heuristic_values[u]
graph = nx.Graph()
points = ['a', 'b', 'c', 'd']
edges = [('a', 'b', 0.18), ('a', 'c', 0.68), ('b', 'c', 0.5), ('c', 'd', 0.67)]
graph.add_nodes_from(points)
graph.add_weighted_edges_from(edges)
path1 = ['a', 'c', 'd']
path2 = ['a', 'b', 'c', 'd']
assert nx.astar_path(graph, 'a', 'd', h) in (path1, path2)
```

## Next Steps


---

*Source: test_astar.py:25 | Complexity: Advanced | Last updated: 2026-06-02*