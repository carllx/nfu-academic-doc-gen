# How To: Random Spanning Tree Multiplicative Small

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Using a fixed seed, sample one tree for repeatability.

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

### Step 1: '\n    Using a fixed seed, sample one tree for repeatability.\n    '

```python
'\n    Using a fixed seed, sample one tree for repeatability.\n    '
```

**Verification:**
```python
assert nx.utils.edges_equal(solution.edges, sampled_tree.edges)
```

### Step 2: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 3: Assign gamma = value

```python
gamma = {(0, 1): -0.6383, (0, 2): -0.6827, (0, 5): 0, (1, 2): -1.0781, (1, 4): 0, (2, 3): 0, (5, 3): -0.282, (5, 4): -0.3327, (4, 3): -0.9927}
```

### Step 4: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 5: Assign solution_edges = value

```python
solution_edges = [(2, 3), (3, 4), (0, 5), (5, 4), (4, 1)]
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
sampled_tree = nx.random_spanning_tree(G, 'lambda_key', seed=42)
```

**Verification:**
```python
assert nx.utils.edges_equal(solution.edges, sampled_tree.edges)
```

### Step 9: Call G.add_edge()

```python
G.add_edge(u, v, lambda_key=exp(gamma[u, v]))
```


## Complete Example

```python
# Workflow
'\n    Using a fixed seed, sample one tree for repeatability.\n    '
from math import exp
pytest.importorskip('scipy')
gamma = {(0, 1): -0.6383, (0, 2): -0.6827, (0, 5): 0, (1, 2): -1.0781, (1, 4): 0, (2, 3): 0, (5, 3): -0.282, (5, 4): -0.3327, (4, 3): -0.9927}
G = nx.Graph()
for u, v in gamma:
    G.add_edge(u, v, lambda_key=exp(gamma[u, v]))
solution_edges = [(2, 3), (3, 4), (0, 5), (5, 4), (4, 1)]
solution = nx.Graph()
solution.add_edges_from(solution_edges)
sampled_tree = nx.random_spanning_tree(G, 'lambda_key', seed=42)
assert nx.utils.edges_equal(solution.edges, sampled_tree.edges)
```

## Next Steps


---

*Source: test_mst.py:536 | Complexity: Advanced | Last updated: 2026-06-02*