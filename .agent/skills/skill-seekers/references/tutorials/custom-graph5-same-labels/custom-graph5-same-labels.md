# How To: Custom Graph5 Same Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom graph5 same labels

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
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 2: Assign edges1 = value

```python
edges1 = [(1, 5), (1, 2), (1, 4), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 8), (5, 6), (6, 7), (7, 8)]
```

**Verification:**
```python
assert len(all_self_mappings) == 48
```

### Step 3: Assign mapped = value

```python
mapped = {1: 'a', 2: 'h', 3: 'd', 4: 'i', 5: 'g', 6: 'b', 7: 'j', 8: 'c'}
```

**Verification:**
```python
assert all((sum((1 for m in all_self_mappings if m[u] == u)) == 6 for u in G1))
```

### Step 4: Call G1.add_edges_from()

```python
G1.add_edges_from(edges1)
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 5: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, mapped)
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_same))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_same))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 8: Assign all_self_mappings = list(...)

```python
all_self_mappings = list(vf2pp_all_isomorphisms(G1, G1))
```

**Verification:**
```python
assert len(all_self_mappings) == 48
```

### Step 9: Call G1.add_edges_from()

```python
G1.add_edges_from([(3, 6), (2, 7), (2, 5), (1, 3), (4, 7), (6, 8)])
```

### Step 10: Call G2.add_edges_from()

```python
G2.add_edges_from([(mapped[6], mapped[3]), (mapped[2], mapped[7]), (mapped[1], mapped[6]), (mapped[5], mapped[7]), (mapped[3], mapped[8]), (mapped[2], mapped[4])])
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 11: Assign H1 = nx.Graph(...)

```python
H1 = nx.Graph(G1.subgraph([1, 5, 8, 6, 7, 3]))
```

### Step 12: Assign H2 = nx.Graph(...)

```python
H2 = nx.Graph(G2.subgraph([mapped[1], mapped[4], mapped[8], mapped[7], mapped[3], mapped[5]]))
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 13: Call H1.remove_node()

```python
H1.remove_node(8)
```

### Step 14: Call H2.remove_node()

```python
H2.remove_node(mapped[7])
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 15: Call H1.add_edge()

```python
H1.add_edge(1, 6)
```

### Step 16: Call H1.remove_edge()

```python
H1.remove_edge(3, 6)
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
edges1 = [(1, 5), (1, 2), (1, 4), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 8), (5, 6), (6, 7), (7, 8)]
mapped = {1: 'a', 2: 'h', 3: 'd', 4: 'i', 5: 'g', 6: 'b', 7: 'j', 8: 'c'}
G1.add_edges_from(edges1)
G2 = nx.relabel_nodes(G1, mapped)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_same))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_same))), 'label')
assert vf2pp_isomorphism(G1, G2, node_label='label')
all_self_mappings = list(vf2pp_all_isomorphisms(G1, G1))
assert len(all_self_mappings) == 48
assert all((sum((1 for m in all_self_mappings if m[u] == u)) == 6 for u in G1))
G1.add_edges_from([(3, 6), (2, 7), (2, 5), (1, 3), (4, 7), (6, 8)])
G2.add_edges_from([(mapped[6], mapped[3]), (mapped[2], mapped[7]), (mapped[1], mapped[6]), (mapped[5], mapped[7]), (mapped[3], mapped[8]), (mapped[2], mapped[4])])
assert vf2pp_isomorphism(G1, G2, node_label='label')
H1 = nx.Graph(G1.subgraph([1, 5, 8, 6, 7, 3]))
H2 = nx.Graph(G2.subgraph([mapped[1], mapped[4], mapped[8], mapped[7], mapped[3], mapped[5]]))
assert vf2pp_isomorphism(H1, H2, node_label='label')
H1.remove_node(8)
H2.remove_node(mapped[7])
assert vf2pp_isomorphism(H1, H2, node_label='label')
H1.add_edge(1, 6)
H1.remove_edge(3, 6)
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

## Next Steps


---

*Source: test_vf2pp.py:523 | Complexity: Advanced | Last updated: 2026-06-02*