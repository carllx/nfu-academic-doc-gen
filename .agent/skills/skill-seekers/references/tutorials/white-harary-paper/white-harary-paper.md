# How To: White Harary Paper

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test white harary paper

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.disjoint_union(...)

```python
G = nx.disjoint_union(nx.complete_graph(4), nx.complete_graph(4))
```

**Verification:**
```python
assert 3 == len(edge_cut), errmsg
```

### Step 2: Call G.remove_node()

```python
G.remove_node(7)
```

**Verification:**
```python
assert not nx.is_connected(H), errmsg
```

### Step 3: Assign G = nx.disjoint_union(...)

```python
G = nx.disjoint_union(G, nx.complete_graph(4))
```

**Verification:**
```python
assert {0} == node_cut, errmsg
```

### Step 4: Call G.remove_node()

```python
G.remove_node(G.order() - 1)
```

**Verification:**
```python
assert not nx.is_connected(H), errmsg
```

### Step 5: Call G.add_edge()

```python
G.add_edge(0, i)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(0, i)
```

### Step 7: Assign kwargs = value

```python
kwargs = {'flow_func': flow_func}
```

### Step 8: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__}'
```

### Step 9: Assign edge_cut = nx.minimum_edge_cut(...)

```python
edge_cut = nx.minimum_edge_cut(G, **kwargs)
```

**Verification:**
```python
assert 3 == len(edge_cut), errmsg
```

### Step 10: Assign H = G.copy(...)

```python
H = G.copy()
```

### Step 11: Call H.remove_edges_from()

```python
H.remove_edges_from(edge_cut)
```

**Verification:**
```python
assert not nx.is_connected(H), errmsg
```

### Step 12: Assign node_cut = nx.minimum_node_cut(...)

```python
node_cut = nx.minimum_node_cut(G, **kwargs)
```

**Verification:**
```python
assert {0} == node_cut, errmsg
```

### Step 13: Assign H = G.copy(...)

```python
H = G.copy()
```

### Step 14: Call H.remove_nodes_from()

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
G = nx.disjoint_union(nx.complete_graph(4), nx.complete_graph(4))
G.remove_node(7)
for i in range(4, 7):
    G.add_edge(0, i)
G = nx.disjoint_union(G, nx.complete_graph(4))
G.remove_node(G.order() - 1)
for i in range(7, 10):
    G.add_edge(0, i)
for flow_func in flow_funcs:
    kwargs = {'flow_func': flow_func}
    errmsg = f'Assertion failed in function: {flow_func.__name__}'
    edge_cut = nx.minimum_edge_cut(G, **kwargs)
    assert 3 == len(edge_cut), errmsg
    H = G.copy()
    H.remove_edges_from(edge_cut)
    assert not nx.is_connected(H), errmsg
    node_cut = nx.minimum_node_cut(G, **kwargs)
    assert {0} == node_cut, errmsg
    H = G.copy()
    H.remove_nodes_from(node_cut)
    assert not nx.is_connected(H), errmsg
```

## Next Steps


---

*Source: test_cuts.py:93 | Complexity: Advanced | Last updated: 2026-06-02*