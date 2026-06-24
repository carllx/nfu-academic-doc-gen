# How To: This One Specific Tree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test the tree pictured at the bottom of [West01]_, p. 78.

## Prerequisites

**Required Modules:**
- `itertools`
- `math`
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.distance_measures`


## Step-by-Step Guide

### Step 1: 'Test the tree pictured at the bottom of [West01]_, p. 78.'

```python
'Test the tree pictured at the bottom of [West01]_, p. 78.'
```

**Verification:**
```python
assert list(b) == ['z']
```

### Step 2: Assign g = nx.Graph(...)

```python
g = nx.Graph({'a': ['b'], 'b': ['a', 'x'], 'x': ['b', 'y'], 'y': ['x', 'z'], 'z': ['y', 0, 1, 2, 3, 4], 0: ['z'], 1: ['z'], 2: ['z'], 3: ['z'], 4: ['z']})
```

**Verification:**
```python
assert not b.edges
```

### Step 3: Assign b = self.barycenter_as_subgraph(...)

```python
b = self.barycenter_as_subgraph(g, attr='barycentricity')
```

**Verification:**
```python
assert g.nodes[node]['barycentricity'] == barycentricity
```

### Step 4: Assign expected_barycentricity = value

```python
expected_barycentricity = {0: 23, 1: 23, 2: 23, 3: 23, 4: 23, 'a': 35, 'b': 27, 'x': 21, 'y': 17, 'z': 15}
```

**Verification:**
```python
assert list(b) == ['z']
```

### Step 5: Assign b = self.barycenter_as_subgraph(...)

```python
b = self.barycenter_as_subgraph(g, weight='weight', attr='barycentricity2')
```

**Verification:**
```python
assert not b.edges
```

### Step 6: Assign unknown = 2

```python
g.edges[edge]['weight'] = 2
```

**Verification:**
```python
assert g.nodes[node]['barycentricity2'] == barycentricity * 2
```


## Complete Example

```python
# Workflow
'Test the tree pictured at the bottom of [West01]_, p. 78.'
g = nx.Graph({'a': ['b'], 'b': ['a', 'x'], 'x': ['b', 'y'], 'y': ['x', 'z'], 'z': ['y', 0, 1, 2, 3, 4], 0: ['z'], 1: ['z'], 2: ['z'], 3: ['z'], 4: ['z']})
b = self.barycenter_as_subgraph(g, attr='barycentricity')
assert list(b) == ['z']
assert not b.edges
expected_barycentricity = {0: 23, 1: 23, 2: 23, 3: 23, 4: 23, 'a': 35, 'b': 27, 'x': 21, 'y': 17, 'z': 15}
for node, barycentricity in expected_barycentricity.items():
    assert g.nodes[node]['barycentricity'] == barycentricity
for edge in g.edges:
    g.edges[edge]['weight'] = 2
b = self.barycenter_as_subgraph(g, weight='weight', attr='barycentricity2')
assert list(b) == ['z']
assert not b.edges
for node, barycentricity in expected_barycentricity.items():
    assert g.nodes[node]['barycentricity2'] == barycentricity * 2
```

## Next Steps


---

*Source: test_distance_measures.py:631 | Complexity: Intermediate | Last updated: 2026-06-02*