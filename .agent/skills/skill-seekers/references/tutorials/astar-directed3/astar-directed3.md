# How To: Astar Directed3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astar directed3

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign heuristic_values = value

```python
heuristic_values = {'n5': 36, 'n2': 4, 'n1': 0, 'n0': 0}
```

**Verification:**
```python
assert nx.astar_path(graph, 'n5', 'n0', h) == answer
```

### Step 2: Assign edges = value

```python
edges = [('n5', 'n1', 11), ('n5', 'n2', 9), ('n2', 'n1', 1), ('n1', 'n0', 32)]
```

### Step 3: Assign graph = nx.DiGraph(...)

```python
graph = nx.DiGraph()
```

### Step 4: Call graph.add_weighted_edges_from()

```python
graph.add_weighted_edges_from(edges)
```

### Step 5: Assign answer = value

```python
answer = ['n5', 'n2', 'n1', 'n0']
```

**Verification:**
```python
assert nx.astar_path(graph, 'n5', 'n0', h) == answer
```


## Complete Example

```python
# Workflow
heuristic_values = {'n5': 36, 'n2': 4, 'n1': 0, 'n0': 0}

def h(u, v):
    return heuristic_values[u]
edges = [('n5', 'n1', 11), ('n5', 'n2', 9), ('n2', 'n1', 1), ('n1', 'n0', 32)]
graph = nx.DiGraph()
graph.add_weighted_edges_from(edges)
answer = ['n5', 'n2', 'n1', 'n0']
assert nx.astar_path(graph, 'n5', 'n0', h) == answer
```

## Next Steps


---

*Source: test_astar.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*