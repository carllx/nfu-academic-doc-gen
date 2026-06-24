# How To: Minimum Weight Full Matching Incomplete Graph

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test minimum weight full matching incomplete graph

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

**Verification:**
```python
assert matching == {1: 4, 2: 3, 4: 1, 3: 2}
```

### Step 2: Call B.add_nodes_from()

```python
B.add_nodes_from([1, 2], bipartite=0)
```

### Step 3: Call B.add_nodes_from()

```python
B.add_nodes_from([3, 4], bipartite=1)
```

### Step 4: Call B.add_edge()

```python
B.add_edge(1, 4, weight=100)
```

### Step 5: Call B.add_edge()

```python
B.add_edge(2, 3, weight=100)
```

### Step 6: Call B.add_edge()

```python
B.add_edge(2, 4, weight=50)
```

### Step 7: Assign matching = minimum_weight_full_matching(...)

```python
matching = minimum_weight_full_matching(B)
```

**Verification:**
```python
assert matching == {1: 4, 2: 3, 4: 1, 3: 2}
```


## Complete Example

```python
# Workflow
B = nx.Graph()
B.add_nodes_from([1, 2], bipartite=0)
B.add_nodes_from([3, 4], bipartite=1)
B.add_edge(1, 4, weight=100)
B.add_edge(2, 3, weight=100)
B.add_edge(2, 4, weight=50)
matching = minimum_weight_full_matching(B)
assert matching == {1: 4, 2: 3, 4: 1, 3: 2}
```

## Next Steps


---

*Source: test_matching.py:224 | Complexity: Intermediate | Last updated: 2026-06-02*