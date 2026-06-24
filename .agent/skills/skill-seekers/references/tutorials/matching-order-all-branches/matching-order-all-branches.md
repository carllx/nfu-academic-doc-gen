# How To: Matching Order All Branches

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matching order all branches

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.isomorphism.vf2pp`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)])
```

**Verification:**
```python
assert _matching_order(gparams) == expected
```

### Step 2: Call G1.add_node()

```python
G1.add_node(5)
```

### Step 3: Assign G2 = G1.copy(...)

```python
G2 = G1.copy()
```

### Step 4: Assign unknown = 'black'

```python
G1.nodes[0]['label'] = 'black'
```

### Step 5: Assign unknown = 'blue'

```python
G1.nodes[1]['label'] = 'blue'
```

### Step 6: Assign unknown = 'blue'

```python
G1.nodes[2]['label'] = 'blue'
```

### Step 7: Assign unknown = 'red'

```python
G1.nodes[3]['label'] = 'red'
```

### Step 8: Assign unknown = 'red'

```python
G1.nodes[4]['label'] = 'red'
```

### Step 9: Assign unknown = 'blue'

```python
G1.nodes[5]['label'] = 'blue'
```

### Step 10: Assign unknown = 'black'

```python
G2.nodes[0]['label'] = 'black'
```

### Step 11: Assign unknown = 'blue'

```python
G2.nodes[1]['label'] = 'blue'
```

### Step 12: Assign unknown = 'blue'

```python
G2.nodes[2]['label'] = 'blue'
```

### Step 13: Assign unknown = 'red'

```python
G2.nodes[3]['label'] = 'red'
```

### Step 14: Assign unknown = 'red'

```python
G2.nodes[4]['label'] = 'red'
```

### Step 15: Assign unknown = 'blue'

```python
G2.nodes[5]['label'] = 'blue'
```

### Step 16: Assign unknown = value

```python
l1, l2 = (nx.get_node_attributes(G1, 'label'), nx.get_node_attributes(G2, 'label'))
```

### Step 17: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
```

### Step 18: Assign expected = value

```python
expected = [0, 4, 1, 3, 2, 5]
```

**Verification:**
```python
assert _matching_order(gparams) == expected
```


## Complete Example

```python
# Workflow
G1 = nx.Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)])
G1.add_node(5)
G2 = G1.copy()
G1.nodes[0]['label'] = 'black'
G1.nodes[1]['label'] = 'blue'
G1.nodes[2]['label'] = 'blue'
G1.nodes[3]['label'] = 'red'
G1.nodes[4]['label'] = 'red'
G1.nodes[5]['label'] = 'blue'
G2.nodes[0]['label'] = 'black'
G2.nodes[1]['label'] = 'blue'
G2.nodes[2]['label'] = 'blue'
G2.nodes[3]['label'] = 'red'
G2.nodes[4]['label'] = 'red'
G2.nodes[5]['label'] = 'blue'
l1, l2 = (nx.get_node_attributes(G1, 'label'), nx.get_node_attributes(G2, 'label'))
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
expected = [0, 4, 1, 3, 2, 5]
assert _matching_order(gparams) == expected
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:139 | Complexity: Advanced | Last updated: 2026-06-02*