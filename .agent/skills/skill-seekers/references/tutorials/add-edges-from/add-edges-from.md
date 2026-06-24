# How To: Add Edges From

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add edges from

## Prerequisites

**Required Modules:**
- `collections`
- `pytest`
- `networkx`
- `networkx.utils`
- `test_multigraph`
- `test_multigraph`
- `test_multigraph`


## Step-by-Step Guide

### Step 1: Assign G = self.Graph(...)

```python
G = self.Graph()
```

**Verification:**
```python
assert G._adj == {0: {1: {0: {}, 1: {'weight': 3}}}, 1: {}}
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (0, 1, {'weight': 3})])
```

**Verification:**
```python
assert G._succ == {0: {1: {0: {}, 1: {'weight': 3}}}, 1: {}}
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (0, 1, {'weight': 3})], weight=2)
```

**Verification:**
```python
assert G._pred == {0: {}, 1: {0: {0: {}, 1: {'weight': 3}}}}
```

### Step 4: Assign G = self.Graph(...)

```python
G = self.Graph()
```

**Verification:**
```python
assert G._succ == {0: {1: {0: {}, 1: {'weight': 3}, 2: {'weight': 2}, 3: {'weight': 3}}}, 1: {}}
```

### Step 5: Assign edges = value

```python
edges = [(0, 1, {'weight': 3}), (0, 1, (('weight', 2),)), (0, 1, 5), (0, 1, 's')]
```

**Verification:**
```python
assert G._pred == {0: {}, 1: {0: {0: {}, 1: {'weight': 3}, 2: {'weight': 2}, 3: {'weight': 3}}}}
```

### Step 6: Call G.add_edges_from()

```python
G.add_edges_from(edges)
```

**Verification:**
```python
assert G._succ == {0: {1: keydict}, 1: {}}
```

### Step 7: Assign keydict = value

```python
keydict = {0: {'weight': 3}, 1: {'weight': 2}, 5: {}, 's': {}}
```

**Verification:**
```python
assert G._pred == {1: {0: keydict}, 0: {}}
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, G.add_edges_from, [(0,)])
```

### Step 9: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, G.add_edges_from, [(0, 1, 2, 3, 4)])
```

### Step 10: Call pytest.raises()

```python
pytest.raises(TypeError, G.add_edges_from, [0])
```

### Step 11: Call G.add_edges_from()

```python
G.add_edges_from([(None, 3), (3, 2)])
```


## Complete Example

```python
# Workflow
G = self.Graph()
G.add_edges_from([(0, 1), (0, 1, {'weight': 3})])
assert G._adj == {0: {1: {0: {}, 1: {'weight': 3}}}, 1: {}}
assert G._succ == {0: {1: {0: {}, 1: {'weight': 3}}}, 1: {}}
assert G._pred == {0: {}, 1: {0: {0: {}, 1: {'weight': 3}}}}
G.add_edges_from([(0, 1), (0, 1, {'weight': 3})], weight=2)
assert G._succ == {0: {1: {0: {}, 1: {'weight': 3}, 2: {'weight': 2}, 3: {'weight': 3}}}, 1: {}}
assert G._pred == {0: {}, 1: {0: {0: {}, 1: {'weight': 3}, 2: {'weight': 2}, 3: {'weight': 3}}}}
G = self.Graph()
edges = [(0, 1, {'weight': 3}), (0, 1, (('weight', 2),)), (0, 1, 5), (0, 1, 's')]
G.add_edges_from(edges)
keydict = {0: {'weight': 3}, 1: {'weight': 2}, 5: {}, 's': {}}
assert G._succ == {0: {1: keydict}, 1: {}}
assert G._pred == {1: {0: keydict}, 0: {}}
pytest.raises(nx.NetworkXError, G.add_edges_from, [(0,)])
pytest.raises(nx.NetworkXError, G.add_edges_from, [(0, 1, 2, 3, 4)])
pytest.raises(TypeError, G.add_edges_from, [0])
with pytest.raises(ValueError, match='None cannot be a node'):
    G.add_edges_from([(None, 3), (3, 2)])
```

## Next Steps


---

*Source: test_multidigraph.py:291 | Complexity: Advanced | Last updated: 2026-06-02*