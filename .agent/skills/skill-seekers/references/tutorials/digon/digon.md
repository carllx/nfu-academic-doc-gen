# How To: Digon

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check if digons are handled properly. Taken from ticket
#618 by arv.

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Check if digons are handled properly. Taken from ticket\n        #618 by arv.'

```python
'Check if digons are handled properly. Taken from ticket\n        #618 by arv.'
```

**Verification:**
```python
assert flowCost == 2857140
```

### Step 2: Assign nodes = value

```python
nodes = [(1, {}), (2, {'demand': -4}), (3, {'demand': 4})]
```

**Verification:**
```python
assert nx.min_cost_flow_cost(G) == 2857140
```

### Step 3: Assign edges = value

```python
edges = [(1, 2, {'capacity': 3, 'weight': 600000}), (2, 1, {'capacity': 2, 'weight': 0}), (2, 3, {'capacity': 5, 'weight': 714285}), (3, 2, {'capacity': 2, 'weight': 0})]
```

**Verification:**
```python
assert H == soln
```

### Step 4: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(edges)
```

**Verification:**
```python
assert nx.min_cost_flow(G) == soln
```

### Step 5: Call G.add_nodes_from()

```python
G.add_nodes_from(nodes)
```

**Verification:**
```python
assert nx.cost_of_flow(G, H) == 2857140
```

### Step 6: Assign unknown = nx.network_simplex(...)

```python
flowCost, H = nx.network_simplex(G)
```

**Verification:**
```python
assert flowCost == 2857140
```

### Step 7: Assign soln = value

```python
soln = {1: {2: 0}, 2: {1: 0, 3: 4}, 3: {2: 0}}
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
assert nx.cost_of_flow(G, H) == 2857140
```


## Complete Example

```python
# Workflow
'Check if digons are handled properly. Taken from ticket\n        #618 by arv.'
nodes = [(1, {}), (2, {'demand': -4}), (3, {'demand': 4})]
edges = [(1, 2, {'capacity': 3, 'weight': 600000}), (2, 1, {'capacity': 2, 'weight': 0}), (2, 3, {'capacity': 5, 'weight': 714285}), (3, 2, {'capacity': 2, 'weight': 0})]
G = nx.DiGraph(edges)
G.add_nodes_from(nodes)
flowCost, H = nx.network_simplex(G)
soln = {1: {2: 0}, 2: {1: 0, 3: 4}, 3: {2: 0}}
assert flowCost == 2857140
assert nx.min_cost_flow_cost(G) == 2857140
assert H == soln
assert nx.min_cost_flow(G) == soln
assert nx.cost_of_flow(G, H) == 2857140
flowCost, H = nx.capacity_scaling(G)
assert flowCost == 2857140
assert H == soln
assert nx.cost_of_flow(G, H) == 2857140
```

## Next Steps


---

*Source: test_mincost.py:304 | Complexity: Advanced | Last updated: 2026-06-02*