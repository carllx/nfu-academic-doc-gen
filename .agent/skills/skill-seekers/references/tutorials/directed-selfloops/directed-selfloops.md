# How To: Directed Selfloops

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed selfloops

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert G_partition != G_expected_partition
```

### Step 2: Call G.add_nodes_from()

```python
G.add_nodes_from(range(11))
```

**Verification:**
```python
assert G_partition == G_expected_partition
```

### Step 3: Assign G_edges = value

```python
G_edges = [(0, 2), (0, 1), (1, 0), (2, 1), (2, 0), (3, 4), (4, 3), (7, 8), (8, 7), (9, 10), (10, 9)]
```

### Step 4: Call G.add_edges_from()

```python
G.add_edges_from(G_edges)
```

### Step 5: Assign G_expected_partition = nx.community.louvain_communities(...)

```python
G_expected_partition = nx.community.louvain_communities(G, seed=123, weight=None)
```

### Step 6: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(i, i, i * 1000) for i in range(3)])
```

### Step 7: Assign G_partition = nx.community.louvain_communities(...)

```python
G_partition = nx.community.louvain_communities(G, seed=123, weight='weight')
```

**Verification:**
```python
assert G_partition != G_expected_partition
```

### Step 8: Assign G_partition = nx.community.louvain_communities(...)

```python
G_partition = nx.community.louvain_communities(G, seed=123, weight=None)
```

**Verification:**
```python
assert G_partition == G_expected_partition
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_nodes_from(range(11))
G_edges = [(0, 2), (0, 1), (1, 0), (2, 1), (2, 0), (3, 4), (4, 3), (7, 8), (8, 7), (9, 10), (10, 9)]
G.add_edges_from(G_edges)
G_expected_partition = nx.community.louvain_communities(G, seed=123, weight=None)
G.add_weighted_edges_from([(i, i, i * 1000) for i in range(3)])
G_partition = nx.community.louvain_communities(G, seed=123, weight='weight')
assert G_partition != G_expected_partition
G_partition = nx.community.louvain_communities(G, seed=123, weight=None)
assert G_partition == G_expected_partition
```

## Next Steps


---

*Source: test_louvain.py:75 | Complexity: Advanced | Last updated: 2026-06-02*