# How To: All Triads

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests the all_triads function.

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Tests the all_triads function.'

```python
'Tests the all_triads function.'
```

**Verification:**
```python
assert all((any((nx.is_isomorphic(G1, G2) for G1 in expected)) for G2 in actual))
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(['01', '02', '03', '04', '05', '12', '16', '51', '56', '65'])
```

### Step 4: Assign expected = value

```python
expected = [f'{i},{j},{k}' for i in range(7) for j in range(i + 1, 7) for k in range(j + 1, 7)]
```

### Step 5: Assign expected = value

```python
expected = [G.subgraph(x.split(',')) for x in expected]
```

### Step 6: Assign actual = list(...)

```python
actual = list(nx.all_triads(G))
```

**Verification:**
```python
assert all((any((nx.is_isomorphic(G1, G2) for G1 in expected)) for G2 in actual))
```


## Complete Example

```python
# Workflow
'Tests the all_triads function.'
G = nx.DiGraph()
G.add_edges_from(['01', '02', '03', '04', '05', '12', '16', '51', '56', '65'])
expected = [f'{i},{j},{k}' for i in range(7) for j in range(i + 1, 7) for k in range(j + 1, 7)]
expected = [G.subgraph(x.split(',')) for x in expected]
actual = list(nx.all_triads(G))
assert all((any((nx.is_isomorphic(G1, G2) for G1 in expected)) for G2 in actual))
```

## Next Steps


---

*Source: test_triads.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*