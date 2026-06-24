# How To: Inter Community Edges With Digraphs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inter community edges with digraphs

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.community`
- `networkx.algorithms.community.quality`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(2, create_using=nx.DiGraph())
```

**Verification:**
```python
assert inter_community_edges(G, partition) == 2
```

### Step 2: Assign partition = value

```python
partition = [{0}, {1}]
```

**Verification:**
```python
assert inter_community_edges(G, partition) == 70
```

### Step 3: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(10, create_using=nx.DiGraph())
```

**Verification:**
```python
assert inter_community_edges(G, partition) == 2
```

### Step 4: Assign partition = value

```python
partition = [{0}, {1, 2}, {3, 4, 5}, {6, 7, 8, 9}]
```

**Verification:**
```python
assert inter_community_edges(G, partition) == 70
```

### Step 5: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4, create_using=nx.DiGraph())
```

### Step 6: Assign partition = value

```python
partition = [{0, 1}, {2, 3}]
```

**Verification:**
```python
assert inter_community_edges(G, partition) == 2
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(2, create_using=nx.DiGraph())
partition = [{0}, {1}]
assert inter_community_edges(G, partition) == 2
G = nx.complete_graph(10, create_using=nx.DiGraph())
partition = [{0}, {1, 2}, {3, 4, 5}, {6, 7, 8, 9}]
assert inter_community_edges(G, partition) == 70
G = nx.cycle_graph(4, create_using=nx.DiGraph())
partition = [{0, 1}, {2, 3}]
assert inter_community_edges(G, partition) == 2
```

## Next Steps


---

*Source: test_quality.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*