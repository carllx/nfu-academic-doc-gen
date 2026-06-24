# How To: All Pairs Dijkstra

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs dijkstra

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: Assign cycle = nx.cycle_graph(...)

```python
cycle = nx.cycle_graph(7)
```

**Verification:**
```python
assert out[0][0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

### Step 2: Assign out = dict(...)

```python
out = dict(nx.all_pairs_dijkstra(cycle))
```

**Verification:**
```python
assert out[0][1][3] == [0, 1, 2, 3]
```

### Step 3: Assign unknown = 10

```python
cycle[1][2]['weight'] = 10
```

**Verification:**
```python
assert out[0][0] == {0: 0, 1: 1, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
```

### Step 4: Assign out = dict(...)

```python
out = dict(nx.all_pairs_dijkstra(cycle))
```

**Verification:**
```python
assert out[0][1][3] == [0, 6, 5, 4, 3]
```


## Complete Example

```python
# Workflow
cycle = nx.cycle_graph(7)
out = dict(nx.all_pairs_dijkstra(cycle))
assert out[0][0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert out[0][1][3] == [0, 1, 2, 3]
cycle[1][2]['weight'] = 10
out = dict(nx.all_pairs_dijkstra(cycle))
assert out[0][0] == {0: 0, 1: 1, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
assert out[0][1][3] == [0, 6, 5, 4, 3]
```

## Next Steps


---

*Source: test_weighted.py:406 | Complexity: Intermediate | Last updated: 2026-06-02*