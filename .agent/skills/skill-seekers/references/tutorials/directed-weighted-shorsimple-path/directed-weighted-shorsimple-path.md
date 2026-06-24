# How To: Directed Weighted Shorsimple Path

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed weighted shortest simple path

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

### Step 2: Assign G = G.to_directed(...)

```python
G = G.to_directed()
```

### Step 3: Assign weight = value

```python
weight = {(u, v): random.randint(1, 100) for u, v in G.edges()}
```

### Step 4: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, weight, 'weight')
```

### Step 5: Assign cost = 0

```python
cost = 0
```

### Step 6: Assign this_cost = cost_func(...)

```python
this_cost = cost_func(path)
```

**Verification:**
```python
assert cost <= this_cost
```

### Step 7: Assign cost = this_cost

```python
cost = this_cost
```


## Complete Example

```python
# Workflow
def cost_func(path):
    return sum((G.adj[u][v]['weight'] for u, v in zip(path, path[1:])))
G = nx.complete_graph(5)
G = G.to_directed()
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

*Source: test_simple_paths.py:551 | Complexity: Intermediate | Last updated: 2026-06-02*