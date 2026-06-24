# How To: Weight Key

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weight key

## Prerequisites

**Required Modules:**
- `itertools`
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.connectivity`
- `networkx.algorithms.connectivity.edge_augmentation`
- `networkx.utils`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Call G.add_nodes_from()

```python
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(3, 8), (1, 2), (2, 3)])
```

### Step 4: Assign impossible = value

```python
impossible = {(3, 6), (3, 9)}
```

### Step 5: Assign rng = random.Random(...)

```python
rng = random.Random(0)
```

### Step 6: Assign avail_uv = list(...)

```python
avail_uv = list(set(complement_edges(G)) - impossible)
```

### Step 7: Assign avail = value

```python
avail = [(u, v, {'cost': rng.random()}) for u, v in avail_uv]
```

### Step 8: Call _augment_and_check()

```python
_augment_and_check(G, k=1)
```

### Step 9: Call _augment_and_check()

```python
_augment_and_check(G, k=1, avail=avail_uv)
```

### Step 10: Call _augment_and_check()

```python
_augment_and_check(G, k=1, avail=avail, weight='cost')
```

### Step 11: Call _check_augmentations()

```python
_check_augmentations(G, avail, weight='cost')
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edges_from([(3, 8), (1, 2), (2, 3)])
impossible = {(3, 6), (3, 9)}
rng = random.Random(0)
avail_uv = list(set(complement_edges(G)) - impossible)
avail = [(u, v, {'cost': rng.random()}) for u, v in avail_uv]
_augment_and_check(G, k=1)
_augment_and_check(G, k=1, avail=avail_uv)
_augment_and_check(G, k=1, avail=avail, weight='cost')
_check_augmentations(G, avail, weight='cost')
```

## Next Steps


---

*Source: test_edge_augmentation.py:40 | Complexity: Advanced | Last updated: 2026-06-02*