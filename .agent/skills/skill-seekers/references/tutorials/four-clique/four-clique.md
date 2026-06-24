# How To: Four Clique

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test four clique

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.connectivity`
- `networkx.algorithms.connectivity.edge_kcomponents`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign paths = value

```python
paths = [(11, 12, 13, 14, 11, 13, 14, 12), (21, 22, 23, 24, 21, 23, 24, 22), (100, 13), (12, 100, 22), (13, 200, 23), (14, 300, 24)]
```

**Verification:**
```python
assert local_ccs != subgraphs
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph(it.chain(*[pairwise(path) for path in paths]))
```

**Verification:**
```python
assert clique1.union(clique2).union({100}) in local_ccs
```

### Step 3: Assign local_ccs = fset(...)

```python
local_ccs = fset(nx.k_edge_components(G, k=3))
```

**Verification:**
```python
assert clique1 in subgraphs
```

### Step 4: Assign subgraphs = fset(...)

```python
subgraphs = fset(nx.k_edge_subgraphs(G, k=3))
```

**Verification:**
```python
assert clique2 in subgraphs
```

### Step 5: Assign clique1 = frozenset(...)

```python
clique1 = frozenset(paths[0])
```

**Verification:**
```python
assert G.degree(100) == 3
```

### Step 6: Assign clique2 = frozenset(...)

```python
clique2 = frozenset(paths[1])
```

**Verification:**
```python
assert clique1.union(clique2).union({100}) in local_ccs
```

### Step 7: Call _check_edge_connectivity()

```python
_check_edge_connectivity(G)
```


## Complete Example

```python
# Workflow
paths = [(11, 12, 13, 14, 11, 13, 14, 12), (21, 22, 23, 24, 21, 23, 24, 22), (100, 13), (12, 100, 22), (13, 200, 23), (14, 300, 24)]
G = nx.Graph(it.chain(*[pairwise(path) for path in paths]))
local_ccs = fset(nx.k_edge_components(G, k=3))
subgraphs = fset(nx.k_edge_subgraphs(G, k=3))
assert local_ccs != subgraphs
clique1 = frozenset(paths[0])
clique2 = frozenset(paths[1])
assert clique1.union(clique2).union({100}) in local_ccs
assert clique1 in subgraphs
assert clique2 in subgraphs
assert G.degree(100) == 3
_check_edge_connectivity(G)
```

## Next Steps


---

*Source: test_edge_kcomponents.py:360 | Complexity: Intermediate | Last updated: 2026-06-02*