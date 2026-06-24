# How To: Different Degree Sequences2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test different degree sequences2

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([(0, 1), (1, 2), (0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 3), (4, 7), (7, 8), (8, 3)])
```

**Verification:**
```python
assert not vf2pp_is_isomorphic(G1, G2)
```

### Step 2: Assign G2 = G1.copy(...)

```python
G2 = G1.copy()
```

**Verification:**
```python
assert vf2pp_is_isomorphic(G1, G2)
```

### Step 3: Call G2.add_edge()

```python
G2.add_edge(8, 0)
```

**Verification:**
```python
assert not vf2pp_is_isomorphic(G1, G2)
```

### Step 4: Call G1.add_edge()

```python
G1.add_edge(6, 1)
```

### Step 5: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(['a']))), 'label')
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle('a'))), 'label')
```

**Verification:**
```python
assert vf2pp_is_isomorphic(G1, G2)
```


## Complete Example

```python
# Workflow
G1 = nx.Graph([(0, 1), (1, 2), (0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 3), (4, 7), (7, 8), (8, 3)])
G2 = G1.copy()
G2.add_edge(8, 0)
assert not vf2pp_is_isomorphic(G1, G2)
G1.add_edge(6, 1)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(['a']))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle('a'))), 'label')
assert vf2pp_is_isomorphic(G1, G2)
```

## Next Steps


---

*Source: test_vf2pp.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*