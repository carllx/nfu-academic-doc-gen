# How To: Path Weighted Projected Directed Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test path weighted projected directed graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert nodes_equal(list(P), [1, 3])
```

### Step 2: Call nx.add_path()

```python
nx.add_path(G, range(4))
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(1, 3)], directed=True)
```

### Step 3: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, [1, 3])
```

**Verification:**
```python
assert nodes_equal(list(P), [0, 2])
```

### Step 4: Assign unknown = 1

```python
P[1][3]['weight'] = 1
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(0, 2)], directed=True)
```

### Step 5: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, [0, 2])
```

**Verification:**
```python
assert nodes_equal(list(P), [0, 2])
```

### Step 6: Assign unknown = 1

```python
P[0][2]['weight'] = 1
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
nx.add_path(G, range(4))
P = bipartite.weighted_projected_graph(G, [1, 3])
assert nodes_equal(list(P), [1, 3])
assert edges_equal(list(P.edges()), [(1, 3)], directed=True)
P[1][3]['weight'] = 1
P = bipartite.weighted_projected_graph(G, [0, 2])
assert nodes_equal(list(P), [0, 2])
assert edges_equal(list(P.edges()), [(0, 2)], directed=True)
P[0][2]['weight'] = 1
```

## Next Steps


---

*Source: test_project.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*