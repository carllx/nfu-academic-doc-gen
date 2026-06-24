# How To: All Pairs Dijkstra Path

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs dijkstra path

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
assert p[0][3] == [0, 1, 2, 3]
```

### Step 2: Assign p = dict(...)

```python
p = dict(nx.all_pairs_dijkstra_path(cycle))
```

**Verification:**
```python
assert p[0][3] == [0, 6, 5, 4, 3]
```

### Step 3: Assign unknown = 10

```python
cycle[1][2]['weight'] = 10
```

### Step 4: Assign p = dict(...)

```python
p = dict(nx.all_pairs_dijkstra_path(cycle))
```

**Verification:**
```python
assert p[0][3] == [0, 6, 5, 4, 3]
```


## Complete Example

```python
# Workflow
cycle = nx.cycle_graph(7)
p = dict(nx.all_pairs_dijkstra_path(cycle))
assert p[0][3] == [0, 1, 2, 3]
cycle[1][2]['weight'] = 10
p = dict(nx.all_pairs_dijkstra_path(cycle))
assert p[0][3] == [0, 6, 5, 4, 3]
```

## Next Steps


---

*Source: test_weighted.py:388 | Complexity: Intermediate | Last updated: 2026-06-02*