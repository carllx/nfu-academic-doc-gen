# How To: Average Connectivity

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test average connectivity

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.path_graph(...)

```python
G1 = nx.path_graph(3)
```

**Verification:**
```python
assert nx.average_node_connectivity(G1, **kwargs) == 1, errmsg
```

### Step 2: Call G1.add_edges_from()

```python
G1.add_edges_from([(1, 3), (1, 4)])
```

**Verification:**
```python
assert nx.average_node_connectivity(G2, **kwargs) == 2.2, errmsg
```

### Step 3: Assign G2 = nx.path_graph(...)

```python
G2 = nx.path_graph(3)
```

**Verification:**
```python
assert nx.average_node_connectivity(G3, **kwargs) == 0, errmsg
```

### Step 4: Call G2.add_edges_from()

```python
G2.add_edges_from([(1, 3), (1, 4), (0, 3), (0, 4), (3, 4)])
```

### Step 5: Assign G3 = nx.Graph(...)

```python
G3 = nx.Graph()
```

### Step 6: Assign kwargs = value

```python
kwargs = {'flow_func': flow_func}
```

### Step 7: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__}'
```

**Verification:**
```python
assert nx.average_node_connectivity(G1, **kwargs) == 1, errmsg
```


## Complete Example

```python
# Workflow
G1 = nx.path_graph(3)
G1.add_edges_from([(1, 3), (1, 4)])
G2 = nx.path_graph(3)
G2.add_edges_from([(1, 3), (1, 4), (0, 3), (0, 4), (3, 4)])
G3 = nx.Graph()
for flow_func in flow_funcs:
    kwargs = {'flow_func': flow_func}
    errmsg = f'Assertion failed in function: {flow_func.__name__}'
    assert nx.average_node_connectivity(G1, **kwargs) == 1, errmsg
    assert nx.average_node_connectivity(G2, **kwargs) == 2.2, errmsg
    assert nx.average_node_connectivity(G3, **kwargs) == 0, errmsg
```

## Next Steps


---

*Source: test_connectivity.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*