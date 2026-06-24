# How To: Mst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mst

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

**Verification:**
```python
assert x.number_of_edges() == len(edges)
```

### Step 2: Assign edgelist = value

```python
edgelist = [(0, 3, [('weight', 5)]), (0, 1, [('weight', 7)]), (1, 3, [('weight', 9)]), (1, 2, [('weight', 8)]), (1, 4, [('weight', 7)]), (3, 4, [('weight', 15)]), (3, 5, [('weight', 6)]), (2, 4, [('weight', 5)]), (4, 5, [('weight', 8)]), (4, 6, [('weight', 9)]), (5, 6, [('weight', 11)])]
```

**Verification:**
```python
assert ({u, v}, d['weight']) in edges
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

### Step 6: Assign edges = value

```python
edges = [({0, 1}, 7), ({0, 3}, 5), ({3, 5}, 6), ({1, 4}, 7), ({4, 2}, 5), ({4, 6}, 9)]
```

**Verification:**
```python
assert x.number_of_edges() == len(edges)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
edgelist = [(0, 3, [('weight', 5)]), (0, 1, [('weight', 7)]), (1, 3, [('weight', 9)]), (1, 2, [('weight', 8)]), (1, 4, [('weight', 7)]), (3, 4, [('weight', 15)]), (3, 5, [('weight', 6)]), (2, 4, [('weight', 5)]), (4, 5, [('weight', 8)]), (4, 6, [('weight', 9)]), (5, 6, [('weight', 11)])]
G.add_edges_from(edgelist)
G = G.to_directed()
x = branchings.minimum_spanning_arborescence(G)
edges = [({0, 1}, 7), ({0, 3}, 5), ({3, 5}, 6), ({1, 4}, 7), ({4, 2}, 5), ({4, 6}, 9)]
assert x.number_of_edges() == len(edges)
for u, v, d in x.edges(data=True):
    assert ({u, v}, d['weight']) in edges
```

## Next Steps


---

*Source: test_branchings.py:375 | Complexity: Intermediate | Last updated: 2026-06-02*