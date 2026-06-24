# How To: Custom Graph4 Different Labels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom graph4 different labels

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph()
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 2: Assign edges1 = value

```python
edges1 = [(1, 2), (2, 3), (3, 8), (3, 4), (4, 5), (4, 6), (3, 6), (8, 7), (8, 9), (5, 9), (10, 11), (11, 12), (12, 13), (11, 13)]
```

### Step 3: Assign mapped = value

```python
mapped = {1: 'n', 2: 'm', 3: 'l', 4: 'j', 5: 'k', 6: 'i', 7: 'g', 8: 'h', 9: 'f', 10: 'b', 11: 'a', 12: 'd', 13: 'e'}
```

### Step 4: Call G1.add_edges_from()

```python
G1.add_edges_from(edges1)
```

### Step 5: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, mapped)
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip([mapped[n] for n in G1], it.cycle(labels_many))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
edges1 = [(1, 2), (2, 3), (3, 8), (3, 4), (4, 5), (4, 6), (3, 6), (8, 7), (8, 9), (5, 9), (10, 11), (11, 12), (12, 13), (11, 13)]
mapped = {1: 'n', 2: 'm', 3: 'l', 4: 'j', 5: 'k', 6: 'i', 7: 'g', 8: 'h', 9: 'f', 10: 'b', 11: 'a', 12: 'd', 13: 'e'}
G1.add_edges_from(edges1)
G2 = nx.relabel_nodes(G1, mapped)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
nx.set_node_attributes(G2, dict(zip([mapped[n] for n in G1], it.cycle(labels_many))), 'label')
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

## Next Steps


---

*Source: test_vf2pp.py:396 | Complexity: Intermediate | Last updated: 2026-06-02*