# How To: Undirected Selfloops

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test undirected selfloops

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

**Verification:**
```python
assert expected_partition == part
```

### Step 2: Assign expected_partition = nx.community.louvain_communities(...)

```python
expected_partition = nx.community.louvain_communities(G, seed=2, weight=None)
```

**Verification:**
```python
assert part != partition
```

### Step 3: Assign part = value

```python
part = [{0, 1, 2, 3, 7, 9, 11, 12, 13, 17, 19, 21}, {16, 4, 5, 6, 10}, {23, 25, 27, 28, 24, 31}, {32, 33, 8, 14, 15, 18, 20, 22, 26, 29, 30}]
```

**Verification:**
```python
assert part == partition
```

### Step 4: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(i, i, i * 1000) for i in range(9)])
```

### Step 5: Assign partition = nx.community.louvain_communities(...)

```python
partition = nx.community.louvain_communities(G, seed=2, weight='weight')
```

**Verification:**
```python
assert part != partition
```

### Step 6: Assign partition = nx.community.louvain_communities(...)

```python
partition = nx.community.louvain_communities(G, seed=2, weight=None)
```

**Verification:**
```python
assert part == partition
```


## Complete Example

```python
# Workflow
G = nx.karate_club_graph()
expected_partition = nx.community.louvain_communities(G, seed=2, weight=None)
part = [{0, 1, 2, 3, 7, 9, 11, 12, 13, 17, 19, 21}, {16, 4, 5, 6, 10}, {23, 25, 27, 28, 24, 31}, {32, 33, 8, 14, 15, 18, 20, 22, 26, 29, 30}]
assert expected_partition == part
G.add_weighted_edges_from([(i, i, i * 1000) for i in range(9)])
partition = nx.community.louvain_communities(G, seed=2, weight='weight')
assert part != partition
partition = nx.community.louvain_communities(G, seed=2, weight=None)
assert part == partition
```

## Next Steps


---

*Source: test_louvain.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*