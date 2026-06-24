# How To: Weight Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weight name

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

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(7)
```

**Verification:**
```python
assert paths == solution
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, 1, 'weight')
```

### Step 3: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, 1, 'foo')
```

### Step 4: Assign unknown = 7

```python
G.adj[1][2]['foo'] = 7
```

### Step 5: Assign paths = list(...)

```python
paths = list(nx.shortest_simple_paths(G, 0, 3, weight='foo'))
```

### Step 6: Assign solution = value

```python
solution = [[0, 6, 5, 4, 3], [0, 1, 2, 3]]
```

**Verification:**
```python
assert paths == solution
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(7)
nx.set_edge_attributes(G, 1, 'weight')
nx.set_edge_attributes(G, 1, 'foo')
G.adj[1][2]['foo'] = 7
paths = list(nx.shortest_simple_paths(G, 0, 3, weight='foo'))
solution = [[0, 6, 5, 4, 3], [0, 1, 2, 3]]
assert paths == solution
```

## Next Steps


---

*Source: test_simple_paths.py:608 | Complexity: Intermediate | Last updated: 2026-06-02*