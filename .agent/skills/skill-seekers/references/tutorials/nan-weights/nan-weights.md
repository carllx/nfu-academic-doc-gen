# How To: Nan Weights

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nan weights

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

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert edges_equal(actual, expected)
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 12, weight=float('nan'))
```

### Step 3: Assign edges = nx.minimum_spanning_edges(...)

```python
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False, ignore_nan=True)
```

### Step 4: Assign actual = sorted(...)

```python
actual = sorted(((min(u, v), max(u, v)) for u, v in edges))
```

### Step 5: Assign expected = value

```python
expected = [(u, v) for u, v, d in self.minimum_spanning_edgelist]
```

**Verification:**
```python
assert edges_equal(actual, expected)
```

### Step 6: Assign edges = nx.minimum_spanning_edges(...)

```python
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False, ignore_nan=False)
```

### Step 7: Assign edges = nx.minimum_spanning_edges(...)

```python
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False)
```

### Step 8: Call list()

```python
list(edges)
```

### Step 9: Call list()

```python
list(edges)
```


## Complete Example

```python
# Workflow
G = self.G
G.add_edge(0, 12, weight=float('nan'))
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False, ignore_nan=True)
actual = sorted(((min(u, v), max(u, v)) for u, v in edges))
expected = [(u, v) for u, v, d in self.minimum_spanning_edgelist]
assert edges_equal(actual, expected)
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False, ignore_nan=False)
with pytest.raises(ValueError):
    list(edges)
edges = nx.minimum_spanning_edges(G, algorithm=self.algo, data=False)
with pytest.raises(ValueError):
    list(edges)
```

## Next Steps


---

*Source: test_mst.py:90 | Complexity: Advanced | Last updated: 2026-06-02*