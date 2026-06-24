# How To: Simple Digraph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple digraph

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
assert flowCost == 24
```

### Step 2: Call G.add_node()

```python
G.add_node('a', demand=-5)
```

**Verification:**
```python
assert nx.min_cost_flow_cost(G) == 24
```

### Step 3: Call G.add_node()

```python
G.add_node('d', demand=5)
```

**Verification:**
```python
assert H == soln
```

### Step 4: Call G.add_edge()

```python
G.add_edge('a', 'b', weight=3, capacity=4)
```

**Verification:**
```python
assert nx.min_cost_flow(G) == soln
```

### Step 5: Call G.add_edge()

```python
G.add_edge('a', 'c', weight=6, capacity=10)
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 24
```

### Step 6: Call G.add_edge()

```python
G.add_edge('b', 'd', weight=1, capacity=9)
```

**Verification:**
```python
assert flowCost == 24
```

### Step 7: Call G.add_edge()

```python
G.add_edge('c', 'd', weight=2, capacity=5)
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 24
```

### Step 8: Assign unknown = nx.network_simplex(...)

```python
flowCost, H = nx.network_simplex(G)
```

**Verification:**
```python
assert H == soln
```

### Step 9: Assign soln = value

```python
soln = {'a': {'b': 4, 'c': 1}, 'b': {'d': 4}, 'c': {'d': 1}, 'd': {}}
```

**Verification:**
```python
assert flowCost == 24
```

### Step 10: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, H = nx.capacity_scaling(G)
```

**Verification:**
```python
assert flowCost == 24
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_node('a', demand=-5)
G.add_node('d', demand=5)
G.add_edge('a', 'b', weight=3, capacity=4)
G.add_edge('a', 'c', weight=6, capacity=10)
G.add_edge('b', 'd', weight=1, capacity=9)
G.add_edge('c', 'd', weight=2, capacity=5)
flowCost, H = nx.network_simplex(G)
soln = {'a': {'b': 4, 'c': 1}, 'b': {'d': 4}, 'c': {'d': 1}, 'd': {}}
assert flowCost == 24
assert nx.min_cost_flow_cost(G) == 24
assert H == soln
assert nx.min_cost_flow(G) == soln
assert nx.cost_of_flow(G, H) == 24
flowCost, H = nx.capacity_scaling(G)
assert flowCost == 24
assert nx.cost_of_flow(G, H) == 24
assert H == soln
```

## Next Steps


---

*Source: test_mincost.py:11 | Complexity: Advanced | Last updated: 2026-06-02*