# How To: Custom Graph3 Different Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom graph3 different labels

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
mapped = {1: 9, 2: 8, 3: 7, 4: 6, 5: 3, 8: 5, 9: 4, 7: 1, 6: 2}
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 3: Assign edges1 = value

```python
edges1 = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 7), (4, 9), (5, 8), (8, 9), (5, 6), (6, 7), (5, 2)]
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 4: Call G1.add_edges_from()

```python
G1.add_edges_from(edges1)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 5: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, mapped)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip([mapped[n] for n in G1], it.cycle(labels_many))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 8: Call G1.add_edge()

```python
G1.add_edge(1, 7)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 9: Call G2.add_edge()

```python
G2.add_edge(9, 1)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 10: Call G1.add_node()

```python
G1.add_node('A')
```

### Step 11: Call G2.add_node()

```python
G2.add_node('K')
```

### Step 12: Assign unknown = 'green'

```python
G1.nodes['A']['label'] = 'green'
```

### Step 13: Assign unknown = 'green'

```python
G2.nodes['K']['label'] = 'green'
```

### Step 14: Call mapped.update()

```python
mapped.update({'A': 'K'})
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
```

### Step 15: Call G1.add_edge()

```python
G1.add_edge('A', 6)
```

### Step 16: Call G2.add_edge()

```python
G2.add_edge('K', 5)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 17: Call G1.add_edge()

```python
G1.add_edge(1, 5)
```

### Step 18: Call G1.add_edge()

```python
G1.add_edge(2, 9)
```

### Step 19: Call G2.add_edge()

```python
G2.add_edge(9, 3)
```

### Step 20: Call G2.add_edge()

```python
G2.add_edge(8, 4)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
```

### Step 21: Assign color = 'red'

```python
color = 'red'
```

### Step 22: Assign unknown = color

```python
G1.nodes[node]['label'] = color
```

### Step 23: Assign unknown = color

```python
G2.nodes[mapped[node]]['label'] = color
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
mapped = {1: 9, 2: 8, 3: 7, 4: 6, 5: 3, 8: 5, 9: 4, 7: 1, 6: 2}
edges1 = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 7), (4, 9), (5, 8), (8, 9), (5, 6), (6, 7), (5, 2)]
G1.add_edges_from(edges1)
G2 = nx.relabel_nodes(G1, mapped)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
nx.set_node_attributes(G2, dict(zip([mapped[n] for n in G1], it.cycle(labels_many))), 'label')
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
G1.add_edge(1, 7)
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
G2.add_edge(9, 1)
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
G1.add_node('A')
G2.add_node('K')
G1.nodes['A']['label'] = 'green'
G2.nodes['K']['label'] = 'green'
mapped.update({'A': 'K'})
assert vf2pp_isomorphism(G1, G2, node_label='label') == mapped
G1.add_edge('A', 6)
G2.add_edge('K', 5)
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
G1.add_edge(1, 5)
G1.add_edge(2, 9)
G2.add_edge(9, 3)
G2.add_edge(8, 4)
assert vf2pp_isomorphism(G1, G2, node_label='label') is None
for node in G1.nodes():
    color = 'red'
    G1.nodes[node]['label'] = color
    G2.nodes[mapped[node]]['label'] = color
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

## Next Steps


---

*Source: test_vf2pp.py:331 | Complexity: Advanced | Last updated: 2026-06-02*