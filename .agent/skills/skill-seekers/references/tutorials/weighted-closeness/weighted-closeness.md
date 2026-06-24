# How To: Weighted Closeness

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weighted closeness

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [('s', 'u', 10), ('s', 'x', 5), ('u', 'v', 1), ('u', 'x', 2), ('v', 'y', 1), ('x', 'u', 3), ('x', 'v', 5), ('x', 'y', 2), ('y', 's', 7), ('y', 'v', 6)]
```

**Verification:**
```python
assert c[n] == pytest.approx(d[n], abs=0.001)
```

### Step 2: Assign XG = nx.Graph(...)

```python
XG = nx.Graph()
```

### Step 3: Call XG.add_weighted_edges_from()

```python
XG.add_weighted_edges_from(edges)
```

### Step 4: Assign c = nx.closeness_centrality(...)

```python
c = nx.closeness_centrality(XG, distance='weight')
```

### Step 5: Assign d = value

```python
d = {'y': 0.2, 'x': 0.286, 's': 0.138, 'u': 0.235, 'v': 0.2}
```

**Verification:**
```python
assert c[n] == pytest.approx(d[n], abs=0.001)
```


## Complete Example

```python
# Workflow
edges = [('s', 'u', 10), ('s', 'x', 5), ('u', 'v', 1), ('u', 'x', 2), ('v', 'y', 1), ('x', 'u', 3), ('x', 'v', 5), ('x', 'y', 2), ('y', 's', 7), ('y', 'v', 6)]
XG = nx.Graph()
XG.add_weighted_edges_from(edges)
c = nx.closeness_centrality(XG, distance='weight')
d = {'y': 0.2, 'x': 0.286, 's': 0.138, 'u': 0.235, 'v': 0.2}
for n in sorted(XG):
    assert c[n] == pytest.approx(d[n], abs=0.001)
```

## Next Steps


---

*Source: test_closeness_centrality.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*