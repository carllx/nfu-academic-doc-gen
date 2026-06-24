# How To: Hidden Nodes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hidden nodes

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign hide_nodes = value

```python
hide_nodes = [4, 5, 111]
```

**Verification:**
```python
assert self.G.nodes - G.nodes == {4, 5}
```

### Step 2: Assign nodes_gone = nx.filters.hide_nodes(...)

```python
nodes_gone = nx.filters.hide_nodes(hide_nodes)
```

**Verification:**
```python
assert self.G.edges - G.edges == self.hide_edges_w_hide_nodes
```

### Step 3: Assign gview = value

```python
gview = self.gview
```

**Verification:**
```python
assert list(G[3]) == []
```

### Step 4: Assign G = gview(...)

```python
G = gview(self.G, filter_node=nodes_gone)
```

**Verification:**
```python
assert list(G[2]) == [3]
```

### Step 5: Call pytest.raises()

```python
pytest.raises(KeyError, G.__getitem__, 4)
```

**Verification:**
```python
assert list(G[3]) == [2]
```

### Step 6: Call pytest.raises()

```python
pytest.raises(KeyError, G.__getitem__, 112)
```

**Verification:**
```python
assert set(G[2]) == {1, 3}
```

### Step 7: Call pytest.raises()

```python
pytest.raises(KeyError, G.__getitem__, 111)
```

**Verification:**
```python
assert G.degree(3) == (3 if G.is_multigraph() else 1)
```


## Complete Example

```python
# Workflow
hide_nodes = [4, 5, 111]
nodes_gone = nx.filters.hide_nodes(hide_nodes)
gview = self.gview
G = gview(self.G, filter_node=nodes_gone)
assert self.G.nodes - G.nodes == {4, 5}
assert self.G.edges - G.edges == self.hide_edges_w_hide_nodes
if G.is_directed():
    assert list(G[3]) == []
    assert list(G[2]) == [3]
else:
    assert list(G[3]) == [2]
    assert set(G[2]) == {1, 3}
pytest.raises(KeyError, G.__getitem__, 4)
pytest.raises(KeyError, G.__getitem__, 112)
pytest.raises(KeyError, G.__getitem__, 111)
assert G.degree(3) == (3 if G.is_multigraph() else 1)
assert G.size() == (7 if G.is_multigraph() else 5)
```

## Next Steps


---

*Source: test_subgraphviews.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*