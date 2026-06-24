# How To: Random Spanning Tree Additive Small

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Sample a single spanning tree from the additive method.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `math`
- `math`
- `random`
- `random`
- `itertools`


## Step-by-Step Guide

### Step 1: '\n    Sample a single spanning tree from the additive method.\n    '

```python
'\n    Sample a single spanning tree from the additive method.\n    '
```

**Verification:**
```python
assert nx.utils.edges_equal(solution.edges, sampled_tree.edges)
```

### Step 2: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 3: Assign edges = value

```python
edges = {(0, 1): 1, (0, 2): 1, (0, 5): 3, (1, 2): 2, (1, 4): 3, (2, 3): 3, (5, 3): 4, (5, 4): 5, (4, 3): 4}
```

### Step 4: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 5: Assign solution_edges = value

```python
solution_edges = [(0, 2), (1, 2), (2, 3), (3, 4), (3, 5)]
```

### Step 6: Assign solution = nx.Graph(...)

```python
solution = nx.Graph()
```

### Step 7: Call solution.add_edges_from()

```python
solution.add_edges_from(solution_edges)
```

### Step 8: Assign sampled_tree = nx.random_spanning_tree(...)

```python
sampled_tree = nx.random_spanning_tree(G, weight='weight', multiplicative=False, seed=37)
```

**Verification:**
```python
assert nx.utils.edges_equal(solution.edges, sampled_tree.edges)
```

### Step 9: Call G.add_edge()

```python
G.add_edge(u, v, weight=edges[u, v])
```


## Complete Example

```python
# Workflow
'\n    Sample a single spanning tree from the additive method.\n    '
pytest.importorskip('scipy')
edges = {(0, 1): 1, (0, 2): 1, (0, 5): 3, (1, 2): 2, (1, 4): 3, (2, 3): 3, (5, 3): 4, (5, 4): 5, (4, 3): 4}
G = nx.Graph()
for u, v in edges:
    G.add_edge(u, v, weight=edges[u, v])
solution_edges = [(0, 2), (1, 2), (2, 3), (3, 4), (3, 5)]
solution = nx.Graph()
solution.add_edges_from(solution_edges)
sampled_tree = nx.random_spanning_tree(G, weight='weight', multiplicative=False, seed=37)
assert nx.utils.edges_equal(solution.edges, sampled_tree.edges)
```

## Next Steps


---

*Source: test_mst.py:662 | Complexity: Advanced | Last updated: 2026-06-02*