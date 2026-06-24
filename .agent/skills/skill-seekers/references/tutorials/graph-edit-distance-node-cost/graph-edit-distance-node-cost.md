# How To: Graph Edit Distance Node Cost

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph edit distance node cost

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
assert graph_edit_distance(G1, G2, node_subst_cost=node_subst_cost, node_del_cost=node_del_cost, node_ins_cost=node_ins_cost) == 6
```

### Step 2: Assign G2 = path_graph(...)

```python
G2 = path_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2, node_subst_cost=node_subst_cost, node_del_cost=node_del_cost, node_ins_cost=node_ins_cost) == 6
```

### Step 3: Assign unknown = value

```python
attr['color'] = 'red' if n % 2 == 0 else 'blue'
```

### Step 4: Assign unknown = value

```python
attr['color'] = 'red' if n % 2 == 1 else 'blue'
```


## Complete Example

```python
# Workflow
G1 = path_graph(6)
G2 = path_graph(6)
for n, attr in G1.nodes.items():
    attr['color'] = 'red' if n % 2 == 0 else 'blue'
for n, attr in G2.nodes.items():
    attr['color'] = 'red' if n % 2 == 1 else 'blue'

def node_subst_cost(uattr, vattr):
    if uattr['color'] == vattr['color']:
        return 1
    else:
        return 10

def node_del_cost(attr):
    if attr['color'] == 'blue':
        return 20
    else:
        return 50

def node_ins_cost(attr):
    if attr['color'] == 'blue':
        return 40
    else:
        return 100
assert graph_edit_distance(G1, G2, node_subst_cost=node_subst_cost, node_del_cost=node_del_cost, node_ins_cost=node_ins_cost) == 6
```

## Next Steps


---

*Source: test_similarity.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*