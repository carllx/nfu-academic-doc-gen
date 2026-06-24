# How To: Node Input

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test node input

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.grid_2d_graph(...)

```python
G = nx.grid_2d_graph(4, 2, periodic=True)
```

**Verification:**
```python
assert nx.is_isomorphic(H, G)
```

### Step 2: Assign H = nx.grid_2d_graph(...)

```python
H = nx.grid_2d_graph(range(4), range(2), periodic=True)
```

**Verification:**
```python
assert nx.is_isomorphic(H, G)
```

### Step 3: Assign H = nx.grid_2d_graph(...)

```python
H = nx.grid_2d_graph('abcd', 'ef', periodic=True)
```

**Verification:**
```python
assert edges_equal(H, G)
```

### Step 4: Assign G = nx.grid_2d_graph(...)

```python
G = nx.grid_2d_graph(5, 6)
```

### Step 5: Assign H = nx.grid_2d_graph(...)

```python
H = nx.grid_2d_graph(range(5), range(6))
```

**Verification:**
```python
assert edges_equal(H, G)
```


## Complete Example

```python
# Workflow
G = nx.grid_2d_graph(4, 2, periodic=True)
H = nx.grid_2d_graph(range(4), range(2), periodic=True)
assert nx.is_isomorphic(H, G)
H = nx.grid_2d_graph('abcd', 'ef', periodic=True)
assert nx.is_isomorphic(H, G)
G = nx.grid_2d_graph(5, 6)
H = nx.grid_2d_graph(range(5), range(6))
assert edges_equal(H, G)
```

## Next Steps


---

*Source: test_lattice.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*