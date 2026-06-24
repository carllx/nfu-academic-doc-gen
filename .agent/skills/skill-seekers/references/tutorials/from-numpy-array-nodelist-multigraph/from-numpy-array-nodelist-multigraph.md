# How To: From Numpy Array Nodelist Multigraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from numpy array nodelist multigraph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: nodes
```

## Step-by-Step Guide

### Step 1: Assign A = np.array(...)

```python
A = np.array([[0, 1, 0, 0, 0], [1, 0, 2, 0, 0], [0, 2, 0, 3, 0], [0, 0, 3, 0, 4], [0, 0, 0, 4, 0]])
```

**Verification:**
```python
assert graphs_equal(G, expected)
```

### Step 2: Assign H = nx.MultiGraph(...)

```python
H = nx.MultiGraph()
```

### Step 3: Assign expected = nx.relabel_nodes(...)

```python
expected = nx.relabel_nodes(H, mapping=dict(enumerate(nodes)), copy=True)
```

### Step 4: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(A, parallel_edges=True, create_using=nx.MultiGraph, edge_attr=None, nodelist=nodes)
```

**Verification:**
```python
assert graphs_equal(G, expected)
```

### Step 5: Call H.add_edges_from()

```python
H.add_edges_from(itertools.repeat(edge, i + 1))
```


## Complete Example

```python
# Setup
# Fixtures: nodes

# Workflow
A = np.array([[0, 1, 0, 0, 0], [1, 0, 2, 0, 0], [0, 2, 0, 3, 0], [0, 0, 3, 0, 4], [0, 0, 0, 4, 0]])
H = nx.MultiGraph()
for i, edge in enumerate(((0, 1), (1, 2), (2, 3), (3, 4))):
    H.add_edges_from(itertools.repeat(edge, i + 1))
expected = nx.relabel_nodes(H, mapping=dict(enumerate(nodes)), copy=True)
G = nx.from_numpy_array(A, parallel_edges=True, create_using=nx.MultiGraph, edge_attr=None, nodelist=nodes)
assert graphs_equal(G, expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:481 | Complexity: Intermediate | Last updated: 2026-06-02*