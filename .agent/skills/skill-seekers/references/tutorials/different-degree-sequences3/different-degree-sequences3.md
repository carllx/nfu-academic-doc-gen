# How To: Different Degree Sequences3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test different degree sequences3

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
```

**Verification:**
```python
assert not vf2pp_is_isomorphic(G1, G2)
```

### Step 2: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph([(0, 1), (0, 6), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
```

**Verification:**
```python
assert vf2pp_is_isomorphic(G1, G2)
```

### Step 3: Call G1.add_edge()

```python
G1.add_edge(3, 5)
```

### Step 4: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(['a']))), 'label')
```

### Step 5: Call nx.set_node_attributes()

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
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
G2 = nx.Graph([(0, 1), (0, 6), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
assert not vf2pp_is_isomorphic(G1, G2)
G1.add_edge(3, 5)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(['a']))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle('a'))), 'label')
assert vf2pp_is_isomorphic(G1, G2)
```

## Next Steps


---

*Source: test_vf2pp.py:92 | Complexity: Intermediate | Last updated: 2026-06-02*