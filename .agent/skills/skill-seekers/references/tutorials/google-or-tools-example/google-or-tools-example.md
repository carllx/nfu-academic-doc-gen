# How To: Google Or Tools Example

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: https://developers.google.com/optimization/flow/mincostflow

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    https://developers.google.com/optimization/flow/mincostflow\n    '

```python
'\n    https://developers.google.com/optimization/flow/mincostflow\n    '
```

**Verification:**
```python
assert flowCost == answer
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert flowCost == get_flowcost_from_flowdict(G, flowDict)
```

### Step 3: Assign start_nodes = value

```python
start_nodes = [0, 0, 1, 1, 1, 2, 2, 3, 4]
```

### Step 4: Assign end_nodes = value

```python
end_nodes = [1, 2, 2, 3, 4, 3, 4, 4, 2]
```

### Step 5: Assign capacities = value

```python
capacities = [15, 8, 20, 4, 10, 15, 4, 20, 5]
```

### Step 6: Assign unit_costs = value

```python
unit_costs = [4, 4, 2, 2, 6, 1, 3, 2, 3]
```

### Step 7: Assign supplies = value

```python
supplies = [20, 0, 0, -5, -15]
```

### Step 8: Assign answer = 150

```python
answer = 150
```

### Step 9: Assign unknown = nx.network_simplex(...)

```python
flowCost, flowDict = nx.network_simplex(G)
```

**Verification:**
```python
assert flowCost == answer
```

### Step 10: Call G.add_node()

```python
G.add_node(i, demand=-1 * supplies[i])
```

### Step 11: Call G.add_edge()

```python
G.add_edge(start_nodes[i], end_nodes[i], weight=unit_costs[i], capacity=capacities[i])
```


## Complete Example

```python
# Workflow
'\n    https://developers.google.com/optimization/flow/mincostflow\n    '
G = nx.DiGraph()
start_nodes = [0, 0, 1, 1, 1, 2, 2, 3, 4]
end_nodes = [1, 2, 2, 3, 4, 3, 4, 4, 2]
capacities = [15, 8, 20, 4, 10, 15, 4, 20, 5]
unit_costs = [4, 4, 2, 2, 6, 1, 3, 2, 3]
supplies = [20, 0, 0, -5, -15]
answer = 150
for i in range(len(supplies)):
    G.add_node(i, demand=-1 * supplies[i])
for i in range(len(start_nodes)):
    G.add_edge(start_nodes[i], end_nodes[i], weight=unit_costs[i], capacity=capacities[i])
flowCost, flowDict = nx.network_simplex(G)
assert flowCost == answer
assert flowCost == get_flowcost_from_flowdict(G, flowDict)
```

## Next Steps


---

*Source: test_networksimplex.py:123 | Complexity: Advanced | Last updated: 2026-06-02*