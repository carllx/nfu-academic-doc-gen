# How To: Brandes Erlebach Book

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test brandes erlebach book

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert 3 == len(nx.minimum_edge_cut(G, 1, 11, **kwargs)), errmsg
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 6), (4, 6), (4, 7), (5, 7), (6, 8), (6, 9), (7, 8), (7, 10), (8, 11), (9, 10), (9, 11), (10, 11)])
```

**Verification:**
```python
assert 2 == len(edge_cut), errmsg
```

### Step 3: Assign kwargs = value

```python
kwargs = {'flow_func': flow_func}
```

**Verification:**
```python
assert not nx.is_connected(H), errmsg
```

### Step 4: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__}'
```

**Verification:**
```python
assert {6, 7} == minimum_st_node_cut(G, 1, 11, **kwargs), errmsg
```

### Step 5: Assign edge_cut = nx.minimum_edge_cut(...)

```python
edge_cut = nx.minimum_edge_cut(G, **kwargs)
```

**Verification:**
```python
assert {6, 7} == nx.minimum_node_cut(G, 1, 11, **kwargs), errmsg
```

### Step 6: Assign H = G.copy(...)

```python
H = G.copy()
```

**Verification:**
```python
assert 2 == len(node_cut), errmsg
```

### Step 7: Call H.remove_edges_from()

```python
H.remove_edges_from(edge_cut)
```

**Verification:**
```python
assert not nx.is_connected(H), errmsg
```

### Step 8: Assign node_cut = nx.minimum_node_cut(...)

```python
node_cut = nx.minimum_node_cut(G, **kwargs)
```

**Verification:**
```python
assert 2 == len(node_cut), errmsg
```

### Step 9: Assign H = G.copy(...)

```python
H = G.copy()
```

### Step 10: Call H.remove_nodes_from()

```python
H.remove_nodes_from(node_cut)
```

**Verification:**
```python
assert not nx.is_connected(H), errmsg
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 6), (3, 4), (3, 6), (4, 6), (4, 7), (5, 7), (6, 8), (6, 9), (7, 8), (7, 10), (8, 11), (9, 10), (9, 11), (10, 11)])
for flow_func in flow_funcs:
    kwargs = {'flow_func': flow_func}
    errmsg = f'Assertion failed in function: {flow_func.__name__}'
    assert 3 == len(nx.minimum_edge_cut(G, 1, 11, **kwargs)), errmsg
    edge_cut = nx.minimum_edge_cut(G, **kwargs)
    assert 2 == len(edge_cut), errmsg
    H = G.copy()
    H.remove_edges_from(edge_cut)
    assert not nx.is_connected(H), errmsg
    assert {6, 7} == minimum_st_node_cut(G, 1, 11, **kwargs), errmsg
    assert {6, 7} == nx.minimum_node_cut(G, 1, 11, **kwargs), errmsg
    node_cut = nx.minimum_node_cut(G, **kwargs)
    assert 2 == len(node_cut), errmsg
    H = G.copy()
    H.remove_nodes_from(node_cut)
    assert not nx.is_connected(H), errmsg
```

## Next Steps


---

*Source: test_cuts.py:45 | Complexity: Advanced | Last updated: 2026-06-02*