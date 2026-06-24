# How To: From Biadjacency Nodelist

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from biadjacency nodelist

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: row_order, column_order, create_using
```

## Step-by-Step Guide

### Step 1: Assign M = sp.sparse.csc_array(...)

```python
M = sp.sparse.csc_array([[1, 2], [0, 3]])
```

**Verification:**
```python
assert edges_equal(mapped_edges, B.edges())
```

### Step 2: Assign B_default = bipartite.from_biadjacency_matrix(...)

```python
B_default = bipartite.from_biadjacency_matrix(M, create_using=create_using())
```

### Step 3: Assign B = bipartite.from_biadjacency_matrix(...)

```python
B = bipartite.from_biadjacency_matrix(M, create_using=create_using(), row_order=row_order, column_order=column_order)
```

### Step 4: Assign row_order = value

```python
row_order = row_order if row_order else list(range(M.shape[0]))
```

### Step 5: Assign column_order = value

```python
column_order = column_order if column_order else list(range(M.shape[0], M.shape[0] + M.shape[1]))
```

### Step 6: Assign top_map = dict(...)

```python
top_map = dict(enumerate(row_order))
```

### Step 7: Assign bottom_map = value

```python
bottom_map = {idx + M.shape[0]: node for idx, node in enumerate(column_order)}
```

### Step 8: Assign mapped_edges = map_edges(...)

```python
mapped_edges = map_edges(B_default.edges())
```

**Verification:**
```python
assert edges_equal(mapped_edges, B.edges())
```


## Complete Example

```python
# Setup
# Fixtures: row_order, column_order, create_using

# Workflow
M = sp.sparse.csc_array([[1, 2], [0, 3]])
B_default = bipartite.from_biadjacency_matrix(M, create_using=create_using())
B = bipartite.from_biadjacency_matrix(M, create_using=create_using(), row_order=row_order, column_order=column_order)
row_order = row_order if row_order else list(range(M.shape[0]))
column_order = column_order if column_order else list(range(M.shape[0], M.shape[0] + M.shape[1]))
top_map = dict(enumerate(row_order))
bottom_map = {idx + M.shape[0]: node for idx, node in enumerate(column_order)}

def map_edges(edges):
    return [(top_map[u], bottom_map[v]) for u, v in edges]
mapped_edges = map_edges(B_default.edges())
assert edges_equal(mapped_edges, B.edges())
```

## Next Steps


---

*Source: test_matrix.py:94 | Complexity: Advanced | Last updated: 2026-06-02*