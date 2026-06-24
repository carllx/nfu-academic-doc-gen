# How To: Isomorphic Edge Attr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Isomorphic graphs with differing edge attributes should yield different graph
hashes if the 'edge_attr' argument is supplied and populated in the graph,
and there are no hash collisions.
The output should still be invariant to node-relabeling

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: "\n    Isomorphic graphs with differing edge attributes should yield different graph\n    hashes if the 'edge_attr' argument is supplied and populated in the graph,\n    and there are no hash collisions.\n    The output should still be invariant to node-relabeling\n    "

```python
"\n    Isomorphic graphs with differing edge attributes should yield different graph\n    hashes if the 'edge_attr' argument is supplied and populated in the graph,\n    and there are no hash collisions.\n    The output should still be invariant to node-relabeling\n    "
```

**Verification:**
```python
assert g1_hash_with_edge_attr1 != g1_hash_no_edge_attr
```

### Step 2: Assign unknown = value

```python
n, r = (100, 10)
```

**Verification:**
```python
assert g1_hash_with_edge_attr2 != g1_hash_no_edge_attr
```

### Step 3: Assign p = value

```python
p = 1.0 / r
```

**Verification:**
```python
assert g1_hash_with_edge_attr1 != g1_hash_with_edge_attr2
```

### Step 4: Assign G1 = nx.erdos_renyi_graph(...)

```python
G1 = nx.erdos_renyi_graph(n, p * i, seed=300 + i)
```

**Verification:**
```python
assert g1_hash_with_edge_attr1 == g2_hash_with_edge_attr1
```

### Step 5: Assign g1_hash_with_edge_attr1 = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_with_edge_attr1 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr1')
```

**Verification:**
```python
assert g1_hash_with_edge_attr2 == g2_hash_with_edge_attr2
```

### Step 6: Assign g1_hash_with_edge_attr2 = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_with_edge_attr2 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr2')
```

### Step 7: Assign g1_hash_no_edge_attr = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_no_edge_attr = nx.weisfeiler_lehman_graph_hash(G1, edge_attr=None)
```

**Verification:**
```python
assert g1_hash_with_edge_attr1 != g1_hash_no_edge_attr
```

### Step 8: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, {u: -1 * u for u in G1.nodes()})
```

### Step 9: Assign g2_hash_with_edge_attr1 = nx.weisfeiler_lehman_graph_hash(...)

```python
g2_hash_with_edge_attr1 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1')
```

### Step 10: Assign g2_hash_with_edge_attr2 = nx.weisfeiler_lehman_graph_hash(...)

```python
g2_hash_with_edge_attr2 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr2')
```

**Verification:**
```python
assert g1_hash_with_edge_attr1 == g2_hash_with_edge_attr1
```

### Step 11: Assign unknown = value

```python
G1[a][b]['edge_attr1'] = f'{a}-{b}-1'
```

### Step 12: Assign unknown = value

```python
G1[a][b]['edge_attr2'] = f'{a}-{b}-2'
```


## Complete Example

```python
# Workflow
"\n    Isomorphic graphs with differing edge attributes should yield different graph\n    hashes if the 'edge_attr' argument is supplied and populated in the graph,\n    and there are no hash collisions.\n    The output should still be invariant to node-relabeling\n    "
n, r = (100, 10)
p = 1.0 / r
for i in range(1, r + 1):
    G1 = nx.erdos_renyi_graph(n, p * i, seed=300 + i)
    for a, b in G1.edges:
        G1[a][b]['edge_attr1'] = f'{a}-{b}-1'
        G1[a][b]['edge_attr2'] = f'{a}-{b}-2'
    g1_hash_with_edge_attr1 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr1')
    g1_hash_with_edge_attr2 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr2')
    g1_hash_no_edge_attr = nx.weisfeiler_lehman_graph_hash(G1, edge_attr=None)
    assert g1_hash_with_edge_attr1 != g1_hash_no_edge_attr
    assert g1_hash_with_edge_attr2 != g1_hash_no_edge_attr
    assert g1_hash_with_edge_attr1 != g1_hash_with_edge_attr2
    G2 = nx.relabel_nodes(G1, {u: -1 * u for u in G1.nodes()})
    g2_hash_with_edge_attr1 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1')
    g2_hash_with_edge_attr2 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr2')
    assert g1_hash_with_edge_attr1 == g2_hash_with_edge_attr1
    assert g1_hash_with_edge_attr2 == g2_hash_with_edge_attr2
```

## Next Steps


---

*Source: test_graph_hashing.py:110 | Complexity: Advanced | Last updated: 2026-06-02*