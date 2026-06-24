# How To: Key Data Bool

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the keys and data values are included in
MST edges based on whether keys and data parameters are
true or false

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `math`
- `math`
- `random`
- `random`
- `itertools`


## Step-by-Step Guide

### Step 1: 'Tests that the keys and data values are included in\n        MST edges based on whether keys and data parameters are\n        true or false'

```python
'Tests that the keys and data values are included in\n        MST edges based on whether keys and data parameters are\n        true or false'
```

**Verification:**
```python
assert edges_equal([(1, 2, 1), (2, 3, 1)], list(mst_edges))
```

### Step 2: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert edges_equal([(1, 2, {'weight': 2}), (2, 3, {'weight': 2})], list(mst_edges))
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2, key=1, weight=2)
```

**Verification:**
```python
assert edges_equal([(1, 2), (2, 3)], list(mst_edges))
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 2, key=2, weight=3)
```

**Verification:**
```python
assert edges_equal([(1, 2, 1, {'weight': 2}), (2, 3, 1, {'weight': 2})], list(mst_edges))
```

### Step 5: Call G.add_edge()

```python
G.add_edge(3, 2, key=1, weight=2)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(3, 1, key=1, weight=4)
```

### Step 7: Assign mst_edges = nx.minimum_spanning_edges(...)

```python
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=True, data=False)
```

**Verification:**
```python
assert edges_equal([(1, 2, 1), (2, 3, 1)], list(mst_edges))
```

### Step 8: Assign mst_edges = nx.minimum_spanning_edges(...)

```python
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=False, data=True)
```

**Verification:**
```python
assert edges_equal([(1, 2, {'weight': 2}), (2, 3, {'weight': 2})], list(mst_edges))
```

### Step 9: Assign mst_edges = nx.minimum_spanning_edges(...)

```python
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=False, data=False)
```

**Verification:**
```python
assert edges_equal([(1, 2), (2, 3)], list(mst_edges))
```

### Step 10: Assign mst_edges = nx.minimum_spanning_edges(...)

```python
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=True, data=True)
```

**Verification:**
```python
assert edges_equal([(1, 2, 1, {'weight': 2}), (2, 3, 1, {'weight': 2})], list(mst_edges))
```


## Complete Example

```python
# Workflow
'Tests that the keys and data values are included in\n        MST edges based on whether keys and data parameters are\n        true or false'
G = nx.MultiGraph()
G.add_edge(1, 2, key=1, weight=2)
G.add_edge(1, 2, key=2, weight=3)
G.add_edge(3, 2, key=1, weight=2)
G.add_edge(3, 1, key=1, weight=4)
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=True, data=False)
assert edges_equal([(1, 2, 1), (2, 3, 1)], list(mst_edges))
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=False, data=True)
assert edges_equal([(1, 2, {'weight': 2}), (2, 3, {'weight': 2})], list(mst_edges))
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=False, data=False)
assert edges_equal([(1, 2), (2, 3)], list(mst_edges))
mst_edges = nx.minimum_spanning_edges(G, algorithm=self.algo, keys=True, data=True)
assert edges_equal([(1, 2, 1, {'weight': 2}), (2, 3, 1, {'weight': 2})], list(mst_edges))
```

## Next Steps


---

*Source: test_mst.py:289 | Complexity: Advanced | Last updated: 2026-06-02*