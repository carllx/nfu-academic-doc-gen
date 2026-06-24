# How To: Incidence Matrix Simple

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test incidence matrix simple

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.exception`


## Step-by-Step Guide

### Step 1: Assign deg = value

```python
deg = [3, 2, 2, 1, 0]
```

### Step 2: Assign G = nx.havel_hakimi_graph(...)

```python
G = nx.havel_hakimi_graph(deg)
```

### Step 3: Assign deg = value

```python
deg = [(1, 0), (1, 0), (1, 0), (2, 0), (1, 0), (2, 1), (0, 1), (0, 1)]
```

### Step 4: Assign MG = nx.random_clustered_graph(...)

```python
MG = nx.random_clustered_graph(deg, seed=42)
```

### Step 5: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(G, dtype=int).todense()
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([[1, 1, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]])
```

### Step 7: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, expected)
```

### Step 8: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(MG, dtype=int).todense()
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 1]])
```

### Step 10: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, expected)
```

### Step 11: Call nx.incidence_matrix()

```python
nx.incidence_matrix(G, nodelist=[0, 1])
```


## Complete Example

```python
# Workflow
deg = [3, 2, 2, 1, 0]
G = nx.havel_hakimi_graph(deg)
deg = [(1, 0), (1, 0), (1, 0), (2, 0), (1, 0), (2, 1), (0, 1), (0, 1)]
MG = nx.random_clustered_graph(deg, seed=42)
I = nx.incidence_matrix(G, dtype=int).todense()
expected = np.array([[1, 1, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]])
np.testing.assert_equal(I, expected)
I = nx.incidence_matrix(MG, dtype=int).todense()
expected = np.array([[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 1]])
np.testing.assert_equal(I, expected)
with pytest.raises(NetworkXError):
    nx.incidence_matrix(G, nodelist=[0, 1])
```

## Next Steps


---

*Source: test_graphmatrix.py:10 | Complexity: Advanced | Last updated: 2026-06-02*