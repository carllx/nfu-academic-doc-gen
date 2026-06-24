# How To: Directed Inward

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that reversing the graph gives the "inward" Voronoi
partition.

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests that reversing the graph gives the "inward" Voronoi\n        partition.\n\n        '

```python
'Tests that reversing the graph gives the "inward" Voronoi\n        partition.\n\n        '
```

**Verification:**
```python
assert expected == cells
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(pairwise(range(6), cyclic=True))
```

### Step 3: Assign G = G.reverse(...)

```python
G = G.reverse(copy=False)
```

### Step 4: Assign cells = nx.voronoi_cells(...)

```python
cells = nx.voronoi_cells(G, {0, 3})
```

### Step 5: Assign expected = value

```python
expected = {0: {0, 4, 5}, 3: {1, 2, 3}}
```

**Verification:**
```python
assert expected == cells
```


## Complete Example

```python
# Workflow
'Tests that reversing the graph gives the "inward" Voronoi\n        partition.\n\n        '
G = nx.DiGraph(pairwise(range(6), cyclic=True))
G = G.reverse(copy=False)
cells = nx.voronoi_cells(G, {0, 3})
expected = {0: {0, 4, 5}, 3: {1, 2, 3}}
assert expected == cells
```

## Next Steps


---

*Source: test_voronoi.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*