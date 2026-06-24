# How To: Digraph2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test digraph2

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
assert flow == soln
```

### Step 2: Call G.add_edge()

```python
G.add_edge('s', 1, capacity=12)
```

**Verification:**
```python
assert flow['t']['s'] == 32
```

### Step 3: Call G.add_edge()

```python
G.add_edge('s', 2, capacity=6)
```

**Verification:**
```python
assert flowCost == -3007
```

### Step 4: Call G.add_edge()

```python
G.add_edge('s', 3, capacity=14)
```

**Verification:**
```python
assert flow == soln
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2, capacity=11, weight=4)
```

**Verification:**
```python
assert nx.cost_of_flow(G, flow) == 193
```

### Step 6: Call G.add_edge()

```python
G.add_edge(2, 3, capacity=9, weight=6)
```

### Step 7: Call G.add_edge()

```python
G.add_edge(1, 4, capacity=5, weight=5)
```

### Step 8: Call G.add_edge()

```python
G.add_edge(1, 5, capacity=2, weight=12)
```

### Step 9: Call G.add_edge()

```python
G.add_edge(2, 5, capacity=4, weight=4)
```

### Step 10: Call G.add_edge()

```python
G.add_edge(2, 6, capacity=2, weight=6)
```

### Step 11: Call G.add_edge()

```python
G.add_edge(3, 6, capacity=31, weight=3)
```

### Step 12: Call G.add_edge()

```python
G.add_edge(4, 5, capacity=18, weight=4)
```

### Step 13: Call G.add_edge()

```python
G.add_edge(5, 6, capacity=9, weight=5)
```

### Step 14: Call G.add_edge()

```python
G.add_edge(4, 't', capacity=3)
```

### Step 15: Call G.add_edge()

```python
G.add_edge(5, 't', capacity=7)
```

### Step 16: Call G.add_edge()

```python
G.add_edge(6, 't', capacity=22)
```

### Step 17: Assign flow = nx.max_flow_min_cost(...)

```python
flow = nx.max_flow_min_cost(G, 's', 't')
```

### Step 18: Assign soln = value

```python
soln = {1: {2: 6, 4: 5, 5: 1}, 2: {3: 6, 5: 4, 6: 2}, 3: {6: 20}, 4: {5: 2, 't': 3}, 5: {6: 0, 't': 7}, 6: {'t': 22}, 's': {1: 12, 2: 6, 3: 14}, 't': {}}
```

**Verification:**
```python
assert flow == soln
```

### Step 19: Call G.add_edge()

```python
G.add_edge('t', 's', weight=-100)
```

### Step 20: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, flow = nx.capacity_scaling(G)
```

### Step 21: Call G.remove_edge()

```python
G.remove_edge('t', 's')
```

**Verification:**
```python
assert flow['t']['s'] == 32
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge('s', 1, capacity=12)
G.add_edge('s', 2, capacity=6)
G.add_edge('s', 3, capacity=14)
G.add_edge(1, 2, capacity=11, weight=4)
G.add_edge(2, 3, capacity=9, weight=6)
G.add_edge(1, 4, capacity=5, weight=5)
G.add_edge(1, 5, capacity=2, weight=12)
G.add_edge(2, 5, capacity=4, weight=4)
G.add_edge(2, 6, capacity=2, weight=6)
G.add_edge(3, 6, capacity=31, weight=3)
G.add_edge(4, 5, capacity=18, weight=4)
G.add_edge(5, 6, capacity=9, weight=5)
G.add_edge(4, 't', capacity=3)
G.add_edge(5, 't', capacity=7)
G.add_edge(6, 't', capacity=22)
flow = nx.max_flow_min_cost(G, 's', 't')
soln = {1: {2: 6, 4: 5, 5: 1}, 2: {3: 6, 5: 4, 6: 2}, 3: {6: 20}, 4: {5: 2, 't': 3}, 5: {6: 0, 't': 7}, 6: {'t': 22}, 's': {1: 12, 2: 6, 3: 14}, 't': {}}
assert flow == soln
G.add_edge('t', 's', weight=-100)
flowCost, flow = nx.capacity_scaling(G)
G.remove_edge('t', 's')
assert flow['t']['s'] == 32
assert flowCost == -3007
del flow['t']['s']
assert flow == soln
assert nx.cost_of_flow(G, flow) == 193
```

## Next Steps


---

*Source: test_mincost.py:187 | Complexity: Advanced | Last updated: 2026-06-02*