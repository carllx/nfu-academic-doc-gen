# How To: Max Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test max level

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
assert partition == expected
```

### Step 2: Assign parts_iter = nx.community.leiden_partitions(...)

```python
parts_iter = nx.community.leiden_partitions(G, seed=42)
```

**Verification:**
```python
assert max_level > 1
```

### Step 3: Assign partition = nx.community.leiden_communities(...)

```python
partition = nx.community.leiden_communities(G, max_level=max_level + 1, seed=42)
```

**Verification:**
```python
assert partition == expected
```

### Step 4: Assign partition = nx.community.leiden_communities(...)

```python
partition = nx.community.leiden_communities(G, max_level=max_level, seed=42)
```

**Verification:**
```python
assert partition == expected
```

### Step 5: Call nx.community.leiden_communities()

```python
nx.community.leiden_communities(G, max_level=0)
```


## Complete Example

```python
# Workflow
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
parts_iter = nx.community.leiden_partitions(G, seed=42)
for max_level, expected in enumerate(parts_iter, 1):
    partition = nx.community.leiden_communities(G, max_level=max_level, seed=42)
    assert partition == expected
assert max_level > 1
partition = nx.community.leiden_communities(G, max_level=max_level + 1, seed=42)
assert partition == expected
with pytest.raises(ValueError, match='max_level argument must be a positive integer'):
    nx.community.leiden_communities(G, max_level=0)
```

## Next Steps


---

*Source: test_leiden.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*