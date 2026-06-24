# How To: Format Keyword

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format keyword

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign WP4 = nx.Graph(...)

```python
WP4 = nx.Graph()
```

### Step 2: Call WP4.add_edges_from()

```python
WP4.add_edges_from(((n, n + 1, {'weight': 0.5, 'other': 0.3}) for n in range(3)))
```

### Step 3: Assign P4 = nx.path_graph(...)

```python
P4 = nx.path_graph(4)
```

### Step 4: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='csr')
```

### Step 5: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

### Step 6: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='csc')
```

### Step 7: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

### Step 8: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='coo')
```

### Step 9: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

### Step 10: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='bsr')
```

### Step 11: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

### Step 12: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='lil')
```

### Step 13: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

### Step 14: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='dia')
```

### Step 15: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

### Step 16: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, format='dok')
```

### Step 17: Call np.testing.assert_equal()

```python
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```


## Complete Example

```python
# Workflow
WP4 = nx.Graph()
WP4.add_edges_from(((n, n + 1, {'weight': 0.5, 'other': 0.3}) for n in range(3)))
P4 = nx.path_graph(4)
A = nx.to_scipy_sparse_array(P4, format='csr')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
A = nx.to_scipy_sparse_array(P4, format='csc')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
A = nx.to_scipy_sparse_array(P4, format='coo')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
A = nx.to_scipy_sparse_array(P4, format='bsr')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
A = nx.to_scipy_sparse_array(P4, format='lil')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
A = nx.to_scipy_sparse_array(P4, format='dia')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
A = nx.to_scipy_sparse_array(P4, format='dok')
np.testing.assert_equal(A.todense(), nx.to_scipy_sparse_array(WP4, weight=None).todense())
```

## Next Steps


---

*Source: test_convert_scipy.py:122 | Complexity: Advanced | Last updated: 2026-06-02*