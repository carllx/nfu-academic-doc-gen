# How To: Tarjan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tarjan

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

### Step 1: Assign G = tarjan_bridge_graph(...)

```python
G = tarjan_bridge_graph()
```

**Verification:**
```python
assert len(aug_edges) == 3
```

### Step 2: Assign aug_edges = set(...)

```python
aug_edges = set(_augment_and_check(G, k=2)[0])
```

**Verification:**
```python
assert len(aug_edges) <= 3 * 2
```

### Step 3: Call print()

```python
print(f'aug_edges = {aug_edges!r}')
```

**Verification:**
```python
assert len(aug_edges) == 3
```

### Step 4: Assign avail = value

```python
avail = [(9, 7), (8, 5), (2, 10), (6, 13), (11, 18), (1, 17), (2, 3), (16, 17), (18, 14), (15, 14)]
```

### Step 5: Assign aug_edges = set(...)

```python
aug_edges = set(_augment_and_check(G, avail=avail, k=2)[0])
```

**Verification:**
```python
assert len(aug_edges) <= 3 * 2
```

### Step 6: Call _check_augmentations()

```python
_check_augmentations(G, avail)
```


## Complete Example

```python
# Workflow
G = tarjan_bridge_graph()
aug_edges = set(_augment_and_check(G, k=2)[0])
print(f'aug_edges = {aug_edges!r}')
assert len(aug_edges) == 3
avail = [(9, 7), (8, 5), (2, 10), (6, 13), (11, 18), (1, 17), (2, 3), (16, 17), (18, 14), (15, 14)]
aug_edges = set(_augment_and_check(G, avail=avail, k=2)[0])
assert len(aug_edges) <= 3 * 2
_check_augmentations(G, avail)
```

## Next Steps


---

*Source: test_edge_augmentation.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*