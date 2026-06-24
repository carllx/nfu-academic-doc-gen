# How To: Path Projected Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test path projected graph

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

### Step 2: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, [1, 3])
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(1, 3)])
```

### Step 3: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, [0, 2])
```

**Verification:**
```python
assert nodes_equal(list(P), [0, 2])
```

### Step 4: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph([(0, 1)])
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [(0, 2)])
```

### Step 5: Call bipartite.projected_graph()

```python
bipartite.projected_graph(G, [0])
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
P = bipartite.projected_graph(G, [1, 3])
assert nodes_equal(list(P), [1, 3])
assert edges_equal(list(P.edges()), [(1, 3)])
P = bipartite.projected_graph(G, [0, 2])
assert nodes_equal(list(P), [0, 2])
assert edges_equal(list(P.edges()), [(0, 2)])
G = nx.MultiGraph([(0, 1)])
with pytest.raises(nx.NetworkXError, match='not defined for multigraphs'):
    bipartite.projected_graph(G, [0])
```

## Next Steps


---

*Source: test_project.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*