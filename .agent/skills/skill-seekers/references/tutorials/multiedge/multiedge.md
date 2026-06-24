# How To: Multiedge

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiedge

## Prerequisites

**Required Modules:**
- `importlib.resources`
- `random`
- `struct`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (10, 11), (11, 12), (11, 12), (12, 13), (12, 13), (13, 14), (13, 14), (14, 15), (14, 15), (15, 16), (15, 16), (16, 17), (16, 17), (17, 18), (17, 18), (18, 19), (18, 19), (19, 0), (19, 0)]
```

**Verification:**
```python
assert gm.is_isomorphic()
```

### Step 2: Assign nodes = list(...)

```python
nodes = list(range(20))
```

**Verification:**
```python
assert gm.subgraph_is_monomorphic()
```

### Step 3: Assign rng = random.Random(...)

```python
rng = random.Random(42)
```

### Step 4: Call g1.add_edges_from()

```python
g1.add_edges_from(edges)
```

### Step 5: Assign new_nodes = list(...)

```python
new_nodes = list(nodes)
```

### Step 6: Call rng.shuffle()

```python
rng.shuffle(new_nodes)
```

### Step 7: Assign d = dict(...)

```python
d = dict(zip(nodes, new_nodes))
```

### Step 8: Assign g2 = nx.relabel_nodes(...)

```python
g2 = nx.relabel_nodes(g1, d)
```

**Verification:**
```python
assert gm.is_isomorphic()
```

### Step 9: Assign gm = iso.GraphMatcher(...)

```python
gm = iso.GraphMatcher(g1, g2)
```

### Step 10: Assign gm = iso.DiGraphMatcher(...)

```python
gm = iso.DiGraphMatcher(g1, g2)
```


## Complete Example

```python
# Workflow
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (10, 11), (11, 12), (11, 12), (12, 13), (12, 13), (13, 14), (13, 14), (14, 15), (14, 15), (15, 16), (15, 16), (16, 17), (16, 17), (17, 18), (17, 18), (18, 19), (18, 19), (19, 0), (19, 0)]
nodes = list(range(20))
rng = random.Random(42)
for g1 in [nx.MultiGraph(), nx.MultiDiGraph()]:
    g1.add_edges_from(edges)
    for _ in range(10):
        new_nodes = list(nodes)
        rng.shuffle(new_nodes)
        d = dict(zip(nodes, new_nodes))
        g2 = nx.relabel_nodes(g1, d)
        if not g1.is_directed():
            gm = iso.GraphMatcher(g1, g2)
        else:
            gm = iso.DiGraphMatcher(g1, g2)
        assert gm.is_isomorphic()
        assert gm.subgraph_is_monomorphic()
```

## Next Steps


---

*Source: test_isomorphvf2.py:192 | Complexity: Advanced | Last updated: 2026-06-02*