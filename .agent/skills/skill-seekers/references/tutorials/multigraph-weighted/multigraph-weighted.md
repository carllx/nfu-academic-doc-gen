# How To: Multigraph Weighted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multigraph weighted

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(0, 1, 10), (0, 1, 10), (1, 2, 1), (1, 2, 100), (2, 3, 1), (2, 3, 100)]
```

**Verification:**
```python
assert expected == cells
```

### Step 2: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

### Step 3: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from(edges)
```

### Step 4: Assign cells = nx.voronoi_cells(...)

```python
cells = nx.voronoi_cells(G, {0, 3})
```

### Step 5: Assign expected = value

```python
expected = {0: {0}, 3: {1, 2, 3}}
```

**Verification:**
```python
assert expected == cells
```


## Complete Example

```python
# Workflow
edges = [(0, 1, 10), (0, 1, 10), (1, 2, 1), (1, 2, 100), (2, 3, 1), (2, 3, 100)]
G = nx.MultiGraph()
G.add_weighted_edges_from(edges)
cells = nx.voronoi_cells(G, {0, 3})
expected = {0: {0}, 3: {1, 2, 3}}
assert expected == cells
```

## Next Steps


---

*Source: test_voronoi.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*