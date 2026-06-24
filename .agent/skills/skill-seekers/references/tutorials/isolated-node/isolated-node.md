# How To: Isolated Node

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isolated node

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

### Step 1: Assign edges = value

```python
edges = [(0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)]
```

**Verification:**
```python
assert edges_equal(actual, shift)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(u + 1, v + 1, wt) for u, v, wt in edges])
```

### Step 4: Call G.add_node()

```python
G.add_node(0)
```

### Step 5: Assign edges = nx.minimum_spanning_edges(...)

```python
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False, ignore_nan=True)
```

### Step 6: Assign actual = sorted(...)

```python
actual = sorted(((min(u, v), max(u, v)) for u, v in edges))
```

### Step 7: Assign shift = value

```python
shift = [(u + 1, v + 1) for u, v, d in self.minimum_spanning_edgelist]
```

**Verification:**
```python
assert edges_equal(actual, shift)
```


## Complete Example

```python
# Workflow
edges = [(0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)]
G = nx.Graph()
G.add_weighted_edges_from([(u + 1, v + 1, wt) for u, v, wt in edges])
G.add_node(0)
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False, ignore_nan=True)
actual = sorted(((min(u, v), max(u, v)) for u, v in edges))
shift = [(u + 1, v + 1) for u, v, d in self.minimum_spanning_edgelist]
assert edges_equal(actual, shift)
```

## Next Steps


---

*Source: test_mst.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*