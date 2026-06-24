# How To: Bfs Layout Complete Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: The complete graph should result in two layers: the starting node and
a second layer containing all neighbors.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `math`

**Setup Required:**
```python
# Fixtures: n
```

## Step-by-Step Guide

### Step 1: 'The complete graph should result in two layers: the starting node and\n    a second layer containing all neighbors.'

```python
'The complete graph should result in two layers: the starting node and\n    a second layer containing all neighbors.'
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), [1, n - 1])
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(n)
```

### Step 3: Call nx.bfs_layout()

```python
nx.bfs_layout(G, start=0, store_pos_as='pos')
```

### Step 4: Assign pos = nx.get_node_attributes(...)

```python
pos = nx.get_node_attributes(G, 'pos')
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), [1, n - 1])
```


## Complete Example

```python
# Setup
# Fixtures: n

# Workflow
'The complete graph should result in two layers: the starting node and\n    a second layer containing all neighbors.'
G = nx.complete_graph(n)
nx.bfs_layout(G, start=0, store_pos_as='pos')
pos = nx.get_node_attributes(G, 'pos')
assert np.array_equal(_num_nodes_per_bfs_layer(pos), [1, n - 1])
```

## Next Steps


---

*Source: test_layout.py:529 | Complexity: Intermediate | Last updated: 2026-06-02*