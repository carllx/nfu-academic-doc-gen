# How To: Grid Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: grid_graph([n,m]) is a connected simple graph with the
following properties:
number_of_nodes = n*m
degree_histogram = [0,0,4,2*(n+m)-8,(n-2)*(m-2)]

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'grid_graph([n,m]) is a connected simple graph with the\n        following properties:\n        number_of_nodes = n*m\n        degree_histogram = [0,0,4,2*(n+m)-8,(n-2)*(m-2)]\n        '

```python
'grid_graph([n,m]) is a connected simple graph with the\n        following properties:\n        number_of_nodes = n*m\n        degree_histogram = [0,0,4,2*(n+m)-8,(n-2)*(m-2)]\n        '
```

**Verification:**
```python
assert len(g) == n * m
```

### Step 2: Assign dim = value

```python
dim = [n, m]
```

**Verification:**
```python
assert nx.degree_histogram(g) == [0, 0, 4, 2 * (n + m) - 8, (n - 2) * (m - 2)]
```

### Step 3: Assign g = nx.grid_graph(...)

```python
g = nx.grid_graph(dim)
```

**Verification:**
```python
assert len(g) == n * m
```

### Step 4: Assign dim = value

```python
dim = [n, m]
```

**Verification:**
```python
assert nx.is_isomorphic(g, nx.path_graph(5))
```

### Step 5: Assign g = nx.grid_graph(...)

```python
g = nx.grid_graph(dim)
```

**Verification:**
```python
assert len(g) == n * m
```


## Complete Example

```python
# Workflow
'grid_graph([n,m]) is a connected simple graph with the\n        following properties:\n        number_of_nodes = n*m\n        degree_histogram = [0,0,4,2*(n+m)-8,(n-2)*(m-2)]\n        '
for n, m in [(3, 5), (5, 3), (4, 5), (5, 4)]:
    dim = [n, m]
    g = nx.grid_graph(dim)
    assert len(g) == n * m
    assert nx.degree_histogram(g) == [0, 0, 4, 2 * (n + m) - 8, (n - 2) * (m - 2)]
for n, m in [(1, 5), (5, 1)]:
    dim = [n, m]
    g = nx.grid_graph(dim)
    assert len(g) == n * m
    assert nx.is_isomorphic(g, nx.path_graph(5))
```

## Next Steps


---

*Source: test_lattice.py:110 | Complexity: Intermediate | Last updated: 2026-06-02*