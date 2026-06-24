# How To: Isomorphic Edge Attr And Node Attr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Isomorphic graphs with differing node attributes should yield different graph
hashes if the 'node_attr' and 'edge_attr' argument is supplied and populated in
the graph, and there are no hash collisions.
The output should still be invariant to node-relabeling

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: "\n    Isomorphic graphs with differing node attributes should yield different graph\n    hashes if the 'node_attr' and 'edge_attr' argument is supplied and populated in\n    the graph, and there are no hash collisions.\n    The output should still be invariant to node-relabeling\n    "

```python
"\n    Isomorphic graphs with differing node attributes should yield different graph\n    hashes if the 'node_attr' and 'edge_attr' argument is supplied and populated in\n    the graph, and there are no hash collisions.\n    The output should still be invariant to node-relabeling\n    "
```

**Verification:**
```python
assert g1_hash_edge1_node1 != g1_hash_no_attr
```

### Step 2: Assign unknown = value

```python
n, r = (100, 10)
```

**Verification:**
```python
assert g1_hash_edge2_node2 != g1_hash_no_attr
```

### Step 3: Assign p = value

```python
p = 1.0 / r
```

**Verification:**
```python
assert g1_hash_edge1_node1 != g1_hash_edge2_node2
```

### Step 4: Assign G1 = nx.erdos_renyi_graph(...)

```python
G1 = nx.erdos_renyi_graph(n, p * i, seed=500 + i)
```

**Verification:**
```python
assert g1_hash_edge1_node2 != g1_hash_edge2_node2
```

### Step 5: Assign g1_hash_edge1_node1 = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_edge1_node1 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr1', node_attr='node_attr1')
```

**Verification:**
```python
assert g1_hash_edge1_node2 != g1_hash_edge1_node1
```

### Step 6: Assign g1_hash_edge2_node2 = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_edge2_node2 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr2', node_attr='node_attr2')
```

**Verification:**
```python
assert g1_hash_edge1_node1 == g2_hash_edge1_node1
```

### Step 7: Assign g1_hash_edge1_node2 = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_edge1_node2 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr1', node_attr='node_attr2')
```

**Verification:**
```python
assert g1_hash_edge2_node2 == g2_hash_edge2_node2
```

### Step 8: Assign g1_hash_no_attr = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash_no_attr = nx.weisfeiler_lehman_graph_hash(G1)
```

**Verification:**
```python
assert g1_hash_edge1_node1 != g1_hash_no_attr
```

### Step 9: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, {u: -1 * u for u in G1.nodes()})
```

### Step 10: Assign g2_hash_edge1_node1 = nx.weisfeiler_lehman_graph_hash(...)

```python
g2_hash_edge1_node1 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1', node_attr='node_attr1')
```

### Step 11: Assign g2_hash_edge2_node2 = nx.weisfeiler_lehman_graph_hash(...)

```python
g2_hash_edge2_node2 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr2', node_attr='node_attr2')
```

**Verification:**
```python
assert g1_hash_edge1_node1 == g2_hash_edge1_node1
```

### Step 12: Assign unknown = value

```python
G1.nodes[u]['node_attr1'] = f'{u}-1'
```

### Step 13: Assign unknown = value

```python
G1.nodes[u]['node_attr2'] = f'{u}-2'
```

### Step 14: Assign unknown = value

```python
G1[a][b]['edge_attr1'] = f'{a}-{b}-1'
```

### Step 15: Assign unknown = value

```python
G1[a][b]['edge_attr2'] = f'{a}-{b}-2'
```


## Complete Example

```python
# Workflow
"\n    Isomorphic graphs with differing node attributes should yield different graph\n    hashes if the 'node_attr' and 'edge_attr' argument is supplied and populated in\n    the graph, and there are no hash collisions.\n    The output should still be invariant to node-relabeling\n    "
n, r = (100, 10)
p = 1.0 / r
for i in range(1, r + 1):
    G1 = nx.erdos_renyi_graph(n, p * i, seed=500 + i)
    for u in G1.nodes():
        G1.nodes[u]['node_attr1'] = f'{u}-1'
        G1.nodes[u]['node_attr2'] = f'{u}-2'
    for a, b in G1.edges:
        G1[a][b]['edge_attr1'] = f'{a}-{b}-1'
        G1[a][b]['edge_attr2'] = f'{a}-{b}-2'
    g1_hash_edge1_node1 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr1', node_attr='node_attr1')
    g1_hash_edge2_node2 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr2', node_attr='node_attr2')
    g1_hash_edge1_node2 = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='edge_attr1', node_attr='node_attr2')
    g1_hash_no_attr = nx.weisfeiler_lehman_graph_hash(G1)
    assert g1_hash_edge1_node1 != g1_hash_no_attr
    assert g1_hash_edge2_node2 != g1_hash_no_attr
    assert g1_hash_edge1_node1 != g1_hash_edge2_node2
    assert g1_hash_edge1_node2 != g1_hash_edge2_node2
    assert g1_hash_edge1_node2 != g1_hash_edge1_node1
    G2 = nx.relabel_nodes(G1, {u: -1 * u for u in G1.nodes()})
    g2_hash_edge1_node1 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1', node_attr='node_attr1')
    g2_hash_edge2_node2 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr2', node_attr='node_attr2')
    assert g1_hash_edge1_node1 == g2_hash_edge1_node1
    assert g1_hash_edge2_node2 == g2_hash_edge2_node2
```

## Next Steps


---

*Source: test_graph_hashing.py:213 | Complexity: Advanced | Last updated: 2026-06-02*