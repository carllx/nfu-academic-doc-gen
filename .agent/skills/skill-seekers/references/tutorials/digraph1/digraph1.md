# How To: Digraph1

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test digraph1

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert flowCost == 150
```

### Step 2: Call G.add_node()

```python
G.add_node(1, demand=-20)
```

**Verification:**
```python
assert nx.min_cost_flow_cost(G) == 150
```

### Step 3: Call G.add_node()

```python
G.add_node(4, demand=5)
```

**Verification:**
```python
assert H == soln
```

### Step 4: Call G.add_node()

```python
G.add_node(5, demand=15)
```

**Verification:**
```python
assert nx.min_cost_flow(G) == soln
```

### Step 5: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2, {'capacity': 15, 'weight': 4}), (1, 3, {'capacity': 8, 'weight': 4}), (2, 3, {'weight': 2}), (2, 4, {'capacity': 4, 'weight': 2}), (2, 5, {'capacity': 10, 'weight': 6}), (3, 4, {'capacity': 15, 'weight': 1}), (3, 5, {'capacity': 5, 'weight': 3}), (4, 5, {'weight': 2}), (5, 3, {'capacity': 4, 'weight': 1})])
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 150
```

### Step 6: Assign unknown = nx.network_simplex(...)

```python
flowCost, H = nx.network_simplex(G)
```

**Verification:**
```python
assert flowCost == 150
```

### Step 7: Assign soln = value

```python
soln = {1: {2: 12, 3: 8}, 2: {3: 8, 4: 4, 5: 0}, 3: {4: 11, 5: 5}, 4: {5: 10}, 5: {3: 0}}
```

**Verification:**
```python
assert H == soln
```

### Step 8: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, H = nx.capacity_scaling(G)
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 150
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_node(1, demand=-20)
G.add_node(4, demand=5)
G.add_node(5, demand=15)
G.add_edges_from([(1, 2, {'capacity': 15, 'weight': 4}), (1, 3, {'capacity': 8, 'weight': 4}), (2, 3, {'weight': 2}), (2, 4, {'capacity': 4, 'weight': 2}), (2, 5, {'capacity': 10, 'weight': 6}), (3, 4, {'capacity': 15, 'weight': 1}), (3, 5, {'capacity': 5, 'weight': 3}), (4, 5, {'weight': 2}), (5, 3, {'capacity': 4, 'weight': 1})])
flowCost, H = nx.network_simplex(G)
soln = {1: {2: 12, 3: 8}, 2: {3: 8, 4: 4, 5: 0}, 3: {4: 11, 5: 5}, 4: {5: 10}, 5: {3: 0}}
assert flowCost == 150
assert nx.min_cost_flow_cost(G) == 150
assert H == soln
assert nx.min_cost_flow(G) == soln
assert nx.cost_of_flow(G, H) == 150
flowCost, H = nx.capacity_scaling(G)
assert flowCost == 150
assert H == soln
assert nx.cost_of_flow(G, H) == 150
```

## Next Steps


---

*Source: test_mincost.py:148 | Complexity: Advanced | Last updated: 2026-06-02*