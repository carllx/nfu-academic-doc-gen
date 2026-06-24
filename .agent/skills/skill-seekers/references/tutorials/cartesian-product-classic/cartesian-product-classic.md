# How To: Cartesian Product Classic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cartesian product classic

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign P2 = nx.path_graph(...)

```python
P2 = nx.path_graph(2)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cubical_graph())
```

### Step 2: Assign P3 = nx.path_graph(...)

```python
P3 = nx.path_graph(3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.grid_2d_graph(3, 3))
```

### Step 3: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(P2, P2)
```

### Step 4: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(P2, G)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cubical_graph())
```

### Step 5: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(P3, P3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.grid_2d_graph(3, 3))
```


## Complete Example

```python
# Workflow
P2 = nx.path_graph(2)
P3 = nx.path_graph(3)
G = nx.cartesian_product(P2, P2)
G = nx.cartesian_product(P2, G)
assert nx.is_isomorphic(G, nx.cubical_graph())
G = nx.cartesian_product(P3, P3)
assert nx.is_isomorphic(G, nx.grid_2d_graph(3, 3))
```

## Next Steps


---

*Source: test_product.py:180 | Complexity: Intermediate | Last updated: 2026-06-02*