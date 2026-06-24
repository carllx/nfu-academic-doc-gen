# How To: Path Weighted Projected Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test path weighted projected graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

**Verification:**
```python
assert nodes_equal(list(P), [1, 3])
```

### Step 2: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, [1, 3])
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(1, 3)])
```

### Step 3: Assign unknown = 1

```python
P[1][3]['weight'] = 1
```

**Verification:**
```python
assert nodes_equal(list(P), [0, 2])
```

### Step 4: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, [0, 2])
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(0, 2)])
```

### Step 5: Assign unknown = 1

```python
P[0][2]['weight'] = 1
```

### Step 6: Call bipartite.weighted_projected_graph()

```python
bipartite.weighted_projected_graph(G, [1, 2, 3, 3])
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
with pytest.raises(nx.NetworkXAlgorithmError):
    bipartite.weighted_projected_graph(G, [1, 2, 3, 3])
P = bipartite.weighted_projected_graph(G, [1, 3])
assert nodes_equal(list(P), [1, 3])
assert edges_equal(list(P.edges()), [(1, 3)])
P[1][3]['weight'] = 1
P = bipartite.weighted_projected_graph(G, [0, 2])
assert nodes_equal(list(P), [0, 2])
assert edges_equal(list(P.edges()), [(0, 2)])
P[0][2]['weight'] = 1
```

## Next Steps


---

*Source: test_project.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*