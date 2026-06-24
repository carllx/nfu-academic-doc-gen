# How To: Multigraph Unweighted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the Voronoi cells for a multigraph are the same as
for a simple graph.

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests that the Voronoi cells for a multigraph are the same as\n        for a simple graph.\n\n        '

```python
'Tests that the Voronoi cells for a multigraph are the same as\n        for a simple graph.\n\n        '
```

**Verification:**
```python
assert G_cells == H_cells
```

### Step 2: Assign edges = value

```python
edges = [(0, 1), (1, 2), (2, 3)]
```

### Step 3: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph(2 * edges)
```

### Step 4: Assign H = nx.Graph(...)

```python
H = nx.Graph(G)
```

### Step 5: Assign G_cells = nx.voronoi_cells(...)

```python
G_cells = nx.voronoi_cells(G, {0, 3})
```

### Step 6: Assign H_cells = nx.voronoi_cells(...)

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
'Tests that the Voronoi cells for a multigraph are the same as\n        for a simple graph.\n\n        '
edges = [(0, 1), (1, 2), (2, 3)]
G = nx.MultiGraph(2 * edges)
H = nx.Graph(G)
G_cells = nx.voronoi_cells(G, {0, 3})
H_cells = nx.voronoi_cells(H, {0, 3})
assert G_cells == H_cells
```

## Next Steps


---

*Source: test_voronoi.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*