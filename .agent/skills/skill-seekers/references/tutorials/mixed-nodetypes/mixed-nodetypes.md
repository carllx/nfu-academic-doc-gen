# How To: Mixed Nodetypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed nodetypes

## Prerequisites

**Required Modules:**
- `math`
- `operator`
- `pytest`
- `networkx`
- `networkx.algorithms.tree`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Assign edgelist = value

```python
edgelist = [(0, 3, [('weight', 5)]), (0, '1', [('weight', 5)])]
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(edgelist)
```

### Step 4: Assign G = G.to_directed(...)

```python
G = G.to_directed()
```

### Step 5: Assign x = branchings.minimum_spanning_arborescence(...)

```python
x = branchings.minimum_spanning_arborescence(G)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
edgelist = [(0, 3, [('weight', 5)]), (0, '1', [('weight', 5)])]
G.add_edges_from(edgelist)
G = G.to_directed()
x = branchings.minimum_spanning_arborescence(G)
```

## Next Steps


---

*Source: test_branchings.py:410 | Complexity: Intermediate | Last updated: 2026-06-02*