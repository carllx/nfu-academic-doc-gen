# How To: Trivial Labels Isomorphism

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Trivial labelling of the graph should not change isomorphism verdicts.

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    Trivial labelling of the graph should not change isomorphism verdicts.\n    '

```python
'\n    Trivial labelling of the graph should not change isomorphism verdicts.\n    '
```

**Verification:**
```python
assert equal == equal_node
```

### Step 2: Assign unknown = value

```python
n, r = (100, 10)
```

**Verification:**
```python
assert equal_node == equal_edge
```

### Step 3: Assign p = value

```python
p = 1.0 / r
```

**Verification:**
```python
assert equal_edge == equal_both
```

### Step 4: Assign G1 = nx.erdos_renyi_graph(...)

```python
G1 = nx.erdos_renyi_graph(n, p * i, seed=500 + i)
```

### Step 5: Assign G2 = nx.erdos_renyi_graph(...)

```python
G2 = nx.erdos_renyi_graph(n, p * i, seed=42 + i)
```

### Step 6: Assign G1_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
G1_hash = nx.weisfeiler_lehman_graph_hash(G1)
```

### Step 7: Assign G2_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
G2_hash = nx.weisfeiler_lehman_graph_hash(G2)
```

### Step 8: Assign equal = value

```python
equal = G1_hash == G2_hash
```

### Step 9: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, values=1, name='weight')
```

### Step 10: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, values=1, name='weight')
```

### Step 11: Assign G1_hash_node = nx.weisfeiler_lehman_graph_hash(...)

```python
G1_hash_node = nx.weisfeiler_lehman_graph_hash(G1, node_attr='weight')
```

### Step 12: Assign G2_hash_node = nx.weisfeiler_lehman_graph_hash(...)

```python
G2_hash_node = nx.weisfeiler_lehman_graph_hash(G2, node_attr='weight')
```

### Step 13: Assign equal_node = value

```python
equal_node = G1_hash_node == G2_hash_node
```

### Step 14: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G1, values='a', name='e_weight')
```

### Step 15: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G2, values='a', name='e_weight')
```

### Step 16: Assign G1_hash_edge = nx.weisfeiler_lehman_graph_hash(...)

```python
G1_hash_edge = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='e_weight')
```

### Step 17: Assign G2_hash_edge = nx.weisfeiler_lehman_graph_hash(...)

```python
G2_hash_edge = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='e_weight')
```

### Step 18: Assign equal_edge = value

```python
equal_edge = G1_hash_edge == G2_hash_edge
```

### Step 19: Assign G1_hash_both = nx.weisfeiler_lehman_graph_hash(...)

```python
G1_hash_both = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='e_weight', node_attr='weight')
```

### Step 20: Assign G2_hash_both = nx.weisfeiler_lehman_graph_hash(...)

```python
G2_hash_both = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='e_weight', node_attr='weight')
```

### Step 21: Assign equal_both = value

```python
equal_both = G1_hash_both == G2_hash_both
```

**Verification:**
```python
assert equal == equal_node
```


## Complete Example

```python
# Workflow
'\n    Trivial labelling of the graph should not change isomorphism verdicts.\n    '
n, r = (100, 10)
p = 1.0 / r
for i in range(1, r + 1):
    G1 = nx.erdos_renyi_graph(n, p * i, seed=500 + i)
    G2 = nx.erdos_renyi_graph(n, p * i, seed=42 + i)
    G1_hash = nx.weisfeiler_lehman_graph_hash(G1)
    G2_hash = nx.weisfeiler_lehman_graph_hash(G2)
    equal = G1_hash == G2_hash
    nx.set_node_attributes(G1, values=1, name='weight')
    nx.set_node_attributes(G2, values=1, name='weight')
    G1_hash_node = nx.weisfeiler_lehman_graph_hash(G1, node_attr='weight')
    G2_hash_node = nx.weisfeiler_lehman_graph_hash(G2, node_attr='weight')
    equal_node = G1_hash_node == G2_hash_node
    nx.set_edge_attributes(G1, values='a', name='e_weight')
    nx.set_edge_attributes(G2, values='a', name='e_weight')
    G1_hash_edge = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='e_weight')
    G2_hash_edge = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='e_weight')
    equal_edge = G1_hash_edge == G2_hash_edge
    G1_hash_both = nx.weisfeiler_lehman_graph_hash(G1, edge_attr='e_weight', node_attr='weight')
    G2_hash_both = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='e_weight', node_attr='weight')
    equal_both = G1_hash_both == G2_hash_both
    assert equal == equal_node
    assert equal_node == equal_edge
    assert equal_edge == equal_both
```

## Next Steps


---

*Source: test_graph_hashing.py:319 | Complexity: Advanced | Last updated: 2026-06-02*