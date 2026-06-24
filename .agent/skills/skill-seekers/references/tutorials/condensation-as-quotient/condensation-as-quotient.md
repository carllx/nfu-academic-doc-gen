# How To: Condensation As Quotient

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: This tests that the condensation of a graph can be viewed as the
quotient graph under the "in the same connected component" equivalence
relation.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'This tests that the condensation of a graph can be viewed as the\n    quotient graph under the "in the same connected component" equivalence\n    relation.\n\n    '

```python
'This tests that the condensation of a graph can be viewed as the\n    quotient graph under the "in the same connected component" equivalence\n    relation.\n\n    '
```

**Verification:**
```python
assert nx.is_isomorphic(C, Q)
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2), (2, 3), (2, 11), (2, 12), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5), (6, 7), (7, 8), (7, 9), (7, 10), (8, 9), (9, 7), (10, 6), (11, 2), (11, 4), (11, 6), (12, 6), (12, 11)])
```

### Step 4: Assign scc = list(...)

```python
scc = list(nx.strongly_connected_components(G))
```

### Step 5: Assign C = nx.condensation(...)

```python
C = nx.condensation(G, scc)
```

### Step 6: Assign component_of = value

```python
component_of = C.graph['mapping']
```

### Step 7: Assign Q = nx.quotient_graph(...)

```python
Q = nx.quotient_graph(G, same_component)
```

**Verification:**
```python
assert nx.is_isomorphic(C, Q)
```


## Complete Example

```python
# Workflow
'This tests that the condensation of a graph can be viewed as the\n    quotient graph under the "in the same connected component" equivalence\n    relation.\n\n    '
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (2, 11), (2, 12), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5), (6, 7), (7, 8), (7, 9), (7, 10), (8, 9), (9, 7), (10, 6), (11, 2), (11, 4), (11, 6), (12, 6), (12, 11)])
scc = list(nx.strongly_connected_components(G))
C = nx.condensation(G, scc)
component_of = C.graph['mapping']

def same_component(u, v):
    return component_of[u] == component_of[v]
Q = nx.quotient_graph(G, same_component)
assert nx.is_isomorphic(C, Q)
```

## Next Steps


---

*Source: test_contraction.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*