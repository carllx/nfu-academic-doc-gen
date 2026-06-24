# How To: From Biadjacency Weight

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from biadjacency weight

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign M = sp.sparse.csc_array(...)

```python
M = sp.sparse.csc_array([[1, 2], [0, 3]])
```

**Verification:**
```python
assert edges_equal(B.edges(), [(0, 2), (0, 3), (1, 3)])
```

### Step 2: Assign B = bipartite.from_biadjacency_matrix(...)

```python
B = bipartite.from_biadjacency_matrix(M)
```

**Verification:**
```python
assert edges_equal(B.edges(data=True), e)
```

### Step 3: Assign B = bipartite.from_biadjacency_matrix(...)

```python
B = bipartite.from_biadjacency_matrix(M, edge_attribute='weight')
```

### Step 4: Assign e = value

```python
e = [(0, 2, {'weight': 1}), (0, 3, {'weight': 2}), (1, 3, {'weight': 3})]
```

**Verification:**
```python
assert edges_equal(B.edges(data=True), e)
```


## Complete Example

```python
# Workflow
M = sp.sparse.csc_array([[1, 2], [0, 3]])
B = bipartite.from_biadjacency_matrix(M)
assert edges_equal(B.edges(), [(0, 2), (0, 3), (1, 3)])
B = bipartite.from_biadjacency_matrix(M, edge_attribute='weight')
e = [(0, 2, {'weight': 1}), (0, 3, {'weight': 2}), (1, 3, {'weight': 3})]
assert edges_equal(B.edges(data=True), e)
```

## Next Steps


---

*Source: test_matrix.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*