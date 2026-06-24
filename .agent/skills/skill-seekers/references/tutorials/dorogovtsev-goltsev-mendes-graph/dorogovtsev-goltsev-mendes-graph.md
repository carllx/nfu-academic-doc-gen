# How To: Dorogovtsev Goltsev Mendes Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dorogovtsev goltsev mendes graph

## Prerequisites

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.dorogovtsev_goltsev_mendes_graph(...)

```python
G = nx.dorogovtsev_goltsev_mendes_graph(0)
```

**Verification:**
```python
assert edges_equal(G.edges(), [(0, 1)])
```

### Step 2: Assign G = nx.dorogovtsev_goltsev_mendes_graph(...)

```python
G = nx.dorogovtsev_goltsev_mendes_graph(1)
```

**Verification:**
```python
assert nodes_equal(list(G), [0, 1])
```

### Step 3: Assign G = nx.dorogovtsev_goltsev_mendes_graph(...)

```python
G = nx.dorogovtsev_goltsev_mendes_graph(2)
```

**Verification:**
```python
assert edges_equal(G.edges(), [(0, 1), (0, 2), (1, 2)])
```

### Step 4: Assign G = nx.dorogovtsev_goltsev_mendes_graph(...)

```python
G = nx.dorogovtsev_goltsev_mendes_graph(10)
```

**Verification:**
```python
assert nx.average_clustering(G) == 1.0
```

### Step 5: Call nx.dorogovtsev_goltsev_mendes_graph()

```python
nx.dorogovtsev_goltsev_mendes_graph(-1)
```

**Verification:**
```python
assert nx.average_shortest_path_length(G) == 1.0
```

### Step 6: Call nx.dorogovtsev_goltsev_mendes_graph()

```python
nx.dorogovtsev_goltsev_mendes_graph(7, create_using=nx.DiGraph)
```

**Verification:**
```python
assert sorted(nx.triangles(G).values()) == [1, 1, 1]
```

### Step 7: Call nx.dorogovtsev_goltsev_mendes_graph()

```python
nx.dorogovtsev_goltsev_mendes_graph(7, create_using=nx.MultiGraph)
```

**Verification:**
```python
assert nx.is_planar(G)
```

### Step 8: Call nx.dorogovtsev_goltsev_mendes_graph()

```python
nx.dorogovtsev_goltsev_mendes_graph(7, create_using=nx.MultiDiGraph)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 6
```


## Complete Example

```python
# Workflow
G = nx.dorogovtsev_goltsev_mendes_graph(0)
assert edges_equal(G.edges(), [(0, 1)])
assert nodes_equal(list(G), [0, 1])
G = nx.dorogovtsev_goltsev_mendes_graph(1)
assert edges_equal(G.edges(), [(0, 1), (0, 2), (1, 2)])
assert nx.average_clustering(G) == 1.0
assert nx.average_shortest_path_length(G) == 1.0
assert sorted(nx.triangles(G).values()) == [1, 1, 1]
assert nx.is_planar(G)
G = nx.dorogovtsev_goltsev_mendes_graph(2)
assert nx.number_of_nodes(G) == 6
assert nx.number_of_edges(G) == 9
assert nx.average_clustering(G) == 0.75
assert nx.average_shortest_path_length(G) == 1.4
assert nx.is_planar(G)
G = nx.dorogovtsev_goltsev_mendes_graph(10)
assert nx.number_of_nodes(G) == 29526
assert nx.number_of_edges(G) == 59049
assert G.degree(0) == 1024
assert G.degree(1) == 1024
assert G.degree(2) == 1024
with pytest.raises(nx.NetworkXError, match='n must be greater than'):
    nx.dorogovtsev_goltsev_mendes_graph(-1)
with pytest.raises(nx.NetworkXError, match='directed graph not supported'):
    nx.dorogovtsev_goltsev_mendes_graph(7, create_using=nx.DiGraph)
with pytest.raises(nx.NetworkXError, match='multigraph not supported'):
    nx.dorogovtsev_goltsev_mendes_graph(7, create_using=nx.MultiGraph)
with pytest.raises(nx.NetworkXError):
    nx.dorogovtsev_goltsev_mendes_graph(7, create_using=nx.MultiDiGraph)
```

## Next Steps


---

*Source: test_classic.py:232 | Complexity: Advanced | Last updated: 2026-06-02*