# How To: Is Weighted

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is weighted

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert not nx.is_weighted(G)
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

**Verification:**
```python
assert not nx.is_weighted(G)
```

### Step 3: Call G.add_node()

```python
G.add_node(4)
```

**Verification:**
```python
assert not nx.is_weighted(G, (2, 3))
```

### Step 4: Call G.add_edge()

```python
G.add_edge(3, 4, weight=4)
```

**Verification:**
```python
assert not nx.is_weighted(G)
```

### Step 5: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert nx.is_weighted(G, (3, 4))
```

### Step 6: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([('0', '3', 3), ('0', '1', -5), ('1', '0', -5), ('0', '2', 2), ('1', '2', 4), ('2', '3', 1)])
```

**Verification:**
```python
assert nx.is_weighted(G)
```

### Step 7: Assign G = G.to_undirected(...)

```python
G = G.to_undirected()
```

**Verification:**
```python
assert nx.is_weighted(G, ('1', '0'))
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.is_weighted, G, (1, 2))
```

**Verification:**
```python
assert nx.is_weighted(G)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
assert not nx.is_weighted(G)
G = nx.path_graph(4)
assert not nx.is_weighted(G)
assert not nx.is_weighted(G, (2, 3))
G.add_node(4)
G.add_edge(3, 4, weight=4)
assert not nx.is_weighted(G)
assert nx.is_weighted(G, (3, 4))
G = nx.DiGraph()
G.add_weighted_edges_from([('0', '3', 3), ('0', '1', -5), ('1', '0', -5), ('0', '2', 2), ('1', '2', 4), ('2', '3', 1)])
assert nx.is_weighted(G)
assert nx.is_weighted(G, ('1', '0'))
G = G.to_undirected()
assert nx.is_weighted(G)
assert nx.is_weighted(G, ('1', '0'))
pytest.raises(nx.NetworkXError, nx.is_weighted, G, (1, 2))
```

## Next Steps


---

*Source: test_function.py:365 | Complexity: Advanced | Last updated: 2026-06-02*