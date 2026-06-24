# How To: Attr Matrix Multigraph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attr matrix multigraph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 1, thickness=1, weight=3)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 1, thickness=1, weight=3)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 1, thickness=1, weight=3)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(0, 2, thickness=2)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(1, 2, thickness=3)
```

### Step 7: Assign M = nx.attr_matrix(...)

```python
M = nx.attr_matrix(G, rc_order=[0, 1, 2])
```

### Step 8: Assign data = np.array(...)

```python
data = np.array([[0.0, 3.0, 1.0], [3.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
```

### Step 9: Call np.testing.assert_equal()

```python
np.testing.assert_equal(M, np.array(data))
```

### Step 10: Assign M = nx.attr_matrix(...)

```python
M = nx.attr_matrix(G, edge_attr='weight', rc_order=[0, 1, 2])
```

### Step 11: Assign data = np.array(...)

```python
data = np.array([[0.0, 9.0, 1.0], [9.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
```

### Step 12: Call np.testing.assert_equal()

```python
np.testing.assert_equal(M, np.array(data))
```

### Step 13: Assign M = nx.attr_matrix(...)

```python
M = nx.attr_matrix(G, edge_attr='thickness', rc_order=[0, 1, 2])
```

### Step 14: Assign data = np.array(...)

```python
data = np.array([[0.0, 3.0, 2.0], [3.0, 0.0, 3.0], [2.0, 3.0, 0.0]])
```

### Step 15: Call np.testing.assert_equal()

```python
np.testing.assert_equal(M, np.array(data))
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph()
G.add_edge(0, 1, thickness=1, weight=3)
G.add_edge(0, 1, thickness=1, weight=3)
G.add_edge(0, 1, thickness=1, weight=3)
G.add_edge(0, 2, thickness=2)
G.add_edge(1, 2, thickness=3)
M = nx.attr_matrix(G, rc_order=[0, 1, 2])
data = np.array([[0.0, 3.0, 1.0], [3.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
np.testing.assert_equal(M, np.array(data))
M = nx.attr_matrix(G, edge_attr='weight', rc_order=[0, 1, 2])
data = np.array([[0.0, 9.0, 1.0], [9.0, 0.0, 1.0], [1.0, 1.0, 0.0]])
np.testing.assert_equal(M, np.array(data))
M = nx.attr_matrix(G, edge_attr='thickness', rc_order=[0, 1, 2])
data = np.array([[0.0, 3.0, 2.0], [3.0, 0.0, 3.0], [2.0, 3.0, 0.0]])
np.testing.assert_equal(M, np.array(data))
```

## Next Steps


---

*Source: test_attrmatrix.py:43 | Complexity: Advanced | Last updated: 2026-06-02*