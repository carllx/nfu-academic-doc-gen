# How To: Quality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test quality

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
assert quality >= 0.65
```

### Step 2: Assign H = nx.MultiGraph(...)

```python
H = nx.MultiGraph(G)
```

**Verification:**
```python
assert quality2 >= 0.65
```

### Step 3: Assign partition = nx.community.leiden_communities(...)

```python
partition = nx.community.leiden_communities(G)
```

### Step 4: Assign partition2 = nx.community.leiden_communities(...)

```python
partition2 = nx.community.leiden_communities(H)
```

### Step 5: Assign quality = value

```python
quality = nx.community.partition_quality(G, partition)[0]
```

### Step 6: Assign quality2 = value

```python
quality2 = nx.community.partition_quality(H, partition2)[0]
```

**Verification:**
```python
assert quality >= 0.65
```


## Complete Example

```python
# Workflow
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
H = nx.MultiGraph(G)
partition = nx.community.leiden_communities(G)
partition2 = nx.community.leiden_communities(H)
quality = nx.community.partition_quality(G, partition)[0]
quality2 = nx.community.partition_quality(H, partition2)[0]
assert quality >= 0.65
assert quality2 >= 0.65
```

## Next Steps


---

*Source: test_leiden.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*