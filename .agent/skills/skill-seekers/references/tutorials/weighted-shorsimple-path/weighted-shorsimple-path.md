# How To: Weighted Shorsimple Path

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weighted shortest simple path

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.simple_paths`
- `networkx.utils`
- `itertools`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert cost <= this_cost
```

### Step 2: Assign weight = value

```python
weight = {(u, v): random.randint(1, 100) for u, v in G.edges()}
```

### Step 3: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, weight, 'weight')
```

### Step 4: Assign cost = 0

```python
cost = 0
```

### Step 5: Assign this_cost = cost_func(...)

```python
this_cost = cost_func(path)
```

**Verification:**
```python
assert cost <= this_cost
```

### Step 6: Assign cost = this_cost

```python
cost = this_cost
```


## Complete Example

```python
# Workflow
def cost_func(path):
    return sum((G.adj[u][v]['weight'] for u, v in zip(path, path[1:])))
G = nx.complete_graph(5)
weight = {(u, v): random.randint(1, 100) for u, v in G.edges()}
nx.set_edge_attributes(G, weight, 'weight')
cost = 0
for path in nx.shortest_simple_paths(G, 0, 3, weight='weight'):
    this_cost = cost_func(path)
    assert cost <= this_cost
    cost = this_cost
```

## Next Steps


---

*Source: test_simple_paths.py:537 | Complexity: Intermediate | Last updated: 2026-06-02*