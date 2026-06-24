# How To: From Scipy Sparse Array Parallel Edges

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the :func:`networkx.from_scipy_sparse_array` function
interprets integer weights as the number of parallel edges when
creating a multigraph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests that the :func:`networkx.from_scipy_sparse_array` function\n        interprets integer weights as the number of parallel edges when\n        creating a multigraph.\n\n        '

```python
'Tests that the :func:`networkx.from_scipy_sparse_array` function\n        interprets integer weights as the number of parallel edges when\n        creating a multigraph.\n\n        '
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 2: Assign A = sp.sparse.csr_array(...)

```python
A = sp.sparse.csr_array([[1, 1], [1, 2]])
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 3: Assign expected = nx.DiGraph(...)

```python
expected = nx.DiGraph()
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 4: Assign edges = value

```python
edges = [(0, 0), (0, 1), (1, 0)]
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 5: Call expected.add_weighted_edges_from()

```python
expected.add_weighted_edges_from([(u, v, 1) for u, v in edges])
```

### Step 6: Call expected.add_edge()

```python
expected.add_edge(1, 1, weight=2)
```

### Step 7: Assign actual = nx.from_scipy_sparse_array(...)

```python
actual = nx.from_scipy_sparse_array(A, parallel_edges=True, create_using=nx.DiGraph)
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 8: Assign actual = nx.from_scipy_sparse_array(...)

```python
actual = nx.from_scipy_sparse_array(A, parallel_edges=False, create_using=nx.DiGraph)
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 9: Assign edges = value

```python
edges = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 1)]
```

### Step 10: Assign expected = nx.MultiDiGraph(...)

```python
expected = nx.MultiDiGraph()
```

### Step 11: Call expected.add_weighted_edges_from()

```python
expected.add_weighted_edges_from([(u, v, 1) for u, v in edges])
```

### Step 12: Assign actual = nx.from_scipy_sparse_array(...)

```python
actual = nx.from_scipy_sparse_array(A, parallel_edges=True, create_using=nx.MultiDiGraph)
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```

### Step 13: Assign expected = nx.MultiDiGraph(...)

```python
expected = nx.MultiDiGraph()
```

### Step 14: Call expected.add_edges_from()

```python
expected.add_edges_from(set(edges), weight=1)
```

### Step 15: Assign unknown = 2

```python
expected[1][1][0]['weight'] = 2
```

### Step 16: Assign actual = nx.from_scipy_sparse_array(...)

```python
actual = nx.from_scipy_sparse_array(A, parallel_edges=False, create_using=nx.MultiDiGraph)
```

**Verification:**
```python
assert graphs_equal(actual, expected)
```


## Complete Example

```python
# Workflow
'Tests that the :func:`networkx.from_scipy_sparse_array` function\n        interprets integer weights as the number of parallel edges when\n        creating a multigraph.\n\n        '
A = sp.sparse.csr_array([[1, 1], [1, 2]])
expected = nx.DiGraph()
edges = [(0, 0), (0, 1), (1, 0)]
expected.add_weighted_edges_from([(u, v, 1) for u, v in edges])
expected.add_edge(1, 1, weight=2)
actual = nx.from_scipy_sparse_array(A, parallel_edges=True, create_using=nx.DiGraph)
assert graphs_equal(actual, expected)
actual = nx.from_scipy_sparse_array(A, parallel_edges=False, create_using=nx.DiGraph)
assert graphs_equal(actual, expected)
edges = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 1)]
expected = nx.MultiDiGraph()
expected.add_weighted_edges_from([(u, v, 1) for u, v in edges])
actual = nx.from_scipy_sparse_array(A, parallel_edges=True, create_using=nx.MultiDiGraph)
assert graphs_equal(actual, expected)
expected = nx.MultiDiGraph()
expected.add_edges_from(set(edges), weight=1)
expected[1][1][0]['weight'] = 2
actual = nx.from_scipy_sparse_array(A, parallel_edges=False, create_using=nx.MultiDiGraph)
assert graphs_equal(actual, expected)
```

## Next Steps


---

*Source: test_convert_scipy.py:212 | Complexity: Advanced | Last updated: 2026-06-02*