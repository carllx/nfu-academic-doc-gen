# How To: Custom Graph1 Same Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom graph1 same labels

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

### Step 2: Assign mapped = value

```python
mapped = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'Z', 6: 'E'}
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 3: Assign edges1 = value

```python
edges1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 6), (3, 4), (5, 1), (5, 2)]
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 4: Call G1.add_edges_from()

```python
G1.add_edges_from(edges1)
```

**Verification:**
```python
assert len(all_self_mappings) == 2
```

### Step 5: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, mapped)
```

**Verification:**
```python
assert sum((1 for m in all_self_mappings if m[2] == 2)) == 1
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_many))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 8: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_same))), 'label')
```

### Step 9: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_same))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 10: Call G1.add_edge()

```python
G1.add_edge(3, 7)
```

### Step 11: Assign unknown = 'blue'

```python
G1.nodes[7]['label'] = 'blue'
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 12: Assign all_self_mappings = list(...)

```python
all_self_mappings = list(vf2pp_all_isomorphisms(G1, G1))
```

**Verification:**
```python
assert len(all_self_mappings) == 2
```

### Step 13: Call G2.add_edges_from()

```python
G2.add_edges_from([(mapped[3], 'X'), (mapped[6], mapped[5])])
```

### Step 14: Call G1.add_edge()

```python
G1.add_edge(4, 7)
```

### Step 15: Assign unknown = 'blue'

```python
G2.nodes['X']['label'] = 'blue'
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 16: Call G1.remove_edges_from()

```python
G1.remove_edges_from([(1, 4), (1, 3)])
```

### Step 17: Call G2.remove_edges_from()

```python
G2.remove_edges_from([(mapped[1], mapped[5]), (mapped[1], mapped[2])])
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
mapped = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'Z', 6: 'E'}
edges1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 6), (3, 4), (5, 1), (5, 2)]
G1.add_edges_from(edges1)
G2 = nx.relabel_nodes(G1, mapped)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_many))), 'label')
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_same))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_same))), 'label')
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
G1.add_edge(3, 7)
G1.nodes[7]['label'] = 'blue'
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
all_self_mappings = list(vf2pp_all_isomorphisms(G1, G1))
assert len(all_self_mappings) == 2
assert sum((1 for m in all_self_mappings if m[2] == 2)) == 1
G2.add_edges_from([(mapped[3], 'X'), (mapped[6], mapped[5])])
G1.add_edge(4, 7)
G2.nodes['X']['label'] = 'blue'
assert vf2pp_isomorphism(G1, G2, node_label='label')
G1.remove_edges_from([(1, 4), (1, 3)])
G2.remove_edges_from([(mapped[1], mapped[5]), (mapped[1], mapped[2])])
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

## Next Steps


---

*Source: test_vf2pp.py:149 | Complexity: Advanced | Last updated: 2026-06-02*