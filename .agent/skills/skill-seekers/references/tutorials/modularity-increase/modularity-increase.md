# How To: Modularity Increase

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test modularity increase

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
assert nx.community.modularity(G, partition) > mod
```

### Step 2: Assign partition = value

```python
partition = [{u} for u in G.nodes()]
```

### Step 3: Assign mod = nx.community.modularity(...)

```python
mod = nx.community.modularity(G, partition)
```

### Step 4: Assign partition = nx.community.leiden_communities(...)

```python
partition = nx.community.leiden_communities(G)
```

**Verification:**
```python
assert nx.community.modularity(G, partition) > mod
```


## Complete Example

```python
# Workflow
G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.009, average_degree=5, min_community=20, seed=10)
partition = [{u} for u in G.nodes()]
mod = nx.community.modularity(G, partition)
partition = nx.community.leiden_communities(G)
assert nx.community.modularity(G, partition) > mod
```

## Next Steps


---

*Source: test_leiden.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*