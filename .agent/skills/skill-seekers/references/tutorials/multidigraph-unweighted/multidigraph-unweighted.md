# How To: Multidigraph Unweighted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multidigraph unweighted

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign edges = list(...)

```python
edges = list(pairwise(range(6), cyclic=True))
```

**Verification:**
```python
assert G_cells == H_cells
```

### Step 2: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph(2 * edges)
```

### Step 3: Assign H = nx.DiGraph(...)

```python
H = nx.DiGraph(G)
```

### Step 4: Assign G_cells = nx.voronoi_cells(...)

```python
G_cells = nx.voronoi_cells(G, {0, 3})
```

### Step 5: Assign H_cells = nx.voronoi_cells(...)

```python
H_cells = nx.voronoi_cells(H, {0, 3})
```

**Verification:**
```python
assert G_cells == H_cells
```


## Complete Example

```python
# Workflow
edges = list(pairwise(range(6), cyclic=True))
G = nx.MultiDiGraph(2 * edges)
H = nx.DiGraph(G)
G_cells = nx.voronoi_cells(G, {0, 3})
H_cells = nx.voronoi_cells(H, {0, 3})
assert G_cells == H_cells
```

## Next Steps


---

*Source: test_voronoi.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*