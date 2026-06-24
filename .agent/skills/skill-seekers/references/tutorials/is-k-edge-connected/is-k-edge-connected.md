# How To: Is K Edge Connected

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is k edge connected

## Prerequisites

**Required Modules:**
- `itertools`
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.connectivity`
- `networkx.algorithms.connectivity.edge_augmentation`
- `networkx.utils`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(10, 0)
```

**Verification:**
```python
assert is_k_edge_connected(G, k=1)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert not is_k_edge_connected(G, k=2)
```

### Step 3: Call G.add_nodes_from()

```python
G.add_nodes_from([5, 15])
```

**Verification:**
```python
assert not is_k_edge_connected(G, k=1)
```

### Step 4: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert not is_k_edge_connected(G, k=2)
```

### Step 5: Assign G = nx.compose(...)

```python
G = nx.compose(nx.complete_graph([0, 1, 2]), nx.complete_graph([3, 4, 5]))
```

**Verification:**
```python
assert is_k_edge_connected(G, k=1)
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(10, 0)
assert is_k_edge_connected(G, k=1)
assert not is_k_edge_connected(G, k=2)
G = nx.Graph()
G.add_nodes_from([5, 15])
assert not is_k_edge_connected(G, k=1)
assert not is_k_edge_connected(G, k=2)
G = nx.complete_graph(5)
assert is_k_edge_connected(G, k=1)
assert is_k_edge_connected(G, k=2)
assert is_k_edge_connected(G, k=3)
assert is_k_edge_connected(G, k=4)
G = nx.compose(nx.complete_graph([0, 1, 2]), nx.complete_graph([3, 4, 5]))
assert not is_k_edge_connected(G, k=1)
assert not is_k_edge_connected(G, k=2)
assert not is_k_edge_connected(G, k=3)
```

## Next Steps


---

*Source: test_edge_augmentation.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*