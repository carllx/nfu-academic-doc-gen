# How To: Star Projected Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test star projected graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.star_graph(...)

```python
G = nx.star_graph(3)
```

**Verification:**
```python
assert nodes_equal(list(P), [1, 2, 3])
```

### Step 2: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, [1, 2, 3])
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(1, 2), (1, 3), (2, 3)])
```

### Step 3: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, [1, 2, 3])
```

**Verification:**
```python
assert nodes_equal(list(P), [1, 2, 3])
```

### Step 4: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, [0])
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(1, 2), (1, 3), (2, 3)])
```


## Complete Example

```python
# Workflow
G = nx.star_graph(3)
P = bipartite.projected_graph(G, [1, 2, 3])
assert nodes_equal(list(P), [1, 2, 3])
assert edges_equal(list(P.edges()), [(1, 2), (1, 3), (2, 3)])
P = bipartite.weighted_projected_graph(G, [1, 2, 3])
assert nodes_equal(list(P), [1, 2, 3])
assert edges_equal(list(P.edges()), [(1, 2), (1, 3), (2, 3)])
P = bipartite.projected_graph(G, [0])
assert nodes_equal(list(P), [0])
assert edges_equal(list(P.edges()), [])
```

## Next Steps


---

*Source: test_project.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*