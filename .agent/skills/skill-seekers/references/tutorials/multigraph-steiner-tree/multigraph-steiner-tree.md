# How To: Multigraph Steiner Tree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multigraph steiner tree

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.approximation.steinertree`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert edges_equal(S.edges(data=True, keys=True), expected_edges)
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2, 0, {'weight': 1}), (2, 3, 0, {'weight': 999}), (2, 3, 1, {'weight': 1}), (3, 4, 0, {'weight': 1}), (3, 5, 0, {'weight': 1})])
```

### Step 3: Assign terminal_nodes = value

```python
terminal_nodes = [2, 4, 5]
```

### Step 4: Assign expected_edges = value

```python
expected_edges = [(2, 3, 1, {'weight': 1}), (3, 4, 0, {'weight': 1}), (3, 5, 0, {'weight': 1})]
```

### Step 5: Assign S = steiner_tree(...)

```python
S = steiner_tree(G, terminal_nodes, method=method)
```

**Verification:**
```python
assert edges_equal(S.edges(data=True, keys=True), expected_edges)
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
G = nx.MultiGraph()
G.add_edges_from([(1, 2, 0, {'weight': 1}), (2, 3, 0, {'weight': 999}), (2, 3, 1, {'weight': 1}), (3, 4, 0, {'weight': 1}), (3, 5, 0, {'weight': 1})])
terminal_nodes = [2, 4, 5]
expected_edges = [(2, 3, 1, {'weight': 1}), (3, 4, 0, {'weight': 1}), (3, 5, 0, {'weight': 1})]
S = steiner_tree(G, terminal_nodes, method=method)
assert edges_equal(S.edges(data=True, keys=True), expected_edges)
```

## Next Steps


---

*Source: test_steinertree.py:191 | Complexity: Intermediate | Last updated: 2026-06-02*