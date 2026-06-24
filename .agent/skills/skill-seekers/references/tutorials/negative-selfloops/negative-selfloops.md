# How To: Negative Selfloops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Negative selfloops should cause an exception if uncapacitated and
always be saturated otherwise.

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Negative selfloops should cause an exception if uncapacitated and\n        always be saturated otherwise.\n        '

```python
'Negative selfloops should cause an exception if uncapacitated and\n        always be saturated otherwise.\n        '
```

**Verification:**
```python
assert flowCost == -2
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert H == {1: {1: 2}}
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 1, weight=-1)
```

**Verification:**
```python
assert flowCost == -2
```

### Step 4: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.network_simplex, G)
```

**Verification:**
```python
assert H == {1: {1: 2}}
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.capacity_scaling, G)
```

**Verification:**
```python
assert flowCost == -2
```

### Step 6: Assign unknown = 2

```python
G[1][1]['capacity'] = 2
```

**Verification:**
```python
assert H == {1: {1: {'x': 2, 'y': 0}}}
```

### Step 7: Assign unknown = nx.network_simplex(...)

```python
flowCost, H = nx.network_simplex(G)
```

**Verification:**
```python
assert flowCost == -2
```

### Step 8: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, H = nx.capacity_scaling(G)
```

**Verification:**
```python
assert H == {1: {1: {'x': 2, 'y': 0}}}
```

### Step 9: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph()
```

### Step 10: Call G.add_edge()

```python
G.add_edge(1, 1, 'x', weight=-1)
```

### Step 11: Call G.add_edge()

```python
G.add_edge(1, 1, 'y', weight=1)
```

### Step 12: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.network_simplex, G)
```

### Step 13: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.capacity_scaling, G)
```

### Step 14: Assign unknown = 2

```python
G[1][1]['x']['capacity'] = 2
```

### Step 15: Assign unknown = nx.network_simplex(...)

```python
flowCost, H = nx.network_simplex(G)
```

**Verification:**
```python
assert flowCost == -2
```

### Step 16: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, H = nx.capacity_scaling(G)
```

**Verification:**
```python
assert flowCost == -2
```


## Complete Example

```python
# Workflow
'Negative selfloops should cause an exception if uncapacitated and\n        always be saturated otherwise.\n        '
G = nx.DiGraph()
G.add_edge(1, 1, weight=-1)
pytest.raises(nx.NetworkXUnbounded, nx.network_simplex, G)
pytest.raises(nx.NetworkXUnbounded, nx.capacity_scaling, G)
G[1][1]['capacity'] = 2
flowCost, H = nx.network_simplex(G)
assert flowCost == -2
assert H == {1: {1: 2}}
flowCost, H = nx.capacity_scaling(G)
assert flowCost == -2
assert H == {1: {1: 2}}
G = nx.MultiDiGraph()
G.add_edge(1, 1, 'x', weight=-1)
G.add_edge(1, 1, 'y', weight=1)
pytest.raises(nx.NetworkXUnbounded, nx.network_simplex, G)
pytest.raises(nx.NetworkXUnbounded, nx.capacity_scaling, G)
G[1][1]['x']['capacity'] = 2
flowCost, H = nx.network_simplex(G)
assert flowCost == -2
assert H == {1: {1: {'x': 2, 'y': 0}}}
flowCost, H = nx.capacity_scaling(G)
assert flowCost == -2
assert H == {1: {1: {'x': 2, 'y': 0}}}
```

## Next Steps


---

*Source: test_mincost.py:382 | Complexity: Advanced | Last updated: 2026-06-02*