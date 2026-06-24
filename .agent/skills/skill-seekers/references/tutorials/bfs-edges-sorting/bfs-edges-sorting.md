# How To: Bfs Edges Sorting

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bfs edges sorting

## Prerequisites

**Required Modules:**
- `functools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign D = nx.DiGraph(...)

```python
D = nx.DiGraph()
```

**Verification:**
```python
assert list(edges_asc) == [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
```

### Step 2: Call D.add_edges_from()

```python
D.add_edges_from([(0, 1), (0, 2), (1, 4), (1, 3), (2, 5)])
```

**Verification:**
```python
assert list(edges_desc) == [(0, 2), (0, 1), (2, 5), (1, 4), (1, 3)]
```

### Step 3: Assign sort_desc = partial(...)

```python
sort_desc = partial(sorted, reverse=True)
```

### Step 4: Assign edges_asc = nx.bfs_edges(...)

```python
edges_asc = nx.bfs_edges(D, source=0, sort_neighbors=sorted)
```

### Step 5: Assign edges_desc = nx.bfs_edges(...)

```python
edges_desc = nx.bfs_edges(D, source=0, sort_neighbors=sort_desc)
```

**Verification:**
```python
assert list(edges_asc) == [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
```


## Complete Example

```python
# Workflow
D = nx.DiGraph()
D.add_edges_from([(0, 1), (0, 2), (1, 4), (1, 3), (2, 5)])
sort_desc = partial(sorted, reverse=True)
edges_asc = nx.bfs_edges(D, source=0, sort_neighbors=sorted)
edges_desc = nx.bfs_edges(D, source=0, sort_neighbors=sort_desc)
assert list(edges_asc) == [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
assert list(edges_desc) == [(0, 2), (0, 1), (2, 5), (1, 4), (1, 3)]
```

## Next Steps


---

*Source: test_bfs.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*