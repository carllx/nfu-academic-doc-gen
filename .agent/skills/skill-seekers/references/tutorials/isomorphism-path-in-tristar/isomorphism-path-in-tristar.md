# How To: Isomorphism Path In Tristar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isomorphism path in tristar

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign g1 = nx.path_graph(...)

```python
g1 = nx.path_graph(3)
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric)
```

### Step 2: Assign g2 = g1.copy(...)

```python
g2 = g1.copy()
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric + expected_asymmetric)
```

### Step 3: Call g2.add_edge()

```python
g2.add_edge(1, 3)
```

### Step 4: Assign ismags = iso.ISMAGS(...)

```python
ismags = iso.ISMAGS(g2, g1)
```

### Step 5: Assign matches = ismags.subgraph_isomorphisms_iter(...)

```python
matches = ismags.subgraph_isomorphisms_iter(symmetry=True)
```

### Step 6: Assign expected_symmetric = value

```python
expected_symmetric = [{0: 0, 1: 1, 2: 2}, {0: 0, 1: 1, 3: 2}, {2: 0, 1: 1, 3: 2}]
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric)
```

### Step 7: Assign matches = ismags.subgraph_isomorphisms_iter(...)

```python
matches = ismags.subgraph_isomorphisms_iter(symmetry=False)
```

### Step 8: Assign expected_asymmetric = value

```python
expected_asymmetric = [{0: 2, 1: 1, 2: 0}, {0: 2, 1: 1, 3: 0}, {2: 2, 1: 1, 3: 0}]
```

**Verification:**
```python
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric + expected_asymmetric)
```


## Complete Example

```python
# Workflow
g1 = nx.path_graph(3)
g2 = g1.copy()
g2.add_edge(1, 3)
ismags = iso.ISMAGS(g2, g1)
matches = ismags.subgraph_isomorphisms_iter(symmetry=True)
expected_symmetric = [{0: 0, 1: 1, 2: 2}, {0: 0, 1: 1, 3: 2}, {2: 0, 1: 1, 3: 2}]
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric)
matches = ismags.subgraph_isomorphisms_iter(symmetry=False)
expected_asymmetric = [{0: 2, 1: 1, 2: 0}, {0: 2, 1: 1, 3: 0}, {2: 2, 1: 1, 3: 0}]
assert _matches_to_sets(matches) == _matches_to_sets(expected_symmetric + expected_asymmetric)
```

## Next Steps


---

*Source: test_ismags.py:191 | Complexity: Advanced | Last updated: 2026-06-02*