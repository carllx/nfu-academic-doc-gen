# How To: Zero Distance

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zero distance

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign XG = nx.DiGraph(...)

```python
XG = nx.DiGraph()
```

**Verification:**
```python
assert dist[u][u] == 0
```

### Step 2: Call XG.add_weighted_edges_from()

```python
XG.add_weighted_edges_from([('s', 'u', 10), ('s', 'x', 5), ('u', 'v', 1), ('u', 'x', 2), ('v', 'y', 1), ('x', 'u', 3), ('x', 'v', 5), ('x', 'y', 2), ('y', 's', 7), ('y', 'v', 6)])
```

### Step 3: Assign unknown = nx.floyd_warshall_predecessor_and_distance(...)

```python
path, dist = nx.floyd_warshall_predecessor_and_distance(XG)
```

### Step 4: Assign GG = XG.to_undirected(...)

```python
GG = XG.to_undirected()
```

### Step 5: Assign unknown = 2

```python
GG['u']['x']['weight'] = 2
```

### Step 6: Assign unknown = nx.floyd_warshall_predecessor_and_distance(...)

```python
path, dist = nx.floyd_warshall_predecessor_and_distance(GG)
```

**Verification:**
```python
assert dist[u][u] == 0
```

### Step 7: Assign unknown = 0

```python
dist[u][u] = 0
```


## Complete Example

```python
# Workflow
XG = nx.DiGraph()
XG.add_weighted_edges_from([('s', 'u', 10), ('s', 'x', 5), ('u', 'v', 1), ('u', 'x', 2), ('v', 'y', 1), ('x', 'u', 3), ('x', 'v', 5), ('x', 'y', 2), ('y', 's', 7), ('y', 'v', 6)])
path, dist = nx.floyd_warshall_predecessor_and_distance(XG)
for u in XG:
    assert dist[u][u] == 0
GG = XG.to_undirected()
GG['u']['x']['weight'] = 2
path, dist = nx.floyd_warshall_predecessor_and_distance(GG)
for u in GG:
    dist[u][u] = 0
```

## Next Steps


---

*Source: test_dense.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*