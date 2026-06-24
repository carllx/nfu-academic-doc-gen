# How To: Biadjacency Matrix Weight

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test biadjacency matrix weight

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
assert M[0, 0] == 2
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(5)
```

**Verification:**
```python
assert M[0, 0] == 4
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 1, weight=2, other=4)
```

### Step 4: Assign X = value

```python
X = [1, 3]
```

### Step 5: Assign Y = value

```python
Y = [0, 2, 4]
```

### Step 6: Assign M = bipartite.biadjacency_matrix(...)

```python
M = bipartite.biadjacency_matrix(G, X, weight='weight')
```

**Verification:**
```python
assert M[0, 0] == 2
```

### Step 7: Assign M = bipartite.biadjacency_matrix(...)

```python
M = bipartite.biadjacency_matrix(G, X, weight='other')
```

**Verification:**
```python
assert M[0, 0] == 4
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
G = nx.path_graph(5)
G.add_edge(0, 1, weight=2, other=4)
X = [1, 3]
Y = [0, 2, 4]
M = bipartite.biadjacency_matrix(G, X, weight='weight')
assert M[0, 0] == 2
M = bipartite.biadjacency_matrix(G, X, weight='other')
assert M[0, 0] == 4
```

## Next Steps


---

*Source: test_basic.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*