# How To: Graph From Pr 2053

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph from pr 2053

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert are_edge_disjoint_paths(G, edge_paths), errmsg
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([('A', 'B'), ('A', 'D'), ('A', 'F'), ('A', 'G'), ('B', 'C'), ('B', 'D'), ('B', 'G'), ('C', 'D'), ('C', 'E'), ('C', 'Z'), ('D', 'E'), ('D', 'F'), ('E', 'F'), ('E', 'Z'), ('F', 'Z'), ('G', 'Z')])
```

**Verification:**
```python
assert nx.edge_connectivity(G, 'A', 'Z') == len(edge_paths), errmsg
```

### Step 3: Assign kwargs = value

```python
kwargs = {'flow_func': flow_func}
```

**Verification:**
```python
assert are_node_disjoint_paths(G, node_paths), errmsg
```

### Step 4: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__}'
```

**Verification:**
```python
assert nx.node_connectivity(G, 'A', 'Z') == len(node_paths), errmsg
```

### Step 5: Assign edge_paths = list(...)

```python
edge_paths = list(nx.edge_disjoint_paths(G, 'A', 'Z', **kwargs))
```

**Verification:**
```python
assert are_edge_disjoint_paths(G, edge_paths), errmsg
```

### Step 6: Assign node_paths = list(...)

```python
node_paths = list(nx.node_disjoint_paths(G, 'A', 'Z', **kwargs))
```

**Verification:**
```python
assert are_node_disjoint_paths(G, node_paths), errmsg
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'D'), ('A', 'F'), ('A', 'G'), ('B', 'C'), ('B', 'D'), ('B', 'G'), ('C', 'D'), ('C', 'E'), ('C', 'Z'), ('D', 'E'), ('D', 'F'), ('E', 'F'), ('E', 'Z'), ('F', 'Z'), ('G', 'Z')])
for flow_func in flow_funcs:
    kwargs = {'flow_func': flow_func}
    errmsg = f'Assertion failed in function: {flow_func.__name__}'
    edge_paths = list(nx.edge_disjoint_paths(G, 'A', 'Z', **kwargs))
    assert are_edge_disjoint_paths(G, edge_paths), errmsg
    assert nx.edge_connectivity(G, 'A', 'Z') == len(edge_paths), errmsg
    node_paths = list(nx.node_disjoint_paths(G, 'A', 'Z', **kwargs))
    assert are_node_disjoint_paths(G, node_paths), errmsg
    assert nx.node_connectivity(G, 'A', 'Z') == len(node_paths), errmsg
```

## Next Steps


---

*Source: test_disjoint_paths.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*