# How To: Different Degree Sequences1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test different degree sequences1

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (0, 4)])
```

**Verification:**
```python
assert not vf2pp_is_isomorphic(G1, G2)
```

### Step 2: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (0, 4), (2, 5)])
```

**Verification:**
```python
assert vf2pp_is_isomorphic(G1, G2)
```

### Step 3: Call G2.remove_node()

```python
G2.remove_node(3)
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
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (0, 4)])
G2 = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (0, 4), (2, 5)])
assert not vf2pp_is_isomorphic(G1, G2)
G2.remove_node(3)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(['a']))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle('a'))), 'label')
assert vf2pp_is_isomorphic(G1, G2)
```

## Next Steps


---

*Source: test_vf2pp.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*