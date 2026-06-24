# How To: Bfs Layout Barbell

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bfs layout barbell

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 3)
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
```

### Step 2: Assign pos = nx.bfs_layout(...)

```python
pos = nx.bfs_layout(G, start=0)
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
```

### Step 3: Assign expected_nodes_per_layer = value

```python
expected_nodes_per_layer = [1, 4, 1, 1, 1, 1, 4]
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
```

### Step 4: Assign pos = nx.bfs_layout(...)

```python
pos = nx.bfs_layout(G, start=12)
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
```

### Step 5: Assign pos = nx.bfs_layout(...)

```python
pos = nx.bfs_layout(G, start=6)
```

### Step 6: Assign expected_nodes_per_layer = value

```python
expected_nodes_per_layer = [1, 2, 2, 8]
```

**Verification:**
```python
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(5, 3)
pos = nx.bfs_layout(G, start=0)
expected_nodes_per_layer = [1, 4, 1, 1, 1, 1, 4]
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
pos = nx.bfs_layout(G, start=12)
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
pos = nx.bfs_layout(G, start=6)
expected_nodes_per_layer = [1, 2, 2, 8]
assert np.array_equal(_num_nodes_per_bfs_layer(pos), expected_nodes_per_layer)
```

## Next Steps


---

*Source: test_layout.py:538 | Complexity: Intermediate | Last updated: 2026-06-02*