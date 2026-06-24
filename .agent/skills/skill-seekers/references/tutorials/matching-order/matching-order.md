# How To: Matching Order

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matching order

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.isomorphism.vf2pp`


## Step-by-Step Guide

### Step 1: Assign labels = value

```python
labels = ['blue', 'blue', 'red', 'red', 'red', 'red', 'green', 'green', 'green', 'yellow', 'purple', 'purple', 'blue', 'blue']
```

**Verification:**
```python
assert _matching_order(gparams) == expected
```

### Step 2: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 5), (2, 4), (1, 3), (1, 4), (3, 6), (4, 6), (6, 7), (7, 8), (9, 10), (9, 11), (11, 12), (11, 13), (12, 13), (10, 13)])
```

### Step 3: Assign G2 = G1.copy(...)

```python
G2 = G1.copy()
```

### Step 4: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels))), 'label')
```

### Step 5: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels))), 'label')
```

### Step 6: Assign unknown = value

```python
l1, l2 = (nx.get_node_attributes(G1, 'label'), nx.get_node_attributes(G2, 'label'))
```

### Step 7: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
```

### Step 8: Assign expected = value

```python
expected = [9, 11, 10, 13, 12, 1, 2, 4, 0, 3, 6, 5, 7, 8]
```

**Verification:**
```python
assert _matching_order(gparams) == expected
```


## Complete Example

```python
# Workflow
labels = ['blue', 'blue', 'red', 'red', 'red', 'red', 'green', 'green', 'green', 'yellow', 'purple', 'purple', 'blue', 'blue']
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 5), (2, 4), (1, 3), (1, 4), (3, 6), (4, 6), (6, 7), (7, 8), (9, 10), (9, 11), (11, 12), (11, 13), (12, 13), (10, 13)])
G2 = G1.copy()
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(labels))), 'label')
l1, l2 = (nx.get_node_attributes(G1, 'label'), nx.get_node_attributes(G2, 'label'))
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
expected = [9, 11, 10, 13, 12, 1, 2, 4, 0, 3, 6, 5, 7, 8]
assert _matching_order(gparams) == expected
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:77 | Complexity: Advanced | Last updated: 2026-06-02*