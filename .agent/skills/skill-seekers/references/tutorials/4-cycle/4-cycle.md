# How To: 4 Cycle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 4 cycle

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 0)])
```

**Verification:**
```python
assert dist == {0: 0, 1: 1, 2: 2, 3: 1}
```

### Step 2: Assign unknown = nx.single_source_bellman_ford(...)

```python
dist, path = nx.single_source_bellman_ford(G, 0)
```

**Verification:**
```python
assert path[0] == [0]
```

### Step 3: Assign unknown = nx.bellman_ford_predecessor_and_distance(...)

```python
pred, dist = nx.bellman_ford_predecessor_and_distance(G, 0)
```

**Verification:**
```python
assert path[1] == [0, 1]
```

### Step 4: Assign unknown = nx.goldberg_radzik(...)

```python
pred, dist = nx.goldberg_radzik(G, 0)
```

**Verification:**
```python
assert path[2] in [[0, 1, 2], [0, 3, 2]]
```


## Complete Example

```python
# Workflow
G = nx.Graph([(0, 1), (1, 2), (2, 3), (3, 0)])
dist, path = nx.single_source_bellman_ford(G, 0)
assert dist == {0: 0, 1: 1, 2: 2, 3: 1}
assert path[0] == [0]
assert path[1] == [0, 1]
assert path[2] in [[0, 1, 2], [0, 3, 2]]
assert path[3] == [0, 3]
pred, dist = nx.bellman_ford_predecessor_and_distance(G, 0)
assert pred[0] == []
assert pred[1] == [0]
assert pred[2] in [[1, 3], [3, 1]]
assert pred[3] == [0]
assert dist == {0: 0, 1: 1, 2: 2, 3: 1}
pred, dist = nx.goldberg_radzik(G, 0)
assert pred[0] is None
assert pred[1] == 0
assert pred[2] in [1, 3]
assert pred[3] == 0
assert dist == {0: 0, 1: 1, 2: 2, 3: 1}
```

## Next Steps


---

*Source: test_weighted.py:848 | Complexity: Intermediate | Last updated: 2026-06-02*