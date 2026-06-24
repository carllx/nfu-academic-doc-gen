# How To: Max Flow Min Cost

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test max flow min cost

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
G.add_edge('s', 'a', bandwidth=6)
```

**Verification:**
```python
assert nx.cost_of_flow(G, flow, weight='cost') == 90
```

### Step 3: Call G.add_edge()

```python
G.add_edge('s', 'c', bandwidth=10, cost=10)
```

**Verification:**
```python
assert flowCost == -410
```

### Step 4: Call G.add_edge()

```python
G.add_edge('a', 'b', cost=6)
```

**Verification:**
```python
assert flow['t']['s'] == 5
```

### Step 5: Call G.add_edge()

```python
G.add_edge('b', 'd', bandwidth=8, cost=7)
```

**Verification:**
```python
assert flow == soln
```

### Step 6: Call G.add_edge()

```python
G.add_edge('c', 'd', cost=10)
```

**Verification:**
```python
assert nx.cost_of_flow(G, flow, weight='cost') == 90
```

### Step 7: Call G.add_edge()

```python
G.add_edge('d', 't', bandwidth=5, cost=5)
```

### Step 8: Assign soln = value

```python
soln = {'s': {'a': 5, 'c': 0}, 'a': {'b': 5}, 'b': {'d': 5}, 'c': {'d': 0}, 'd': {'t': 5}, 't': {}}
```

### Step 9: Assign flow = nx.max_flow_min_cost(...)

```python
flow = nx.max_flow_min_cost(G, 's', 't', capacity='bandwidth', weight='cost')
```

**Verification:**
```python
assert flow == soln
```

### Step 10: Call G.add_edge()

```python
G.add_edge('t', 's', cost=-100)
```

### Step 11: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, flow = nx.capacity_scaling(G, capacity='bandwidth', weight='cost')
```

### Step 12: Call G.remove_edge()

```python
G.remove_edge('t', 's')
```

**Verification:**
```python
assert flowCost == -410
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge('s', 'a', bandwidth=6)
G.add_edge('s', 'c', bandwidth=10, cost=10)
G.add_edge('a', 'b', cost=6)
G.add_edge('b', 'd', bandwidth=8, cost=7)
G.add_edge('c', 'd', cost=10)
G.add_edge('d', 't', bandwidth=5, cost=5)
soln = {'s': {'a': 5, 'c': 0}, 'a': {'b': 5}, 'b': {'d': 5}, 'c': {'d': 0}, 'd': {'t': 5}, 't': {}}
flow = nx.max_flow_min_cost(G, 's', 't', capacity='bandwidth', weight='cost')
assert flow == soln
assert nx.cost_of_flow(G, flow, weight='cost') == 90
G.add_edge('t', 's', cost=-100)
flowCost, flow = nx.capacity_scaling(G, capacity='bandwidth', weight='cost')
G.remove_edge('t', 's')
assert flowCost == -410
assert flow['t']['s'] == 5
del flow['t']['s']
assert flow == soln
assert nx.cost_of_flow(G, flow, weight='cost') == 90
```

## Next Steps


---

*Source: test_mincost.py:119 | Complexity: Advanced | Last updated: 2026-06-02*