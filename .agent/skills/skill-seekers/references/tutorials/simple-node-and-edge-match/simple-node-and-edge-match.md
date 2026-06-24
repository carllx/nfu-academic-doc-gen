# How To: Simple Node And Edge Match

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test simple node and edge match

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms`

**Setup Required:**
```python
# Fixtures: graph_class
```

## Step-by-Step Guide

### Step 1: Assign g1 = graph_class(...)

```python
g1 = graph_class()
```

**Verification:**
```python
assert is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 2: Call g1.add_weighted_edges_from()

```python
g1.add_weighted_edges_from([(0, 0, 1.2), (0, 1, 1.4), (1, 0, 1.6)])
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 3: Assign g2 = g1.copy(...)

```python
g2 = g1.copy()
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 4: Assign nm = iso.numerical_node_match(...)

```python
nm = iso.numerical_node_match('size', 1)
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 5: Assign unknown = 3

```python
g2.nodes[0]['size'] = 3
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 6: Assign g2 = g1.copy(...)

```python
g2 = g1.copy()
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 7: Assign g2 = g1.copy(...)

```python
g2 = g1.copy()
```

### Step 8: Assign unknown = 3

```python
g2.nodes[0]['size'] = 3
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

### Step 9: Assign em = iso.numerical_multiedge_match(...)

```python
em = iso.numerical_multiedge_match('weight', 1)
```

### Step 10: Assign em = iso.numerical_edge_match(...)

```python
em = iso.numerical_edge_match('weight', 1)
```

### Step 11: Assign unknown = 2.1

```python
g2.edges[0, 1, 0]['weight'] = 2.1
```

### Step 12: Assign unknown = 2.1

```python
g2.edges[0, 1]['weight'] = 2.1
```

### Step 13: Assign unknown = 2.1

```python
g2.edges[0, 1, 0]['weight'] = 2.1
```

### Step 14: Assign unknown = 2.1

```python
g2.edges[0, 1]['weight'] = 2.1
```


## Complete Example

```python
# Setup
# Fixtures: graph_class

# Workflow
g1 = graph_class()
g1.add_weighted_edges_from([(0, 0, 1.2), (0, 1, 1.4), (1, 0, 1.6)])
g2 = g1.copy()
nm = iso.numerical_node_match('size', 1)
if g1.is_multigraph():
    em = iso.numerical_multiedge_match('weight', 1)
else:
    em = iso.numerical_edge_match('weight', 1)
assert is_isomorphic(g1, g2, node_match=nm, edge_match=em)
g2.nodes[0]['size'] = 3
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
g2 = g1.copy()
if g1.is_multigraph():
    g2.edges[0, 1, 0]['weight'] = 2.1
else:
    g2.edges[0, 1]['weight'] = 2.1
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
g2 = g1.copy()
g2.nodes[0]['size'] = 3
if g1.is_multigraph():
    g2.edges[0, 1, 0]['weight'] = 2.1
else:
    g2.edges[0, 1]['weight'] = 2.1
assert not is_isomorphic(g1, g2, node_match=nm, edge_match=em)
```

## Next Steps


---

*Source: test_ismags.py:623 | Complexity: Advanced | Last updated: 2026-06-02*