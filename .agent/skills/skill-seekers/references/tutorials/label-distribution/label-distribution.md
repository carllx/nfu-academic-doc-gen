# How To: Label Distribution

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test label distribution

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
assert not vf2pp_is_isomorphic(G1, G2, node_label='label')
```

### Step 2: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
```

**Verification:**
```python
assert vf2pp_is_isomorphic(G1, G2, node_label='label')
```

### Step 3: Assign colors1 = value

```python
colors1 = ['blue', 'blue', 'blue', 'yellow', 'black', 'purple', 'purple']
```

### Step 4: Assign colors2 = value

```python
colors2 = ['blue', 'blue', 'yellow', 'yellow', 'black', 'purple', 'purple']
```

### Step 5: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(colors1[::-1]))), 'label')
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(colors2[::-1]))), 'label')
```

**Verification:**
```python
assert not vf2pp_is_isomorphic(G1, G2, node_label='label')
```

### Step 7: Assign unknown = 'blue'

```python
G2.nodes[3]['label'] = 'blue'
```

**Verification:**
```python
assert vf2pp_is_isomorphic(G1, G2, node_label='label')
```


## Complete Example

```python
# Workflow
G1 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
G2 = nx.Graph([(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (2, 5), (2, 6)])
colors1 = ['blue', 'blue', 'blue', 'yellow', 'black', 'purple', 'purple']
colors2 = ['blue', 'blue', 'yellow', 'yellow', 'black', 'purple', 'purple']
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(colors1[::-1]))), 'label')
nx.set_node_attributes(G2, dict(zip(G2, it.cycle(colors2[::-1]))), 'label')
assert not vf2pp_is_isomorphic(G1, G2, node_label='label')
G2.nodes[3]['label'] = 'blue'
assert vf2pp_is_isomorphic(G1, G2, node_label='label')
```

## Next Steps


---

*Source: test_vf2pp.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*