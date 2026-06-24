# How To: Zero Weight

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zero weight

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert int(np.min(dist)) == -14
```

### Step 2: Assign edges = value

```python
edges = [(1, 2, -2), (2, 3, -4), (1, 5, 1), (5, 4, 0), (4, 3, -5), (2, 5, -7)]
```

**Verification:**
```python
assert int(np.min(dist)) == -14
```

### Step 3: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from(edges)
```

### Step 4: Assign dist = nx.floyd_warshall_numpy(...)

```python
dist = nx.floyd_warshall_numpy(G)
```

**Verification:**
```python
assert int(np.min(dist)) == -14
```

### Step 5: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph()
```

### Step 6: Call edges.append()

```python
edges.append((2, 5, -7))
```

### Step 7: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from(edges)
```

### Step 8: Assign dist = nx.floyd_warshall_numpy(...)

```python
dist = nx.floyd_warshall_numpy(G)
```

**Verification:**
```python
assert int(np.min(dist)) == -14
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
edges = [(1, 2, -2), (2, 3, -4), (1, 5, 1), (5, 4, 0), (4, 3, -5), (2, 5, -7)]
G.add_weighted_edges_from(edges)
dist = nx.floyd_warshall_numpy(G)
assert int(np.min(dist)) == -14
G = nx.MultiDiGraph()
edges.append((2, 5, -7))
G.add_weighted_edges_from(edges)
dist = nx.floyd_warshall_numpy(G)
assert int(np.min(dist)) == -14
```

## Next Steps


---

*Source: test_dense_numpy.py:67 | Complexity: Advanced | Last updated: 2026-06-02*