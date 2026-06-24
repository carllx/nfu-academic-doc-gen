# How To: All Pairs Dijkstra Path Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs dijkstra path length

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
assert pl[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

### Step 2: Assign pl = dict(...)

```python
pl = dict(nx.all_pairs_dijkstra_path_length(cycle))
```

**Verification:**
```python
assert pl[0] == {0: 0, 1: 1, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
```

### Step 3: Assign unknown = 10

```python
cycle[1][2]['weight'] = 10
```

### Step 4: Assign pl = dict(...)

```python
pl = dict(nx.all_pairs_dijkstra_path_length(cycle))
```

**Verification:**
```python
assert pl[0] == {0: 0, 1: 1, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
```


## Complete Example

```python
# Workflow
cycle = nx.cycle_graph(7)
pl = dict(nx.all_pairs_dijkstra_path_length(cycle))
assert pl[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
cycle[1][2]['weight'] = 10
pl = dict(nx.all_pairs_dijkstra_path_length(cycle))
assert pl[0] == {0: 0, 1: 1, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
```

## Next Steps


---

*Source: test_weighted.py:397 | Complexity: Intermediate | Last updated: 2026-06-02*