# How To: Labeled Nodes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test labeled nodes

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign g1 = nx.cycle_graph(...)

```python
g1 = nx.cycle_graph(3)
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric)
```

### Step 2: Assign unknown = True

```python
g1.nodes[1]['attr'] = True
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric + expected_asymmetric)
```

### Step 3: Assign g2 = g1.copy(...)

```python
g2 = g1.copy()
```

### Step 4: Call g2.add_edge()

```python
g2.add_edge(1, 3)
```

### Step 5: Assign ismags = iso.ISMAGS(...)

```python
ismags = iso.ISMAGS(g2, g1, node_match=lambda x, y: x == y)
```

### Step 6: Assign matches = ismags.subgraph_isomorphisms_iter(...)

```python
matches = ismags.subgraph_isomorphisms_iter(symmetry=True)
```

### Step 7: Assign expected_symmetric = value

```python
expected_symmetric = [{0: 0, 1: 1, 2: 2}]
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric)
```

### Step 8: Assign matches = ismags.subgraph_isomorphisms_iter(...)

```python
matches = ismags.subgraph_isomorphisms_iter(symmetry=False)
```

### Step 9: Assign expected_asymmetric = value

```python
expected_asymmetric = [{0: 2, 1: 1, 2: 0}]
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric + expected_asymmetric)
```


## Complete Example

```python
# Workflow
g1 = nx.cycle_graph(3)
g1.nodes[1]['attr'] = True
g2 = g1.copy()
g2.add_edge(1, 3)
ismags = iso.ISMAGS(g2, g1, node_match=lambda x, y: x == y)
matches = ismags.subgraph_isomorphisms_iter(symmetry=True)
expected_symmetric = [{0: 0, 1: 1, 2: 2}]
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric)
matches = ismags.subgraph_isomorphisms_iter(symmetry=False)
expected_asymmetric = [{0: 2, 1: 1, 2: 0}]
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric + expected_asymmetric)
```

## Next Steps


---

*Source: test_ismags.py:216 | Complexity: Advanced | Last updated: 2026-06-02*