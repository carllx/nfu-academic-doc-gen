# How To: Zero Capacity Edges

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Address issue raised in ticket #617 by arv.

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Address issue raised in ticket #617 by arv.'

```python
'Address issue raised in ticket #617 by arv.'
```

**Verification:**
```python
assert flowCost == 6
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert nx.min_cost_flow_cost(G) == 6
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2, {'capacity': 1, 'weight': 1}), (1, 5, {'capacity': 1, 'weight': 1}), (2, 3, {'capacity': 0, 'weight': 1}), (2, 5, {'capacity': 1, 'weight': 1}), (5, 3, {'capacity': 2, 'weight': 1}), (5, 4, {'capacity': 0, 'weight': 1}), (3, 4, {'capacity': 2, 'weight': 1})])
```

**Verification:**
```python
assert H == soln
```

### Step 4: Assign unknown = value

```python
G.nodes[1]['demand'] = -1
```

**Verification:**
```python
assert nx.min_cost_flow(G) == soln
```

### Step 5: Assign unknown = value

```python
G.nodes[2]['demand'] = -1
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 6
```

### Step 6: Assign unknown = 2

```python
G.nodes[4]['demand'] = 2
```

**Verification:**
```python
assert flowCost == 6
```

### Step 7: Assign unknown = nx.network_simplex(...)

```python
flowCost, H = nx.network_simplex(G)
```

**Verification:**
```python
assert H == soln
```

### Step 8: Assign soln = value

```python
soln = {1: {2: 0, 5: 1}, 2: {3: 0, 5: 1}, 3: {4: 2}, 4: {}, 5: {3: 2, 4: 0}}
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 6
```

### Step 9: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, H = nx.capacity_scaling(G)
```

**Verification:**
```python
assert flowCost == 6
```


## Complete Example

```python
# Workflow
'Address issue raised in ticket #617 by arv.'
G = nx.DiGraph()
G.add_edges_from([(1, 2, {'capacity': 1, 'weight': 1}), (1, 5, {'capacity': 1, 'weight': 1}), (2, 3, {'capacity': 0, 'weight': 1}), (2, 5, {'capacity': 1, 'weight': 1}), (5, 3, {'capacity': 2, 'weight': 1}), (5, 4, {'capacity': 0, 'weight': 1}), (3, 4, {'capacity': 2, 'weight': 1})])
G.nodes[1]['demand'] = -1
G.nodes[2]['demand'] = -1
G.nodes[4]['demand'] = 2
flowCost, H = nx.network_simplex(G)
soln = {1: {2: 0, 5: 1}, 2: {3: 0, 5: 1}, 3: {4: 2}, 4: {}, 5: {3: 2, 4: 0}}
assert flowCost == 6
assert nx.min_cost_flow_cost(G) == 6
assert H == soln
assert nx.min_cost_flow(G) == soln
assert nx.cost_of_flow(G, H) == 6
flowCost, H = nx.capacity_scaling(G)
assert flowCost == 6
assert H == soln
assert nx.cost_of_flow(G, H) == 6
```

## Next Steps


---

*Source: test_mincost.py:273 | Complexity: Advanced | Last updated: 2026-06-02*