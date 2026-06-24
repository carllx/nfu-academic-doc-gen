# How To: Valid Partition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test valid partition

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.LFR_benchmark_graph(...)

```python
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
```

**Verification:**
```python
assert nx.community.is_partition(G, partition)
```

### Step 2: Assign H = G.to_directed(...)

```python
H = G.to_directed()
```

**Verification:**
```python
assert nx.community.is_partition(H, partition2)
```

### Step 3: Assign partition = nx.community.louvain_communities(...)

```python
partition = nx.community.louvain_communities(G)
```

### Step 4: Assign partition2 = nx.community.louvain_communities(...)

```python
partition2 = nx.community.louvain_communities(H)
```

**Verification:**
```python
assert nx.community.is_partition(G, partition)
```


## Complete Example

```python
# Workflow
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
H = G.to_directed()
partition = nx.community.louvain_communities(G)
partition2 = nx.community.louvain_communities(H)
assert nx.community.is_partition(G, partition)
assert nx.community.is_partition(H, partition2)
```

## Next Steps


---

*Source: test_louvain.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*