# How To: Navigable Small World

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test navigable small world

## Prerequisites

**Required Modules:**
- `math`
- `random`
- `itertools`
- `pytest`
- `networkx`
- `string`
- `string`
- `string`


## Step-by-Step Guide

### Step 1: Assign G = nx.navigable_small_world_graph(...)

```python
G = nx.navigable_small_world_graph(5, p=1, q=0, seed=42)
```

**Verification:**
```python
assert nx.is_isomorphic(G, gg)
```

### Step 2: Assign gg = nx.grid_2d_graph.to_directed(...)

```python
gg = nx.grid_2d_graph(5, 5).to_directed()
```

**Verification:**
```python
assert nx.is_isomorphic(G, gg)
```

### Step 3: Assign G = nx.navigable_small_world_graph(...)

```python
G = nx.navigable_small_world_graph(5, p=1, q=0, dim=3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, gg)
```

### Step 4: Assign gg = nx.grid_graph.to_directed(...)

```python
gg = nx.grid_graph([5, 5, 5]).to_directed()
```

**Verification:**
```python
assert nx.is_isomorphic(G, gg)
```

### Step 5: Assign G = nx.navigable_small_world_graph(...)

```python
G = nx.navigable_small_world_graph(5, p=1, q=0, dim=1)
```

### Step 6: Assign gg = nx.grid_graph.to_directed(...)

```python
gg = nx.grid_graph([5]).to_directed()
```

**Verification:**
```python
assert nx.is_isomorphic(G, gg)
```


## Complete Example

```python
# Workflow
G = nx.navigable_small_world_graph(5, p=1, q=0, seed=42)
gg = nx.grid_2d_graph(5, 5).to_directed()
assert nx.is_isomorphic(G, gg)
G = nx.navigable_small_world_graph(5, p=1, q=0, dim=3)
gg = nx.grid_graph([5, 5, 5]).to_directed()
assert nx.is_isomorphic(G, gg)
G = nx.navigable_small_world_graph(5, p=1, q=0, dim=1)
gg = nx.grid_graph([5]).to_directed()
assert nx.is_isomorphic(G, gg)
```

## Next Steps


---

*Source: test_geometric.py:239 | Complexity: Intermediate | Last updated: 2026-06-02*