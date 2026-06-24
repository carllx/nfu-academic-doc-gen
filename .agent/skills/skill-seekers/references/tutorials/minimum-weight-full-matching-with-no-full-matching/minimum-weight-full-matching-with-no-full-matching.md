# How To: Minimum Weight Full Matching With No Full Matching

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test minimum weight full matching with no full matching

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.bipartite.matching`


## Step-by-Step Guide

### Step 1: Assign B = nx.Graph(...)

```python
B = nx.Graph()
```

### Step 2: Call B.add_nodes_from()

```python
B.add_nodes_from([1, 2, 3], bipartite=0)
```

### Step 3: Call B.add_nodes_from()

```python
B.add_nodes_from([4, 5, 6], bipartite=1)
```

### Step 4: Call B.add_edge()

```python
B.add_edge(1, 4, weight=100)
```

### Step 5: Call B.add_edge()

```python
B.add_edge(2, 4, weight=100)
```

### Step 6: Call B.add_edge()

```python
B.add_edge(3, 4, weight=50)
```

### Step 7: Call B.add_edge()

```python
B.add_edge(3, 5, weight=50)
```

### Step 8: Call B.add_edge()

```python
B.add_edge(3, 6, weight=50)
```

### Step 9: Call minimum_weight_full_matching()

```python
minimum_weight_full_matching(B)
```


## Complete Example

```python
# Workflow
B = nx.Graph()
B.add_nodes_from([1, 2, 3], bipartite=0)
B.add_nodes_from([4, 5, 6], bipartite=1)
B.add_edge(1, 4, weight=100)
B.add_edge(2, 4, weight=100)
B.add_edge(3, 4, weight=50)
B.add_edge(3, 5, weight=50)
B.add_edge(3, 6, weight=50)
with pytest.raises(ValueError):
    minimum_weight_full_matching(B)
```

## Next Steps


---

*Source: test_matching.py:234 | Complexity: Advanced | Last updated: 2026-06-02*