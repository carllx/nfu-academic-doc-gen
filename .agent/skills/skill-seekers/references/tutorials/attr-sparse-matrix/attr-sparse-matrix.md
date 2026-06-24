# How To: Attr Sparse Matrix

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attr sparse matrix

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

**Verification:**
```python
assert M[1] == [0, 1, 2]
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 1, thickness=1, weight=3)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 2, thickness=2)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2, thickness=3)
```

### Step 6: Assign M = nx.attr_sparse_matrix(...)

```python
M = nx.attr_sparse_matrix(G)
```

### Step 7: Assign mtx = value

```python
mtx = M[0]
```

### Step 8: Assign data = np.ones(...)

```python
data = np.ones((3, 3), float)
```

### Step 9: Call np.fill_diagonal()

```python
np.fill_diagonal(data, 0)
```

### Step 10: Call np.testing.assert_equal()

```python
np.testing.assert_equal(mtx.todense(), np.array(data))
```

**Verification:**
```python
assert M[1] == [0, 1, 2]
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
G = nx.Graph()
G.add_edge(0, 1, thickness=1, weight=3)
G.add_edge(0, 2, thickness=2)
G.add_edge(1, 2, thickness=3)
M = nx.attr_sparse_matrix(G)
mtx = M[0]
data = np.ones((3, 3), float)
np.fill_diagonal(data, 0)
np.testing.assert_equal(mtx.todense(), np.array(data))
assert M[1] == [0, 1, 2]
```

## Next Steps


---

*Source: test_attrmatrix.py:79 | Complexity: Advanced | Last updated: 2026-06-02*