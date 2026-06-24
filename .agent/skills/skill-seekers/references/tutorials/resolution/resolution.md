# How To: Resolution

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resolution

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.LFR_benchmark_graph(...)

```python
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
```

**Verification:**
```python
assert len(partition1) <= len(partition2)
```

### Step 2: Assign partition1 = nx.community.leiden_communities(...)

```python
partition1 = nx.community.leiden_communities(G, resolution=0.5, seed=12)
```

**Verification:**
```python
assert len(partition2) <= len(partition3)
```

### Step 3: Assign partition2 = nx.community.leiden_communities(...)

```python
partition2 = nx.community.leiden_communities(G, seed=12)
```

### Step 4: Assign partition3 = nx.community.leiden_communities(...)

```python
partition3 = nx.community.leiden_communities(G, resolution=2, seed=12)
```

**Verification:**
```python
assert len(partition1) <= len(partition2)
```


## Complete Example

```python
# Workflow
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
partition1 = nx.community.leiden_communities(G, resolution=0.5, seed=12)
partition2 = nx.community.leiden_communities(G, seed=12)
partition3 = nx.community.leiden_communities(G, resolution=2, seed=12)
assert len(partition1) <= len(partition2)
assert len(partition2) <= len(partition3)
```

## Next Steps


---

*Source: test_leiden.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*