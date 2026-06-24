# How To: Directed Combinatorial Laplacian

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Directed combinatorial Laplacian

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Directed combinatorial Laplacian'

```python
'Directed combinatorial Laplacian'
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(((1, 2), (1, 3), (3, 1), (3, 2), (3, 5), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4)))
```

### Step 4: Assign GL = np.array(...)

```python
GL = np.array([[0.0366, -0.0132, -0.0153, -0.0034, -0.002, -0.0027], [-0.0132, 0.045, -0.0111, -0.0076, -0.0062, -0.0069], [-0.0153, -0.0111, 0.0408, -0.0035, -0.0083, -0.0027], [-0.0034, -0.0076, -0.0035, 0.3688, -0.1356, -0.2187], [-0.002, -0.0062, -0.0083, -0.1356, 0.2026, -0.0505], [-0.0027, -0.0069, -0.0027, -0.2187, -0.0505, 0.2815]])
```

### Step 5: Assign L = nx.directed_combinatorial_laplacian_matrix(...)

```python
L = nx.directed_combinatorial_laplacian_matrix(G, alpha=0.9, nodelist=sorted(G))
```

### Step 6: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(L, GL, decimal=3)
```

### Step 7: Call G.add_edges_from()

```python
G.add_edges_from(((2, 5), (6, 1)))
```

### Step 8: Assign GL = np.array(...)

```python
GL = np.array([[0.1395, -0.0349, -0.0465, 0.0, 0.0, -0.0581], [-0.0349, 0.093, -0.0116, 0.0, -0.0465, 0.0], [-0.0465, -0.0116, 0.0698, 0.0, -0.0116, 0.0], [0.0, 0.0, 0.0, 0.2326, -0.1163, -0.1163], [0.0, -0.0465, -0.0116, -0.1163, 0.2326, -0.0581], [-0.0581, 0.0, 0.0, -0.1163, -0.0581, 0.2326]])
```

### Step 9: Assign L = nx.directed_combinatorial_laplacian_matrix(...)

```python
L = nx.directed_combinatorial_laplacian_matrix(G, alpha=0.9, nodelist=sorted(G), walk_type='random')
```

### Step 10: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(L, GL, decimal=3)
```

### Step 11: Assign GL = np.array(...)

```python
GL = np.array([[0.0698, -0.0174, -0.0233, 0.0, 0.0, -0.0291], [-0.0174, 0.0465, -0.0058, 0.0, -0.0233, 0.0], [-0.0233, -0.0058, 0.0349, 0.0, -0.0058, 0.0], [0.0, 0.0, 0.0, 0.1163, -0.0581, -0.0581], [0.0, -0.0233, -0.0058, -0.0581, 0.1163, -0.0291], [-0.0291, 0.0, 0.0, -0.0581, -0.0291, 0.1163]])
```

### Step 12: Assign L = nx.directed_combinatorial_laplacian_matrix(...)

```python
L = nx.directed_combinatorial_laplacian_matrix(G, alpha=0.9, nodelist=sorted(G), walk_type='lazy')
```

### Step 13: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(L, GL, decimal=3)
```

### Step 14: Assign E = nx.DiGraph(...)

```python
E = nx.DiGraph(nx.margulis_gabber_galil_graph(2))
```

### Step 15: Assign L = nx.directed_combinatorial_laplacian_matrix(...)

```python
L = nx.directed_combinatorial_laplacian_matrix(E)
```

### Step 16: Assign expected = np.array(...)

```python
expected = np.array([[0.16666667, -0.08333333, -0.08333333, 0.0], [-0.08333333, 0.16666667, 0.0, -0.08333333], [-0.08333333, 0.0, 0.16666667, -0.08333333], [0.0, -0.08333333, -0.08333333, 0.16666667]])
```

### Step 17: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(L, expected, decimal=6)
```

### Step 18: Call nx.directed_combinatorial_laplacian_matrix()

```python
nx.directed_combinatorial_laplacian_matrix(G, walk_type='pagerank', alpha=100)
```

### Step 19: Call nx.directed_combinatorial_laplacian_matrix()

```python
nx.directed_combinatorial_laplacian_matrix(G, walk_type='silly')
```


## Complete Example

```python
# Workflow
'Directed combinatorial Laplacian'
G = nx.DiGraph()
G.add_edges_from(((1, 2), (1, 3), (3, 1), (3, 2), (3, 5), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4)))
GL = np.array([[0.0366, -0.0132, -0.0153, -0.0034, -0.002, -0.0027], [-0.0132, 0.045, -0.0111, -0.0076, -0.0062, -0.0069], [-0.0153, -0.0111, 0.0408, -0.0035, -0.0083, -0.0027], [-0.0034, -0.0076, -0.0035, 0.3688, -0.1356, -0.2187], [-0.002, -0.0062, -0.0083, -0.1356, 0.2026, -0.0505], [-0.0027, -0.0069, -0.0027, -0.2187, -0.0505, 0.2815]])
L = nx.directed_combinatorial_laplacian_matrix(G, alpha=0.9, nodelist=sorted(G))
np.testing.assert_almost_equal(L, GL, decimal=3)
G.add_edges_from(((2, 5), (6, 1)))
GL = np.array([[0.1395, -0.0349, -0.0465, 0.0, 0.0, -0.0581], [-0.0349, 0.093, -0.0116, 0.0, -0.0465, 0.0], [-0.0465, -0.0116, 0.0698, 0.0, -0.0116, 0.0], [0.0, 0.0, 0.0, 0.2326, -0.1163, -0.1163], [0.0, -0.0465, -0.0116, -0.1163, 0.2326, -0.0581], [-0.0581, 0.0, 0.0, -0.1163, -0.0581, 0.2326]])
L = nx.directed_combinatorial_laplacian_matrix(G, alpha=0.9, nodelist=sorted(G), walk_type='random')
np.testing.assert_almost_equal(L, GL, decimal=3)
GL = np.array([[0.0698, -0.0174, -0.0233, 0.0, 0.0, -0.0291], [-0.0174, 0.0465, -0.0058, 0.0, -0.0233, 0.0], [-0.0233, -0.0058, 0.0349, 0.0, -0.0058, 0.0], [0.0, 0.0, 0.0, 0.1163, -0.0581, -0.0581], [0.0, -0.0233, -0.0058, -0.0581, 0.1163, -0.0291], [-0.0291, 0.0, 0.0, -0.0581, -0.0291, 0.1163]])
L = nx.directed_combinatorial_laplacian_matrix(G, alpha=0.9, nodelist=sorted(G), walk_type='lazy')
np.testing.assert_almost_equal(L, GL, decimal=3)
E = nx.DiGraph(nx.margulis_gabber_galil_graph(2))
L = nx.directed_combinatorial_laplacian_matrix(E)
expected = np.array([[0.16666667, -0.08333333, -0.08333333, 0.0], [-0.08333333, 0.16666667, 0.0, -0.08333333], [-0.08333333, 0.0, 0.16666667, -0.08333333], [0.0, -0.08333333, -0.08333333, 0.16666667]])
np.testing.assert_almost_equal(L, expected, decimal=6)
with pytest.raises(nx.NetworkXError):
    nx.directed_combinatorial_laplacian_matrix(G, walk_type='pagerank', alpha=100)
with pytest.raises(nx.NetworkXError):
    nx.directed_combinatorial_laplacian_matrix(G, walk_type='silly')
```

## Next Steps


---

*Source: test_laplacian.py:256 | Complexity: Advanced | Last updated: 2026-06-02*