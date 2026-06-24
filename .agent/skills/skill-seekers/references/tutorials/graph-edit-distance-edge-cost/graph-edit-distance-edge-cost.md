# How To: Graph Edit Distance Edge Cost

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph edit distance edge cost

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.similarity`
- `networkx.generators.classic`


## Step-by-Step Guide

### Step 1: Assign G1 = path_graph(...)

```python
G1 = path_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2, edge_subst_cost=edge_subst_cost, edge_del_cost=edge_del_cost, edge_ins_cost=edge_ins_cost) == 0.23
```

### Step 2: Assign G2 = path_graph(...)

```python
G2 = path_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2, edge_subst_cost=edge_subst_cost, edge_del_cost=edge_del_cost, edge_ins_cost=edge_ins_cost) == 0.23
```

### Step 3: Assign unknown = value

```python
attr['color'] = 'red' if min(e) % 2 == 0 else 'blue'
```

### Step 4: Assign unknown = value

```python
attr['color'] = 'red' if min(e) // 3 == 0 else 'blue'
```


## Complete Example

```python
# Workflow
G1 = path_graph(6)
G2 = path_graph(6)
for e, attr in G1.edges.items():
    attr['color'] = 'red' if min(e) % 2 == 0 else 'blue'
for e, attr in G2.edges.items():
    attr['color'] = 'red' if min(e) // 3 == 0 else 'blue'

def edge_subst_cost(gattr, hattr):
    if gattr['color'] == hattr['color']:
        return 0.01
    else:
        return 0.1

def edge_del_cost(attr):
    if attr['color'] == 'blue':
        return 0.2
    else:
        return 0.5

def edge_ins_cost(attr):
    if attr['color'] == 'blue':
        return 0.4
    else:
        return 1.0
assert graph_edit_distance(G1, G2, edge_subst_cost=edge_subst_cost, edge_del_cost=edge_del_cost, edge_ins_cost=edge_ins_cost) == 0.23
```

## Next Steps


---

*Source: test_similarity.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*