# How To: Directed Partition

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test 2 cases that were looping infinitely
from issues #5175 and #5704

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    Test 2 cases that were looping infinitely\n    from issues #5175 and #5704\n    '

```python
'\n    Test 2 cases that were looping infinitely\n    from issues #5175 and #5704\n    '
```

**Verification:**
```python
assert G_partition == G_expected_partition
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert H_partition == H_expected_partition
```

### Step 3: Assign H = nx.DiGraph(...)

```python
H = nx.DiGraph()
```

### Step 4: Call G.add_nodes_from()

```python
G.add_nodes_from(range(10))
```

### Step 5: Call H.add_nodes_from()

```python
H.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
```

### Step 6: Assign G_edges = value

```python
G_edges = [(0, 2), (0, 1), (1, 0), (2, 1), (2, 0), (3, 4), (4, 3), (7, 8), (8, 7), (9, 10), (10, 9)]
```

### Step 7: Assign H_edges = value

```python
H_edges = [(1, 2), (1, 6), (1, 9), (2, 3), (2, 4), (2, 5), (3, 4), (4, 3), (4, 5), (5, 4), (6, 7), (6, 8), (9, 10), (9, 11), (10, 11), (11, 10)]
```

### Step 8: Call G.add_edges_from()

```python
G.add_edges_from(G_edges)
```

### Step 9: Call H.add_edges_from()

```python
H.add_edges_from(H_edges)
```

### Step 10: Assign G_expected_partition = value

```python
G_expected_partition = [{0, 1, 2}, {3, 4}, {5}, {6}, {8, 7}, {9, 10}]
```

### Step 11: Assign G_partition = nx.community.louvain_communities(...)

```python
G_partition = nx.community.louvain_communities(G, seed=123, weight=None)
```

### Step 12: Assign H_expected_partition = value

```python
H_expected_partition = [{2, 3, 4, 5}, {8, 1, 6, 7}, {9, 10, 11}]
```

### Step 13: Assign H_partition = nx.community.louvain_communities(...)

```python
H_partition = nx.community.louvain_communities(H, seed=123, weight=None)
```

**Verification:**
```python
assert G_partition == G_expected_partition
```


## Complete Example

```python
# Workflow
'\n    Test 2 cases that were looping infinitely\n    from issues #5175 and #5704\n    '
G = nx.DiGraph()
H = nx.DiGraph()
G.add_nodes_from(range(10))
H.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
G_edges = [(0, 2), (0, 1), (1, 0), (2, 1), (2, 0), (3, 4), (4, 3), (7, 8), (8, 7), (9, 10), (10, 9)]
H_edges = [(1, 2), (1, 6), (1, 9), (2, 3), (2, 4), (2, 5), (3, 4), (4, 3), (4, 5), (5, 4), (6, 7), (6, 8), (9, 10), (9, 11), (10, 11), (11, 10)]
G.add_edges_from(G_edges)
H.add_edges_from(H_edges)
G_expected_partition = [{0, 1, 2}, {3, 4}, {5}, {6}, {8, 7}, {9, 10}]
G_partition = nx.community.louvain_communities(G, seed=123, weight=None)
H_expected_partition = [{2, 3, 4, 5}, {8, 1, 6, 7}, {9, 10, 11}]
H_partition = nx.community.louvain_communities(H, seed=123, weight=None)
assert G_partition == G_expected_partition
assert H_partition == H_expected_partition
```

## Next Steps


---

*Source: test_louvain.py:104 | Complexity: Advanced | Last updated: 2026-06-02*