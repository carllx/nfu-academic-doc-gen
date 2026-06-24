# How To: Multigraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests the edge boundary of a multigraph.

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests the edge boundary of a multigraph.'

```python
'Tests the edge boundary of a multigraph.'
```

**Verification:**
```python
assert boundary == expected
```

### Step 2: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph(list(nx.cycle_graph(5).edges()) * 2)
```

### Step 3: Assign S = value

```python
S = {0, 1}
```

### Step 4: Assign boundary = list(...)

```python
boundary = list(nx.edge_boundary(G, S))
```

### Step 5: Assign expected = value

```python
expected = [(0, 4), (0, 4), (1, 2), (1, 2)]
```

**Verification:**
```python
assert boundary == expected
```


## Complete Example

```python
# Workflow
'Tests the edge boundary of a multigraph.'
G = nx.MultiGraph(list(nx.cycle_graph(5).edges()) * 2)
S = {0, 1}
boundary = list(nx.edge_boundary(G, S))
expected = [(0, 4), (0, 4), (1, 2), (1, 2)]
assert boundary == expected
```

## Next Steps


---

*Source: test_boundary.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*