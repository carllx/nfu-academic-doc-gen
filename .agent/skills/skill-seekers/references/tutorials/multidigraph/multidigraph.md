# How To: Multidigraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests the edge boundary of a multidigraph.

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests the edge boundary of a multidigraph.'

```python
'Tests the edge boundary of a multidigraph.'
```

**Verification:**
```python
assert boundary == expected
```

### Step 2: Assign edges = value

```python
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
```

### Step 3: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph(edges * 2)
```

### Step 4: Assign S = value

```python
S = {0, 1}
```

### Step 5: Assign boundary = list(...)

```python
boundary = list(nx.edge_boundary(G, S))
```

### Step 6: Assign expected = value

```python
expected = [(1, 2), (1, 2)]
```

**Verification:**
```python
assert boundary == expected
```


## Complete Example

```python
# Workflow
'Tests the edge boundary of a multidigraph.'
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
G = nx.MultiDiGraph(edges * 2)
S = {0, 1}
boundary = list(nx.edge_boundary(G, S))
expected = [(1, 2), (1, 2)]
assert boundary == expected
```

## Next Steps


---

*Source: test_boundary.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*