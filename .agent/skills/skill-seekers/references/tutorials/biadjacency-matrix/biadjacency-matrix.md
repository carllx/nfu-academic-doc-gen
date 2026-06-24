# How To: Biadjacency Matrix

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test biadjacency matrix

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
assert M.shape[0] == tops[i]
```

### Step 2: Assign tops = value

```python
tops = [2, 5, 10]
```

**Verification:**
```python
assert M.shape[1] == bots[i]
```

### Step 3: Assign bots = value

```python
bots = [5, 10, 15]
```

### Step 4: Assign G = bipartite.random_graph(...)

```python
G = bipartite.random_graph(tops[i], bots[i], 0.2)
```

### Step 5: Assign top = value

```python
top = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
```

### Step 6: Assign M = bipartite.biadjacency_matrix(...)

```python
M = bipartite.biadjacency_matrix(G, top)
```

**Verification:**
```python
assert M.shape[0] == tops[i]
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
tops = [2, 5, 10]
bots = [5, 10, 15]
for i in range(len(tops)):
    G = bipartite.random_graph(tops[i], bots[i], 0.2)
    top = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
    M = bipartite.biadjacency_matrix(G, top)
    assert M.shape[0] == tops[i]
    assert M.shape[1] == bots[i]
```

## Next Steps


---

*Source: test_basic.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*