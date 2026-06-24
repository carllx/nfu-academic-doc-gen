# How To: Local Subgraph Difference

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test local subgraph difference

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
paths = [(11, 12, 13, 14, 11, 13, 14, 12), (21, 22, 23, 24, 21, 23, 24, 22), (11, 101, 21), (12, 102, 22), (13, 103, 23), (14, 104, 24)]
```

**Verification:**
```python
assert subgraph_ccs == subgraph_target
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph(it.chain(*[pairwise(path) for path in paths]))
```

**Verification:**
```python
assert local_ccs == local_target
```

### Step 3: Assign aux_graph = EdgeComponentAuxGraph.construct(...)

```python
aux_graph = EdgeComponentAuxGraph.construct(G)
```

### Step 4: Assign subgraph_ccs = fset(...)

```python
subgraph_ccs = fset(aux_graph.k_edge_subgraphs(3))
```

### Step 5: Assign subgraph_target = fset(...)

```python
subgraph_target = fset([{101}, {102}, {103}, {104}, {21, 22, 23, 24}, {11, 12, 13, 14}])
```

**Verification:**
```python
assert subgraph_ccs == subgraph_target
```

### Step 6: Assign local_ccs = fset(...)

```python
local_ccs = fset(aux_graph.k_edge_components(3))
```

### Step 7: Assign local_target = fset(...)

```python
local_target = fset([{101}, {102}, {103}, {104}, {11, 12, 13, 14, 21, 22, 23, 24}])
```

**Verification:**
```python
assert local_ccs == local_target
```


## Complete Example

```python
# Workflow
paths = [(11, 12, 13, 14, 11, 13, 14, 12), (21, 22, 23, 24, 21, 23, 24, 22), (11, 101, 21), (12, 102, 22), (13, 103, 23), (14, 104, 24)]
G = nx.Graph(it.chain(*[pairwise(path) for path in paths]))
aux_graph = EdgeComponentAuxGraph.construct(G)
subgraph_ccs = fset(aux_graph.k_edge_subgraphs(3))
subgraph_target = fset([{101}, {102}, {103}, {104}, {21, 22, 23, 24}, {11, 12, 13, 14}])
assert subgraph_ccs == subgraph_target
local_ccs = fset(aux_graph.k_edge_components(3))
local_target = fset([{101}, {102}, {103}, {104}, {11, 12, 13, 14, 21, 22, 23, 24}])
assert local_ccs == local_target
```

## Next Steps


---

*Source: test_edge_kcomponents.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*