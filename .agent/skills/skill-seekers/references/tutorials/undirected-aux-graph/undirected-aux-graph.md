# How To: Undirected Aux Graph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test undirected aux graph

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.connectivity`
- `networkx.algorithms.connectivity.edge_kcomponents`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign unknown = 'abcdefghi'

```python
a, b, c, d, e, f, g, h, i = 'abcdefghi'
```

**Verification:**
```python
assert target_1 == components_1
```

### Step 2: Assign paths = value

```python
paths = [(a, d, b, f, c), (a, e, b), (a, e, b, c, g, b, a), (c, b), (f, g, f), (h, i)]
```

**Verification:**
```python
assert alt_1 == components_1
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph(it.chain(*[pairwise(path) for path in paths]))
```

**Verification:**
```python
assert target_2 == components_2
```

### Step 4: Assign aux_graph = EdgeComponentAuxGraph.construct(...)

```python
aux_graph = EdgeComponentAuxGraph.construct(G)
```

**Verification:**
```python
assert alt_2 == components_2
```

### Step 5: Assign components_1 = fset(...)

```python
components_1 = fset(aux_graph.k_edge_subgraphs(k=1))
```

**Verification:**
```python
assert target_3 == components_3
```

### Step 6: Assign target_1 = fset(...)

```python
target_1 = fset([{a, b, c, d, e, f, g}, {h, i}])
```

**Verification:**
```python
assert target_4 == components_4
```

### Step 7: Assign alt_1 = fset(...)

```python
alt_1 = fset(nx.k_edge_subgraphs(G, k=1))
```

**Verification:**
```python
assert alt_1 == components_1
```

### Step 8: Assign components_2 = fset(...)

```python
components_2 = fset(aux_graph.k_edge_subgraphs(k=2))
```

### Step 9: Assign target_2 = fset(...)

```python
target_2 = fset([{a, b, c, d, e, f, g}, {h}, {i}])
```

**Verification:**
```python
assert target_2 == components_2
```

### Step 10: Assign alt_2 = fset(...)

```python
alt_2 = fset(nx.k_edge_subgraphs(G, k=2))
```

**Verification:**
```python
assert alt_2 == components_2
```

### Step 11: Assign components_3 = fset(...)

```python
components_3 = fset(aux_graph.k_edge_subgraphs(k=3))
```

### Step 12: Assign target_3 = fset(...)

```python
target_3 = fset([{a}, {b, c, f, g}, {d}, {e}, {h}, {i}])
```

**Verification:**
```python
assert target_3 == components_3
```

### Step 13: Assign components_4 = fset(...)

```python
components_4 = fset(aux_graph.k_edge_subgraphs(k=4))
```

### Step 14: Assign target_4 = fset(...)

```python
target_4 = fset([{a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}, {i}])
```

**Verification:**
```python
assert target_4 == components_4
```

### Step 15: Call _check_edge_connectivity()

```python
_check_edge_connectivity(G)
```


## Complete Example

```python
# Workflow
a, b, c, d, e, f, g, h, i = 'abcdefghi'
paths = [(a, d, b, f, c), (a, e, b), (a, e, b, c, g, b, a), (c, b), (f, g, f), (h, i)]
G = nx.Graph(it.chain(*[pairwise(path) for path in paths]))
aux_graph = EdgeComponentAuxGraph.construct(G)
components_1 = fset(aux_graph.k_edge_subgraphs(k=1))
target_1 = fset([{a, b, c, d, e, f, g}, {h, i}])
assert target_1 == components_1
alt_1 = fset(nx.k_edge_subgraphs(G, k=1))
assert alt_1 == components_1
components_2 = fset(aux_graph.k_edge_subgraphs(k=2))
target_2 = fset([{a, b, c, d, e, f, g}, {h}, {i}])
assert target_2 == components_2
alt_2 = fset(nx.k_edge_subgraphs(G, k=2))
assert alt_2 == components_2
components_3 = fset(aux_graph.k_edge_subgraphs(k=3))
target_3 = fset([{a}, {b, c, f, g}, {d}, {e}, {h}, {i}])
assert target_3 == components_3
components_4 = fset(aux_graph.k_edge_subgraphs(k=4))
target_4 = fset([{a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}, {i}])
assert target_4 == components_4
_check_edge_connectivity(G)
```

## Next Steps


---

*Source: test_edge_kcomponents.py:257 | Complexity: Advanced | Last updated: 2026-06-02*