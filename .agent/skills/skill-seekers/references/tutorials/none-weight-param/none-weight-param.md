# How To: None Weight Param

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test none weight param

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

**Verification:**
```python
assert partition1 != partition2
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {edge: i * i for i, edge in enumerate(G.edges)}, name='foo')
```

**Verification:**
```python
assert partition2 != partition3
```

### Step 3: Assign partition1 = nx.community.leiden_communities(...)

```python
partition1 = nx.community.leiden_communities(G, weight=None, seed=2)
```

### Step 4: Assign partition2 = nx.community.leiden_communities(...)

```python
partition2 = nx.community.leiden_communities(G, weight='foo', seed=2)
```

### Step 5: Assign partition3 = nx.community.leiden_communities(...)

```python
partition3 = nx.community.leiden_communities(G, weight='weight', seed=2)
```

**Verification:**
```python
assert partition1 != partition2
```


## Complete Example

```python
# Workflow
G = nx.karate_club_graph()
nx.set_edge_attributes(G, {edge: i * i for i, edge in enumerate(G.edges)}, name='foo')
partition1 = nx.community.leiden_communities(G, weight=None, seed=2)
partition2 = nx.community.leiden_communities(G, weight='foo', seed=2)
partition3 = nx.community.leiden_communities(G, weight='weight', seed=2)
assert partition1 != partition2
assert partition2 != partition3
```

## Next Steps


---

*Source: test_leiden.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*