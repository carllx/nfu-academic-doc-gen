# How To: Custom Graph2 Same Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom graph2 same labels

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

### Step 2: Assign mapped = value

```python
mapped = {1: 'A', 2: 'C', 3: 'D', 4: 'E', 5: 'G', 7: 'B', 6: 'F'}
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 3: Assign edges1 = value

```python
edges1 = [(1, 2), (1, 5), (5, 6), (2, 3), (2, 4), (3, 4), (4, 5), (2, 7)]
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
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
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_same))), 'label')
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_same))), 'label')
```

**Verification:**
```python
assert vf2pp_isomorphism(G1, G2, node_label='label')
```

### Step 8: Call G2.remove_edge()

```python
G2.remove_edge(mapped[1], mapped[2])
```

### Step 9: Call G2.add_edge()

```python
G2.add_edge(mapped[1], mapped[4])
```

### Step 10: Assign H1 = nx.Graph(...)

```python
H1 = nx.Graph(G1.subgraph([2, 3, 4, 7]))
```

### Step 11: Assign H2 = nx.Graph(...)

```python
H2 = nx.Graph(G2.subgraph([mapped[1], mapped[4], mapped[5], mapped[6]]))
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

### Step 12: Call H1.add_edges_from()

```python
H1.add_edges_from([(3, 7), (4, 7)])
```

### Step 13: Call H2.add_edges_from()

```python
H2.add_edges_from([(mapped[1], mapped[6]), (mapped[4], mapped[6])])
```

**Verification:**
```python
assert vf2pp_isomorphism(H1, H2, node_label='label')
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
mapped = {1: 'A', 2: 'C', 3: 'D', 4: 'E', 5: 'G', 7: 'B', 6: 'F'}
edges1 = [(1, 2), (1, 5), (5, 6), (2, 3), (2, 4), (3, 4), (4, 5), (2, 7)]
G1.add_edges_from(edges1)
G2 = nx.relabel_nodes(G1, mapped)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_same))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels_same))), 'label')
assert vf2pp_isomorphism(G1, G2, node_label='label')
G2.remove_edge(mapped[1], mapped[2])
G2.add_edge(mapped[1], mapped[4])
H1 = nx.Graph(G1.subgraph([2, 3, 4, 7]))
H2 = nx.Graph(G2.subgraph([mapped[1], mapped[4], mapped[5], mapped[6]]))
assert vf2pp_isomorphism(H1, H2, node_label='label')
H1.add_edges_from([(3, 7), (4, 7)])
H2.add_edges_from([(mapped[1], mapped[6]), (mapped[4], mapped[6])])
assert vf2pp_isomorphism(H1, H2, node_label='label')
```

## Next Steps


---

*Source: test_vf2pp.py:192 | Complexity: Advanced | Last updated: 2026-06-02*