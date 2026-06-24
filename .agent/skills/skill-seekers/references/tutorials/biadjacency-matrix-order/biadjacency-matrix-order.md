# How To: Biadjacency Matrix Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test biadjacency matrix order

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

**Verification:**
```python
assert M[1, 2] == 2
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(5)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 1, weight=2)
```

### Step 4: Assign X = value

```python
X = [3, 1]
```

### Step 5: Assign Y = value

```python
Y = [4, 2, 0]
```

### Step 6: Assign M = bipartite.biadjacency_matrix(...)

```python
M = bipartite.biadjacency_matrix(G, X, Y, weight='weight')
```

**Verification:**
```python
assert M[1, 2] == 2
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
G = nx.path_graph(5)
G.add_edge(0, 1, weight=2)
X = [3, 1]
Y = [4, 2, 0]
M = bipartite.biadjacency_matrix(G, X, Y, weight='weight')
assert M[1, 2] == 2
```

## Next Steps


---

*Source: test_basic.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*