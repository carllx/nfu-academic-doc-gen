# How To: Hidden Edges

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hidden edges

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign hide_edges = value

```python
hide_edges = [(2, 3), (8, 7), (222, 223)]
```

**Verification:**
```python
assert self.G.nodes == G.nodes
```

### Step 2: Assign edges_gone = self.hide_edges_filter(...)

```python
edges_gone = self.hide_edges_filter(hide_edges)
```

**Verification:**
```python
assert self.G.edges - G.edges == {(2, 3)}
```

### Step 3: Assign gview = value

```python
gview = self.gview
```

**Verification:**
```python
assert list(G[2]) == []
```

### Step 4: Assign G = gview(...)

```python
G = gview(self.G, filter_edge=edges_gone)
```

**Verification:**
```python
assert list(G.pred[3]) == []
```

### Step 5: Call pytest.raises()

```python
pytest.raises(KeyError, G.__getitem__, 221)
```

**Verification:**
```python
assert list(G.pred[2]) == [1]
```

### Step 6: Call pytest.raises()

```python
pytest.raises(KeyError, G.__getitem__, 222)
```

**Verification:**
```python
assert G.size() == 7
```


## Complete Example

```python
# Workflow
hide_edges = [(2, 3), (8, 7), (222, 223)]
edges_gone = self.hide_edges_filter(hide_edges)
gview = self.gview
G = gview(self.G, filter_edge=edges_gone)
assert self.G.nodes == G.nodes
if G.is_directed():
    assert self.G.edges - G.edges == {(2, 3)}
    assert list(G[2]) == []
    assert list(G.pred[3]) == []
    assert list(G.pred[2]) == [1]
    assert G.size() == 7
else:
    assert self.G.edges - G.edges == {(2, 3), (7, 8)}
    assert list(G[2]) == [1]
    assert G.size() == 6
assert list(G[3]) == [4]
pytest.raises(KeyError, G.__getitem__, 221)
pytest.raises(KeyError, G.__getitem__, 222)
assert G.degree(3) == 1
```

## Next Steps


---

*Source: test_subgraphviews.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*