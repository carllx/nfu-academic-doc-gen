# How To: Selfloop Mono

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test selfloop mono

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

### Step 1: Assign edges0 = value

```python
edges0 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 1), (3, 2), (4, 2), (4, 5), (5, 4)]
```

**Verification:**
```python
assert not gm.subgraph_is_monomorphic()
```

### Step 2: Assign edges = value

```python
edges = edges0 + [(2, 2)]
```

### Step 3: Assign nodes = list(...)

```python
nodes = list(range(6))
```

### Step 4: Assign rng = random.Random(...)

```python
rng = random.Random(42)
```

### Step 5: Call g1.add_edges_from()

```python
g1.add_edges_from(edges)
```

### Step 6: Assign new_nodes = list(...)

```python
new_nodes = list(nodes)
```

### Step 7: Call rng.shuffle()

```python
rng.shuffle(new_nodes)
```

### Step 8: Assign d = dict(...)

```python
d = dict(zip(nodes, new_nodes))
```

### Step 9: Assign g2 = nx.relabel_nodes(...)

```python
g2 = nx.relabel_nodes(g1, d)
```

### Step 10: Call g2.remove_edges_from()

```python
g2.remove_edges_from(nx.selfloop_edges(g2))
```

**Verification:**
```python
assert not gm.subgraph_is_monomorphic()
```

### Step 11: Assign gm = iso.GraphMatcher(...)

```python
gm = iso.GraphMatcher(g2, g1)
```

### Step 12: Assign gm = iso.DiGraphMatcher(...)

```python
gm = iso.DiGraphMatcher(g2, g1)
```


## Complete Example

```python
# Workflow
edges0 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 1), (3, 2), (4, 2), (4, 5), (5, 4)]
edges = edges0 + [(2, 2)]
nodes = list(range(6))
rng = random.Random(42)
for g1 in [nx.Graph(), nx.DiGraph()]:
    g1.add_edges_from(edges)
    for _ in range(100):
        new_nodes = list(nodes)
        rng.shuffle(new_nodes)
        d = dict(zip(nodes, new_nodes))
        g2 = nx.relabel_nodes(g1, d)
        g2.remove_edges_from(nx.selfloop_edges(g2))
        if not g1.is_directed():
            gm = iso.GraphMatcher(g2, g1)
        else:
            gm = iso.DiGraphMatcher(g2, g1)
        assert not gm.subgraph_is_monomorphic()
```

## Next Steps


---

*Source: test_isomorphvf2.py:308 | Complexity: Advanced | Last updated: 2026-06-02*